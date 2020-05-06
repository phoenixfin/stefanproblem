from . import dirichlet, neumann

def main(bound):
    return getattr(globals()[bound.lower()], 'main')()