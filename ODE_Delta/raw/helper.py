#helper
import numpy as np
from scipy.integrate import odeint
from numpy import c_
from numpy import r_
import sympy

def foo():
	return "HW"

def mkMatrA(va):
	n = np.size(va,0)
	r = np.zeros( (n-1, n-1) )
	for i in range(1, n):
		for j in range(0, i):
			r[i-1,j] = va[i-1-j]

	return r

def mkVecD_Type1(b, va):
	n = np.size(va,0)-1
	r = np.zeros((n))
	r[n-1] = b
	return r


def mkDeltaIC_Type1(va, b):
	A = mkMatrA(va)
	d = mkVecD_Type1(b, va)
	r = np.linalg.solve(A,d)
	return r

def mkDiff_Type1(P, t, va):
	n = np.size(va,0)
	if 2==n:
		r = -1.0*(va[1]/va[0])*P[0]
		return [r]
	if 3==n:
		iMax = n-2
		r = 0
		for i in range(0, iMax+1):#!! only for second ODE
				r += -P[i]*va[iMax+1-i]/va[0]
		return [P[1], r]
	if 4==n:
		iMax = n-2
		r = 0
		for i in range(0, iMax+1):
				r += -P[i]*va[iMax+1-i]/va[0]
		return [P[1], P[2], r]	

def mkIC_Type1(va, b, IC0):
	deltaIC = mkDeltaIC_Type1(va, b)
	IC = IC0 + deltaIC
	return IC

def augment(v1,v2):
	r = c_[v1, v2]
	return r

def stack(v1,v2):
	r = r_[v1, v2]
	return r		

def mkSlnT0(va, IC0, t0, tb, N):
	diff = mkDiff_Type1
	vt = np.linspace(t0, tb, N)
	Z = odeint(diff, IC0, vt, args=(va,))
	R = augment(vt, Z)
	return R


def mkSlnT1_a(va, b, IC0, t0, tb, N):
	IC = mkIC_Type1(va, b, IC0)
	diff = mkDiff_Type1
	vt = np.linspace(t0, tb, N)
	Z = odeint(diff, IC, vt, args=(va,))
	R = augment(vt, Z)
	return R

def lastRow(Z):
	return Z[-1]

def extractIC(Z):
	lr = lastRow(Z)
	ic = lr[1:]
	return ic

def mkZrowByIC(t, IC):
	R = r_[t, IC]
	return R

def mkSlnT1_b(va, b, c, IC0, t0, tb, N):
	if t0 == tb:
		return mkZrowByIC(t0, IC0)

	if (c<t0) or (c>=tb):
		Z0 = mkSlnT0(va, IC0, t0, tb, N)
		return Z0

	if t0 == c:
		Z = mkSlnT1_a(va, b, IC0, t0, tb, N)
		return Z

	Z1 = mkSlnT0(va, IC0, t0, c, N)
	IC1_ = extractIC(Z1)
	IC1 = mkIC_Type1(va, b, IC1_)
	Z2 = (mkZrowByIC(c, IC1) if c == tb else mkSlnT0(va, IC1, c, tb, N))
	Z = stack(Z1, Z2)
	return Z

def sortByColumn(A, cIndex):
	ind = np.argsort( A[:,cIndex] ); 
	r = A[ind]
	#r = sorted(A, key=lambda a_entry: a_entry[cIndex]) 
	return r

def rows(A):
	d = np.ndim(A)
	if d == 1:
		return 1;
	#print("QQQ_1, ", np.shape(A)[0])
	r = np.shape(A)[0]
	return r

def cols(A):
	return np.shape(A)[1]	

def mkReducedVcVb(vc, vb):
	vcvb = augment(vc, vb)
	vcb = sortByColumn(vcvb, 0)
	r = np.array(vcb[0])
	#
	n = rows(vcb)
	print("vcb=", vcb)
	print("r=", r)
	#return r
	#
	if n == 1:
		print("QQQ_1")
		return r
	j = 0
	#
	for i in range(1, n):
		#
		if rows(r) == 1:
			#
			if r[0] == vcb[i,0]:
				r[1] += vcb[i][1]
			else:
				nr = np.array([vcb[i,0], vcb[i,1]])
				#r = stack(r, nr)
				#print("QQQ_1_2, r=", r, ", nr=", nr)
				r = np.vstack((r, nr))
				j += 1
				#print("QQQ_1_3, r=", r, " rows(r)=", rows(r))
		else:
			print("QQQ_2, r=", r)
			if r[j,0] == vcb[i,0]:
				r[j][1] += vcb[i][1]
				
			else:
				#print("QQQ_3, r=", r)
				j += 1
				nr = np.array([vcb[i,0], vcb[i,1]])
				print("i=", i, " nr=", nr)
				r = np.vstack((r, nr))
	return r



