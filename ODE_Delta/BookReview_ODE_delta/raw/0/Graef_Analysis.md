# Graef & Ouahab: First Order Impulsive Differential Inclusions with Periodic Conditions

## Reference
**Paper**: First Order Impulsive Differential Inclusions with Periodic Conditions  
**Authors**: John R. Graef (University of Tennessee at Chattanooga), Abdelghani Ouahab (Université de Sidi Bel Abbès, Algeria)  
**Journal**: Electronic Journal of Qualitative Theory of Differential Equations  
**Date**: 2008, No. 31, pp. 1–40  
**Scope**: Rigorous theoretical treatment of impulsive differential inclusions using topological degree and fixed-point methods

---

## CENTRAL MISSION: Set-Valued Impulsive Differential Equations with Periodic Boundary Conditions

### The Problem Class

**Primary problem (Equations 1–3):**
```
y'(t) - λy(t) ∈ F(t, y(t)),  a.e. t ∈ J\{t₁,...,tₘ}
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻)), k = 1,...,m
y(0) = y(b)  [periodic boundary condition]

where:
- λ ≠ 0 is a parameter
- F: J × ℝⁿ → P(ℝⁿ) is multi-valued (set-valued)
- Iₖ: ℝⁿ → ℝⁿ characterize jump magnitudes
- J = [0,b]
```

**Secondary problem (Equations 16–18):**
```
x'(t) - λx(t) ∈ co F(t, x(t)),  a.e. t ∈ J\{t₁,...,tₘ}
x(tₖ⁺) - x(tₖ⁻) = Iₖ(x(tₖ⁻)), k = 1,...,m
x(0) = x(b)  [relaxed/convex hull version]

where co F is the convex hull of F
```

---

## HOW GRAEF & OUAHAB ADDRESS DISCONTINUITIES AND INITIAL CONDITIONS

### 1. Multi-Valued Analysis Framework

**Key advantage over single-valued theory:**
```
Single-valued ODE:  ẏ = f(t,y)  [deterministic behavior]
Multi-valued inclusion: ẏ ∈ F(t,y)  [set of possible behaviors]

Set-valued approach captures:
- Discontinuous uncertainty
- Multiple regimes
- Nonuniqueness of solutions
```

**Multi-valued properties (Definition 2.5-2.6 in paper):**
- **Carathéodory function**: Measurable in t, u.s.c. in y
- **L¹-Carathéodory**: Locally integrably bounded
- **Hausdorff metric**: Distance between sets

### 2. Jump Discontinuities via Impulse Functions

**Impulsive jumps formalized (Equation 2):**
```
y(tₖ⁺) - y(tₖ⁻) = Iₖ(y(tₖ⁻))

Jump magnitude at time tₖ depends on pre-jump state
Captured by impulse function Iₖ

Assumptions on Iₖ (Hypothesis H2):
|Iₖ(u) - Iₖ(z)| ≤ cₖ|u - z|
(Lipschitz continuity ensures stability)
```

### 3. Filippov's Theorem for Impulsive Inclusions

**Core theorem (Theorem 3.3):**
```
Given:
- Multi-valued F satisfies Carathéodory conditions
- Lipschitz condition with Hausdorff metric: Hd(F(t,z₁), F(t,z₂)) ≤ p(t)|z₁-z₂|
- Impulse functions Iₖ are Lipschitz continuous
- Non-resonance condition: H* ||p||_{L¹} < 1 - Σcₖ

Conclusion:
- Solution y exists
- Error bounds are explicit
- Estimate: ||y - x||_{PC} ≤ ||γ||_{L¹} / (1 - H* Σcₖ - H* ||p||_{L¹})
```

**What this means:**
- Approximates multivalued system by single-valued function g
- Measures distance γ(t) = d(g(t), F(t,x(t)))
- Bounds error propagation through jumps and continuous evolution

### 4. Solution Space: PC (Piecewise Continuous Functions)

**Definition (Page 7):**
```
PC = {y: J → ℝⁿ | yₖ ∈ C(Jₖ, ℝⁿ) for k=0,...,m,
                   left and right limits exist,
                   y(tₖ⁻) = y(tₖ⁺) [left-continuous at jumps]}

Norm: ||y||_{PC} = max{||yₖ||_∞ : k=0,...,m}
```

**Why PC space matters:**
- Solutions are continuous except at predetermined jump times
- Jumps are finite (not infinite at any point)
- Perfectly suited for impulsive systems

### 5. Green's Function / Fundamental Solution Matrix

**Green's function for linear part (Page 7):**
```
y(t) = ∫₀ᵇ H(t,s)f(y(s))ds + Σ H(t,tₖ)Iₖ(y(tₖ))

where:
H(t,s) = e^(-λ(b-s))/(e^(-λb) - 1),  0 ≤ s ≤ t ≤ b
        = e^(-λ(s-t)),               0 ≤ t < s ≤ b
```

