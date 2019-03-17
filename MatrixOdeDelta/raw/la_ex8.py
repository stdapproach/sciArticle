#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example8. Lay, p.165'

A = np.array([[1, 5, 0], [2, 4, -1], [0, -2, 0]])
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html
det = la.det(A)
testVal = -2
print("det=", det, "\n testVal=", testVal)
delta = det - testVal
print("delta=", delta)
