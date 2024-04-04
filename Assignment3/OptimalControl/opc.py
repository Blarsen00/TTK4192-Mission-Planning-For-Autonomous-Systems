import numpy as np
from casadi import *

T = 10.0    # Time hoizon
N = 20      # Number of control intervals

# Decalre system variables
x = MX.sym('x')
y = MX.sym('y')
theta = MX.sym('theta')
eta = vertcat(x, y, theta)

# Declare the control variables
v = MX.sym('v')
psi = MX.sym('psi')
u = vertcat(v, psi)

# Model equations
xdot = vertcat(
        v*np.cos(theta),
        v*np.sin(theta),
        v*psi)

# The objective function
L = -v**2 - theta**2

#Fixed step Runge-Kutta 4 integrator
M = 4
DT = T/N/M
f = Function('f', [x,u], [xdot, L])
X0 = MX.sym('x0', 3)
U = MX.sym('U')
X = X0
Q = 0
for j in range(M):
    k1, k1_q = f(X, U)
    k2, k2_q = f(X + DT/2 * k1, U)
    k2, k3_q = f(X + DT/2 * k2, U)
    k4, k4_q = f(X + DT * k3, U)
    X=X+DT/6*(k1 +2*k2 +2*k3 +k4)
    Q = Q + DT/6*(k1_q + 2*k2_q + 2*k3_q + k4_q)
F = Function('F', [X0, U], [X, Q], ['x0', 'p'], ['xf', 'qf'])


