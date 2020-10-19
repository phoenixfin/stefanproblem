    for t in ts:
        ys = np.array([u_n(x, t) for x in xs])
        plt.plot(xs, ys)