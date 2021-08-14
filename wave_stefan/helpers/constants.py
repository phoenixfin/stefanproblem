A_p = 0.5
L = 10.
B = 1.
H_r = 0.01

A_n = 1.
B_n = 0
n = 1

alpha = (A_p * L**2)
b = B / L
epsilon = 0.01
h = H_r / L

print("alpha={}, beta={}, h={}".format(alpha, b, h))

BC = "DIRICHLET"
def get_BC():

    return BC

def set_BC(cond):
    global BC
    BC = cond
