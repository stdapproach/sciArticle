# Hallauer: Introduction to Linear, Time-Invariant, Dynamic Systems for Students of Engineering

## Reference
**Book**: Introduction to Linear, Time-Invariant, Dynamic Systems for Students of Engineering  
**Author**: William L. Hallauer Jr., Department of Aerospace and Ocean Engineering, Virginia Polytechnic Institute  
**Publisher**: Self-published (Creative Commons License), Virginia Tech  
**Date**: 2016  
**Pages**: ~600+  
**Scope**: Comprehensive undergraduate-to-graduate level treatment of LTI systems with explicit chapters on impulses, Dirac delta functions, impulse response, and control fundamentals

---

## CENTRAL MISSION: Complete LTI Systems Education with Explicit Discontinuity Treatment

### The Textbook Philosophy

**Goal**: Comprehensive treatment of linear time-invariant system fundamentals for engineering students:

1. **Foundation** (Chapters 1-4) — LTI systems, ODEs, complex numbers, Laplace transforms
2. **First-Order Systems** (Chapters 3-6) — Transient response, frequency response, convolution
3. **Undamped Second-Order** (Chapter 7) — Undamped vibration, natural frequency
4. **Impulses and Discontinuities** (Chapter 8) — **EXPLICIT TREATMENT**
5. **Damped Second-Order** (Chapters 9-10) — Damping, resonance, identification
6. **Multi-DOF Systems** (Chapters 11-12) — Rigid body rotation, vibration modes
7. **Control Systems** (Chapters 13-17) — Feedback, PID, stability analysis
8. **Applications** — Mechanical, electrical, aerospace examples throughout

**Target audience**: Undergraduate and graduate engineering students (junior level and above), with emphasis on aerospace engineering applications.

**Unique aspect**: **Explicit mathematical treatment of discontinuities through impulses and Dirac delta function.**

---

## CHAPTER 8: PULSE INPUTS, DIRAC DELTA FUNCTION, IMPULSE RESPONSE

### The Problem with Pulse Inputs

**Why Chapter 8 is essential:**

```
Real systems experience discontinuous disturbances:
- Hammer strike (force pulse)
- Sudden gust in aircraft wing
- Collision (impulse-momentum)
- Step load application

Classical methods (integration) work for smooth inputs
But what about idealized instantaneous impulse?

Standard ODE methods can't directly handle δ(t)
Need special theory for discontinuous inputs
```

### Section 8-1: Flat Pulse

**Practical discontinuity:**
```
Real pulse:  Defined over duration td
             Force = F for 0 ≤ t ≤ td
             Force = 0 otherwise
             Graphically: rectangular pulse

Questions:
1. How does system respond during pulse?
2. What if td → 0 (pulse becomes instantaneous)?
3. What is limiting behavior as td → 0?
```

### Section 8-2: Impulse-Momentum Theorem

**Bridge from physics to mathematics:**
```
Impulse-momentum theorem (from mechanics):
  ∫ F(t) dt = m·Δv  (over impulse duration)
  
Physical meaning:
  Integrating force over time = change in momentum
  Instantaneous change in velocity is possible!

For system: m·v̇ + c·v = f(t)

If impulse: ∫ f(t) dt = F_imp (impulse magnitude)
Then:       Δv = F_imp / m  (instantaneous)
```

**Critical insight for discontinuities:**
```
A discontinuous jump in velocity is POSSIBLE
via impulsive force acting on mass

This is different from classical smooth evolution!
Discontinuity can be rigorously justified via impulse
```

### Section 8-3-8-4: Dirac Delta Function

**Mathematical idealization:**
```
Dirac delta function δ(t):
  δ(t) = 0,  t ≠ 0
  δ(t) = ∞,  t = 0  (infinite peak)
  ∫₋∞^∞ δ(t) dt = 1  (area = 1)

Graphical representation:
  Impulse at t=0 with area 1
  Infinitely tall, infinitesimally wide
  ↑
  |
  |_____  (area under curve = 1)
  
Time-shifted version:
  δ(t - t₀) = impulse at t = t₀
```

