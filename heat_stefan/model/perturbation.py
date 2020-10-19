from numpy import sqrt, zeros

from helpers.constants import *
from helpers.grapher import plot_single_s

def get_s(t, bound):
    if bound == "Neumann":    
        return b+eps*a*t
    elif bound == "Dirichlet":
        return sqrt(b**2 + 2*eps*a*t)

def main(bound, plot=False):
    u = None #TODO: function for u
    
    s = zeros([nt])
    for n in range(nt):
        s[n] = get_s(n*dt, bound)
    
    if plot: plot_single_s(s)
    return u, s

        
        