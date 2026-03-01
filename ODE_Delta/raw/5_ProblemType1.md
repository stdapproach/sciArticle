### 5. Problem Type 1

We now consider a more general class of problems, which we denote as Type 1:

$$
\sum_{i=0}^{n} a_i y^{(n-i)}(t) = \sum_{j=0}^{m} b_j \delta^{(m-j)}(t), \qquad m < n \tag{5.1}
$$

subject to the initial conditions

$$
\{y\}\big|_{t_0} = \mathbf{IC}_0 =
\begin{pmatrix}
y(t_0) \\
y'(t_0) \\
y''(t_0) \\
\vdots \\
y^{(n-1)}(t_0)
\end{pmatrix} \tag{5.2}
$$

Equations (5.1) and (5.2) together define an initial value problem (IVP). As before, we set $t_0 = 0$ without loss of generality; the extension to arbitrary $t_0$ is straightforward. The condition $m < n$ will be justified shortly.

#### 5.1 Modification of Initial Conditions

Our objective remains the same: to transform the nonhomogeneous IVP (5.1)–(5.2) into an equivalent homogeneous system by suitably altering the initial conditions.

Applying the Laplace transform to both sides of (5.1) with nonzero initial conditions and collecting terms yields an algebraic structure analogous to that of Section 3. After straightforward algebra, we obtain a matrix formulation similar to (3.1). Specifically, we define

$$
A = \begin{bmatrix}
a_0 & 0 & 0 & \cdots & 0 \\
a_1 & a_0 & 0 & \cdots & 0 \\
a_2 & a_1 & a_0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 \\
a_{n-1} & a_{n-2} & a_{n-3} & \cdots & a_0
\end{bmatrix},\qquad
\mathbf{d} = \begin{bmatrix}
0 \\ \vdots \\ 0 \\ b_0 \\ b_1 \\ \vdots \\ b_m
\end{bmatrix} \tag{5.3}
$$

where the first $n-(m+1)$ entries of $\mathbf{d}$ are zero, followed by the coefficients $b_0, b_1, \dots, b_m$ from the right‑hand side of (5.1).

The main result for Type 1 is then
$$
\boxed{
\begin{cases}
L_n(\{a\}, y) = L_m(\{b\}, \delta) \\[2pt]
\mathbf{IC}_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{a\}, y) = \mathbf{0} \\[2pt]
\mathbf{IC}_0 + A^{-1}\mathbf{d}
\end{cases}
} \tag{5.4}
$$

In words, the original IVP forced by a linear combination of the delta function and its derivatives is equivalent to the homogeneous system with the same left‑hand side, provided that the initial conditions are augmented by the vector $A^{-1}\mathbf{d}$. The structure of $\mathbf{d}$ ensures that only the last $m+1$ initial conditions are affected; the first $n-(m+1)$ remain unchanged.

We can now see why the condition $m < n$ is essential. If $m \ge n$, the matrix $A$ would be ill‑defined for the purpose of matching terms in the Laplace‑domain equation. More importantly, from a physical standpoint, a right‑hand side containing derivatives of the delta function of order equal to or higher than the order of the ODE would imply a solution that itself contains singularities (Dirac deltas or their derivatives), which is not admissible in the context of classical physical interpretations of system response.

#### 5.2 Connection with Control Theory

In control theory, the **impulse response** of a linear time‑invariant (LTI) system is defined as its output when the input is a Dirac delta function, assuming zero initial conditions. This concept is fundamental because the impulse response completely characterizes the system dynamics: the Laplace transform of the impulse response yields the system's transfer function [Genta, p. 180; Meirovitch, p. 180; Kelly, p. 314; Ogata, p. 17]. Conversely, the impulse response is the inverse Laplace transform of the transfer function [Meirovitch, p. 180].

Specifically, let the transfer function be
$
W(s) = \frac{b_0 s^m + b_1 s^{m-1} + \cdots + b_{m-1} s + b_m}{a_0 s^n + a_1 s^{n-1} + \cdots + a_{n-1} s + a_n}.
$

Then the impulse response $g(t)$ is given by $g(t) = \mathcal{L}^{-1}\{W(s)\}$. The transfer function satisfies $W(s) = Y(s)/X(s)$ precisely when the system is governed by
$
\begin{cases}
a_0 y^{(n)} + a_1 y^{(n-1)} + \cdots + a_{n-1} y' + a_n y
= b_0 x^{(m)} + b_1 x^{(m-1)} + \cdots + b_{m-1} x' + b_m x, \\[4pt]
\mathbf{IC} = \mathbf{0}.
\end{cases}
$

Consequently, the impulse response is exactly the solution of the Type 1 problem with zero initial conditions:
$$
IR \equiv g(t) = \begin{cases}
L_n(\{a\}, y) = L_m(\{b\}, \delta) \\[2pt]
\mathbf{IC}_0 = \mathbf{0}
\end{cases} \tag{5.5}
$$

Thus, the result (5.4) provides a direct method for computing the impulse response: one need only solve the homogeneous system with the modified initial conditions $A^{-1}\mathbf{d}$ (since $\mathbf{IC}_0 = \mathbf{0}$). This offers an alternative to explicit Laplace inversion and may be particularly advantageous for numerical implementation.
