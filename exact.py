from numpy import sqrt, exp, pi, zeros
from scipy.special import erf, erfc
from scipy.optimize import fsolve

from plot import plot
from constants import c_1, c_2, K_1, K_2, T_m, \
    L, rho, l, t0, nx, nt, dx, dt

T_S = 350.
T_L = 250.

a_1 = K_1/(rho*c_1)
a_2 = K_2/(rho*c_2)

St_1 = c_1*(T_S-T_m)/L
St_2 = c_2*(T_L-T_m)/L

v = sqrt(a_2/a_1)

def get_lambda():
    def flambda(x):
        p1 = St_1/(exp((v*x)**2)*erf(v*x))
        p2 = St_2/(exp(x**2)*erf(x))
        return p2-p1-x*sqrt(pi)
    return fsolve(flambda, 0.1)[0]
    
lambd = get_lambda()

print(lambd, a_2)
def get_s(t):
    return lambd*sqrt(2*a_1*t)

def get_T(x,t):    
    s = get_s(t)


    if x<=s:
        T = T_S + (T_m - T_S) * erf(x/sqrt(2*a_2*t))/erf(lambd)
    else:
        T = T_L + (T_m - T_L) * erfc(x/sqrt(2*a_1*t))/erfc(lambd*v)
    return T

if __name__ == "__main__":
    T = zeros([nx+1, nt])
    s = zeros([nt])
    for n in range(nt):
        s[n] = get_s(n*dt)
        for i in range(nx+1):
            T[i, n] = get_T(i*dx, n*dt)
    
    plot(T, s, "Exact", "Dirichlet")