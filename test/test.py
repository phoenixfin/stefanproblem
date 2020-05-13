
from model import numerics, exact, perturbation
from helpers.grapher import plot_compare_s 

bound_types = ['Dirichlet', 'Neumann', 'Robin']
init_types = ['none','constant', 'linear', 'parabolic']
method = ['exact', 'numerics', 'perturbation']

def compare_all_method(typ):    
    bound = bound_types[typ]
    args = []
    for meth in method:
        func = getattr(globals()[meth], "main")
        u, s = func(bound)
        args.append((s,meth))
    plot_compare_s(*args, save = bound+'_compare.png')

def compare_with_init(typ, typ2):
    bound = bound_types[typ]
    init = init_types[typ2]
    from helpers import constants
    constants.b = 1.
    
    _, s1 = numerics.main(bound, init)
    _, s2 = perturbation.main(bound)
    args = [(s1, 'numerics'),(s2, 'perturbation')]
    plot_compare_s(*args, save = bound+'_compare_with_init_{}.png'.format(init))
    
def exact_run(typ):
    exact.main(bound_types[typ])

def numerics_run(typ):
    numerics.main(bound_types[typ])
    
def perturbation_run(typ):
    perturbation.main(bound_types[typ])
    
def compare_numerics_all_init():
    for j in bound_types:
        for j1 in init_types:
            numerics.main(j, j1)

            