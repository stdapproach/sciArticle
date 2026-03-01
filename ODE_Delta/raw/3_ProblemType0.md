### 3. Problem Type 0

This section addresses problems of the following forms:

| **Type 0a** | **Type 0b** | **Type 0c** |
|--------------|----------------|---------------|
| $\begin{cases} L_n(y) = b \,\delta(t), \\[2pt] \mathbf {IC}_0, \quad n \ge 1 \end{cases}$ | $\begin{cases}L_n(y) = b \,\delta(t - c), \\[2pt]\mathbf{IC}_0, \quad n \ge 1\end{cases}$ | $\begin{cases}L_n(y) = \displaystyle\sum_{i=0}^k b_i \,\delta(t - c_i), \\[4pt]\mathbf{IC}_0, \quad n \ge 1\end{cases}$ |

Without loss of generality we set $t_0 = 0$; for time‑invariant systems with a different initial time, one may simply shift the time variable via $t^* = t - t_0$.

### 3.1 Problem Type 0a

We seek initial conditions for the homogeneous system that yield a solution identical to that of the nonhomogeneous one. Specifically, we require
$z(t) = y(t) \quad \forall\, t \ge 0$
for the two systems:
$
\begin{cases}
L_n(\{a\}, y) = b \,\delta(t) \\[2pt]
IC|_{t_0=0} = \mathbf{IC}_y
\end{cases}
\qquad\text{and}\qquad
\begin{cases}
L_n(\{a\}, z) = 0 \\[2pt]
IC_z \quad \text{(to be determined)}
\end{cases}
$

#### 3.1.1 The Laplace Transform

The Laplace transform (LT) is an integral transform that maps a function of a real variable $t$ (typically time) into a function of a complex variable $s$ (complex frequency). It is defined for functions on $[0,\infty)$ and is invertible on a large class of functions. The LT is particularly useful for solving differential and integral equations, as it converts differentiation into multiplication by $s$ and convolution into ordinary multiplication.

A comprehensive treatment of the Laplace transform can be found in: Cohen (p. 12), Nagy (p. 196), Weber (p. 693), Schiff (p. 210, table of transforms), the Wikipedia article on the Laplace transform

#### 3.1.2 Laplace Transform Method for ODEs

The procedure for solving an ODE via the Laplace transform consists of three steps:
1. Apply the Laplace transform to both sides of the equation.
2. Solve the resulting algebraic equation for $Y(s) = \mathcal{L}\{y(t)\}$.
3. Compute the inverse Laplace transform to obtain $y(t) = \mathcal{L}^{-1}\{Y(s)\}$.

Additional details on this technique can be found in:
Cohen (p. 7), Schiff (p. 59), Xue (p. 380, table of inverse transforms)

#### 3.1.3 Solution of Type 0a

Let $Y(s) = \mathcal{L}\{y(t)\}$. Applying the Laplace transform to the ODE
$
\sum_{i=0}^n a_i y^{(n-i)}(t) = b\,\delta(t)
$

and using the differentiation rule
$
\mathcal{L}\{y^{(k)}(t)\} = s^k Y(s) - s^{k-1}y(0) - s^{k-2}y'(0) - \cdots - y^{(k-1)}(0),
$

we obtain an algebraic equation. Collecting terms by powers of $s$ yields

$$
\begin{aligned}
0 = &\ s^n (a_0 Y) \\
    &+ s^{n-1} \bigl(a_1 Y - a_0 y_0\bigr) \\
    &+ s^{n-2} \bigl(a_2 Y - a_1 y_0 - a_0 y_1\bigr) \\
    &+ s^{n-3} \bigl(a_3 Y - a_2 y_0 - a_1 y_1 - a_0 y_2\bigr) \\
    &+ \cdots \\
    &+ s^1 \Bigl(a_{n-1} Y - \sum_{i=0}^{n-2} a_{n-2-i} y_i \Bigr) \\
    &+ s^0 \Bigl(a_n Y - \sum_{i=0}^{n-1} a_{n-1-i} y_i - b \Bigr),
