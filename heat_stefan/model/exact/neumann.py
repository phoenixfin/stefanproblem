from numpy import sqrt, exp, pi, arange
from scipy.special import erf
from scipy.integrate import solve_ivp

from helpers.constants import *
from helpers.grapher import plot_single_s

def s_t(t, s):
    ex = 2*exp(-s**2/(4*t))*sqrt(t)
    er = s*sqrt(pi)*erf(s/(2*sqrt(t)))
    return (eps*a*ex/(ex+er))

def get_s(start, end, step):
    evals = arange(start, end, step)
    res = solve_ivp(s_t, [start,end], [0.0001], t_eval=evals)
    return res

def similarity():
    res = solve_ivp(s_t, [0,T], [0.0001], t_eval=evals1)
    return res

# def get_u(x,t):
#     c_1 = ...
#     c_2 = -eps*a
#     return c_2*x-c_1(exp(-x**2/(4*t))*sqrt(t)+sqrt(pi)*x*erf(x/(2*sqrt(t))))

def main(plot=False):
    res = get_s(0, t0, dt)
    s = res.y[0]
    if plot: plot_single_s(s)

    u = None # TODO: function for u
    
    return u, s