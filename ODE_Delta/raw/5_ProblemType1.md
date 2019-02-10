###5. A problem Type 1
This part ragarding the following problem, we called Type 1:

$$
\sum_{i=0}^{n} a_iy^{(n-i)}(t)=\sum_{j=0}^{m} b_j\delta^{(m-j)}(t),\\
m < n\tag{5.1}
$$
$$
    \{y\}|_{t_0}=IC|_{t_0}=\left\{
    \begin{matrix}
    y(t_0)\\
    y'(t_0)\\
    y''(t_0)\\
    \vdots \\ 
    y^{(n-1)}(t_0)\\ 
    \end{matrix}\right\}\tag{5.2}
$$
Again, (5.1) and (5.2) together delivered IVP and we suppose that $t_0=0$, otherwise ... you know how to handle with it. We explain later why m should be less than n.

####5.1 Change IC for IVP
Again, we're trying to find a solution for change IC for IVP such as (5.1, 5.2) which delivered an eqivalence solution for honogenous system.

To solve this problemlet's perform LT for $y(t)$, and right side with respect to non-null initial condition.
Skipping the trivial part we've got the similar for (3.1) equation:

Rewrite it at this way:
$$
A=\left[
    \begin{array}
    a_0 & 0 & 0 &\cdots & 0 \\
    a_1 & a_0 & 0 &\cdots & 0 \\
    a_2 & a_1 & a_0 &\cdots & 0 \\
    \vdots & \vdots & \vdots &\ddots & 0 \\
    a_{n-1} & a_{n-2} & a_{n-3} &\cdots & a_0 \\
    \end{array}\right],
    \{d\}=\left\{
    \begin{matrix} 0 \\ \vdots \\ b_0 \\ \vdots \\ b_{m-1}\\b_m\\ \end{matrix}\right\}
    \tag{5.3}
$$

The main result for Type1 is following:
$$
\bbox[5px,border:2px solid red]
{
\begin{cases}
L_n(\{a\},y)=L_m(\{b\},\delta)\\
IC_0
\end{cases}
\equiv
{\begin{cases}
L_n(\{a\},y)=\mathbf{0}\\
IC_0+[A]^{-1}\begin{matrix}\{  0 & \cdots & b_0 & b_1\cdots b_m\end{matrix} \}^\intercal
\end{cases}}
}\tag{5.4}
$$
Now it's obvious why m should be less than n. Otherwise the system (5.3) couldn't been even written. Phisically it means that if m great or equal n the solution would contain Delta function (and/or it's derivatives) which is phisically impossible.

####5.2 Connection for Control Theory
In control theory the impulse response is the response of a system to a Dirac delta input. This proves useful in the analysis of dynamic systems; the Laplace transform of the delta function is 1, so the impulse response is equivalent to the inverse Laplace transform of the system's transfer function (https://en.wikipedia.org/wiki/Impulse_response#Control_systems)
This kind of knowledge also could be found at some books:
$\circ$ The impulse response completely characterizes the system [Genta p.180];
$\circ$ the impulse response is equal to the Inverse Laplace Transform of the transfer function [Meirovich p.180];
$\circ$ the transfer function is also the Laplace transform of its impulsive response, which is the response due to a unit impulse [Kelly p.314];
$\circ$ the response of a system due to a unit impulse can be determined as the free response
with zero initial displacement and an initial velocity equal to velocity imparted by the
impulse [Kelly p.370];
$\circ$  the transfer function and impulse-response function of a linear, time-invariant system contain the same information about the system dynamics. It is hence possible to obtain complete information about the dynamic characteristics of the system by exciting it with an impulse input and measuring the response [Ogata p.17].
$$
IR=g(t)=L^{-1}(W(s));\\
W(s)=\frac{b_0s^m+b_1s^{m-1}+\cdots+b_{m-1}s+b_m}{a_0s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n}
$$

$$
W(s)=\frac{Y(s)}{X(s)}\iff
\begin{cases}
a_0y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}y'+a_ny=\\
=b_0x^{(m)}+b_1s^{(m-1)}+\cdots+b_{m-1}x'+b_mx;\\
IC=\{0 \cdots 0\}^\intercal
\end{cases}
$$
$\Rightarrow$
$$
IR=
\begin{cases}
L_n(\{a\},y)=L_m(\{b\},\delta)\\
IC_0
\end{cases}\tag{5.5}
$$

