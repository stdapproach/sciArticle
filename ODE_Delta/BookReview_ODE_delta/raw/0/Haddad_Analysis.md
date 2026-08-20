# Haddad, Chellaboina & Hui: Nonnegative and Compartmental Dynamical Systems

## Reference
**Book**: Nonnegative and Compartmental Dynamical Systems  
**Authors**: Wassim M. Haddad (Georgia Tech), VijaySekhar Chellaboina (Nortel Networks/IIIT Hyderabad), Qing Hui (Texas A&M)  
**Publisher**: Princeton University Press  
**Date**: 2010  
**Pages**: ~600  
**Scope**: Comprehensive unified framework for stability, dissipativity, control, and thermodynamics of nonnegative and compartmental systems with applications to medicine, biology, and chemistry

---

## CENTRAL MISSION: Unified Control and Stability Framework for Compartmental Systems

### The Monograph Philosophy

**Goal**: Develop complete mathematical and control framework for systems with inherent nonnegative state constraints and compartmental structure:

1. **Stability Theory** (Chapter 2) — Lyapunov methods for nonnegative systems
2. **Time-Delay Systems** (Chapter 3) — Nonnegative systems with memory
3. **Monotonicity & Nonoscillation** (Chapter 4) — Qualitative solution behavior
4. **Dissipativity Theory** (Chapter 5) — Energy dissipation and conservation laws
5. **Hybrid/Impulsive Systems** (Chapter 6) — Discontinuous jumps in nonnegative systems
6. **System Thermodynamics** (Chapters 7-8) — Compartmental interpretation of thermodynamics
7. **Mass-Action Kinetics** (Chapter 9) — Chemical reaction networks
8. **Equipartition** (Chapter 10) — State convergence to balanced distributions
9. **Robustness** (Chapter 11) — Uncertainty in nonnegative systems
10. **Clinical Pharmacology** (Chapters 12-16) — Drug dosing and anesthesia control
11. **Respiratory Modeling** (Chapter 17) — Lung dynamics and respirator control
12. **System Identification** (Chapter 18) — Reconstructing compartmental structure

**Target audience**: Research mathematicians, control engineers, and applied scientists in pharmacology, biology, chemistry, and medicine.

**Unifying concept**: **Conservation laws** — Mass/energy balance inherent to compartmental structure.

---

## KEY CONCEPT: COMPARTMENTAL SYSTEMS

### Definition and Structure

**Compartmental system:**
```
System where:
1. State variables xᵢ represent quantities (mass, energy, drug concentration)
   in distinct compartments i=1,...,n

2. Flow between compartments:
   dxᵢ/dt = Σⱼ₌₁ⁿ aᵢⱼ(x) xⱼ + uᵢ(t)
   
   where:
   aᵢⱼ(x) = fractional transfer rate from j to i
   uᵢ(t) = external input to compartment i

3. Nonnegative constraint:
   xᵢ(t) ≥ 0 for all t ≥ 0
   (cannot have negative mass/energy)

4. Conservation property:
   Total quantity Σxᵢ changes only via external flows
```

**Physical interpretation (from preface):**
```
Biology:   Compartments = tissues; flows = diffusion of drug
Medicine:  Compartments = body regions; flows = blood circulation
Chemistry: Compartments = chemical species; flows = reaction rates
Ecology:   Compartments = soil/atmosphere; flows = nutrient cycling
Economics: Compartments = market sectors; flows = money exchange
```

---

## CHAPTER 6: HYBRID NONNEGATIVE AND COMPARTMENTAL DYNAMICAL SYSTEMS

### Section 6.5: Linear Impulsive Dynamical Systems

**This is the key chapter on discontinuities!**

**Hybrid system formulation:**
```
Continuous dynamics (between impulses):
  ẋ(t) = Acx(t) + Bcu(t),  t ≠ tₖ, k = 1,2,...

Discrete dynamics (at impulse times):
  x(tₖ⁺) = Adx(tₖ⁻) + Bdu(tₖ),  k = 1,2,...

where:
- Ac is continuous-time system matrix
- Ad is discrete-time (jump) system matrix
- tₖ are impulse times (predetermined or state-dependent)
```

