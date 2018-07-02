from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import helper as hlp
#==============================
from numpy import c_
#==============================

title1 = 'Example8'
va = [1, 2, 2, 0]
c=2
b = 1
IC0 = np.array([1, 0, 0])
t0 = 0
tb = 10
N = 100
#
a = hlp.mkSlnT1_b(va, b, c, IC0, t0, t0, N)
print(a)

a0 = 1
a1 = 2
a2 = 2

def D_ex(P, t):
	r = - (a2*P[0]/a0 + a1*P[1]/a0)
	return [P[1], r]

def y_ex(t):
	return np.heaviside(t-c,1)*np.exp(-(t-c))*np.sin(t-c)

ts1 = np.linspace(0, c, N)
ts2 = np.linspace(c, 10, N)
ts = np.concatenate((ts1, ts2), axis=0)
IC1 = [0, 0]
IC2 = [0, 1]

Z1 = odeint(D_ex, IC1, ts1)
Z2 = odeint(D_ex, IC2, ts2)
Z = np.concatenate((Z1, Z2), axis=0)
prey = Z[:,0]

R = c_[ts, Z]

#hlp.showNumSolution(plt, R, y_ex, title1)	
#hlp.showPhase(plt, R, title1)
