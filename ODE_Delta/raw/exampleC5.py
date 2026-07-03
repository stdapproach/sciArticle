import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'ExampleC5 [Campbell, p. 263] 1stOrder with shift'

def y_ex1_scalar(t):
    if t < 0:
        return 0
    if t < 1:
        return np.exp(-t)
    return np.exp(-t) * (np.exp(1) + 1)

y_ex1 = np.vectorize(y_ex1_scalar)

va = [1, 1]
b = 1
c = 1
IC0 = [1]
t0 = 0
tb = 10
N = 100

Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

hlp.showNumSolutionWithErrorTogether(plt, Z, y_ex1, title1)
