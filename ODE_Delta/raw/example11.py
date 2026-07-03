import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'Example11. W(s)=s/[(s+a)(s+b)]'
a = 1
b = 2
va = [1, a + b, a * b]
vb = [1, 0]
IC0 = [0, 0]
t0 = 0
tb = 10
N = 100

def y_ex(t):
    return (1 / (a - b)) * (a * np.exp(-a * t) - b * np.exp(-b * t))

Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)

hlp.showNumSolutionWithErrorTogether(plt, Z1, y_ex, title1)
Z0 = hlp.mkZrowByIC(t0, IC0)
Z2 = hlp.stack(Z0, Z1)
hlp.showPhase(plt, Z2, title1)
