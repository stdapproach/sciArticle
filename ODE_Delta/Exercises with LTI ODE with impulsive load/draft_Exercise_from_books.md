# Exercises from Books: LTI ODE with Impulsive Loads

## Introduction

This document compiles and organizes exercises from the reference books listed in `BOOKS_DELTA_EXAMPLES_TABLE_SORTED.md`. Exercises are categorized by type and difficulty level, with references to source materials.

**Last Updated:** August 23, 2026

---

## Table of Contents

### Quick Navigation by Difficulty
- 🟢 [Beginner Exercises](#beginner)
- 🟡 [Intermediate Exercises](#intermediate)
- 🔴 [Advanced Exercises](#advanced)

### Full Exercise List

1. **[Dirac Delta Function Basics](#dirac-delta-function-basics)** (2 exercises)
   - 1.1 [Delta Function Properties](#exercise-11-delta-function-properties) — 🟢 Beginner
   - 1.2 [Delta Derivatives in ODE](#exercise-12-delta-derivatives-in-ode) — 🟡 Intermediate

2. **[Impulse Response Analysis](#impulse-response-analysis)** (2 exercises)
   - 2.1 [First-Order System Response to Impulse](#exercise-21-first-order-system-response-to-impulse) — 🟢 Beginner
   - 2.2 [Impulse Response via Laplace Transform](#exercise-22-impulse-response-via-laplace-transform) — 🟡 Intermediate

3. **[Modified Initial Conditions](#modified-initial-conditions)** (2 exercises)
   - 3.1 [IC Change Under Impulse (Second-Order System)](#exercise-31-ic-change-under-impulse-second-order-system) — 🟡 Intermediate
   - 3.2 [Damped Oscillator with Impulsive Force](#exercise-32-damped-oscillator-with-impulsive-force) — 🟡 Intermediate

4. **[Laplace Transform Methods](#laplace-transform-methods)** (2 exercises)
   - 4.1 [Solving ODE with Delta Forcing via Laplace](#exercise-41-solving-ode-with-delta-forcing-via-laplace) — 🟡 Intermediate
   - 4.2 [Multiple Impulses](#exercise-42-multiple-impulses) — 🔴 Advanced

5. **[Second-Order LTI Systems](#second-order-lti-systems)** (2 exercises)
   - 5.1 [Delta and Delta Derivative Forcing](#exercise-51-delta-and-delta-derivative-forcing) — 🔴 Advanced
   - 5.2 [Underdamped System with Impulse Train](#exercise-52-underdamped-system-with-impulse-train) — 🔴 Advanced

6. **[Control Theory Applications](#control-theory-applications)** (2 exercises)
   - 6.1 [Step and Impulse Response Relationship](#exercise-61-step-and-impulse-response-relationship) — 🟡 Intermediate
   - 6.2 [Transfer Function and Impulse Response](#exercise-62-transfer-function-and-impulse-response) — 🟡 Intermediate

7. **[Structural Dynamics & Vibrations](#structural-dynamics--vibrations)** (2 exercises)
   - 7.1 [Impact Loading on Structures](#exercise-71-impact-loading-on-structures) — 🟡 Intermediate
   - 7.2 [Vibration Impulse Response](#exercise-72-vibration-impulse-response) — 🔴 Advanced

8. **[Advanced Problems](#advanced-problems)** (2 exercises)
   - 8.1 [System with Parametric Impulses](#exercise-81-system-with-parametric-impulses) — 🔴 Advanced
   - 8.2 [Coupled System with Impulsive Forcing](#exercise-82-coupled-system-with-impulsive-forcing) — 🔴 Advanced

### References & Resources
- [Solutions and References](#solutions-and-references)
- [Suggestions for Extension](#suggestions-for-extension)

---

## Dirac Delta Function Basics

### Exercise 1.1: Delta Function Properties
**Source:** Schiff (1999), Karris (2003)
**Difficulty:** Beginner

Verify the following properties of the Dirac delta function δ(t):

1. $\int_{-\infty}^{\infty} \delta(t) \, dt = 1$ (sifting property)
2. $\int_{-\infty}^{\infty} f(t) \delta(t - a) \, dt = f(a)$ (filtering property)
3. $t \cdot \delta(t) = 0$
4. $\delta(at) = \frac{1}{|a|} \delta(t)$ (scaling property)

**Questions:**
- a) Prove the sifting property using the definition of δ(t)
- b) Apply the filtering property to find $\int_{-\infty}^{\infty} (3t^2 + 2t + 1) \delta(t - 2) \, dt$
- c) Show that $\delta'(t)$ (derivative of delta) satisfies $\int_{-\infty}^{\infty} f(t) \delta'(t) \, dt = -f'(0)$

---

### Exercise 1.2: Delta Derivatives in ODE
**Source:** Oliveira & Cortes (2011), Schiff (1999)
**Difficulty:** Intermediate

Consider the forcing terms:
- $f_1(t) = \delta(t)$ (Dirac delta)
- $f_2(t) = \delta'(t)$ (first derivative of delta)

**Question:** For a second-order LTI system, explain physically and mathematically how these forcing terms differ in their effect on initial conditions.

---

## Impulse Response Analysis

### Exercise 2.1: First-Order System Response to Impulse
**Source:** Karris (2003), Cohen (2007)
**Difficulty:** Beginner

Consider the first-order LTI system:
$$\dot{x}(t) + 2x(t) = \delta(t)$$

with initial condition $x(0^-) = 0$.

**Questions:**
- a) Find the impulse response $h(t)$ for $t \geq 0$
- b) Determine the change in initial condition at $t = 0$ due to the impulse
- c) Sketch the response for $t \geq 0$

---

### Exercise 2.2: Impulse Response via Laplace Transform
**Source:** Boyce & DiPrima (2012), Cohen (2007)
**Difficulty:** Intermediate

Given the system transfer function:
$$H(s) = \frac{1}{s^2 + 3s + 2}$$

**Questions:**
- a) Find the impulse response $h(t)$ by taking the inverse Laplace transform
- b) Verify that $H(s) = \mathcal{L}\{h(t)\}$
- c) Discuss the stability of the system based on the poles

---

## Modified Initial Conditions

### Exercise 3.1: IC Change Under Impulse (Second-Order System)
**Source:** Meirovitch (2001), Beards (1996), Schmitz & Smith (2012)
**Difficulty:** Intermediate

Consider the second-order system:
$$\ddot{x}(t) + 4\dot{x}(t) + 3x(t) = \delta(t)$$

with pre-impulse conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.

**Questions:**
- a) Determine the post-impulse conditions $x(0^+)$ and $\dot{x}(0^+)$
- b) Solve for the complete response $x(t)$ for $t \geq 0$
- c) Verify that the impulse changes only the velocity, not the position

---

### Exercise 3.2: Damped Oscillator with Impulsive Force
**Source:** Meirovitch (2001), Inman (2014)
**Difficulty:** Intermediate

A damped harmonic oscillator with mass $m = 1$ kg, damping $c = 0.4$ N·s/m, and stiffness $k = 1$ N/m receives an impulse of magnitude $J = 2$ N·s at $t = 0$.

$$\ddot{x}(t) + 0.4\dot{x}(t) + x(t) = 2\delta(t)$$

Initial conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.

**Questions:**
- a) Find the post-impulse velocity $\dot{x}(0^+)$
- b) Classify the system (underdamped, critically damped, or overdamped)
- c) Solve for $x(t)$ and sketch the response
- d) Interpret the result physically (what happens to the oscillator?)

---

## Laplace Transform Methods

### Exercise 4.1: Solving ODE with Delta Forcing via Laplace
**Source:** Schiff (1999), Cohen (2007), Zill (2009)
**Difficulty:** Intermediate

Solve using Laplace transform:
$$\ddot{x} + 5\dot{x} + 6x = \delta(t)$$

with $x(0) = 0, \dot{x}(0) = 0$.

**Questions:**
- a) Take the Laplace transform of both sides
- b) Solve for $X(s)$
- c) Find the inverse Laplace transform to get $x(t)$
- d) Verify the solution satisfies the ODE

---

### Exercise 4.2: Multiple Impulses
**Source:** Karris (2003), Schiff (1999)
**Difficulty:** Advanced

Consider the system:
$$\dot{x}(t) + 3x(t) = \delta(t) + 2\delta(t - 2)$$

with $x(0^-) = 0$.

**Questions:**
- a) Use Laplace transform to solve for $x(t)$
- b) Identify the response due to each impulse separately
- c) Sketch the complete response showing the effect of both impulses
- d) Find the value of $x(t)$ at $t = 1, 2, 3$

---

## Second-Order LTI Systems

### Exercise 5.1: Delta and Delta Derivative Forcing
**Source:** Oliveira & Cortes (2011), Schiff (1999)
**Difficulty:** Advanced

Consider:
$$\ddot{x}(t) + 2\dot{x}(t) + x(t) = \delta(t) + \delta'(t)$$

with $x(0^-) = 0, \dot{x}(0^-) = 0$.

**Questions:**
- a) What are the post-impulse conditions $x(0^+)$ and $\dot{x}(0^+)$?
- b) Solve using Laplace transform
- c) Compare the response to $\delta(t)$ alone vs. $\delta(t) + \delta'(t)$
- d) Discuss the physical interpretation of including $\delta'(t)$ in the forcing

---

### Exercise 5.2: Underdamped System with Impulse Train
**Source:** Meirovitch (2001)
**Difficulty:** Advanced

A second-order underdamped system:
$$\ddot{x} + 0.5\dot{x} + 2x = f(t)$$

where $f(t) = \delta(t) + \delta(t - 3) + \delta(t - 6)$ (three impulses at $t = 0, 3, 6$)

Initial conditions: $x(0^-) = 0, \dot{x}(0^-) = 0$.

**Questions:**
- a) Find the response to each impulse separately
- b) Determine the total response using superposition
- c) Plot the response for $0 \leq t \leq 10$ seconds
- d) Identify resonance effects if the impulse spacing matches the system's natural period