**Nonnegative constraint with impulses:**
```
For compartmental systems, BOTH must preserve nonnegativity:

1. Continuous part: x(t) ≥ 0 between impulses
   Requires: Ac is essentially nonnegative (off-diagonal ≥ 0)

2. Discrete part: x(tₖ⁺) ≥ 0 after each impulse
   Requires: Ad is nonnegative, Adu(tₖ) ≥ 0
   
Critical: Jump cannot violate nonnegativity constraint!
```

**Physical application: Drug dosing**
```
Continuous dynamics:
  dxᵢ/dt = -λᵢxᵢ  (drug elimination)
  
Impulsive dynamics (at tₖ):
  x(tₖ⁺) = x(tₖ⁻) + δₖ  (drug administration)
  
where δₖ ≥ 0 is dose (nonnegative!)

This is exactly the Kruger-Thiemer model from Graef/Ouahab monograph!
```

### Theorem 6.5.1: Stability of Impulsive Nonnegative Systems

**Main result:**
```
For impulsive compartmental system:
  ẋ(t) = Acx(t),  t ≠ tₖ
  x(tₖ⁺) = Adx(tₖ⁻),  k = 1,2,...

with both Ac and Ad nonnegative matrices, if:

1. Ac is Hurwitz (all eigenvalues have Re(λ) < 0)
2. Ad is stochastic (row sums = 1) or substochastic (row sums ≤ 1)
3. Impulses occur at regular intervals or with sufficient separation

Then: System is globally exponentially stable
      x(t) → 0 as t → ∞
      Nonnegativity preserved throughout evolution
```

**Why this is different from general impulsive systems:**
```
General theory (Graef):
  y'(t) - λy(t) ∈ F(t,y(t))
  Jump: y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
  
  Can be any linear/nonlinear functional form

Compartmental theory (Haddad):
  ẋ(t) = Acx(t)
  Jump: x(tₖ⁺) = Adx(tₖ⁻)
  
  CONSTRAINED by:
  - Nonnegativity requirement
  - Conservation of mass/energy
  - Physical interpretation (flows cannot be negative)
```

---

## CHAPTER 2: STABILITY THEORY FOR NONNEGATIVE DYNAMICAL SYSTEMS

### Section 2.1: Lyapunov Theory with Nonnegative Constraints

**Modified Lyapunov approach:**
```
Classical Lyapunov: V(x) > 0, V̇(x) < 0 ⟹ stable

Nonnegative systems modification:
- Cannot use arbitrary V(x)
- Must respect cone structure {x : x ≥ 0}
- V(x) should be compatible with nonnegative dynamics

Use: Linear copositive Lyapunov functions
  V(x) = cᵀx  (linear! not quadratic)
  
where c > 0 vector satisfying:
  cᵀAc ≤ -λc  (exponential convergence)
```

**Key insight: Nonnegative systems require DIFFERENT Lyapunov analysis**
```
For x' = Acx with Ac nonnegative:

Standard quadratic V(x) = xᵀPx doesn't work!
Reason: Nonnegative cone is not ellipsoidal
        Linear V(x) = cᵀx respects cone structure

Stability condition:
  Ac has all eigenvalues with Re(λ) < 0
  ⟺ ∃c > 0: Acᵀc ≤ -λc
```

### Section 2.6: Nonlinear Compartmental Systems

**Nonlinear compartmental model:**
```
ẋᵢ = Σⱼ₌₁ⁿ (aᵢⱼ(x) xⱼ - aⱼᵢ(x) xᵢ) + uᵢ

where:
- aᵢⱼ(x) = state-dependent transfer rate i←j
- aⱼᵢ(x) = state-dependent transfer rate j←i

Conserves total quantity:
  d/dt(Σxᵢ) = Σuᵢ only

Example: Enzyme kinetics
  Substrate S, Enzyme E, Product P
  S + E ⇌ SE → P + E
  
  Transfer rates depend on S, E concentrations
```

### Theorem 2.6.1: Asymptotic Stability of Nonlinear Compartmental Systems

**Result:**
```
For nonlinear compartmental system with:
1. aᵢⱼ(x) ≥ 0 for all i≠j, x ≥ 0
2. aᵢᵢ(x) = -Σⱼ≠ᵢ aⱼᵢ(x) ≤ 0
3. ∃ globally attractive equilibrium x*

Then: x(t) → x* exponentially
      Nonnegativity preserved for all t ≥ 0
      No need for explicit Lyapunov construction
```

---

## CHAPTER 4: NONOSCILLATION AND MONOTONICITY

