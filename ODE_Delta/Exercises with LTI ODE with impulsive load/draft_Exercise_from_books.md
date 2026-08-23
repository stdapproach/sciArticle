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


---

## Additional Exercises

This section provides supplementary exercises and variations on the main problems. These exercises are designed to deepen understanding and explore edge cases.

Boyce: p.273-274 has many exercises

Bottega: p.236-238 couple 2nd order system with impulse load; p.269: Ex.4.4-4.6; p.429: MDOF system under impuls load; p.470: double pendulum under impulse load; p.488: Ex 8.17 elastically supported frame under struck; p.501 Ex 8.7; p.507: Ex 8.26; p.715: Ex 11.3 PDE "Determine the response of the rod it is struck on its right end by an impulse of magnitude"; p.718: Ex 11.17 "The beam is impacted at its left end"

Campbell: p.264 Exercises 1–8

Dorf: p.174 P2.36 "Determine the impulse response of the system"; p.178 "Consider the unity feedback system described in the block diagram ... Compute analytically the response of the system to an impulse disturbance"; p.392 CP5.1 "Obtain the impulse response analytically"

Edwards: 9.326 4.6 Problems 1-8, 15-16 (equality of solution by changing IC)

---

## References
Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-37792-4)

Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. (ISBN: 978-0-691-12474-6)

Dorf, R. C., & Bishop, R. H. (2008). Modern control systems: Solution manual (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

Edwards, C. H., & Penney, D. E. (2008). Elementary differential equations with boundary value problems (6th ed.). Pearson Education. ISBN 0-13-600613-2

## Impulse Response Analysis

### Exercise 2.1: First-Order System Response to Impulse
**Source:** Karris (2003), Cohen (2007)
**Difficulty:** Beginner

Consider the first-order LTI system:
$$\dot{x}(t) + 2x(t) = \delta(t)$$

with initial condition $x(0^-) = 0$.
---

### Exercise 2.2: Impulse Response via Laplace Transform
**Source:** Boyce & DiPrima (2012), Cohen (2007)
**Difficulty:** Intermediate

Given the system transfer function:
$$H(s) = \frac{1}{s^2 + 3s + 2}$$

---

## Modified Initial Conditions

### Exercise 3.1: IC Change Under Impulse (Second-Order System)
**Source:** Meirovitch (2001), Beards (1996), Schmitz & Smith (2012)
**Difficulty:** Intermediate

Consider the second-order system:
$$\ddot{x}(t) + 4\dot{x}(t) + 3x(t) = \delta(t)$$

with pre-impulse conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.

---

### Exercise 3.2: Damped Oscillator with Impulsive Force
**Source:** Meirovitch (2001), Inman (2014)
**Difficulty:** Intermediate

A damped harmonic oscillator with mass $m = 1$ kg, damping $c = 0.4$ N·s/m, and stiffness $k = 1$ N/m receives an impulse of magnitude $J = 2$ N·s at $t = 0$.

$$\ddot{x}(t) + 0.4\dot{x}(t) + x(t) = 2\delta(t)$$

Initial conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.

---

## Laplace Transform Methods

### Exercise 4.1: Solving ODE with Delta Forcing via Laplace
**Source:** Schiff (1999), Cohen (2007), Zill (2009)
**Difficulty:** Intermediate

Solve using Laplace transform:
$$\ddot{x} + 5\dot{x} + 6x = \delta(t)$$

with $x(0) = 0, \dot{x}(0) = 0$.

---

### Exercise 4.2: Multiple Impulses
**Source:** Karris (2003), Schiff (1999)
**Difficulty:** Advanced

Consider the system:
$$\dot{x}(t) + 3x(t) = \delta(t) + 2\delta(t - 2)$$

with $x(0^-) = 0$.

---

## Second-Order LTI Systems

### Exercise 5.1: Delta and Delta Derivative Forcing
**Source:** Oliveira & Cortes (2011), Schiff (1999)
**Difficulty:** Advanced

Consider:
$$\ddot{x}(t) + 2\dot{x}(t) + x(t) = \delta(t) + \delta'(t)$$

with $x(0^-) = 0, \dot{x}(0^-) = 0$.

---

### Exercise 5.2: Underdamped System with Impulse Train
**Source:** Meirovitch (2001)
**Difficulty:** Advanced

A second-order underdamped system:
$$\ddot{x} + 0.5\dot{x} + 2x = f(t)$$

where $f(t) = \delta(t) + \delta(t - 3) + \delta(t - 6)$ (three impulses at $t = 0, 3, 6$)

Initial conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.
---

## Control Theory Applications

### Exercise 6.2: Transfer Function and Impulse Response
**Source:** Ogata (2010), Karris (2003)
**Difficulty:** Intermediate

Given the transfer function:
$$H(s) = \frac{s + 1}{(s + 1)(s + 2)(s + 3)}$$

---

## Structural Dynamics & Vibrations

### Exercise 7.1: Impact Loading on Structures
**Source:** Beards (1996), Schmitz & Smith (2012)
**Difficulty:** Intermediate

A structure modeled as a second-order system experiences an impact:
$$m\ddot{x} + c\dot{x} + kx = F(t)$$

where the impact imparts impulse $J = 10$ N·s.

Given: $m = 1$ kg, $c = 2$ N·s/m, $k = 10$ N/m, pre-impact at rest.

---

## Advanced Problems

### Exercise 8.2: Coupled System with Impulsive Forcing
**Source:** Meirovitch (2001)
**Difficulty:** Advanced

A two-degree-of-freedom system:
$$\begin{bmatrix} m_1 & 0 \\ 0 & m_2 \end{bmatrix} \begin{bmatrix} \ddot{x}_1 \\ \ddot{x}_2 \end{bmatrix} + \begin{bmatrix} c_1 + c_c & -c_c \\ -c_c & c_2 + c_c \end{bmatrix} \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} + \begin{bmatrix} k_1 + k_c & -k_c \\ -k_c & k_2 + k_c \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} \delta(t) \\ 0 \end{bmatrix}$$

with $m_1 = m_2 = 1$, $k_1 = k_2 = 10$, $k_c = 5$, $c_1 = c_2 = 0.2$, $c_c = 0.1$.

Initial conditions: $x_1(0^-) = x_2(0^-) = \dot{x}_1(0^-) = \dot{x}_2(0^-) = 0$.
---


**Document Status:** Draft  
**Maintenance:** Updated as exercises are solved and verified  
**Contributing:** To add exercises, reference source books and specify difficulty level
