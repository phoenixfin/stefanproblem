from numpy import sqrt, exp, pi, arange
from scipy.special import erf, erfc
from scipy.integrate import solve_ivp

from constants import c_1, c_2, K_1, K_2, T_m, b, \
    L, rho, l, t0, nx, nt, dx, dt

eps = c_1/L
a = 0.1

def s_t(t, s):
    ex = 2*exp(-s**2/(4*t))*sqrt(t)
    er = s*sqrt(pi)*erf(s/(2*sqrt(t)))
    return (eps*a*ex/(ex+er))

def get_s(start, end, step):
    evals = arange(start, end, step)
    res = solve_ivp(s_t, [start,end], [1], t_eval=evals)
    return res

# def get_u(x,t):
#     c_1 = ...
#     c_2 = -eps*a
#     return c_2*x-c_1(exp(-x**2/(4*t))*sqrt(t)+sqrt(pi)*x*erf(x/(2*sqrt(t))))

def main():
    from matplotlib import pyplot as plt
    res = get_s(0, 10, 0.1)
    plt.plot(res.t, res.y[0])
    plt.show()
