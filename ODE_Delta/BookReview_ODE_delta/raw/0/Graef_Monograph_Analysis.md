# Graef, Henderson & Ouahab: Impulsive Differential Inclusions — A Fixed Point Approach (Monograph)

## Reference
**Book**: Impulsive Differential Inclusions: A Fixed Point Approach  
**Authors**: John R. Graef (University of Tennessee at Chattanooga), Johnny Henderson (Baylor University), Abdelghani Ouahab (Université de Sidi Bel Abbès)  
**Publisher**: De Gruyter Series in Nonlinear Analysis and Applications, Volume 20  
**Date**: 2013  
**Pages**: ~400+  
**Scope**: Comprehensive fixed-point theoretical treatment of impulsive differential inclusions across infinite delays, boundary value problems, semilinear operators, stochastic systems, and neutral equations

---

## CENTRAL MISSION: Unified Fixed-Point Framework for Impulsive Inclusions

### The Monograph Philosophy

**Goal**: Provide complete rigorous mathematical treatment of impulsive differential inclusions across all major problem classes:

1. **Single-delay impulsive FDEs** (Chapter 3) — First order with history dependence
2. **Multiple-delay FDEs** (Chapter 3) — Infinite delay formulations
3. **Boundary value problems on infinite intervals** (Chapter 4) — Asymptotic behavior
4. **Differential inclusions** (Chapter 5) — Filippov's theorem & relaxation
5. **Infinite-delay inclusions** (Chapter 6) — Functional differential inclusions
6. **Variable-time impulses** (Chapter 7) — State-dependent jump times
7. **Neutral inclusions** (Chapter 8) — Neutral-type functional differential inclusions
8. **Solution set topology** (Chapter 9) — Geometric and topological structure
9. **Semilinear problems** (Chapter 10) — Nondensely defined operators, controllability
10. **Stochastic impulses** (Chapter 11) — Random differential equations
11. **Sweeping processes & integral inclusions** (Chapter 11) — Extended applications

**Target audience**: Research mathematicians and advanced graduate students in nonlinear analysis, differential equations, and control theory.

**Unifying method**: **Fixed-point theorems** throughout—replacing classical techniques with topological degree and measure-of-noncompactness (MNC) approaches.

---

## KEY CHAPTERS RELEVANT TO DISCONTINUOUS SYSTEMS

### Chapter 1: Introduction and Motivations

**Physical motivations (Sections 1.2):**

```
Kruger-Thiemer Model (pharmacokinetics):
- Impulses represent drug administration
- x'(t) = -k₁x(t)  [absorption in GI tract]
- y'(t) = -k₂y(t) + k₁x(t)  [distribution in bloodstream]
- Impulses at t₁,t₂,...,tₘ: x(tₖ⁺) = x(tₖ⁻) - δₖ
- Minimize Σ δₖ² subject to therapeutic constraints

Lotka-Volterra with impulses:
- Population dynamics with periodic harvesting
- x'ᵢ = xᵢ(aᵢ + Σ bᵢⱼxⱼ),  t ≠ tₖ
- x(tₖ⁺) - x(tₖ⁻) = I(tₖ, x(tₖ⁻))
- Impulses model pest control, vaccination, culling

Pulse vaccination model:
- SEIR epidemiology with vaccination at fixed times
- Impulses represent vaccination campaigns
- Complex coupling: S, E, I, R with delays and jumps

Integrated pest management:
- State-dependent impulses at economic threshold (ET)
- x(t) = px(t⁻) + I₁(...) when x = ET
- Represents release of natural enemies when pest density reaches threshold
```

**Why these motivations matter:**
```
Each shows:
1. Jumps at predetermined or state-dependent times
2. Jump magnitudes depend on pre-jump state
3. Coupled with continuous evolution
4. All handled within impulsive inclusion framework
```

### Chapter 2: Preliminaries — The Mathematical Toolkit

**Fixed-Point Theorems (Section 2.4):**
```
Core methods replacing classical techniques:

1. Nonlinear Alternative (Theorem 2.4):
   For Fréchet spaces with contraction N:
   EITHER: N has unique fixed point
   OR: ∃ chain extending to boundary

2. Covitz-Nadler Theorem:
   Set-valued γ-Lipschitz contraction (γ < 1)
   ⟹ Fix(G) ≠ ∅

3. Measure of Noncompactness (Section 2.5):
   μ(A) = inf{ε > 0 | ∃ compact A_ε with A ⊂ A_ε + B(0,ε)}
   
   Enables fixed-point results without compactness
   Essential for infinite-delay problems
```

