# Brogliato: Nonsmooth Mechanics - Models, Dynamics and Control (3rd Ed.)

## Reference
**Book**: Nonsmooth Mechanics: Models, Dynamics and Control, Third Edition  
**Author**: Bernard Brogliato  
**Publisher**: Springer (2016)  
**Key Chapter**: Chapter 1 - "Impulsive Dynamics and Measure Differential Equations"  
**Key Pages**: 1-36 (Introduction to impulsive forces and problem formulation)

---

## CENTRAL EQUIVALENCE: Impulsive Forces ↔ Velocity Jumps with Continuous Position

### Fundamental Proposition 1.1 (Pages 260-264)

**Proposition 1.1**: "Assume the mass is submitted to an impulsive force at t = tₖ. Then there is a discontinuity σẋ(tₖ) in the velocity ẋ(·) at the time tₖ while the position x(·) remains continuous. **Conversely if the velocity is discontinuous at t = tₖ and the position is continuous, then there is an impulsive force at t = tₖ, and the acceleration is a Dirac measure.**"

This is the **mathematical expression of the equivalence** the user seeks.

### Mathematical Formulation

#### Example 1.1: Single Mass with Impulsive Force (Pages 147-250)

**Mechanical System:**
```
Mass m subjected to impulsive force pk·δtk

mẍ = pkδtk        (1.2) - equality of distributions
```

where:
- δtk is the Dirac measure at time tₖ
- pk is the impulse magnitude
- ẍ is the acceleration (a priori a singular distribution)

#### Distributional Derivatives

The **key step** is recognizing that position and velocity derivatives must be expressed as distributions:

```
ẋ = {ẋ} + σx(tₖ)δtk                      (1.3a)

ẍ = {ẍ} + σx(tₖ)δ̇tₖ + σ{ẋ}(tₖ)δtₖ       (1.3b)
```

Where:
- {ẋ} = classical derivative (ignoring discontinuities)
- σx(tₖ) = x(tₖ⁺) - x(tₖ⁻) = position jump
- σ{ẋ}(tₖ) = {ẋ}(tₖ⁺) - {ẋ}(tₖ⁻) = velocity jump
- δtk = Dirac measure at tₖ
- δ̇tₖ = derivative of Dirac measure (singular, not a measure)

#### Resolution via Distribution Theory

Substituting (1.3) into (1.2):

```
m{ẍ} = pkδtk - mσx(tₖ)δ̇tₖ - mσ{ẋ}(tₖ)δtₖ    (1.4)
```

**On interval [t₀, tₖ)**: m{ẍ} has support in [t₀, tₖ) (smooth dynamics)  
**At t = tₖ**: RHS has support at tₖ (impulsive term)

Since these must equal as distributions, and distributions with different supports must both be zero:

```
m{ẍ} = 0
pkδtk - mσ{ẋ}(tₖ)δtk + mσxδ̇tₖ = 0
```

From the second equation, using test functions φ ∈ D:

```
(pkδtk - mσ{ẋ}(tₖ)δtk, φ) + (mσxδ̇tₖ, φ) = 0
```

Taking derivatives: pk - mσ{ẋ}(tₖ) = 0 and mσx(tₖ) = 0

**Therefore:**

```
σx(tₖ) = 0                          Position is CONTINUOUS
σ{ẋ}(tₖ) = pk/m                     Velocity JUMPS by pk/m
{ẍ} = 0 almost everywhere           
ẍ = (pk/m)δtₖ                       Acceleration is Dirac measure
```

**This proves the equivalence!**

### Complete Solution

**For t < tₖ:**
```
ẋ = ẋ₀  (constant)
x = ẋ₀·t + x₀
```

**For t ≥ tₖ:**
```
ẋ = ẋ₀ + pk/m  (jumped by pk/m)
x = (ẋ₀ + pk/m)·t - (pk/m)·tₖ + x₀
```

**Key Result**: The continuous position and jumped velocity are the **necessary and sufficient** conditions for the impulsive force to exist.

---

## MATHEMATICAL FRAMEWORK: Measure Differential Equations (MDEs)

### Definition 1.3-1.4: MDE Solutions

**MDE Form (Equation 1.15):**
```
Dx = f(t,x) + G(t)Du           x(t₀) = x₀
```

Where:
- D = distributional differentiation operator
- u(t) = bounded variation (BV) input
- G(t) = time-continuous matrix
- Du = differential measure (Stieltjes measure)

