###2 Introduction
In this paper, we shall show how to:
• Analyze a linear time-invariant systems subjected to abruptly changing forces that are applied to the element of the system.

Time dependent forces may be classified as impulsive or nonimpulsive. Impulsive forces are those that act over very short periods of time but possess very large magnitudes. Nonimpulsive forces are those that are well behaved over time, such as the gravitational force, the elastic spring force and the viscous damping force.

The dynamics of evolving processes is often subjected to abrupt changes such
as:
• impact by hammer to a beam,
• explosions or shock,
• a bat striking a ball or a bolt of lightning striking a tower,
• a large applied voltage to an electrical network over a very short time frame,
• harvesting, and natural disasters.
Often these short-term perturbations are treated as having acted instantaneously or in the form of “impulses”. In this case, the output corresponding to this sudden force is referred to as the "impulse response". Mathematically, an impulse can be modeled by an initial value problem (IVP) with a special type of function known as the Dirac delta function as the external force, i.e., the nonhomogeneous term. Theimpulse response of a system is its response to the input ∂(t) when the system is initially at rest. The impulse response is usually denoted h(t). Sometimes it's called Green's function.

Let's take a look at first order system
(order of a differential equation is the largest derivative present in the differential equation):
$$
{\begin{cases}
x'+Ax=Bu(t),\\
x(0)=x_0
\end{cases}
}\tag{2.1}
$$
Solution of (2.1) is a function
$$
{
x(t)=e^{-At}x_0+\int_{0}^t e^{-A(t-\tau)}Bu(\tau)d\tau
}\tag{2.2}
$$
The expression (2.2) delivers solution for the equation (2.1), which could be rewritten in a short form
$$
x(t)=IVP\left(\{1,A\},Bu(t),t_0=0,x_0\right)
$$
The solution of homogenous system (free response) is:
$$
x_{free}(t)=IVP\left(\{1,A\},0,t_0=0,x_0\right)=e^{-At}x_0
$$
And substitute the Dirac delta function as load, so the system (1) becomes as
$$
{\begin{cases}
x'+Ax=B\delta(t),\\
x(0)=x_0
\end{cases}
}\tag{2.3}
$$
The solution is:
$$
x_\delta(t)=x_0e^{-At}+\int_{0}^t e^{-A(t-\tau)}B\delta(\tau)d\tau=\\
=x_0e^{-At}+Be^{-At}=e^{-At}(x_0+B)\tag{2.4}
$$
Obviosely the solution of (2.4) is the same as solution of next system:
$$
{\begin{cases}
x'+Ax=0,\\
x(0)=x_0+B
\end{cases}
}\tag{2.5}
$$
So we can write a next statement:
$$
IVP\left(\{1,A\},B\delta(t),t_0=0,x_0\right)=IVP\left(\{1,A\},\mathbf0,t_0=0,x_0\mathbf{+B}\right)\tag{2.6}
$$
##### About change IC
Some books provided an analitical solution for ODE_LC with delta function as load. For example: Dawkins (p.234), Finan (p.57), Nagy (pp.189-190), Ogata (p.190), Zill (p.293).
Some other books noticed that the solution of IVP for ODE_LC with delta function as load is the same as solution the similar homogenous ODE_LC with defferernt initial condition (IC).
Rao (p.407) noticed that follow systems are equal.
$${\begin{cases}
y'+ay=F\delta(t),\\
y(0)=0
\end{cases}}\equiv{\begin{cases}
y'+ay=0,\\
y(0)=F
\end{cases}}
$$
Weber (p.733) noticed that follow systems are equal.
$${\begin{cases}
mx''=P\delta(t),\\
y(0)=0\\
y'(0)=0
\end{cases}}\equiv{\begin{cases}
mx''=0,\\
y(0)=0\\
y'(0)=P/m
\end{cases}}
$$
Kelly (p.315) noticed that follow systems are equal.
$${\begin{cases}
mx''+cx'+kx=\delta(t),\\
y(0)=0\\
y'(0)=0
\end{cases}}\equiv{\begin{cases}
mx''+cx'+kx=0,\\
y(0)=0\\
y'(0)=1/m
\end{cases}}
$$
And Balachandran (p.286) and Genta (p.179) noticed that follow systems are equal.
$${\begin{cases}
mx''+cx'+kx=f_0\delta(t),\\
y(0)=0\\
y'(0)=0
\end{cases}}\equiv{\begin{cases}
mx''+cx'+kx=0,\\
y(0)=0\\
y'(0)=f_0/m
\end{cases}}
$$
It looks like (but not proven yet) these two following systems are equal:
$${\begin{cases}
    y(t)=IVP(\{a\}, b\delta(t), t_0,\{y\}_0),\\
    \{a\} = \{a_0,a_1,\ldots a_n\}\\
    \{y\}_0=\{y_0,y'_0,\ldots ,y^{(n-2)} , y^{(n-1)}_0\}\\
\end{cases}}
\equiv
{\begin{cases}
    y(t)=IVP(\{a\}, \mathbf0, t_0,\{z\}_0),\\
    \{a\} = \{a_0,a_1,\ldots a_n\}\\
    \{z\}_0=\{y_0,y'_0,\ldots ,y^{(n-2)} , \mathbf{y^{(n-1)}_0+b/a_0}\}\\
\end{cases}}
$$






