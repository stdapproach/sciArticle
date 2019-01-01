import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

T = 2.0

title1 = 'Example1'

def y_ex1(t):
	return (1.0/T)*(1-np.exp(-t*T))

va = [1, T, 0]
b = 1
c = 0
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

plt.xkcd()

#hlp.showNumSolution(plt, Z, y_ex, title1)
#print(Z)
hlp.showNumSolutionWithError(plt, Z, y_ex1, title1)
#hlp.showPhase(plt, Z, "Phase diagram:"+title1)
