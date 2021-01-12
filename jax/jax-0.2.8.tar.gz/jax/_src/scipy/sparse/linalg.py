# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from functools import partial
import operator

import numpy as np
import jax.numpy as jnp
from jax import scipy as jsp
from jax import lax, device_put
from jax.tree_util import (tree_leaves, tree_map, tree_multimap, tree_structure,
                           tree_reduce, Partial)
from jax._src.util import safe_map as map


_dot = partial(jnp.dot, precision=lax.Precision.HIGHEST)
_vdot = partial(jnp.vdot, precision=lax.Precision.HIGHEST)
_einsum = partial(jnp.einsum, precision=lax.Precision.HIGHEST)


# aliases for working with pytrees
def _vdot_real_part(x, y):
  """Vector dot-product guaranteed to have a real valued result despite
     possibly complex input. Thus neglects the real-imaginary cross-terms.
     The result is a real float.
  """
  # all our uses of vdot() in CG are for computing an operator of the form
  #  z^H M z
  #  where M is positive definite and Hermitian, so the result is
  # real valued:
  # https://en.wikipedia.org/wiki/Definiteness_of_a_matrix#Definitions_for_complex_matrices
  result = _vdot(x.real, y.real)
  if jnp.iscomplexobj(x) or jnp.iscomplexobj(y):
    result += _vdot(x.imag, y.imag)
  return result


def _vdot_real_tree(x, y):
  return sum(tree_leaves(tree_multimap(_vdot_real_part, x, y)))


def _norm(x):
  xs = tree_leaves(x)
  return jnp.sqrt(sum(map(_vdot_real_part, xs, xs)))


def _mul(scalar, tree):
  return tree_map(partial(operator.mul, scalar), tree)


def _div(tree, scalar):
  return tree_map(partial(lambda v: v / scalar), tree)


_add = partial(tree_multimap, operator.add)
_sub = partial(tree_multimap, operator.sub)
_dot_tree = partial(tree_multimap, _dot)


@Partial
def _identity(x):
  return x


def _normalize_matvec(f):
  """Normalize an argument for computing matrix-vector products."""
  if callable(f):
    return f
  elif isinstance(f, (np.ndarray, jnp.ndarray)):
    if f.ndim != 2 or f.shape[0] != f.shape[1]:
      raise ValueError(
          f'linear operator must be a square matrix, but has shape: {f.shape}')
    return partial(_dot, f)
  else:
    # TODO(shoyer): handle sparse arrays?
    raise TypeError(
        f'linear operator must be either a function or ndarray: {f}')


def _cg_solve(A, b, x0=None, *, maxiter, tol=1e-5, atol=0.0, M=_identity):

  # tolerance handling uses the "non-legacy" behavior of scipy.sparse.linalg.cg
  bs = _vdot_real_tree(b, b)
  atol2 = jnp.maximum(jnp.square(tol) * bs, jnp.square(atol))

  # https://en.wikipedia.org/wiki/Conjugate_gradient_method#The_preconditioned_conjugate_gradient_method

  def cond_fun(value):
    _, r, gamma, _, k = value
    rs = gamma if M is _identity else _vdot_real_tree(r, r)
    return (rs > atol2) & (k < maxiter)

  def body_fun(value):
    x, r, gamma, p, k = value
    Ap = A(p)
    alpha = gamma / _vdot_real_tree(p, Ap)
    x_ = _add(x, _mul(alpha, p))
    r_ = _sub(r, _mul(alpha, Ap))
    z_ = M(r_)
    gamma_ = _vdot_real_tree(r_, z_)
    beta_ = gamma_ / gamma
    p_ = _add(z_, _mul(beta_, p))
    return x_, r_, gamma_, p_, k + 1

  r0 = _sub(b, A(x0))
  p0 = z0 = M(r0)
  gamma0 = _vdot_real_tree(r0, z0)
  initial_value = (x0, r0, gamma0, p0, 0)

  x_final, *_ = lax.while_loop(cond_fun, body_fun, initial_value)

  return x_final


