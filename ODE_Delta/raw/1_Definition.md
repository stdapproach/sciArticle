### 1. Definitions and Terminology

#### 1.1 Function and Derivative Notation

Let $y(t)$ denote a real-valued function of a real variable:
$$y: \mathbb{R} \rightarrow \mathbb{R}$$

Derivatives of $y(t)$ are denoted as follows:
$$
y' = \frac{dy}{dt},\qquad
y'' = \frac{d^2y}{dt^2},\qquad
y^{(n)} = \frac{d^{n}y}{dt^{n}},\qquad
y^{(0)} = y
$$

#### 1.2 The Dirac Delta Function

The Dirac delta function is a well-known generalized function (distribution) used to model impulsive phenomena. Its properties are discussed extensively in the literature, including Balachandran (p. 287), Bottega (p. 233), Chasnov (p. 62), Finan (p. 53), Nagy (p. 185), Rao (p. 381), Weber (p. 86), Zill (p. 292), and Appendix A of this article.

#### 1.3 Initial Value Problem (IVP)

Consider an $n$-th order linear time-invariant (LTI) ordinary differential equation

$$
L_n(\{a\}, y) = \sum_{i=0}^{n} a_i y^{(n-i)}(t) = f(t), \qquad a_i \in \mathbb{R} \text{ constant}, \; i = 0,1,\dots,n \tag{1.1}
$$

subject to the initial conditions specified at $t = t_0$:

$$
\{y\}|_{t_0} = \mathbf{IC}_0 =
\begin{pmatrix}
y(t_0)   \\
y'(t_0)  \\
y''(t_0) \\
\vdots   \\
y^{(n-1)}(t_0)
\end{pmatrix} \tag{1.2}
$$

The combination of (1.1) and (1.2) constitutes an **initial value problem (IVP)**. Under standard assumptions, this problem admits a unique solution $y(t)$.

For convenience, we employ three equivalent shorthand notations for the same IVP:

$
\begin{cases}
L_n(y) = f(t)   \\
\{y\}|_{t_0} = \mathbf{IC}_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{a\}, y) = f(t) \\
\mathbf{IC}|_{t_0} = \mathbf{IC}_0
\end{cases}
\;\equiv\;
\operatorname{IVP}(\{a\}, f(t), t_0, \mathbf{IC}_0)
$

#### 1.4 Impulse Response Function (IRF)

The **impulse response function** $g(t)$ of a linear time-invariant system is defined as the system's output when the input is a unit impulse $\delta(t)$ and all initial conditions are zero. The Laplace transform of the impulse response yields the system's transfer function (Ogata, p. 17).