### Monotonic Solutions

**Definition:**
```
Solution xᵢ(t) is monotonically nondecreasing:
  ∃T : xᵢ(t) is constant for t ≤ T
       xᵢ(t) monotone increasing for t ≥ T

Physical meaning:
  Once substance accumulates in compartment,
  it never decreases (except through outflow)
```

**Theorem 4.2.1: Conditions for Monotonicity**
```
For ẋ = Acx with Ac essentially nonnegative:

Solution xᵢ(t) is monotone increasing iff
  (Ac)ᵢᵢ ≤ 0 (no self-production!)
  (Ac)ᵢⱼ ≥ 0 for j ≠ i (positive inflow)

This is natural! Compartment i can only:
  - Receive from j (positive flow)
  - Send to j (negative diagonal)
```

**Example: Three-compartment system**
```
ẋ₁ = -λ₁x₁ + λ₂₁x₂
ẋ₂ = -λ₂x₂ + λ₁₂x₁
ẋ₃ = λ₂x₂

Matrix form:
  | -λ₁  λ₂₁   0  |
Ac = | λ₁₂  -λ₂   0  |
  |  0   λ₂    0  |

Monotonicity:
  x₁, x₂: Can oscillate (bidirectional flow)
  x₃: Monotone increasing (sink compartment)
```

---

## CHAPTER 7-8: SYSTEM THERMODYNAMICS

### Section 7.2-7.5: Compartmental Systems as Thermodynamic Model

**Unified framework:**
```
Compartmental system:  ẋᵢ = Σ(aᵢⱼxⱼ - aⱼᵢxᵢ)
Thermodynamic system:  dEᵢ/dt = Qᵢ - Wᵢ + Σ flows

Interpretation:
  xᵢ ↔ Energy Eᵢ in compartment i
  aᵢⱼxⱼ ↔ Heat/work flow from j to i
  
Compartmental dynamics is EXACTLY thermodynamic balance!
```

### Section 7.6: Entropy and Irreversibility

**Key theorem (7.6.1): Semistability and Entropy**
```
For compartmental system on nonnegative orthant:

System evolves to equilibrium x* where:
  ∇S(x*) = 0  (entropy extremum)

Entropy function:
  S(x) = Σᵢ [xᵢ ln(xᵢ) - xᵢ]  (Shannon entropy)

Physical meaning:
  System increases entropy until reaching equilibrium
  Irreversibility is consequence of compartmental structure!
  "Entropic arrow of time" follows from dynamics
```

**Semistability vs. Asymptotic Stability:**
```
Asymptotic: x(t) → x* for ALL initial conditions

Semistability: x(t) → x* but x* depends on initial conditions
  (e.g., equilibrium of pendulum at bottom)

For compartmental systems:
  Usually semistable (conserved quantity determines equilibrium)
  
Example: Drug compartments
  Total drug = Σxᵢ = conserved
  Equilibrium x* depends on initial dose distribution
```

---

## CHAPTER 12: CLINICAL PHARMACOLOGY APPLICATION

### Section 12.2-12.4: Pharmacokinetic Models

**Two-compartment model (most common):**
```
Central compartment x₁:
  - Rapid equilibration
  - Drug administration site
  - Concentration measured here

Peripheral compartment x₂:
  - Slower equilibration
  - Tissue distribution
  - Elimination occurs here

Dynamics:
  ẋ₁ = -λ₁₀x₁ - λ₁₂x₁ + λ₂₁x₂ + u(t)
  ẋ₂ = λ₁₂x₁ - λ₂₁x₂
  
  y = x₁/V₁ (concentration measurement)

where:
  λᵢⱼ = rate constant i→j
  u(t) = drug infusion/bolus
```

**Three-compartment model (advanced):**
```
Central (C): Fast elimination, measurement site
Shallow (S): Moderate equilibration, drug distribution
Deep (D): Slow equilibration, long-term storage

Example: Anesthesia
  C = blood (where drug works)
  S = muscle/tissue
  D = fat stores
```

### Section 12.7-12.8: Drug Dosing Control

**Open-loop dosing:**
```
Fixed schedule: u(t) = constant dose every Δt
  Advantage: Simple, no measurement needed
  Disadvantage: Cannot adjust to individual differences
```