**Set-Valued Topology (Section 2.3):**
```
Vietoris topology, Hausdorff metric, decomposable selection
Three types of continuity:
  - Upper semicontinuity (u.s.c.)
  - Lower semicontinuity (l.s.c.)
  - Hausdorff continuity

Selection theorems (Kuratowski-Ryll-Nardzewski):
  Measurable selection from closed-valued multifunctions
```

**Semigroups (Section 2.6):**
```
C₀-semigroups: {T(t) : t ≥ 0}
Integrated semigroups: S(t) = ∫₀ᵗ T(s)ds

Used for infinite-dimensional problems
Essential for Chapter 10 (semilinear inclusions)
```

---

## CHAPTER 3: FDEs WITH INFINITE DELAY

### Problem Formulation

**First-order impulsive FDE (Equations 1.1–1.3):**
```
y'(t) = f(t, y_t),  a.e. t ∈ J := [0,b], t ≠ tₖ, k=1,...,m
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻)),  k = 1,...,m
y(t) = φ(t),  t ∈ (-∞, 0]

where:
- y_t = {y(t+s) : s ∈ (-∞, 0]} is the "history segment"
- f: J × B → ℝⁿ where B is a Banach phase space
- φ ∈ B represents initial history
```

**Multiple-delay version (Equations 1.4–1.6):**
```
y'(t) = f(t, y_t) + Σ y(t - Tᵢ),  i=1,...,n
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(t) = φ(t),  t ∈ (-∞, 0]

Finite/infinite horizon formulations
```

### Key Innovation: Phase Spaces

**Examples (Section 3.1.1):**
```
Different spaces for different delays:

1. C_r space (bounded history):
   B = {φ: (-∞,0] → ℝⁿ | φ continuous, lim_{t→-∞} φ(t) exists}

2. L² phase space:
   B = {φ: (-∞,0] → ℝⁿ | φ measurable, ∫₋∞⁰ |φ(s)|² ds < ∞}

3. Fading memory space:
   B = {φ | ∫₋∞⁰ e^{αs}|φ(s)|² ds < ∞} for some α > 0

4. Sobolev phase space:
   B = {φ: (-∞,0] → ℝⁿ | φ, φ' ∈ L²}

Each choice of phase space affects solution structure
Determines which historical information matters
```

### Main Theorems

**Theorem 3.3 (Local Existence & Uniqueness):**
```
Suppose:
1. f is Carathéodory
2. f is L¹-Carathéodory with bound h_q ∈ L¹([0,b])
3. Iₖ are Lipschitz: |Iₖ(u) - Iₖ(v)| ≤ cₖ|u - v|
4. φ ∈ B (initial history)

Then:
∃ δ > 0 such that y'(t) = f(t, y_t) has unique solution on [0, δ]
with y(0⁺) = y(0) and jumps at t₁, ..., tₘ ∩ [0,δ]
```

**Theorem 3.11 (Global Existence & Uniqueness on infinite horizon):**
```
For problem (1.7)–(1.9) on [0,∞):
y'(t) = f(t, y_t) + Σ y(t - Tᵢ),  t ≠ tₖ
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(t) = φ(t),  t ∈ (-∞, 0]

If:
1. f and Iₖ satisfy Lipschitz conditions
2. Σ cₖ < 1 (impulses not too large)
3. Decay assumptions on f

Then: ∃! global solution on [0,∞)
      Solution is continuous except at impulse times
      Solution decays to zero as t → ∞
```

**Stability Result (Theorem 3.15):**
```
Under Lipschitz assumptions, solution y(t) depends continuously on:
- Initial history φ(t)
- Impulse functions Iₖ
- Right-hand side f(t, y_t)

Quantitative bounds on perturbations
```

### Second-Order Impulsive FDEs (Section 3.4)

**Problem:**
```
y''(t) = f(t, y_t),  a.e. t ∈ [0,b], t ≠ tₖ
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y'(tₖ⁺) - y'(tₖ⁻) = Ī_k(y(tₖ⁻))  [velocity jump]
y(t) = φ(t), y'(0) = ψ,  t ∈ (-∞,0]
```

