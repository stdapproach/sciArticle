#import matplotlib.pyplot as plt
import numpy as np
import helperLA as la
import scipy
from scipy.sparse import linalg

title1 = 'Example41. Kwon, p.6'
#
A = np.array([[0.2190, 0.6793, 0.5194], [0.0470, 0.9347, 0.8310], [0.6789, 0.3835, 0.0346]])
print("A=", A)
#
expA=la.expm(A)
print("exp(A)=", expA)
#
#delta = expA-tstMAtr
#print("delta=", delta)