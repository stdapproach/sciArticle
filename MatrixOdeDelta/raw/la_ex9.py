#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example9. Beezer, p.395'

A = np.array([[3, 2, -1], [4, 1, 6], [-3, -1, 2]])
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html
det = la.det(A)
testVal = -27
print("det=", det, "\n testVal=", testVal)
delta = det - testVal
print("delta=", delta)
