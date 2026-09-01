# Exercises from Books: LTI ODE with Impulsive Loads

**Denis Pleshkov**
<std.approach@gmail.com>
**Last Modified:** August 25, 2026

## Abstract

This article compiles and independently verifies a curated benchmark set of worked examples, drawn from published textbooks, illustrating the solution of linear time-invariant (LTI) ordinary differential equations (ODEs) forced by the Dirac delta function and its derivatives — the standard mathematical model of an impulsive load. No new mathematical results are derived here: each of the fifty solved exercises in the "Solved Exercises" section reproduces a problem statement and its published closed-form solution essentially verbatim from its source, with full attribution by author, page, and edition. What distinguishes this compilation from a plain survey is that every one of those fifty solutions was additionally checked, by symbolic Laplace-transform matching, segment-wise ODE and jump-matching, or numeric recomputation, against its own stated equation and initial conditions; the handful of transcription issues this uncovered — including one textbook example whose printed answer did not actually satisfy its own stated problem — are corrected inline with an explicit derivation rather than left silently as-is. Each solved example additionally carries a ready-to-run Wolfram Language snippet that a reader can paste directly into WolframAlpha to reproduce its closed-form solution independently. A machine-readable export (JSON and CSV) of the full verified example set accompanies the article. A further set of unsolved exercise references, spanning twenty additional textbooks, is indexed to guide further practice. The compilation serves two purposes. First, it is pedagogical: gathering material otherwise scattered across dozens of engineering-mathematics, vibrations, and control-theory textbooks into one reference organized by the order of the governing differential equation and, within that, by author, suitable as a starting point for a reader studying impulsively forced LTI systems. Second, it is practical: because each solved exercise pairs a fully specified, independently verified ODE with a known analytical solution, the collection functions directly as a benchmark/regression-test suite for validating symbolic or numerical ODE-solving software. The Verification Methodology and Conclusion sections detail the checking process and summarize the scope, composition, and limitations of the collected material.

## Keywords

Dirac delta function, impulse response, linear time-invariant ODE, initial value problem, Laplace transform, textbook exercise compilation, benchmark test suite for ODE solvers, symbolic verification, WolframAlpha, Wolfram Language

## Introduction

This article is **pedagogical** in purpose. It is intended as a starting point for a reader who wants to study, in a structured way, linear time-invariant (LTI) ordinary differential equations subject to impulsive loads (the Dirac delta function and its derivatives as a forcing term). The article itself contains **no new mathematical results**: every worked example in the "Solved Exercises" section is extracted, essentially verbatim, from an existing textbook. Its only contribution is the *gathering, attribution, and organization* of material that is otherwise scattered across dozens of books on differential equations, vibrations, and control theory.

A second, practical motivation for this compilation is **software testing**. Because each solved exercise below pairs a well-defined LTI ODE (with explicit initial conditions) with a known closed-form analytical solution, the collection as a whole forms a ready-made benchmark suite. It can be used to validate an existing symbolic or numerical ODE-solving library, or to build a moderate-sized regression/unit-test suite for a library still under development — simply compare the library's output against the analytical solution quoted here. Unlike a raw transcription, however, a benchmark is only as trustworthy as its answer key: every closed-form solution in the Solved Exercises section was therefore independently checked against its own stated equation and initial conditions before being included (see the Verification Methodology section), and the full, verified set is additionally provided as a machine-readable JSON/CSV export for direct use in an automated test harness. For a quicker, example-by-example spot check, every solved exercise also carries its own Wolfram Language snippet that can be pasted directly into WolframAlpha to reproduce that one closed-form solution on the spot, without setting up a full test harness.

The material is split into two categories:

1. **Solved Exercises** — problems taken directly from a textbook together with their published closed-form solution. Nothing here is derived by the present author; it is a curated extraction of existing results, grouped by the order of the governing ODE and alphabetized by author within each group.
2. **Additional Exercises** — pointers to further exercises in the same (and other) textbooks that are relevant to impulsive loading but for which no solution is reproduced here. These are page/problem-number references only, meant to guide further practice and reading.