**Bound on H:**
```
H* = sup{H(t,s) | (t,s) ∈ J×J}

Used to control error propagation through system
Critical in non-resonance condition
```

### 6. Handling Initial Condition Changes

**Periodic boundary condition (Equation 3):**
```
y(0) = y(b)

NOT standard initial condition
Requires solution to "wrap around" after one period
```

**Effect on solution:**
```
Solution must satisfy:
1) Differential inclusion throughout [0,b]
2) Impulsive jumps at t₁,...,tₘ
3) Closure condition: y(0) = y(b)

Changes asymptotic behavior significantly
```

---

## RELAXATION THEOREM (SECTION 4)

### Problem of Nonconvexity

**Classical issue:**
```
Nonconvex F(t,y) may have no solutions
But co F(t,y) [convex hull] always has solutions

Question: Are solutions of nonconvex system
         contained in solutions of convex system?
```

### Filippov-Wasewski Result

**Theorem 4.3:**
```
Solutions of nonconvex problem (1)–(3) are dense in
solutions of relaxed problem (16)–(18)

Physical meaning:
- Nonconvex problem has "economical" solutions (simpler control)
- Convex relaxation adds unnecessary solutions
- Density means: any convex solution approximated by nonconvex ones
```

---

## MATHEMATICAL FRAMEWORK

### Multi-Valued Analysis Tools Used

**1. Measurability (Lemma 2.1):**
```
F is measurable iff for each x, distance function
ζ(t) = dist(x, F(t)) is Lebesgue measurable

Critical for defining solutions via integrals
```

**2. Selection Theorem (Lemma 2.3 - Kuratowski-Ryll-Nardzewski):**
```
If G has nonempty closed values, ∃ measurable selection u: J → E
such that u(t) ∈ G(t) for all t

Key step in Filippov proof (constructs approximations fₙ)
```

**3. Hausdorff Distance:**
```
Hd(A,B) = max{ sup d(a,B), sup d(A,b) }
              a∈A         b∈B

Measures "distance between two sets"
Used to define Lipschitz condition on F
```

**4. Topological Degree & Fixed-Point Theory:**
```
Poincaré operator approach (Section 6):
- Map solution space to itself via: y → T(y)
- T has fixed points ↔ solutions exist
- Degree theory ensures fixed point existence
```

### Contraction Mapping Principle (Lemma 4.2)

**Covitz-Nadler Theorem:**
```
If G: X → P_cl(X) is γ-Lipschitz contraction (γ < 1):
  Hd(G(x), G(y)) ≤ γ · d(x,y)

Then G has nonempty fixed-point set Fix(G) ≠ ∅
```

**Application to impulsive systems:**
```
Define T: PC → P(PC) by solutions of perturbed problem
Non-resonance condition ensures T is contraction
Guarantees unique solution (or at least existence)
```

---

## COMPLETE SOLUTION CONSTRUCTION

### Iterative Procedure (Proof of Theorem 3.3)

**Step 0: Start with reference solution**
```
y₀ from linear problem with reference input g
```

**Step 1: Construct approximating multivalued sets**
```
U₁(t) = F(t, y₀(t)) ∩ B(g(t), γ(t))
        [intersection of F with ball around g]

By Lemma 2.4 (Measurable Selection):
∃ measurable selection f₁ ∈ U₁
```

**Step 2: Solve linearized problem**
```
y'(t) - λy(t) = f₁(t),  with jumps Iₖ(y₁(tₖ⁻))
y₁(0) = y₁(b)

Error bound: ||y₁ - y₀||_{PC} ≤ (H* ||γ||_{L¹}) / (1 - H* Σcₖ)
```

**Step 3: Iterate**
```
Define Uₙ₊₁(t) = F(t, yₙ(t)) ∩ B(fₙ(t), p(t)||yₙ - yₙ₋₁||)

Each iteration reduces error by factor H* ||p||_{L¹} < 1

Limit y = lim yₙ satisfies original inclusion
```

### Error Bounds

**Measure-theoretic control (Page 12-14):**
```
||yₙ₊₁ - yₙ||_{PC} ≤ (H*)ⁿ⁺¹ / (1 - H* Σcₖ)ⁿ⁺¹ · ||p||_{L¹}ⁿ · ||γ||_{L¹}

Non-resonance condition H* ||p||_{L¹} / (1 - H* Σcₖ) < 1 ensures convergence

Final error: ||y - x||_{PC} ≤ ||γ||_{L¹} / (1 - H* Σcₖ - H* ||p||_{L¹})
```

---

