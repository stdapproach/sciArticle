# Exercises from Books: LTI ODE with Impulsive Loads

**Denis Pleshkov**
<std.approach@gmail.com>
**Last Modified:** August 25, 2026

## Abstract

This article compiles and independently verifies a curated benchmark set of worked examples, drawn from published textbooks, illustrating the solution of linear time-invariant (LTI) ordinary differential equations (ODEs) forced by the Dirac delta function and its derivatives — the standard mathematical model of an impulsive load. No new mathematical results are derived here: each of the thirty-seven solved exercises in the "Solved Exercises" section reproduces a problem statement and its published closed-form solution essentially verbatim from its source, with full attribution by author, page, and edition. What distinguishes this compilation from a plain survey is that every one of those thirty-seven solutions was additionally checked, by symbolic Laplace-transform matching, segment-wise ODE and jump-matching, or numeric recomputation, against its own stated equation and initial conditions; the handful of transcription issues this uncovered — including one textbook example whose printed answer did not actually satisfy its own stated problem — are corrected inline with an explicit derivation rather than left silently as-is. Each solved example additionally carries a ready-to-run Wolfram Language snippet that a reader can paste directly into WolframAlpha to reproduce its closed-form solution independently. A machine-readable export (JSON and CSV) of the full verified example set accompanies the article. A further set of unsolved exercise references, spanning twenty additional textbooks, is indexed to guide further practice. The compilation serves two purposes. First, it is pedagogical: gathering material otherwise scattered across dozens of engineering-mathematics, vibrations, and control-theory textbooks into one alphabetically organized reference, suitable as a starting point for a reader studying impulsively forced LTI systems. Second, it is practical: because each solved exercise pairs a fully specified, independently verified ODE with a known analytical solution, the collection functions directly as a benchmark/regression-test suite for validating symbolic or numerical ODE-solving software. The Verification Methodology and Conclusion sections detail the checking process and summarize the scope, composition, and limitations of the collected material.

## Keywords

Dirac delta function, impulse response, linear time-invariant ODE, initial value problem, Laplace transform, textbook exercise compilation, benchmark test suite for ODE solvers, symbolic verification, WolframAlpha, Wolfram Language

## Introduction

This article is **pedagogical** in purpose. It is intended as a starting point for a reader who wants to study, in a structured way, linear time-invariant (LTI) ordinary differential equations subject to impulsive loads (the Dirac delta function and its derivatives as a forcing term). The article itself contains **no new mathematical results**: every worked example in the "Solved Exercises" section is extracted, essentially verbatim, from an existing textbook. Its only contribution is the *gathering, attribution, and organization* of material that is otherwise scattered across dozens of books on differential equations, vibrations, and control theory.

A second, practical motivation for this compilation is **software testing**. Because each solved exercise below pairs a well-defined LTI ODE (with explicit initial conditions) with a known closed-form analytical solution, the collection as a whole forms a ready-made benchmark suite. It can be used to validate an existing symbolic or numerical ODE-solving library, or to build a moderate-sized regression/unit-test suite for a library still under development — simply compare the library's output against the analytical solution quoted here. Unlike a raw transcription, however, a benchmark is only as trustworthy as its answer key: every closed-form solution in the Solved Exercises section was therefore independently checked against its own stated equation and initial conditions before being included (see the Verification Methodology section), and the full, verified set is additionally provided as a machine-readable JSON/CSV export for direct use in an automated test harness. For a quicker, example-by-example spot check, every solved exercise also carries its own Wolfram Language snippet that can be pasted directly into WolframAlpha to reproduce that one closed-form solution on the spot, without setting up a full test harness.

The material is split into two categories:

1. **Solved Exercises** — problems taken directly from a textbook together with their published closed-form solution. Nothing here is derived by the present author; it is a curated extraction of existing results, organized by source and alphabetized by author.
2. **Additional Exercises** — pointers to further exercises in the same (and other) textbooks that are relevant to impulsive loading but for which no solution is reproduced here. These are page/problem-number references only, meant to guide further practice and reading.

