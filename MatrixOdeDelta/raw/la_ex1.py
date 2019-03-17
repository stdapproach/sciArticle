#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example1. Lay p.5'

a = np.array([[1,-2,1], [0,2,-8], [-4, 5, 9]])
b = np.array([0, 8, -9])
x = la.lsolve(a, b)
testVal = np.array([29, 16, 3])
print("x=", x, ", testVal=", testVal)
delta = x-testVal
flag = la.checkLEsolution(a, testVal, b)
print("isOKsolution=", flag, ", delta=", delta)
