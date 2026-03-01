import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = "[Dobrushkin: p.342, Ex.5.4.5] 3rdOrder with d+d'+d''"

va = [1, 3, 9, -13]
vc=0
vb = [2, 6, 10]
IC0 = [0, 0, 0]
t0 = 0
tb = 2
N = 100

def y_ex1_scalar(t):
    if t<0:
        return 0
    return np.exp(t)+ np.exp(-2*t)*np.cos(3*t)+(1/3)*np.exp(-2*t)*np.sin(3*t)

y_ex1 = np.vectorize(y_ex1_scalar)

Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)

hlp.showNumSolutionWithErrorTogether(plt, Z1, y_ex1, title1)