**New aspect: Velocity jumps**
```
At each impulse time tₖ:
- Position may jump: y(tₖ⁺) ≠ y(tₖ⁻)
- Velocity may jump: y'(tₖ⁺) ≠ y'(tₖ⁻)

Physical example: collision of two particles
  Before: velocity v₁, v₂
  After: different velocities v'₁, v'₂
  Position jump relates to contact/rebound
  Velocity jump relates to elasticity coefficient
```

---

## CHAPTER 4: BOUNDARY VALUE PROBLEMS ON INFINITE INTERVALS

### Asymptotic Behavior

**Problem (Equations 4.18–4.20):**
```
y'(t) = f(t, y_t),  a.e. t ∈ [0,∞), t ≠ tₖ
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻)),  k = 1,2,...  (infinite sequence)
lim_{t→∞} y(t) = y₁,  A > 1
y(t) = φ(t),  t ∈ (-∞, 0]
```

**Key difference from finite intervals:**
```
Classical BVPs: y(0) = a, y(b) = b (two endpoints)
Infinite-interval: y(0) = φ, lim y(∞) = y₁ (asymptotic condition)

Requires:
1. Infinite sequence of impulses
2. Convergent behavior as t → ∞
3. Uniform bounds throughout [0,∞)
```

**Fixed-point formulation:**
```
Transform to integral equation:
y(t) = ∫₀ᵗ G(t,s)f(s, y_s)ds + Σ G(t, tₖ)Iₖ(y(tₖ⁻))

where G is Green's function for infinite interval
Poincaré operator maps solution set to itself on [0,∞)
```

---

## CHAPTER 5: DIFFERENTIAL INCLUSIONS (CORE THEORETICAL CHAPTER)

### Filippov's Theorem for Impulsive Systems

**Problem:**
```
y'(t) - λy(t) ∈ F(t, y(t)),  a.e. t ∈ J\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(0) = y₀  [initial or periodic condition]

F: J × ℝⁿ → P(ℝⁿ) is multi-valued (set-valued)
```

**Filippov's Theorem (5.1.1):**
```
If:
1. F is nonempty, closed, bounded, convex-valued
2. F is measurable in t
3. F is Hausdorff continuous in y: Hd(F(t,z₁), F(t,z₂)) ≤ p(t)|z₁-z₂|
4. Impulses satisfy Lipschitz conditions
5. Non-resonance: H* ||p||_{L¹} < 1 - Σcₖ

Then:
∃ solution y ∈ PC([0,b])  [piecewise continuous]
Error estimate: ||y - x||_{PC} ≤ ||γ||_{L¹} / (1 - H*||p||_{L¹} - H* Σcₖ)
```

**Why this matters:**
```
Filippov's theorem allows "regularization" of discontinuities:
1. Start with discontinuous/uncertain right-hand side F
2. Construct approximating single-valued g ∈ S_F (selection)
3. Solve g(y) instead
4. Error is bounded and measurable
5. True solution lies within error bounds
```

### Relaxation Theorem (Section 5.1.2)

**Problem of nonconvexity:**
```
Nonconvex F may have NO classical solutions
But convex hull co F always has solutions

Filippov-Wazewski Theorem (5.2):
Solutions of y'(t) ∈ F(t, y(t)) are dense in solutions of y'(t) ∈ co F(t, y(t))
```

**Meaning:**
```
- Nonconvex problem (e.g., optimal control with discontinuous cost)
- Convex relaxation (add all convex combinations)
- Solutions of nonconvex ⊂ closure of solutions of convex
- Optimal solutions of nonconvex approximate optimal of convex
```

### Upper Semicontinuity Without Convexity (Section 5.3)

**New theorem (Thm 5.3.1):**
```
Without assuming convexity of F values:
If F is u.s.c. (upper semicontinuous) and satisfies growth bounds,
Then solution set S_F(y₀) is nonempty, compact, and u.s.c. in y₀

"Nonconvex Theorem"
```

---

## CHAPTER 6: DIFFERENTIAL INCLUSIONS WITH INFINITE DELAY

**Problem:**
```
y'(t) ∈ F(t, y_t),  a.e. t ∈ [0,b]\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(t) = φ(t),  t ∈ (-∞, 0]

where F: [0,b] × B → P(ℝⁿ) and B is phase space
```

**New challenges:**
```
1. History dependence: y_t includes all past values
2. Phase space topology: Different choices of B
3. Measure of noncompactness: MNC essential for infinite delay
4. Selection theorems: Must work in phase space B
```

