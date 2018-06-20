#1 Definition & Terminology
Function
$$
y,y(t)\text{ - function takes an argument}\in\mathbb{R}\text{ and returns a result}\in\mathbb{R}
$$
Derivative:
$$
y'=\frac{dy}{dt}
$$
$$
y''=\frac{d^2y}{dt^2}
$$
$$
y^{(n)}=\frac{d^{n}y}{dt^{n}}
$$
$$
y^{(0)}=y
$$
Dirac delta function
$$
\delta(t)
$$
Heaviside step function
$$
H(t)=\int_{-\infty}^t \delta(x)dx
$$
Initial Value Problem (IVP), Caushy problem
Differential equation
$$
\sum_{i=0}^{n} a_iy^{(n-i)}=f(t)\text{ , }a_i=const\in \mathbb{R}\text{ , }i\in 0\ldots n\tag{1}
$$
and initial conditions (IC)
$$
\begin{matrix}
y_0=y(0)\\
y_1=y'(0)\\
y_2=y''(0)\\
\ldots\\
y_{n-1}=y^{(n-1)}(0)
\end{matrix}
\tag2
$$
named IVP. Equations (1) and (2) has a unique solution y(t) satisfied (1) and (2)
$$
$$
Let's write it in a short form:
$$
y(t)=IVP(\{a\}, f(t), \{y\}_0),\tag3
$$
where
$$
\{a\} = \{a_0,a_1,\ldots a_n\}\\
\{y\}_0=\{y_0,y'_0,\ldots y^{(n-1)}_0\}\\
$$