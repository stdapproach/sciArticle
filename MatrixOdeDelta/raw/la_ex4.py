#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example4. Lay, p.95'

a = np.array([[2,3], [1,-5]])
b = np.array([[4, 3, 6], [1,-2,3]])
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html
x = np.dot(a,b)
testVal = np.array([[11, 0, 21], [-1, 13, -9]])
print("x=", x, "\n testVal=", testVal)
delta = x-testVal
print("delta=", delta)
