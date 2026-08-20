# Hägglund: Automatic Control Lecture Notes

## Reference
**Book**: Automatic Control: Lecture Notes  
**Author**: Tore Hägglund, Department of Automatic Control, Lund University  
**Publisher**: Lund University, Faculty of Engineering  
**Date**: 2021 (Copyright 2009)  
**Pages**: ~136  
**Scope**: Pedagogical undergraduate-level treatment emphasizing impulse/step response analysis and transfer functions

---

## CENTRAL MISSION: Transfer Function and Response-Based Control Education

### The Book Philosophy

**Goal**: Provide practical, intuitive education in automatic control using impulse and step response analysis:

1. **Introduction** — PID controller structure and motivation
2. **Process Models** — State-space, linearization, transfer functions
3. **Response Analysis** — Impulse response, step response, pole-response relationships
4. **Frequency Analysis** — Bode plots, frequency response
5. **Feedback and Stability** — Closed-loop analysis, stability concepts
6. **Nyquist Criterion** — Stability margins, practical robustness
7. **Sensitivity Function** — Error tracking, disturbance rejection
8. **State Feedback** — Pole placement, control design
9. **Kalman Filtering** — State estimation from noisy measurements
10. **Output Feedback** — Practical implementation considerations
11. **Lead-Lag Compensation** — Practical controller design
12. **PID Control** — Most common industrial controller
13. **Controller Implementation** — Real-world practical issues
14. **Practical Example** — Ball-on-beam demonstration

**Target audience**: Undergraduate engineering students (electrical, mechanical, control disciplines).

**Approach**: Emphasizes **impulse response as fundamental tool** for understanding system dynamics.

---

## HOW HÄGGLUND TREATS IMPULSES

### Lecture 3: Impulse- and Step Response Analysis

**Central concept: Weighting function h(t)**

**Definition (Section 3.1):**
```
Given state-space system:
  ẋ = Ax + Bu
  y = Cx + Du

Solution (Equation 3.1):
  y(t) = Ce^(At)x(0) + C∫₀ᵗ e^(A(t-τ))Bu(τ)dτ + Du(t)

Three components:
  1. Initial condition response: Ce^(At)x(0)
  2. Forced response: C∫₀ᵗ e^(A(t-τ))Bu(τ)dτ
  3. Direct feedthrough: Du(t)
```

### The Impulse Response (Weighting Function)

**Mathematical definition (Equation 3.2):**
```
For ideal impulse input u(t) = δ(t) with x(0) = 0:

y(t) = C∫₀ᵗ e^(A(t-τ))Bδ(τ)dτ + Dδ(t) = Ce^(At)B + Dδ(t) ≐ h(t)

Impulse response = weighting function h(t)
```

**Why it's called "weighting function":**
```
General output formula (Equation 3.3):
  y(t) = ∫₀ᵗ h(t-τ)u(τ)dτ

Interpretation:
  h(t-τ) tells how much WEIGHT to assign to past input u(τ)
  
Example: If h(t) = e^(-t) and u(τ) = 1 for τ < t:
  Recent inputs (small t-τ) have large weight
  Old inputs (large t-τ) have small weight
  Exponential decay of "memory"
```

**Laplace transform of impulse:**
```
L[δ(t)] = ∫₀^∞ e^(-st)δ(t)dt = 1

Therefore:
  Transfer function = L[impulse response]
  G(s) = Y(s)/U(s) = Y(s)  [when U(s)=1 from impulse]
```

### The Step Response

**Mathematical relationship (Section 3.2, Equation 3.4):**
```
Step input: u(t) = 1 for t ≥ 0

Step response: y_step(t) = ∫₀ᵗ h(τ)dτ

Key insight: Step response IS the integral of impulse response

Physical meaning:
  Impulse = instantaneous disturbance
  Step = sustained change
  Step response = cumulative effect of sustained input
```

**Laplace transform:**
```
L[step] = 1/s

For step input:
  Y(s) = G(s)/s

Using Final Value Theorem (if applicable):
  lim y(t) as t→∞ = lim sY(s) = lim sG(s)/s = G(0) = DC gain
            t→∞        s→0            s→0
```

---

## KEY INNOVATION: Pole-Response Relationship

### Section 3.3: Poles Determine Step Response

