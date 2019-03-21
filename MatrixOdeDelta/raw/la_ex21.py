#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example11. Sen, p.288'

A = np.array([[1, -1], [0, 1]])
#A = np.array([[1, 1], [0, 1]])
tstVals_ = np.array([1, 1])
tstV1 = np.array([1, 0])
tstV2 = np.array([0, -1])
tstVecs_ = la.augment(tstV1, tstV2)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#
L, V = la.eig(A)
#
print("Eigenvalues=", L)
print("Eigenvectors=", V)
tolerance=0.0001
eqVals = la.isEqualEigenVals(tstVals, L, atol = tolerance)
print("tstVals == eigenvalues ->", eqVals, " with atol=", tolerance)
#
#print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V, atol = tolerance)
print("tstVecs == Eigenvectors ->", flag, " with atol=", tolerance)

v1 = la.getCol(V, 0);
v2 = la.getCol(V, 1)
print("v1*v2=", la.norm(v1.dot(v2)) )#??