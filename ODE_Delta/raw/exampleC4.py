import matplotlib.pyplot as plt
import numpy as np
import helper as hlp

title1 = 'ExampleC4 [Boyce, p. 346] 2ndOrder with damping and shift'

va = [2, 1, 2]  # left side
c = 5
vb = 1  # right side
IC0 = [0, 0]  # x0, vx0
t0 = 0
tb = 20
N = 100

Z1 = hlp.mkSlnT1_c(va, vb, c, IC0, t0, tb, N)
hlp.showNumSolutionWithErrorTogether(plt, Z1, None, title1)
