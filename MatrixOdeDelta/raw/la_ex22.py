#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example22. Sen, p.287'

A = np.array([[0, -2], [2, 0]])
#
tstVals_ = np.array([2j, -2j])
tstV1 = np.array([1j, 1])
tstV2 = np.array([-1j, 1])
tstVecs_ = la.augment(tstV1, tstV2)
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