**Main result:**
```
Theorem 6.1.1 (Existence in Convex Case):
Under Carathéodory conditions on F and Lipschitz conditions on Iₖ,
∃ solution y ∈ C([0,b]; B) or y ∈ PC([0,b]; B)
Solution satisfies y(0) = φ(0) and impulse conditions

Proof via:
1. Approximate by single-valued f_n ∈ S_F (selections)
2. Solve linear equation: y'(t) = f_n(t, y_t)
3. Show solutions are relatively compact (using MNC)
4. Take limit as n → ∞
```

---

## CHAPTER 7: IMPULSIVE FDEs WITH VARIABLE TIMES

### State-Dependent Impulses

**Problem:**
```
y'(t) = f(t, y_t),  a.e. t ∈ [0,b], t ≠ τₖ(y)
y(τₖ⁺) - y(τₖ⁻) = Iₖ(y(τₖ⁻)),  k = 1,2,...
y(t) = φ(t),  t ∈ (-∞, 0]

where:
τₖ = τₖ(y) depends on solution y itself (state-dependent)
Impulse times are not predetermined
```

**Example (integrated pest management):**
```
x' = g(x)x - h(x,y)y  [prey dynamics]
y' = h(x,y)y - dy     [predator dynamics]
x(tₖ⁺) = px(tₖ⁻)      [culling when x = ET]
y(tₖ⁺) = y(tₖ⁻) + σ   [release natural enemies]

where tₖ = first time y(tₖ) = ET (economic threshold)
```

**Mathematical difficulty:**
```
1. Impulse times not predetermined (implicit in y)
2. Possible accumulation of impulses in finite time
3. Solution existence not automatic
4. Iterative scheme: guess τₖ → solve ODE → find actual τₖ
```

**Main theorem (7.1.2):**
```
Under conditions ensuring uniform separation of τₖ values:
τₖ₊₁ - τₖ ≥ δ > 0  for all k

∃ unique solution y on [0,b]
Solution is continuous except at τ₁, τ₂, ..., τₘ(y)
```

### Neutral Functional Differential Equations

**Problem:**
```
d/dt [y(t) - Ay(t-τ)] = f(t, y_t),  a.e. t ≠ tₖ
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(t) = φ(t),  t ∈ (-∞, 0]

where A is linear operator and Ay(t-τ) is "memory" term
Derivative applies to entire state y and its past
```

**Why different from retarded:**
```
Retarded: y' = f(t, y_t)
         Only y's past affects y'

Neutral: d/dt[y - Ay_{t-τ}] = f(...)
        Both y and its past affect y'
        More complex structure
```

---

## CHAPTER 8: NEUTRAL DIFFERENTIAL INCLUSIONS

**Problem:**
```
d/dt[y(t) - Ay(t-τ)] ∈ F(t, y_t),  a.e. t ∈ [0,b]\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(t) = φ(t),  t ∈ (-∞, 0]

F is multi-valued (differential inclusion instead of equation)
```

**Filippov's Theorem for Neutral Inclusions (Theorem 8.1.2):**
```
Under appropriate Carathéodory, Lipschitz, and measure conditions:

∃ solution to neutral inclusion
Error bounds via Filippov approximation
Relaxation theorem applies
```

---

## CHAPTER 9: TOPOLOGY AND GEOMETRY OF SOLUTION SETS

### Aronszajn Type Results

**Question:** What is the structure of S_F(y₀) = {all solutions with y(0) = y₀}?

**Theorem 9.2.3:**
```
For impulsive differential equations y' = f(t,y) with jumps:
Solution set S_F(y₀) forms an R_δ-set  [Aronszajn space]

R_δ sets:
- Generalize compact sets
- Have nice topological properties
- Can be "filtered" through retracts
```

### Contractible Solution Sets

**Definition (Section 9.4):**
```
A set X is contractible if:
∃ continuous H: X × [0,1] → X
such that:
  H(x, 0) = x (identity)
  H(x, 1) = x₀ (constant)

Intuitively: X can be "shrunk" to a point continuously
```

**Theorem 9.4.1:**
```
Under appropriate conditions on f and Iₖ:
S_F(y₀) is contractible

Meaning: All solutions can be continuously deformed into one solution
        No "holes" or separated branches
```

### Periodic Solutions (Section 9.6)

**Problem:**
```
y'(t) ∈ F(t, y(t)),  a.e. t ∈ [0,b]\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(0) = y(b)  [periodic boundary condition]

with period-matching impulse structure
```

