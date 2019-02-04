import matplotlib.pyplot as plt
import numpy as np
import helper as hlp
import math

title1 = 'Example5. Chasnov p.65'
va = [2, 1, 2]
c = 5.0
b = 1
IC0 = np.array([0, 0])
t0 = 0
tb = 20.0
N = 100
#
plt.xkcd()

def y_ex(t):
	return (2/math.sqrt(15.0))*hlp.heaviside(t-c)*np.exp(-(t-c)/4.0)*np.sin(math.sqrt(15.0)*(t-c)/4.0)

#Z = hlp.mkSlnT1_b(va, b, c, IC0, t0, tb, N)
Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

#hlp.showNumSolution(plt, Z, y_ex, title1)
hlp.showNumSolutionWithError(plt, Z, y_ex, title1)	
hlp.showPhase(plt, Z, title1)
