### 2.1 First glimpse

We begin by examining a first‑order linear system (the order of a differential equation is the highest derivative appearing in it):

$
\begin{cases}
x' + A x = B u(t) \\[2pt]
x(0) = x_0
\end{cases}
$

Using the notation introduced in Section 1, this can be written compactly as

$$
\begin{cases}
L_n(\{1,A\}, x) = B u(t) \\[2pt]
IC|_{t_0=0} = x_0
\end{cases}
\tag{2.1}
$$

The solution to (2.1) is well known:

$$
x(t) = e^{-At} x_0 + \int_0^t e^{-A(t-\tau)} B u(\tau) \, d\tau \tag{2.2}
$$

The free response (homogeneous solution) is obtained from

$
\begin{cases}
L_n(\{1,A\}, x) = 0 \\[2pt]
IC|_{t_0=0} = x_0
\end{cases}
\quad\Longrightarrow\quad
x_{\text{free}}(t) = e^{-At} x_0
$

Now let the forcing function be the Dirac delta, i.e. set $u(t) = \delta(t)$ in (2.1). Then the system becomes

$$
\begin{cases}
x' + A x = B \delta(t), \\[2pt]
x(0) = x_0
\end{cases}
\tag{2.3}
$$

Its solution follows from (2.2) with $u(\tau)=\delta(\tau)$:

$$
\begin{aligned}
x_\delta(t) &= x_0 e^{-At} + \int_0^t e^{-A(t-\tau)} B \delta(\tau) \, d\tau \\
            &= x_0 e^{-At} + B e^{-At}
            = e^{-At} (x_0 + B) \tag{2.4}
\end{aligned}
$$

It is evident that $x_\delta(t)$ coincides with the solution of the following homogeneous initial value problem:

$$
\begin{cases}
x' + A x = 0, \\[2pt]
x(0) = x_0 + B
\end{cases}
\tag{2.5}
$$

In the shorthand notation we can therefore write

$$
\begin{cases}
L_n(\{1,A\}, y) = B \delta(t) \\[2pt]
IC|_{t_0=0} = x_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{1,A\}, y) = \mathbf{0} \\[2pt]
IC|_{t_0=0} = x_0 \mathbf{+ B}
\end{cases}
\tag{2.6}
$$

Thus, for the first‑order system (2.3), the response to an impulsive input is exactly the free response of the same system, but with the initial condition shifted by the magnitude of the impulse.
