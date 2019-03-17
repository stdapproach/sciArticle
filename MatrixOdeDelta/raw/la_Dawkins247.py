#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Dawkins, p.247'

a = np.array([[1, -2, 1], [-1, 1, -2], [2, -1, 3]])
b = np.array([-2, 3, -7])
x = la.lsolve(a, b)
testVal = np.array([0, 0, 0])
flag = la.checkLEsolution(a, testVal, b)
print("x=", x, " testVal=", testVal, " isOK_solution=", flag)
print("rank(A)=", la.rank(a))
delta = x-testVal
print("delta=", delta)