---

## Control Theory Applications

### Exercise 6.1: Step and Impulse Response Relationship
**Source:** Ogata (2010), Lathi & Green (2018)
**Difficulty:** Intermediate

Given a system with step response:
$$y_{step}(t) = 1 - e^{-t} - t e^{-t}$$

**Questions:**
- a) Find the impulse response $h(t)$ using the relationship: $h(t) = \frac{d}{dt}y_{step}(t)$
- b) Verify this is consistent with the system's transfer function
- c) Find the pole locations and discuss stability

---

### Exercise 6.2: Transfer Function and Impulse Response
**Source:** Ogata (2010), Karris (2003)
**Difficulty:** Intermediate

Given the transfer function:
$$H(s) = \frac{s + 1}{(s + 1)(s + 2)(s + 3)}$$

**Questions:**
- a) Simplify the transfer function
- b) Find the impulse response $h(t)$
- c) Compute the step response from the impulse response using convolution
- d) Determine the settling time and steady-state error to a unit step

---

## Structural Dynamics & Vibrations

### Exercise 7.1: Impact Loading on Structures
**Source:** Beards (1996), Schmitz & Smith (2012)
**Difficulty:** Intermediate

A structure modeled as a second-order system experiences an impact:
$$m\ddot{x} + c\dot{x} + kx = F(t)$$

