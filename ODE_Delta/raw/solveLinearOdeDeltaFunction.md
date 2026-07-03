## An Efficient Method to Solve ODEs with the Delta Function

**Denis Pleshkov**
<std.approach@gmail.com>
2019, 2026Jun

The article and accompanying Python scripts can be downloaded from:
[https://github.com/stdapproach/sciArticle/tree/develop/ODE_Delta](https://github.com/stdapproach/sciArticle/tree/develop/ODE_Delta)

### Abstract

This article addresses linear time-invariant (LTI) ordinary differential equations (ODEs) that include the Dirac delta function and its derivatives as forcing functions. We present an algorithm to transform the original nonhomogeneous ODE, subject to any given initial conditions, into an equivalent homogeneous ODE with modified initial conditions. The resulting homogeneous equation can then be solved using standard analytical or numerical methods. The algorithm is verified through several examples with known analytical solutions. A detailed review of relevant literature is provided, along with recommended exercises.

### Keywords

Impulse response function, time domain, linear ODE, delta function
### Introduction

The dynamics of evolving processes are often subject to abrupt changes, such as:
- impact of a hammer on a beam,
- a bat striking a ball,
- or a bolt of lightning striking a tower.

Such short-term perturbations are frequently treated as instantaneous events, often modeled as "impulses." According to Rao (p. 381), an impulsive force is characterized by a large magnitude acting over a very short duration. The system's response to such a force is termed the impulse response function (IRF). Mathematically, an impulse can be represented within an initial value problem (IVP) by incorporating the Dirac delta function as the external forcing term. The impulse response of a system is defined as its output in response to an input $\delta(t)$, assuming the system is initially at rest.

As Cohen (p. 13) notes, "The impulse function is useful when we are trying to model physical situations, such as the case of two billiard balls impinging, where we have a large force acting for a short time which produces a finite change of momentum."

While seeking a general method to solve such systems, we found that existing literature primarily offers solutions for specific first- and second-order ODEs. This gap motivated us to develop—or perhaps rediscover—a more general approach.

The material presented in this paper assumes only a basic familiarity with ordinary differential equations, Laplace transforms, and linear algebra.
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
### 2.2 Literature review: equivalence through initial condition modification

Several textbooks provide analytical solutions for LTI ODEs with a Dirac delta forcing function. Examples include Finan (p. 57), Nagy (pp. 189–190), Ogata (p. 190), Oliveira and Cortes (p. 3), Rao (p. 381), and Zill (p. 293).

Other authors explicitly note that the solution of an IVP with a delta load coincides with the solution of the corresponding homogeneous ODE subject to modified initial conditions. A brief survey of such observations follows.

Genta (p. 180) gives a formula for adjusting zero initial conditions in a second‑order ODE under delta loading.
Rao (p. 407) states the equivalence

$
\begin{cases}
y' + a y = F \delta(t), \\
y(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
y' + a y = 0, \\
y(0) = F
\end{cases}
$

Weber (p. 733) notes the analogous result

$
\begin{cases}
m x'' = P \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' = 0, \\
x(0) = 0, \\
x'(0) = P/m
\end{cases}
$

Kelly (p. 315) observes

$
\begin{cases}
m x'' + c x' + k x = \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' + c x' + k x = 0, \\
x(0) = 0, \\
x'(0) = 1/m
\end{cases}
$

Balachandran (pp. 287–288), Beards (p. 66), Bottega (pp. 235–236), Genta (p. 179), Meirovitch (pp. 160–161), Schiff (p. 83) and Schmitz (p. 118) all remark that

$
\begin{cases}
m x'' + c x' + k x = f_0 \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' + c x' + k x = 0, \\
x(0) = 0, \\
x'(0) = f_0/m
\end{cases}
$

Chasnov (p. 63) provides a formula for changing the initial conditions of a second‑order LTI ODE, while Oliveira and Cortes (p. 2) give a similar treatment for particular systems with zero initial conditions.

The above examples suggest a general pattern (though a formal proof appears to be missing in the literature): an IVP forced by a delta function may be equivalent to a homogeneous IVP with a shifted initial condition. Specifically, for an $n$-th order system one might conjecture

$$
\begin{cases}
L_n(\{a\}, y) = b \delta(t) \\[2pt]
IC|_{t_0} = \mathbf{IC}_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{a\}, y) = 0 \\[2pt]
IC|_{t_0} = \mathbf{IC}_0 + \bigl(0,0,\ldots, b/a_0\bigr)^{\!T}
\end{cases}
\tag{2.7}
$$

### 2.3 Detailed literature classification

For the purposes of this article we have surveyed a wide range of sources dealing with LTI ODEs subject to impulsive loads (the Dirac delta and its derivatives). The books and articles examined fall into five categories:

1. **Provide a solution without mentioning the equivalence**
   Asadi, Agarwal (IRF for state‑space systems), Alam (p. 219 1st order, p. 270 2nd order), Benaroya (p. 147 IRF 2nd order), Boyce (p. 346 2nd order with time shift), Brandt, Campbell, Dobrushkin (pp. 341–342, 348, 688), Dorf (pp. 123, 208), Duffy (pp. 93, 166, 284), Etkin (pp. 74, 76), Goode (pp. 708–709), Gupta (pp. 72, 86, 116), Holmes, Jack (p. 575), Kani, Korman (p. 160), Kreyszig (p. 227, 230–231), Liu (p. 50), McOwen (p. 98), Ram (pp. 845, 847), Ricardo, Jain.

2. **Mention the change of initial condition without giving an explicit formula**
   Adkins (p. 319, using momentum / Laplace transform), Anderson (p. 8, 2nd order, momentum argument), Angeles (pp. 115–119, 132, 136, 144), Balachandran (p. 301), Baruh (pp. 259, 303), Campos (p. 166, oscillator with one derivative of delta), Chopra (pp. 121, 489, 604, 616–626), Esfandiari (pp. 57, 351–359, 365, 394, 485), Franklin (pp. 110, 115, 144–149, 589), Howell (p. 560), Inman (pp. 220–225, 557–571), Iyengar (p. 87), James (pp. 345–353, 365–367), Jazar (pp. 173, 188–189), Kabe (pp. 149, 234, 300–302, 469–474), Kausel (p. 82), Lathi (p. 88), Logan (pp. 168–173, 344), Luintel (pp. 215, 507), MacCluer (pp. 373–375), Meirovitch (pp. 161, 181, 371, 463, 615), Nagle (pp. 407–408), Nielsen (pp. 24, 63), Palm (pp. 128, 134), Peterson (p. 363), Polking (pp. 231–232), Shabana (p. 206), Thorby (pp. 50–51), Trench (pp. 478–480), Tse (p. 54).

3. **Provide an explicit formula for changing initial conditions for specific equations**
   Edwards (p. 500, 2nd order with time shift), Klee (pp. 169–187).

4. **Supply a full formula for the case where the load contains only the delta function (and possibly its derivatives) for general $n$**
   Angeles (p. 144, state‑space IRF as a changed initial condition), Beneš (article, closed‑form using Laplace transform), Filippov (pp. 18–29, recurrence for IRF with one distribution on the right‑hand side, also delta in coefficients).

5. **Provide a closed‑form solution for an LTI ODE with a sum of derivatives of the Dirac delta as the forcing function**
   To the best of our knowledge, the present work appears to be the only one offering such a general treatment.
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
### 4. Verification of Type 0 by Examples

We verify the main result of Section 3 using the examples collected in Appendix B (systems of Type 0). To demonstrate the method, we have developed a set of Python scripts that perform the necessary calculations and generate the corresponding plots. All scripts are available at:

[https://github.com/stdapproach/sciArticle/tree/develop/ODE_Delta/raw](https://github.com/stdapproach/sciArticle/tree/develop/ODE_Delta/raw)

#### 4.1 Example 1 [Oliveira and Cortes, p. 3], [Schiff, p. 82]

Consider the second‑order ODE (Type 0a)
$
\begin{cases}
y'' + a y' = \delta(t), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\;\Longrightarrow\;
\operatorname{IVP}(\{1, a, 0\}, \delta(t), t_0=0, \mathbf{y}_0=\{0,0\}).$
From (3.1),
$
A = \begin{bmatrix}
1 & 0 \\
a & 1
\end{bmatrix},\quad
\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\;\Longrightarrow\;
A^{-1} = \begin{bmatrix}
1 & 0 \\
-a & 1
\end{bmatrix},\quad
A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
$

Applying (3.2)–(3.3), the following two systems are equivalent:

$
\begin{cases}
y'' + a y' = \delta(t), \\
y(0) = y'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
y'' + a y' = 0, \\
y(0) = 0,\; y'(0) = 1
\end{cases}.
$

In compact notation,
$
\operatorname{IVP}(\{1, a, 0\}, \delta(t), t_0=0, \mathbf{y}_0=\{0,0\})
\;\equiv\;
\operatorname{IVP}(\{1, a, 0\}, 0, t_0=0, \mathbf{y}_0=\{0,1\}).
$

For $a = 2$, we compare the numerical solution of the homogeneous system with modified initial conditions against the analytical solution of the original problem.

**Analytical solution** (from Appendix B):
$
y(t) = \frac{1}{a}\bigl(1 - e^{-a t}\bigr).
$

The numerical solution, analytical solution, and error (from `example1.py`) are shown below:

#### 4.1 Example 1

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex1.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex1_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.2 Example 2 [Finan, pp. 57–58]

Consider the second‑order ODE (Type 0a)
$
\begin{cases}
2y'' + 4y' + 10y = \delta(t) \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
\;\Longrightarrow\;
\operatorname{IVP}(\{2,4,10\}, \delta(t), t_0=0, \mathbf{y}_0=\{0,0\}).
$
Then
$
A = \begin{bmatrix}
2 & 0 \\
4 & 2
\end{bmatrix},\quad
\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\;\Longrightarrow\;
A^{-1} = \begin{bmatrix}
1/2 & 0 \\
-1   & 1/2
\end{bmatrix},\quad
A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 1/2 \end{bmatrix}.
$
Hence
$
\mathbf{z}_0 = \mathbf{y}_0 + A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 1/2 \end{bmatrix}.
$
The equivalent homogeneous system is therefore
$
\begin{cases}
2z'' + 4z' + 10z = 0 \\[2pt]
z(0) = 0,\; z'(0) = 1/2
\end{cases}.
$

**Analytical solution**:
$
y(t) = \frac{1}{4} e^{-t} \sin(2t).
$
Results from `example2.py`:
<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex2.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex2_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.3 Example 3 [Nagy, p. 189]

Consider the second‑order ODE (Type 0a)
$
\begin{cases}
y'' + 2y' + 2y = \delta(t) \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
\;\Longrightarrow\;
\operatorname{IVP}(\{1,2,2\}, \delta(t), t_0=0, \mathbf{y}_0=\{0,0\}).
$
Here
$
A = \begin{bmatrix}
1 & 0 \\
2 & 1
\end{bmatrix},\quad
\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\;\Longrightarrow\;
A^{-1} = \begin{bmatrix}
1 & 0 \\
-2 & 1
\end{bmatrix},\quad
A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
$
Thus
$
\mathbf{z}_0 = \mathbf{y}_0 + A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
$
The equivalent homogeneous system is
$
\begin{cases}
z'' + 2z' + 2z = 0 \\[2pt]
z(0) = 0,\; z'(0) = 1
\end{cases}.
$

**Analytical solution**:
$
y(t) = e^{-t} \sin(t).
$
Results from `example3.py`:
<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex3.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex3_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.4 Example 4 [Nagy, p. 189]

Consider the second‑order ODE with a time‑delayed impulse (Type 0b):
$
\begin{cases}
y'' + 2y' + 2y = \delta(t - c), \\[2pt]
y(0) = y'(0) = 0, \\[2pt]
c = 2.
\end{cases}
$
The solution strategy splits the problem into two stages:

1. On $0 \le t \le c$, the system is homogeneous with zero initial conditions:
   $$
   \begin{cases}
   y_1'' + 2y_1' + 2y_1 = 0, \\[2pt]
   y_1(0) = 0,\; y_1'(0) = 0.
   \end{cases}
   $$
   The solution is $y_1(t) \equiv 0$.

2. For $t \ge c$, we solve the same system with the impulse, using the final values from the first stage as initial conditions:
   $$
   \begin{cases}
   y_2'' + 2y_2' + 2y_2 = \delta(t - c), \\[2pt]
   y_2(c) = y_1(c),\; y_2'(c) = y_1'(c).
   \end{cases}
   $$

The overall solution is
$
y(t) =
\begin{cases}
y_1(t), & 0 \le t \le c, \\[2pt]
y_2(t), & t \ge c.
\end{cases}
$

**Analytical solution**:
$
y(t) = H(t - c)\, e^{-(t-c)} \sin(t - c).
$
Results from `example4.py`:
<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex4.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex4_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.5 Example 5 [Chasnov, p. 65]

Consider the second‑order ODE (Type 0b)
$
\begin{cases}
2y'' + y' + 2y = \delta(t - c), \\[2pt]
y(0) = y'(0) = 0, \\[2pt]
c = 2.
\end{cases}
$
Following the same splitting procedure:

- On $0 \le t \le c$:
  $$
  \begin{cases}
  2y_1'' + y_1' + 2y_1 = 0, \\[2pt]
  y_1(0) = 0,\; y_1'(0) = 0,
  \end{cases}
  $$
  giving $y_1(t) \equiv 0$.

- On $t \ge c$:
  $$
  \begin{cases}
  2y_2'' + y_2' + 2y_2 = \delta(t - c), \\[2pt]
  y_2(c) = y_1(c),\; y_2'(c) = y_1'(c).
  \end{cases}
  $$

**Analytical solution**:
$
y(t) = \frac{2}{\sqrt{15}}\, H(t - c)\, e^{-(t-c)/4} \sin\!\left(\frac{\sqrt{15}}{4}(t - c)\right).
$
Results from `example5.py`:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex5.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex5_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.6 Example 6 [Zill, p. 293]

Consider the second‑order ODE (Type 0b)
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 0,\; y'(0) = 0.
\end{cases}
$

Splitting yields:

- On $0 \le t \le 2\pi$: $y_1'' + y_1 = 0$, $y_1(0)=0$, $y_1'(0)=0$ → $y_1(t) \equiv 0$.
- On $t \ge 2\pi$: $y_2'' + y_2 = 4\delta(t - 2\pi)$, with $y_2(2\pi)=0$, $y_2'(2\pi)=0$.

**Analytical solution**:
$
y(t) = 4 H(t - 2\pi) \sin(t).
$
Results from `example6.py`:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex6.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex6_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.7 Example 7 [Zill, p. 293]

Consider the same system but with non‑zero initial conditions (Type 0b):
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 1,\; y'(0) = 0.
\end{cases}
$

Splitting:

- On $0 \le t \le 2\pi$: $y_1'' + y_1 = 0$, $y_1(0)=1$, $y_1'(0)=0$ → $y_1(t) = \cos t$.
- On $t \ge 2\pi$: $y_2'' + y_2 = 4\delta(t - 2\pi)$, with $y_2(2\pi) = \cos(2\pi)=1$, $y_2'(2\pi) = -\sin(2\pi)=0$.

**Analytical solution**:
$y(t) = \cos t + 4 H(t - 2\pi) \sin t.$

Results from `example7.py`:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex7.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex7_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.8 Example 8 [Nagy, p. 190]

Consider a system with two impulses (Type 0c):
$
\begin{cases}
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \\[2pt]
y(0) = y'(0) = 0.
\end{cases}
$

The solution follows the same principle as for Type 0b: the time axis is divided into intervals $[0,\pi]$, $[\pi,2\pi]$, and $[2\pi,\infty)$. The initial conditions for each subsequent interval are taken from the final values of the preceding interval.

**Analytical solution**:
$
y(t) = \frac{1}{2}\bigl[H(t - \pi) - H(t - 2\pi)\bigr] \sin(2t).
$
Results from `example8.py`:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex8.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex8_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

> **Remark:** This example illustrates that an impulsive load can both excite and suppress vibration.

#### 4.9 Example 9 (Third‑order system, Type 0a)

Consider the third‑order ODE
$
\begin{cases}
y''' + 2y'' + 2y' = \delta(t), \\[2pt]
y(0) = 0,\; y'(0) = 0,\; y''(0) = 0
\end{cases}
\;\Longrightarrow\;
\operatorname{IVP}(\{1,2,2,0\}, \delta(t), t_0=0, \mathbf{y}_0=\{0,0,0\}).
$
Here
$
A = \begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
2 & 2 & 1
\end{bmatrix},\quad
\mathbf{d} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
\;\Longrightarrow\;
A^{-1} = \begin{bmatrix}
 1 & 0 & 0 \\
-2 & 1 & 0 \\
 2 & -2 & 1
\end{bmatrix},\quad
A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
$
Thus
$
\mathbf{z}_0 = \mathbf{y}_0 + A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
$
The equivalent homogeneous system is
$
\begin{cases}
y''' + 2y'' + 2y' = 0 \\[2pt]
y(0)=0,\; y'(0)=0,\; y''(0)=1
\end{cases}.
$

**Analytical solution**:
$
y(t) = \frac{1}{2} - \frac{1}{2} e^{-t}\bigl(\sin t + \cos t\bigr).
$
Results from `example9.py`:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex9.png" alt="Time domain" style="width: 45%; height: auto; max-width: 100%;">
  <img src="ex9_Phase.png" alt="Phase plane" style="width: 45%; height: auto; max-width: 100%;">
</div>

#### 4.10 Additional examples

The following examples (from the literature) can be handled by the same method; we list them without detailed exposition:

- **Example 10.1** [Asadi, p. 62] – second‑order system.
- **Example 10.2** [Adkins, p. 435] – second‑order system.
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
### 6. Verification of Type 1 by Examples

We now verify the main result (5.5) of Section 5 using the examples collected in Appendix B. The first example illustrates a first‑order system (Type 0a), while the remaining examples are of Type 1. To validate the method, we have developed a set of Python scripts that perform the calculations and generate the corresponding plots.

#### 6.1 Example 10 [Ogata, p. 163]

Consider the transfer function
$
C(s) = \frac{1}{Ts + 1}.
$

The impulse response corresponds to the system
$
\begin{cases}
T y' + y = \delta(t), \\
y(0) = 0
\end{cases}
\;\Longrightarrow\;
g(t) = \operatorname{IVP}(\{T, 1\}, \delta(t), t_0 = 0, \mathbf{y}_0 = \{0\}).
$
From Appendix B, the analytical solution (impulse response) is
$
g(t) = \frac{1}{T}\, e^{-t/T}.
$
For $T = 2$, we compare the numerical solution of the homogeneous system with modified initial condition against this analytical solution. The script `example10.py` produces the following plot:

<div style="text-align: center;">
  <img src="ex10.png" alt="Time response for Example 10" style="width: 60%;">
</div>

#### 6.2 Example 11 [Xue, p. 380]

Transfer function:
$
TF = \frac{s}{(s+a)(s+b)} = \frac{s}{s^2 + (a+b)s + ab}.
$
The impulse response is the solution of
$
\begin{cases}
y'' + (a+b)y' + ab\,y = \delta'(t), \\
y(0) = y'(0) = 0
\end{cases}
\;\Longrightarrow\;
g(t) = \operatorname{IVP}(\{1, (a+b), ab\}, \{1, 0\}, t_0 = 0, \mathbf{y}_0 = \{0,0\}).
$
Analytical solution (Appendix B):
$
g(t) = \mathcal{L}^{-1}\!\left\{\frac{s}{(s+a)(s+b)}\right\}
      = \frac{1}{a-b}\bigl[ a e^{-a t} - b e^{-b t} \bigr].
$
We test the case $a = 1$, $b = 2$. The numerical solution, analytical solution, and error from `example11.py` are shown below:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex11.png" alt="Time domain" style="width: 45%;">
  <img src="ex11_Phase.png" alt="Phase plane" style="width: 45%;">
</div>

#### 6.3 Example 12 [Xue, p. 380]

Transfer function:
$
TF = \frac{s+d}{(s+a)(s+b)} = \frac{s+d}{s^2 + (a+b)s + ab}.
$
Impulse response system:
$
\begin{cases}
y'' + (a+b)y' + ab\,y = \delta'(t) + d\,\delta(t), \\
y(0) = y'(0) = 0
\end{cases}
\;\Longrightarrow\;
g(t) = \operatorname{IVP}(\{1, (a+b), ab\}, \{1, d\}, t_0 = 0, \mathbf{y}_0 = \{0,0\}).
$
Analytical solution:
$
g(t) = \mathcal{L}^{-1}\!\left\{\frac{s+d}{(s+a)(s+b)}\right\}
      = \frac{1}{b-a}\bigl[ (d-a)e^{-a t} - (d-b)e^{-b t} \bigr].
$

For $a = 1$, $b = 2$, $d = 1.5$, the script `example12.py` yields:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex12.png" alt="Time domain" style="width: 45%;">
  <img src="ex12_Phase.png" alt="Phase plane" style="width: 45%;">
</div>

#### 6.4 Example 13 [Xue, p. 380]

Transfer function:
$
TF = \frac{s+d}{s(s+a)(s+b)} = \frac{s+d}{s^3 + (a+b)s^2 + ab\,s}.
$
Impulse response system:
$
\begin{cases}
y''' + (a+b)y'' + ab\,y' = \delta'(t) + d\,\delta(t), \\
y(0) = y'(0) = y''(0) = 0
\end{cases}
\;\Longrightarrow\;
g(t) = \operatorname{IVP}(\{1, (a+b), ab, 0\}, \{1, d\}, t_0 = 0, \mathbf{y}_0 = \{0,0,0\}).
$
Analytical solution:
$
g(t) = \mathcal{L}^{-1}\!\left\{\frac{s+d}{s(s+a)(s+b)}\right\}
      = \frac{1}{ab}\left[ d - \frac{b(d-a)}{b-a}e^{-a t} + \frac{a(d-b)}{b-a}e^{-b t} \right].
$
For $a = 1$, $b = 2$, $d = 1.5$, the script `example13.py` produces:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex13.png" alt="Time domain" style="width: 45%;">
  <img src="ex13_Phase.png" alt="Phase plane" style="width: 45%;">
</div>

#### 6.5 Example 14 [Xue, p. 380]

Transfer function:
$
TF = \frac{s+a}{s^2 + \omega^2}.
$
Impulse response system:
$
\begin{cases}
y'' + \omega^2 y = \delta'(t) + a\,\delta(t), \\
y(0) = y'(0) = 0
\end{cases}
\;\Longrightarrow\;
g(t) = \operatorname{IVP}(\{1, 0, \omega^2\}, \{1, a\}, t_0 = 0, \mathbf{y}_0 = \{0,0\}).
$
Analytical solution:
$
g(t) = \mathcal{L}^{-1}\!\left\{\frac{s+a}{s^2+\omega^2}\right\}
      = \frac{\sqrt{a^2+\omega^2}}{\omega}\, \sin\!\left(\omega t + \tan^{-1}\!\left(\frac{\omega}{a}\right)\right).
$

For $a = 1.5$, $\omega = 0.7$, the script `example14.py` gives:

<div style="display: flex; justify-content: center; gap: 5%; align-items: flex-start;">
  <img src="ex14.png" alt="Time domain" style="width: 45%;">
  <img src="ex14_Phase.png" alt="Phase plane" style="width: 45%;">
</div>
## Appendix A

#### General Formulas
| Dirac Delta Function 1 | Laplace Transform |
|----------|----------|
| $ \int_{-\infty}^\infty \delta(x-a)f(x)\,dx = f(a) $   | $ \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt = F(s) $   |
| $ \int_{-\infty}^\infty \delta(x-a)\,dx = \int_{-\infty}^\infty \delta(x)\,dx = 1 $   | $ \mathcal{L}\{\delta(t-t_0)\} = e^{-st_0} $   |
| $ \int_{-\infty}^\infty f(x)\,\delta^{(n)}(x-a)\,dx = (-1)^n f^{(n)}(a) $   | $ \mathcal{L}\{\delta(t)\} = 1 $   |
| $ \int_{-\infty}^\infty f(x)\,\delta'(x-a)\,dx = -f'(a) $   | $ \mathcal{L}\{f'\} = s\mathcal{L}\{f\} - f(0) $   |
| $ \delta(-x) = \delta(x) $   | $ \mathcal{L}\{f''\} = s^2\mathcal{L}\{f\} - s f(0) - f'(0) $   |
## Appendix B: Reference Examples

This appendix collects the analytical solutions used throughout the main text to verify the proposed method. Examples are numbered consistently with the verification sections.

### Type 0 Examples (Single Delta Function)

##### Example 1 [Oliveira and Cortes, p. 3]
$
\begin{cases}
y'' + a y' = \delta(t), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = \frac{1}{a}\bigl(1 - e^{-a t}\bigr)
$

##### Example 2 [Finan, pp. 57–58]
$
\begin{cases}
2y'' + 4y' + 10y = \delta(t), \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
$

**Solution:** The original book contains a typographical error; the correct formula (verified with Mathcad 14 and WolframAlpha) is
$
y(t) = \frac{1}{4} e^{-t} \sin(2t)
$

##### Example 3 [Nagy, p. 189]
$
\begin{cases}
y'' + 2y' + 2y = \delta(t), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = e^{-t} \sin(t)
$

##### Example 4 [Nagy, p. 189]
$
\begin{cases}
y'' + 2y' + 2y = \delta(t - c), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = H(t - c)\, e^{-(t - c)} \sin(t - c)
$

##### Example 5 [Chasnov, p. 65]
$
\begin{cases}
2y'' + y' + 2y = \delta(t - 5), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) = \frac{2}{\sqrt{15}}\, H(t - 5)\, e^{-(t - 5)/4} \sin\!\left(\frac{\sqrt{15}}{4}(t - 5)\right)
$

##### Example 6 [Zill, p. 293]
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) =
\begin{cases}
0, & 0 \le t < 2\pi \\[4pt]
4\sin(t), & t \ge 2\pi
\end{cases}
$

##### Example 7 [Zill, p. 293]
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 1,\; y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = \cos(t) + 4H(t - 2\pi)\sin(t)
$

##### Example 8 [Nagy, p. 190] (Two impulses)
$
\begin{cases}
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) = \frac{1}{2}\bigl[H(t - \pi) - H(t - 2\pi)\bigr]\sin(2t)
$

##### Example 9 (Third‑order system)
$
\begin{cases}
y''' + 2y'' + 2y' = \delta(t), \\[2pt]
y(0) = y'(0) = y''(0) = 0
\end{cases}
$
**Solution:** obtained from WolframAlpha,
$
y(t) = \frac{1}{2} - \frac{1}{2}e^{-t}\bigl(\sin(t) + \cos(t)\bigr)
$

### Type 1 Examples (Derivatives of Delta)

##### Example 10 [Ogata, p. 163] (First‑order system)
Transfer function:
$
C(s) = \frac{1}{Ts + 1}
\qquad\Longrightarrow\qquad
g(t) = \frac{1}{T}\, e^{-t/T}
$

##### Example 11 [Xue, p. 380]
Inverse Laplace transform:
$
\mathcal{L}^{-1}\!\left\{\frac{s}{(s+a)(s+b)}\right\}
 = \frac{1}{a-b}\bigl[ a e^{-a t} - b e^{-b t} \bigr]
$

##### Example 12 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+d}{(s+a)(s+b)}\right\}
 = \frac{1}{b-a}\bigl[ (d-a)e^{-a t} - (d-b)e^{-b t} \bigr]
$

##### Example 13 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+d}{s(s+a)(s+b)}\right\}
 = \frac{1}{ab}\left[ d - \frac{b(d-a)}{b-a}e^{-a t} + \frac{a(d-b)}{b-a}e^{-b t} \right]
$

##### Example 14 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+a}{s^2+\omega^2}\right\}
 = \frac{\sqrt{a^2+\omega^2}}{\omega}\,
   \sin\!\left(\omega t + \tan^{-1}\!\left(\frac{\omega}{a}\right)\right)
$
## Appendix C

### Additional examples
Here are some additional examples, presented without detailed explanation.

##### Example C.1 [Asadi, p. 62], script: exampleC1.py
$
H(s) = \frac{100}{s^2 + 6s + 100}
$

##### Example C.2 [Adkins, p. 435], script: exampleC2.py
$
y'' + 20y = \delta_3, \quad y(0) = 0.10, \quad y'(0) = 0.
$

##### Example C.3 [Angeles, p. 132], script: exampleC3.py
$
\ddot{x} + \omega_n^2 x = \dot{\delta}(t), \quad x(0^-) = 0, \quad \dot{x}(0^-) = 0, \quad t > 0^-
$

##### Example C.4 [Boyce, p. 346], script: exampleC4.py
Find the analytical solution.

##### Example C.5 [Campbell, p. 263], script: exampleC5.py
$
y' + y = \delta(t - 1), \, y(0) = 1
$

##### Example C.6 [Dobrushkin, p. 342, Ex. 5.4.3], script: exampleC6.py
$
\mathcal{L}^{-1} \left[ \frac{\lambda + 5}{\lambda^2 + 2\lambda + 5} \right]
$

##### Example C.7 [Dobrushkin, p. 342, Ex. 5.4.5], script: exampleC7.py
$
\mathcal{L}^{-1} \left[ \frac{2\lambda^2 + 6\lambda + 10}{(\lambda - 1)(\lambda^2 + 4\lambda + 13)} \right] = e^t + e^{-2t} \cos 3t + \frac{1}{3}e^{-2t} \sin 3t, \quad t > 0.
$

### Additional exercises from the referenced books
Here is a list of books, with the page numbers where the corresponding example or exercise can be found:
Adkins (p. 319, p. 437, p. 448), Benaroya (p. 171), Boyce (p. 348), Brandt (p. 37, p. 101, p. 126), Campbell (p. 264), Chopra (p. 61, p. 489, p. 604, p. 616, p. 617, p. 626), Dobrushkin (p. 350, p. 688), Edwards (p. 504), Esfandiari (p. 353, p. 359, p. 365, p. 394, p. 485), Franklin (p. 115, p. 589), Goode (pp. 708–710), Gupta (p. 116), Holmes (p. 179, p. 181), Howell (p. 566), Inman (p. 287, p. 289, p. 429), Iyengar (p. 121, p. 154, p. 192), Jain (p. 358, p. 359, p. 409), James (p. 352, p. 353, pp. 365–367), Jazar (p. 188), Kabe (p. 300, p. 302, p. 469), Kani (p. 185, p. 198), Klee (p. 187), Kreyszig (p. 230, p. 231), Lathi (p. 160, p. 164), Logan (p. 169, p. 172, p. 344), MacCluer (p. 375), McOwen (p. 99), Meirovitch (p. 181, p. 371, p. 463, p. 615), Nagle (p. 404, p. 409, p. 410), Palm (p. 146, IRF, SDOF; p. 153, exercises; p. 205, IRF; p. 206, p. 209; p. 222, exercises; p. 266, exercises; p. 287, IRF; p. 538, p. 541, exercises), Peterson (p. 365), Polking (p. 232), Ricardo (p. 215, p. 216), Trench (p. 483), Tse (p. 184, p. 239), Williams (p. 63, p. 67, p. 76), Yang (p. 510, p. 522)
### REFERENCES

[1] Adkins, W. A., & Davidson, M. G. (2012). *Ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4614-3618-8

[2] Agarwal, R. P., & O'Regan, D. (2008). *An introduction to ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-0-387-71276-5

[3] Alam, J., Hu, G., Babu, H. M. H., & Xu, H. (2023). *Control engineering: Theory and applications*. CRC Press. https://doi.org/10.1201/9781003293859

[4] Anderson, B., & Rufer, S. (2018, August 13). *Control theory: A brief introduction*. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

[5] Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4419-1027-1

[6] Asadi, F., Bolanos, R. E., & Rodríguez, J. (2019). *Feedback control systems: The MATLAB®/Simulink® approach* (Synthesis Lectures on Control and Mechatronics, Lecture #5). Morgan & Claypool Publishers. https://doi.org/10.2200/S00909ED1V01Y201903CRM005

[7] Balachandran, B., & Magrab, E. B. (2009). *Vibrations* (2nd ed., International SI ed.). Cengage Learning. (ISBN: 9780534552060, 0495411256)

[8] Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781108615839

[9] Baruh, H. (2015). *Applied dynamics*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-0734-7) https://doi.org/10.1201/b18272

[10] Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press. (ISBN: 0340645806, 9780340645802, 0470235861, 9780470235867)

[11] Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-5265-7) https://doi.org/10.1201/b22347

[12] Benchohra, M., Henderson, J., & Ntouyas, S. (2006). *Impulsive differential equations and inclusions*. Hindawi Publishing Corporation. (ISBN: 977-5945-50-X)

[13] Beneš, K. (1978). On modelling dynamic systems excited by the Dirac function. *Sborník prací Přírodovědecké fakulty University Palackého v Olomouci. Matematika, 17*(1), 123–129. http://dml.cz/dmlcz/120062

[14] Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

[15] Boyce, W. E., & DiPrima, R. C. (2012). *Elementary differential equations and boundary value problems* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45831-0)

