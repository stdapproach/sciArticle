#from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import helper as hlp
#from numpy import c_

title1 = 'Example5'
va = [1, 0, 1]
c=2*np.pi
b = 4
IC0 = np.array([1, 0])
t0 = 0
tb = 15.0
N = 100
#
plt.xkcd()

def y_ex(t):
	return hlp.heaviside(t-c)*4*np.sin(t)+np.cos(t)

Z = hlp.mkSlnT1_b(va, b, c, IC0, t0, tb, N)

hlp.showNumSolution(plt, Z, y_ex, title1)	
hlp.showPhase(plt, Z, title1)
