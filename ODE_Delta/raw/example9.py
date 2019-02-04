import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example9. 3rd order'
va = [1, 2, 2, 0]
vc=0
vb = [1]
IC0 = [0, 0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
	return 0.5-0.5*np.exp(-t)*(np.sin(t)+np.cos(t))
#====================
plt.xkcd()
#Z1 = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
Z1 = hlp.mkSlnT1_c(va, vb, vc, IC0, t0, tb, N)

hlp.showNumSolution3(plt, Z1, y_ex, title1)	
hlp.showPhase3(plt, Z1, title1)
