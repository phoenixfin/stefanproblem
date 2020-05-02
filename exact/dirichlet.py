from numpy import sqrt, exp, pi, zeros
from scipy.special import erf, erfc
from scipy.optimize import fsolve

from plot import plot
from constants import c_1, c_2, K_1, K_2, T_m, eps, \
    L, rho, l, t0, nx, nt, dx, dt

a = 10.

def get_alpha():
    def falpha(x):
        return eps*a*exp(-x**2)-2*x*sqrt(pi)*erf(x)
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

def main():
    u = zeros([nx+1, nt])
    s = zeros([nt])
    for n in range(nt):
        s[n] = get_s(n*dt)
        for i in range(nx+1):
            u[i, n] = get_u(i*dx, n*dt)
    
    plot(u, s, "Exact", "Dirichlet")
