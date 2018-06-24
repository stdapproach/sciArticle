#Apendix A
## General formulas
####Unit impulse function (Dirac's function)
$$
\int_{-\infty}^\infty \delta(x-a)f(x) dx=f(a)
$$
$$
\int_{-\infty}^\infty \delta(x-a)dx=\int_{-\infty}^\infty \delta(x)dx=1
$$
$$
\int_{-\infty}^\infty f(x)\delta^{(n)}(x-a)dx=(-1)^nf^{(n)}(a)
$$
$$
\int_{-\infty}^\infty f(x)\delta'(x-a)dx=-f'(a)
$$
$$
\delta(-x)=\delta(x)
$$
$$
\delta(ax)=\frac 1{|a|}\delta(x), a\neq0
$$
$$
x\delta(x)=0
$$
####Laplas transform
$$
L\{f(t) \}=\int_0^\infty e^{-st}f(t)dt
$$
$$
L\{\delta(t-t_0) \}=e^{-st_0}
$$
$$
L\{\delta(t) \}=1
$$
$$
L\{f'\}=sL\{f\}-f(0)
$$
$$
L\{f''\}=s^2L\{f\}-sf(0)-f'(0)
$$
$$
L\{f^{(n)}\}=s^nL\{f\}-s^{(n-1)}f(0)-s^{(n-2)}f'(0)-...-y^{(n-1)}(0)=s^nL\{f\}-\sum_{i=0}^{n-1} s^{(i)}f^{(n-1-i)}(0)
$$