where the impact imparts impulse $J = 10$ N·s.

Given: $m = 1$ kg, $c = 2$ N·s/m, $k = 10$ N/m, pre-impact at rest.

**Questions:**
- a) Write the equivalent ODE with delta forcing
- b) Find the post-impact velocity
- c) Solve for the structural response $x(t)$ for $t > 0$
- d) Calculate the maximum displacement

---

### Exercise 7.2: Vibration Impulse Response
**Source:** Inman (2014), Rao (2011), Meirovitch (2001)
**Difficulty:** Advanced

A building floor system (modeled as SDOF) has:
- Natural frequency: $f_n = 2$ Hz
- Damping ratio: $\zeta = 0.05$ (5% critical damping)
- Mass: $m = 1000$ kg

An impulse (wind gust) imparts $J = 5000$ N·s.

**Questions:**
- a) Calculate the post-impulse velocity
- b) Determine the natural frequency in rad/s and damped frequency
- c) Find the maximum displacement and its time of occurrence
- d) Calculate the period of oscillation and time to settle to <1% of peak displacement

---

## Advanced Problems

### Exercise 8.1: System with Parametric Impulses
**Source:** Schiff (1999), Oliveira & Cortes (2011)
**Difficulty:** Advanced

Consider:
$$\ddot{x} + (2 + \sin t)\dot{x} + (1 + \cos t)x = \delta(t)$$

