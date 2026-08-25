# Exercises from Books: LTI ODE with Impulsive Loads

## Introduction

This document compiles and organizes exercises from the reference books listed in `BOOKS_DELTA_EXAMPLES_TABLE_SORTED.md`. Exercises are categorized by type and difficulty level, with references to source materials.

**Last Updated:** August 23, 2026

---

## Table of Contents

1. [Balachandran & Magrab](#balachandran--magrab)
2. [Additional Exercises](#additional-exercises)
3. [References](#references)
4. [Dirac Delta Function Basics](#dirac-delta-function-basics)
5. [Impulse Response Analysis](#impulse-response-analysis)
6. [Modified Initial Conditions](#modified-initial-conditions)
7. [Laplace Transform Methods](#laplace-transform-methods)
8. [Second-Order LTI Systems](#second-order-lti-systems)
9. [Control Theory Applications](#control-theory-applications)
10. [Structural Dynamics & Vibrations](#structural-dynamics--vibrations)
11. [Advanced Problems](#advanced-problems)

---

## Boyce & DiPrima Elementary differential equations and boundary value problems
p.272 Initial Value Problem (IVP) for 2nd order with zero Initial Condition (IC)
$$
\begin{aligned}
&2y'' + y' + 2y = \delta(t - 5) \\
&y(0) = 0, \quad y'(0) = 0
\end{aligned}
\implies y(t) = 
\begin{cases}
0, & t < 5 \\[6pt]
\dfrac{2}{\sqrt{15}} e^{-(t-5)/4} \sin\left(\dfrac{\sqrt{15}}{4}(t-5)\right), & t \ge 5
\end{cases}
$$

## Bottega Engineering vibrations
p.238: Example 4.2 A tethered 1 pound ball hangs in the vertical plane
when it is tapped with a racket. Following the tap the ball is observed to exhibit oscillatory motion of amplitude 0.2 radians with a period of 2 seconds. Determine the impulse imparted by the racket.

## Campbell & Haberman Introduction to differential equations with dynamical systems
p.263 IVP for 1st order system $$ y' + y = \delta(t - 1), \, y(0) = 1 \implies  y(t)=\begin{cases}
e^{-t}, & t < 1 \\[4pt]
e^{-t} + e^{-(t-1)}, & t \ge 1
\end{cases}$$

## Edwards & Penney Elementary differential equations with boundary value problems
p.318
The IVP is
$$
  x'' + 4x = 8\delta_{2\pi}(t); \; x(0) = 3, \; x'(0) = 0 \implies xy(t)= \begin{cases}
3\cos 2t, & t < 2\pi \\[4pt]
3\cos 2t + 4\sin 2t, & t \ge 2\pi
\end{cases}
$$

## Esfandiari & Lu Modeling and analysis of dynamic systems

p.57 "Example 2.27: Initial Condition ≠ Initial Value"
$$
 \ddot{x} + \dot{x} + 2x = \delta(t), \, x(0^-) = 0, \, \dot{x}(0^-) = 0
\implies \dot{x}(0^+) =  1
$$

p.343 "Impulse Response of First-Order Systems"
$$ x(t) = e^{-t/\tau} x_0 + \frac{A}{\tau} e^{-t/\tau} $$
where A - impulse's magnitude $\tau$ - cofficient for higher derivative in ODE.


## Franklin & Powell & Emami-Naeini Feedback control of dynamic systems

p. 110
$$
\dot{y} + ky = u = \delta(t), y(0) = 0 \equiv \dot{y} + ky = 0, \quad y(0^+) = 1
$$

p.151
$$ 
H(s) = \frac{2s + 1}{(s+1)^2 + 2^2} \implies h(t) = \left( 2e^{-t} \cos 2t - \frac{1}{2}e^{-t} \sin 2t \right) 1(t)
$$

## Lathi Linear systems and signals
p.164 "EXAMPLE 2.5 Impulse Response via Impulse Matching"
Find the impulse response h(t) for a system specified by (D2 +5D+6)y(t) = (D+1)x(t)
Solution
$$ h(t) = (-e^{-2t} + 2e^{-3t})u(t) $$

p.166 EXAMPLE 2.6
Determine the unit impulse response h(t) for a system specified by the equation
(D^2 +3D+2)y(t) = Dx(t)
Solution
$$ h(t) = (-e^{-t} + 2e^{-2t})u(t) $$

p.167 DRILL 2.4 Finding the Impulse Response
Determine the unit impulse response of LTIC systems described by the following equations:

(a) $ (D + 2)y(t) = (3D + 5)x(t) \implies h(t)=3\delta(t) - e^{-2t}u(t) $

(b) $ D(D + 2)y(t) = (D + 4)x(t) \implies h(t)=(2 - e^{-2t})u(t)$

(c) $ (D^2 + 2D + 1)y(t) = Dx(t) \implies h(t)=(1 - t)e^{-t}u(t)$

p.364 DRILL 4.7 Laplace Transform to Solve a Second-Order Linear Differential Equation
$$
\frac{d^2y(t)}{dt^2} + 4\frac{dy(t)}{dt} + 3y(t) = 2\frac{dx(t)}{dt} + x(t) \\
y(0^-) = 1 \quad \text{and} \quad \dot{y}(0^-) = 2 \implies \boxed{y(t) = \frac{1}{3}\left(1 + 9e^{-t} - 7e^{-3t}\right)u(t)}
$$

## Nagy Ordinary differential equations
p.202
$$
y'' + \omega_0^2 y = f_0 \delta(t - t_0), \quad y(0) = y_0, \quad y'(0) = 0 \\
\implies y(t) = y_0 \cos(\omega_0 t) + \frac{f_0}{\omega_0} u(t - t_0) \sin(\omega_0 (t - t_0))
$$

p.205 Example 3.4.6. Find the impulse response function
$$
L(y) = y'' + 2y' + 2y \implies y_\delta(t) = u(t-c)e^{-(t-c)}\sin(t-c)
$$

p.205 Example 3.4.7. Find the solution y to the initial value problem
$$
y'' - y = -20 \delta(t-3), \quad y(0) = 1, \quad y'(0) = 0 \implies y(t) = \cosh(t) - 20 \, u(t-3) \, \sinh(t-3)
$$

p.206 Example 3.4.8. Find the solution to the initial value problem
$$
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \quad y(0) = 0, \quad y'(0) = 0 \\
\implies y(t) = \frac{1}{2} \left[ u(t - \pi) - u(t - 2\pi) \right] \sin(2t)
$$

## Nagle Fundamentals of differential equations
p.403 Example 4 A linear system is governed by the differential equation
$$
y'' + 2y' + 5y \implies = \frac{1}{2} e^{-t} \sin 2t
$$

p.409 Example 1
$$
\frac{d^2x}{dt^2} + 9x = 3\delta(t - \pi); \quad x(0) = 1, \quad \frac{dx}{dt}(0) = 0, \\
\implies x(t) = 
\begin{cases} 
\cos 3t, & t < \pi, \\ 
\cos 3t - \sin 3t, & \pi < t
\end{cases}
$$

## Ogata Modern control engineering
p.163 Unit-Impulse Response of First-Order Systems
$$
C(s) = \frac{1}{Ts + 1} \implies c(t) = \frac{1}{T} e^{-t/T}, \quad \text{for } t \geq 0
$$

p.178 Impulse Response of Second-Order Systems
$$
C(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2} \implies \\
$$

For $ 0 \leq \zeta < 1 $,

$$
c(t) = \frac{\omega_n}{\sqrt{1 - \zeta^2}} e^{-\zeta \omega_n t} \sin \omega_n \sqrt{1 - \zeta^2} t, \quad \text{for } t \geq 0
$$

For $ \zeta = 1 $,

$$
c(t) = \omega_n^2 t e^{-\omega_n t}, \quad \text{for } t \geq 0
$$

For $ \zeta > 1 $,

$$
c(t) = \frac{\omega_n}{2 \sqrt{\zeta^2 - 1}} e^{-\left( \zeta - \sqrt{\zeta^2 - 1} \right) \omega_n t} - \frac{\omega_n}{2 \sqrt{\zeta^2 - 1}} e^{-\left( \zeta + \sqrt{\zeta^2 - 1} \right) \omega_n t}, \quad \text{for } t \geq 0
$$


## Shabana Vibration of discrete and continuous systems
p.41
Example 1.10
Find the response of the single degree of freedom system shown in Fig. 17 to the
rectangular impulsive force shown in Fig. 16, where m = 10 kg, k = 9,000 N/m,
c = 18 N· slm, and Fo = 10,000 N. The force is assumed to act at time t = 0 and
the impact interval is assumed to be 0.005 s.
The system response to the impulsive force is then given by
$$
\begin{aligned}
x(t) &= \frac{l}{m\omega_d} e^{-\xi\omega t} \sin \omega_d t = \frac{50}{(10)(29.986)} e^{-(0.03)(30)t} \sin 29.986t = 0.1667e^{-0.9t} \sin 29.986t
\end{aligned}
$$

## Xie Differential equations for engineers
p.258 
Example 6.11
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s-2)^5} \right\} \implies f(t) = \frac{1}{12} e^{2t} t^3 (2 + t)
$$

Example 6.12
$$
\mathcal{L}^{-1} \left\{ \frac{1 + e^{-3s}}{s^4} \right\} \implies \frac{1}{6} \left[ t^3 + (t-3)^3 u(t-3) \right]
$$

Example 6.13
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s^2 + 4)^2} \right\} \implies \frac{1}{4} l \sin 2l
$$

Example 6.14
$$
\mathcal{L}^{-1} \left\{ \frac{8}{(s-1)(s^2+2s+5)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = e^t - e^{-t} \cos 2t - e^{-t} \sin 2t
$$

Example 6.15
$$
\mathcal{L}^{-1} \left\{ \frac{s+1}{(s^2+1)(s^2+9)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{8} \left( \cos t + \sin t - \cos 3t - \frac{1}{3} \sin 3t \right)
$$

## Xue & Chen & Atherton Linear feedback control: Analysis and design with MATLAB
??

---

## Additional Exercises

This section provides supplementary exercises and variations on the main problems. These exercises are designed to deepen understanding and explore edge cases.

Boyce: p.273-274 has many exercises

Bottega: p.236-238 couple 2nd order system with impulse load; p.269: Ex.4.4-4.6; p.429: MDOF system under impuls load; p.470: double pendulum under impulse load; p.488: Ex 8.17 elastically supported frame under struck; p.501 Ex 8.7; p.507: Ex 8.26; p.715: Ex 11.3 PDE "Determine the response of the rod it is struck on its right end by an impulse of magnitude"; p.718: Ex 11.17 "The beam is impacted at its left end"

Campbell: p.264 Exercises 1–8

De Oliveira
p.82 Problem 3.41 "Compute the inverse Laplace transform of the following complex-valued functions"
p.83 Problem 3.44 "Compute the inverse Laplace transform"

Dorf: p.174 P2.36 "Determine the impulse response of the system"; p.178 "Consider the unity feedback system described in the block diagram ... Compute analytically the response of the system to an impulse disturbance"; p.392 CP5.1 "Obtain the impulse response analytically"

Edwards: 9.326 4.6 Problems 1-8, 15-16 (equality of solution by changing IC)

Esfandiari: p.59 Problems 19 through 24; p.62 Problem 10 "Solve the IVP"
p.352 "8.3.2   Impulse Response of Second-Order Systems"
p.353 "Example 8.5: Impulse Response"
p.359  "Example 8.8: Impulse Response"
p.363  "PROBLEM SET 8.2"/7-11, 20

Franklin:
p.230 EXAMPLE 4.9
p.589 Problem 7.20

Inman
p.221 Example 3.1.1
p.222 Example 3.1.3
p.224 Example 3.1.4
p.232 Example 3.2.3
p.245 Example 3.4.4, Example 3.4.5
p.287 Problems 3.1-3.6, 3.10-3.13
p.377 Example 4.8.1 MDOF system with impulse
p.382  Example 4.8.2 MDOF system with impulse
p.386 Example 4.8.3 MDOF system with impulse
p.428 Problem 4.76
p.429 Problem 4.78
p.440 Example 5.1.2
p.557 Example 6.8.1 "Calculate the forced response of the string fixed at both ends ... subject to unit impulse"
p.571 Problem 6.67

Karris
p.6-2 "Example 6.1"
p.6-3 "Example 6.2"

Kelly
p.317 EXAMPLE 5 .1
p.374 Problem 5.21-5.23

Lathi: p.471 Problem 4.3-6

Meirovitch: p.371 Problem 7.49
p.463 Problem 8.38, 8.42, 8.44

Nagle p.404 7.8 EXERCISES 5-12, 23-28
p.410 7.9 Exercises 13-29, 35
p.416 REVIEW PROBLEMS FOR CHAPTER 7 Problem 29-30

Ogata
p.196 MATLAB Program 5–8 "Unit-Impulse Response of G(s) = 1/(s^2 + 0.2s + 1)"
p.264 B–5–4 "Consider the system shown in Figure 5–72.The system is initially at rest. Suppose that the cart is set into motion by an impulsive force whose strength is unity. Can it be stopped by another such impulsive force?"
p.264 B-5-5, B-5-6
p.265 B-5-10/11
p.267 B-5-16

Rao
p.382 "4.5.1 Response to an Impulse"
p.384 EXAMPLE 4.7 "Response of a Structure Under Impact"
p.385 EXAMPLE 4.8 Response of a Structure Under Double Impact
p.407  EXAMPLE 4.9 Unit Impulse Response of a First-Order System
p.409  EXAMPLE 4.21 Unit Impulse Response of a Second-Order System
p.437 EXAMPLE 4.33 Impulse Response of a Structure
p.511 EXAMPLE 5.12 Response Under Impulse Using Laplace Transform Method

Schiff
p.87 Exercises 2.5 1-7

Schabana
p.45 Problems 1.3, 1.9

Thorby
p.51 Example 3.2

Xue
p.76 Example 3.20. Consider again the system model studied in Example 3.17. The impulse
response of the system can be obtained as shown in Figure 3.11:
>> G=tf([10 20],[10 23 26 23 10],’ioDelay’,1); impulse(G, 30);

p.106 Problem 9
Find impulse response for the system:
$$
\frac{18s^7 + 514s^6 + 5982s^5 + 36380s^4 + 122664s^3 + 222088s^2 + 185760s + 40320}{s^8 + 36s^7 + 546s^6 + 4536s^5 + 22449s^4 + 67284s^3 + 118124s^2 + 109584s + 40320}
$$

---

## References
Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-37792-4)

Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. (ISBN: 978-0-691-12474-6)

De Oliveira, M. C. (2017). Fundamentals of linear control: A concise approach. Cambridge University Press. https://doi.org/10.1017/9781316941409 ISBN 978-1-107-18752-8 Hardback

Dorf, R. C., & Bishop, R. H. (2008). Modern control systems: Solution manual (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

Edwards, C. H., & Penney, D. E. (2008). Elementary differential equations with boundary value problems (6th ed.). Pearson Education. ISBN 0-13-600613-2

Esfandiari, R. S., & Lu, B. (2014). Modeling and analysis of dynamic systems (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3)
https://doi.org/10.1201/b16443

Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). Feedback control of dynamic
systems (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

Inman, D. J. (2014). Engineering vibration (4th ed.). Pearson Education, Inc. (ISBN:
978-0-13-287169-3)

Karris, S. T. (2003). Signals and systems with MATLAB® applications (2nd ed.). Orchard Publications. (ISBN: 9780970951168, 0970951167)

Kelly, S. G. (2012). Mechanical vibrations: Theory and applications, SI. Cengage Learning. (ISBN: 9781439062142)

Lathi, B. P., & Green, R. A. (2018). Linear systems and signals (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

Meirovitch, L. (2001). Fundamentals of vibrations (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

Nagy, G. (n.d.). Ordinary differential equations. Mathematics Department, Michigan State University

Nagle, R. K., Saff, E. B., & Snider, A. D. (2018). Fundamentals of differential equations
(9th ed.). Pearson Education, Inc. (ISBN: 978-0-321-97706-9)

Ogata, K. (2010). Modern control engineering (5th ed.). Pearson Education, Inc. (ISBN-
13: 978-0-13-615673-4)

Rao, S. S. (2011). Mechanical vibrations (5th ed.). Pearson Education. ISBN 978-0-13-212819-3

Schiff, Joel L. (1999). The Laplace transform: Theory and applications. Springer-Verlag New York,
Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

Shabana, A. A. (1997). Vibration of discrete and continuous systems (2nd ed.). Springer-Verlag. https://doi.org/10.1007/978-1-4612-4036-5 Print ISBN-13: 978-1-4612-8474-1

Thorby, D. (2008). Structural dynamics and vibration in practice: An engineering handbook. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

Xie, W.-C. (2010). Differential equations for engineers. Cambridge University Press. ISBN-13 978-0-521-19424-2

Xue, D., Chen, Y., & Atherton, D. P. (2007). Linear feedback control: Analysis and design with MATLAB. Society for Industrial and Applied Mathematics. ISBN 978-0-898716-38-2


**Document Status:** Draft  
**Maintenance:** Updated as exercises are solved and verified  
**Contributing:** To add exercises, reference source books and specify difficulty level
