from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example8'
va = [1, 2, 2, 0]
#c=0
b = 1
IC0 = [0, 0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
	return 0.5-0.5*np.exp(-t)*(np.sin(t)+np.cos(t))
#====================
plt.xkcd()
Z1 = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)

hlp.showNumSolution3(plt, Z1, y_ex, title1)	
hlp.showPhase3(plt, Z1, title1)
