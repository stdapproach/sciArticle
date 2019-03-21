import numpy as np
#import scipy as np

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

def getCol(A, i):
	return A[:,i]

def sortEig(val, vec):
	#https://stackoverflow.com/questions/8092920/sort-eigenvalues-and-associated-eigenvectors-after-using-numpy-linalg-eig-in-pyt/50562995#50562995
	idx = np.argsort(val)
	val2 = val[idx]
	vec2 = getCol(vec, idx)#vec[:,idx]
	return (val2, vec2)

def eig(A):
	eigenValues, eigenVectors = np.linalg.eig(A)
	return sortEig(eigenValues, eigenVectors)

def transpose(A):
	return np.transpose(A)

def augment(v1, v2):
	return np.column_stack((v1,v2))
	#return np.stack((v1, v2), 1)
	#return np.concatenate((v1, v2), axis=0)

def cols(A):
	return np.size(A, 1)

def rows(A):
	return np.size(A, 0)

def norm(v):
	return np.linalg.norm(v)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / norm(vector)#np.linalg.norm(vector)

def getFirstNonNullItem(v):
	for y in np.nditer(v):
		if y != 0.0:
			return y

	print("QQQ_strange result!")

def positive_normalisation(v):
	first_non_nul = getFirstNonNullItem(v)
	#print("first_non_nul=", first_non_nul, "for v=", v)
	sign = np.sign(first_non_nul)
	return v/sign

def isSame_(v1, v2):
	return np.allclose(v1,v2)

def isEqual(v1, v2, atol=1e-5):
	return np.allclose(v1, v2, atol = atol)

def isEqualEigenVals(v1, v2, atol=1e-5):
	#print("v1.shape=", v1.shape)
	#print("v2.shape=", v2.shape)
	a = sort(v1)
	b = sort(v2)
	return isEqual(v1,v2, atol = atol)

def isEqualVec(v1, v2, atol=1e-5):
	a1 = unit_vector(v1)
	b1 = unit_vector(v2)
	a2 = positive_normalisation(a1)
	b2 = positive_normalisation(b1)
	#print("after norma v1=", a2, " v2=", b2)
	return isEqual(a2, b2, atol=atol)

def checkVecIsEigVec(v, A, atol=1e-5):
	v2 = A.dot(v)
	#check wheter v2 is null-vector
	isNull = not np.count_nonzero(v2)
	if isNull:
		return True#null eigenValue's case

	#print("v=", v, " A*v=", v2)
	return isEqualVec(v, v2, atol=atol)

def getCol(A, i):
	return A[:, i]

def isEqualEigenVecs(V, tstV, atol=1e-5):
	n = cols(V)
	for i in range(0, n):
		v1 = getCol(V, i)
		v2 = getCol(tstV, i)
		pred = isEqualVec(v1, v2, atol=atol)
		#print("v1=", v1, " v2=", v2, " isEqual->", pred)
		if not(pred):
			return False

	return True