**Closed-loop dosing:**
```
Feedback: u(t) = f(C(t) - C_target)
  Measure concentration y = x₁
  Adjust infusion to maintain target level
  
This is EXACTLY an impulsive control problem!
  u(t) = impulse at each dosing time
  Magnitude adjusted based on current concentration
```

### Section 12.10-12.12: Anesthesia Control

**Critical medical application:**
```
State vector:
  x₁ = drug concentration in blood
  x₂ = drug concentration in tissue
  
Measurement:
  y = effect site concentration (estimated from x₁, x₂)
  Or: Bispectral Index (BIS) score from EEG

Control goal:
  Maintain BIS in range [40-60] for safe anesthesia

Challenge:
  Patient-dependent pharmacokinetics
  Impulsive disturbances (surgical stress)
  Measurement noise/delay
```

**Closed-loop anesthesia control:**
```
Traditional: Fixed infusion rate (open-loop)
Modern:      Measure effect → adjust infusion (closed-loop)

Benefits:
  - Reduced overdose/underdose
  - Faster recovery
  - Personalized dosing
  - Improved patient safety
```

---

## CHAPTER 6: HYBRID NONNEGATIVE SYSTEMS (IMPULSIVE)

### Full Hybrid Formulation

**Continuous and discrete dynamics:**
```
Flow (continuous):     ẋ = f(x,u), x ∈ C (flow set)
Jump (discrete):       x⁺ = g(x), x ∈ D (jump set)

For nonnegative compartmental:
  C = {x ≥ 0 : intercompartmental flow feasible}
  D = {(t, x) : impulse time detected}
  
  f(x,u) = Acx + Bu  (nonnegative dynamics)
  g(x) = Adx + w     (nonnegative impulse)
```

### Theorem 6.2.1: Stability of Hybrid Systems

**Global attractivity:**
```
If:
1. f(x,u) is nonnegative, asymptotically stable
2. g(x) = Adx where Ad is nonnegative, rank-one update
3. Impulses satisfy: Ad(x + Bu) ≥ 0

Then: Hybrid system is globally asymptotically stable
      Nonnegativity preserved through jumps
```

**Discrete-time compartmental:**
```
xₖ₊₁ = Adxₖ + Buₖ

Stability condition (Theorem 6.5.2):
  Spectral radius ρ(Ad) ≤ 1 (or < 1 for asymptotic stability)
  Ad nonnegative (row stochastic)
```

---

## CHAPTER 9: MASS-ACTION KINETICS

### Chemical Reaction Networks

**Law of mass action:**
```
For reaction: A + B → C

Rate = k[A][B]
where k is reaction constant, [·] is concentration

Compartmental interpretation:
  xₐ = moles of A
  xᵦ = moles of B
  xᶜ = moles of C
  
  dxₐ/dt = -kxₐxᵦ  (A consumed)
  dxᵦ/dt = -kxₐxᵦ  (B consumed)
  dxᶜ/dt = kxₐxᵦ   (C produced)
```

**Nonlinear compartmental structure:**
```
General chemical system:
  ẋᵢ = Σⱼ (νᵢⱼ - ν'ᵢⱼ) rⱼ
  
where:
  νᵢⱼ = stoichiometric coefficient (reactant)
  ν'ᵢⱼ = stoichiometric coefficient (product)
  rⱼ = reaction rate for reaction j
```

### Zero-Deficiency Theorem (9.8)

**Main result (Horn-Jackson, 1972):**
```
For reaction network with:
  s = number of species
  m = number of reactions
  l = number of connected components

Deficiency δ = m - s - l + 1

If δ = 0 and regular kinetics, then:
  System has unique positive equilibrium
  Every positive trajectory converges to equilibrium
  No oscillations or complex behavior
```

**Application to pharmacokinetics:**
```
Drug metabolism involves chain of reactions:
  Drug → Metabolite₁ → Metabolite₂ → Excretion

Most drug pathways have δ = 0
  → Guaranteed convergence to steady state
  → Predictable pharmacokinetics
```

---

## KEY DISTINCTIONS FROM OTHER FRAMEWORKS

| Framework | Scope | Key Focus | Treatment of Jumps |
|-----------|-------|-----------|-------------------|
| **Graef** | Set-valued, general | Theoretical rigor | Filippov approx, relaxation |
| **Haddad** | Nonnegative, compartmental | Application + theory | Hybrid systems (Ch. 6) |
| **Dishliev** | Impulsive systems | Asymptotic analysis | Specific to impulsive ODE |
| **Gear** | Numerical ODE | Automatic detection | Discontinuity detection |
| **Falsone** | Mechanical systems | Beam bending | Generalized functions |

