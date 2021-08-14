from model import develop, paper
import numpy as np
from matplotlib import pyplot as plt


def plot_u():
    ts = np.arange(0, 2, 0.2)
    xs = np.arange(0, 1, 0.0001)
    obstacle = np.array([max(0., develop.y_o(x)) for x in xs])
    for t in ts:
        ys1 = np.array([develop.u_n(x, t) for x in xs])
        ys2 = np.array([paper.y_n(x, t) for x in xs])
        plt.plot(xs, ys1, '.', markersize=1., color='blue', label=round(t, 2))
        plt.plot(xs, ys2, '.', markersize=1., color='red', label=round(t, 2))
    plt.plot(xs, obstacle)
    plt.xlabel("t")
    plt.ylabel("u")
    plt.grid()
    # plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_u()
