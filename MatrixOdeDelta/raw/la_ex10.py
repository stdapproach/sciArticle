#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example10. Hirsch, p.31'

A = np.array([[1, 3], [1, -1]])
tstVals_ = np.array([2, -2])
tstV1 = np.array([3, 1])
tstV2 = np.array([1, -1])
tstVecs_ = la.augment(tstV1, tstV2)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#print("tstVecs=", tstVecs)
#
#eigVals = la.eigvals(A)
#print("eigVals=", eigVals)
#
L, V = la.eig(A)
#print("eigVals_=", L)
#print("eigVecs_=", V)
#a = la.getFirstNonNullItem(np.array([1, -2]))
#b = la.positive_normalisation(np.array([0, -1, -2]))
#print("b=", b)
#
print("Eigenvalues=", L)
eqVals = la.isEqualEigenVals(tstVals, L)
print("tstVals == eigenvalues ->", eqVals)
#
#eqVec1 = la.isEqualVec(tstVecs[:,0], V[:,0])
#eqVec2 = la.isEqualVec(tstVecs[:,1], V[:,1])
#print("eqVec1 ?= eigVecs[1]->", eqVec1)
#print("eqVec2 ?= eigVecs[2]->", eqVec2)
#
#B = np.array([[1, 3, 0], [1, -1, -10]])
#print("cols=", la.cols(B))
#print("B[2]=", B[:, 2])
#
print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V)
print("tstVecs == Eigenvectors ->", flag)