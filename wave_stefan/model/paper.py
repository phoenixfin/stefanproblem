import numpy as np

from helpers.constants import n, A_n, B_n, epsilon, h, alpha, b

omega = n * np.pi


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
    r = alpha * (b - 2 * gamma_hat()) * gamma_tilde(t) * (1 - xi(x, t))
    u = beta(tau(t)) * np.sin(omega * xi(x, t))
    return u + r


# SUPPORTS
def y_o(x):
    return alpha * x * (beta - x)


def y_n(x, t):
    if x < gamma_n(t):
        return 0
    else:
        return y_hat(x, t) + epsilon * y_tilde(x, t)