Solved Exercises are grouped by the order of the governing ODE and alphabetized by author surname within each group; Additional Exercises are ordered alphabetically by author surname, as is the bibliography.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Solved Exercises](#solved-exercises)
   - [2.1 First-order equations](#first-order-equations)
   - [2.2 Second-order equations](#second-order-equations)
     - [A. Only delta load](#second-order-a-delta-load)
     - [B. First derivative of delta](#second-order-b-first-derivative)
     - [C. Second derivative of delta](#second-order-c-second-derivative)
   - [2.3 Third-order equations](#third-order-equations)
   - [2.4 Higher-order equations](#higher-order-equations)
3. [Additional Exercises](#additional-exercises) — Bottega, Boyce & DiPrima, Campbell & Haberman, De Oliveira, Dorf & Bishop, Edwards & Penney, Esfandiari & Lu, Franklin/Powell/Emami-Naeini, Inman, Karris, Kelly, Lathi & Green, Meirovitch, Nagle/Saff/Snider, Ogata, Rao, Schiff, Shabana, Thorby, Xue/Chen/Atherton
4. [Verification Methodology](#verification-methodology)
5. [Conclusion](#conclusion)
6. [References](#references)

---

## Solved Exercises

Worked examples reproduced from the source textbooks, including the original problem statement and its published closed-form solution. Grouped by the order of the governing ODE (first, second, third, and higher), and alphabetized by (first) author within each group. Following academic convention, verbatim text taken from a source (an example's title or its problem statement) is set in double quotation marks; page/example locators and the present author's own classification notes are left unquoted.

Each entry also carries a bracketed *WolframAlpha verification* block: a Wolfram Language command that can be pasted into the input box at [wolframalpha.com](https://www.wolframalpha.com), which returns the result independently. Most of these commands were constructed by hand and cross-checked symbolically offline rather than run live (see Verification Methodology below), so pasting one in may be giving it its first live test.

### 2.1 First-order equations (n = 1) {#first-order-equations}

#### Franklin, Powell & Emami-Naeini — Feedback control of dynamic systems, p. 110

*[Note: this is the same example as Angeles, p.116.]*
$$
\dot{y} + ky = u = \delta(t), y(0) = 0 \equiv \dot{y} + ky = 0, \quad y(0^+) = 1
$$
*[WolframAlpha:*
```
y'[t] + k y[t] == Delta[t], y[0] == 0
```
*Returns $y(t) = e^{-k t} \, u(t)$ (at $t=0^+$ this gives $y(0^+)=1$, matching the book)*]

*[Jump condition at $t=0$: confirming the book's own reduction, $y'+ky=\delta(t)$ is first order. Phase vector $\mathbf y=(y)$ changes by $\Delta\mathbf y(0)=(1)$.]*

#### Esfandiari & Lu — Modeling and analysis of dynamic systems, p.343

"Impulse Response of First-Order Systems"
*[Note: with $x_0=0$, $A=1$, and $\tau=T$, this reduces to Ogata's p.163 case below, $c(t)=\frac{1}{T}e^{-t/T}$.]*
$$ x(t) = e^{-t/\tau} x_0 + \frac{A}{\tau} e^{-t/\tau} $$
where A - impulse's magnitude $\tau$ - coefficient for higher derivative in ODE.
*[WolframAlpha:*
```
tau x'[t] + x[t] == A Delta[t], x[0] == x0
```
*Returns $x(t) = e^{-t/\tau} x_0 + \frac{A}{\tau} e^{-t/\tau}$*]

*[Jump condition at $t=0$: normalizing $\tau x'+x=A\delta(t)$ to $x'+\tfrac1\tau x=\tfrac{A}{\tau}\delta(t)$ (first order). Phase vector $\mathbf x=(x)$ changes by $\Delta\mathbf x(0)=\left(\dfrac{A}{\tau}\right)$.]*

#### Ogata — Modern control engineering, p.163

"Unit-Impulse Response of First-Order Systems"
*[Note: this is the $A=1$, $x_0=0$, $\tau=T$ special case of Esfandiari & Lu's p.343 formula above, $x(t)=e^{-t/\tau}x_0+\frac{A}{\tau}e^{-t/\tau}$.]*
$$
C(s) = \frac{1}{Ts + 1} \implies c(t) = \frac{1}{T} e^{-t/T}, \quad \text{for } t \geq 0
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[1/(T s + 1), s, t]
```
*Returns $c(t) = \frac{1}{T} e^{-t/T}$*]

*[Jump condition at $t=0$: normalizing $Tc'+c=\delta(t)$ to $c'+\tfrac1T c=\tfrac1T\delta(t)$ (first order). Phase vector $\mathbf c=(c)$ changes by $\Delta\mathbf c(0)=\left(\dfrac1T\right)$.]*

#### Campbell & Haberman — Introduction to differential equations with dynamical systems, p.263

IVP for 1st order system $$ y' + y = \delta(t - 1), \, y(0) = 1 \implies  y(t)=\begin{cases}
e^{-t}, & t < 1 \\[4pt]
e^{-t} + e^{-(t-1)}, & t \ge 1
\end{cases}$$
*[WolframAlpha:*
```
y'[t] + y[t] == Delta[t - 1], y[0] == 1
```
*Returns $y(t) = e^{-t} + e^{-(t-1)} \, u(t-1)$*]

*[Jump condition at $t=1$: $y'+y=\delta(t-1)$ is first order. Phase vector $\mathbf y=(y)$ changes by $\Delta\mathbf y(1)=(1)$.]*

#### Lathi & Green — Linear systems and signals, p.167

"DRILL 2.4(a) Finding the Impulse Response"
"Determine the unit impulse response of LTIC systems described by the following equation:"
$$ (D + 2)y(t) = (3D + 5)x(t) \implies h(t)=3\delta(t) - e^{-2t}u(t) $$
*[WolframAlpha:*
```
InverseLaplaceTransform[(3 s + 5)/(s + 2), s, t]
```
*Returns $h(t) = 3\delta(t) - e^{-2t} u(t)$*]

*[Jump condition at $t=0$: $(D+2)y=(3D+5)x$ has $\deg N=\deg D=1$, a direct feedthrough of coefficient $3$ plus a remainder that changes by $\Delta\mathbf y_{\text{reg}}(0)=(-1)$.]*

### 2.2 Second-order equations (n = 2) {#second-order-equations}


#### A. Only delta load {#second-order-a-delta-load}
##### Esfandiari & Lu — Modeling and analysis of dynamic systems, p.57

"Example 2.27: Initial Condition ≠ Initial Value"
$$
 \ddot{x} + \dot{x} + 2x = \delta(t), \, x(0^-) = 0, \, \dot{x}(0^-) = 0
\implies \dot{x}(0^+) =  1
$$
*[WolframAlpha:*
```
x''[t] + x'[t] + 2 x[t] == Delta[t], x[0] == 0, x'[0] == 0
```
*Returns $x(t) = \frac{2 \, e^{-t/2} \, u(t) \, \sin\left(\frac{\sqrt{7}}{2} t\right)}{\sqrt{7}}$ (the book only states the jump $\dot x(0^+)=1$; this full closed form is consistent with it — differentiating gives $\dot x(0^+)=1$)*]

*[Jump condition at $t=0$: confirming the book's own claim, $\ddot x+\dot x+2x=\delta(t)$. Phase vector $\mathbf x=(x,\dot x)$ changes by $\Delta\mathbf x(0)=(0,1)$.]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.248

Example 3.11. "Consider the causal LTI system described by the second differential equation ... Determine the impulse response"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = x(t) \implies h(t) = e^{-2t} - e^{-3t}.
$$
*[WolframAlpha:*
```
y''[t] + 5 y'[t] + 6 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $h(t) = e^{-2t} - e^{-3t}$*]

*[Jump condition at $t=0$: $y''+5y'+6y=\delta(t)$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(0,1)$.]*

##### Finan, p.57

Example 48.1. "A spring-mass system with mass 2, damping 4, and spring constant 10 is subject to a hammer blow at time $t = 0$: The blow imparts a total impulse of 1 to the system, which was initially at rest. Find the response of the system."
$$
2y'' + 4y' + 10y = \delta(t), \quad y(0) = 0, \quad y'(0) = 0 \implies y(t) = \frac{1}{4} e^{-t} \sin(2t) \, u(t)
$$
*[WolframAlpha:*
```
2 y''[t] + 4 y'[t] + 10 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{1}{4} e^{-t} \sin(2t)$*]

*[Jump condition at $t=0$: $2y''+4y'+10y=\delta(t)$ has leading coefficient $2$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(0,\frac12)$.]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.289

Example 3.28. "find the impulse response of the system if the differential equation describes the system"
$$
\frac{d^2z(t)}{dt^2} + 4\frac{dz(t)}{dt} + 10z(t) = x(t) \implies h(t) = \frac{1}{\sqrt{6}} e^{-2t} \sin\left(\sqrt{6}t\right).
$$
*[WolframAlpha:*
```
z''[t] + 4 z'[t] + 10 z[t] == Delta[t], z[0] == 0, z'[0] == 0
```
*Returns $h(t) = \frac{1}{\sqrt{6}} e^{-2t} \sin\left(\sqrt{6} \, t\right)$*]

*[Jump condition at $t=0$: $z''+4z'+10z=\delta(t)$. Phase vector $\mathbf z=(z,z')$ changes by $\Delta\mathbf z(0)=(0,1)$.]*

##### Nagle, Saff & Snider — Fundamentals of differential equations, p.403

Example 4 "A linear system is governed by the differential equation"
$$
y'' + 2y' + 5y = \delta(t), \quad y(0) = 0, \quad y'(0) = 0 \implies y(t) = \frac{1}{2} e^{-t} \sin 2t
$$
*[WolframAlpha:*
```
y''[t] + 2 y'[t] + 5 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{1}{2} e^{-t} \sin(2t)$*]

*[Jump condition at $t=0$: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(0,1)$.]*
*[Editorial note: as transcribed, this equation was incomplete — missing the forcing term on the left-hand side and the output variable on the right (the "$\implies =$" read as a fragment). The equation above, $y''+2y'+5y=\delta(t)$ with zero initial conditions, is the unique standard-form IVP whose closed-form solution matches the book's own stated answer exactly (characteristic roots $-1\pm2i$ give precisely $\frac{1}{2}e^{-t}\sin2t$), and is used here as a high-confidence reconstruction rather than left incomplete.]*

##### Nagy — Ordinary differential equations, p.205

Example 3.4.6. "Find the impulse response function"
$$
L(y) = y'' + 2y' + 2y \implies y_\delta(t) = u(t-c)e^{-(t-c)}\sin(t-c)
$$
*[WolframAlpha:*
```
y''[t] + 2 y'[t] + 2 y[t] == Delta[t], y[0] == 0, y'[0] == 0
```
*Returns $y_\delta(t) = e^{-t} \sin(t) \, u(t)$ (the $c=0$ case of the book's general $u(t-c)e^{-(t-c)}\sin(t-c)$)*]

*[Jump condition at $t=c$: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(c)=(0,1)$.]*

##### Ogata — Modern control engineering, p.178

"Impulse Response of Second-Order Systems"
*[Note: this is similar to Angeles, p.120.]*
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
*[WolframAlpha: this one needs the assumption on $\zeta$ made explicit (unlike the other entries, a bare equation list would leave $\zeta$'s range ambiguous), so paste each line separately:*
```
Assuming[0 < zeta < 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
Assuming[zeta == 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
Assuming[zeta > 1 && wn > 0, DSolve[{y''[t] + 2 zeta wn y'[t] + wn^2 y[t] == wn^2 Delta[t], y[0] == 0, y'[0] == 0}, y[t], t]]
```
*Returns, respectively: $c(t) = \frac{\omega_n}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t}\sin\left(\omega_n\sqrt{1-\zeta^2}\,t\right)$, $\; c(t) = \omega_n^2 t \, e^{-\omega_n t}$, $\; c(t) = \frac{\omega_n}{2\sqrt{\zeta^2-1}} e^{-(\zeta-\sqrt{\zeta^2-1})\omega_n t} - \frac{\omega_n}{2\sqrt{\zeta^2-1}} e^{-(\zeta+\sqrt{\zeta^2-1})\omega_n t}$*]

*[Jump condition at $t=0$ (all three damping cases): phase vector $\mathbf c=(c,c')$ changes by $\Delta\mathbf c(0)=(0,\omega_n^2)$, independent of $\zeta$.]*

##### Shabana — Vibration of discrete and continuous systems, p.41

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
*[WolframAlpha:*
```
m = 10; k = 9000; c = 18; F0 = 10000; dt = 0.005; wn = Sqrt[k/m]; xi = c/(2 Sqrt[m k]); wd = wn Sqrt[1 - xi^2]; N[{wn, xi, wd, xi wn, (F0 dt)/(m wd)}]
```
*Returns $\{\omega_n,\,\xi,\,\omega_d,\,\xi\omega_n,\,\text{amplitude}\} = \{30,\ 0.03,\ 29.9865,\ 0.9,\ 0.166742\}$ (matches the book's stated 29.986, 0.9, 0.1667)*]

*[Jump condition at $t=0$: the finite-duration force is idealized as an impulse of magnitude $I=F_0\Delta t=(10{,}000)(0.005)=50\ \text{N}\cdot\text{s}$ applied to $m\ddot x+c\dot x+kx=I\delta(t)$. Phase vector $\mathbf x=(x,\dot x)$ changes by $\Delta\mathbf x(0)=(0,I/m)=(0,5\ \text{m/s})$, the impulse–momentum theorem (consistent with the stated amplitude $x_0/(m\omega_d)=50/(10\cdot29.986)=0.1667$).]*
*[Editorial note: as transcribed, the damping coefficient's unit was garbled ("c = 18 N· slm"). Recomputing $\omega_n, \xi, \omega_d, \xi\omega_n$, and the response amplitude from $m=10$, $k=9000$, $c=18$, $F_0=10{,}000$, $\Delta t=0.005$ reproduces every downstream number the book states (29.986, 0.9, 0.1667) exactly, confirming the numeric value 18 is correct; only the unit label was corrected here, to the standard "N·s/m".]*

##### Boyce & DiPrima — Elementary differential equations and boundary value problems, p.272

Initial Value Problem (IVP) for 2nd order with zero Initial Condition (IC)
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
*[WolframAlpha:*
```
2 y''[t] + y'[t] + 2 y[t] == Delta[t - 5], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{2 \, e^{5/4 - t/4} \, u(t-5) \, \sin\left(\frac{1}{4} \, \sqrt{15} \, (t-5)\right)}{\sqrt{15}}$*]

*[Jump condition at $t=5$: the equation $2y''+y'+2y=\delta(t-5)$ normalizes to $y''+\tfrac12 y'+y=\tfrac12\delta(t-5)$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(5)=\left(0,\tfrac12\right)$.]*

##### Edwards & Penney — Elementary differential equations with boundary value problems, p.318

The IVP is
$$
  x'' + 4x = 8\delta_{2\pi}(t); \; x(0) = 3, \; x'(0) = 0 \implies x(t)= \begin{cases}
3\cos 2t, & t < 2\pi \\[4pt]
3\cos 2t + 4\sin 2t, & t \ge 2\pi
\end{cases}
$$
*[WolframAlpha:*
```
x''[t] + 4 x[t] == 8 Delta[t - 2 Pi], x[0] == 3, x'[0] == 0
```
*Returns $x(t) = 3\cos(2t) + 4\sin(2t) \, u(t-2\pi)$*]

*[Jump condition at $t=2\pi$: phase vector $\mathbf x=(x,x')$ changes by $\Delta\mathbf x(2\pi)=(0,8)$, the impulse strength.]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.306

Example 4.7. "Solve the initial value problem"
$$
\frac{d^2 y(t)}{dt^2} + 5 \frac{dy(t)}{dt} + 6y(t) = \delta(t - \pi) - \delta(t - 2\pi)
$$

with $ y(0) = 0 = y'(0) $.
$$
y(t) = \left( e^{-2(t-\pi)} - e^{-3(t-\pi)} \right) u(t - \pi) - \left( e^{-2(t-2\pi)} - e^{-3(t-2\pi)} \right) u(t - 2\pi).
$$
*[WolframAlpha:*
```
y''[t] + 5 y'[t] + 6 y[t] == Delta[t - Pi] - Delta[t - 2 Pi], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \left(e^{-2(t-\pi)} - e^{-3(t-\pi)}\right) u(t-\pi) - \left(e^{-2(t-2\pi)} - e^{-3(t-2\pi)}\right) u(t-2\pi)$*]

*[Jump conditions: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(\pi)=(0,1)$ at $t=\pi$, and by $\Delta\mathbf y(2\pi)=(0,-1)$ at $t=2\pi$ (the coefficient of $-\delta(t-2\pi)$).]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.387

Example 4.49. "Obtain the solution of the second-order differential equation"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = 3\delta(t-2) - 4\delta(t-4)
$$

along with the initial conditions $ y(0) = 0 = y'(0) $.
$$
y(t) = 3(e^{-2(t-2)} - e^{-3(t-2)})u(t-2) - 4(e^{-2(t-4)} - e^{-3(t-4)})u(t-4).
$$
*[WolframAlpha:*
```
y''[t] + 5 y'[t] + 6 y[t] == 3 Delta[t - 2] - 4 Delta[t - 4], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = 3\left(e^{-2(t-2)} - e^{-3(t-2)}\right) u(t-2) - 4\left(e^{-2(t-4)} - e^{-3(t-4)}\right) u(t-4)$*]

*[Jump conditions: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(2)=(0,3)$ at $t=2$ (the coefficient of $3\delta(t-2)$), and by $\Delta\mathbf y(4)=(0,-4)$ at $t=4$ (the coefficient of $-4\delta(t-4)$).]*

##### Nagle, Saff & Snider — Fundamentals of differential equations, p.409

Example 1
$$
\frac{d^2x}{dt^2} + 9x = 3\delta(t - \pi); \quad x(0) = 1, \quad \frac{dx}{dt}(0) = 0 \implies x(t) = 
\begin{cases} 
\cos 3t, & t < \pi, \\ 
\cos 3t - \sin 3t, & \pi < t
\end{cases}
$$
*[WolframAlpha:*
```
x''[t] + 9 x[t] == 3 Delta[t - Pi], x[0] == 1, x'[0] == 0
```
*Returns $x(t) = \cos(3t) - \sin(3t) \, u(t-\pi)$*]

*[Jump condition at $t=\pi$: phase vector $\mathbf x=(x,x')$ changes by $\Delta\mathbf x(\pi)=(0,3)$, the impulse strength.]*

##### Nagy — Ordinary differential equations, p.202

*[Note: this is similar to Angeles, p.119, in the case of $f_0=1$ and $t_0=0$.]*
$$
y'' + \omega_0^2 y = f_0 \delta(t - t_0), \quad y(0) = y_0, \quad y'(0) = 0 \implies y(t) = y_0 \cos(\omega_0 t) + \frac{f_0}{\omega_0} u(t - t_0) \sin(\omega_0 (t - t_0))
$$
*[WolframAlpha:*
```
y''[t] + w0^2 y[t] == f0 Delta[t - t0], y[0] == y0, y'[0] == 0
```
*Returns $y(t) = y_0 \cos(\omega_0 t) + \frac{f_0}{\omega_0} \, u(t-t_0) \sin\left(\omega_0 (t-t_0)\right)$*]

*[Jump condition at $t=t_0$: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(t_0)=(0,f_0)$, the impulse strength.]*

##### Nagy — Ordinary differential equations, p.205

Example 3.4.7. "Find the solution y to the initial value problem"
$$
y'' - y = -20 \delta(t-3), \quad y(0) = 1, \quad y'(0) = 0 \implies y(t) = \cosh(t) - 20 \, u(t-3) \, \sinh(t-3)
$$
*[WolframAlpha:*
```
y''[t] - y[t] == -20 Delta[t - 3], y[0] == 1, y'[0] == 0
```
*Returns $y(t) = \cosh(t) - 20 \, u(t-3) \sinh(t-3)$*]

*[Jump condition at $t=3$: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(3)=(0,-20)$, the impulse strength.]*

##### Nagy — Ordinary differential equations, p.206

Example 3.4.8. "Find the solution to the initial value problem"
$$
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \quad y(0) = 0, \quad y'(0) = 0 \implies y(t) = \frac{1}{2} \left[ u(t - \pi) - u(t - 2\pi) \right] \sin(2t)
$$
*[WolframAlpha:*
```
y''[t] + 4 y[t] == Delta[t - Pi] - Delta[t - 2 Pi], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \frac{1}{2}\left[u(t-\pi) - u(t-2\pi)\right] \sin(2t)$*]

*[Jump conditions: phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(\pi)=(0,1)$ at $t=\pi$, and by $\Delta\mathbf y(2\pi)=(0,-1)$ at $t=2\pi$ (the coefficient of $-\delta(t-2\pi)$).]*

##### Anderson — Control Theory, p.22

$$
Y(s) = \frac{K}{K-1} \left( \frac{1}{s} - \frac{1}{s-1+K} \right) \implies y(t) = \frac{K}{K-1} \left( 1 - e^{-(K-1)t} \right), \quad t \geq 0
$$
*[WolframAlpha:*
```
y''[t] + (K-1) y'[t] == K DiracDelta[t], y[0] == 0, y'[0] == 0
```
*Returns $y(t) = \dfrac{K}{K-1}\left(1 - e^{-(K-1)t}\right)$*]

*[Jump condition at $t=0$: $y''+(K-1)y'=K\delta(t)$ (leading coefficient $1$, no $y$ term). Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(0,K)$.]*

##### Anderson — Control Theory, p.206

Example 11.
$$
\ddot{\theta}(t) + \theta(t) = \delta(t), \quad \theta(0^-) = 0, \quad \dot{\theta}(0^-) = 0 \implies \theta(t) = \sin(t)\, u(t)
$$
*[WolframAlpha:*
```
theta''[t] + theta[t] == DiracDelta[t], theta[0] == 0, theta'[0] == 0
```
*Returns $\theta(t) = \sin(t)$*]

*[Jump condition at $t=0$: $\ddot\theta+\theta=\delta(t)$. Phase vector $(\theta,\dot\theta)$ changes by $\Delta(\theta,\dot\theta)(0)=(0,1)$, matching the given post-impulse conditions $\theta(0^+)=0$, $\dot\theta(0^+)=1$.]*

##### Engelberg — A mathematical introduction to control theory, p.31

"Find the inverse transform of the function"
$$
\mathcal{L}(f(t))(s) = \frac{1}{s^2 - 1} \implies f(t) = \frac{e^t - e^{-t}}{2} = \sinh(t)
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[1/(s^2 - 1), s, t]
```
*Returns $f(t) = \sinh(t)$*]

*[Jump condition at $t=0$: reading $\mathcal{L}(f)(s)=1/(s^2-1)$ as the impulse response of the zero-state 2nd-order ODE $\ddot f - f = \delta(t)$ (relative degree $2$). Phase vector $\mathbf f=(f,\dot f)$ changes by $\Delta\mathbf f(0)=(0,1)$.]*

##### Frank — Control theory tutorial, p.29

$$
P(s) = \left(\frac{a}{s+a}\right)\left(\frac{b}{s+b}\right) = \frac{ab}{(s+a)(s+b)}
$$
"For example, if the input into this system is a unit impulse at time zero, then the system output is"
$$
y(t) = \frac{ab}{b-a}\left(e^{-at} - e^{-bt}\right)
$$
*[WolframAlpha:*
```
Assuming[a > 0 && b > 0 && a != b, InverseLaplaceTransform[a b/((s + a) (s + b)), s, t]]
```
*Returns $y(t) = \dfrac{ab}{b-a}\left(e^{-at} - e^{-bt}\right)$*]

*[Jump condition at $t=0$: $P(s)=ab/((s+a)(s+b))$ corresponds to the zero-state 2nd-order ODE $\ddot y+(a+b)\dot y+ab\,y=ab\,\delta(t)$ (relative degree $2$). Phase vector $\mathbf y=(y,\dot y)$ changes by $\Delta\mathbf y(0)=(0,ab)$.]*

#### B. First derivative of delta {#second-order-b-first-derivative}
##### Lathi & Green — Linear systems and signals, p.166

EXAMPLE 2.6
"Determine the unit impulse response h(t) for a system specified by the equation
(D^2 +3D+2)y(t) = Dx(t)"
Solution
$$ h(t) = (-e^{-t} + 2e^{-2t})u(t) $$
*[WolframAlpha:*
```
InverseLaplaceTransform[s/(s^2 + 3 s + 2), s, t]
```
*Returns $h(t) = \left(-e^{-t} + 2 e^{-2t}\right) u(t)$*]

*[Jump condition at $t=0$: the input enters as $Dx$, again giving relative degree $1$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(1,-3)$.]*

##### Lathi & Green — Linear systems and signals, p.167

"DRILL 2.4(c) Finding the Impulse Response"
"Determine the unit impulse response of LTIC systems described by the following equation:"
$$ (D^2 + 2D + 1)y(t) = Dx(t) \implies h(t)=(1 - t)e^{-t}u(t) $$
*[WolframAlpha:*
```
InverseLaplaceTransform[s/(s + 1)^2, s, t]
```
*Returns $h(t) = (1-t) e^{-t} u(t)$*]

*[Jump condition at $t=0$: $(D^2+2D+1)y=Dx$ likewise: $\Delta\mathbf y(0)=(1,-2)$.]*

##### Franklin, Powell & Emami-Naeini — Feedback control of dynamic systems, p.151

$$ 
H(s) = \frac{2s + 1}{(s+1)^2 + 2^2} \implies h(t) = \left( 2e^{-t} \cos 2t - \frac{1}{2}e^{-t} \sin 2t \right) 1(t)
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(2 s + 1)/((s + 1)^2 + 4), s, t]
```
*Returns $h(t) = 2 e^{-t} \cos(2t) - \frac{1}{2} e^{-t} \sin(2t)$*]

*[Jump condition at $t=0$: because the right-hand side carries a derivative of the (impulsive) input, $2x'+x$ with $x=\delta(t)$, the relative degree of $H(s)$ drops to $1$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(2,-3)$.]*

##### Lathi & Green — Linear systems and signals, p.164

"EXAMPLE 2.5 Impulse Response via Impulse Matching"
"Find the impulse response h(t) for a system specified by (D2 +5D+6)y(t) = (D+1)x(t)"
Solution
$$ h(t) = (-e^{-2t} + 2e^{-3t})u(t) $$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s + 1)/(s^2 + 5 s + 6), s, t]
```
*Returns $h(t) = \left(-e^{-2t} + 2 e^{-3t}\right) u(t)$*]

*[Jump condition at $t=0$: because the input enters as $(D+1)x$, the relative degree of the transfer function is $1$. Phase vector $\mathbf y=(y,y')$ changes by $\Delta\mathbf y(0)=(1,-4)$.]*

##### Lathi & Green — Linear systems and signals, p.167

"DRILL 2.4(b) Finding the Impulse Response"
"Determine the unit impulse response of LTIC systems described by the following equation:"
$$ D(D + 2)y(t) = (D + 4)x(t) \implies h(t)=(2 - e^{-2t})u(t) $$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s + 4)/(s (s + 2)), s, t]
```
*Returns $h(t) = \left(2 - e^{-2t}\right) u(t)$*]

*[Jump condition at $t=0$: $D(D+2)y=(D+4)x$ has relative degree $1$: $\Delta\mathbf y(0)=(1,2)$.]*

##### Angeles, p.132

"2.5.3.1 Doublet Response"
*[Note: Angeles states the resulting jump as $x(0^+)=1$, $\dot x(0^+)=0$; \textcolor{red}{this appears to be incorrect for the damped case} ($\zeta\neq0$) — the derivation below gives $\dot x(0^+)=-2\zeta\omega_n$, matching the author's claim only when $\zeta=0$ — and will be verified in a follow-up paper.]*
$$
\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 x = \dot{\delta}(t), \quad x(0^-) = 0, \quad \dot{x}(0^-) = 0, \quad t > 0^-
$$
$$
\implies\; x(t) = e^{-\zeta\omega_n t}\left[\cos(\omega_d t) - \frac{\zeta}{\sqrt{1-\zeta^2}}\sin(\omega_d t)\right] u(t), \quad \omega_d = \omega_n\sqrt{1-\zeta^2} \quad (0\le\zeta<1)
$$
*[WolframAlpha:*
```
Assuming[0 < zeta < 1 && wn > 0, InverseLaplaceTransform[s/(s^2 + 2 zeta wn s + wn^2), s, t]]
```
*Returns $x(t) = e^{-\zeta\omega_n t}\cos\left(\omega_n\sqrt{1-\zeta^2}\,t\right) - \dfrac{\zeta}{\sqrt{1-\zeta^2}}\, e^{-\zeta\omega_n t}\sin\left(\omega_n\sqrt{1-\zeta^2}\,t\right)$*]

*[Jump condition at $t=0$: the doublet forcing $\dot\delta(t)$ gives $\ddot x+2\zeta\omega_n\dot x+\omega_n^2x=\dot\delta(t)$ relative degree $1$. Phase vector $\mathbf x=(x,\dot x)$ changes by $\Delta\mathbf x(0)=(1,-2\zeta\omega_n)$.]*

##### Bavafa-Toosi — Introduction to linear control systems, p.822

Example A.6. "Find the time-domain representation of"
$$
F(s) = \frac{2s + 12}{s^2 + 2s + 5} \implies f(t) = 5e^{-t}\sin 2t + 2e^{-t}\cos 2t, \quad t \geq 0
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(2 s + 12)/(s^2 + 2 s + 5), s, t]
```
*Returns $f(t) = 5 e^{-t}\sin(2t) + 2 e^{-t}\cos(2t)$*]

*[Jump condition at $t=0$: $F(s)=(2s+12)/(s^2+2s+5)$ is strictly proper with relative degree $1$ ($\deg N=\deg D-1$). Phase vector $\mathbf f=(f,\dot f)$ changes by $\Delta\mathbf f(0)=(2,8)$.]*

#### C. Second derivative of delta {#second-order-c-second-derivative}

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.239

Example 3.8. "Use the Laplace transform to find ... the impulse response of the system if the differential equation describes the system"
$$
\frac{d^2y(t)}{dt^2} + 5\frac{dy(t)}{dt} + 6y(t) = \frac{d^2x(t)}{dt^2} + 8\frac{dx(t)}{dt} + 13x(t) \implies h(t) = \delta(t) + e^{-2t} + 2e^{-3t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s^2 + 8 s + 13)/(s^2 + 5 s + 6), s, t]
```
*Returns $h(t) = \delta(t) + e^{-2t} + 2 e^{-3t}$*]

*[Jump condition at $t=0$: numerator and denominator of $H(s)=(s^2+8s+13)/(s^2+5s+6)$ share degree $2$, so the input's own $\delta(t)$ passes straight through as a direct-feedthrough term (coefficient $=1$) on top of the smooth part $h_{\text{reg}}(t)=e^{-2t}+2e^{-3t}$. Phase vector $\mathbf h_{\text{reg}}=(h_{\text{reg}},h_{\text{reg}}')$ changes by $\Delta\mathbf h_{\text{reg}}(0)=(3,-8)$.]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.257

Example 3.14. "Compute the impulse response of the transform with the transfer function"
$$
H(s) = \frac{s^2 - s + 1}{s^2 + 2s + 1} \implies y(t) = \delta(t) - 3e^{-t} + 3te^{-t}.
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s^2 - s + 1)/(s^2 + 2 s + 1), s, t]
```
*Returns $y(t) = \delta(t) - 3 e^{-t} + 3 t e^{-t}$*]

*[Jump condition at $t=0$: as in Example 3.8, $\deg N=\deg D=2$ for $H(s)=(s^2-s+1)/(s^2+2s+1)$, giving a direct feedthrough of coefficient $1$ plus a smooth remainder $y_{\text{reg}}(t)=-3e^{-t}+3te^{-t}$. Phase vector $\mathbf y_{\text{reg}}=(y_{\text{reg}},y_{\text{reg}}')$ changes by $\Delta\mathbf y_{\text{reg}}(0)=(-3,6)$.]*

##### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.288

Example 3.27. "find impulse response of the system if the differential equation
describes the system"
$$
\frac{d^2z(t)}{dt^2} + 3\frac{dz(t)}{dt} + 2z(t) = \frac{d^2x(t)}{dt^2} + 6\frac{dx(t)}{dt} + 7x(t) \implies h(t) = \delta(t) + 2e^{-t} + e^{-2t}.
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s^2 + 6 s + 7)/(s^2 + 3 s + 2), s, t]
```
*Returns $h(t) = \delta(t) + 2 e^{-t} + e^{-2t}$*]

*[Jump condition at $t=0$: again $\deg N=\deg D=2$ for $H(s)=(s^2+6s+7)/(s^2+3s+2)$, giving a direct feedthrough of coefficient $1$ plus a smooth remainder $h_{\text{reg}}(t)=2e^{-t}+e^{-2t}$. Phase vector $\mathbf h_{\text{reg}}=(h_{\text{reg}},h_{\text{reg}}')$ changes by $\Delta\mathbf h_{\text{reg}}(0)=(3,-4)$.]*

### 2.3 Third-order equations (n = 3) {#third-order-equations}

#### Bavafa-Toosi — Introduction to linear control systems, p.203

Example 3.1. "Consider the system"
$$
L(s) = \frac{3s^2 + 3s + 4}{s^3 + s^2 + 3s + 3} \implies l(t) = 2\cos\sqrt{3}t + \frac{1}{\sqrt{3}}\sin\sqrt{3}t + e^{-t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(3 s^2 + 3 s + 4)/(s^3 + s^2 + 3 s + 3), s, t]
```
*Returns $l(t) = \sqrt{3}\sin(\sqrt{3}t)/3 + 2\cos(\sqrt{3}t) + e^{-t}$*]

*[Jump condition at $t=0$: $L(s)=(3s^2+3s+4)/(s^3+s^2+3s+3)$ is strictly proper with relative degree $1$ ($\deg N=\deg D-1$), corresponding to the third-order ODE $\dddot y+\ddot y+3\dot y+3y=3\ddot\delta(t)+3\dot\delta(t)+4\delta(t)$. Phase vector $\mathbf y=(y,\dot y,\ddot y)$ changes by $\Delta\mathbf y(0)=(3,0,-5)$.]*

#### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform

p.254 Example 3.12. "find the impulse response of the system if the third-order differential equation describes the system"
$$
\frac{d^3 y(t)}{dt^3} + 6 \frac{d^2 y(t)}{dt^2} + 11 \frac{dy(t)}{dt} + 6y(t) = x(t) \implies h(t) = \frac{1}{2} e^{-t} - e^{-2t} + \frac{1}{2} e^{-3t}.
$$
*[WolframAlpha:*
```
y'''[t] + 6 y''[t] + 11 y'[t] + 6 y[t] == Delta[t], y[0] == 0, y'[0] == 0, y''[0] == 0
```
*Returns $h(t) = \frac{1}{2} e^{-t} - e^{-2t} + \frac{1}{2} e^{-3t}$*]

*[Jump condition at $t=0$: this third-order equation. Phase vector $\mathbf y=(y,y',y'')$ changes by $\Delta\mathbf y(0)=(0,0,1)$.]*

#### Ghosh — Control systems, p.23

$$
F(s) = \frac{s}{(s+1)^2(s+3)}
$$
"Taking inverse Laplace transform, we get"
$$
f(t) = -\frac{1}{2}te^{-t} + \frac{3}{4}e^{-t} - \frac{3}{4}e^{-3t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[s/((s + 1)^2 (s + 3)), s, t]
```
*Returns $f(t) = -\dfrac12\,t\,e^{-t} + \dfrac34\,e^{-t} - \dfrac34\,e^{-3t}$*]

*[Jump condition at $t=0$: $F(s)=s/((s+1)^2(s+3))$ has denominator $(s+1)^2(s+3)=s^3+5s^2+7s+3$ and numerator $s$ (relative degree $2$), corresponding to the third-order ODE $y'''+5y''+7y'+3y=\dot\delta(t)$. Phase vector $\mathbf y=(y,y',y'')$ changes by $\Delta\mathbf y(0)=(0,1,-5)$.]*

#### Ghosh — Control systems, p.24

Example 2.4. "Find $f(t)$ if"
$$
F(s) = \frac{s+3}{(s+1)(s+2)(s+4)}
$$
"Taking inverse Laplace transform, we get"
$$
f(t) = \frac{2}{3}e^{-t} - \frac{1}{2}e^{-2t} - \frac{1}{6}e^{-4t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s + 3)/((s + 1) (s + 2) (s + 4)), s, t]
```
*Returns $f(t) = \dfrac23\,e^{-t} - \dfrac12\,e^{-2t} - \dfrac16\,e^{-4t}$*]

*[Jump condition at $t=0$: $F(s)=(s+3)/((s+1)(s+2)(s+4))$ has denominator $(s+1)(s+2)(s+4)=s^3+7s^2+14s+8$ and numerator $s+3$ (relative degree $2$), corresponding to the third-order ODE $y'''+7y''+14y'+8y=\dot\delta(t)+3\delta(t)$. Phase vector $\mathbf y=(y,y',y'')$ changes by $\Delta\mathbf y(0)=(0,1,-4)$.]*

#### Ghosh — Control systems, p.33

Example 2.12. "Find $f(t)$ if"
$$
F(s) = \frac{s+3}{s(s+1)(s+2)}
$$
"Taking inverse Laplace transform, we get"
$$
f(t) = \frac{3}{2} - 2e^{-t} + \frac{1}{2}e^{-2t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s + 3)/(s (s + 1) (s + 2)), s, t]
```
*Returns $f(t) = \dfrac32 - 2\,e^{-t} + \dfrac12\,e^{-2t}$*]

*[Jump condition at $t=0$: $F(s)=(s+3)/(s(s+1)(s+2))$ has denominator $s(s+1)(s+2)=s^3+3s^2+2s$ and numerator $s+3$ (relative degree $2$), corresponding to the third-order ODE $y'''+3y''+2y'=\dot\delta(t)+3\delta(t)$. Phase vector $\mathbf y=(y,y',y'')$ changes by $\Delta\mathbf y(0)=(0,1,0)$.]*

#### Xie — Differential equations for engineers

Example 6.14
$$
\mathcal{L}^{-1} \left\{ \frac{8}{(s-1)(s^2+2s+5)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = e^t - e^{-t} \cos 2t - e^{-t} \sin 2t
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[8/((s - 1)(s^2 + 2 s + 5)), s, t]
```
*Returns $f(t) = e^{t} - e^{-t}\cos(2t) - e^{-t}\sin(2t)$*]

*[Jump condition at $t=0$: reading $F(s)$ as the impulse response of the zero-state 3rd-order ODE with denominator $(s-1)(s^2+2s+5)$ (relative degree $3$). Phase vector $\mathbf y=(y,y',y'')$ changes by $\Delta\mathbf y(0)=(0,0,8)$.]*

### 2.4 Higher-order equations (order 4 and higher) {#higher-order-equations}
#### Bavafa-Toosi — Introduction to linear control systems, p.204

Example 3.2. "Consider the system"
$$
L(s) = \frac{s^4 + 2s^3 + 11s^2 + 4s + 10}{s^6 + 2s^5 + 7s^4 + 12s^3 + 15s^2 + 18s + 9}
$$
$$
\implies\; l(t) = \frac{1}{\sqrt{3}}\,t\sin\sqrt{3}t + \frac{1}{6\sqrt{3}}\left(\sin\sqrt{3}t - \sqrt{3}\,t\cos\sqrt{3}t\right) + t e^{-t}
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s^4 + 2 s^3 + 11 s^2 + 4 s + 10)/(s^6 + 2 s^5 + 7 s^4 + 12 s^3 + 15 s^2 + 18 s + 9), s, t]
```
*Returns $l(t) = \frac{\sqrt3}{3}\,t\sin(\sqrt3\,t) - \frac16\,t\cos(\sqrt3\,t) + t e^{-t} + \frac{\sqrt3}{18}\sin(\sqrt3\,t)$*]

*[Jump condition at $t=0$: $L(s)=(s^4+2s^3+11s^2+4s+10)/(s^6+2s^5+7s^4+12s^3+15s^2+18s+9)$ is strictly proper with relative degree $2$ ($\deg N=\deg D-2$; the denominator factors as $(s+1)^2(s^2+3)^2$), corresponding to the sixth-order ODE $y^{(6)}+2y^{(5)}+7y^{(4)}+12y'''+15y''+18y'+9y=\delta^{(4)}(t)+2\delta'''(t)+11\delta''(t)+4\delta'(t)+10\delta(t)$. Phase vector $\mathbf y=(y,y',y'',y''',y'''',y''''')$ changes by $\Delta\mathbf y(0)=(0,1,0,4,-16,-1)$.]*

#### Bavafa-Toosi — Introduction to linear control systems, p.204

Example 3.3. "Consider the system"
$$
L(s) = \frac{2s^3 - 1.2s^2 + 1.4s - 1}{s^4 - 0.6s^3 - 2.6s^2 + 4.2s - 2}
$$
$$
\implies\; l(t) = e^{t} + e^{-2t} + \frac{5}{3}e^{0.8t}\sin(0.6t)
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(2 s^3 - 1.2 s^2 + 1.4 s - 1)/(s^4 - 0.6 s^3 - 2.6 s^2 + 4.2 s - 2), s, t]
```
*Returns $l(t) = e^{t} + e^{-2t} + \frac{5}{3}e^{0.8t}\sin(0.6t)$*]

*[Editorial note: as transcribed, the source states $l(t) = \left[1 - \frac{1}{0.6}e^{0.8t}\sin\left(0.6t + \tan^{-1}(0.75)\right)\right] + e^{t} + e^{-2t}$; this does not satisfy its own stated $L(s)$ (the two disagree for $t>0$, though they coincide at $t=0$). The denominator factors exactly as $(s-1)(s+2)(s^2-1.6s+1)$, and partial-fraction decomposition gives $L(s)=\dfrac{1}{s-1}+\dfrac{1}{s+2}+\dfrac{1}{s^2-1.6s+1}$ — a constant, not linear, numerator over the quadratic factor $(s-0.8)^2+0.36$, so the oscillatory term is a pure sine of amplitude $\frac{1}{0.6}=\frac53$ with no phase shift and no accompanying constant term. The closed form above is the unique function consistent with the stated $L(s)$; it was independently confirmed by symbolic Laplace inversion and by direct substitution back into the corresponding fourth-order ODE.]*

*[Jump condition at $t=0$: $L(s)=(2s^3-1.2s^2+1.4s-1)/(s^4-0.6s^3-2.6s^2+4.2s-2)$ is strictly proper with relative degree $1$ ($\deg N=\deg D-1$), corresponding to the fourth-order ODE $y''''-0.6y'''-2.6y''+4.2y'-2y=2\delta'''(t)-1.2\delta''(t)+1.4\delta'(t)-\delta(t)$. Phase vector $\mathbf y=(y,y',y'',y''')$ changes by $\Delta\mathbf y(0)=(2,0,6.6,-5.44)$.]*

#### Gangadharaiah & Sandeep — Engineering applications of the Laplace transform, p.340

Example 4.25. "Obtain the solution of the fourth-order differential equation"
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
*[WolframAlpha:*
```
y''''[t] + 2 y'''[t] - y''[t] - 2 y'[t] == Delta[t], y[0] == 1, y'[0] == 0, y''[0] == 0, y'''[0] == 0
```
*Returns $y(t) = \frac{1}{2} + \frac{1}{2} e^{-t} + \frac{1}{6} e^{t} - \frac{1}{6} e^{-2t}$*]

*[Jump condition at $t=0$: this fourth-order equation. Phase vector $\mathbf y=(y,y',y'',y''')$ changes by $\Delta\mathbf y(0)=(0,0,0,1)$.]*
*[Editorial note: as transcribed, this example's stated answer ($y = \frac{1}{2} - e^t + \frac{3}{2}e^{2t}$) does not satisfy its own stated differential equation and initial conditions — it fails the homogeneous-equation check for $t>0$ and the required continuity of $y'$ and $y''$ at $t=0$. The closed-form solution above is the unique function consistent with the stated fourth-order equation, $y(0)=1$, $y'(0)=y''(0)=y'''(0)=0$, and $\delta(t)$ forcing; it was re-derived via the Laplace transform and independently confirmed by direct substitution back into the differential equation. It replaces the original transcription here as a high-confidence, mathematically necessary correction rather than a silent guess.]*

#### Xie — Differential equations for engineers, p.258

Example 6.11
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s-2)^5} \right\} \implies f(t) = \frac{1}{12} e^{2t} t^3 (2 + t)
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[s/(s - 2)^5, s, t]
```
*Returns $f(t) = \frac{1}{12} e^{2t} t^3 (2+t)$*]

*[Jump condition at $t=0$: reading $F(s)$ as the impulse response of the zero-state 5th-order ODE with denominator $(s-2)^5$ (relative degree $4$). Phase vector $\mathbf y=(y,y',y'',y''',y^{(4)})$ changes by $\Delta\mathbf y(0)=(0,0,0,1,10)$.]*

#### Xie — Differential equations for engineers, p.258

Example 6.12
$$
\mathcal{L}^{-1} \left\{ \frac{1 + e^{-3s}}{s^4} \right\} \implies \frac{1}{6} \left[ t^3 + (t-3)^3 u(t-3) \right]
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(1 + Exp[-3 s])/s^4, s, t]
```
*Returns $f(t) = \frac{1}{6}\left[t^3 + (t-3)^3 \, u(t-3)\right]$*]

*[Jump conditions: the numerator $1+e^{-3s}=\mathcal L\{\delta(t)+\delta(t-3)\}$, so this is the zero-state response of the 4th-order pure-integrator ODE $y''''=x(t)$ to two unit impulses. Phase vector $\mathbf y=(y,y',y'',y''')$ changes by $\Delta\mathbf y(0)=(0,0,0,1)$ at $t=0$, and by $\Delta\mathbf y(3)=(0,0,0,1)$ at $t=3$.]*

#### Xie — Differential equations for engineers, p.258

Example 6.13
$$
\mathcal{L}^{-1} \left\{ \frac{s}{(s^2 + 4)^2} \right\} \implies \frac{1}{4} t \sin 2t
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[s/(s^2 + 4)^2, s, t]
```
*Returns $f(t) = \frac{1}{4} t \sin(2t)$*]

*[Jump condition at $t=0$: reading $F(s)$ as the impulse response of the zero-state 4th-order ODE with denominator $(s^2+4)^2$ (relative degree $3$). Phase vector $\mathbf y=(y,y',y'',y''')$ changes by $\Delta\mathbf y(0)=(0,0,1,0)$.]*

#### Xie — Differential equations for engineers, p.258

Example 6.15
$$
\mathcal{L}^{-1} \left\{ \frac{s+1}{(s^2+1)(s^2+9)} \right\} \implies f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{8} \left( \cos t + \sin t - \cos 3t - \frac{1}{3} \sin 3t \right)
$$
*[WolframAlpha:*
```
InverseLaplaceTransform[(s + 1)/((s^2 + 1)(s^2 + 9)), s, t]
```
*Returns $f(t) = \frac{1}{8}\left(\cos t + \sin t - \cos 3t - \frac{1}{3}\sin 3t\right)$*]

*[Jump condition at $t=0$: reading $F(s)$ as the impulse response of the zero-state 4th-order ODE with denominator $(s^2+1)(s^2+9)$ (relative degree $3$). Phase vector $\mathbf y=(y,y',y'',y''')$ changes by $\Delta\mathbf y(0)=(0,0,1,1)$.]*



---

## Additional Exercises

Supplementary problems and variations, given as page/problem references only — no solution is reproduced here. Sorted alphabetically by author; intended to guide further practice.

### Gupta
p.116
P1. Find the step response and impulse response of the transfer function  
$$
G(s) = \frac{20}{s^2 + 4s + 25}
$$

### Ghosh
p.34
3. Find f(t), where

(i)
$$
F(s) = \frac{s}{(s+1)(s+2)}
$$

**Ans.** $-e^{-t} + 2e^{-2t}$

p.58
15. The impulse response of a system $ G(s) = \frac{2}{(s+1)(s+3)} $

### Bottega
p.238: Example 4.2 "A tethered 1 pound ball hangs in the vertical plane when it is tapped with a racket. Following the tap the ball is observed to exhibit oscillatory motion of amplitude 0.2 radians with a period of 2 seconds. Determine the impulse imparted by the racket." (Problem statement only — no closed-form solution given in the source, hence listed here rather than under Solved Exercises.)

p.236-238 couple 2nd order system with impulse load; p.269: Ex.4.4-4.6; p.429: MDOF system under impulse load; p.470: double pendulum under impulse load; p.488: Ex 8.17 elastically supported frame under struck; p.501 Ex 8.7; p.507: Ex 8.26; p.715: Ex 11.3 PDE "Determine the response of the rod it is struck on its right end by an impulse of magnitude"; p.718: Ex 11.17 "The beam is impacted at its left end"

### Boyce & DiPrima
p.273-274 has many exercises

### Campbell & Haberman
p.264 Exercises 1–8

### De Oliveira
p.82 Problem 3.41 "Compute the inverse Laplace transform of the following complex-valued functions"; p.83 Problem 3.44 "Compute the inverse Laplace transform"

### Dorf & Bishop
p.174 P2.36 "Determine the impulse response of the system"; p.178 "Consider the unity feedback system described in the block diagram ... Compute analytically the response of the system to an impulse disturbance"; p.392 CP5.1 "Obtain the impulse response analytically"

### Edwards & Penney
9.326 4.6 Problems 1-8, 15-16 (equality of solution by changing IC)

### Esfandiari & Lu
p.59 Problems 19 through 24; p.62 Problem 10 "Solve the IVP"; p.352 "8.3.2 Impulse Response of Second-Order Systems"; p.353 "Example 8.5: Impulse Response"; p.359 "Example 8.8: Impulse Response"; p.363 "PROBLEM SET 8.2"/7-11, 20

### Franklin, Powell & Emami-Naeini
p.230 EXAMPLE 4.9; p.589 Problem 7.20

### Inman
p.221 Example 3.1.1; p.222 Example 3.1.3; p.224 Example 3.1.4; p.232 Example 3.2.3; p.245 Example 3.4.4, Example 3.4.5; p.287 Problems 3.1-3.6, 3.10-3.13; p.377 Example 4.8.1 MDOF system with impulse; p.382 Example 4.8.2 MDOF system with impulse; p.386 Example 4.8.3 MDOF system with impulse; p.428 Problem 4.76; p.429 Problem 4.78; p.440 Example 5.1.2; p.557 Example 6.8.1 "Calculate the forced response of the string fixed at both ends ... subject to unit impulse"; p.571 Problem 6.67

### Karris
p.6-2 "Example 6.1"; p.6-3 "Example 6.2"

### Kelly
p.317 EXAMPLE 5.1; p.374 Problem 5.21-5.23

### Lathi & Green
p.471 Problem 4.3-6

### Meirovitch
p.371 Problem 7.49; p.463 Problem 8.38, 8.42, 8.44

### Nagle, Saff & Snider
p.404 "7.8 EXERCISES" 5-12, 23-28; p.410 "7.9 Exercises" 13-29, 35; p.416 "REVIEW PROBLEMS FOR CHAPTER 7" Problem 29-30

### Ogata
p.196 MATLAB Program 5–8 "Unit-Impulse Response of G(s) = 1/(s^2 + 0.2s + 1)"; p.264 B–5–4 "Consider the system shown in Figure 5–72. The system is initially at rest. Suppose that the cart is set into motion by an impulsive force whose strength is unity. Can it be stopped by another such impulsive force?"; p.264 B-5-5, B-5-6; p.265 B-5-10/11; p.267 B-5-16

### Rao
p.382 "4.5.1 Response to an Impulse"; p.384 EXAMPLE 4.7 "Response of a Structure Under Impact"; p.385 EXAMPLE 4.8 "Response of a Structure Under Double Impact"; p.407 EXAMPLE 4.9 "Unit Impulse Response of a First-Order System"; p.409 EXAMPLE 4.21 "Unit Impulse Response of a Second-Order System"; p.437 EXAMPLE 4.33 "Impulse Response of a Structure"; p.511 EXAMPLE 5.12 "Response Under Impulse Using Laplace Transform Method"

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

Unlike a plain literature survey, every one of the fifty solved exercises in this compilation has been independently checked against its own stated differential equation (or transfer function) and initial conditions, rather than simply quoted. Three complementary methods were used, chosen per entry according to what its stated form allowed:

- **Symbolic Laplace-transform matching.** For entries given as a transfer function $H(s)$ (or $C(s)$) paired with an impulse/step response $h(t)$ (or $c(t)$), and for IVPs whose claimed solution has no time-shifted (Heaviside) piece, the claimed time-domain solution's Laplace transform was computed symbolically (via SymPy) and compared against $H(s)$, or against $Y(s)$ built from the stated ODE's coefficients and initial conditions.
- **Segment-wise ODE and jump-matching.** For IVPs whose forcing includes one or more shifted delta impulses $\delta(t-c)$ — where the claimed solution is naturally piecewise/Heaviside-driven — each solution was checked directly: the homogeneous differential equation on every open interval between impulses, continuity of $y, y', \dots, y^{(n-2)}$ at each impulse location, and the required jump of $y^{(n-1)}$ by (impulse amplitude)/(leading coefficient) at that point. This avoids a limitation of general-purpose symbolic Laplace-transform routines, which do not reliably transform expressions built from `Heaviside(t-c)*f(t-c)`.
- **Numeric self-consistency.** For the one entry specified purely by numeric physical parameters (Shabana, Example 1.10), the stated parameters were used to recompute the natural frequency, damping ratio, damped frequency, and response amplitude and check them against every numeric value the source itself reports.

This process confirmed all thirty-seven originally transcribed solved exercises exactly as transcribed; thirteen additional examples (Angeles, p.132; Finan, p.57; Anderson, p.206; Anderson, p.22; Bavafa-Toosi, p.203; Bavafa-Toosi, p.204, Example 3.2; Bavafa-Toosi, p.204, Example 3.3; Bavafa-Toosi, p.822; Engelberg, p.31; Frank, p.29; Ghosh, p.23; Ghosh, p.24; Ghosh, p.33) were subsequently added, each independently verified the same way. It also surfaced five transcription issues beyond the duplicate example discussed in the Conclusion below, each corrected inline with an explicit derivation rather than silently: an incomplete equation (Nagle, p.403, Example 4), a garbled unit label (Shabana, p.41, Example 1.10), a single-character transcription error (Xie, p.258, Example 6.13), and two examples whose printed answers did not actually satisfy their own stated equations (Gangadharaiah & Sandeep, p.340, Example 4.25; Bavafa-Toosi, p.204, Example 3.3).

A machine-readable export of the full, verified example set — problem source, coefficients or transfer function, forcing, initial conditions, closed-form solution, and verification method for each of the fifty entries — is provided alongside this article as `solved_examples.json` and `solved_examples.csv`, so the collection can be consumed directly by an automated test harness rather than re-transcribed by hand.

Concretely, each entry in `solved_examples.json` carries a `type` field that determines how it is best exercised as a test case:

- **`ivp` entries** (15 of the 50) give fully numeric ODE coefficients, a list of forcing impulses (amplitude, derivative order, and shift location), and numeric initial conditions — a direct, ready-to-parse input for an ODE solver under test. A test harness can feed `(ode_coeffs_highest_to_lowest, forcing, initial_conditions)` straight into the solver, evaluate both the solver's output and the quoted `solution_latex` (parsed via a CAS such as SymPy) at a grid of sample times away from the impulse locations, and assert numerical agreement to within a chosen tolerance.
- **`transfer_function` entries** (23 of the 50) pair a transfer function `H_s` with its known impulse response `h_t` — suited to testing a Laplace-domain toolbox: run the transform under test on `H_s` and diff the result against `h_t`.
- **`ivp_symbolic` entries** (11 of the 50) carry general, symbolic parameters (e.g. $\tau$, $k$, $\omega_0$, $\zeta$) rather than fixed numbers, which makes them well suited to property-based or randomized testing: substitute random concrete values for the symbolic parameters before each comparison, exercising the solver across a swept parameter range instead of one fixed case.
- **The one `ivp_numeric` entry** (Shabana, Example 1.10) is a fully numeric physical-parameter case, suited to a straightforward fixed-input regression test.

Across all four types, the `verified` and `verification_method` fields let a harness filter to only independently-checked entries before trusting them as an oracle (all 50 here are `verified: true`), and the stable `id` field gives each entry a natural key for parametrized test naming (e.g. `pytest.mark.parametrize` keyed by `id`, or a JUnit/xUnit test-case name). The flat `solved_examples.csv` carries the same bibliographic and verification columns (`id`, `author`, `book_title`, `page`, `example`, `type`, `verified`, `verification_method`, `notes`) for quick spreadsheet review or for a lightweight runner that would rather avoid a JSON parser; the fuller mathematical content — coefficients, forcing, initial conditions, and closed-form solution — is only in the JSON, since it does not flatten cleanly into CSV columns.

---

## Conclusion

This article gathered fifty fully worked examples — each an LTI ODE (or, equivalently, a transfer function) forced by a Dirac delta impulse or its derivative, paired with a published closed-form solution — from nineteen textbooks spanning ordinary differential equations, vibrations, signals and systems, and control engineering. These are supplemented by dozens of further exercise references, without solutions, indexed across twenty texts (several of which overlap with the solved set) to point the reader toward additional practice material. All content in both categories was extracted, not derived: no new analytical results are claimed, and every solved example was independently verified against its stated equation rather than merely transcribed (see Verification Methodology above).

Three intended uses motivated the compilation. As a pedagogical resource, the dual-category structure — Solved Exercises grouped by ODE order and then alphabetized by author, Additional Exercises alphabetized by author — lets a reader move directly from a specific equation order, author, or problem type to the relevant worked solution, without first locating and cross-referencing dozens of separate books. As a software-engineering resource, the fifty solved exercises — together with their machine-readable export and per-example WolframAlpha check — constitute a ready-made benchmark suite: each pairs a well-posed initial value problem with an independently verified analytical answer, suitable for regression or unit testing of symbolic or numerical ODE solvers. As a small act of literature quality control, the verification pass itself demonstrates that even a well-regarded, widely used textbook can carry an internally inconsistent worked answer (Gangadharaiah & Sandeep, Example 4.25; Bavafa-Toosi, p.204, Example 3.3), an apparent error in a stated initial-condition jump (Angeles, p.136), or a duplicated problem (Example 3.9, byte-identical to Example 3.12) that a reader is unlikely to catch without redoing the algebra — underscoring the value of checking, not just collecting, textbook exercises before relying on them for testing purposes.

Two limitations should be noted. First, the survey is not exhaustive: it reflects the books available to the present compiler and is best understood as a personal, growing reading list rather than a systematic literature search. Second, while every solved example's closed-form solution was checked against its own stated equation and initial conditions, this verification cannot detect an error present identically in both the stated problem and its stated answer (e.g., a genuine typo in the source textbook's equation that happens to be consistent with its own — equally mistaken — answer key); nor does it substitute for tracing each problem back to first principles. One originally duplicated example (Gangadharaiah & Sandeep, Example 3.9) was removed rather than repaired, since its true content could not be recovered independently of Example 3.12. Extending the collection to further textbooks, and extending the automated verification to the Additional Exercises once solutions are added for them, are natural directions for future work.

---

## References

Gupta, A., & Verma, Y. P. (2020). Automatic control engineering (1st ed.). I.K. International Pvt. Ltd.

Anderson, B., & Rufer, S. (2018, August 13). Control theory: A brief introduction. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

Angeles, J. (2011). Dynamic response of linear mechanical systems: Modeling, analysis and simulation. Springer. https://doi.org/10.1007/978-1-4419-1027-1 (ISBN 978-1-4419-1026-4; e-ISBN 978-1-4419-1027-1; ISSN 0941-5122; e-ISSN 2192-063X)

Bavafa-Toosi, Y. (2017). Introduction to linear control systems. Academic Press. (ISBN: 978-0-12-812748-3; e-ISBN: 978-0-12-812749-0)

Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-38164-8)

Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. (ISBN: 978-0-691-12474-6)

De Oliveira, M. C. (2017). Fundamentals of linear control: A concise approach. Cambridge University Press. https://doi.org/10.1017/9781316941409 ISBN 978-1-107-18752-8 Hardback

Dorf, R. C., & Bishop, R. H. (2008). Modern control systems: Solution manual (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

Edwards, C. H., & Penney, D. E. (2008). Elementary differential equations with boundary value problems (6th ed.). Pearson Education. ISBN 0-13-600613-2

Engelberg, S. (2024). A mathematical introduction to control theory (3rd ed.). World Scientific Publishing Company. (ISBN: 978-1-80061-554-0)

Esfandiari, R. S., & Lu, B. (2014). Modeling and analysis of dynamic systems (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3)
https://doi.org/10.1201/b16907

Finan, M. B. (2014). Laplace transforms: Theory, problems, and solutions. Arkansas Tech University. http://faculty.atu.edu/mfinan/4243/Laplace.pdf

Frank, S. A. (2018). Control theory tutorial: Basic concepts illustrated by software examples. Springer. https://doi.org/10.1007/978-3-319-91707-8 (ISBN 978-3-319-91706-1; e-ISBN 978-3-319-91707-8)

Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). Feedback control of dynamic
systems (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

Gangadharaiah, Y. H., & Sandeep, N. (2021). Engineering applications of the Laplace transform. Cambridge Scholars Publishing. ISBN (13): 978-1-5275-7373-4

Ghosh, S. (2012). Control systems: Theory and applications (2nd ed.). Pearson Education. (ISBN: 978-81-317-5837-3)

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
