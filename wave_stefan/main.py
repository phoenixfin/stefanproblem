A_p = 1.5
L = 10.
B = 2.
H_r = 1.

n = 2

alpha = A_p * L**2 / H_r
beta = B/L
epsilon = 0.001
print("alpha={}, beta={}".format(alpha, beta))

A_n = 50
B_n = 0

import numpy as np
from matplotlib import pyplot as plt

def tau(t):
    return t/gamma_hat()

def phi_n(t):
    return A_n * np.sin(B_n + n*np.pi*tau(t))

def gamma_hat():
    return np.sqrt(1. - beta - 1./alpha)

def gamma_n_tilde(t):
    return (-1)**(n+1) * n * np.pi * phi_n(t) / (2. * alpha * gamma_hat())

def gamma_n(t):    
    return gamma_hat() + epsilon * gamma_n_tilde(t)

def xi(x, t):
    return (1. - x) / gamma_n(t)

def H_n(x, t):
    nom = (-1)**n * n * np.pi * (1. - x) * (2. * (1.- gamma_hat()) - beta)
    denom = 2. * gamma_hat() * gamma_n(t)
    return -nom/denom
    
def psi_n(x, t):
    return np.sin(n * np.pi * (1. - x) / gamma_n(t))

def u_hat(x, t):
    # a = alpha * gamma_hat() * (beta - 2. * (1. - gamma_hat()))
    a = 1. - alpha * (1 - gamma_hat()) * (beta - (1 - gamma_hat()))
    c = 1.
    return c - a * xi(x, t)

def u_n_tilde(x, t):
    # return 0
    return phi_n(t) * (psi_n(x, t) + H_n(x, t))

def u_n(x, t):
    if x < 1 - gamma_n(t):
        return 0
    else:
        return u_hat(x, t) + epsilon * u_n_tilde(x, t)

def Y_o(x):
    return alpha * x * (beta - x)

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

def plot_u():
    ts = np.arange(0, 1, 0.1)
    xs = np.arange(0, 1, 0.0001)
    obstacle = np.array([max(0., Y_o(x)) for x in xs])
    for t in ts:
        ys = np.array([u_n(x, t) for x in xs])
        plt.plot(xs, ys, label = round(t,2))
    plt.plot(xs, obstacle)
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_u()