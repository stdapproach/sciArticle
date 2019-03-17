#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example2. Malham, p.58'

a = np.array([[2,3,-1], [4,4,-3], [2, -3, 1]])
b = np.array([5, 3, -1])
x = la.lsolve(a, b)
testVal = np.array([1, 2, 3])
print("x=", x, " testVal=", testVal)
delta = x-testVal
flag = la.checkLEsolution(a, testVal, b)
print("isOKsolution=", flag, ", delta=", delta)
