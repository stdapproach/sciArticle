import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example5'
va = [1, 0, 1]
c=2*np.pi
b = 4
IC0 = np.array([0, 0])
t0 = 0
tb = 15.0
N = 100
#
plt.xkcd()

def y_ex(t):
	return hlp.heaviside(t-c)*4*np.sin(t)

#Z = hlp.mkSlnT1_b(va, b, c, IC0, t0, tb, N)
Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

hlp.showNumSolution(plt, Z, y_ex, title1)	
hlp.showPhase(plt, Z, title1)
