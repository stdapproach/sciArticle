#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example3. Malham, p.62'

a = np.array([[3,2,1], [2,1,1], [6, 2, 4]])
b = np.array([3, 0, 6])
x = la.lsolve(a, b)
#testVal = np.array([1, 2, 3])
#this system has no solution
print("x=", x)
#delta = x-testVal
#flag = la.checkLEsolution(a, testVal, b)
#print("isOKsolution=", flag, ", delta=", delta)
