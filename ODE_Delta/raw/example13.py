import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example13. W(s)=(s+d)/[s(s+a)(s+b)]'
a = 1
b = 2
d = 1.5
va = [1, a+b, a*b, 0]
vc=0
vb = [1, d]
IC0 = [0, 0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
	return (1/(a*b))*(d-(b*(d-a)/(b-a))*np.exp(-a*t)+(a*(d-b)/(b-a))*np.exp(-b*t))
#====================
plt.xkcd()
#Z1 = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)

hlp.showNumSolutionWithError(plt, Z1, y_ex, title1)
#hlp.showNumSolution(plt, Z1, y_ex, title1)
Z0 = hlp.mkZrowByIC(t0, IC0)
Z2 = hlp.stack(Z0, Z1)
hlp.showPhase(plt, Z2, title1)