**Equivalent Integral Equation (1.16):**
```
x(t) = x₀ + ∫ᵗt₀ f(s,x(s))ds + ∫(t₀,t] G(s)du(s)
```

**Solution Definition (Definition 1.3):**
- x(·) is a bounded variation n-vector
- x(t) is continuous from the right
- (t, x(t)) satisfies the dynamics
- x(t₀) = x₀

### Theorem 1.1: Equivalence of Formulations

The solution of the differential equation form **equals** the solution of the integral equation form (extension of Carathéodory theory).

### Jump Characterization: Proposition 1.3 (Pages 836-884)

For systems of the form:
```
dx = f(x)dt + g(x)du           x(0) = x₀     (1.23)
```

**At discontinuity times {tₖ} of du:**

```
x(tₖ⁺) = ΦG(1; x(tₖ⁻), u(tₖ⁺) - u(tₖ⁻))      (1.25)
```

Where ΦG(s; z₀, v) is the solution of the auxiliary ODE:
```
ż(t) = Σⱼ vʲgⱼ(z(t))    z(0) = z₀
```

evaluated at time s = 1.

**Interpretation:**
- x(tₖ⁻) = state **before** the discontinuity
- u(tₖ⁺) - u(tₖ⁻) = **magnitude of input jump**
- x(tₖ⁺) = state **after** the discontinuity
- The map ΦG encodes how the system **responds** to the input jump

### Example 1.1 Continued: Scalar System

For system dx = 0·dt + x·du (f=0, g(x)=x):

If u jumps by amount c at time t₁:
```
x(t₁⁺) = (1 + c)·x(t₁⁻)
```

The state jumps by factor (1+c), proportional to the input jump.

---

## Extension to Lagrangian Mechanical Systems

### Example 1.3: Rigid Body with Impulsive Forces

**System:**
```
q̇ = velocity
M(q)q̈ + C(q,q̇)q̇ + g(q) = u + J(q)ᵀλ

When subjected to impulsive force λ = pkδtₖ:
```

**Distribution equation yields:**
```
q(tₖ⁺) - q(tₖ⁻) = 0              Position continuous
M(q)(q̇(tₖ⁺) - q̇(tₖ⁻)) = J(q)ᵀpk    Velocity jumps
```

**Result:**
```
Δq̇ = M(q)⁻¹J(q)ᵀpk    (velocity jump as function of impulse)
```

### Example 1.4: Flexible Joint Manipulator

System with elastic joints driven by impulsive input shows:
```
- q̇₂ is DISCONTINUOUS at impact times (velocity jumps)
- q₂ is continuous but piecewise differentiable (position smooth)
- q̇₁ remains continuous throughout
- q₁ remains continuously twice differentiable
```

This demonstrates the **hierarchy of regularity** created by impulses.

---

## Key Concepts: Carathéodory Measure Systems (CMS)

### Definition 1.5: Conditions for Well-Posedness

An MDE is a **Carathéodory Measure System** if:
1. f(t,x) is measurable in t for each fixed x
2. f(t,x) is locally Lipschitz continuous in x (constant K)
3. |f(t,x)| ≤ r(t) (bounded by summable function)
4. ||G(s)du|| < b on the interval

### Theorem 1.2: Existence & Uniqueness

For every point (t₀, x₀) in domain S, there exists a **unique solution** ϕ(t, t₀, x₀) of the MDE on a maximal open interval containing t₀.

**Key insight**: Unlike classical ODEs, solutions exist outside the initial domain S because state jumps can take x outside initially specified domains.

---

## Critical Difference from Smooth Differential Equations

### Discontinuity in Initial Time

Unlike ordinary Carathéodory ODEs, MDE solutions are:
- **NOT continuous** with respect to initial time t₀
- **Of bounded variation** in t₀
- Depend on whether the initial time is before, at, or after impulse times

**Example (page 652-668)**: For equation Dx = x + δ₀:
```
Starting at t₁ < 0: ϕ(t; t₁, 1) = exp(t - t₁) for t < 0
                                  = (exp(-t₁) + 1)exp(t) for t > 0

Starting at t₂ > 0: ϕ(t; t₂, 1) = exp(t - t₂) for t ≥ 0
                    (NOT affected by impulse at t=0)
```

At t = 0:
```
ϕ(0; t₁, 1) - ϕ(0; t₂, 1) → 1  (jump equals input impulse magnitude)
```

