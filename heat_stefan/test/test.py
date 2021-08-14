
from model import numerics, exact, perturbation
from helpers.grapher import plot_compare_s, plot_compare_e

bound_types = ['Dirichlet', 'Neumann', 'Robin']
init_types = ['none','constant', 'linear', 'parabolic']
method = ['exact', 'numerics', 'perturbation']

def compare_all_method(typ):    
    compare_methods(typ, method)

def compare_methods(typ, meths):
    bound = bound_types[typ]
    argss = []
    argsu = []
    for meth in meths:
        func = getattr(globals()[meth], "main")
        u, s = func(bound)
        argss.append((s,meth))
        # argsu.append((u,meth))        
    plot_compare_s(*argss, save = bound+'_compare.png')    
    # plot_compare()

def compare_with_init(typ, typ2):
    bound = bound_types[typ]
    init = init_types[typ2]
    from helpers import constants
    constants.b = 1.
    
    _, s1 = numerics.main(bound, init)
    _, s2 = perturbation.main(bound)
    args = [(s1, 'numerics'),(s2, 'perturbation')]
    plot_compare_s(*args, save = bound+'_compare_with_init_{}.png'.format(init))

def compare_init(typ):
    bound = bound_types[typ]    
    _, s1 = numerics.main(bound, 'constant')
    _, s2 = numerics.main(bound, 'linear')
    args = [(s1, 'constant'),(s2, 'linear')]
    plot_compare_s(*args, save = bound+'_compare_init.png')

def compare_perturbation_bound():
    args = []
    for bound in bound_types[:-1]:
        _, s = perturbation.main(bound)
        args.append((s,bound))
    plot_compare_s(*args, save = bound+'_compare_bound.png')

def exact_run(typ):
    exact.main(bound_types[typ])

def numerics_run(typ):
    numerics.main(bound_types[typ])
    
def perturbation_run(typ):
    perturbation.main(bound_types[typ])

def exact_plot(typ):
    exact.main(bound_types[typ], plot=True)


def numerics_plot(typ):
    numerics.main(bound_types[typ], plot=True)


def perturbation_plot(typ):
    perturbation.main(bound_types[typ], plot=True)

def compare_numerics_all_init():
    for j in bound_types:
        for j1 in init_types:
            numerics.main(j, j1)

def compare_differences(typ):
    bound = bound_types[typ]
    _, s = perturbation.main(bound)
    _, s1 = numerics.main(bound)
    _, s2 = exact.main(bound)

    args = [((s-s1), 'Numerics result difference'),
            ((s-s2), 'Exact result difference')]
    plot_compare_e(*args, save='error_compare_bound.png')