#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example23. Beezer, p.423??'

A = np.array([[-13, -8, -4], [12, 7, 4], [24, 16, 7]])
#
tstVals_ = np.array([3, -1, -1])
tstV1 = np.array([-1, 1, 2])??
tstV2 = np.array([-2, 3, 0])
tstV3 = np.array([-1, 0, 3])
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