This shows the **fundamentally different structure** of impulsive systems.

---

## Physical Interpretation: Nonsmooth Mechanics

### Section 1.1: Impulsive Forces in Mechanics

**Definition 1.1 & 1.2**: Distinction between:
- **Regular force** F(t): density w.r.t. Lebesgue measure
- **Contact percussion** pₖδtₖ: atom of impulse measure at impact

**Key Quote (pages 91-98):**
> "Impulsive mechanics involves only measures (Dirac 'functions'), and no distribution of higher degree. Impact between two bodies is a phenomenon of very short duration that implies a sudden change in the bodies' dynamics (fast velocity variation)."

### Why Dirac Measures Are Necessary

For impulse to be nonzero as Δt → 0, force F must be infinite (concentrated on zero-measure set):

```
pk = lim[Δt→0] ∫[tₖ,tₖ+Δt] F(τ)dτ

As Δt → 0:
- Integration interval → zero Lebesgue measure
- For nonzero integral, F must → ∞
- This is precisely a Dirac measure distribution
```

**Brogliato states (page 140-143):**
> "It is worth noting that this is not just one way to represent the impulsive force... but this is the only formulation of such a phenomenon that is mathematically correct: 'Mathematical distributions provide a correct mathematical definition of distributions encountered in physics.'"

---

## Summary: The Complete Equivalence Framework

### Discontinuous Right-Hand Side Problem

**Standard Smooth System:**
```
ẋ = f(t,x)     x(t₀) = x₀
(continuous RHS, smooth solution)
```

**System with Impulsive Input (Discontinuous RHS):**
```
Dx = f(t,x) + G(t)·δtₖ     x(t₀) = x₀
(RHS contains Dirac delta - discontinuous/singular)
```

### Equivalent Free Vibration Problem

**Between impulses (t ∉ {t₁, t₂, ...}):**
```
ẋ = f(t,x)     (standard, continuous RHS)
```

**At each impulse time tₖ:**
```
x(tₖ⁺) = ΦG(1; x(tₖ⁻), Δu)    (jump in state)
```

### The Bridge Between Formulations

**Proposition 1.3** provides the exact state jump map via the auxiliary flow ΦG, which:
1. Operates on the input jump magnitude Δu = u(tₖ⁺) - u(tₖ⁻)
2. Uses the input coupling g(x) from the system
3. Computes the resulting state change over "unit pseudo-time"

**Result**: The complete system response is fully characterized by:
- Smooth dynamics between jumps
- State jump maps at impulse times
- Joint evolution law (measure differential equation)

---

## Relevance to Differential Equations with Discontinuous Right-Hand Sides

**HIGHLY RELEVANT** - Brogliato provides:

✓ **Rigorous mathematical treatment** of discontinuous right-hand sides via distribution theory  
✓ **Complete characterization** of impulsive systems (Chapter 1)  
✓ **Explicit state jump formulas** (Proposition 1.3, Jump Characterization)  
✓ **Existence & uniqueness theorems** for nonsmooth systems (Theorems 1.2, Carathéodory Measure Systems)  
✓ **Practical examples** showing discontinuous RHS ↔ velocity jumps equivalence  
✓ **Control engineering applications** (impacts, unilateral constraints, robotics)  
✓ **Bridge to Filippov differential inclusions** (mentioned in preface, developed in later chapters)

**This book is THE reference for mathematically rigorous treatment of nonsmooth mechanical systems with discontinuous right-hand sides.**

---

## Connection to Other Works in Collection

**Brogliato's Framework Relates To:**
- **Benchohra**: Both use measure theory; Benchohra focuses on existence/uniqueness proofs via fixed points; Brogliato focuses on mechanical applications
- **d'Andréa-Novel**: Brogliato's state jumps (Proposition 1.3) implement what d'Andréa-Novel's impulse response h(t) = CeᵗᴬB describes in transfer function form
- **Babitsky**: Brogliato's framework formalizes the jump conditions in Babitsky's vibro-impact systems

**Unified Perspective:**
- **d'Andréa-Novel**: Input-output (frequency domain) view of impulse response
- **Brogliato**: State-space (time domain) view of measure differential equations
- **Benchohra**: Theoretical (fixed-point) view of impulsive systems
- **Babitsky**: Applied (vibro-mechanics) view of impact dynamics

All are mathematically equivalent, just different perspectives.