def _shapes(pytree):
  return map(jnp.shape, tree_leaves(pytree))


def cg(A, b, x0=None, *, tol=1e-5, atol=0.0, maxiter=None, M=None):
  """Use Conjugate Gradient iteration to solve ``Ax = b``.

  The numerics of JAX's ``cg`` should exact match SciPy's ``cg`` (up to
  numerical precision), but note that the interface is slightly different: you
  need to supply the linear operator ``A`` as a function instead of a sparse
  matrix or ``LinearOperator``.

  Derivatives of ``cg`` are implemented via implicit differentiation with
  another ``cg`` solve, rather than by differentiating *through* the solver.
  They will be accurate only if both solves converge.

  Parameters
  ----------
  A: ndarray or function
      2D array or function that calculates the linear map (matrix-vector
      product) ``Ax`` when called like ``A(x)``. ``A`` must represent a
      hermitian, positive definite matrix, and must return array(s) with the
      same structure and shape as its argument.
  b : array or tree of arrays
      Right hand side of the linear system representing a single vector. Can be
      stored as an array or Python container of array(s) with any shape.

  Returns
  -------
  x : array or tree of arrays
      The converged solution. Has the same structure as ``b``.
  info : None
      Placeholder for convergence information. In the future, JAX will report
      the number of iterations when convergence is not achieved, like SciPy.

  Other Parameters
  ----------------
  x0 : array
      Starting guess for the solution. Must have the same structure as ``b``.
  tol, atol : float, optional
      Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
      We do not implement SciPy's "legacy" behavior, so JAX's tolerance will
      differ from SciPy unless you explicitly pass ``atol`` to SciPy's ``cg``.
  maxiter : integer
      Maximum number of iterations.  Iteration will stop after maxiter
      steps even if the specified tolerance has not been achieved.
  M : ndarray or function
      Preconditioner for A.  The preconditioner should approximate the
      inverse of A.  Effective preconditioning dramatically improves the
      rate of convergence, which implies that fewer iterations are needed
      to reach a given error tolerance.

  See also
  --------
  scipy.sparse.linalg.cg
  jax.lax.custom_linear_solve
  """
  if x0 is None:
    x0 = tree_map(jnp.zeros_like, b)

  b, x0 = device_put((b, x0))

  if maxiter is None:
    size = sum(bi.size for bi in tree_leaves(b))
    maxiter = 10 * size  # copied from scipy

  if M is None:
    M = _identity
  A = _normalize_matvec(A)
  M = _normalize_matvec(M)

  if tree_structure(x0) != tree_structure(b):
    raise ValueError(
        'x0 and b must have matching tree structure: '
        f'{tree_structure(x0)} vs {tree_structure(b)}')

  if _shapes(x0) != _shapes(b):
    raise ValueError(
        'arrays in x0 and b must have matching shapes: '
        f'{_shapes(x0)} vs {_shapes(b)}')

  cg_solve = partial(
      _cg_solve, x0=x0, tol=tol, atol=atol, maxiter=maxiter, M=M)

  # real-valued positive-definite linear operators are symmetric
  def real_valued(x):
    return not issubclass(x.dtype.type, np.complexfloating)
  symmetric = all(map(real_valued, tree_leaves(b)))
  x = lax.custom_linear_solve(
      A, b, solve=cg_solve, transpose_solve=cg_solve, symmetric=symmetric)
  info = None  # TODO(shoyer): return the real iteration count here
  return x, info


def _safe_normalize(x, thresh=None):
  """
  Returns the L2-normalized vector (which can be a pytree) x, and optionally
  the computed norm. If the computed norm is less than the threshold `thresh`,
  which by default is the machine precision of x's dtype, it will be
  taken to be 0, and the normalized x to be the zero vector.
  """
  norm = _norm(x)
  dtype = jnp.result_type(*tree_leaves(x))
  if thresh is None:
    thresh = jnp.finfo(norm.dtype).eps
  thresh = thresh.astype(dtype).real

  use_norm = norm > thresh
  normalized_x = tree_map(lambda y: jnp.where(use_norm, y / norm, 0.0), x)
  norm = jnp.where(use_norm, norm, 0.0)
  return normalized_x, norm


