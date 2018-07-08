#1 Definition & Terminology
Function
$$
y(t)\text{ - function takes an argument}\in\mathbb{R}\text{ and returns a result}\in\mathbb{R}
$$
Derivative:
$$
y'=\frac{dy}{dt}\text{ , }
y''=\frac{d^2y}{dt^2}\text{ , }
y^{(n)}=\frac{d^{n}y}{dt^{n}}\text{ , }
y^{(0)}=y
$$
Dirac delta function
$$
\delta(t)
$$
Heaviside step function
$$
H(t)
$$
#####Initial Value Problem (IVP), Caushy problem
Differential equation (linear differential equation with constant coefficients, ODE_LC)
$$
\sum_{i=0}^{n} a_iy^{(n-i)}=f(t)\text{ , }a_i=const\in \mathbb{R}\text{ , }i\in 0\ldots n\tag{1}
$$
and initial conditions (IC)
$$
\begin{matrix}
y_0=y(t_0)\\
y_1=y'(t_0)\\
y_2=y''(t_0)\\
\ldots\\
y_{n-1}=y^{(n-1)}(t_0)
\end{matrix}
\tag2
$$
named IVP which has an unique solution y(t) satisfied (1) and (2)
$$
$$
We often use the following 3 equivalence short forms for IVP:
$$\begin{cases}
\sum_{i=0}^n a_iy^{(n-i)}(t)=f(t)\\
\{y\}|_{t_0}
\end{cases}
\equiv
\begin{cases}
L_n(y)=f(t)\\
\{y\}|_{t_0}
\end{cases}
\equiv
\begin{cases}
L_n(\{a\},y)=f(t)\\
IC|_{t_0}=IC_0
\end{cases}
$$

