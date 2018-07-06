from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

import helper as hlp

print("Hola!")

plt.xkcd()
plt.grid(True)

title1 = 'Example7'
ylabel1 = "y"
title2 = 'Error ' + title1
ylabel2 = "Numerical-Analytical"

#====================
va = [1, 0, 4]
#c=0
b = 1
IC0 = [0, 0]
t0 = 0
tb = 15
N = 100
#====================

def y_ex(t):
	return 0.5*(hlp.heaviside(t-np.pi)-hlp.heaviside(t-2*np.pi))*np.sin(2*t)

vb = [1, -1, 2, 0]
vc = [np.pi, 2.0*np.pi, -np.pi, 2]

a = hlp.mkReducedVcVb(vc, vb)
#print("A=", a)
vcb = a[ (tb>a[:,0]) & (a[:,0]>=t0) ]
#print("A2=", vcb)

n = hlp.rows(vcb)

if n == 0:
	Z = hlp.mkSlnT1_a(va, b, IC0, t0, tb, N)
else:
	Z = hlp.mkSlnT0(va, IC0, t0, vcb[0,0], N)
	for i in range(0, n-1):
		d = np.ndim(Z)
		if d == 1:
			IC_i = Z[1:]
		else:
			IC_i = hlp.extractIC(Z)
		z = hlp.mkSlnT1_b(va, vcb[i,1], vcb[i,0], IC_i, vcb[i,0], vcb[i+1,0], N)
		Z = hlp.stack(Z, z)

	IC_i = hlp.extractIC(Z)
	z = hlp.mkSlnT1_b(va, vcb[n-1,1], vcb[n-1,0], IC_i, vcb[n-1,0], tb, N)
	Z = hlp.stack(Z, z)


hlp.showNumSolution(plt, Z, y_ex, title1)	
hlp.showPhase(plt, Z, title1)
