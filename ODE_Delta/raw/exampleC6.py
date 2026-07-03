import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = "ExampleC6 [Dobrushkin, p. 342, Ex. 5.4.3] 2ndOrder with d+d'"

va = [1, 2, 5]
vb = [1, 5]
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

def y_ex1_scalar(t):
    if t < 0:
        return 0
    return np.exp(-t) * np.cos(2 * t) + 2 * np.exp(-t) * np.sin(2 * t)

y_ex1 = np.vectorize(y_ex1_scalar)

Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)

hlp.showNumSolutionWithErrorTogether(plt, Z1, y_ex1, title1)
