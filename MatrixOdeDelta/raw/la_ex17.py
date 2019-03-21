#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example16. Kwon, p.7'

A = np.array([[5, 3, 2], [1, 4, 6], [9, 7, 2]])
tstVals_ = np.array([12.5361, 1.7486, -3.2847])
#print("tstVals_=", tstVals_)
tstV1 = np.array([0.4127, 0.5557, 0.7217])
tstV2 = np.array([0.5992, -0.7773, 0.1918])
tstV3 = np.array([0.0459, -0.6388, 0.7680])
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
print("Eigenvectors=", V)
flag = la.isEqualEigenVecs(tstVecs, V, atol = tolerance)
print("tstVecs == Eigenvectors ->", flag, " with atol=", tolerance)