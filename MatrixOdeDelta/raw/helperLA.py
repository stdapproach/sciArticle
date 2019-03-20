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

def eigvals(A):
	return np.linalg.eigvals(A)

def sort(v):
	idx = np.argsort(v)
	res = v[idx]
	return res

def sortEig(val, vec):
	#eigenValues, eigenVectors = np.linalg.eig(A)
	idx = np.argsort(val)
	val2 = val[idx]
	vec2 = vec[:,idx]
	return (val2, vec2)

def eig(A):
	eigenValues, eigenVectors = np.linalg.eig(A)
	return sortEig(eigenValues, eigenVectors)
	#idx = np.argsort(eigenValues)
	#eigenValues = eigenValues[idx]
	#eigenVectors = eigenVectors[:,idx]
	#return (eigenValues, eigenVectors)

def transpose(A):
	return np.transpose(A)

def augment(v1, v2):
	return np.stack((v1, v2), 1)

def cols(A):
	return np.size(A, 1)

def rows(A):
	return np.size(A, 0)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def getFirstNonNullItem(v):
	for y in np.nditer(v):
		if y != 0.0:
			return y

def positive_normalisation(v):
	first_non_nul = getFirstNonNullItem(v)
	sign = np.sign(first_non_nul)
	return v/sign

def isSame_(v1, v2):
	return np.allclose(v1,v2)

def isEqualEigenVals(v1, v2):
	a = sort(v1)
	b = sort(v2)
	return np.allclose(a,b)

def isEqualVec(v1, v2):
	a1 = unit_vector(v1)
	b1 = unit_vector(v2)
	a2 = positive_normalisation(a1)
	b2 = positive_normalisation(b1)
	return np.allclose(a2,b2)

def getCol(A, i):
	return A[:, i]

def isEqualEigenVecs(V, tstV):
	n = cols(V)
	for i in range(0, n):
		v1 = getCol(V, i)
		v2 = getCol(tstV, i)
		pred = isEqualVec(v1, v2)
		if not(pred):
			return False

	return True