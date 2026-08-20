# Dishliev & Dishlieva: Specific Asymptotic Properties of Solutions of Impulsive Differential Equations

## Reference
**Book**: Specific Asymptotic Properties of the Solutions of Impulsive Differential Equations. Methods and Applications  
**Authors**: Angel Dishliev¹, Katya Dishlieva², Svetoslav Nenov¹,³  
**Institutions**: 
- ¹Department of Mathematics, University of Chemical Technology and Metallurgy, Sofia, Bulgaria  
- ²Faculty of Applied Mathematics and Informatics, Technical University of Sofia, Bulgaria  
**Publisher**: Academic Publications, Ltd.  
**Date**: 2012 (309 pages)  
**Dedication**: To Professor D. Bainov (pioneer of impulsive DE theory)

---

## CENTRAL MISSION: Qualitative Theory of Impulsive Systems

### The Book Philosophy

**Goal**: Develop qualitative theory (continuous dependence, stability, differentiability) specifically for impulsive differential equations:

1. **Asymptotic behavior** — How solutions evolve over time
2. **Continuous dependence** — Sensitivity to initial conditions and impulsive parameters
3. **Stability analysis** — Long-term behavior and robustness
4. **Variable impulse moments** — When impulses occur dynamically (state-dependent)
5. **Applications** — Population dynamics, pharmacokinetics, ecology, control

**Key insight**: Classical results for continuous DE's don't directly apply to systems with discontinuous jumps—new theory required.

---

## DEFINING IMPULSIVE DIFFERENTIAL EQUATIONS

### Three-Part Structure (Equations 0.1–0.3)

**Complete impulsive system consists of:**

**Part 1: Differential equation (smooth evolution)**
```
dx/dt = f(t, x)    (0.1)

Describes the differentiable parts of solution between impulses
Function f continuous in (t, x)
```

**Part 2: Impulsive moment condition (when impulses occur)**
```
g(t, x(t)) = 0    (0.2)

Determines moments t_imp when impulses take place
Function g continuous in extended phase space
Cases:
- Fixed moments: t_imp = t₁, t₂, t₃, ... (predetermined)
- Hypersurface crossing: Integral curve meets predefined surfaces
- Variable moments: State-dependent, dynamically determined
```

**Part 3: Impulsive jump function (what happens at impulse)**
```
x(t_imp + 0) = I(x(t_imp⁻))    (0.3)

Defines magnitude and direction of instantaneous state change
Function I continuous in phase space
x(t_imp⁻) = value just before impulse (left-limit)
x(t_imp + 0) = value just after impulse (right-limit)
```

### Solution Structure

**Solutions are piecewise continuous functions:**
```
x(t) is differentiable except at impulse moments t_imp
At t_imp: x has jump discontinuity (first-type)
Convention: x is left-continuous at impulse moments
           x(t_imp⁻) = lim x(t) as t → t_imp from left
           x(t_imp + 0) = I(x(t_imp⁻))  (computed by jump function)
```

---

## KEY TECHNICAL CHALLENGES

### Specific Difficulties in Impulsive DE Theory (Intro, pp. xiii–xv)

Dishliev identifies 9 phenomena unique to impulsive systems:

#### 1. **Discontinuity of Solutions**
```
Solutions have jump discontinuities at impulse moments
Size of jump determined by I(x(t_imp⁻))
Not differentiable at t_imp, but continuous from left
Makes classical existence/uniqueness results inapplicable
```

#### 2. **"Beating" Phenomenon** (Critical)
```
Integral curve meets impulsive set repeatedly
Possibly infinitely many impulses occur in finite time
Impulsive moments have a compression point
Solution may "die" (not continuable to right)

Example: Zeno's paradox—sequence of impulses accumulate
t_imp → T as the system undergoes infinite impulses in finite time

Makes asymptotic analysis extremely difficult
```

#### 3. **Loss of Autonomous Property**
```
Even if equation is autonomous (no explicit time dependence):
ẋ = f(x),  g(x) = 0

The impulsive moments depend on solution x(t), which is time-dependent
Therefore moments t_imp = t_imp(t₀, x₀) depend on initial condition
Result: Solution is NOT autonomous even if RHS is

Consequence: Classical autonomous system theory doesn't apply
```

