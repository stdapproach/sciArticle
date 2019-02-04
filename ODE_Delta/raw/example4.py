import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example4. Nagy p.189'
va = [1, 2, 2]
c=2.0
b = 1
IC0 = np.array([0, 0])
t0 = 0
tb = 10.0
N = 100
#
plt.xkcd()

def y_ex(t):
	return hlp.heaviside(t-c)*np.exp(-(t-c))*np.sin(t-c)

#Z = hlp.mkSlnT1_b(va, b, c, IC0, t0, tb, N)
Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

hlp.showNumSolution(plt, Z, y_ex, title1)	
hlp.showPhase(plt, Z, title1)
