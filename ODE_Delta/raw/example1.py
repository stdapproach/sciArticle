from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

T = 2.0

title1 = 'Example1'

def y_ex1(t):
	return (1.0/T)*np.exp(-t/T)

va = [T, 1]
b = 1
IC0 = [0]
t0 = 0
tb = 10
N = 100

Z = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
vt = Z[:,0]
vy = Z[:,1]

plt.xkcd()

#hlp.showNumSolution(plt, Z, y_ex, title1)
hlp.showNumSolutionWithError(plt, Z, y_ex1, title1)
#hlp.showPhase(plt, Z, "Phase diagram:"+title1)
