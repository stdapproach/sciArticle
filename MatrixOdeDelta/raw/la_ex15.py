#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example15. Genta, p.104'

A = np.array([[20, -10, 0], [-2.5, 3.5, -1], [0, -8, 8]])
tstVals_ = np.array([1.0166**2, 3.0042**2, 4.6305**2])
print("tstVals_=", tstVals_)
tstV1 = np.array([0.45913, 0.87081, 1])
tstV2 = np.array([0.11677, 0.12815, -1])
tstV3 = np.array([1, -0.14412, 0.08578])
tstVecs_ = la.augment(la.augment(tstV1, tstV2), tstV3)
tstVals, tstVecs = la.sortEig(tstVals_, tstVecs_)
#
L, V = la.eig(A)
#
print("Eigenvalues=", L)
tolerance=0.0001
eqVals = la.isEqualEigenVals(tstVals, L, atol = tolerance)
print("tstVals == eigenvalues ->", eqVals, " with atol=", tolerance)
#
#print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V, atol = tolerance)
print("tstVecs == Eigenvectors ->", flag, " with atol=", tolerance)