\end{aligned}
\tag{*}
$$

where $y_k = y^{(k)}(0)$ denote the initial conditions.
For the homogeneous system $\sum a_i z^{(n-i)} = 0$ with (unknown) initial conditions $z_0, z_1, \dots, z_{n-1}$, we similarly have

$$
\begin{aligned}
0 = &\ s^n (a_0 Z) \\
    &+ s^{n-1} \bigl(a_1 Z - a_0 z_0\bigr) \\
    &+ s^{n-2} \bigl(a_2 Z - a_1 z_0 - a_0 z_1\bigr) \\
    &+ \cdots \\
    &+ s^0 \Bigl(a_n Z - \sum_{i=0}^{n-1} a_{n-1-i} z_i \Bigr).
\end{aligned}
\tag{**}
$$

If $y(t) = z(t)$ for all $t$, then $Y(s) = Z(s)$. Equating the coefficients of like powers of $s$ in (*) and (**) and canceling the common terms involving $Y$ and $Z$ gives a system of equations for the unknown initial conditions $z_k$:

$
\begin{aligned}
& (s^{n-1}): & a_0 y_0 &= a_0 z_0 \\
& (s^{n-2}): & a_1 y_0 + a_0 y_1 &= a_1 z_0 + a_0 z_1 \\
& \qquad\vdots \\
& (s^{0}): & \sum_{j=0}^{n-1} a_{n-1-j} y_j + b &= \sum_{j=0}^{n-1} a_{n-1-j} z_j .
\end{aligned}
$

These equations can be expressed in matrix form. Define the lower‑triangular matrix

$$
A = \begin{bmatrix}
a_0 & 0 & 0 & \cdots & 0 \\
a_1 & a_0 & 0 & \cdots & 0 \\
a_2 & a_1 & a_0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 \\
a_{n-1} & a_{n-2} & a_{n-3} & \cdots & a_0
\end{bmatrix},
\qquad
\mathbf{d} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ \vdots \\ 0 \\ b \end{bmatrix}.
\tag{3.1}
$$

Then the system becomes
$
A \mathbf{y} + \mathbf{d} = A \mathbf{z},
$

where $\mathbf{y} = [y_0, y_1, \dots, y_{n-1}]^T$ and $\mathbf{z} = [z_0, z_1, \dots, z_{n-1}]^T$. Since $A$ is lower triangular with $a_0 \neq 0$ (the ODE is of order $n$), $\det(A) \neq 0$, and we obtain
$$
\mathbf{z} = \mathbf{y} + A^{-1}\mathbf{d}.
\tag{3.2}
$$

Because $\mathbf{d}$ has only its last entry nonzero and $A$ is lower triangular, the correction term $A^{-1}\mathbf{d}$ simplifies dramatically. A direct calculation shows that $A^{-1}\mathbf{d} = [0, 0, \dots, 0, b/a_0]^T$. Consequently,

$$
\boxed{
\begin{cases}
L_n(\{a\}, y) = b\,\delta(t) \\[2pt]
\mathbf{IC}_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{a\}, y) = 0 \\[2pt]
\mathbf{IC}_0 + \bigl(0, 0, \ldots, 0, b/a_0\bigr)^T
\end{cases}
}
\tag{3.3}
$$

Formula (3.3) provides a simple algorithm for solving an LTI ODE with a Dirac delta forcing term: modify the initial conditions as indicated and solve the resulting homogeneous system using any analytical or numerical method (e.g., the fourth‑order Runge–Kutta method; see Butcher, p. 98).

Observe that (3.3) confirms the conjecture (2.7) and establishes their equivalence. The Type 0a problem can also be viewed as a special case of an impulsive differential equation (see Benchohra, Henderson, and Ntouyas, *Impulsive Differential Equations and Inclusions*).

### 3.2 Problem Type 0b

The solution strategy for Type 0b is straightforward and will be developed in Sections 4.4–4.6.

### 3.3 Problem Type 0c

The solution strategy for Type 0c is similarly straightforward and will be presented in Section 4.7.
