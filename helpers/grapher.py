import numpy as np
import matplotlib.pyplot as plt
from helpers.constants import nt, dt, nx, dx

default_info = {
    "s": {
        "title" : "Moving Boundary Profile",
        "ylabel" : "Interface location",
        "xlabel" : "Time"
    },
    "u" : {
        "title" : "Temperature Profile",
        "ylabel" : "Temperature",
        "xlabel" : "Location"
    }
}

def setup(info, ax=None):
    obj = ax if ax else plt
    for attr in info:
        meth = 'set_'+attr if ax else attr 
        getattr(obj, meth)(info[attr])
    obj.grid(which='both')
    obj.legend()
    if not ax: plt.show()
    
def plot_both(U, s, points, title, bound, save=None):    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    fig.set_size_inches(13.5, 5.5)

    ax1.plot(np.arange(nt)*dt, s)
    ax1.plot(points*dt, s[points],'o')

    ax2.plot(np.arange(nx+1)*dx, U[:,0],label='t=0')
    strt = 0 if bound == "Dirichlet" else 1
    for n in points[1:]:
        t = round(n*dt, 2)
        ax2.plot(np.arange(nx+1-strt)*dx, U[strt:,n], label='t='+str(t))

    setup(default_info['s'], ax1)
    setup(default_info['u'], ax2)
    
    if save:
        fig.savefig(save, dpi=100)
    plt.show()

def plot_single_u(U, points):
    ax2.plot(np.arange(nx+1)*dx, U[:,0],label='t=0')
    strt = 0 if bound == "Dirichlet" else 1
    for n in points[1:]:
        t = round(n*dt, 2)
        ax2.plot(np.arange(nx+1-strt)*dx, U[strt:,n], label='t='+str(t))

    setup(default_info['u'])
    
def plot_single_s(s):
    plt.plot(np.arange(nt)*dt, s)
    setup(default_info['s'])

def plot_compare_s(*args):
    for data in args:
        s, label = data
        print(label)
        print(s)
        plt.plot(np.arange(nt)*dt, s, label=label)
    setup(default_info['s'])