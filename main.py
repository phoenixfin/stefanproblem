
from model import numerics, exact, perturbation
from helpers.grapher import plot_compare_s 

bound_types = ['Dirichlet', 'Neumann', 'Robin']
init_types = ['none','constant', 'linear', 'parabolic']
method = ['exact', 'numerics', 'perturbation']

if __name__ == "__main__":
    # for j in bound_types:
    #     for j1 in init_types:
    #         numerics.main(j, j1)

    # exact.main("Dirichlet")
    # numerics.main("Dirichlet")
    # perturbation.main("Dirichlet")

    args = []
    for meth in method:
        func = getattr(locals()[meth], "main")
        u, s = func("Dirichlet")
        args.append((s,meth))
    plot_compare_s(*args)
    