def _project_on_columns(A, v):
  """
  Returns A.T.conj() @ v.
  """
  v_proj = tree_multimap(
      lambda X, y: _einsum("...n,...->n", X.conj(), y), A, v,
  )
  return tree_reduce(operator.add, v_proj)


def _iterative_classical_gram_schmidt(Q, x, xnorm, max_iterations=2):
  """
  Orthogonalize x against the columns of Q. The process is repeated
  up to `max_iterations` times, or fewer if the condition
  ||r|| < (1/sqrt(2)) ||x|| is met earlier (see below for the meaning
  of r and x).

  Parameters
  ----------
  Q : array or tree of arrays
      A matrix of orthonormal columns.
  x : array or tree of arrays
      A vector. It will be replaced with a new vector q which is orthonormal
      to the columns of Q, such that x in span(col(Q), q).
  xnorm : float
      Norm of x.

  Returns
  -------
  q : array or tree of arrays
      A unit vector, orthonormal to each column of Q, such that
      x in span(col(Q), q).
  r : array
      Stores the overlaps of x with each vector in Q.
  """
  # "twice is enough"
  # http://slepc.upv.es/documentation/reports/str1.pdf

  # TODO(shoyer): consider switching to only one iteration, like SciPy?

  # This assumes that Q's leaves all have the same dimension in the last
  # axis.
  r = jnp.zeros((tree_leaves(Q)[0].shape[-1]))
  q = x
  xnorm_scaled = xnorm / jnp.sqrt(2)

  def body_function(carry):
    k, q, r, qnorm_scaled = carry
    h = _project_on_columns(Q, q)
    Qh = tree_map(lambda X: _dot(X, h), Q)
    q = _sub(q, Qh)
    r = _add(r, h)

    def qnorm_cond(carry):
      k, not_done, _, _ = carry
      return jnp.logical_and(not_done, k < (max_iterations - 1))

    def qnorm(carry):
      k, _, q, qnorm_scaled = carry
      _, qnorm = _safe_normalize(q)
      qnorm_scaled = qnorm / jnp.sqrt(2)
      return (k, False, q, qnorm_scaled)

    init = (k, True, q, qnorm_scaled)
    _, _, q, qnorm_scaled = lax.while_loop(qnorm_cond, qnorm, init)
    return (k + 1, q, r, qnorm_scaled)

  def cond_function(carry):
    k, _, r, qnorm_scaled = carry
    _, rnorm = _safe_normalize(r)
    return jnp.logical_and(k < (max_iterations - 1), rnorm < qnorm_scaled)

  k, q, r, qnorm_scaled = body_function((0, q, r, xnorm_scaled))
  k, q, r, _ = lax.while_loop(cond_function, body_function,
                              (k, q, r, qnorm_scaled))
  return q, r


def _kth_arnoldi_iteration(k, A, M, V, H):
  """
  Performs a single (the k'th) step of the Arnoldi process. Thus,
  adds a new orthonormalized Krylov vector A(M(V[:, k])) to V[:, k+1],
  and that vectors overlaps with the existing Krylov vectors to
  H[k, :]. The tolerance 'tol' sets the threshold at which an invariant
  subspace is declared to have been found, in which case in which case the new
  vector is taken to be the zero vector.
  """
  eps = jnp.finfo(jnp.result_type(*tree_leaves(V))).eps

  v = tree_map(lambda x: x[..., k], V)  # Gets V[:, k]
  v = M(A(v))
  _, v_norm_0 = _safe_normalize(v)
  v, h = _iterative_classical_gram_schmidt(V, v, v_norm_0, max_iterations=2)

  tol = eps * v_norm_0
  unit_v, v_norm_1 = _safe_normalize(v, thresh=tol)
  V = tree_multimap(lambda X, y: X.at[..., k + 1].set(y), V, unit_v)

  h = h.at[k + 1].set(v_norm_1)
  H = H.at[k, :].set(h)
  breakdown = v_norm_1 == 0.
  return V, H, breakdown


