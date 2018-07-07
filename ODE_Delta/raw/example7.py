import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

plt.xkcd()
plt.grid(True)

title1 = 'Example7'
ylabel1 = "y"

#====================
va = [1, 0, 4]
#c=0
b = 1
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100
#====================

def y_ex(t):
	return 0.5*(hlp.heaviside(t-np.pi)-hlp.heaviside(t-2*np.pi))*np.sin(2*t)

vb = [1, -1, 2, 0]
vc = [np.pi, 2.0*np.pi, -np.pi, 2]

Z2 = hlp.mkSlnT1_c(va, vb, vc, IC0, t0, tb, N)

hlp.showNumSolution(plt, Z2, y_ex, title1)	
hlp.showPhase(plt, Z2, title1)
