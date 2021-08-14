import numpy as np
from matplotlib import pyplot as plt
from helpers.constants import n, A_n, B_n, epsilon, h, alpha, b

h = h/epsilon

# VARS
def tau(t):
    return t / gamma_hat()


def xi(x, t):
    return (1. - x) / gamma_n(t)


# EIGENS
def phi_n(t):
    return A_n * np.sin(B_n + n * np.pi * tau(t))


def psi_n(x, t):
    return np.sin(n * np.pi * (1. - x) / gamma_n(t))


# GAMMA
def gamma_hat():
    return np.sqrt(1. - b)


def gamma_tilde(t):
    denom = (2. * alpha * gamma_hat())
    return (h + (-1) ** (n + 1) * n * np.pi * phi_n(t))/ denom


def gamma_n(t):
    return gamma_hat() + epsilon * gamma_tilde(t)


# SUPPORTS
def y_o(x):
    return alpha * x * (b - x)


# U
def u_hat(x, t):
    # a = alpha * gamma_hat() * (beta - 2. * (1. - gamma_hat()))
    a = alpha * (1 - gamma_hat()) * (b - (1 - gamma_hat()))
    c = 0.
    return c + a * xi(x, t)


def u_tilde(x, t):
    # return 0
    coef = (2 * (1 - gamma_hat()) - b) / (2 * gamma_hat())
    p = coef * xi(x, t)

    H_n = (-1)**n * n * np.pi * p
    osc = phi_n(t) * (psi_n(x, t) - H_n)
    stat = h * (p + 1. - xi(x, t))
    return osc + stat


def u_n(x, t):
    if x < 1 - gamma_n(t):
        return 0
    else:
        return u_hat(x, t) + epsilon * u_tilde(x, t)


def plot_gamma():
    ts = np.arange(0, 3, 0.005)
    gamma = []
    gamhat = [gamma_hat()] * len(ts)
    for t in ts:
        gamma.append(gamma_n(t))
    plt.plot(ts, gamma)
    plt.plot(ts, gamhat)
    plt.grid()
    plt.legend()
    plt.show()

