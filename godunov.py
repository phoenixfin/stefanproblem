import numpy as np

from constants import *
from plot import plot

U_m = 0
U_ = c_1*T_m/L
beta = K_2/K_1
gamma = c_2/c_1
eps = c_1/L
b = 3.


print(dt, dx, gamma)

def get_kappa(U_in):
    left_melt = (U_in > U_m)
    right_melt = (U_in > U_m)
    if left_melt:
        if right_melt:
            return 1.
        else:
            return (2.*beta)/(1.+beta)
    else:
        return beta

def get_q(U_n, i):
    kap = get_kappa(U_n[i])
    return -kap*(U_n[i+1] - U_n[i])/dx

def get_E(E_in, q_n, i):
    # if n<=1:
    #     print(i, n, q_n[i], q_n[i+1], E_in)
    return E_in + (dt/dx)*(q_n[i]-q_n[i+1])

def get_E_init(U_0):
    dif_U = (U_0-U_m)
    if dif_U <= 0:
        return gamma*dif_U
    else:
        return dif_U + 1

def get_s(E_n):
    x = 0
    for i, e in enumerate(E_n):
        if e <= 0:
            lam = 0.
        elif e >= 1:
            lam = 1.
        else:
            lam = e
        x += dx*(lam)
    # if n == 1 and abs(x-b)>= dx:
    #     x -= dx
    return x

def get_U(E_in):
    if E_in <= 0:
        return U_m + E_in/gamma
    elif E_in >= 1:
        return U_m + E_in - 1
    else:
        return U_m

def F(x, typ):
    up = 0.1
    if x >= b: return U_m
    if typ == 'none':
        return U_m
    elif typ == 'constant':
        return U_m + 5*up
    elif typ == 'linear':
        return U_m + 5*up*(1.- x/b)
    elif typ == 'parabolic':
        return U_m + up*(10/18)*(x-b)**2

bound_types = ['Dirichlet', 'Neumann', 'Robin']
init_types = ['none','constant', 'linear', 'parabolic']

def main(bound_ops, init_ops):
    bound = bound_types[bound_ops]
    init = init_types[init_ops]
    koef = 0.1

    U = np.zeros([nx+1, nt])
    E = np.zeros([nx, nt])
    q = np.zeros([nx+1, nt])
    s = np.zeros([nt])

    # Initial condition
    for i in range(nx):
        U[i+1, 0] = F((i+1)*dx, init)        
        E[i, 0] = get_E_init(U[i, 0])
        q[i, 0] = get_q(U[:, 0], i)
    s[0] = b if init != 'none' else 0

    # Boundary condition
    for n in range(nt):
        q[nx, n] = 0.
        if bound == 'Dirichlet':
            U[0, n] = U_m + 5*koef
            q[0, 0] = get_q(U[:, 0], 0)            
        elif bound == 'Neumann':
            U[0, 0] = F(0, init)
            q[0, n] = koef
        elif bound == 'Robin':
            U[0, 0] = F(0, init)
            q[0, 0] = 5*koef*(U[0,0] + 0.2)
        E[0, 0] = get_E_init(U[0, 0])

    # Main iterations
    for n in range(nt-1):
        if n<=3:
            print(n,'\n', U[:, n],'\n', E[:, n],'\n', q[:, n])

        if bound != "Dirichlet":
            U[0, n+1] = get_U(E[0,n])
        if bound == "Robin":
            q[0, n+1] = 5*koef*(U[0, n+1] + 0.2)
        for i in range(nx):
            if i != nx-1:
                U[i+1, n+1] = get_U(E[i,n])
            E[i, n+1] = get_E(E[i,n], q[:,n], i)
            if bound == 'Dirichlet' or i>0:
                q[i, n+1] = get_q(U[:,n], i)
        U[nx, n+1] = U[nx-1, n+1]
        s[n+1] = get_s(E[:,n+1])

    # plotting
    case = bound+'-type Boundary Case'
    save = bound+'_'+init+'.png'

    plot(U, s, case, save)

if __name__ == "__main__":
    for j in range(3):
        for j1 in range(3):
            main(j, j1)