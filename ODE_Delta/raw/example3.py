from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#Example2
title1 = 'Example3'
ylabel1 = "y"
title2 = 'Error ' + title1
ylabel2 = "Numerical-Analytical"
a0 = 1
a1 = 2
a2 = 2

N = 100
def D_ex(P, t):
	r = - (a2*P[0]/a0 + a1*P[1]/a0)
	return [P[1], r]

def y_ex(t):
	return np.exp(-t)*np.sin(t)

ts = np.linspace(0, 10, N)
IC = [0, 1]
P = odeint(D_ex, IC, ts)
prey = P[:,0]

plt.xkcd()
#plt.subplot(211)
plt.title(title1)
plt.plot(ts, prey, 'bo', markevery=5, color='r', label="Numerical")
plt.plot(ts, y_ex(ts), 'k', markevery=5, color='b', label="Analytical")
plt.xlabel("Time")
plt.ylabel(ylabel1)
plt.legend();

#plt.subplot(212)
#plt.title(title2)
#plt.plot(ts, prey-y_ex1(ts), 'k', color='b', label="An")
#plt.xlabel("Time")
#plt.ylabel(ylabel2)

plt.grid(True)
plt.show()

plt.title("Phase diagram:"+title1)
plt.plot(P[:,0], P[:,1], 'k', color='b', label="Analytical")
#plt.plot(P[:,0], , 'bo', markevery=5, color='r', label="Numerical")
plt.xlabel("y")
plt.ylabel("y'")

def addAnnotate(index, plot):
	cap = "%.2f" % ts[index]
	plt.annotate(
    	't='+cap,
    	xy=(P[index,0], P[index,1]))#, arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

addAnnotate(0, plt)

indYmax = np.argmax(P[:,0])
addAnnotate(indYmax, plt)
indYmin = np.argmin(P[:,0])
addAnnotate(indYmin, plt)


plt.show()
