import numpy as np


kb = 1.3806488e-23  # K/J
Na = 6.02214e23

a = np.array([[14.8359, 22.2019, 7220.9599, 23193.475, -6207.4663, 1732.96],
              [8.0034, -22.5111, 3.5750, 60.3129, 0., 0.],
              [6.9829, -13.7097, -1.9604, 17.3237, 0, 0],
              [6.4159, -34.3656, 59.6108, -21.6579, -35.8210, 27.2358],
              [6.1284, -9.1568, -0.2229, 4.5311, 0., 0.],
              [5.9217, -8.0711, 0.4264, 2.5600, 0., 0.]])

b = np.array([[0, -6.9630, 468.7358, -983.6038, 914.3608, -1383.4441],
              [0, -5.2669, 10.2299, -6.4860, 0., 0.],
              [0, -3.869, 5.2519, -2.3637, 0., 0.],
              [0, -6.9751, 19.2063, -26.0583, 17.4222, -4.5757],
              [0., -2.8486, 2.7828, -0.9030, 0., 0.],
             [0, -2.5291, 2.1864, -0.6298, 0., 0.]])

c = np.array([[0.1284, 1.6772, 0., 0., 0., 0.],
             [0.1125, 1.5404, -5.8769, 5.2427, 0., 0.],
             [-0.2092, 4.2672, -9.7703, 4.8661, -0.1950, 4.2125],
             [0.1350, 1.3115, -10.1437, 24.0729, -24.8084, 9.7109],
              [0.1107, 1.9807, -6.6720, 5.4841, 0., 0.],
             [0.1302, 1.9357, -6.4591, 5.1864, 0., 0.]])

d = np.array([[0., 0.4049, -0.1592, 0., 0., 0.],
             [0., -3.1964, 2.5174, 0.3518, -0.1654, 0.],
             [0, -1.3778, -2.4836, 3.5280, 0.7918, -0.1246],
             [0., -5.8540, 13.3411, -14.3302, 6.7309, -0.7830],
             [0, -3.1341, 2.7657, -0.2737, -0.0431, 0.],
             [0, -3.1078, 2.8058, -0.4375, 0., 0.]])

j = np.array([[1.8966, -6.9808, 10.6330, -9.2041, 4.2503, 0.],
              [-0.0696, -1.9440, 6.2575, -5.4431, 0.8731, 0.],
              [0.0656, -1.4630, 3.6991, -2.5081, 0., 0.],
              [0.1025, -1.1948, 2.8448, -1.9519, 0., 0.],
              [0.1108, -0.9900, 2.2187, -1.5027, 0., 0.],
              [0.2665, -0.4268, -0.2732, 0.6486, 0., 0.]])

k = np.array([[0, -1.6205, -0.8019, 1.7086, -0.5333, 1.0536],
             [0, -10.5646, 25.4914, -20.5091, 3.6753, 0.],
             [0., -8.9309, 18.9584, -11.6668, -0.2561, 0.],
             [0, -8.1077, 16.7865, -9.6354, -1.2390, 0.],
             [0., -7.3749, 14.5313, -7.4967, -1.9209, 0.],
             [0., 1.7499, -10.1370, 9.4381, 0., 0.]])


# Force Fields for Coarse-Grained Molecular Simulations
# from a Corresponding States Correlation. Mejia et al, 2014
def saft_forcefield(ms, Tc, w, rhol07):
    lambda_a = 6.
    index = np.int(ms-1)
    ai = a[index]
    bi = b[index]
    ci = c[index]
    di = d[index]
    ji = j[index]
    ki = k[index]
    exponent = np.arange(6)

    # Eq 13 lambda_r
    wi = w**exponent
    lambda_r = np.dot(ai, wi) / (1 + np.dot(bi, wi))

    # Eq 14 alpha VdW
    alpha = (lambda_r/(lambda_r-6))*(lambda_r/6)
    alpha **= (6/(lambda_r-6))*(1/3-1/(lambda_r-3))

    # Eq 15 T*c
    alphai = alpha**exponent
    Tc_r = np.dot(ci, alphai) / (1 + np.dot(di, alphai))

    # Eq 16 calculo eps
    eps = Tc / Tc_r * kb

    # Eq 18 rho*c
    rhoc_r = np.dot(ji, alphai) / (1 + np.dot(ki, alphai))

    # Eq 17 calculo sigma
    sigma = (rhoc_r / rhol07 / Na)**(1/3)

    return lambda_r, lambda_a, ms, eps, sigma