**Limit definition (Section 8-4):**
```
δ(t) = lim_{Δ→0} [rectangular pulse of height 1/Δ and width Δ]

As Δ → 0:
  Height → ∞
  Width → 0
  Area = (height) × (width) = (1/Δ) × Δ = 1 (constant!)

This is the mathematical definition of Dirac delta
```

**Physical interpretation:**
```
Instantaneous force impulse:
  f(t) = I₀·δ(t)  where I₀ is impulse magnitude

System response:
  v(0⁺) - v(0⁻) = I₀/m  (instantaneous velocity jump!)
  Position x(t) continuous (velocity jump is ok)
```

### Section 8-5: Ideal Impulse Response of 1st Order System

**Complete solution (Section 8-5):**

For first-order system:
```
ODE:  m·v̇ + c·v = I₀·δ(t)
IC:   v(0⁻) = 0  (at rest before impulse)

Step 1: Find initial condition after impulse
  Integrate ODE from t=0⁻ to t=0⁺:
  m[v(0⁺) - v(0⁻)] + c·∫ v dt = I₀
  
  Since impulse is instantaneous:
  m·v(0⁺) = I₀  ⟹  v(0⁺) = I₀/m

Step 2: Solve ODE for t > 0
  After impulse, force is zero: f(t)=0
  ODE becomes: m·v̇ + c·v = 0
  
  Solution: v(t) = v(0⁺)·e^{-(c/m)t} = (I₀/m)·e^{-(c/m)t}

Complete impulse response:
  v(t) = {  (I₀/m)·e^{-(c/m)t},  t ≥ 0
          {  0,                  t < 0
```

**Graphical behavior:**
```
Response to impulse δ(t):
  
  v(t)
   │     │
   │     ├── (I₀/m)·exp(-(c/m)t)
   │     │
   │     └─ decaying exponential
   │
   └─────────────────── t
         0⁺
   
Instantaneous jump at t=0⁺
Then smooth exponential decay
```

### Section 8-7: Ideal Impulse Response of Undamped 2nd Order System

**Second-order system response:**

```
System: m·ẍ + k·x = I₀·δ(t)

Initial conditions at t=0⁻:
  x(0⁻) = 0  (displacement)
  ẋ(0⁻) = 0  (velocity)

After impulse at t=0:
  Position x still zero (continuous)
  But velocity jumps: ẋ(0⁺) = I₀/m

For t > 0 (no forcing):
  m·ẍ + k·x = 0
  
  Solution (underdamped case):
  x(t) = (I₀/√(km))·sin(ωₙ·t)
  where ωₙ = √(k/m) is natural frequency

Response is pure sinusoidal oscillation!
Amplitude: I₀/√(km)
Frequency: ωₙ
```

**Physical interpretation:**
```
Mass-spring system:
  Impulse imparts velocity I₀/m
  Spring force converts to oscillation
  No damping → perpetual oscillation
  No decay in amplitude!

Impulse response shows natural frequency directly
This is HOW we measure ωₙ experimentally!
Apply impulse, measure oscillation frequency
```

### Section 8-8: Ideal vs. Real Impulse Response

**Critical practical distinction:**

```
Ideal impulse:  δ(t) infinitely tall, infinitesimally narrow
                Velocity jumps instantaneously

Real impulse:   Finite peak, finite duration
                Velocity changes over time
                But result is essentially the same if duration << natural period
```

**Example:**
```
Idealized:  100 N-sec impulse via δ(t)
Real:       100 N force for 0.001 sec = 0.1 N impulse
            
If system natural period is 1 second >> 0.001 sec:
  Ideal and real responses nearly identical
  Can use δ(t) model
  
If system natural period is 0.0005 sec << 0.001 sec:
  Must account for pulse duration
  δ(t) approximation breaks down
```

### Section 8-10: Convolution Integral as Superposition of Impulse Responses

**Fundamental theorem for LTI systems:**