#### 4. **Fusion of Solutions**
```
Two different solutions may converge at impulse moment
After impulse, they follow same trajectory
Solutions "merge" after jumping to same state
```

#### 5. **Impulsive Moments Change with Initial Condition**
```
Different initial conditions → different impulse sequences
One solution may have no impulses, another many
Even small perturbation Δx₀ changes when (and if) impulses occur

Classical continuous dependence (small Δx₀ → small solution difference)
is NOT guaranteed for impulsive systems
```

#### 6. **Changing Impulsive Moments Under Perturbation**
```
Perturbations of system parameters change impulse sequence:
- Modified RHS changes when solution hits impulsive surface
- Changed parameters change timing
- Changed impulse function I changes jump magnitude

Perturbed solution may have different number of impulses
```

#### 7. **Accumulation of Errors**
```
Perturbations and inaccuracies "accumulate" at each impulse
After many impulses, error may grow unboundedly
For infinite impulse sequences, errors may become insuperable
Leads to qualitatively different behavior despite small perturbations
```

#### 8. **Proximity Near Impulse Moments**
```
Two "nearby" solutions may have impulses at different times
At moment when solution 1 has impulse, solution 2 may not
Cannot expect proximity between solutions near impulse times
Solutions can diverge significantly despite starting close together
```

#### 9. **Coupling of Impulsive Effects and Parameters**
```
All aspects interact:
- Moment of impulse depends on system parameters AND initial condition
- Jump size depends on state at impulse moment
- Future trajectory depends on post-impulse state
Complex coupling makes analysis difficult
```

---

## MATHEMATICAL FRAMEWORK

### Chapter 1: Fixed Moments of Impulses

**System form:**
```
dx/dt = f(t, x),           t ≠ tₖ
x(tₖ + 0) = Iₖ(x(tₖ⁻))    k = 1, 2, 3, ...
x(t₀) = x₀
```

**Where:**
- Moments t₁, t₂, ... are predetermined (fixed in advance)
- f: RHS of ODE between impulses
- Iₖ: Impulse function at k-th impulse
- Solution is piecewise smooth

**Key Theorems (Chapter 1):**

1. **Continuous Dependence on Initial Condition**
   - Sufficient conditions ensuring small Δx₀ → small Δx(t) for all t
   - Uses comparison functions and Lyapunov methods

2. **Continuous Dependence on Impulsive Moments**
   - When perturbations in tₖ values cause bounded solution changes
   - Requires conditions on impulse function derivatives

3. **Stability of Solutions**
   - Lyapunov stability: Does solution remain near equilibrium?
   - Applied to pharmacokinetic model

### Chapter 2: Differentiability of Solutions

**Problem**: How do solutions change if we perturb:
- Initial condition x₀
- Impulsive effects (the jump functions Iₖ)

**Main Results:**
```
∂x/∂x₀ = sensitivity of solution to initial condition
∂x/∂(impulse effect) = sensitivity to jump magnitude

Both computed via variational equations
```

**Application**: Logistic model with fixed impulses

### Chapter 3: Variable Impulse Moments on Hypersurfaces

**System form (generalization):**
```
dx/dt = f(t, x),           between impulses
g(t, x(t)) = 0             determines impulse moment
x(t_imp + 0) = I(x(t_imp⁻))  jump at impulse

Hypersurface Σ = {(t, x) : g(t, x) = 0}
Integral curve meets Σ → impulse occurs
```

**Key Innovation**: Non-intersecting hypersurfaces
```
Hypersurfaces Σ₁, Σ₂, ... do not cross each other
This prevents infinite impulses in finite time ("beating")
Makes analysis tractable
```

**Main Results:**

1. **Absence of Beating**
   - Sufficient conditions ensuring finite number of impulses in any bounded time
   - Non-intersecting hypersurfaces + condition on vector field direction

2. **Continuous Dependence on Hypersurfaces**
   - Perturbations in position/shape of Σₖ cause bounded solution changes
   - Critical for robustness under model uncertainty

3. **Uniform Stability**
   - Zero solution is uniformly stable despite perturbations
   - Uniform across initial conditions and impulsive perturbations

