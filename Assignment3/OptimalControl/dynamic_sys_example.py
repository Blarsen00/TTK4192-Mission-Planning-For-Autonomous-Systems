import numpy as np
import matplotlib.pyplot as pyplot
import casadi as cas

x = cas.MX.sym('x', 2)

z = 1-x[1]**2
rhs = cas.vertcat(z*x[0]-x[1], x[0])

ode = {}
ode['x'] = x
ode['ode'] = rhs

F = cas.integrator('F', 'cvodes', ode, 0, 4)

res = F(x0=[0,1])
print(res["xf"])

res = F(x0=x)
S = cas.Function('S', [x], [cas.jacobian(res["xf"], x)])
print(S([0,1]))
