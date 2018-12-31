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
LT\{f(t) \}=\int_0^\infty e^{-st}f(t)dt=F(s)
$$
$$
LT\{\delta(t-t_0) \}=e^{-st_0}
$$
$$
LT\{\delta(t) \}=1
$$
$$
LT\{f'\}=sL\{f\}-f(0)
$$
$$
LT\{f''\}=s^2L\{f\}-sf(0)-f'(0)
$$
$$
LT\{f^{(n)}\}=s^nLT\{f\}-s^{n-1}f(0)-s^{n-2}f'(0)-...-s^0y^{(n-1)}(0)=s^nLT\{f\}-\sum_{i=0}^{n-1} s^{i}f^{(n-1-i)}(0)
$$

