###3. A problem Type 0
This part ragarding the following problems.

Type 0a
$$\begin{cases}L_n(y)=b\delta(t),\\
IC_0, n \ge 1
\end{cases}$$

Type 0b
$$\begin{cases}
L_n(y)=b\delta(t-c),\\
IC_0, n \ge 1
\end{cases}$$

Type 0c
$$\begin{cases}
L_n(y)=\sum_{i=0}^k b_i\delta(t-c_i),\\
IC_0, n \ge 1
\end{cases}$$

We suppose that $t_0=0$, otherwise for such time-invariant systems we could just change time variable as $t^*=t-t_0$.
####3.1 Problem Type 0a
Find an IC for homogenous system which delivers the equivalence for non-homogenous one.
At this case 'equivalence' means:
$$z(t)=y(t), \forall t\ge  t_0 $$
for the next systems: a given non homogenous system
$$
\begin{cases}
L_n(\{a\},y)=b\delta(t)\\
IC|_{t_0=0}=IC_y
\end{cases}
$$
the homogenous system which IC supposed to be found
$$
\begin{cases}
L_n(\{a\},z)=0\\
IC_z
\end{cases}
$$
To solve the problem Type 0a let's perform Laplace Transform (LT) for $y(t)$ with respect to non-null initial condition.
$$
LT\{y(t)\}=Y(s)
$$
$$
Y(s)=LT\left\{\sum_{i=0}^n \left( a_iy^{(n-i)}(t)-b\delta(t)\right)\right\}=\sum_{i=0}^n \left( a_iL\{y^{(n-i)}(t)\}\right)-bL\{\delta(t)\}
$$
$$\begin{equation}\begin{aligned}
LT\{a_0y^{(n-0)}\}&=a_0\left[s^nY-s^{n-1}y(0)-s^{n-2}y'(0)-s^{n-3}y''(0)- ...-s^1y^{(n-2)}(0)-s^0y^{(n-1)}(0)\right]\\

LT\{a_1y^{(n-1)}\}&=a_1\left[s^{n-1}Y-s^{n-2}y(0)-s^{n-3}y'(0)-s^{n-2}y''(0)- ...-s^1y^{(n-3)}-s^0y^{(n-2)}(0)\right]\\

LT\{a_2y^{(n-2)}\}&=a_2\left[s^{n-2}Y-s^{n-3}y(0)-s^{n-4}y'(0)-s^{n-5}y''(0)- ...-s^1y^{(n-4)}(0)-s^0y^{(n-3)}(0)\right]\\
&...\\

LT\{a_{n-1}y'\}&=a_{n-1}\left[s'Y-s^0y(0) \right]\\

LT\{a_{n}y\}&=a_{n}\left(Y\right)\\

-bLT\{\delta(t)\}&=-be^{(-s)0}=-b

\end{aligned}\end{equation}$$

Let's using (1.2) and rewrite at this way:

$$\begin{equation}\begin{aligned}
LT\{y(t)\} = &s^n\left(a_0Y\right)+\\
  & s^{n-1}\left(a_1Y-a_0y_0\right)+\\
  & s^{n-2}\left(a_2Y-a_1y_0-a_0y_1\right)+\\
  & s^{n-3}\left(a_3Y-a_2y_0-a_1y_1-a_0y_2\right)+\\
  & ...\\
  & s^1\left(a_{n-1}Y-\sum_{i=0}^{n-2} a_{n-2-i}y_i\right)+\\
  & s^0\left(a_{n}Y-\sum_{i=0}^{n-1} a_{n-1-i}y_i+b\right)=\\
  & =\sum_{i=0}^{n} s^{n-i}a_iY-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b
\end{aligned}\end{equation}$$

Let's perform LT for $z(t)$ with respect to non-null initial condition.
$$
LT\{z(t)\}=Z(s)
$$
$$\begin{equation}\begin{aligned}
LT\{z(t)\} = \sum_{i=0}^{n} s^{n-i}a_iZ-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)
\end{aligned}\end{equation}$$
$$
y(t)=z(t)\implies Y(s)=Z(s)\implies\\
\sum_{i=0}^{n} s^{n-i}a_iY-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b=\sum_{i=0}^{n} s^{n-i}a_iZ-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)
$$
Due to
$$
s^{n-i}a_iY=s^{n-i}a_iZ, i=0...n\implies
$$

$$
\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b=\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)\implies
$$
following equations:
$$\begin{equation}\begin{aligned}
&i=1\to(s^{n-1}):a_0y_0=a_0z_0\\
&i=2\to(s^{n-2}):\sum_{j=0}^{1}a_{1-j}y_j=\sum_{j=0}^{1}a_{1-j}z_j\\
&...\\
&i=n\to(s^{n-n}):\sum_{j=0}^{n-1}a_{n-1-j}y_j+b=\sum_{j=0}^{n-1}a_{n-1-j}z_j
\end{aligned}\end{equation}$$

Rewrite it at this way:
$$
A=\left[
    \begin{matrix}
    a_0 & 0 & 0 &\cdots & 0 \\
    a_1 & a_0 & 0 &\cdots & 0 \\
    a_2 & a_1 & a_0 &\cdots & 0 \\
    \vdots & \vdots & \vdots &\ddots & 0 \\
    a_{n-1} & a_{n-2} & a_{n-3} &\cdots & a_0 \\
    \end{matrix}\right],
    \{d\}=\left\{
    \begin{matrix} 0 \\ 0 \\ 0 \\ \vdots \\ 0\\b\\ \end{matrix}\right\}\tag{3.1}
$$
$$
[A]\left\{
    \begin{matrix} y_0 \\y_1 \\y_2 \\ \vdots \\ y_{n-1} \end{matrix}\right\}+
    \{d\}=
    [A]\left\{
    \begin{matrix} z_0 \\z_1 \\z_2 \\ \vdots \\ z_{n-1} \end{matrix}\right\}
$$
$$
[A]\{y\}+\{d\}=[A]\{z\}, det([A])\ne 0\Rightarrow
$$
$$
\{z\}=\{y\}+[A]^{-1}\{d\}\tag{3.2}
$$
Due to $[A]$ is lower-triangle matrix and $\{d\}=\{0,0,...,b\}$ the main result is following:

$$
\bbox[5px,border:2px solid red]
{
\begin{cases}
L_n(\{a\},y)=b\delta(t)\\
IC_0
\end{cases}
\equiv
{\begin{cases}
L_n(\{a\},y)=\mathbf{0}\\
IC_0+\mathbf{[A]^{-1}\{d\}}
\end{cases}}
\equiv
\begin{cases}
L_n(\{a\},y)=0\\
IC_0+\{0,0,...,b/a_0\}^\intercal
\end{cases}
}\tag{3.3}
$$
The formula (3.3) is the mathematical notation of algorythm how to solve LTI ODE with Dirac function load. There is only need to change IC and solve the similar homogenous system using any method you like (analytical or numerical). A numerical one called Runge-Kutta fourth order method could be found at Butcher (p.98).
There has been proven (2.7). Indeed, (3.3) and (2.7) are the same.
The system Type 0a could be rewritten as simple impulse differential equation (look Benchohra, Henderson and Ntouyas "Impulsive Differential Equations and Inclusions")

####3.2 Problem Type 0b
The idea how to solve the Type 0b's problem is very simple and well explained at the part 4.4-4.6.

####3.3 Problem Type 0c
The idea how to solve the Type 0c's problem is very simple and well explained at the part 4.7.

