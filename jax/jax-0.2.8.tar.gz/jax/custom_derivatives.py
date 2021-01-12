# coding=utf-8
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

from functools import update_wrapper, reduce, partial
import inspect
import operator as op
from typing import Callable, Sequence, Tuple, Any

from . import core
from . import dtypes
from . import linear_util as lu
from .tree_util import (tree_flatten, tree_unflatten, tree_map, tree_multimap,
                        register_pytree_node_class)
from ._src.util import cache, safe_zip, safe_map, split_list
from .api_util import flatten_fun_nokwargs, argnums_partial, wrap_hashably
from .core import raise_to_shaped
from .ad_util import Zero, zeros_like_aval, stop_gradient_p
from .interpreters import partial_eval as pe
from .interpreters import ad
from .interpreters import batching
from .interpreters import xla
from .interpreters.batching import not_mapped
from .config import config

from ._src import traceback_util
traceback_util.register_exclusion(__file__)

map = safe_map
zip = safe_zip


### util

def _resolve_kwargs(fun, args, kwargs):
  ba = inspect.signature(fun).bind(*args, **kwargs)
  ba.apply_defaults()
  if ba.kwargs:
    raise TypeError("keyword arguments could not be resolved to positions")
  else:
    return ba.args

def _initial_style_jaxpr(fun, in_avals):
  jaxpr, _, consts = pe.trace_to_jaxpr_dynamic(fun, in_avals)
  return jaxpr, consts

def _initial_style_staging() -> bool:
  return core.thread_local_state.trace_state.initial_style

def _sum_tangents(_, x, *xs):
  return reduce(ad.add_tangents, xs, x)

def _zeros_like_pytree(x):
  return tree_map(Zero.from_value, x)

@partial(partial, tree_map)
def _stop_gradient(x):
  if isinstance(x, core.Tracer):
    return stop_gradient_p.bind(x)
  else:
    return x


### JVPs

class custom_jvp:
  """Set up a JAX-transformable function for a custom JVP rule definition.

  This class is meant to be used as a function decorator. Instances are
  callables that behave similarly to the underlying function to which the
  decorator was applied, except when a differentiation transformation (like
  :py:func:`jax.jvp` or :py:func:`jax.grad`) is applied, in which case a custom
  user-supplied JVP rule function is used instead of tracing into and
  performing automatic differentiation of the underlying function's
  implementation.

  There are two instance methods available for defining the custom JVP rule:
  :py:func:`~jax.custom_jvp.defjvp` for defining a *single* custom JVP rule for
  all the function's inputs, and for convenience
  :py:func:`~jax.custom_jvp.defjvps`, which wraps
  :py:func:`~jax.custom_jvp.defjvp`, and allows you to provide separate
  definitions for the partial derivatives of the function w.r.t. each of its
  arguments.

  For example::

    import jax.numpy as jnp

    @jax.custom_jvp
    def f(x, y):
      return jnp.sin(x) * y

    @f.defjvp
    def f_jvp(primals, tangents):
      x, y = primals
      x_dot, y_dot = tangents
      primal_out = f(x, y)
      tangent_out = jnp.cos(x) * x_dot * y + jnp.sin(x) * y_dot
      return primal_out, tangent_out

  For a more detailed introduction, see the tutorial_.

  .. _tutorial: https://jax.readthedocs.io/en/latest/notebooks/Custom_derivative_rules_for_Python_code.html
  """

  def __init__(self, fun, nondiff_argnums=()):
    self.fun = fun
    self.nondiff_argnums = nondiff_argnums
    self.jvp = None
    update_wrapper(self, fun)

  def defjvp(self, jvp):
    """Define a custom JVP rule for the function represented by this instance.

    Args:
      jvp: a Python callable representing the custom JVP rule. When there are no
        ``nondiff_argnums``, the ``jvp`` function should accept two arguments,
        where the first is a tuple of primal inputs and the second is a tuple of
        tangent inputs. The lengths of both tuples is equal to the number of
        parameters of the ``custom_jvp`` function. The ``jvp`` function should
        produce as output a pair where the first element is the primal output
        and the second element is the tangent output. Elements of the input and
        output tuples may be arrays or any nested tuples/lists/dicts thereof.

    Returns:
      None.

    Example::

      import jax.numpy as jnp

      @jax.custom_jvp
      def f(x, y):
        return jnp.sin(x) * y

      @f.defjvp
      def f_jvp(primals, tangents):
        x, y = primals
        x_dot, y_dot = tangents
        primal_out = f(x, y)
        tangent_out = jnp.cos(x) * x_dot * y + jnp.sin(x) * y_dot
        return primal_out, tangent_out
    """
    self.jvp = jvp

  def defjvps(self, *jvps):
    """Convenience wrapper for defining JVPs for each argument separately.

    This convenience wrapper cannot be used together with ``nondiff_argnums``.

    Args:
      *jvps: a sequence of functions, one for each positional argument of the
        ``custom_jvp`` function. Each function takes as arguments the tangent
        value for the corresponding primal input, the primal output, and the
        primal inputs. See the example below.

    Returns:
      None.

    Example::

      @jax.custom_jvp
      def f(x, y):
        return jnp.sin(x) * y

      f.defjvps(lambda x_dot, primal_out, x, y: jnp.cos(x) * x_dot * y,
                lambda y_dot, primal_out, x, y: jnp.sin(x) * y_dot)
    """
    if self.nondiff_argnums:
      raise TypeError("Can't use ``defjvps`` with ``nondiff_argnums``.")

    def jvp(primals, tangents):
      primal_out = self(*primals)
      zeros = _zeros_like_pytree(primal_out)
      all_tangents_out = [jvp(t, primal_out, *primals) if jvp else zeros
                          for t, jvp in zip(tangents, jvps)]
      tangent_out = tree_multimap(_sum_tangents, primal_out, *all_tangents_out)
      return primal_out, tangent_out

    self.defjvp(jvp)

  def __call__(self, *args, **kwargs):
    if not self.jvp:
      msg = "No JVP defined for custom_jvp function {} using defjvp."
      raise AttributeError(msg.format(self.__name__))
    args = _resolve_kwargs(self.fun, args, kwargs)
    if self.nondiff_argnums:
      nondiff_argnums = set(self.nondiff_argnums)
      args = [_stop_gradient(x) if i in nondiff_argnums else x
              for i, x in enumerate(args)]
      diff_argnums = [i for i in range(len(args)) if i not in nondiff_argnums]
      f_, dyn_args = argnums_partial(lu.wrap_init(self.fun), diff_argnums, args)
      static_args = [args[i] for i in self.nondiff_argnums]
      jvp = _add_args(lu.wrap_init(self.jvp), static_args)
    else:
      f_, dyn_args = lu.wrap_init(self.fun), args
      jvp = lu.wrap_init(self.jvp)
    args_flat, in_tree = tree_flatten(dyn_args)
    flat_fun, out_tree1 = flatten_fun_nokwargs(f_, in_tree)
    flat_jvp, out_tree2 = _flatten_jvp(jvp, in_tree)
    if config.omnistaging_enabled:
      out_flat = custom_jvp_call_p.bind(flat_fun, flat_jvp, *args_flat)
      _, out_tree = lu.merge_linear_aux(out_tree1, out_tree2)
    else:
      if _initial_style_staging():
        out_flat = custom_jvp_call_jaxpr(flat_fun, flat_jvp, *args_flat)  # type: ignore
        out_tree = out_tree1()
      else:
        out_flat = custom_jvp_call_p.bind(flat_fun, flat_jvp, *args_flat)
        _, out_tree = lu.merge_linear_aux(out_tree1, out_tree2)
    return tree_unflatten(out_tree, out_flat)