## RELEVANCE TO DISCONTINUOUS RHS RESEARCH

**Graef & Ouahab's contribution is specialized and rigorous** because:

✓ **Set-valued framework** — Handles uncertainty, multiplicity, nonuniqueness  
✓ **Filippov's theorem** — Approximation theory for discontinuous systems  
✓ **Impulse functions Iₖ** — Explicit characterization of jump behavior  
✓ **Periodic boundary conditions** — Non-standard, reflects cyclic dynamics  
✓ **Green's function** — Systematic solution representation  
✓ **Relaxation theory** — Convexification and density of solutions  
✓ **Error bounds** — Explicit, quantitative stability results  
✓ **Topological methods** — Fixed-point theory guarantees solutions  

**Connection to other frameworks:**

- **Dishliev**: Analyzes asymptotic behavior → Graef constructs solutions
- **Gear**: Numerical detection → Graef provides rigorous theory
- **Brogliato**: Measure equations → Graef extends to set-valued form
- **Falsone**: Analytical for special cases → Graef handles general nonconvex F

---

## COMPLETE HIERARCHY: All Sixteen Frameworks

| # | Author | Level | Method | Best For |
|---|--------|-------|--------|----------|
| 1 | **Camporesi (1)** | Elementary | Initial conditions | Intuition |
| 2 | **Camporesi (2)** | Elementary | Factorization | Variable coeff |
| 3 | **Chen** | Classical | State-space | Foundational |
| 4 | **d'Andréa-Novel** | Classical | Transfer functions | Frequency domain |
| 5 | **Brogliato** | Rigorous | Measures | Nonsmooth mech |
| 6 | **Chalishajar** | Applied | Generalized functions | Beams (advanced) |
| 7 | **Chicurel-Uziel** | Novel | Parametrization | Nonlinear |
| 8 | **Cooper** | Foundation | Distribution theory | Math rigor |
| 9 | **Dahleh** | Practice | Systems theory | Engineering |
| 10 | **Datta** | Computation | Numerical algorithms | Implementation |
| 11 | **Dishliev** | Qualitative | Impulsive theory | Asymptotic |
| 12 | **Fairman** | Design | Control synthesis | Advanced design |
| 13 | **Falsone** | Applied | Generalized functions | Beams (pedagogy) |
| 14 | **Gear** | Computational | Automatic methods | Numerical ODE |
| 15 | **Ghosh** | Academic | Comprehensive integration | Student education |
| 16 | **Graef** | Theoretical | Multi-valued analysis | Set-valued systems |

**The complete ecosystem:**

```
Mathematical Foundations
    ├─ Cooper (Distributions)
    └─ Graef (Multi-valued analysis)
         ↓
Classical Theory
    ├─ Chen, d'Andréa-Novel, Dahleh, Fairman
    └─ Ghosh (Comprehensive synthesis)
         ↓
Computational Implementation
    ├─ Gear (Automatic detection)
    └─ Datta (Numerical algorithms)
         ↓
Impulsive-Specific Theory
    ├─ Dishliev (Asymptotic)
    ├─ Brogliato (Measure theory)
    └─ Graef (Set-valued rigorous) ← NEW
         ↓
Extensions & Applications
    ├─ Chicurel-Uziel (Nonlinear)
    ├─ Falsone (Beams, pedagogy)
    └─ Chalishajar (Beams, advanced)
```

---

## SUMMARY

**Graef & Ouahab's contribution is uniquely specialized** because:

✓ **Set-valued differential equations** — Most general framework  
✓ **Filippov's theorem** — Approximation/perturbation theory  
✓ **Impulse functions Iₖ** — Explicit discontinuity characterization  
✓ **Periodic boundary conditions** — Cyclic, non-standard setting  
✓ **Relaxation theorems** — Convexification of solution sets  
✓ **Error estimates** — Explicit, verifiable bounds  
✓ **Topological methods** — Fixed-point theory, degree theory  
✓ **Multi-valued analysis** — Rigorous generalization  

**Why Graef matters for discontinuous systems:**

Graef & Ouahab provide the **most general rigorous mathematical framework** for impulsive differential inclusions. They show:

1. **Solutions always exist** (via topological methods)
2. **Error can be bounded** (via Filippov theorem)
3. **Approximation works** (via relaxation theory)
4. **Convexification is dense** (density in solution space)

This completes the theoretical hierarchy: starting from Cooper's distributions, through Dishliev's asymptotic analysis and Brogliato's measure theory, Graef & Ouahab provide the **most advanced rigorous treatment** using set-valued/multi-valued analysis.

Graef represents the **apex of theoretical rigor** for discontinuous systems—everything more specialized than this is application-specific (beams, control, nonlinear) rather than foundational.
