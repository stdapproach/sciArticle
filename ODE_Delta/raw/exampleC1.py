import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'ExampleC1 [Asadi, p.62] 2ndOrder'
va = [1, 6, 100]
vc=0
vb = [100]
IC0 = [0, 0]
t0 = 0
tb = 2
N = 1000

Z1 = hlp.mkSlnT2_a(va, vb, IC0, t0, tb, N)
hlp.showNumSolution(plt, Z1, None, title1)