**Poincaré Operator Approach (9.6.1):**
```
Define P: y(0) ↦ y(b|y₀) [solution map at one period]

Periodic solutions ↔ fixed points of P
P: ℝⁿ → P(ℝⁿ) is multi-valued

Use topological degree theory to count fixed points
```

**Theorem 9.6.3:**
```
Under Lipschitz and non-resonance conditions:
∃ at least one periodic solution

Proof: Topological degree of P ≠ 0 ⟹ Fix(P) ≠ ∅
```

### Solution Set for Terminal Problems (Section 9.8)

**Problem:**
```
y'(t) ∈ F(t, y(t))
y(0) = y₀  (initial condition)
y(b) ∈ C   (terminal constraint)

What is S_C(y₀) = {solutions satisfying terminal condition}?
```

**Theorem 9.8.1:**
```
Under appropriate conditions:
S_C(y₀) is nonempty, compact, contractible

Shows solution set has nice structure even with constraints
```

---

## CHAPTER 10: IMPULSIVE SEMILINEAR DIFFERENTIAL INCLUSIONS

### Infinite-Dimensional Setting

**Problem:**
```
y'(t) ∈ Ay(t) + F(t, y(t)),  a.e. t ∈ J\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(0) = y₀

where:
- E is Banach space
- A: D(A) ⊆ E → E is nondensely defined operator
- F: J × E → P(E) is multi-valued
- y₀ ∈ E (could be outside domain of A)
```

**Nondensely defined operators:**
```
Classical theory assumes D(A) = E (densely defined)

Nondensely defined:
- D(A) ≠ E (proper subset)
- y₀ might not be in domain!
- Requires integral semigroup theory

Example: Partial differential equations
  ∂u/∂t = Δu + F(t,u)  in domain Ω
  Operator A = Δ has domain ≠ all of L²(Ω)
  Initial condition might not be in domain
```

### Integral Solutions

**Definition (Section 10.2):**
```
Mild/integral solution:
y(t) = T(t)y₀ + ∫₀ᵗ T(t-s)f(s, y(s))ds + Σ T(t-tₖ)Iₖ(y(tₖ⁻))

where T(t) is integrated semigroup (not classical solution)

Avoids differentiability: y doesn't need to be in D(A)
```

### Controllability (Section 10.3)

**Problem:**
```
y'(t) = Ay(t) + Bu(t) + F(t,y(t))
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(0) = y₀

Question: Can we reach target y₁ at time T by choosing u(·)?
```

**Exact controllability:**
```
System is exactly controllable if:
For any y₀, y₁ ∈ E and T > 0,
∃ control u: [0,T] → U such that solution reaches y₁

Theorem 10.3.1:
Controllability depends on:
1. Rank of controllability matrix [B, AB, A²B, ...]
2. Impulse functions Iₖ
3. Nonlinear perturbation F
```

---

## CHAPTER 11: SELECTED TOPICS

### Impulsive Stochastic Differential Equations

**Problem:**
```
d[y(t) - Ay(t)] = f(t, y(t))dt + g(t, y(t))dW(t),  t ∈ J\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))
y(0) = y₀

where W(t) is Hilbert-space-valued Wiener process
```

**New difficulty:** Stochasticity
```
Classical: Deterministic evolution
Stochastic: Random perturbations + jumps

Solution concept: Mild solution using Itô integral
Existence via fixed-point theorems on stochastic function spaces
```

### Impulsive Sweeping Processes

**Problem:**
```
y'(t) ∈ N_{K(t)}(y(t)),  a.e. t ∈ J
y(0) ∈ K(0)

where:
K(t) is time-dependent moving constraint set
N_{K(t)}(y) is normal cone to K(t) at y
y(t) stays inside K(t) while "sweeping" along its boundary
```

**Application:** Friction and unilateral constraints
```
Example: Ball rolling in moving box
- Box K(t) moves with prescribed motion
- Ball y(t) constrained inside: y(t) ∈ K(t)
- No penetration allowed
- Friction dissipates energy
```

### Integral Inclusions of Volterra Type

**Problem:**
```
y(t) ∈ ∫₀ᵗ a(t-s)[Ay(s) + F(s, y(s))]ds,  t ∈ [0,b]

where a is resolvent kernel
```

