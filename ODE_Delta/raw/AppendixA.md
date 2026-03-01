## Appendix A

#### General Formulas
| Dirac Delta Function 1 | Laplace Transform |
|----------|----------|
| $ \int_{-\infty}^\infty \delta(x-a)f(x)\,dx = f(a) $   | $ \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt = F(s) $   |
| $ \int_{-\infty}^\infty \delta(x-a)\,dx = \int_{-\infty}^\infty \delta(x)\,dx = 1 $   | $ \mathcal{L}\{\delta(t-t_0)\} = e^{-st_0} $   |
| $ \int_{-\infty}^\infty f(x)\,\delta^{(n)}(x-a)\,dx = (-1)^n f^{(n)}(a) $   | $ \mathcal{L}\{\delta(t)\} = 1 $   |
| $ \int_{-\infty}^\infty f(x)\,\delta'(x-a)\,dx = -f'(a) $   | $ \mathcal{L}\{f'\} = s\mathcal{L}\{f\} - f(0) $   |
| $ \delta(-x) = \delta(x) $   | $ \mathcal{L}\{f''\} = s^2\mathcal{L}\{f\} - s f(0) - f'(0) $   |
