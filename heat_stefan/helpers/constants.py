# physical constants
c_1 = 4.1868
c_2 = 1.7
K_1 = 0.0006
K_2 = 0.00266
T_m = 273.
L = 333.73
rho = 1000.

# problem domain
l = 5.
T = 20.
a = 40.
b = 0.1

# scaled parameter
U_m = 0.
U_ = c_1*T_m/L
beta = K_2/K_1
gamma = c_2/c_1
eps = c_1/L
zeta = K_1/(c_1*l**2*rho)
t0 = T

# discretization
nx = 100
nt = 100000
dx = l/nx
dt = t0/nt

print(dt/dx)
print(eps)