[16] Brandt, A. (2023). *Noise and vibration analysis: Signal analysis and experimental procedures* (2nd ed.). John Wiley & Sons Ltd. (ISBN: 978-1-118-96120-1) https://doi.org/10.1002/9781118961232

[17] Butcher, J. C. (2008). *Numerical methods for ordinary differential equations* (2nd ed.). John Wiley & Sons, Ltd. (ISBN: 978-0-470-72335-7) https://doi.org/10.1002/9780470753767

[18] Campbell, S. L., & Haberman, R. (2008). *Introduction to differential equations with dynamical systems*. Princeton University Press. (ISBN: 978-0-691-12474-6)

[19] Campos, L. M. B. C. (2020). *Linear differential equations and oscillators* (Vol. 4). CRC Press, Taylor & Francis Group. (ISBN: 978-0-367-13718-2) https://doi.org/10.1201/9780429028984

[20] Chasnov, J. R. (2009–2016). *Introduction to differential equations: Lecture notes for MATH 2351/2352*. The Hong Kong University of Science and Technology.

[21] Chopra, A. K. (2020). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed., SI units). Pearson Education Limited. (ISBN: 978-1-292-24918-6)

[22] Cohen, A. M. (2007). *Numerical methods for Laplace transform inversion*. Springer Science+Business Media. (ISBN: 9780387282619, 0387282610) https://doi.org/10.1007/978-0-387-68855-8