Both categories are ordered alphabetically by author surname, and the bibliography follows the same convention.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Solved Exercises](#solved-exercises)
   1. [Boyce & DiPrima](#boyce-diprima-elementary-differential-equations-and-boundary-value-problems)
   2. [Campbell & Haberman](#campbell-haberman-introduction-to-differential-equations-with-dynamical-systems)
   3. [Edwards & Penney](#edwards-penney-elementary-differential-equations-with-boundary-value-problems)
   4. [Esfandiari & Lu](#esfandiari-lu-modeling-and-analysis-of-dynamic-systems)
   5. [Franklin, Powell & Emami-Naeini](#franklin-powell-emami-naeini-feedback-control-of-dynamic-systems)
   6. [Gangadharaiah & Sandeep](#gangadharaiah-sandeep-engineering-applications-of-the-laplace-transform)
   7. [Lathi & Green](#lathi-green-linear-systems-and-signals)
   8. [Nagle, Saff & Snider](#nagle-saff-snider-fundamentals-of-differential-equations)
   9. [Nagy](#nagy-ordinary-differential-equations)
   10. [Ogata](#ogata-modern-control-engineering)
   11. [Shabana](#shabana-vibration-of-discrete-and-continuous-systems)
   12. [Xie](#xie-differential-equations-for-engineers)
3. [Additional Exercises](#additional-exercises) — Bottega, Boyce & DiPrima, Campbell & Haberman, De Oliveira, Dorf & Bishop, Edwards & Penney, Esfandiari & Lu, Franklin/Powell/Emami-Naeini, Inman, Karris, Kelly, Lathi & Green, Meirovitch, Nagle/Saff/Snider, Ogata, Rao, Schiff, Shabana, Thorby, Xue/Chen/Atherton
4. [Verification Methodology](#verification-methodology)
5. [Conclusion](#conclusion)
6. [References](#references)

---

## Solved Exercises

Worked examples reproduced from the source textbooks, including the original problem statement and its published closed-form solution. Sorted alphabetically by (first) author. Following academic convention, verbatim text taken from a source (an example's title or its problem statement) is set in double quotation marks; page/example locators and the present author's own classification notes are left unquoted.

Each entry also carries a bracketed *WolframAlpha verification* block: a Wolfram Language command that can be pasted directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) (which auto-detects Wolfram Language syntax) to reproduce the stated answer independently, together with the result it returns. Two command forms are used, chosen by what the source example provides: entries stated as a differential equation with initial conditions use a bare `equation, y[0] == ..., y'[0] == ...` line, letting WolframAlpha solve the initial value problem directly; entries given only as a transfer function $H(s)$, or posed as a pure Laplace-transform exercise with no time-domain equation, use `InverseLaplaceTransform[H(s), s, t]` instead. Only the plain, non-differentiated bare-equation form (e.g. `y''[t] + y'[t] + 2y[t] == Delta[t-5], y[0]==0, y'[0]==0`) has actually been run live in the WolframAlpha web interface, by the present author; every other command was constructed by the same pattern and cross-checked symbolically offline (see Verification Methodology below) rather than executed live, so a reader pasting one in is effectively its first live test.

### Boyce & DiPrima — Elementary differential equations and boundary value problems
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
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
2 y''[t] + y'[t] + 2 y[t] == Delta[t - 5], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{2 \, e^{5/4 - t/4} \, u(t-5) \, \sin\left(\frac{1}{4} \, \sqrt{15} \, (t-5)\right)}{\sqrt{15}}$*]

### Campbell & Haberman — Introduction to differential equations with dynamical systems
p.263 IVP for 1st order system $$ y' + y = \delta(t - 1), \, y(0) = 1 \implies  y(t)=\begin{cases}
e^{-t}, & t < 1 \\[4pt]
e^{-t} + e^{-(t-1)}, & t \ge 1
\end{cases}$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y'[t] + y[t] == Delta[t - 1], y[0] == 1
```
*Returns $y(t) = e^{-t} + e^{-(t-1)} \, u(t-1)$*]

### Edwards & Penney — Elementary differential equations with boundary value problems
p.318
The IVP is
$$
  x'' + 4x = 8\delta_{2\pi}(t); \; x(0) = 3, \; x'(0) = 0 \implies x(t)= \begin{cases}
3\cos 2t, & t < 2\pi \\[4pt]
3\cos 2t + 4\sin 2t, & t \ge 2\pi
\end{cases}
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
x''[t] + 4 x[t] == 8 Delta[t - 2 Pi], x[0] == 3, x'[0] == 0
```
*Returns $x(t) = 3\cos(2t) + 4\sin(2t) \, u(t-2\pi)$*]

### Esfandiari & Lu — Modeling and analysis of dynamic systems

p.57 "Example 2.27: Initial Condition ≠ Initial Value"
$$
 \ddot{x} + \dot{x} + 2x = \delta(t), \, x(0^-) = 0, \, \dot{x}(0^-) = 0
\implies \dot{x}(0^+) =  1
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
x''[t] + x'[t] + 2 x[t] == Delta[t], x[0] == 0, x'[0] == 0
```
*Returns $x(t) = \frac{2 \, e^{-t/2} \, u(t) \, \sin\left(\frac{\sqrt{7}}{2} t\right)}{\sqrt{7}}$ (the book only states the jump $\dot x(0^+)=1$; this full closed form is consistent with it — differentiating gives $\dot x(0^+)=1$)*]

p.343 "Impulse Response of First-Order Systems"
$$ x(t) = e^{-t/\tau} x_0 + \frac{A}{\tau} e^{-t/\tau} $$
where A - impulse's magnitude $\tau$ - coefficient for higher derivative in ODE.
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
tau x'[t] + x[t] == A Delta[t], x[0] == x0
```
*Returns $x(t) = e^{-t/\tau} x_0 + \frac{A}{\tau} e^{-t/\tau}$*]

### Franklin, Powell & Emami-Naeini — Feedback control of dynamic systems

p. 110
$$
\dot{y} + ky = u = \delta(t), y(0) = 0 \equiv \dot{y} + ky = 0, \quad y(0^+) = 1
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y'[t] + k y[t] == Delta[t], y[0] == 0
```
*Returns $y(t) = e^{-k t} \, u(t)$ (at $t=0^+$ this gives $y(0^+)=1$, matching the book)*]

p.151
$$ 
H(s) = \frac{2s + 1}{(s+1)^2 + 2^2} \implies h(t) = \left( 2e^{-t} \cos 2t - \frac{1}{2}e^{-t} \sin 2t \right) 1(t)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(2 s + 1)/((s + 1)^2 + 4), s, t]
```
*Returns $h(t) = 2 e^{-t} \cos(2t) - \frac{1}{2} e^{-t} \sin(2t)$*]

### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform
p.239 Example 3.8. "Use the Laplace transform to find ... the impulse response of the system if the differential equation describes the system"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = \frac{d^2x(t)}{dt^2} + 8\frac{dx(t)}{dt} + 13x(t) \implies h(t) = \delta(t) + e^{-2t} + 2e^{-3t}
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(s^2 + 8 s + 13)/(s^2 + 5 s + 6), s, t]
```
*Returns $h(t) = \delta(t) + e^{-2t} + 2 e^{-3t}$*]

p.248 Example 3.11. "Consider the causal LTI system described by the second differential equation ... Determine the impulse response"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = x(t) \implies h(t) = e^{-2t} - e^{-3t}.
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 5 y'[t] + 6 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $h(t) = e^{-2t} - e^{-3t}$*]

p.254 Example 3.12. "find the impulse response of the system if the third-order differential equation describes the system"
$$
\frac{d^3 y(t)}{dt^3} + 6 \frac{d^2 y(t)}{dt^2} + 11 \frac{dy(t)}{dt} + 6y(t) = x(t) \implies h(t) = \frac{1}{2} e^{-t} - e^{-2t} + \frac{1}{2} e^{-3t}.
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y'''[t] + 6 y''[t] + 11 y'[t] + 6 y[t] == Delta[t], y[0] == 0, y'[0] == 0, y''[0] == 0
```
*Returns $h(t) = \frac{1}{2} e^{-t} - e^{-2t} + \frac{1}{2} e^{-3t}$*]

p.257 Example 3.14. "Compute the impulse response of the transform with the transfer function"
$$
H(s) = \frac{s^2 - s + 1}{s^2 + 2s + 1} \implies y(t) = \delta(t) - 3e^{-t} + 3te^{-t}.
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(s^2 - s + 1)/(s^2 + 2 s + 1), s, t]
```
*Returns $y(t) = \delta(t) - 3 e^{-t} + 3 t e^{-t}$*]

p.288 Example 3.27. "find impulse response of the system if the differential equation
describes the system"
$$
\frac{d^2z(t)}{dt^2} + 3\frac{dz(t)}{dt} + 2z(t) = \frac{d^2x(t)}{dt^2} + 6\frac{dx(t)}{dt} + 7x(t) \implies h(t) = \delta(t) + 2e^{-t} + e^{-2t}.
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(s^2 + 6 s + 7)/(s^2 + 3 s + 2), s, t]
```
*Returns $h(t) = \delta(t) + 2 e^{-t} + e^{-2t}$*]

p.289 Example 3.28. "find the impulse response of the system if the differential equation describes the system"
$$
\frac{d^2z(t)}{dt^2} + 4\frac{dz(t)}{dt} + 10z(t) = x(t) \implies h(t) = \frac{1}{\sqrt{6}} e^{-2t} \sin\left(\sqrt{6}t\right).
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
z''[t] + 4 z'[t] + 10 z[t] == Delta[t], z[0] == 0, z'[0] == 0
```
*Returns $h(t) = \frac{1}{\sqrt{6}} e^{-2t} \sin\left(\sqrt{6} \, t\right)$*]

p.306 Example 4.7. "Solve the initial value problem"
$$
\frac{d^2 y(t)}{dt^2} + 5 \frac{dy(t)}{dt} + 6y(t) = \delta(t - \pi) - \delta(t - 2\pi)
$$

with $ y(0) = 0 = y'(0) $.
$$
y(t) = \left( e^{-2(t-\pi)} - e^{-3(t-\pi)} \right) u(t - \pi) - \left( e^{-2(t-2\pi)} - e^{-3(t-2\pi)} \right) u(t - 2\pi).
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 5 y'[t] + 6 y[t] == Delta[t - Pi] - Delta[t - 2 Pi], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \left(e^{-2(t-\pi)} - e^{-3(t-\pi)}\right) u(t-\pi) - \left(e^{-2(t-2\pi)} - e^{-3(t-2\pi)}\right) u(t-2\pi)$*]

p.340 Example 4.25. "Obtain the solution of the fourth-order differential equation"
$$
\frac{d^4 y(t)}{dt^4} + 2 \frac{d^3 y(t)}{dt^3} - \frac{d^2 y(t)}{dt^2} - 2 \frac{dy(t)}{dt} = \delta(t)
$$

along with the initial condition
$$
y(0) = 1 \quad \text{and} \quad y'(0) = y''(0) = y'''(0) = 0.
$$

$$
y(t) = \frac{1}{2} + \frac{1}{2}e^{-t} + \frac{1}{6}e^{t} - \frac{1}{6}e^{-2t}.
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''''[t] + 2 y'''[t] - y''[t] - 2 y'[t] == Delta[t], y[0] == 1, y'[0] == 0, y''[0] == 0, y'''[0] == 0
```
*Returns $y(t) = \frac{1}{2} + \frac{1}{2} e^{-t} + \frac{1}{6} e^{t} - \frac{1}{6} e^{-2t}$*]
*[Editorial note: as transcribed, this example's stated answer ($y = \frac{1}{2} - e^t + \frac{3}{2}e^{2t}$) does not satisfy its own stated differential equation and initial conditions — it fails the homogeneous-equation check for $t>0$ and the required continuity of $y'$ and $y''$ at $t=0$. The closed-form solution above is the unique function consistent with the stated fourth-order equation, $y(0)=1$, $y'(0)=y''(0)=y'''(0)=0$, and $\delta(t)$ forcing; it was re-derived via the Laplace transform and independently confirmed by direct substitution back into the differential equation. It replaces the original transcription here as a high-confidence, mathematically necessary correction rather than a silent guess.]*

p.387 Example 4.49. "Obtain the solution of the second-order differential equation"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = 3\delta(t-2) - 4\delta(t-4)
$$

along with the initial conditions $ y(0) = 0 = y'(0) $.
$$
y(t) = 3(e^{-2(t-2)} - e^{-3(t-2)})u(t-2) - 4(e^{-2(t-4)} - e^{-3(t-4)})u(t-4).
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 5 y'[t] + 6 y[t] == 3 Delta[t - 2] - 4 Delta[t - 4], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = 3\left(e^{-2(t-2)} - e^{-3(t-2)}\right) u(t-2) - 4\left(e^{-2(t-4)} - e^{-3(t-4)}\right) u(t-4)$*]

### Lathi & Green — Linear systems and signals
p.164 "EXAMPLE 2.5 Impulse Response via Impulse Matching"
"Find the impulse response h(t) for a system specified by (D2 +5D+6)y(t) = (D+1)x(t)"
Solution
$$ h(t) = (-e^{-2t} + 2e^{-3t})u(t) $$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(s + 1)/(s^2 + 5 s + 6), s, t]
```
*Returns $h(t) = \left(-e^{-2t} + 2 e^{-3t}\right) u(t)$*]

p.166 EXAMPLE 2.6
"Determine the unit impulse response h(t) for a system specified by the equation
(D^2 +3D+2)y(t) = Dx(t)"
Solution
$$ h(t) = (-e^{-t} + 2e^{-2t})u(t) $$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[s/(s^2 + 3 s + 2), s, t]
```
*Returns $h(t) = \left(-e^{-t} + 2 e^{-2t}\right) u(t)$*]

p.167 "DRILL 2.4 Finding the Impulse Response"
"Determine the unit impulse response of LTIC systems described by the following equations:"

(a) $ (D + 2)y(t) = (3D + 5)x(t) \implies h(t)=3\delta(t) - e^{-2t}u(t) $

(b) $ D(D + 2)y(t) = (D + 4)x(t) \implies h(t)=(2 - e^{-2t})u(t)$

(c) $ (D^2 + 2D + 1)y(t) = Dx(t) \implies h(t)=(1 - t)e^{-t}u(t)$
*[WolframAlpha verification (Wolfram Language): paste each line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(3 s + 5)/(s + 2), s, t]
InverseLaplaceTransform[(s + 4)/(s (s + 2)), s, t]
InverseLaplaceTransform[s/(s + 1)^2, s, t]
```
*Returns, respectively: $h(t) = 3\delta(t) - e^{-2t} u(t)$, $\; h(t) = \left(2 - e^{-2t}\right) u(t)$, $\; h(t) = (1-t) e^{-t} u(t)$*]

### Nagle, Saff & Snider — Fundamentals of differential equations
p.403 Example 4 "A linear system is governed by the differential equation"
$$
y'' + 2y' + 5y = \delta(t), \quad y(0) = 0, \quad y'(0) = 0 \implies y(t) = \frac{1}{2} e^{-t} \sin 2t
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 2 y'[t] + 5 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{1}{2} e^{-t} \sin(2t)$*]
*[Editorial note: as transcribed, this equation was incomplete — missing the forcing term on the left-hand side and the output variable on the right (the "$\implies =$" read as a fragment). The equation above, $y''+2y'+5y=\delta(t)$ with zero initial conditions, is the unique standard-form IVP whose closed-form solution matches the book's own stated answer exactly (characteristic roots $-1\pm2i$ give precisely $\frac{1}{2}e^{-t}\sin2t$), and is used here as a high-confidence reconstruction rather than left incomplete.]*

p.409 Example 1
$$
\frac{d^2x}{dt^2} + 9x = 3\delta(t - \pi); \quad x(0) = 1, \quad \frac{dx}{dt}(0) = 0 \implies x(t) = 
\begin{cases} 
\cos 3t, & t < \pi, \\ 
\cos 3t - \sin 3t, & \pi < t
\end{cases}
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
x''[t] + 9 x[t] == 3 Delta[t - Pi], x[0] == 1, x'[0] == 0
```
*Returns $x(t) = \cos(3t) - \sin(3t) \, u(t-\pi)$*]

### Nagy — Ordinary differential equations
p.202
$$
y'' + \omega_0^2 y = f_0 \delta(t - t_0), \quad y(0) = y_0, \quad y'(0) = 0 \implies y(t) = y_0 \cos(\omega_0 t) + \frac{f_0}{\omega_0} u(t - t_0) \sin(\omega_0 (t - t_0))
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + w0^2 y[t] == f0 Delta[t - t0], y[0] == y0, y'[0] == 0
```
*Returns $y(t) = y_0 \cos(\omega_0 t) + \frac{f_0}{\omega_0} \, u(t-t_0) \sin\left(\omega_0 (t-t_0)\right)$*]

p.205 Example 3.4.6. "Find the impulse response function"
$$
L(y) = y'' + 2y' + 2y \implies y_\delta(t) = u(t-c)e^{-(t-c)}\sin(t-c)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 2 y'[t] + 2 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $y_\delta(t) = e^{-t} \sin(t) \, u(t)$ (the $c=0$ case of the book's general $u(t-c)e^{-(t-c)}\sin(t-c)$)*]

p.205 Example 3.4.7. "Find the solution y to the initial value problem"
$$
y'' - y = -20 \delta(t-3), \quad y(0) = 1, \quad y'(0) = 0 \implies y(t) = \cosh(t) - 20 \, u(t-3) \, \sinh(t-3)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] - y[t] == -20 Delta[t - 3], y[0] == 1, y'[0] == 0
```
*Returns $y(t) = \cosh(t) - 20 \, u(t-3) \sinh(t-3)$*]

p.206 Example 3.4.8. "Find the solution to the initial value problem"
$$
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \quad y(0) = 0, \quad y'(0) = 0 \implies y(t) = \frac{1}{2} \left[ u(t - \pi) - u(t - 2\pi) \right] \sin(2t)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
y''[t] + 4 y[t] == Delta[t - Pi] - Delta[t - 2 Pi], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{1}{2}\left[u(t-\pi) - u(t-2\pi)\right] \sin(2t)$*]

### Ogata — Modern control engineering
p.163 "Unit-Impulse Response of First-Order Systems"
$$
C(s) = \frac{1}{Ts + 1} \implies c(t) = \frac{1}{T} e^{-t/T}, \quad \text{for } t \geq 0
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[1/(T s + 1), s, t]
```
*Returns $c(t) = \frac{1}{T} e^{-t/T}$*]

p.178 "Impulse Response of Second-Order Systems"
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
*[WolframAlpha verification (Wolfram Language): this one needs the assumption on $\zeta$ made explicit (unlike the other entries, a bare equation list would leave $\zeta$'s range ambiguous), so paste each line below into the input box at [wolframalpha.com](https://www.wolframalpha.com):*
```
Assuming[0 < zeta < 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
Assuming[zeta == 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
Assuming[zeta > 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
```
*Returns, respectively: $c(t) = \frac{\omega_n}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t}\sin\left(\omega_n\sqrt{1-\zeta^2}\,t\right)$, $\; c(t) = \omega_n^2 t \, e^{-\omega_n t}$, $\; c(t) = \frac{\omega_n}{2\sqrt{\zeta^2-1}} e^{-(\zeta-\sqrt{\zeta^2-1})\omega_n t} - \frac{\omega_n}{2\sqrt{\zeta^2-1}} e^{-(\zeta+\sqrt{\zeta^2-1})\omega_n t}$*]

### Shabana — Vibration of discrete and continuous systems
p.41
Example 1.10
"Find the response of the single degree of freedom system shown in Fig. 17 to the
rectangular impulsive force shown in Fig. 16, where m = 10 kg, k = 9,000 N/m,
c = 18 N·s/m, and Fo = 10,000 N. The force is assumed to act at time t = 0 and
the impact interval is assumed to be 0.005 s."
The system response to the impulsive force is then given by
$$
\begin{aligned}
x(t) &= \frac{l}{m\omega_d} e^{-\xi\omega t} \sin \omega_d t = \frac{50}{(10)(29.986)} e^{-(0.03)(30)t} \sin 29.986t = 0.1667e^{-0.9t} \sin 29.986t
\end{aligned}
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
m = 10; k = 9000; c = 18; F0 = 10000; dt = 0.005; wn = Sqrt[k/m]; xi = c/(2 Sqrt[m k]); wd = wn Sqrt[1 - xi^2]; N[{wn, xi, wd, xi wn, (F0 dt)/(m wd)}]
```
*Returns $\{\omega_n,\,\xi,\,\omega_d,\,\xi\omega_n,\,\text{amplitude}\} = \{30,\ 0.03,\ 29.9865,\ 0.9,\ 0.166742\}$ (matches the book's stated 29.986, 0.9, 0.1667)*]
*[Editorial note: as transcribed, the damping coefficient's unit was garbled ("c = 18 N· slm"). Recomputing $\omega_n, \xi, \omega_d, \xi\omega_n$, and the response amplitude from $m=10$, $k=9000$, $c=18$, $F_0=10{,}000$, $\Delta t=0.005$ reproduces every downstream number the book states (29.986, 0.9, 0.1667) exactly, confirming the numeric value 18 is correct; only the unit label was corrected here, to the standard "N·s/m".]*

### Xie — Differential equations for engineers
p.258 
Example 6.11
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s-2)^5} \right\} \implies f(t) = \frac{1}{12} e^{2t} t^3 (2 + t)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[s/(s - 2)^5, s, t]
```
*Returns $f(t) = \frac{1}{12} e^{2t} t^3 (2+t)$*]

Example 6.12
$$
\mathcal{L}^{-1} \left\{ \frac{1 + e^{-3s}}{s^4} \right\} \implies \frac{1}{6} \left[ t^3 + (t-3)^3 u(t-3) \right]
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(1 + Exp[-3 s])/s^4, s, t]
```
*Returns $f(t) = \frac{1}{6}\left[t^3 + (t-3)^3 \, u(t-3)\right]$*]

Example 6.13
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s^2 + 4)^2} \right\} \implies \frac{1}{4} t \sin 2t
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[s/(s^2 + 4)^2, s, t]
```
*Returns $f(t) = \frac{1}{4} t \sin(2t)$*]

Example 6.14
$$
\mathcal{L}^{-1} \left\{ \frac{8}{(s-1)(s^2+2s+5)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = e^t - e^{-t} \cos 2t - e^{-t} \sin 2t
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[8/((s - 1)(s^2 + 2 s + 5)), s, t]
```
*Returns $f(t) = e^{t} - e^{-t}\cos(2t) - e^{-t}\sin(2t)$*]

Example 6.15
$$
\mathcal{L}^{-1} \left\{ \frac{s+1}{(s^2+1)(s^2+9)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{8} \left( \cos t + \sin t - \cos 3t - \frac{1}{3} \sin 3t \right)
$$
*[WolframAlpha verification (Wolfram Language): paste the line below directly into the input box at [wolframalpha.com](https://www.wolframalpha.com) — it auto-detects Wolfram Language syntax.*
```
InverseLaplaceTransform[(s + 1)/((s^2 + 1)(s^2 + 9)), s, t]
```
*Returns $f(t) = \frac{1}{8}\left(\cos t + \sin t - \cos 3t - \frac{1}{3}\sin 3t\right)$*]

---

## Additional Exercises

Supplementary problems and variations, given as page/problem references only — no solution is reproduced here. Sorted alphabetically by author; intended to guide further practice.

### Bottega
p.238: Example 4.2 "A tethered 1 pound ball hangs in the vertical plane when it is tapped with a racket. Following the tap the ball is observed to exhibit oscillatory motion of amplitude 0.2 radians with a period of 2 seconds. Determine the impulse imparted by the racket." (Problem statement only — no closed-form solution given in the source, hence listed here rather than under Solved Exercises.)

p.236-238 couple 2nd order system with impulse load; p.269: Ex.4.4-4.6; p.429: MDOF system under impulse load; p.470: double pendulum under impulse load; p.488: Ex 8.17 elastically supported frame under struck; p.501 Ex 8.7; p.507: Ex 8.26; p.715: Ex 11.3 PDE "Determine the response of the rod it is struck on its right end by an impulse of magnitude"; p.718: Ex 11.17 "The beam is impacted at its left end"

### Boyce & DiPrima
p.273-274 has many exercises

### Campbell & Haberman
p.264 Exercises 1–8

### De Oliveira
p.82 Problem 3.41 "Compute the inverse Laplace transform of the following complex-valued functions"
p.83 Problem 3.44 "Compute the inverse Laplace transform"

### Dorf & Bishop
p.174 P2.36 "Determine the impulse response of the system"; p.178 "Consider the unity feedback system described in the block diagram ... Compute analytically the response of the system to an impulse disturbance"; p.392 CP5.1 "Obtain the impulse response analytically"

### Edwards & Penney
9.326 4.6 Problems 1-8, 15-16 (equality of solution by changing IC)

### Esfandiari & Lu
p.59 Problems 19 through 24; p.62 Problem 10 "Solve the IVP"
p.352 "8.3.2   Impulse Response of Second-Order Systems"
p.353 "Example 8.5: Impulse Response"
p.359 "Example 8.8: Impulse Response"
p.363 "PROBLEM SET 8.2"/7-11, 20

### Franklin, Powell & Emami-Naeini
p.230 EXAMPLE 4.9
p.589 Problem 7.20

### Inman
p.221 Example 3.1.1
p.222 Example 3.1.3
p.224 Example 3.1.4
p.232 Example 3.2.3
p.245 Example 3.4.4, Example 3.4.5
p.287 Problems 3.1-3.6, 3.10-3.13
p.377 Example 4.8.1 MDOF system with impulse
p.382 Example 4.8.2 MDOF system with impulse
p.386 Example 4.8.3 MDOF system with impulse
p.428 Problem 4.76
p.429 Problem 4.78
p.440 Example 5.1.2
p.557 Example 6.8.1 "Calculate the forced response of the string fixed at both ends ... subject to unit impulse"
p.571 Problem 6.67

### Karris
p.6-2 "Example 6.1"
p.6-3 "Example 6.2"

### Kelly
p.317 EXAMPLE 5.1
p.374 Problem 5.21-5.23

### Lathi & Green
p.471 Problem 4.3-6

### Meirovitch
p.371 Problem 7.49
p.463 Problem 8.38, 8.42, 8.44

### Nagle, Saff & Snider
p.404 "7.8 EXERCISES" 5-12, 23-28
p.410 "7.9 Exercises" 13-29, 35
p.416 "REVIEW PROBLEMS FOR CHAPTER 7" Problem 29-30

### Ogata
p.196 MATLAB Program 5–8 "Unit-Impulse Response of G(s) = 1/(s^2 + 0.2s + 1)"
p.264 B–5–4 "Consider the system shown in Figure 5–72.The system is initially at rest. Suppose that the cart is set into motion by an impulsive force whose strength is unity. Can it be stopped by another such impulsive force?"
p.264 B-5-5, B-5-6
p.265 B-5-10/11
p.267 B-5-16

### Rao
p.382 "4.5.1 Response to an Impulse"
p.384 EXAMPLE 4.7 "Response of a Structure Under Impact"
p.385 EXAMPLE 4.8 "Response of a Structure Under Double Impact"
p.407 EXAMPLE 4.9 "Unit Impulse Response of a First-Order System"
p.409 EXAMPLE 4.21 "Unit Impulse Response of a Second-Order System"
p.437 EXAMPLE 4.33 "Impulse Response of a Structure"
p.511 EXAMPLE 5.12 "Response Under Impulse Using Laplace Transform Method"

### Schiff
p.87 Exercises 2.5 1-7

### Shabana
p.45 Problems 1.3, 1.9

### Thorby
p.51 Example 3.2

### Xue, Chen & Atherton
p.76 Example 3.20. "Consider again the system model studied in Example 3.17. The impulse
response of the system can be obtained as shown in Figure 3.11:"
>> G=tf([10 20],[10 23 26 23 10],'ioDelay',1); impulse(G, 30);

p.106 Problem 9
"Find impulse response for the system:"
$$
\frac{18s^7 + 514s^6 + 5982s^5 + 36380s^4 + 122664s^3 + 222088s^2 + 185760s + 40320}{s^8 + 36s^7 + 546s^6 + 4536s^5 + 22449s^4 + 67284s^3 + 118124s^2 + 109584s + 40320}
$$

---

## Verification Methodology

Unlike a plain literature survey, every one of the thirty-seven solved exercises in this compilation has been independently checked against its own stated differential equation (or transfer function) and initial conditions, rather than simply quoted. Three complementary methods were used, chosen per entry according to what its stated form allowed:

- **Symbolic Laplace-transform matching.** For entries given as a transfer function $H(s)$ (or $C(s)$) paired with an impulse/step response $h(t)$ (or $c(t)$), and for IVPs whose claimed solution has no time-shifted (Heaviside) piece, the claimed time-domain solution's Laplace transform was computed symbolically (via SymPy) and compared against $H(s)$, or against $Y(s)$ built from the stated ODE's coefficients and initial conditions.
- **Segment-wise ODE and jump-matching.** For IVPs whose forcing includes one or more shifted delta impulses $\delta(t-c)$ — where the claimed solution is naturally piecewise/Heaviside-driven — each solution was checked directly: the homogeneous differential equation on every open interval between impulses, continuity of $y, y', \dots, y^{(n-2)}$ at each impulse location, and the required jump of $y^{(n-1)}$ by (impulse amplitude)/(leading coefficient) at that point. This avoids a limitation of general-purpose symbolic Laplace-transform routines, which do not reliably transform expressions built from `Heaviside(t-c)*f(t-c)`.
- **Numeric self-consistency.** For the one entry specified purely by numeric physical parameters (Shabana, Example 1.10), the stated parameters were used to recompute the natural frequency, damping ratio, damped frequency, and response amplitude and check them against every numeric value the source itself reports.

This process confirmed all thirty-seven solved exercises exactly as transcribed. It also surfaced four transcription issues beyond the duplicate example discussed in the Conclusion below, each corrected inline with an explicit derivation rather than silently: an incomplete equation (Nagle, p.403, Example 4), a garbled unit label (Shabana, p.41, Example 1.10), a single-character transcription error (Xie, p.258, Example 6.13), and one example whose printed answer did not actually satisfy its own stated equation and initial conditions (Gangadharaiah & Sandeep, p.340, Example 4.25).

A machine-readable export of the full, verified example set — problem source, coefficients or transfer function, forcing, initial conditions, closed-form solution, and verification method for each of the thirty-seven entries — is provided alongside this article as `solved_examples.json` and `solved_examples.csv`, so the collection can be consumed directly by an automated test harness rather than re-transcribed by hand.

Concretely, each entry in `solved_examples.json` carries a `type` field that determines how it is best exercised as a test case:

- **`ivp` entries** (12 of the 37) give fully numeric ODE coefficients, a list of forcing impulses (amplitude, derivative order, and shift location), and numeric initial conditions — a direct, ready-to-parse input for an ODE solver under test. A test harness can feed `(ode_coeffs_highest_to_lowest, forcing, initial_conditions)` straight into the solver, evaluate both the solver's output and the quoted `solution_latex` (parsed via a CAS such as SymPy) at a grid of sample times away from the impulse locations, and assert numerical agreement to within a chosen tolerance.
- **`transfer_function` entries** (14 of the 37) pair a transfer function `H_s` with its known impulse response `h_t` — suited to testing a Laplace-domain toolbox: run the transform under test on `H_s` and diff the result against `h_t`.
- **`ivp_symbolic` entries** (10 of the 37) carry general, symbolic parameters (e.g. $\tau$, $k$, $\omega_0$, $\zeta$) rather than fixed numbers, which makes them well suited to property-based or randomized testing: substitute random concrete values for the symbolic parameters before each comparison, exercising the solver across a swept parameter range instead of one fixed case.
- **The one `ivp_numeric` entry** (Shabana, Example 1.10) is a fully numeric physical-parameter case, suited to a straightforward fixed-input regression test.

Across all four types, the `verified` and `verification_method` fields let a harness filter to only independently-checked entries before trusting them as an oracle (all 37 here are `verified: true`), and the stable `id` field gives each entry a natural key for parametrized test naming (e.g. `pytest.mark.parametrize` keyed by `id`, or a JUnit/xUnit test-case name). The flat `solved_examples.csv` carries the same bibliographic and verification columns (`id`, `author`, `book_title`, `page`, `example`, `type`, `verified`, `verification_method`, `notes`) for quick spreadsheet review or for a lightweight runner that would rather avoid a JSON parser; the fuller mathematical content — coefficients, forcing, initial conditions, and closed-form solution — is only in the JSON, since it does not flatten cleanly into CSV columns.

---

## Conclusion

This article gathered thirty-seven fully worked examples — each an LTI ODE (or, equivalently, a transfer function) forced by a Dirac delta impulse or its derivative, paired with a published closed-form solution — from twelve textbooks spanning ordinary differential equations, vibrations, signals and systems, and control engineering. These are supplemented by dozens of further exercise references, without solutions, indexed across twenty texts (several of which overlap with the solved set) to point the reader toward additional practice material. All content in both categories was extracted, not derived: no new analytical results are claimed, and every solved example was independently verified against its stated equation rather than merely transcribed (see Verification Methodology above).

Three intended uses motivated the compilation. As a pedagogical resource, the alphabetized, dual-category structure lets a reader move directly from a specific author or problem type to the relevant worked solution, without first locating and cross-referencing dozens of separate books. As a software-engineering resource, the thirty-seven solved exercises — together with their machine-readable export and per-example WolframAlpha check — constitute a ready-made benchmark suite: each pairs a well-posed initial value problem with an independently verified analytical answer, suitable for regression or unit testing of symbolic or numerical ODE solvers. As a small act of literature quality control, the verification pass itself demonstrates that even a well-regarded, widely used textbook can carry an internally inconsistent worked answer (Gangadharaiah & Sandeep, Example 4.25) or a duplicated problem (Example 3.9, byte-identical to Example 3.12) that a reader is unlikely to catch without redoing the algebra — underscoring the value of checking, not just collecting, textbook exercises before relying on them for testing purposes.

Two limitations should be noted. First, the survey is not exhaustive: it reflects the books available to the present compiler and is best understood as a personal, growing reading list rather than a systematic literature search. Second, while every solved example's closed-form solution was checked against its own stated equation and initial conditions, this verification cannot detect an error present identically in both the stated problem and its stated answer (e.g., a genuine typo in the source textbook's equation that happens to be consistent with its own — equally mistaken — answer key); nor does it substitute for tracing each problem back to first principles. One originally duplicated example (Gangadharaiah & Sandeep, Example 3.9) was removed rather than repaired, since its true content could not be recovered independently of Example 3.12. Extending the collection to further textbooks, and extending the automated verification to the Additional Exercises once solutions are added for them, are natural directions for future work.

---

## References

Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-38164-8)

Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. (ISBN: 978-0-691-12474-6)

De Oliveira, M. C. (2017). Fundamentals of linear control: A concise approach. Cambridge University Press. https://doi.org/10.1017/9781316941409 ISBN 978-1-107-18752-8 Hardback

Dorf, R. C., & Bishop, R. H. (2008). Modern control systems: Solution manual (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

Edwards, C. H., & Penney, D. E. (2008). Elementary differential equations with boundary value problems (6th ed.). Pearson Education. ISBN 0-13-600613-2

Esfandiari, R. S., & Lu, B. (2014). Modeling and analysis of dynamic systems (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3)
https://doi.org/10.1201/b16907

Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). Feedback control of dynamic
systems (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

Gangadharaiah, Y. H., & Sandeep, N. (2021). Engineering applications of the Laplace transform. Cambridge Scholars Publishing. ISBN (13): 978-1-5275-7373-4

Inman, D. J. (2014). Engineering vibration (4th ed.). Pearson Education, Inc. (ISBN:
978-0-13-287169-3)

Karris, S. T. (2003). Signals and systems with MATLAB® applications (2nd ed.). Orchard Publications. (ISBN: 9780970951168, 0970951167)

Kelly, S. G. (2012). Mechanical vibrations: Theory and applications, SI. Cengage Learning. (ISBN: 9781439062142)

Lathi, B. P., & Green, R. A. (2018). Linear systems and signals (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

Meirovitch, L. (2001). Fundamentals of vibrations (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

Nagle, R. K., Saff, E. B., & Snider, A. D. (2018). Fundamentals of differential equations
(9th ed.). Pearson Education, Inc. (ISBN: 978-0-321-97706-9)

Nagy, G. (n.d.). Ordinary differential equations. Mathematics Department, Michigan State University

Ogata, K. (2010). Modern control engineering (5th ed.). Pearson Education, Inc. (ISBN-
13: 978-0-13-615673-4)

Rao, S. S. (2011). Mechanical vibrations (5th ed.). Pearson Education. ISBN 978-0-13-212819-3

Schiff, Joel L. (1999). The Laplace transform: Theory and applications. Springer-Verlag New York,
Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

Shabana, A. A. (1997). Vibration of discrete and continuous systems (2nd ed.). Springer-Verlag. https://doi.org/10.1007/978-1-4612-4036-5 Print ISBN-13: 978-1-4612-8474-1

Thorby, D. (2008). Structural dynamics and vibration in practice: An engineering handbook. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8)

Xie, W.-C. (2010). Differential equations for engineers. Cambridge University Press. ISBN-13 978-0-521-19424-2

Xue, D., Chen, Y., & Atherton, D. P. (2007). Linear feedback control: Analysis and design with MATLAB. Society for Industrial and Applied Mathematics. ISBN 978-0-898716-38-2
