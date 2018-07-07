import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example3'
va = [1, 2, 2]
b = 1
c = 0
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
	return np.exp(-t)*np.sin(t)

#Z = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

plt.xkcd()

#hlp.showNumSolution(plt, Z, y_ex, title1)
hlp.showNumSolutionWithError(plt, Z, y_ex, title1)
hlp.showPhase(plt, Z, title1)