[23] Dobrushkin, V. A. (2015). *Applied differential equations: The primary course*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-2835-5) https://doi.org/10.1201/b17886

[24] Dorf, R. C., & Bishop, R. H. (2008). *Modern control systems: Solution manual* (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

[25] Duffy, D. G. (2015). *Green's functions with applications* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-5103-6) https://doi.org/10.1201/b17973

[26] Edwards, C. H., Penney, D. E., & Calvis, D. (2016). *Differential equations and boundary value problems: Computing and modeling* (5th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-10877-3)

[27] Esfandiari, R. S., & Lu, B. (2014). *Modeling and analysis of dynamic systems* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3) https://doi.org/10.1201/b16443

[28] Etkin, B. (2005). *Dynamics of atmospheric flight*. Dover Publications, Inc. (ISBN: 0-486-44522-4) (Original work published 1972)

[29] Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

[30] Finan, M. B. (n.d.). *Laplace transforms: Theory, problems, and solutions*. Arkansas Tech University.

[31] Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

[32] Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media, LLC. (ISBN: 978-0-387-79579-9, 9780387795805) https://doi.org/10.1007/978-0-387-79580-5

[33] Goode, S. W., & Annin, S. A. (2015). *Differential equations and linear algebra* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-321-96467-0)

[34] Gupta, A., & Verma, Y. P. (2020). *Automatic control engineering*. I.K. International Pvt. Ltd. (ISBN: 978-93-89583-74-8)

