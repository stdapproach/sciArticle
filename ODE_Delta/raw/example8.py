from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

import helper as hlp

plt.xkcd()
plt.grid(True)

title1 = 'Example8'
ylabel1 = "y"
title2 = 'Error ' + title1
ylabel2 = "Numerical-Analytical"

va = [1, 2, 2, 0]
c=0
b = 1
N = 100
IC0 = [0, 0, 0]
#====================
stubDiff = hlp.mkDiff_Type1
vt = np.linspace(0, 10, N)
IC1 = hlp.mkIC_Type1(va, b, IC0)
Z1 = odeint(stubDiff, IC1, vt, args=(va,))

def y_ex(t):
	return 0.5-0.5*np.exp(-t)*(np.sin(t)+np.cos(t))
prey = Z1[:,0]
#=====================
plt.subplot(311)
plt.title(title1)
plt.plot(vt, prey, 'bo', markevery=5, color='r', label="Numerical")
plt.plot(vt, y_ex(vt), 'k', markevery=5, color='b', label="Analytical")
plt.xlabel("Time")
plt.ylabel(ylabel1)
plt.legend();

plt.subplot(312)
plt.plot(vt, Z1[:,1], 'k', color='b', label="y'(t)")
plt.xlabel("Time")
plt.ylabel("y'")
plt.legend();

plt.subplot(313)
plt.plot(vt, Z1[:,2], 'k', color='r', label="y''(t)")
plt.xlabel("Time")
plt.ylabel("y''")
plt.legend();

plt.show()

plt.xkcd()
plt.grid(True)
plt.title("Phase diagram:"+title1)
plt.plot(Z1[:,0], Z1[:,1], 'k', color='b', label="y'(y)")
plt.plot(Z1[:,0], Z1[:,2], 'k', color='r', label="y''(y)")
plt.xlabel("y")
plt.ylabel("y', y''")
plt.legend();

def addAnnotate(Z,index, plot):
	cap = "%.2f" % vt[index]
	plt.annotate(
    	't='+cap,
    	xy=(Z[index,0], Z[index,1]))#, arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

addAnnotate(Z1, 0, plt)

indYmax = np.argmax(Z1[:,0])
addAnnotate(Z1, indYmax, plt)
indYmin = np.argmin(Z1[:,0])
addAnnotate(Z1, indYmin, plt)

indYtmax = np.argmax(Z1[:,1])
addAnnotate(Z1, indYtmax, plt)
indYtmin = np.argmin(Z1[:,1])
addAnnotate(Z1, indYtmin, plt)

plt.show()
