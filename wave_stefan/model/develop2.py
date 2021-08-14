import numpy as np

from wave_stefan.helpers.constants import n, A_n, B_n, epsilon, h, alpha, b

omega = n * np.pi
DIRICHLET = "DIRICHLET"
NEUMANN = "NEUMANN"
ROBIN = "ROBIN"
BC = ""

# VARS
def tau(t):
    return t


def xi(x, t):
    return (x - gamma_n(t)) / (1 - gamma_n(t))


def beta(tau):
    return A_n * np.sin(B_n + (omega) ** 2 * tau / (1 - gamma_hat()))


def gamma_n(t):
    return gamma_hat() + epsilon * gamma_tilde(t)


def gamma_hat():
    return 1 - np.sqrt(1 + h - b)


def gamma_tilde(t):
    return (-1. / (2 * alpha * (1 - gamma_hat()))) * omega * beta(tau(t))


def y_hat(x, t):
    c1 = alpha * gamma_hat() * (b - gamma_hat())
    c0 = h - c1
    return c0 * xi(x, t) + c1


def y_tilde(x, t):
    if BC == DIRICHLET:
        r = 0
    elif BC == NEUMANN:
        r = n * np.pi * (1 - xi(x,t))
    elif BC == ROBIN:
        temp1 = omega * (b - 2 * gamma_hat())
        temp2 = 2 * (3 * gamma_hat() - b +1)
        temp3 = xi(x, t) - 1 + 2 * np.cos(omega)
        r = -(temp1 / temp2) * temp3
    u = np.sin(omega * xi(x, t))
    return beta(tau(t))(u + r)


# SUPPORTS
def y_o(x):
    return alpha * x * (beta - x)


def y_n(x, t):
    if x < gamma_n(t):
        return 0
    else:
        return y_hat(x, t) + epsilon * y_tilde(x, t)
