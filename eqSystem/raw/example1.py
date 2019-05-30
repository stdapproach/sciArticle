import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('../../ODE_Delta/raw')

import helper as hlp

T1 = .1
x10 = T1*2

title1 = 'Example1'

def y_ex1(t):
	return T1*(np.exp(-t*T1))

va1 = [1, T1]
IC10 = [x10]
t0 = 0
tb = 10
N = 100
#
T2 = 0.5
x20 = T2*3
va2 = [1, T2]
IC20 = [x20]
#
K2 = T2/T1
C2 = x10/x20
#
Z1 = hlp.mkSlnT0(va1, IC10, t0, tb, N)
Y1 = hlp.mkSlnT0(va2, IC20, t0, tb, N)
Y2 = Y1
x2 = Y2[:,0]
y2 = Y2[:,1]
t21 = np.linspace(0, tb/K2, N)
Y2[:,1] = C2*np.interp(t21, x2, y2)

plt.xkcd()



def showNumSol(plt, Z1, Z2, fy_an, title):
	plt.subplot(211)
	plt.title(title)
	vt1 = Z1[:,0]
	vy1 = Z1[:,1]
	vt2 = Z2[:,0]
	vy2 = Z2[:,1]
	plt.plot(vt1, vy1, 'bo', markevery=5, color='r', label="y1")
	plt.plot(vt2, vy2, 'k', markevery=5, color='b', label="y2")
	plt.ylabel("y(t)")
	plt.legend();
	plt.grid(True)

	plt.subplot(212)
	vt = Z1[:,0]
	vy = Z1[:,1]
	plt.plot(vt, vy-vy2, 'k', markevery=5, color='b', label="Error")
	plt.ylabel("Error")
	plt.legend();
	plt.grid(True)

	plt.show()

showNumSol(plt, Z1, Y2, y_ex1, title1)