[35] Holmes, M. H. (2023). *Introduction to differential equations* (3rd ed.). Mark H. Holmes. (ISBN: 978-1-71147-191-4)

[36] Howell, K. B. (2020). *Ordinary differential equations: An introduction to the fundamentals* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-138-60583-1) https://doi.org/10.1201/9780429347429

[37] Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-13-287169-3)

[38] Iyengar, R. N. (2019). *Elements of mechanical vibration*. I.K. International Pvt. Ltd. (ISBN: 978-93-89633-34-4)

[39] Jack, H. (2015). *Dynamic system modeling and control*. Hugh Jack. (ISBN: 978-1-5089-9525-8)

[40] Jain, S. (2011). *Modeling & simulation using MATLAB®-Simulink®*. Wiley India Pvt. Ltd. (ISBN: 978-81-265-3005-2)

[41] James, G., Dyke, P., Burley, D., Clements, D., Craven, M., Reis, T., Searl, J., Stander, J., Steele, N., & Wright, J. (2018). *Advanced modern engineering mathematics* (5th ed.). Pearson Education Limited. (ISBN: 978-1-292-17434-1)

[42] Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG. (ISBN: 978-3-031-43485-3) https://doi.org/10.1007/978-3-031-43486-0

[43] Kabe, A. M., & Sako, B. H. (2020). *Structural dynamics: Fundamentals and advanced applications* (Vol. 1). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-821614-9) https://doi.org/10.1016/C2019-0-00137-8

