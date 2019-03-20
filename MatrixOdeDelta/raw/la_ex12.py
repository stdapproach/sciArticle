#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example12. Nagy, p.220'

A = np.array([[1, 2], [2, 1]])
tstVals_ = np.array([3, -1])
tstV1 = np.array([1, 1])
tstV2 = np.array([-1, 1])
tstVecs_ = la.augment(tstV1, tstV2)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#
L, V = la.eig(A)
#
print("Eigenvalues=", L)
eqVals = la.isEqualEigenVals(tstVals, L)
print("tstVals == eigenvalues ->", eqVals)
#
print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V)
print("tstVecs == Eigenvectors ->", flag)