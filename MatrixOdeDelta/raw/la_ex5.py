#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example5. Beezer, p.192'

a = np.array([[2,-3, 4], [1,0, -7]])
b = np.array([[6, 2, -4], [3, 5, 2]])
#
x = a + b
testVal = np.array([[8, -1, 0], [4, 5, -5]])
print("x=", x, "\n testVal=", testVal)
delta = x-testVal
print("delta=", delta)
