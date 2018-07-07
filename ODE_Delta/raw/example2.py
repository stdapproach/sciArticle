import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example2'

def y_ex(t):
	return 0.25*np.exp(-t)*np.sin(2*t)

va = [2, 4, 10]
b = 1
c = 0
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

#Z = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

plt.xkcd()

hlp.showNumSolutionWithError(plt, Z, y_ex, title1)
hlp.showPhase(plt, Z, title1)
