#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example6. Lay, p.103'

a = np.array([[2, 5], [-3, -7]])
c = np.array([[-7, -5], [3, 2]])
#
ac=np.dot(a,c)
ca=np.dot(c,a)
#testVal = np.array([[1, 0], [0, 1]])
print("ac=", ac)#, "\n testVal=", testVal)
print("ca=", ca)#, "\n testVal=", testVal)
delta = ac-ca
#print("delta=", delta)