def _rotate_vectors(H, i, cs, sn):
  x1 = H[i]
  y1 = H[i + 1]
  x2 = cs.conj() * x1 - sn.conj() * y1
  y2 = sn * x1 + cs * y1
  H = H.at[i].set(x2)
  H = H.at[i + 1].set(y2)
  return H


def _givens_rotation(a, b):
  b_zero = abs(b) == 0
  a_lt_b = abs(a) < abs(b)
  t = -jnp.where(a_lt_b, a, b) / jnp.where(a_lt_b, b, a)
  r = lax.rsqrt(1 + abs(t) ** 2)
  cs = jnp.where(b_zero, 1, jnp.where(a_lt_b, r * t, r))
  sn = jnp.where(b_zero, 0, jnp.where(a_lt_b, r, r * t))
  return cs, sn


def _apply_givens_rotations(H_row, givens, k):
  """
  Applies the Givens rotations stored in the vectors cs and sn to the vector
  H_row. Then constructs and applies a new Givens rotation that eliminates
  H_row's k'th element.
  """
  # This call successively applies each of the
  # Givens rotations stored in givens[:, :k] to H_col.

  def apply_ith_rotation(i, H_row):
    return _rotate_vectors(H_row, i, *givens[i, :])
  R_row = lax.fori_loop(0, k, apply_ith_rotation, H_row)

  givens_factors = _givens_rotation(R_row[k], R_row[k + 1])
  givens = givens.at[k, :].set(givens_factors)
  R_row = _rotate_vectors(R_row, k, *givens_factors)
  return R_row, givens


def _gmres_incremental(A, b, x0, unit_residual, residual_norm, ptol, restart, M):
  """
  Implements a single restart of GMRES. The restart-dimensional Krylov subspace
  K(A, x0) = span(A(x0), A@x0, A@A@x0, ..., A^restart @ x0) is built, and the
  projection of the true solution into this subspace is returned.

  This implementation builds the QR factorization during the Arnoldi process.
  """
  # https://www-users.cs.umn.edu/~saad/Calais/PREC.pdf

  V = tree_map(
      lambda x: jnp.pad(x[..., None], ((0, 0),) * x.ndim + ((0, restart),)),
      unit_residual,
  )
  dtype = jnp.result_type(*tree_leaves(b))
  # use eye() to avoid constructing a singular matrix in case of early
  # termination
  R = jnp.eye(restart, restart + 1, dtype=dtype)

  givens = jnp.zeros((restart, 2), dtype=dtype)
  beta_vec = jnp.zeros((restart + 1), dtype=dtype)
  beta_vec = beta_vec.at[0].set(residual_norm)

  def loop_cond(carry):
    k, err, _, _, _, _ = carry
    return jnp.logical_and(k < restart, err > ptol)

  def arnoldi_qr_step(carry):
    k, _, V, R, beta_vec, givens = carry
    V, H, _ = _kth_arnoldi_iteration(k, A, M, V, R)
    R_row, givens = _apply_givens_rotations(H[k, :], givens, k)
    R = R.at[k, :].set(R_row)
    beta_vec = _rotate_vectors(beta_vec, k, *givens[k, :])
    err = abs(beta_vec[k + 1])
    return k + 1, err, V, R, beta_vec, givens

  carry = (0, residual_norm, V, R, beta_vec, givens)
  carry = lax.while_loop(loop_cond, arnoldi_qr_step, carry)
  k, residual_norm, V, R, beta_vec, _ = carry
  del k  # Until we figure out how to pass this to the user.

  y = jsp.linalg.solve_triangular(R[:, :-1].T, beta_vec[:-1])
  dx = tree_map(lambda X: _dot(X[..., :-1], y), V)

  x = _add(x0, dx)
  residual = M(_sub(b, A(x)))
  unit_residual, residual_norm = _safe_normalize(residual)
  # TODO(shoyer): "Inner loop tolerance control" on ptol, like SciPy
  return x, unit_residual, residual_norm


