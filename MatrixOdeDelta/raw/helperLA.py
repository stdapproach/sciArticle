import numpy as np

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html

def lsolve(A, b):
	return np.linalg.solve(A, b)

def inv(A):
	return np.linalg.inv(A)

def det(A):
	return np.linalg.det(A)

def checkLEsolution(A, x, b):
	return np.allclose(np.dot(A, x), b)

def rank(A):
	return np.linalg.matrix_rank(A)