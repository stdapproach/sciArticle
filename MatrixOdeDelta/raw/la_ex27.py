#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la
import scipy as sp


title1 = 'Example27. Hirsch, p.97'

A = np.array([[2, 0, -1], [0, 2, 1], [-1, -1, 2]])
#
tstVals_ = np.array([2, 2, 2])
#
tstV1 = np.array([1, -1, 0])
tstV2 = np.array([0, 0, -1])
tstV3 = np.array([1, 0, 0])
tstVecs_ = la.augment(la.augment(tstV1, tstV2), tstV3)
print("tstVecs_=", tstVecs_)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#print("tstVals_=", tstVals_)
#
L, V = la.eig(A)
#
print("Eigenvalues=", L)
tolerance=0.0001
eqVals = la.isEqualEigenVals(tstVals, L, atol = tolerance)
print("tstVals == eigenvalues ->", eqVals, " with atol=", tolerance)
#
print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V, atol = tolerance)
print("tstVecs == Eigenvectors ->", flag, " with atol=", tolerance)
v1 = la.getCol(V, 1);
v2 = la.getCol(V, 2)
print("v1*v2=", la.norm(v1.dot(v2)) )#??
D = V.dot(np.diag(L).dot(la.transpose(V)))#??
print("D=", D)