#=========================
def showSimpleChart(plt, Z, indX, indY, title=""):
	plt.title(title)
	plt.plot(Z[:,indX], Z[:,indY], 'bo', markevery=5, color='r', label="Numerical")
	plt.show()

def showNumSolution(plt, Z, fy_an, title):
	plt.title(title)
	vt = Z[:,0]
	vy = Z[:,1]
	plt.plot(vt, vy, 'bo', markevery=5, color='r', label="Numerical")
	plt.plot(vt, fy_an(vt), 'k', markevery=5, color='b', label="Analytical")
	plt.xlabel("Time")
	plt.ylabel("y(t)")
	plt.legend();
	plt.grid(True)
	plt.show()

def addAnnotate(Z,index, plot):
	cap = "%.2f" % Z[index,0]
	plot.annotate(
    	't='+cap,
    	xy=(Z[index,1], Z[index,2]))

def addAnnotationToPhase(Z, plt):
	addAnnotate(Z, 0, plt)
	indYmax = np.argmax(Z[:,1])
	addAnnotate(Z, indYmax, plt)
	indYmin = np.argmin(Z[:,1])
	addAnnotate(Z, indYmin, plt)
	indYtmax = np.argmax(Z[:,2])
	addAnnotate(Z, indYtmax, plt)
	indYtmin = np.argmin(Z[:,2])
	addAnnotate(Z, indYtmin, plt)

def showPhase(plt, Z, title):
	plt.title("Phase diagram:"+title)
	plt.plot(Z[:,1], Z[:,2], 'k', color='b', label="Numerical")
	plt.xlabel("y")
	plt.ylabel("y'")

	addAnnotationToPhase(Z, plt)
	plt.legend();
	plt.grid(True)

	plt.show()

def showNumSolution3(plt, Z, fy_an, title):
	plt.subplot(311)
	vt = Z[:,0]
	vy = Z[:,1]
	vy_t = Z[:,2]
	vy_t2 = Z[:,3]
	plt.plot(vt, vy, 'bo', markevery=5, color='r', label="Numerical")
	plt.title(title)
	plt.plot(vt, fy_an(vt), 'k', markevery=5, color='b', label="Analytical")
	plt.xlabel("Time")
	plt.legend();
	plt.grid(True)

	plt.subplot(312)
	plt.plot(vt, vy_t, 'k', color='b', label="y'(t)")
	plt.xlabel("Time")
	plt.ylabel("y'")
	plt.legend();
	plt.grid(True)

	plt.subplot(313)
	plt.plot(vt, vy_t2, 'k', color='r', label="y''(t)")
	plt.xlabel("Time")
	plt.ylabel("y''")
	plt.legend();
	plt.grid(True)

	plt.show()

def showPhase3(plt, Z, title):
	plt.title("Phase diagram: "+title)
	plt.plot(Z[:,1], Z[:,2], 'k', color='b', label="y'(y)")
	plt.plot(Z[:,1], Z[:,3], 'k', color='r', label="y''(y)", dashes=[6, 2])
	plt.xlabel("y")
	plt.ylabel("y'")

	addAnnotationToPhase(Z, plt)
	plt.legend();
	plt.grid(True)

	plt.show()

def showNumSolutionWithError(plt, Z, fy_an, title):
	plt.subplot(211)
	plt.title(title)
	vt = Z[:,0]
	vy = Z[:,1]
	plt.plot(vt, vy, 'bo', markevery=5, color='r', label="Numerical")
	plt.plot(vt, fy_an(vt), 'k', markevery=5, color='b', label="Analytical")
	plt.ylabel("y(t)")
	plt.legend();
	plt.grid(True)

	plt.subplot(212)
	vt = Z[:,0]
	vy = Z[:,1]
	plt.plot(vt, vy-fy_an(vt), 'k', markevery=5, color='r', label="Error")
	plt.xlabel("Time")
	plt.ylabel("error(t)")
	plt.legend();
	plt.grid(True)
	plt.show()

#Make heaviside "theta" function
def heaviside(x):
    return 1.0 * (x > 0.0)
