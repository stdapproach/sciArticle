#1 Definition & Terminology
#####Function:
$$
y(t)\text{ - function takes an argument}\in\mathbb{R}\text{ and returns a result}\in\mathbb{R}
$$
#####Derivative:
$$
y'=\frac{dy}{dt}\text{ , }
y''=\frac{d^2y}{dt^2}\text{ , }
y^{(n)}=\frac{d^{n}y}{dt^{n}}\text{ , }
y^{(0)}=y
$$
#####Heaviside step function
$$
H(t)
$$
##### Dirac delta function
$$
\delta(t)=\frac{dH(t)}{dt}
$$
Delta function is a well known mathematical object. The property of it could be found at: Balakumar (p.287), Bottega (p.233), Chasnov (p.62), Finan (p.53), Nagy (p.185), Rao (p.381), Weber (p.86), Zill (p.292), Appendix A this article.

#####Initial Value Problem (IVP), Caushy problem
LTI ODE
$$
L_n(\{a\},y)=\sum_{i=0}^{n} a_iy^{(n-i)}(t)=f(t)\text{ , }a_i=const\in \mathbb{R}\text{ , }i\in 0\ldots n\tag{1.1}
$$
and initial conditions (IC)
$$
    \{y\}|_{t_0}=IC|_{t_0}=\left\{
    \begin{matrix}
    y(t_0)\\
    y'(t_0)\\
    y''(t_0)\\
    \vdots \\ 
    y^{(n-1)}(t_0)\\ 
    \end{matrix}\right\}\tag{1.2}
$$
named IVP which has an unique solution y(t) satisfied (1.1) and (1.2)
We use the following 3 equivalence short forms for IVP:
$$
\begin{cases}
L_n(y)=f(t)\\
\{y\}|_{t_0}
\end{cases}
\equiv
\begin{cases}
L_n(\{a\},y)=f(t)\\
IC|_{t_0}=IC_0
\end{cases}
\equiv
IVP(\{a\}, f(t),t_0,IC_0)
$$

##### Impulse Response (IR)
The impulse-response function g(t) is thus the response of a linear time-invariant system to a unit-impulse input when the initial conditions are zero. The Laplace transform of this function gives the transfer function (Ogata p.17).