**Application**: General mathematical models from ecology, pharmacokinetics

### Chapter 4: Variable Impulsive Moments on Barrier Curves

**System form:**
```
dx/dt = f(t, x)
x(t_imp + 0) = I(x(t_imp⁻))
Impulse occurs when x(t) crosses predefined curve (barrier)
```

**Differs from Chapter 3**: Curves instead of hypersurfaces (different dimension/structure)

**Main Results:**
- Continuous dependence on position of barrier curves
- Continuous dependence on initial condition

**Application**: Impulsive Gompertz model (population dynamics)

---

## AUTONOMOUS SYSTEMS WITH NON-FIXED IMPULSES (Chapters 5–6)

### Chapter 5: Orbital Hausdorff Continuous Dependence

**System form:**
```
dx/dt = f(x)                    (autonomous—no explicit time)
x(t_imp + 0) = I(x(t_imp⁻))    
Impulse set M ⊂ Rⁿ (phase space, not extended space)
Impulse occurs when x(t) ∈ M
```

**New Concept: Orbital Hausdorff Continuous Dependence**
```
Not just: solution x(t) is close to x̃(t)
But: trajectory {x(t)} is geometrically close to {x̃(t)}
    (up to reparametrization in time)

Hausdorff distance measures "gap" between curves:
dₕ(Orbit₁, Orbit₂) = max{ max d(p₁,Orbit₂), max d(p₂,Orbit₁) }
                           p₁∈C₁        p₂∈C₂

Allows trajectories to be "out of phase" in time but geometrically close
```

**Why this matters:**
- For autonomous systems, exact timing of impulse is less important
- Geometric similarity of trajectory is more meaningful
- Handles case where different initial conditions hit impulse set at different times

**Application**: Lotka-Volterra predator-prey model with impulses

### Chapter 6: Orbital Hausdorff Stability

**New Concept: Orbital Hausdorff Stability**
```
Classical Lyapunov stability: x(t) → equilibrium
Orbital stability: Trajectory geometrically approaches equilibrium
                  (not necessarily with same timing)

"Zero solution is orbitally Hausdorff stable if trajectories 
starting near equilibrium stay geometrically near equilibrium"
```

**Applications:**
- Lotka-Volterra model without impulses (baseline)
- Harmonic oscillator with impulses

---

## OPTIMIZATION AND CONTROL (Chapter 7)

### Impulsive Controllability

**Problem**: Can we steer system to desired state using impulsive controls?

**Three Problems:**
1. **Minimize reproduction time** — Population dynamics with harvesting impulses
2. **Optimal regime of external effects** — When and how much to apply impulses
3. **Lagrange optimization** — Minimize cost functional subject to impulsive dynamics

**Main Result**: 
- Necessary conditions (Lagrange method) for optimal impulse strategy
- Applied to population dynamics optimization

---

## VARIABLE STRUCTURE WITH NON-FIXED MOMENTS (Chapter 8)

### Switched Systems with Impulses

**System form:**
```
dx/dt = fᵢ(t, x)    when in mode i
Mode switches at state-dependent times
Additional impulses at each mode switch

Generalization combining:
- Time-varying RHS (different modes)
- Variable moment impulses (state-dependent switching)
```

**Challenge**: Interaction between continuous switches and discrete impulses

---

## CONNECTION TO DISCONTINUOUS RHS

### How Dishliev's Framework Relates to Discontinuous Right-Hand Sides

| Aspect | Dishliev's Formulation | Discontinuous RHS Form |
|--------|----------------------|------------------------|
| **Smooth part** | dx/dt = f(t,x) | Smooth RHS |
| **Discontinuity** | Jump x(t⁻) → x(t⁺) | Dirac delta in RHS |
| **When occurs** | At predetermined t_k or when g=0 | Automatically via δ(t) |
| **Jump function** | I(x) defines new state | Implicit in convolution |
| **Solution structure** | Piecewise smooth | Piecewise smooth (via integral) |

### Mathematical Equivalence

**Dishliev's impulsive system:**
```
dx/dt = f(t, x),  t ≠ tₖ
x(tₖ⁺) = I(x(tₖ⁻))
```