def _add_args(f, extra_args):
  return _add_args_(f, tuple(map(wrap_hashably, extra_args)))

@lu.transformation
def _add_args_(extra_args, *args, **kwargs):
  extra_args = tuple([arg.val for arg in extra_args])
  all_args = (extra_args + args)
  yield (yield all_args, kwargs)

@lu.transformation_with_aux
def _flatten_jvp(in_tree, *args):
  primals_in, tangents_in = split_list(args, [len(args) // 2])
  py_primals = tree_unflatten(in_tree, primals_in)
  py_tangents = tree_unflatten(in_tree, tangents_in)
  pair_out = yield (py_primals, py_tangents), {}
  if not isinstance(pair_out, (list, tuple)) or len(pair_out) != 2:
    msg = ("Custom JVP rule must produce a pair (list or tuple of length two) "
           "representing primal and tangent outputs, got {}.")
    raise TypeError(msg.format(pair_out))
  py_primals_out, py_tangents_out = pair_out
  primals_out, out_tree = tree_flatten(py_primals_out)
  tangents_out, out_tree2 = tree_flatten(py_tangents_out)
  if out_tree != out_tree2:
    msg = ("Custom JVP rule must produce primal and tangent outputs with equal "
           "container (pytree) structures, but got {} and {} respectively.")
    raise TypeError(msg.format(out_tree, out_tree2))
  primal_avals_out = [raise_to_shaped(core.get_aval(x), weak_type=False) for x in primals_out]
  tangent_avals_out = [raise_to_shaped(core.get_aval(t), weak_type=False) for t in tangents_out]
  if primal_avals_out != tangent_avals_out:
    if len(primal_avals_out) == 1:
      (av1,), (av2,) = primal_avals_out, tangent_avals_out
      msg = ("Custom JVP rule must produce primal and tangent outputs with "
             "equal shapes and dtypes, but got {} and {} respectively.")
      raise TypeError(msg.format(av1.str_short(), av2.str_short()))
    else:
      msg = ("Custom JVP rule must produce primal and tangent outputs with "
             "equal shapes and dtypes, but got:\n{}")
      disagreements = (
          "  primal {} for tangent {}".format(av1.str_short(), av2.str_short())
          for av1, av2 in zip(primal_avals_out, tangent_avals_out) if av1 != av2)
      raise TypeError(msg.format('\n'.join(disagreements)))
  yield primals_out + tangents_out, out_tree

class CustomJVPCallPrimitive(core.CallPrimitive):
  initial_style: core.Primitive

  def bind(self, fun, jvp, *args):
    args = map(core.full_lower, args)
    top_trace = core.find_top_trace(args)
    fun, env_trace_todo1 = core.process_env_traces(
        fun, self, top_trace and top_trace.level, (), None)
    jvp, env_trace_todo2 = core.process_env_traces(
        jvp, self, top_trace and top_trace.level, (), None)
    tracers = map(top_trace.full_raise, args)  # type: ignore
    with core.maybe_new_sublevel(top_trace):
      outs = top_trace.process_custom_jvp_call(self, fun, jvp, tracers)  # type: ignore
    _, env_trace_todo = lu.merge_linear_aux(env_trace_todo1, env_trace_todo2)
    return _apply_todos(env_trace_todo, map(core.full_lower, outs))

  def impl(self, fun, _, *args):
    return fun.call_wrapped(*args)

  def post_process(self, trace, out_tracers, params):
    return trace.post_process_custom_jvp_call(out_tracers, params)

def _apply_todos(todos, outs):
  todos_list = list(todos)
  while todos_list:
    outs = map(core.full_lower, todos_list.pop()(outs))
  return outs

custom_jvp_call_p = CustomJVPCallPrimitive('custom_jvp_call')


def _custom_jvp_call_jaxpr_impl(*args, fun_jaxpr: core.ClosedJaxpr, **params):
  del params  # other params ignored because we're just executing the primal fun
  return core.jaxpr_as_fun(fun_jaxpr)(*args)

def _custom_jvp_call_jaxpr_abstract_eval(*args, fun_jaxpr: core.ClosedJaxpr, **params):
  del args, params
  return fun_jaxpr.out_avals

custom_jvp_call_jaxpr_p = core.Primitive('custom_jvp_call_jaxpr')
custom_jvp_call_jaxpr_p.multiple_results = True
custom_jvp_call_jaxpr_p.def_impl(_custom_jvp_call_jaxpr_impl)
custom_jvp_call_jaxpr_p.def_abstract_eval(_custom_jvp_call_jaxpr_abstract_eval)
CustomJVPCallPrimitive.initial_style = custom_jvp_call_jaxpr_p

def _custom_jvp_call_jaxpr_jvp(
    primals, tangents, *, fun_jaxpr: core.ClosedJaxpr,
    jvp_jaxpr_thunk: Callable[[], Tuple[core.Jaxpr, Sequence[Any]]],
    num_consts: int):
  _, args = split_list(primals, [num_consts])
  consts_dot, args_dot = split_list(tangents, [num_consts])
  if any(type(t) is not Zero for t in consts_dot):
    raise ad.CustomJVPException()
  jvp_jaxpr, jvp_consts = jvp_jaxpr_thunk()  # consts can be tracers!
  args_dot = map(ad.instantiate_zeros, args_dot)
  # Cast float0 to zeros with the primal dtype because custom jvp rules don't
  # currently handle float0s
  args_dot = map(ad.replace_float0s, args, args_dot)
  outs = core.eval_jaxpr(jvp_jaxpr, jvp_consts, *args, *args_dot)
  primals_out, tangents_out = split_list(outs, [len(outs) // 2])
  tangents_out = map(ad.recast_to_float0, primals_out, tangents_out)
  return primals_out, tangents_out
ad.primitive_jvps[custom_jvp_call_jaxpr_p] = _custom_jvp_call_jaxpr_jvp

def _custom_jvp_call_jaxpr_vmap(
    args, in_dims, axis_name, *, fun_jaxpr: core.ClosedJaxpr,
    jvp_jaxpr_thunk: Callable[[], Tuple[core.Jaxpr, Sequence[Any]]],
    num_consts: int):
  size, = {x.shape[d] for x, d in zip(args, in_dims) if d is not not_mapped}
  args = [batching.moveaxis(x, d, 0) if d is not not_mapped and d != 0
          else x for x, d in zip(args, in_dims)]
  num_out = len(fun_jaxpr.out_avals)

  in_batched = [d is not not_mapped for d in in_dims]
  batched_fun_jaxpr, out_batched = batching.batch_jaxpr(fun_jaxpr, size, in_batched, False, axis_name)
  out_dims1 = [0 if b else not_mapped for b in out_batched]
  out_dims2 = []  # mutable cell updated by batched_jvp_jaxpr_thunk

  @pe._memoize
  def batched_jvp_jaxpr_thunk():
    jvp_jaxpr = core.ClosedJaxpr(*jvp_jaxpr_thunk())  # consts can be tracers
    _, args_batched = split_list(in_batched, [num_consts])
    _, all_batched = batching.batch_jaxpr(jvp_jaxpr, size, args_batched * 2, False, axis_name)
    primals_batched, tangents_batched = split_list(all_batched, [num_out])
    out_batched = map(op.or_, primals_batched, tangents_batched)
    out_dims2.append([0 if b else not_mapped for b in out_batched])
    batched_jvp_jaxpr, _ = batching.batch_jaxpr(
        jvp_jaxpr, size, args_batched * 2, out_batched * 2, axis_name)
    return batched_jvp_jaxpr.jaxpr, batched_jvp_jaxpr.consts

  batched_outs = custom_jvp_call_jaxpr_p.bind(
      *args, fun_jaxpr=batched_fun_jaxpr,
      jvp_jaxpr_thunk=batched_jvp_jaxpr_thunk, num_consts=num_consts)
  out_dims = out_dims2[0] if out_dims2 else out_dims1
  return batched_outs, out_dims
batching.initial_style_batchers[custom_jvp_call_jaxpr_p] = _custom_jvp_call_jaxpr_vmap

xla.initial_style_translations[custom_jvp_call_jaxpr_p] = \
    xla.lower_fun_initial_style(_custom_jvp_call_jaxpr_impl)

# If a (multi)linear function is defined with a custom jvp, then
# custom_jvp_call_jaxpr can appear in jaxprs to be transposed. Since it's
# already been linearized, we can drop the jvp rule.
def _custom_jvp_call_jaxpr_transpose(cts, *args, fun_jaxpr, jvp_jaxpr_thunk,
                                     num_consts):
  del jvp_jaxpr_thunk, num_consts
  return ad.backward_pass(fun_jaxpr.jaxpr, fun_jaxpr.consts, args, cts)
ad.primitive_transposes[custom_jvp_call_jaxpr_p] = _custom_jvp_call_jaxpr_transpose


### VJPs

class custom_vjp:
  """Set up a JAX-transformable function for a custom VJP rule definition.

  This class is meant to be used as a function decorator. Instances are
  callables that behave similarly to the underlying function to which the
  decorator was applied, except when a reverse-mode differentiation
  transformation (like :py:func:`jax.grad`) is applied, in which case a custom
  user-supplied VJP rule function is used instead of tracing into and performing
  automatic differentiation of the underlying function's implementation. There
  is a single instance method, :py:func:`~jax.custom_vjp.defvjp`, which may be
  used to define the custom VJP rule.

  This decorator precludes the use of forward-mode automatic differentiation.

  For example::

    import jax.numpy as jnp

    @jax.custom_vjp
    def f(x, y):
      return jnp.sin(x) * y

    def f_fwd(x, y):
      return f(x, y), (jnp.cos(x), jnp.sin(x), y)

    def f_bwd(res, g):
      cos_x, sin_x, y = res
      return (cos_x * g * y, sin_x * g)

    f.defvjp(f_fwd, f_bwd)

  For a more detailed introduction, see the tutorial_.

  .. _tutorial: https://jax.readthedocs.io/en/latest/notebooks/Custom_derivative_rules_for_Python_code.html
  """

  def __init__(self, fun, nondiff_argnums=()):
    self.fun = fun
    self.nondiff_argnums = nondiff_argnums
    self.fwd = None
    self.bwd = None
    update_wrapper(self, fun)

  def defvjp(self, fwd, bwd):
    """Define a custom VJP rule for the function represented by this instance.

    Args:
      fwd: a Python callable representing the forward pass of the custom VJP
        rule. When there are no ``nondiff_argnums``, the ``fwd`` function has
        the same input signature as the underlying primal function. It should
        return as output a pair, where the first element represents the primal
        output and the second element represents any "residual" values to store
        from the forward pass for use on the backward pass by the function
        ``bwd``. Input arguments and elements of the output pair may be arrays
        or nested tuples/lists/dicts thereof.
      bwd: a Python callable representing the backward pass of the custom VJP
        rule. When there are no ``nondiff_argnums``, the ``bwd`` function takes
        two arguments, where the first is the "residual" values produced on the
        forward pass by ``fwd``, and the second is the output cotangent with the
        same structure as the primal function output. The output of ``bwd`` must
        be a tuple of length equal to the number of arguments of the primal
        function, and the tuple elements may be arrays or nested
        tuples/lists/dicts thereof so as to match the structure of the primal
        input arguments.

    Returns:
      None.

    Example::

      import jax.numpy as jnp

      @jax.custom_vjp
      def f(x, y):
        return jnp.sin(x) * y

      def f_fwd(x, y):
        return f(x, y), (jnp.cos(x), jnp.sin(x), y)

      def f_bwd(res, g):
        cos_x, sin_x, y = res
        return (cos_x * g * y, sin_x * g)

      f.defvjp(f_fwd, f_bwd)
    """
    self.fwd = fwd
    self.bwd = bwd

  def __call__(self, *args, **kwargs):
    if not self.fwd or not self.bwd:
      msg = "No VJP defined for custom_vjp function {} using defvjp."
      raise AttributeError(msg.format(self.__name__))
    args = _resolve_kwargs(self.fun, args, kwargs)
    if self.nondiff_argnums:
      for i in self.nondiff_argnums: _check_for_tracers(args[i])
      nondiff_argnums = set(self.nondiff_argnums)
      dyn_argnums = [i for i in range(len(args)) if i not in nondiff_argnums]
      f_, dyn_args = argnums_partial(lu.wrap_init(self.fun), dyn_argnums, args)
      static_args = [args[i] for i in self.nondiff_argnums]
      fwd, _ = argnums_partial(lu.wrap_init(self.fwd), dyn_argnums, args)
      bwd = _add_args(lu.wrap_init(self.bwd), static_args)
    else:
      f_, dyn_args = lu.wrap_init(self.fun), args
      fwd, bwd = lu.wrap_init(self.fwd), lu.wrap_init(self.bwd)
    args_flat, in_tree = tree_flatten(dyn_args)
    in_avals = [core.raise_to_shaped(core.get_aval(x)) for x in args_flat]
    flat_fun, out_tree = flatten_fun_nokwargs(f_, in_tree)
    flat_fwd, out_trees = _flatten_fwd(fwd, in_tree)
    flat_bwd = _flatten_bwd(bwd, in_tree, in_avals, out_trees)
    if config.omnistaging_enabled:
      out_flat = custom_vjp_call_p.bind(flat_fun, flat_fwd, flat_bwd, *args_flat,
                                        out_trees=out_trees)
      fst, aux = lu.merge_linear_aux(out_tree, out_trees)
      out_tree = aux if fst else aux[0]
    else:
      if _initial_style_staging():
        out_flat = custom_vjp_call_jaxpr(flat_fun, flat_fwd, flat_bwd,  # type: ignore
                                         *args_flat, out_trees=out_trees)
        out_tree = out_tree()
      else:
        out_flat = custom_vjp_call_p.bind(flat_fun, flat_fwd, flat_bwd,
                                          *args_flat, out_trees=out_trees)
        fst, aux = lu.merge_linear_aux(out_tree, out_trees)
        out_tree = aux if fst else aux[0]
    return tree_unflatten(out_tree, out_flat)

@partial(partial, tree_map)
def _check_for_tracers(x):
  if isinstance(x, core.Tracer):
    msg = ("Found a JAX Tracer object passed as an argument to a custom_vjp "
           "function in a position indicated by nondiff_argnums as "
           "non-differentiable. Tracers cannot be passed as non-differentiable "
           "arguments to custom_vjp functions; instead, nondiff_argnums should "
           "only be used for arguments that can't be or contain JAX tracers, "
           "e.g. function-valued arguments. In particular, array-valued "
           "arguments should typically not be indicated as nondiff_argnums. "
           "\n\n"
           "This behavior recently changed in JAX. "
           "See https://github.com/google/jax/blob/master/docs/custom_vjp_update.md "
           "for more information.")
    raise core.UnexpectedTracerError(msg)

@lu.transformation_with_aux
def _flatten_fwd(in_tree, *args):
  py_args = tree_unflatten(in_tree, args)
  pair_out = yield py_args, {}
  if not isinstance(pair_out, (list, tuple)) or len(pair_out) != 2:
    msg = ("Custom VJP fwd function must produce a pair (list or tuple of "
           "length two) representing primal outputs and residuals (values "
           "stored from the forward pass for use on the backward pass), "
           "got {}.")
    raise TypeError(msg.format(pair_out))
  py_outs, res = pair_out
  out, out_tree = tree_flatten(py_outs)
  res, res_tree = tree_flatten(res)
  yield res + out, (out_tree, res_tree)

@lu.transformation
def _flatten_bwd(in_tree, in_avals, out_trees, *args):
  out_tree, res_tree = out_trees()
  res, cts_out = split_list(args, [res_tree.num_leaves])
  py_res = tree_unflatten(res_tree, res)
  py_cts_out = tree_unflatten(out_tree, cts_out)
  py_cts_in = yield (py_res, py_cts_out), {}
  # For each None in py_cts_in, indicating an argument for which the rule
  # produces no cotangent, we replace it with a pytree with the structure of the
  # corresponding subtree of in_tree and with leaves of a non-pytree sentinel
  # object, to be replaced with Nones in the final returned result.
  zero = object()  # non-pytree sentinel to replace Nones in py_cts_in
  py_cts_in_ = tuple(zero if ct is None else ct for ct in py_cts_in)
  dummy = tree_unflatten(in_tree, [object()] * in_tree.num_leaves)
  cts_in_flat = []
  append_cts = lambda x, d: cts_in_flat.extend([x] * len(tree_flatten(d)[0]))
  try:
    tree_multimap(append_cts, py_cts_in_, dummy)
  except ValueError:
    _, in_tree2 = tree_flatten(py_cts_in)
    msg = ("Custom VJP rule must produce an output with the same container "
           "(pytree) structure as the args tuple of the primal function, "
           "and in particular must produce a tuple of length equal to the "
           "number of arguments to the primal function, but got VJP output "
           "structure {} for primal input structure {}.")
    raise TypeError(msg.format(in_tree2, in_tree)) from None
  yield [zeros_like_aval(aval.at_least_vspace()) if ct is zero else ct
         for aval, ct in zip(in_avals, cts_in_flat)]


class CustomVJPCallPrimitive(core.CallPrimitive):
  initial_style: core.Primitive

  def bind(self, fun, fwd, bwd, *args, out_trees):
    args = map(core.full_lower, args)
    top_trace = core.find_top_trace(args)
    fun, env_trace_todo1 = core.process_env_traces(
        fun, self, top_trace and top_trace.level, (), None)
    fwd, env_trace_todo2 = core.process_env_traces(
        fwd, self, top_trace and top_trace.level, (), None)
    tracers = map(top_trace.full_raise, args)  # type: ignore
    with core.maybe_new_sublevel(top_trace):
      outs = top_trace.process_custom_vjp_call(self, fun, fwd, bwd, tracers,
                                               out_trees=out_trees)
    _, env_trace_todo = lu.merge_linear_aux(env_trace_todo1, env_trace_todo2)
    return _apply_todos(env_trace_todo, map(core.full_lower, outs))

  def impl(self, fun, fwd, bwd, *args, out_trees):
    del fwd, bwd, out_trees
    return fun.call_wrapped(*args)

  def post_process(self, trace, out_tracers, params):
    return trace.post_process_custom_vjp_call(out_tracers, params)
custom_vjp_call_p = CustomVJPCallPrimitive('custom_vjp_call')

def _custom_vjp_call_jaxpr_impl(*args, fun_jaxpr, **_):
  return core.jaxpr_as_fun(fun_jaxpr)(*args)

def _custom_vjp_call_jaxpr_abstract_eval(*_, fun_jaxpr, **__):
  return fun_jaxpr.out_avals

custom_vjp_call_jaxpr_p = core.Primitive('custom_vjp_call_jaxpr')
custom_vjp_call_jaxpr_p.multiple_results = True
custom_vjp_call_jaxpr_p.def_impl(_custom_vjp_call_jaxpr_impl)
custom_vjp_call_jaxpr_p.def_abstract_eval(_custom_vjp_call_jaxpr_abstract_eval)
CustomVJPCallPrimitive.initial_style = custom_vjp_call_jaxpr_p

def _custom_vjp_call_jaxpr_jvp(
    primals, tangents, *, fun_jaxpr: core.ClosedJaxpr,
    fwd_jaxpr_thunk: Callable[[], Tuple[core.Jaxpr, Sequence[Any]]],
    bwd: lu.WrappedFun, out_trees: Callable, num_consts: int):
  _, args = split_list(primals, [num_consts])
  consts_dot, args_dot = split_list(tangents, [num_consts])
  if any(type(t) is not Zero for t in consts_dot):
    raise ad.CustomVJPException()
  fwd_jaxpr, fwd_consts = fwd_jaxpr_thunk()  # consts can be tracers!
  out_tree, res_tree = out_trees()
  args_dot = map(ad.instantiate_zeros, args_dot)
  # Cast float0 to zeros with the primal dtype because custom vjp rules don't
  # currently handle float0s
  args_dot = map(ad.replace_float0s, args, args_dot)
  res_and_primals_out = core.eval_jaxpr(fwd_jaxpr, fwd_consts, *args)
  res, primals_out = split_list(res_and_primals_out, [res_tree.num_leaves])
  avals_out = [raise_to_shaped(core.get_aval(x)) for x in primals_out]
  tangents_out = ad.custom_lin_p.bind(
      *res, *args_dot, num_res=res_tree.num_leaves, bwd=bwd, avals_out=avals_out)
  tangents_out = map(ad.recast_to_float0, primals_out, tangents_out)
  return primals_out, tangents_out
ad.primitive_jvps[custom_vjp_call_jaxpr_p] = _custom_vjp_call_jaxpr_jvp

def _custom_vjp_call_jaxpr_vmap(
    args, in_dims, axis_name, *, fun_jaxpr: core.ClosedJaxpr,
    fwd_jaxpr_thunk: Callable[[], Tuple[core.Jaxpr, Sequence[Any]]],
    bwd: lu.WrappedFun, out_trees: Callable, num_consts: int):
  size, = {x.shape[d] for x, d in zip(args, in_dims) if d is not not_mapped}
  args = [batching.moveaxis(x, d, 0) if d is not not_mapped and d != 0
          else x for x, d in zip(args, in_dims)]

  in_batched = [d is not not_mapped for d in in_dims]
  _, args_batched = split_list(in_batched, [num_consts])
  batched_fun_jaxpr, out_batched = batching.batch_jaxpr(fun_jaxpr, size, in_batched, False, axis_name)
  out_dims1 = [0 if b else not_mapped for b in out_batched]
  out_dims2 = []

  @pe._memoize
  def batched_fwd_jaxpr_thunk():
    fwd_jaxpr = core.ClosedJaxpr(*fwd_jaxpr_thunk())  # consts can be tracers
    batched_fwd_jaxpr, out_batched = batching.batch_jaxpr(
        fwd_jaxpr, size, args_batched, False, axis_name)
    out_dims2.append([0 if b else not_mapped for b in out_batched])
    return batched_fwd_jaxpr.jaxpr, batched_fwd_jaxpr.consts

  fwd_args_batched = [0 if b else not_mapped for b in args_batched]
  fwd_out_dims = lambda: out_dims2[0]
  # TODO(mattjj,apaszke): Support collectives in custom_vjp?
  batched_bwd = batching.batch_fun(bwd, fwd_out_dims, fwd_args_batched,
                                   axis_name='__unused_axis_name', sum_match=True)

  batched_outs = custom_vjp_call_jaxpr_p.bind(
      *args, fun_jaxpr=batched_fun_jaxpr,
      fwd_jaxpr_thunk=batched_fwd_jaxpr_thunk, bwd=batched_bwd,
      out_trees=out_trees, num_consts=num_consts)
  out_dims = out_dims2[0] if out_dims2 else out_dims1
  if not config.omnistaging_enabled:
    out_dims = out_dims[:len(batched_outs)]
  return batched_outs, out_dims
batching.initial_style_batchers[custom_vjp_call_jaxpr_p] = _custom_vjp_call_jaxpr_vmap

xla.initial_style_translations[custom_vjp_call_jaxpr_p] = \
    xla.lower_fun_initial_style(_custom_vjp_call_jaxpr_impl)

batching.primitive_batchers[ad.custom_lin_p] = ad._raise_custom_vjp_error_on_jvp


@config.register_omnistaging_disabler
def omnistaging_disabler() -> None:
  global _initial_style_jaxpr, custom_vjp_call_jaxpr, custom_jvp_call_jaxpr

  def _initial_style_jaxpr(fun, in_avals):
    in_pvals = [pe.PartialVal.unknown(aval) for aval in in_avals]
    jaxpr, _, consts = pe.trace_to_jaxpr(fun, in_pvals, instantiate=True,
                                         bottom=True, stage_out=False)  # type: ignore
    assert not any(isinstance(c, core.Tracer) for c in consts)
    return jaxpr, consts

  def jvp_bind(self, fun, jvp, *args):
    args = map(core.full_lower, args)
    top_trace = core.find_top_trace(args)
    fun, env_trace_todo1 = core.process_env_traces(
        fun, self, top_trace and top_trace.level, (), None)
    jvp, env_trace_todo2 = core.process_env_traces(
        jvp, self, top_trace and top_trace.level, (), None)
    if top_trace is None:
      with core.new_sublevel():
        outs = self.impl(fun, jvp, *args)
    else:
      tracers = map(top_trace.full_raise, args)
      outs = top_trace.process_custom_jvp_call(self, fun, jvp, tracers)
    _, env_trace_todo = lu.merge_linear_aux(env_trace_todo1, env_trace_todo2)
    if env_trace_todo:
      raise core.UnexpectedTracerError
    return map(core.full_lower, outs)
  CustomJVPCallPrimitive.bind = jvp_bind  # type: ignore

  def jvp_post_process(self, trace, out_tracers, params):
    raise core.UnexpectedTracerError
  CustomJVPCallPrimitive.post_process = jvp_post_process  # type: ignore

  def vjp_bind(self, fun, fwd, bwd, *args, out_trees):
    args = map(core.full_lower, args)
    top_trace = core.find_top_trace(args)
    if top_trace is None:
      outs = fun.call_wrapped(*args)
    else:
      tracers = map(top_trace.full_raise, args)
      outs = top_trace.process_custom_vjp_call(self, fun, fwd, bwd, tracers,
                                               out_trees=out_trees)
    return map(core.full_lower, outs)
  CustomVJPCallPrimitive.bind = vjp_bind  # type: ignore

  def vjp_post_process(self, trace, out_tracers, params):
    raise core.UnexpectedTracerError
  CustomVJPCallPrimitive.post_process = vjp_post_process  # type: ignore

  def custom_jvp_call_jaxpr(fun: Callable, jvp: Callable, *args):
    in_avals = [raise_to_shaped(core.get_aval(x)) for x in args]
    fun_jaxpr, consts = _initial_style_jaxpr(fun, in_avals)  # consts can be tracers!
    closed_fun_jaxpr = core.ClosedJaxpr(pe.convert_constvars_jaxpr(fun_jaxpr), ())
    jvp_jaxpr_thunk = pe._memoize(lambda: _initial_style_jaxpr(jvp, in_avals * 2))
    return custom_jvp_call_jaxpr_p.bind(
        *consts, *args, fun_jaxpr=closed_fun_jaxpr,
        jvp_jaxpr_thunk=jvp_jaxpr_thunk, num_consts=len(consts))

  def custom_vjp_call_jaxpr(fun, fwd, bwd, *args, out_trees):
    in_avals = [raise_to_shaped(core.get_aval(x)) for x in args]
    fun_jaxpr, consts = _initial_style_jaxpr(fun, in_avals)  # consts can be tracers!
    closed_fun_jaxpr = core.ClosedJaxpr(pe.convert_constvars_jaxpr(fun_jaxpr), ())
    fwd_jaxpr_thunk = pe._memoize(lambda: _initial_style_jaxpr(fwd, in_avals))
    return custom_vjp_call_jaxpr_p.bind(
        *consts, *args, fun_jaxpr=closed_fun_jaxpr,
        fwd_jaxpr_thunk=fwd_jaxpr_thunk, bwd=bwd, out_trees=out_trees,
        num_consts=len(consts))


def custom_gradient(fun):
  """Convenience function for defining custom VJP rules (aka custom gradients).

  While the canonical way to define custom VJP rules is via ``jax.custom_vjp``,
  the ``custom_gradient`` convenience wrapper follows TensorFlow's
  ``tf.custom_gradient`` API. The difference here is that ``custom_gradient``
  can be used as a decorator on one function that returns both the primal value
  (representing the output of the mathematical function to be differentiated)
  and the VJP (gradient) function. See
  https://www.tensorflow.org/api_docs/python/tf/custom_gradient.

  If the mathematical function to be differentiated has type signature ``a ->
  b``, then the Python callable ``fun`` should have signature
  ``a -> (b, CT b --o CT a)`` where we use ``CT x`` to denote a cotangent type
  for ``x`` and the ``--o`` arrow to denote a linear function. See the example
  below. That is, ``fun`` should return a pair where the first element
  represents the value of the mathematical function to be differentiated and the
  second element is a function to be called on the backward pass of reverse-mode
  automatic differentiation (i.e. the "custom gradient" function).

  The function returned as the second element of the output of ``fun`` can close
  over intermediate values computed when evaluating the function to be
  differentiated. That is, use lexical closure to share work between the forward
  pass and the backward pass of reverse-mode automatic differentiation. However,
  it cannot support Python control flow.

  Args:
    fun: a Python callable specifying both the mathematical function to be
      differentiated and its reverse-mode differentiation rule. It should return
      a pair consisting of an output value and a Python callable that represents
      the custom gradient function.

  Returns:
    A Python callable that accepts the same arguments as ``fun`` and returns the
    output value specified by the first element of ``fun``'s output pair.

  For example:

  >>> @jax.custom_gradient
  ... def f(x):
  ...   return x ** 2, lambda g: (g * x,)
  ...
  >>> print(f(3.))
  9.0
  >>> print(jax.grad(f)(3.))
  3.0

  An example with a function on two arguments, so that the VJP function must
  return a tuple of length two:

  >>> @jax.custom_gradient
  ... def f(x, y):
  ...   return x * y, lambda g: (y, x)
  ...
  >>> print(f(3., 4.))
  12.0
  >>> print(jax.grad(f, argnums=(0, 1))(3., 4.))
  (4.0, 3.0)
  """
  @custom_vjp
  def wrapped_fun(*args, **kwargs):
    ans, _ = fun(*args, **kwargs)
    return ans

  def fwd(*args, **kwargs):
    ans, rule = fun(*args, **kwargs)
    ans_flat, out_tree = tree_flatten((ans,))
    rule, in_tree = flatten_fun_nokwargs(lu.wrap_init(rule), out_tree)
    ans_avals = [core.get_aval(x).at_least_vspace() for x in ans_flat]
    if config.omnistaging_enabled:
      jaxpr, _, consts = pe.trace_to_jaxpr_dynamic(rule, ans_avals)
    else:
      ans_pvals = [pe.PartialVal.unknown(a) for a in ans_avals]
      jaxpr, _, consts = pe.trace_to_jaxpr(rule, ans_pvals, instantiate=True)
    return ans, Residuals(jaxpr, in_tree(), out_tree, consts)

  def bwd(res, cts):
    jaxpr, in_tree, out_tree, consts = res
    cts_flat, out_tree_ = tree_flatten((cts,))
    if out_tree != out_tree_: raise TypeError(f'{out_tree}\n!=\n{out_tree_}')
    cts_out = core.eval_jaxpr(jaxpr, consts, *cts_flat)
    return tree_unflatten(in_tree, cts_out)

  wrapped_fun.defvjp(fwd, bwd)
  return wrapped_fun

@register_pytree_node_class
class Residuals:
  def __init__(self, jaxpr, in_tree, out_tree, consts):
    self.jaxpr = jaxpr
    self.in_tree = in_tree
    self.out_tree = out_tree
    self.consts = consts
  def __iter__(self):
    return iter((self.jaxpr, self.in_tree, self.out_tree, self.consts))
  def tree_flatten(self):
    return self.consts, (self.jaxpr, self.in_tree, self.out_tree)
  @classmethod
  def tree_unflatten(cls, aux, consts):
    jaxpr, in_tree, out_tree = aux
    return cls(jaxpr, in_tree, out_tree, consts)


def closure_convert(fun, *example_args):
  """Closure conversion utility, for use with higher-order custom derivatives.

  To define custom derivatives such as with ``jax.custom_vjp(f)``, the target
  function ``f`` must take, as formal arguments, all values involved in
  differentiation. If ``f`` is a higher-order function, in that it accepts as an
  argument a Python function ``g``, then values stored away in ``g``'s closure
  will not be visible to the custom derivative rules, and attempts at AD
  involving these values will fail. One way around this is to convert the
  closure by extracting these values, and to pass them as explicit formal
  arguments across the custom derivative boundary. This utility carries out that
  conversion. More precisely, it closure-converts the function ``fun``
  specialized to the types of the arguments given in ``example_args``.

  When we refer here to "values in the closure" of ``fun``, we do not mean the
  values that are captured by Python directly when ``fun`` is defined (e.g. the
  Python objects in ``fun.__closure__``, if the attribute exists). Rather, we
  mean values encountered during the execution of ``fun`` on ``example_args``
  that determine its output. This may include, for instance, arrays captured
  transitively in Python closures, i.e. in the Python closure of functions
  called by ``fun``, the closures of the functions that they call, and so forth.

  The function ``fun`` must be a pure function.

  Example usage::

    def minimize(objective_fn, x0):
      converted_fn, aux_args = closure_convert(objective_fn, x0)
      return _minimize(converted_fn, x0, *aux_args)

    @partial(custom_vjp, nondiff_argnums=(0,))
    def _minimize(objective_fn, x0, *args):
      z = objective_fn(x0, *args)
      # ... find minimizer x_opt ...
      return x_opt

    def fwd(objective_fn, x0, *args):
      y = _minimize(objective_fn, x0, *args)
      return y, (y, args)

    def rev(objective_fn, res, g):
      y, args = res
      y_bar = g
      # ... custom reverse-mode AD ...
      return x0_bar, *args_bars

    _minimize.defvjp(fwd, rev)

  Args:
    fun: Python callable to be converted. Must be a pure function.
    example_args: Arrays, scalars, or (nested) standard Python
      containers (tuples, lists, dicts, namedtuples, i.e., pytrees)
      thereof, used to determine the types of the formal arguments to
      ``fun``. This type-specialized form of ``fun`` is the function
      that will be closure converted.

  """
  flat_args, in_tree = tree_flatten(example_args)
  in_avals = tuple(map(abstractify, flat_args))
  return _closure_convert_for_avals(fun, in_tree, in_avals)

@cache()
def _closure_convert_for_avals(fun, in_tree, in_avals):
  if config.omnistaging_enabled:
    wrapped_fun, out_tree = flatten_fun_nokwargs(lu.wrap_init(fun), in_tree)
    jaxpr, out_pvals, consts = pe.trace_to_jaxpr_dynamic(wrapped_fun, in_avals)
  else:
    in_pvals = [pe.PartialVal.unknown(aval) for aval in in_avals]
    wrapped_fun, out_tree = flatten_fun_nokwargs(lu.wrap_init(fun), in_tree)
    with core.initial_style_staging():  # type: ignore
      jaxpr, out_pvals, consts = pe.trace_to_jaxpr(
        wrapped_fun, in_pvals, instantiate=True, stage_out=False)  # type: ignore
  out_tree = out_tree()

  # We only want to closure convert for constants with respect to which we're
  # differentiating. As a proxy for that, we hoist consts with float dtype.
  # TODO(mattjj): revise this approach
  from .numpy import inexact
  is_float = lambda c: dtypes.issubdtype(dtypes.dtype(c), inexact)
  (closure_consts, hoisted_consts), merge = partition_list(is_float, consts)
  num_consts = len(hoisted_consts)

  def converted_fun(*args_hconsts):
    num_args = len(args_hconsts) - num_consts
    args, hoisted_consts = split_list(args_hconsts, [num_args])
    consts = merge(closure_consts, hoisted_consts)
    all_args, in_tree2 = tree_flatten(tuple(args))
    assert in_tree == in_tree2
    out_flat = core.eval_jaxpr(jaxpr, consts, *all_args)
    return tree_unflatten(out_tree, out_flat)

  return converted_fun, hoisted_consts

def partition_list(choice, lst):
  out = [], []
  which = [out[choice(elt)].append(elt) or choice(elt) for elt in lst]
  def merge(l1, l2):
    i1, i2 = iter(l1), iter(l2)
    return [next(i2 if snd else i1) for snd in which]
  return out, merge

def abstractify(x):
  return core.raise_to_shaped(core.get_aval(x))
