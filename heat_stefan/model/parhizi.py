import numpy as np
from helpers.constants import *
from helpers.grapher import plot_single_s


def get_s(t):
    tn = .5*np.sqrt(7)*((eps*a)**2)*t - np.arctan(1./np.sqrt(7))
    return ((np.sqrt(7)*np.tan(tn)) + 1)/(4*eps*a)

def main(bound, plot=False):
    u = None  # TODO: function for u

    s = np.zeros([nt])
    for n in range(nt):
        s[n] = get_s(n * dt)

    if plot: plot_single_s(s)
    return u, s