**Can be written as discontinuous RHS:**
```
dx/dt = f(t, x) + Σₖ [I(x(tₖ⁻)) - x(tₖ⁻)] δ(t - tₖ)

Right-hand side is:
- f(t, x): smooth part
- Σₖ [...] δ(t - tₖ): singular part (Dirac deltas at impulse times)
```

**Key insight from Dishliev:**
- Impulsive formulation makes the **jump function I explicit**
- Discontinuous RHS approach **implicitly encodes the same behavior**
- Both are mathematically equivalent

---

## FOUNDATIONAL THEOREMS USED

### Theorem 0.1: Classical Continuous Dependence (Base Case)

**For smooth ODE ẋ = f(t, x):**
```
If f is continuous and Lipschitz in x, then
- Solution exists and is unique
- Solution continuously depends on initial condition x₀
  (small Δx₀ → small Δx(t))
```

**Limitation**: Does NOT apply directly to impulsive systems due to discontinuities.

**Dishliev's Contribution**: Reformulates and extends this theorem for impulsive systems under appropriate conditions.

### Theorem 0.2: Grönwall Inequality

**Standard result:**
```
If v(t) ≤ C + ∫ₜ₀ᵗ u(τ)v(τ) dτ

Then v(t) ≤ C·exp(∫ₜ₀ᵗ u(τ) dτ)
```

**Usage in impulsive systems**: Bounds solution growth when perturbations accumulate

**Application to beating phenomenon**:
- If u(t) is unbounded (happens during infinite impulses), v(t) can grow unboundedly
- This explains why "beating" causes loss of continuous dependence

---

## COMPARISON TO OTHER FRAMEWORKS

### Dishliev vs. Nine Previous Papers

| Paper | Method | Focuses On | Dishliev Relationship |
|-------|--------|-----------|----------------------|
| **Camporesi** | Elementary IC | Impulse response | Uses simpler fixed-moment case |
| **Chen** | State-space | Continuous evolution | Uses when between impulses |
| **Brogliato** | Measure theory | Nonsmooth mechanics | Uses measure formulation |
| **Dahleh** | Numerical e^(At) | Engineering tools | Computational method |
| **Datta** | Algorithms | Implementation | Numerical approach |
| **Cooper** | Distribution theory | Math foundations | Rigorous basis |
| **d'Andréa-Novel** | Transfer functions | Frequency domain | Uses for hybrid systems |
| **Chalishajar** | Generalized functions | Beam mechanics | Specialized application |
| **Chicurel-Uziel** | Parametrization | Nonlinear | Extends to nonlinear |
| **Dishliev** | Qualitative theory | Asymptotic behavior | **Comprehensive theory for all cases** |

---

## KEY INNOVATIONS IN DISHLIEV

### 1. Explicit Treatment of Variable Impulse Moments

**Before Dishliev**: Most work assumed fixed moments (simplest case).

**Dishliev's contribution**: Fully develops theory for:
- Hypersurface crossings (common in applications)
- Barrier curves (population dynamics models)
- State-dependent moments (real-world systems)

### 2. Beating Phenomenon Analysis

**Recognition**: System can undergo infinite impulses in finite time.

**Solution**: Sufficient conditions ensuring "no beating"
- Non-intersecting hypersurfaces
- Vector field direction relative to hypersurfaces

**Impact**: Makes analysis possible for previously intractable systems.

### 3. Orbital Hausdorff Continuous Dependence

**Innovation**: For autonomous systems, trajectory geometry matters more than exact timing.

**Practical value**: Allows robust analysis when precise impulse timing is unknown.

### 4. Comprehensive Applications

Each chapter ends with applied example:
- Pharmacokinetics (drug dosing with periodic administration)
- Population dynamics (Logistic, Gompertz, Lotka-Volterra with harvesting)
- Ecological models
- Control optimization

---

## WHY DISHLIEV IS CRITICAL

### Position in Discontinuous ODE Hierarchy

**Dishliev occupies unique position:**

1. **Most comprehensive theory** for impulsive DE's with variable moments
2. **Only source** treating beating phenomenon systematically
3. **Connects theory to applications** (not just abstract math)
4. **Handles all three continuous dependence problems**:
   - On initial condition x₀
   - On impulsive moments tₖ
   - On impulse function I

