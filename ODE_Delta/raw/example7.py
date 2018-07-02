from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

import helper as hlp

plt.xkcd()
plt.grid(True)

title1 = 'Example7'
ylabel1 = "y"
title2 = 'Error ' + title1
ylabel2 = "Numerical-Analytical"

#====================
va = [1, 2, 2]
#c=0
b = 1
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100
#====================
Z = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
hlp.showSimpleChart(plt, Z, 0, 1, "QQQ")


def y_ex(t):
	return 0.5*(np.heaviside(t-np.pi,1)-np.heaviside(t-2*np.pi,1))*np.sin(2*t)

#ts1 = np.linspace(0, c, N)
#ts2 = np.linspace(c, 15, N)
#ts = np.concatenate((ts1, ts2), axis=0)

#IC2 = [0, 4]

#Z1 = odeint(D_ex, IC1, ts1)
#IC2 = Z1[-1,:] + np.transpose(deltaIC1)
#print(IC2)
#Z2 = odeint(D_ex, IC2, ts2)
#Z = np.concatenate((Z1, Z2), axis=0)
#prey = Z[:,0]
