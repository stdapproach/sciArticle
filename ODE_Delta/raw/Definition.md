#1 Definition & Terminology
Function
$$
y,y(t)\text{ - function takes an argument}\in\mathbb{R}\text{ and returns a result}\in\mathbb{R}
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
Initial Value Problem (IVP), Caushy problem
===
The initial value problem (IVP) for a first order linear ODE is the following: Given constant a_i and constants $t_0$, y_0, find a function y solution of
$$
y'= a(t) y + b(t); y (t0) = y
$$
The second equation in (1.2.6) is called the initial condition of the problem
===
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
Let's write it in a short form:
$$
y(t)=IVP(\{a\}, f(t), t_0,\{y\}_0),\tag3
$$
where
$$
\{a\} = \{a_0,a_1,\ldots a_n\}\\
\{y\}_0=\{y_0,y'_0,\ldots y^{(n-1)}_0\}\\
$$
Sometimes we would use following notation for IVP:
$$\begin{cases}
L_n(y)=f(t),\\
y_0
\end{cases}$$