```
General input u(t) decomposed as:
  u(t) = ∫ u(τ)·δ(t - τ) dτ
         -∞
  
  (sum of infinitesimal impulses)

System response by superposition:
  y(t) = ∫ h(τ)·u(t - τ) dτ  ← Convolution integral
         0
  
where h(t) = impulse response

Physical meaning:
  1. Apply infinitesimal impulse u(τ)dτ at time τ
  2. System responds with h(t-τ)·u(τ)dτ
  3. Sum all past impulses (0 to t)
  4. Total output = convolution integral
```

**Why this is revolutionary:**
```
Breakthrough: ANY input can be expressed as
  Superposition of scaled, time-shifted impulses
  
If we know h(t) (impulse response):
  We can calculate response to ANY input!
  
Conversely: 
  Measure system response to impulse
  → Know everything about system (for linear systems)
```

---

## HOW HALLAUER TREATS DISCONTINUITIES

### Three Levels of Treatment

**Level 1: Pulse Inputs (Section 8-1)**
```
Real-world discontinuous disturbances
Rectangular pulse, half-sine pulse
Solution via integration over pulse duration
```

**Level 2: Ideal Impulse (Sections 8-3-8-4)**
```
Dirac delta function δ(t)
Mathematical idealization
Justified by impulse-momentum theorem
```

**Level 3: Convolution (Section 8-10)**
```
Arbitrary input as superposition of impulses
Complete framework for solving with discontinuities
Convolution integral as solution method
```

### Key Equations

**Impulse response:**
```
System: ẏ + a·y = b·f(t)
Impulse input: f(t) = δ(t)

Impulse response: h(t) = b·e^(-at)·u(t)
```

**Convolution integral:**
```
General input u(t), impulse response h(t):

Output: y(t) = ∫₀ᵗ h(τ)·u(t-τ) dτ
```

---

## COMPARISON TO OTHER PEDAGOGICAL TEXTS

| Aspect | Hallauer | Hägglund | Haidekker | Ghosh |
|--------|----------|----------|-----------|-------|
| **Level** | Undergrad/grad | Undergrad | Undergrad/grad | Comprehensive grad |
| **Pages** | ~600+ | ~136 | ~380 | ~800+ |
| **Chapter on impulses** | YES (Ch. 8, extensive) | Brief (Ch. 3.1) | Not explicit | Not explicit |
| **Dirac delta** | Full treatment | Mentioned | Implicit | Not covered |
| **Convolution** | Detailed (8-10) | Brief | Not covered | Detailed |
| **Impulse response** | Core concept | Secondary | Not emphasized | Secondary |
| **Control systems** | Chapters 13-17 | Chapters 1-12 | Chapters 14-17 | All chapters |
| **Aerospace emphasis** | YES (throughout) | NO | NO | NO |

**Hallauer's unique contributions:**
1. **Chapter 8 entirely on impulses** — Most explicit pedagogical treatment found
2. **Impulse-momentum theorem** — Rigorous justification for discontinuities
3. **Dirac delta formalization** — Complete mathematical definition with limit
4. **Convolution integral** — Shows how to handle ANY input via impulses
5. **Aerospace applications** — Aircraft dynamics, spacecraft, aeroelasticity
6. **Free online textbook** — Creative Commons license, accessible to all
7. **MATLAB integration** — Computational methods throughout
8. **Comprehensive scope** — Single volume covers first-order through control systems

---

## COMPLETE TREATMENT OF DISCONTINUITIES

### Section 8-1: Pulse as Model of Reality

**Distinction from impulse:**
```
Pulse: Finite duration, finite amplitude
       u(t) = F,  0 ≤ t ≤ Δt
       u(t) = 0,  otherwise

Example: Half-sine pulse
       u(t) = F·sin(πt/Δt),  0 ≤ t ≤ Δt

Solution method:
  Integrate ODE over pulse duration
  Smooth solution, no discontinuities
```

### Section 8-3-8-4: Ideal Impulse as Limit