[44] Karris, S. T. (2003). *Signals and systems with MATLAB® applications* (2nd ed.). Orchard Publications. (ISBN: 9780970951168, 0970951167)

[45] Kausel, E. (2017). *Advanced structural dynamics*. Cambridge University Press. (ISBN: 978-1-107-17151-0) https://doi.org/10.1017/9781316761403

[46] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications, SI*. Cengage Learning. (ISBN: 9781439062142)

[47] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications*. Cengage Learning. (ISBN-13: 978-1-4390-6212-8)

[48] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

[49] Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

[50] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

[51] Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

[52] Liu, X. (2018). *Systems control theory*. Walter de Gruyter GmbH; Science Press. (ISBN: 978-3-11-057494-4) https://doi.org/10.1515/9783110574951

[53] Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

[54] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

[55] MacCluer, B. D., Bourdon, P. S., & Kriete, T. L. (2019). *Differential equations: Techniques, theory, and applications*. American Mathematical Society. (ISBN: 978-1-4704-4797-7)

[56] McOwen, R. (2012). *Worldwide differential equations with linear algebra*. Worldwide Center of Mathematics, LLC. (ISBN: 978-0-9842071-2-1)

[57] Meirovitch, L. (1986). *Elements of vibration analysis* (Subsequent ed.). McGraw-Hill College. (ISBN: 978-0-07-041342-9)

