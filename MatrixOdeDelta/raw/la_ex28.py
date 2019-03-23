#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la


title1 = 'Example27. Laub, p.37'

A = np.array([[1, 1], [2, 2], [2, 2]])
#
U, D, V = np.linalg.svd(A)
print("U=", U)
print("D=", D)
print("V=", V)
#