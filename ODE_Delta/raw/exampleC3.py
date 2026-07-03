import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'ExampleC3 [Angeles, p. 132] 2ndOrder with doublet, i.e. d(delta)/dt'

w = 2 * np.pi
va = [1, 0, w * w]  # left side
vb = [1, 0]  # right side
IC0 = [0, 0]  # x0, vx0
t0 = 0
tb = 3
N = 100

def y_ex1_scalar(t):
    if t < 0:
        return 0
    return np.cos(w * t)

y_ex1 = np.vectorize(y_ex1_scalar)

Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)
hlp.showNumSolutionWithErrorTogether(plt, Z1, y_ex1, title1)
