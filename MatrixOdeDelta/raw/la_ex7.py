#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example7. Malham, p.71'

A = np.array([[1, 1, 3], [2, 1, 1], [1, 3, 5]])
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html
X = la.inv(A)
testVal = np.array([[1/4.0, 1/2.0, -1/4.0], [-9/8.0, 1/4.0, 5/8.0], [5/8.0, -1/4.0, -1/8.0]])
print("X=", X, "\n testVal=", testVal)
#print("ca=", ca)#, "\n testVal=", testVal)
delta = X - testVal
print("delta=", delta)