[58] Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

[59] Nagle, R. K., Saff, E. B., & Snider, A. D. (2018). *Fundamentals of differential equations* (9th ed.). Pearson Education, Inc. (ISBN: 978-0-321-97706-9)

[60] Nagoor Kani, A. (2019). *Control systems engineering* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-892-6199-8)

[61] Nagy, G. (n.d.). *Ordinary differential equations*. Mathematics Department, Michigan State University.

[62] Nielsen, S. R. K. (2004). *Vibration theory, Vol. 1: Linear vibration theory* (3rd ed.). Department of Civil Engineering, Aalborg University. (U/ Vol. U2004-1)

[63] Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-615673-4)

[64] Oliveira, M. de, & Cortes, J. (2011, January 24). *Computing the impulse response*. http://control.ucsd.edu/mauricio/courses/mae143a/lectures/computingImpulseResponse.pdf

[65] Palm, W. J., III. (2010). *System dynamics* (2nd ed.). McGraw-Hill. (ISBN: 978-0-07-352927-1)

[66] Peterson, G. L., & Sochacki, J. S. (2014). *Linear algebra & differential equations* (Pearson New International ed.). Pearson Education Limited. (ISBN: 978-1-269-37450-7)

[67] Polking, J., Boggess, A., & Arnold, D. (2006). *Differential equations with boundary value problems* (2nd ed.). Pearson Prentice Hall. (ISBN: 0-13-186236-7)

