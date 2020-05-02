import numpy as np
import matplotlib.pyplot as plt
from constants import nt, dt, nx, dx

def plot_complete(U, s, points, title, bound, save=None):    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    fig.set_size_inches(13.5, 5.5)

    ax1.plot(np.arange(nt)*dt, s)
    ax1.plot(ts*dt, s[ts],'o')
    ax1.set_ylabel("Interface location")
    ax1.set_xlabel("Time")
    ax1.set_title("Moving Boundary Profile")    
    ax1.grid(which='both')

    # ts = list(np.arange(0, 100, 10))
    ax2.plot(np.arange(nx+1)*dx, U[:,0],label='t=0')
    strt = 0 if bound == "Dirichlet" else 1
    for n in points[1:]:
        t = round(n*dt, 2)
        ax2.plot(np.arange(nx+1-strt)*dx, U[strt:,n], label='t='+str(t))

    ax2.set_ylabel("Temperature")
    ax2.set_xlabel("Location")
    ax2.set_title("Temperature Profile")

    ax2.grid(which='both')
    ax2.legend()
    if save:
        fig.savefig(save, dpi=100)
    plt.show()

def plot_u(U, points, save=None):
    ts = np.array([0, round(nt/100), round(nt/2), nt-1])    