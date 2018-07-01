#helper
import numpy as np

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
		return r
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
