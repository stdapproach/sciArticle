from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

T = 2

def D_ex1(P, t):
	r = -P[0]/T
	return [(r)]

def y_ex1(t):
	return (1.0/T)*np.exp(-t/T)

ts = np.linspace(0, 10, 100)
IC = [0.5]
P = odeint(D_ex1, IC, ts)
prey = P[:,0]

plt.xkcd()
plt.subplot(211)
plt.title('Example1')
plt.plot(ts, prey, 'bo', markevery=5, color='r', label="Numerical")
plt.plot(ts, y_ex1(ts), 'k', markevery=5, color='b', label="Analytical")
plt.xlabel("Time")
plt.ylabel("y_ex1")
plt.legend();

plt.subplot(212)
plt.title('Error Example1')
#plt.plot(ts, prey-y_ex1(ts), 'bo', markevery=5, color='r', label="Num")
plt.plot(ts, prey-y_ex1(ts), 'k', color='b', label="An")
plt.xlabel("Time")
plt.ylabel("Num_ex1-An_ex1")


plt.grid(True)
plt.show()
#-------------------------------------

#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)

#plt.figure(1)
#plt.subplot(211)
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()