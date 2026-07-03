import matplotlib.pyplot as plt
import numpy as np

import helper as hlp

title1 = 'ExampleC2 [Adkins, p. 435] 2ndOrder'

def y_ex1_scalar(t):
    cmn = (1 / 10) * np.cos(np.sqrt(20) * t)
    if t < 0:
        return 0
    if t < 3:
        return cmn
    return cmn + (1 / np.sqrt(20) * np.sin(np.sqrt(20) * (t - 3)))

y_ex1 = np.vectorize(y_ex1_scalar)

va = [1, 0, 20]
b = 1  # impulse value
c = 3  # time for impulse
IC0 = [0.1, 0]  # x0, vx0
t0 = 0
tb = 10
N = 200

Z = hlp.mkSlnT1_c(va, b, c, IC0, t0, tb, N)

hlp.showNumSolutionWithErrorTogether(plt, Z, y_ex1, title1)
Z0 = hlp.mkZrowByIC(t0, IC0)