**Connection to differential equations:**
```
For a(t) = δ(t) [Dirac delta]:
y' = Ay + F(t,y)  [recovery as special case]

Volterra integral with a(t) = 1:
y' = ∫₀ᵗ [Ay(s) + F(s,y(s))]ds
has memory of entire past evolution
```

---

## COMPARISON: MONOGRAPH vs. 2008 JOURNAL PAPER

| Aspect | 2008 Paper (Periodic) | 2013 Monograph |
|--------|----------------------|-----------------|
| **Scope** | Periodic boundary conditions only | 11 chapters, all major problem classes |
| **Delays** | None (fixed domain [0,b]) | Infinite delay in Chapters 3,6,8,11 |
| **Impulse times** | Fixed (predetermined) | Fixed and variable (Chapter 7) |
| **Problem types** | Single first-order | First/second-order, FDE, neutral, semilinear |
| **Dimension** | Finite (ℝⁿ) | Finite and infinite (Banach spaces) |
| **Methods** | Topological degree only | Fixed-point, degree, MNC, semigroups |
| **Stochasticity** | No | Chapter 11 |
| **Solution sets** | Existence only | Topology, geometry, contractibility |
| **Controllability** | Not addressed | Chapter 10 |
| **Pages** | ~40 (article) | ~400+ (monograph) |

---

## COMPLETE POSITION IN HIERARCHY

This monograph is fundamentally different from the 2008 paper—it's **the definitive research treatise**:

**Graef-Henderson-Ouahab Monograph Role:**

```
Mathematical Foundations
    ├─ Cooper (Distributions)
    └─ Graef/Henderson/Ouahab (Multi-valued, comprehensive)
         ↓
Classical Theory (foundational)
    ├─ Chen, d'Andréa-Novel, Dahleh, Fairman, Ghosh
         ↓
Computational Implementation
    ├─ Gear (Automatic detection)
    └─ Datta (Numerical algorithms)
         ↓
Impulsive-Specific Theory
    ├─ Dishliev (Asymptotic analysis)
    ├─ Brogliato (Measure theory)
    ├─ Graef/Ouahab 2008 (Periodic conditions, journal paper)
    └─ Graef/Henderson/Ouahab 2013 (Comprehensive monograph) ← RESEARCH APEX
         ↓
Applications & Extensions
    ├─ Chicurel-Uziel (Nonlinear)
    ├─ Falsone (Beams, pedagogy)
    └─ Chalishajar (Beams, advanced)
```

---

## SUMMARY

**Graef, Henderson & Ouahab's monograph is the research apex** because:

✓ **Comprehensive scope** — 11 chapters covering all major impulsive inclusion types  
✓ **Infinite delays** — Functional differential equations with full history  
✓ **Variable impulses** — State-dependent jump times  
✓ **Infinite dimension** — Semilinear operators in Banach spaces  
✓ **Fixed-point unification** — All theorems via topological fixed-point methods  
✓ **MNC theory** — Measure of noncompactness for non-compact problems  
✓ **Semigroup methods** — Integrated semigroups for nondensely defined operators  
✓ **Solution geometry** — Topology, contractibility, Aronszajn spaces  
✓ **Stochasticity** — Random impulsive systems  
✓ **Controllability** — Exact controllability in semilinear case  
✓ **Filippov approximation** — Error estimates and relaxation theory  
✓ **Rigorous proofs** — 400+ pages of complete mathematical development  

**Why this matters for discontinuous systems:**

The monograph completes the theoretical hierarchy by providing **the most comprehensive rigorous treatment** of impulsive differential inclusions using fixed-point theory. It extends far beyond the 2008 paper to cover:

1. **Infinite delays** — Systems with full historical dependence
2. **Variable impulses** — State-dependent jump times  
3. **Semilinear infinite-dimensional problems** — PDE-like systems  
4. **Stochastic impulses** — Random perturbations + jumps
5. **Controllability analysis** — Steering systems via controls
6. **Solution set geometry** — Topological structure of all solutions

The 2013 monograph is **where theory meets reality**: it provides the mathematical foundation for analyzing ANY impulsive differential inclusion, from pharmacokinetics (Kruger-Thiemer) to pest management (state-dependent impulses) to stochastic population dynamics.

**Graef & Ouahab transition from 2008 → 2013:**
- **2008 paper**: Specialized rigorous result (periodic conditions)
- **2013 monograph**: Comprehensive research treatise (everything)

Together they represent: **specialized brilliance → generalized mastery**.