[68] Ram, B. (2009). *Engineering mathematics*. Pearson Education. (ISBN: 978-81-317-2691-4)

[69] Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-212819-3)

[70] Ricardo, H. J. (2021). *A modern introduction to differential equations* (3rd ed.). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-823417-4) https://doi.org/10.1016/C2020-0-00717-2

[71] Schiff, J. L. (1999). *The Laplace transform: Theory and applications*. Springer-Verlag New York, Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

[72] Schmitz, T. L., & Smith, K. S. (2012). *Mechanical vibrations: Modeling and measurement*. Springer Science+Business Media, LLC. (ISBN: 978-1-4614-0459-0; e-ISBN: 978-1-4614-0460-6) https://doi.org/10.1007/978-1-4614-0460-6

[73] Shabana, A. A. (1996). *Theory of vibration: An introduction* (2nd ed.). Springer-Verlag. (ISBN: 978-1-4612-8456-7) https://doi.org/10.1007/978-1-4612-3976-5 (Reprinted from *Theory of vibration: An introduction*, by A. A. Shabana, 1991, Springer-Verlag)

[74] Silva, C. W. de. (2000). *Vibration: Fundamentals and practice*. CRC Press LLC. (ISBN: 0-8493-1808-4) https://doi.org/10.1201/9781420052510

