from numpy import sqrt, exp, pi, zeros, array
from scipy.special import erf, erfc
from scipy.optimize import fsolve

from helpers.grapher import plot_both
from helpers.constants import *


def get_alpha():
    def falpha(x):
        return eps*a*exp(-x**2)-x*sqrt(pi)*erf(x)
    return fsolve(falpha, 0.1)[0]
    
alpha = get_alpha()

def get_s(t):
    return 2*alpha*sqrt(t)

def get_u(x,t):    
    s = get_s(t)

    if x<=s:
        u = eps*a*(1-erf(x/(2*sqrt(t)))/erf(alpha))
    else:
        u = 0.
    return u

def main(plot = False):
    u = zeros([nx+1, nt])
    s = zeros([nt])
    for n in range(nt):
        s[n] = get_s(n*dt)
        for i in range(nx+1):
            u[i, n] = get_u(i*dx, n*dt)
    ts = array([0, round(nt/100), round(nt/2), nt-1])    
    if plot: plot_both(u, s, ts, "Exact", "Dirichlet")
    
    return u, s
