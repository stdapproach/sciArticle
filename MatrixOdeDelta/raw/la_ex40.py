#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la
import scipy
from scipy.sparse import linalg

title1 = 'Example40. Moler, p.8'
#
A = np.array([[-49, 24], [-64, 31]])
tstMAtr = np.array([[-0.735759, 0.551819], [-1.471518, 1.103638]])
print("A=", A)
#
expA=la.expm(A)
print("exp(A)=", expA)
#
delta = expA-tstMAtr
print("delta=", delta)