[75] Strang, G. (2016). *Introduction to linear algebra: Manual for instructors* (5th ed.). Wellesley-Cambridge Press. (ISBN: 978-0-9802327-7-6)

[76] Thorby, D. (2008). *Structural dynamics and vibration in practice: An engineering handbook*. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

[77] Trench, W. F. (2024). *Elementary differential equations with boundary values problems*. LibreTexts. Retrieved December 19, 2024, from https://LibreTexts.org

[78] Tse, F. S., Morse, I. E., & Hinkle, R. T. (2018). *Mechanical vibrations: Theory and applications* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-879-6458-7)

[79] Weber, H. J., & Arfken, G. B. (2003). *Essential mathematical methods for physicists*. Academic Press. (ISBN: 978-0-12-059877-9) https://doi.org/10.1016/B978-0-12-059877-9.X5000-7

[80] Williams, R. L., II, & Lawrence, D. A. (2007). *Linear state-space control systems*. John Wiley & Sons, Inc. (ISBN: 978-0-471-73555-7) https://doi.org/10.1002/9780470117873

[81] Xue, D., Chen, Y., & Atherton, D. P. (2002, July 3). *Linear feedback control: Analysis and design with MATLAB*. Springer-Verlag.

[82] Xue, D., Chen, Y., & Atherton, D. P. (2007). *Linear feedback control: Analysis and design with MATLAB*. Society for Industrial and Applied Mathematics. (ISBN: 978-0-89871-638-2) https://doi.org/10.1137/1.9780898718621

[83] Yang, B., & Abramova, I. (2022). *Dynamic systems: Modelling, simulation, and analysis*. Cambridge University Press. (ISBN: 978-1-107-17979-0) https://doi.org/10.1017/9781316841051

[84] Zill, D. G. (2009). *A first course in differential equations with modeling applications* (9th ed.). Brooks/Cole, Cengage Learning. (ISBN-13: 978-0-495-10824-5) https://doi.org/10.1017/9781316841051
