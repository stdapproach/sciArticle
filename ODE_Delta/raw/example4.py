from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#Example2
title1 = 'Example4'
ylabel1 = "y"
title2 = 'Error ' + title1
ylabel2 = "Numerical-Analytical"
a0 = 1
a1 = 2
a2 = 2
c=2
N = 100
def D_ex(P, t):
	r = - (a2*P[0]/a0 + a1*P[1]/a0)
	return [P[1], r]

def y_ex(t):
	return np.heaviside(t-c,1)*np.exp(-(t-c))*np.sin(t-c)

ts1 = np.linspace(0, c, N)
ts2 = np.linspace(c, 10, N)
ts = np.concatenate((ts1, ts2), axis=0)
IC1 = [0, 0]
IC2 = [0, 1]

Z1 = odeint(D_ex, IC1, ts1)
Z2 = odeint(D_ex, IC2, ts2)
Z = np.concatenate((Z1, Z2), axis=0)
prey = Z[:,0]

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
plt.plot(Z[:,0], Z[:,1], 'k', color='b', label="Analytical")
#plt.plot(P[:,0], , 'bo', markevery=5, color='r', label="Numerical")
plt.xlabel("y")
plt.ylabel("y'")

def addAnnotate(Z,index, plot):
	cap = "%.2f" % ts[index]
	plt.annotate(
    	't='+cap,
    	xy=(Z[index,0], Z[index,1]))#, arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

addAnnotate(Z, 0, plt)

indYmax = np.argmax(Z[:,0])
addAnnotate(Z, indYmax, plt)
indYmin = np.argmin(Z[:,0])
addAnnotate(Z, indYmin, plt)

indYtmax = np.argmax(Z[:,1])
addAnnotate(Z, indYtmax, plt)
indYtmin = np.argmin(Z[:,1])
addAnnotate(Z, indYtmin, plt)

plt.show()
