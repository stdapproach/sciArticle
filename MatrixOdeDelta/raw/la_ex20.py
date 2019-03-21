#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example16. Kwon, p.7'

A = np.array([[204, 98, -26, -10], [-280, -134, 36, 14], [716, 348, -90, -36], [-472, -232, 60, 28]])
#
x = np.array([1, -1, 2, 5])
y = np.array([-3, 4, -10, 4])
z = np.array([-3, 7, 0, 8])
w = np.array([1, -1, 4, 0])
#
tolerance=0.0001
print("x=", x, "is EigVec?->", la.checkVecIsEigVec(x, A, atol=tolerance), " with atol=", tolerance)
print("y=", y, "is EigVec?->", la.checkVecIsEigVec(y, A, atol=tolerance), " with atol=", tolerance)
print("z=", z, "is EigVec?->", la.checkVecIsEigVec(z, A, atol=tolerance), " with atol=", tolerance)
print("w=", w, "is EigVec?->", la.checkVecIsEigVec(w, A, atol=tolerance), " with atol=", tolerance)