**Main theorem (Implicit in Hägglund's approach):**
```
For transfer function G(s) with poles at complex s_i = σ_i + jω_i:

Step response y(t) = Σ A_i e^(σ_i·t) cos(ω_i·t + φ_i) + steady-state

Pole location determines:
  σ_i < 0: Exponentially decaying oscillation (STABLE)
  σ_i = 0: Constant oscillation (MARGINALLY STABLE)
  σ_i > 0: Exponentially growing oscillation (UNSTABLE)
  
  ω_i: Frequency of oscillation
  |σ_i|: Rate of decay/growth
```

**Practical implications:**
```
Real pole at σ:
  Contributes exponential response e^(σt)
  
Complex pole pair at σ ± jω:
  Contributes damped oscillation e^(σt)cos(ωt + φ)
  
Pole at origin (s=0):
  Contributes integrating effect
  Step response → infinite ramp
```

---

## DISCONTINUITIES AND INITIAL CONDITIONS

### Lecture 3: Three Terms in Solution

**From Equation 3.1:**
```
y(t) = Ce^(At)x(0) + C∫₀ᵗ e^(A(t-τ))Bu(τ)dτ + Du(t)
        ︸︷︷︸              ︸︷︷︷︸                    ︸︷︷︸
      initial          forced response         direct term
      condition         (input integral)      (instantaneous)
```

**How discontinuities are handled:**

1. **Discontinuous initial condition (jump at t=0)**
   ```
   y(0⁻) = 0
   y(0⁺) = Ce^0·x(0) = C·x(0) = jump
   
   After jump:
   y(t) = Ce^(At)x(0) + C∫₀ᵗ e^(A(t-τ))Bu(τ)dτ + Du(t)
   
   System "remembers" the jump via initial condition term
   ```

2. **Impulse input (discontinuous right-hand side)**
   ```
   u(t) = δ(t) creates discontinuous ẏ
   But solution y(t) remains continuous (except for direct term D)
   
   y(t) = Ce^(At)B  [continuous for t > 0]
   
   Direct term: Dδ(t) [instantaneous, negligible if D=0]
   ```

3. **Step input (discontinuous input)**
   ```
   u(t) = 1 for t ≥ 0 (discontinuous at t=0)
   
   y(0⁺) = 0 + 0 + D·1 = D [instantaneous jump if D≠0]
   y(t) = ... [smooth rise to steady state for t>0]
   ```

### Lecture 2: Linearization Handles Initial Conditions

**Perturbation approach (Section 2.2):**
```
Nonlinear system around operating point (x₀, u₀):

Introduce perturbations:
  Δx = x - x₀
  Δu = u - u₀
  Δy = y - y₀

Linearized system:
  Δẋ = A·Δx + B·Δu
  Δy = C·Δx + D·Δu

Initial condition change at t=0:
  Δx(0) = x(0) - x₀ = perturbation from operating point
  
Solution automatically includes initial condition response
```

---

## COMPARISON: HÄGGLUND vs. OTHER PEDAGOGICAL TEXTS

| Aspect | Hägglund | Ghosh | Chen | d'Andréa-Novel |
|--------|----------|-------|------|-----------------|
| **Level** | Undergrad, concise | Undergrad-grad, comprehensive | Grad, foundational | Grad, specialized |
| **Focus** | Impulse/step response | All aspects of control | State-space | Transfer functions |
| **Tradition** | European (Lund) | Indian | Chinese-American | French |
| **Impulse treatment** | Via weighting function | Via impulse definition + state-space | Via eigenmodes | Via frequency domain |
| **Pages** | ~136 | ~800+ | Specialized | Specialized |
| **PID emphasis** | Yes (Lecture 12) | Yes (Chapter) | Moderate | Limited |
| **Nonlinear systems** | Brief (Lecture 19) | Yes (Chapter 19) | Limited | Limited |

**Hägglund's unique characteristics:**
- **Concise**: ~136 pages vs 800+ for Ghosh
- **Response-centered**: Emphasizes impulse/step not just transfer functions
- **Industrial PID focus**: Detailed Lecture 12 on practical PID
- **European pedagogy**: Different approach than American/Indian texts
- **Practical implementation**: Lecture 13 on real-world controller design

---

## HANDLING OF KEY CONCEPTS

### 1. Dirac Delta Function

**Definition (Lecture 3, Section 3.1):**
```
Impulse u(t) = δ(t):
  Zero everywhere except t=0
  Infinite magnitude at t=0
  Area = 1

Purpose: Idealized instantaneous disturbance
Example: Object struck suddenly, impact load

Laplace: L[δ(t)] = 1
```

**In transfer function context:**
```
If u(t) = δ(t):
  U(s) = 1
  Y(s) = G(s)
  y(t) = h(t) = impulse response

Shows transfer function IS the impulse response
(when initial conditions are zero)
```

### 2. Initial Conditions

**Via initial state x(0) (Lecture 3, Equation 3.1):**
```
First term: Ce^(At)x(0)
This is EXACTLY the response to initial condition
while input u(t) = 0

Classical control assumption: x(0) = 0
Modern control: x(0) can be nonzero
Hägglund shows both perspectives
```

**Via Laplace with initial conditions (Lecture 2, Section 2.3):**
```
L[ẏ] = sY(s) - y(0⁻)

Initial conditions appear EXPLICITLY in Laplace domain
Must be accounted for in transfer function analysis
```

### 3. Transfer Function Derivation

**From state-space (Lecture 2, Section 2.3):**
```
State-space:
  ẋ = Ax + Bu
  y = Cx + Du

Transform:
  sX(s) = AX(s) + BU(s)
  Y(s) = CX(s) + DU(s)

Eliminate X(s):
  X(s) = (sI - A)⁻¹BU(s)
  G(s) = C(sI - A)⁻¹B + D

Poles = eigenvalues of A
```

---

## BLOCK DIAGRAM MANIPULATION

**Lecture 2, Section 2.4: Feedback Loop Analysis**

**Simple feedback (Figure 2.5):**
```
r --[+]-- e --[GR]-- u --[GP]-- y
     [-]                          |
                                  +--

Equations:
  e = r - y
  u = GR·e
  y = GP·u

Closed-loop transfer function:
  Y/R = (GR·GP)/(1 + GR·GP)

Key insight: Denominator (1 + GR·GP) determines poles
             These poles determine closed-loop step response
```

**Stability condition:**
```
All poles of (1 + GR·GP) must have negative real part
For step input: Final value = G(0) = steady-state gain
```

---

## COMPLETE POSITION IN HIERARCHY

**Hägglund's role: Concise pedagogical alternative to Ghosh**

```
Mathematical Foundations
    ├─ Cooper (Distributions)
    └─ Graef/Henderson/Ouahab (Multi-valued)
         ↓
Classical Theory (Different Pedagogical Approaches)
    ├─ Chen (Foundational state-space)
    ├─ d'Andréa-Novel (Frequency-domain)
    ├─ Dahleh (MIT systems theory course)
    ├─ Fairman (Advanced control design)
    ├─ Ghosh (Comprehensive, 800+ pages)
    └─ Hägglund (Concise, 136 pages) ← HERE
         ↓
Computational Implementation
    ├─ Gear (Automatic detection)
    └─ Datta (Numerical algorithms)
         ↓
Specialized Theory & Applications
    ├─ Dishliev, Brogliato, Graef 2008 (Impulsive)
    ├─ Chicurel-Uziel (Nonlinear)
    └─ Falsone, Chalishajar (Beams)
```

---

## KEY CHAPTERS FOR DISCONTINUITIES

### Lecture 1: PID Controller
```
On/off controller → P controller → PI controller → PID controller

Shows evolution from discontinuous (on/off) to continuous (PID)
On/off is piecewise constant (discontinuous)
PI/PID smooth out by adding integral/derivative action
```

### Lecture 2: Linearization (Section 2.2)
```
Handles nonlinear systems by linearization around operating point
Initial perturbation Δx(0) is handled automatically
Works for systems with discontinuous nonlinearities
```

### Lecture 3: Impulse Response
```
δ(t) represents discontinuity/impulse
Weighting function h(t) shows system's response to it
Fundamental tool for understanding discontinuous inputs
```

### Lecture 13: Controller Implementation
```
Practical issues in implementing controllers
Sampling, quantization, saturation (discontinuous effects)
Anti-windup for integral action (handles discontinuities)
```

---

## SUMMARY

**Hägglund's contribution is uniquely pedagogical** because:

✓ **Concise and practical** — 136 pages vs 800+ for Ghosh  
✓ **Impulse-centered** — Emphasizes weighting function h(t)  
✓ **Response-based analysis** — Step response and impulse response  
✓ **Clear pole-response connection** — How poles shape step response  
✓ **European perspective** — Lund University tradition  
✓ **PID-focused** — Extensive Lecture 12 on practical PID  
✓ **Implementation details** — Lecture 13 on real-world issues  
✓ **Linearization for nonlinearities** — Section 2.2 handles discontinuous systems  

**Why Hägglund matters for discontinuous systems:**

While Hägglund doesn't specifically focus on impulses/discontinuities as research topic, it provides:

1. **Impulse response theory** — Via Dirac delta and weighting functions
2. **Initial condition handling** — Via state-space solution formula
3. **Transfer function perspective** — How impulses appear in frequency domain
4. **Practical PID control** — Most common industrial discontinuous controller
5. **Linearization method** — Handles discontinuous nonlinearities
6. **Clear pole-response link** — Understanding dynamical consequences of impulses

**Hägglund vs. Ghosh:**
- **Ghosh**: Comprehensive (classical + modern + nonlinear + digital)
- **Hägglund**: Focused (impulse/step response + PID + practical implementation)

Both are pedagogical, but Hägglund is **the compact European alternative**—ideal for students who want core concepts quickly without comprehensive breadth. Emphasizes **response analysis over comprehensive theory**.

---

## METHODOLOGICAL UNIQUENESS

**Hägglund's pedagogical innovation:**

1. **Early emphasis on h(t)** — Introduces weighting function immediately after state-space
2. **Response-first approach** — Impulse response before transfer functions
3. **Physical intuition** — "Memory" interpretation of h(t)
4. **Practical controller design** — PID as main example throughout
5. **Connection to implementation** — Lecture 13 bridges theory-practice gap

This makes Hägglund particularly suited for:
- Students wanting quick overview
- Engineers designing practical controllers
- Those emphasizing frequency response and Bode analysis
- Industrial control applications (PID-heavy)

**Not suited for:**
- Detailed mathematical rigor (see Graef)
- Impulsive systems theory (see Dishliev)
- Specialized mechanics (see Falsone)
- Comprehensive modern control (see Ghosh)
