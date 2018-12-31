###2 First glimpse

Let's take a look at first order system
(order of a differential equation is the largest derivative present in the differential equation):
$$
{\begin{cases}
x'+Ax=Bu(t)\\
x(0)=x_0
\end{cases}
}
$$
We can write it using our notation:
$$

\begin{cases}
L_n(\{1,A\},x)=Bu(t)\\
IC|_{t_0=0}=x_0
\end{cases}
\tag{2.1}
$$
Solution of (2.1) is a function
$$
{
x(t)=e^{-At}x_0+\int_{0}^t e^{-A(t-\tau)}Bu(\tau)d\tau
}\tag{2.2}
$$
The expression (2.2) delivers solution for the equation (2.1), which could be rewritten in a short form
$$
x(t)=\begin{cases}
L_n(\{1,A\},x)=Bu(t)\\
IC|_{t_0=0}=x_0
\end{cases}
$$
The solution of homogenous system (free response) is:
$$
x_{free}(t)=\begin{cases}
L_n(\{1,A\},x)=0\\
IC|_{t_0=0}=x_0
\end{cases}=e^{-At}x_0
$$
And substitute the Dirac delta function as load, so the system (2.1) becomes as
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
Obviosely the solution of the system (2.4) is the same as solution of next one:
$$
{\begin{cases}
x'+Ax=0,\\
x(0)=x_0+B
\end{cases}
}\tag{2.5}
$$
So we can write a next statement:
$$
\begin{cases}
L_n(\{1,A\},y)=B\delta(t)\\
IC|_{t_0=0}=x_0
\end{cases}
\equiv
\begin{cases}
L_n(\{1,A\},y)=\mathbf0\\
IC|_{t_0=0}=x_0\mathbf{+B}
\end{cases}
\tag{2.6}
$$
For the system (2.3) the solution is the same as free response of the same system but changed IC.
##### About change IC
Some books provided an analitical solution for LTI ODE with delta function as load. For example: Finan (p.57), Nagy (pp.189-190), Ogata (p.190), Zill (p.293).
Some other books noticed that the solution of IVP with delta function as load is the same as solution the similar homogenous ODE with defferernt IC.
Genta (p.180) provided the formulae for changing IC for second-order ODE in case od delta function loaded. 
Rao (p.407) noticed that following systems are equal.
$${\begin{cases}
y'+ay=F\delta(t),\\
y(0)=0
\end{cases}}\equiv{\begin{cases}
y'+ay=0,\\
y(0)=F
\end{cases}}
$$
Weber (p.733) noticed that following systems are equal.
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
Kelly (p.315) noticed that following systems are equal.
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
And Balachandran (p.286) and Genta (p.179) noticed that following systems are equal.
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
$$
\begin{cases}
L_n(\{a\},y)=b\delta(t)\\
IC|_{t_0}=IC_0
\end{cases}\equiv
\begin{cases}
L_n(\{a\},y)=0\\
IC|_{t_0}=IC_0+\{0,0,...,b/a_0\}^\intercal
\end{cases}
\tag{2.7}
$$
