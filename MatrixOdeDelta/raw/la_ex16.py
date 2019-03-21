#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example16. Hirsch, p.85'

A = np.array([[1, 2, -1], [0, 3, -2], [0, 2, -2]])
tstVals_ = np.array([2, 1, -1])
print("tstVals_=", tstVals_)
tstV1 = np.array([3, 2, 1])
tstV2 = np.array([1, 0, 0])
tstV3 = np.array([0, 1, 2])
tstVecs_ = la.augment(la.augment(tstV1, tstV2), tstV3)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#
L, V = la.eig(A)
#
print("Eigenvalues=", L)
tolerance=0.0000001
eqVals = la.isEqualEigenVals(tstVals, L, atol = tolerance)
print("tstVals == eigenvalues ->", eqVals, " with atol=", tolerance)
#
#print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V, atol = tolerance)
print("tstVecs == Eigenvectors ->", flag, " with atol=", tolerance)