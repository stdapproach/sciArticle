import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example14. W(s)=(s+a)/(s^2+w^2)'
a = 1.5
w = 0.7
va = [1, 0, w*w]
#vc=0
vb = [1, a]
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
	return (np.sqrt(a*a+w*w)/w)*np.sin(w*t+np.arctan(w/a))
#====================
plt.xkcd()
#Z1 = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)

hlp.showNumSolutionWithError(plt, Z1, y_ex, title1)
#hlp.showNumSolution(plt, Z1, y_ex, title1)	
Z0 = hlp.mkZrowByIC(t0, IC0)
Z2 = hlp.stack(Z0, Z1)
hlp.showPhase(plt, Z2, title1)