def _lstsq(a, b):
  # faster than jsp.linalg.lstsq
  a2 = _dot(a.T.conj(), a)
  b2 = _dot(a.T.conj(), b)
  return jsp.linalg.solve(a2, b2, sym_pos=True)


def _gmres_batched(A, b, x0, unit_residual, residual_norm, ptol, restart, M):
  """
  Implements a single restart of GMRES. The ``restart``-dimensional Krylov
  subspace
  K(A, x0) = span(A(x0), A@x0, A@A@x0, ..., A^restart @ x0) is built, and the
  projection of the true solution into this subspace is returned.

  This implementation solves a dense linear problem instead of building
  a QR factorization during the Arnoldi process.
  """
  del ptol  # unused
  # https://www-users.cs.umn.edu/~saad/Calais/PREC.pdf
  V = tree_map(
      lambda x: jnp.pad(x[..., None], ((0, 0),) * x.ndim + ((0, restart),)),
      unit_residual,
  )
  dtype = jnp.result_type(*tree_leaves(b))
  H = jnp.eye(restart, restart + 1, dtype=dtype)

  def loop_cond(carry):
    _, _, breakdown, k = carry
    return jnp.logical_and(k < restart, jnp.logical_not(breakdown))

  def arnoldi_process(carry):
    V, H, _, k = carry
    V, H, breakdown = _kth_arnoldi_iteration(k, A, M, V, H)
    return V, H, breakdown, k + 1

  carry = (V, H, False, 0)
  V, H, _, _ = lax.while_loop(loop_cond, arnoldi_process, carry)

  beta_vec = jnp.zeros((restart + 1,), dtype=dtype)
  beta_vec = beta_vec.at[0].set(residual_norm)
  y = _lstsq(H.T, beta_vec)
  dx = tree_map(lambda X: _dot(X[..., :-1], y), V)

  x = _add(x0, dx)

  residual = M(_sub(b, A(x)))
  unit_residual, residual_norm = _safe_normalize(residual)
  return x, unit_residual, residual_norm


def _gmres_solve(A, b, x0, atol, ptol, restart, maxiter, M, gmres_func):
  """
  The main function call wrapped by custom_linear_solve. Repeatedly calls GMRES
  to find the projected solution within the order-``restart``
  Krylov space K(A, x0, restart), using the result of the previous projection
  in place of x0 each time. Parameters are the same as in ``gmres`` except:

  atol: Tolerance for norm(A(x) - b), used between restarts.
  ptol: Tolerance for norm(M(A(x) - b)), used within a restart.
  gmres_func: A function performing a single GMRES restart.

  Returns: The solution.
  """
  residual = M(_sub(b, A(x0)))
  unit_residual, residual_norm = _safe_normalize(residual)

  def cond_fun(value):
    _, k, _, residual_norm = value
    return jnp.logical_and(k < maxiter, residual_norm > atol)

  def body_fun(value):
    x, k, unit_residual, residual_norm = value
    x, unit_residual, residual_norm = gmres_func(
        A, b, x, unit_residual, residual_norm, ptol, restart, M)
    return x, k + 1, unit_residual, residual_norm

  initialization = (x0, 0, unit_residual, residual_norm)
  x_final, k, _, err = lax.while_loop(cond_fun, body_fun, initialization)
  _ = k  # Until we can pass this out
  _ = err
  return x_final  # , info