**Mathematical rigorous approach:**
```
Step 1: Define rectangular pulse
  p_Δ(t) = 1/Δ,  0 ≤ t ≤ Δ
  p_Δ(t) = 0,    otherwise
  
  Area = (height)×(width) = (1/Δ)×Δ = 1

Step 2: Take limit as Δ → 0
  δ(t) = lim_{Δ→0} p_Δ(t)
  
Result: δ(t) is infinitely tall, infinitesimally narrow
        But area = 1 always

This is RIGOROUS definition!
Not hand-waving or informal approximation
```

### Laplace Transform Connection

**Transform of impulse:**
```
L[δ(t)] = ∫₀^∞ δ(t)·e^(-st) dt = e^(-s·0) = 1

L[t_d·δ(t)] = 1  (impulse with area A_d)

Transfer function approach:
  For impulse input U(s) = 1
  Output Y(s) = G(s)·1 = G(s)
  So: y(t) = h(t) (impulse response IS transfer function in time domain)
```

---

## POSITION IN COMPREHENSIVE FRAMEWORK

**Hallauer's unique role: Comprehensive textbook with explicit impulse treatment**

```
Theoretical Foundations
    ├─ Cooper (Distributions)
    └─ Graef (Multi-valued)
         ↓
Pedagogical Texts with Impulse Treatment
    ├─ Hallauer (Comprehensive, explicit Ch. 8) ← HERE
    ├─ Hägglund (Concise, brief impulse)
    └─ Haidekker (Practical, no explicit impulse chapter)
         ↓
Classical Theory (No Explicit Impulse)
    ├─ Chen, d'Andréa-Novel, Dahleh, Fairman
    ├─ Ghosh (Comprehensive but scattered)
         ↓
Theoretical Specialized
    ├─ Dishliev (Impulsive asymptotic)
    ├─ Brogliato (Measure theory)
         ↓
Large-Scale & Applied
    ├─ Haddad (2×), Chicurel-Uziel
    └─ Falsone, Chalishajar
```

---

## SUMMARY

**Hallauer's contribution is uniquely pedagogical with rigorous impulse treatment** because:

✓ **Entire Chapter 8 on impulses** — Most explicit pedagogical treatment available  
✓ **Impulse-momentum theorem** — Physical justification for discontinuous jumps  
✓ **Dirac delta formalization** — Rigorous limit definition, not hand-waving  
✓ **Impulse response** — Core concept throughout book  
✓ **Convolution integral** — Shows how to solve for ANY input via impulses  
✓ **Practical vs. ideal** — Distinguishes real pulses from mathematical impulses  
✓ **Transfer function connection** — L[δ(t)] = 1 → impulse response IS H(s)  
✓ **Comprehensive scope** — From 1st-order systems through control design  
✓ **Aerospace emphasis** — Aircraft dynamics, spacecraft, aeroelasticity  
✓ **Free and accessible** — Creative Commons, online, no paywall  
✓ **MATLAB integrated** — All examples with computational implementation  

**Why Hallauer matters for discontinuous systems:**

Hallauer provides the **most accessible yet rigorous pedagogical treatment** of discontinuities through impulses available in an undergraduate/graduate textbook:

1. **Chapter 8 is comprehensive** — Not scattered mentions but dedicated treatment
2. **Impulse-momentum theorem** — Rigorous physical justification
3. **Dirac delta** — Complete mathematical definition via limiting process
4. **Convolution integral** — Shows discontinuities are not exotic—they're fundamental
5. **Practical connection** — Real pulses → ideal impulses → limit theory

**Three-tier hierarchy of discontinuity treatment:**

1. **Engineering practice (Haidekker)**: Handle saturation, anti-windup
2. **Pedagogical fundamentals (Hallauer)**: Understand impulses, convolution
3. **Mathematical rigor (Graef, Dishliev)**: Set-valued systems, measure theory

Hallauer bridges layers 1 and 3 via rigorous pedagogy—showing students that discontinuous impulses are not pathological edge cases but **fundamental to understanding ANY system's response via superposition**.

**Critical pedagogical insight:**
Every LTI system's complete behavior can be determined by its impulse response h(t). Any arbitrary input is just a superposition of scaled, time-shifted impulses. This is why understanding discontinuities through Dirac delta is NOT optional—it's **central to systems theory**.