**Haddad's unique contributions:**
1. **Nonnegative constraint** — Physical requirement (no negative mass)
2. **Compartmental structure** — Conservative flows between compartments
3. **Medical applications** — Drug dosing, anesthesia control
4. **Thermodynamic framework** — Entropy and irreversibility
5. **Hybrid formulation** — Chapter 6 on impulsive systems
6. **Practical control design** — Chapters 12-17 on real applications

---

## COMPLETE FRAMEWORK POSITION

**Haddad's role: Specialized theory + applied control**

```
Mathematical Foundations
    ├─ Cooper (Distributions)
    └─ Graef/Henderson/Ouahab (Multi-valued, general)
         ↓
Classical Theory
    ├─ Chen, d'Andréa-Novel, Dahleh, Fairman
    ├─ Ghosh (Comprehensive)
    └─ Hägglund (Concise)
         ↓
Specialized Theoretical Frameworks
    ├─ Dishliev (Impulsive asymptotic)
    ├─ Brogliato (Measure theory)
    └─ Graef 2008 (Periodic conditions)
         ↓
Applied Specialized Theory + Design
    ├─ Haddad (Nonnegative/compartmental + control) ← HERE
    ├─ Chicurel-Uziel (Nonlinear)
    ├─ Falsone (Beams)
    └─ Chalishajar (Beams)
```

---

## WHY HADDAD MATTERS FOR DISCONTINUOUS SYSTEMS

**Haddad provides:**

1. **Hybrid system theory** (Chapter 6) — Impulsive and compartmental
2. **Nonnegative constraint** — Physical preservation through jumps
3. **Practical applications** — Medical dosing, anesthesia, respirator control
4. **Control design** — Optimal and adaptive control (Chapters 13-16)
5. **Thermodynamic interpretation** — Deep understanding of dissipative systems
6. **System identification** — Reconstructing structure from data (Chapter 18)

**Unique treatment of discontinuities:**
```
Standard theory:   What happens at jump?
Haddad's approach: How to preserve nonnegativity at jump?

Example: Drug dosing
  Before:  x₁(t⁻), x₂(t⁻)
  Impulse: Add δ ≥ 0 dose (must be nonnegative!)
  After:   x₁(t⁺) = x₁(t⁻) + δ ≥ 0  (automatic!)
           x₂(t⁺) = x₂(t⁻)

Jump matrix Ad must be nonnegative
Control input u must respect nonnegativity
```

---

## SUMMARY

**Haddad's contribution is uniquely applied yet rigorous** because:

✓ **Nonnegative constraint** — Physical fundamental, not mathematical convenience  
✓ **Compartmental structure** — Conservation laws built-in  
✓ **Hybrid systems** — Chapter 6 treats impulsive systems  
✓ **Stability theory** — Modified Lyapunov for nonnegative cone  
✓ **Practical applications** — Medical control (anesthesia, drug dosing)  
✓ **Thermodynamic framework** — Entropy and irreversibility from compartmental dynamics  
✓ **Control design** — Optimal, adaptive, and suboptimal methods (Chapters 13-16)  
✓ **System identification** — Reconstructing compartmental structure (Chapter 18)  
✓ **Hybrid formulation** — Preserving nonnegativity through impulses  

**Position in research landscape:**

- **Graef**: Most general/rigorous theoretical framework
- **Haddad**: Most applied to real systems with physical constraints
- **Dishliev**: Deepest asymptotic analysis
- **Gear**: Practical numerical implementation
- **Falsone/Chalishajar**: Mechanical applications

**Bridge between theory and practice:**
Haddad bridges the gap between abstract impulsive system theory (Graef, Dishliev) and practical engineering applications (medical control, pharmacology). The nonnegative constraint is not just mathematical but **fundamental to physical systems**—mass cannot be negative, energy must be conserved.

**Critical innovation:**
Section 6.5 on linear impulsive nonnegative systems shows how hybrid dynamics naturally arise in compartmental systems, with the jump condition preserving the essential constraint that all states remain nonnegative. This is the **missing link** between abstract impulsive ODE theory and practical medical applications like drug dosing and anesthesia control.