def gmres(A, b, x0=None, *, tol=1e-5, atol=0.0, restart=20, maxiter=None,
          M=None, solve_method='batched'):
  """
  GMRES solves the linear system A x = b for x, given A and b.

  A is specified as a function performing A(vi) -> vf = A @ vi, and in principle
  need not have any particular special properties, such as symmetry. However,
  convergence is often slow for nearly symmetric operators.

  Parameters
  ----------
  A: ndarray or function
      2D array or function that calculates the linear map (matrix-vector
      product) ``Ax`` when called like ``A(x)``. ``A`` must return array(s) with
      the same structure and shape as its argument.
  b : array or tree of arrays
      Right hand side of the linear system representing a single vector. Can be
      stored as an array or Python container of array(s) with any shape.

  Returns
  -------
  x : array or tree of arrays
      The converged solution. Has the same structure as ``b``.
  info : None
      Placeholder for convergence information. In the future, JAX will report
      the number of iterations when convergence is not achieved, like SciPy.

  Other Parameters
  ----------------
  x0 : array, optional
      Starting guess for the solution. Must have the same structure as ``b``.
      If this is unspecified, zeroes are used.
  tol, atol : float, optional
      Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
      We do not implement SciPy's "legacy" behavior, so JAX's tolerance will
      differ from SciPy unless you explicitly pass ``atol`` to SciPy's ``gmres``.
  restart : integer, optional
      Size of the Krylov subspace ("number of iterations") built between
      restarts. GMRES works by approximating the true solution x as its
      projection into a Krylov space of this dimension - this parameter
      therefore bounds the maximum accuracy achievable from any guess
      solution. Larger values increase both number of iterations and iteration
      cost, but may be necessary for convergence. The algorithm terminates
      early if convergence is achieved before the full subspace is built.
      Default is 20.
  maxiter : integer
      Maximum number of times to rebuild the size-``restart`` Krylov space
      starting from the solution found at the last iteration. If GMRES
      halts or is very slow, decreasing this parameter may help.
      Default is infinite.
  M : ndarray or function
      Preconditioner for A.  The preconditioner should approximate the
      inverse of A.  Effective preconditioning dramatically improves the
      rate of convergence, which implies that fewer iterations are needed
      to reach a given error tolerance.
  solve_method : 'incremental' or 'batched'
      The 'incremental' solve method builds a QR decomposition for the Krylov
      subspace incrementally during the GMRES process using Givens rotations.
      This improves numerical stability and gives a free estimate of the
      residual norm that allows for early termination within a single "restart".
      In contrast, the 'batched' solve method solves the least squares problem
      from scratch at the end of each GMRES iteration. It does not allow for
      early termination, but has much less overhead on GPUs.

  See also
  --------
  scipy.sparse.linalg.gmres
  jax.lax.custom_linear_solve
  """

  if x0 is None:
    x0 = tree_map(jnp.zeros_like, b)
  if M is None:
    M = _identity
  A = _normalize_matvec(A)
  M = _normalize_matvec(M)

  b, x0 = device_put((b, x0))
  size = sum(bi.size for bi in tree_leaves(b))

  if maxiter is None:
    maxiter = 10 * size  # copied from scipy
  restart = min(restart, size)

  if tree_structure(x0) != tree_structure(b):
    raise ValueError(
        'x0 and b must have matching tree structure: '
        f'{tree_structure(x0)} vs {tree_structure(b)}')

  b_norm = _norm(b)
  atol = jnp.maximum(tol * b_norm, atol)

  Mb = M(b)
  Mb_norm = _norm(Mb)
  ptol = Mb_norm * jnp.minimum(1.0, atol / b_norm)

  if solve_method == 'incremental':
    gmres_func = _gmres_incremental
  elif solve_method == 'batched':
    gmres_func = _gmres_batched
  else:
    raise ValueError(f"invalid solve_method {solve_method}, must be either "
                     "'incremental' or 'batched'")

  def _solve(A, b):
    return _gmres_solve(A, b, x0, atol, ptol, restart, maxiter, M, gmres_func)
  x = lax.custom_linear_solve(A, b, solve=_solve, transpose_solve=_solve)

  failed = jnp.isnan(_norm(x))
  info = jnp.where(failed, x=-1, y=0)
  return x, info