**Questions:**
- a) Why is this non-trivial compared to constant-coefficient systems?
- b) Can you use standard Laplace transform methods? Why or why not?
- c) Propose a numerical solution strategy
- d) For $t$ near 0, approximate the solution using perturbation methods

---

### Exercise 8.2: Coupled System with Impulsive Forcing
**Source:** Meirovitch (2001)
**Difficulty:** Advanced

A two-degree-of-freedom system:
$$\begin{bmatrix} m_1 & 0 \\ 0 & m_2 \end{bmatrix} \begin{bmatrix} \ddot{x}_1 \\ \ddot{x}_2 \end{bmatrix} + \begin{bmatrix} c_1 + c_c & -c_c \\ -c_c & c_2 + c_c \end{bmatrix} \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} + \begin{bmatrix} k_1 + k_c & -k_c \\ -k_c & k_2 + k_c \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} \delta(t) \\ 0 \end{bmatrix}$$

with $m_1 = m_2 = 1$, $k_1 = k_2 = 10$, $k_c = 5$, $c_1 = c_2 = 0.2$, $c_c = 0.1$.

Initial conditions: $x_1(0^-) = x_2(0^-) = \dot{x}_1(0^-) = \dot{x}_2(0^-) = 0$.

**Questions:**
- a) Write the system in matrix form and identify the modal properties
- b) Use modal analysis to decouple the equations
- c) Solve for the individual modal responses to the impulse
- d) Reconstruct the time-domain responses $x_1(t)$ and $x_2(t)$
- e) Discuss energy transfer between the two degrees of freedom

---

## Solutions and References

**Note:** Solutions and detailed worked examples will be developed as this document is refined.

### Primary References

| Source | Key Content | Pages |
|---|---|---|
| Schiff (1999) | Delta derivatives, Laplace methods | pp.29, 59, 79, 82–83 |
| Oliveira & Cortes (2011) | δ(t) and δ'(t) impulse response | p.4 |
| Meirovitch (2001) | IC change, vibration impulse | pp.160–161, 170–180 |
| Karris (2003) | MATLAB examples, signals/systems | Multiple pages |
| Ogata (2010) | Transfer function, impulse response | Ch.2-2, Ch.5 |

---

## Suggestions for Extension

- [ ] Add MATLAB/Python code for numerical solutions
- [ ] Include graphical representations of solutions
- [ ] Create answer key with detailed solutions
- [ ] Add interactive computational examples
- [ ] Link to specific examples from source books
- [ ] Organize by learning pathway (beginner → advanced)

---

**Document Status:** Draft  
**Maintenance:** Updated as exercises are solved and verified  
**Contributing:** To add exercises, reference source books and specify difficulty level