### Relevance to Discontinuous RHS

While other frameworks use different formulations (distributions, parametrization, state-space), **Dishliev addresses the actual qualitative issues** that arise with discontinuities:

- What happens to solution behavior under perturbations?
- When does continuous dependence break down?
- How do infinite impulses affect stability?
- Can we control systems with impulsive effects?

These are **fundamental questions** for any discontinuous system.

---

## EXAMPLE: Pharmacokinetic Model (Chapter 1, Application)

### The Problem

Drug administration in body modeled as:
```
dx/dt = -ax + ḡ(t)    (elimination between doses)
x(tₖ⁺) = x(tₖ⁻) + dₖ   (absorption at dosing moments)

where:
x(t) = drug concentration
a = elimination rate
dₖ = dose at time tₖ
```

### Classical vs. Impulsive Formulation

**Classical (ignoring absorption impulse):**
```
dx/dt = -ax + ḡ(t) + Σₖ dₖ δ(t - tₖ)

Uses distributions (Dirac delta)
```

**Dishliev's formulation:**
```
dx/dt = -ax
x(tₖ⁺) = x(tₖ⁻) + dₖ

Explicit jump function I(x) = x + dₖ
```

### Key Question

**If dose amounts {dₖ} or timing {tₖ} change slightly, does concentration profile change only slightly?**

**Answer from Dishliev**: Yes, IF conditions on:
- Elimination rate a
- Dose schedule spacing
- Initial condition

are satisfied. Otherwise, continuous dependence fails.

**Practical implication**: Robust dosing schedule requires understanding these conditions.

---

## COMPLETE HIERARCHY: All Eleven Frameworks

| # | Paper/Book | Level | Approach | Best For |
|---|-----------|-------|----------|----------|
| 1 | **Camporesi (1)** | Elementary | Initial conditions | Intuition |
| 2 | **Camporesi (2)** | Elementary | Factorization | Variable coeff |
| 3 | **Chen** | Classical | State-space | Discrete/continuous |
| 4 | **d'Andréa-Novel** | Classical | Transfer functions | Frequency domain |
| 5 | **Brogliato** | Rigorous | Measures | Nonsmooth mech |
| 6 | **Chalishajar** | Applied | Generalized functions | Beam equations |
| 7 | **Chicurel-Uziel** | Novel | Parametrization | Nonlinear |
| 8 | **Cooper** | Foundation | Distribution theory | Math rigor |
| 9 | **Dahleh** | Practice | Systems theory | Engineering tools |
| 10 | **Datta** | Computation | Numerical algorithms | Implementation |
| 11 | **Dishliev** | Qualitative | Impulsive theory | Asymptotic behavior |

**The complete picture:**

```
Cooper (Rigorous distributions)
   ↓
Classical & Engineering (Chen, d'Andréa-Novel, Dahleh)
   ↓
Numerical Implementation (Datta)
   ↓
Impulsive-Specific Theory (Dishliev) ← NEW LEVEL
   ↓
Extensions (Chalishajar, Chicurel-Uziel)
   ↓
Advanced applications (Control, optimization, population dynamics)
```

---

## SUMMARY

**Dishliev's contribution is essential** because it addresses **what happens at the discontinuities** in a mathematically rigorous way:

✓ **Formulates impulsive DE's rigorously** — three-part structure  
✓ **Identifies unique challenges** — beating, loss of autonomy, accumulation of errors  
✓ **Develops sufficient conditions** — when continuous dependence holds despite discontinuities  
✓ **Handles variable impulse moments** — not just fixed times  
✓ **Introduces orbital stability** — geometry matters for autonomous systems  
✓ **Applies to real problems** — pharmacokinetics, ecology, control  
✓ **Bridges theory and practice** — makes theory usable for engineers  

**Why all frameworks are needed:**

- **Cooper**: Why distributions work
- **Chen/Dahleh/Datta**: How to compute
- **Brogliato**: Mechanical applications
- **Dishliev**: What to expect asymptotically
- **Chicurel-Uziel**: How to extend to nonlinear
- **Chalishajar**: How to apply to specialized problems

Dishliev provides the **qualitative theory** essential for understanding systems with discontinuous right-hand sides over long time intervals.
