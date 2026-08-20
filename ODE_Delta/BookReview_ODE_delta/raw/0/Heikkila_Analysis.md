# Heikkila, Kumpulainen & Seikkala: Existence, Uniqueness, and Comparison Results for a Differential Equation with Discontinuous Nonlinearities

## Reference
**Paper**: Existence, Uniqueness, and Comparison Results for a Differential Equation with Discontinuous Nonlinearities  
**Authors**: Seppo Heikkila, Martti Kumpulainen, and Seppo Seikkala, University of Oulu, Finland  
**Journal**: Journal of Mathematical Analysis and Applications  
**Volume/Issue**: 201, pp. 478-488  
**Date**: 1996  
**Scope**: Existence, uniqueness, and comparison theorems for discontinuous ODEs using monotone iterative techniques

---

## CENTRAL MISSION: Discontinuous ODEs via Monotone Iterative Techniques

### The Research Problem

**Special problem class:**
```
Initial value problem:
  x'(t) = q(x(t))·g(t, x(t))
  x(0) = x₀
  
where:
- q: ℝ → (0, ∞) can be discontinuous everywhere
- g: J × ℝ → ℝ can be discontinuous in t (measurable)
- g(t, ·) can be left-continuous discontinuous

Classical solutions may not exist!
Need generalized solution concept using lower/upper solutions
```

**Approach: Monotone Iterative Techniques**
- Uses lower and upper solution framework
- Establishes comparison theorems
- Proves existence and uniqueness
- Shows monotone dependence on parameters

---

## KEY INNOVATION: MULTIPLICATIVE FORM AND GENERALIZED SOLUTIONS

### Why Multiplicative Structure Matters

**Standard form:**
```
x' = f(t, x)  (additive)

Heikkila's form:**
x' = q(x)·g(t,x)  (multiplicative)

Advantage of multiplicative form:
- Separates "scaling" q(x) from "direction" g(t,x)
- Allows q to have wild discontinuities
- g discontinuities manageable
- Enables monotone iterative methods
```

### Solution Definition via Absolutely Continuous Functions

**Not classical solutions:**
```
Classical: x'(t) = q(x(t))g(t,x(t)) for all t
           (requires derivatives to exist everywhere)

Heikkila's generalized:
x ∈ AC([0,T]) (absolutely continuous)
x' = q(x)g(t,x) for a.e. t (almost everywhere)

Weaker requirement!
Allows jump discontinuities in g
```

---

## THEOREM 2.1: EXISTENCE THEOREM

### Conditions on q (Condition q)

```
q: ℝ → (0, ∞) must satisfy:
1. q is measurable (not required to be continuous!)
2. ||q||_∞ is bounded (essentially bounded)
3. 1/q is locally essentially bounded (reciprocal bounded away from 0)

These allow DISCONTINUITIES in q!
Example: q(x) = [x] (greatest integer) satisfies condition (q)
```

### Conditions on g (Conditions g0-g1)

**Condition (g0): Right-continuity and semicontinuity**
```
g(·,z) is measurable (Lebesgue integrable)
For all z ∈ ℝ and a.a. t ∈ J:
  lim sup_{y→z⁻} g(t,y) ≤ g(t,z) = lim_{y→z⁺} g(t,y)

Meaning:
- Right-continuous: g(t,z) = lim_{y→z⁺} g(t,y)  ✓
- Left-hand limit may be DIFFERENT: lim_{y→z⁻} g(t,y) ≤ g(t,z)
- Upper semicontinuity from left

Allows LEFT-DISCONTINUOUS FUNCTIONS!
```

**Condition (g1): Growth bound**
```
|g(t,z)| ≤ p(t)·c(|z|) for all z ∈ ℝ, a.a. t ∈ J

where:
- p ∈ L¹(J, ℝ₊)  (integrable)
- c: ℝ₊ → (0,∞)  (increasing)
- ∫₀^∞ dv/c(v) = ∞  (sublinear growth)

Ensures solutions don't blow up in finite time
```

### Theorem 2.1 Statement

```
If conditions (q), (g0), (g1) hold, then for each x₀ ∈ ℝ,
the IVP x' = q(x)g(t,x), x(0) = x₀ has at least one solution.

Proof idea:
1. Construct bounded comparison functions (upper and lower solutions)
2. Apply existence theorem from monotone iterative techniques
3. Use Carathéodory conditions with discontinuities
```

---

## UNIQUENESS CONDITIONS: GENERALIZATIONS OF CLASSICAL THEOREMS

### Condition (g2): Sign Restriction

```
g(t,z) ≥ 0 for a.a. t ∈ J and all z ∈ ℝ

Why essential:
- Ensures solutions are increasing (monotone)
- Enables comparison principle
- Allows use of monotone iterative framework
```

### Condition (g3): Generalized Osgood Condition

**General form:**
```
For each z₀ ∈ ℝ, ∃ r > 0 such that:
g(t,y) - g(t,z) ≤ h(t, y-z)  for a.a. t ∈ J
                             and z₀ ≤ z < y ≤ z₀ + r

where h: (0,T] × [0,r] → ℝ₊ satisfies:
- h(·,v(·)) ∈ L¹(J, ℝ₊) for absolutely continuous v: J → [0,r]
- v(t) ≡ 0 is ONLY solution of ||q||_∞ ∫₀ᵗ h(s,v(s)) ds ≥ v(t)

Why this works:
- Compares g differences via h
- h can be discontinuous!
- Condition on solution of integral inequality ensures uniqueness
```

### Condition (g4): Generalized Athanassov Condition

**Alternative form:**
```
For each z₀ ∈ ℝ, ∃ r > 0 such that:
g(t,y) - g(t,z) ≤ (u(t)/||q||_∞·U(t))·(y-z)  for a.a. t ∈ J
                                            and z₀ ≤ z < y ≤ z₀ + r

where:
- u ∈ L¹(J, ℝ₊), with U(t) = ∫₀ᵗ u(s) ds > 0 for 0 < t ≤ T
- sup{[g(t,y) - g(t,z)]₊ | z₀ ≤ z ≤ y ≤ z₀ + r} = o(u(t)) as t → 0⁺

Less restrictive than (g3)
Allows larger class of discontinuous functions
```

### Theorem 2.2: Uniqueness Theorem

```
If conditions (q), (g2), and ONE OF (g3) or (g4) hold,
then the IVP has AT MOST ONE solution.

Proof via Lemma 2.1 (Comparison Principle):
Lower solution y and upper solution z satisfy y ≤ z
This comparison holds even with discontinuities!
```

### Theorem 2.3: Complete Existence and Uniqueness

```
If conditions (q), (g0), (g1), (g2), and ONE OF (g3) or (g4) hold,
then for each x₀ ∈ ℝ, the IVP has a UNIQUE solution.
```

---

## SPECIAL CASES: CLASSICAL THEOREMS GENERALIZED

### Proposition 3.1: Six Classical Conditions Recovered

**Condition (g5-g9) recover:**
1. **Bompiani condition**: g(t,y) - g(t,z) ≤ h(t, y-z)
2. **Osgood condition**: g(t,y) - g(t,z) ≤ p(t)w(y-z), ∫₀ʳ dv/w(v) = ∞
3. **Iterated logarithmic condition**: Nested iterated logs for slow growth
4. **Lipschitz condition**: g(t,y) - g(t,z) ≤ p(t)(y-z), standard Lipschitz
5. **Hölder-type condition**: Fractional power growth controlled by t

**Significance:**
```
All these classical conditions are SPECIAL CASES of (g3) or (g4)
This shows Heikkila's conditions are GENUINELY MORE GENERAL
Includes nonlinear growth conditions via iterating logs
```

---

## MONOTONE DEPENDENCE AND RIGHT-CONTINUITY

### Lemma 4.1: Monotone Dependence of Solutions

**Solutions increase with parameters:**
```
If x₀ ≤ x̂₀,  q(u) ≤ q̂(u),  g(t,u) ≤ ĝ(t,u)
Then solution x(t) ≤ x̂(t)  for all t ∈ J

Physical meaning:
- Larger initial condition → larger solution
- Larger scaling q → larger solution  
- Larger direction g → larger solution
```

### Proposition 4.1: Right-Continuity of Solutions

**Decreasing sequences converge:**
```
If (g_n) decreasing, g_n → g, (x_on) decreasing, x_on → x_o
Then the sequence of solutions (x_n) converges uniformly to x

Key requirement: Sequence must be DECREASING
Not true for arbitrary sequences (counterexample given in paper)

Monotone convergence, not uniform convergence!
```

---

## METHOD OF SUCCESSIVE APPROXIMATIONS

### Proposition 5.1: When g is Increasing in Second Argument

**Iterative construction:**
```
If g(t,·) is INCREASING for a.a. t ∈ J, then define:

y₀(t) = solution of w' = ||q||_∞ p(t)c(w),  w(0) = |x₀|

y_{n+1} computed from:
∫_{x₀}^{y_{n+1}(t)} dv/q(v) = ∫₀ᵗ g(s, y_n(s)) ds

Then:
- Sequence (y_n) is decreasing
- Converges uniformly to solution x
- x solves the original IVP
```

**Why monotone improvement works:**
```
If g is increasing: larger y_n gives larger RHS
So y_{n+1} < y_n (decreasing iteration)
Monotone convergence from above
```

---

## COMPARISON TO OTHER APPROACHES

| Framework | Method | Uniqueness Type | Discontinuity Allowed |
|-----------|--------|-----------------|----------------------|
| **Heikkila** | Monotone iterations | One-sided Lipschitz-type | Very general (measurable q, left-discontinuous g) |
| **Hassan** | Angular continuity | Directional continuity | Scalar only, cone structure |
| **Graef** | Filippov regularization | Lipschitz conditions | Measurable, via convex hull |
| **Brogliato** | Measure theory | Integral inequalities | Via Lebesgue-Stieltjes measures |
| **Classical** | None | Lipschitz | Continuous only |

**Heikkila's unique advantages:**

1. **Very weak continuity requirements**
   - g can be left-discontinuous
   - q can be discontinuous everywhere
   - Only measurability needed (almost everywhere)

2. **Multiplicative structure**
   - x' = q(x)g(t,x) separates scaling from direction
   - Enables monotone iterative methods
   - More natural for certain applications

3. **One-sided conditions**
   - (g3) and (g4) generalize classical one-sided Lipschitz
   - Include Bompiani, Osgood, Lipschitz as special cases
   - Hierarchical: (g9) ⊂ (g8) ⊂ (g7) ⊂ ... ⊂ (g3)

4. **Monotone dependence**
   - Solutions depend monotonically on parameters
   - Right-continuous in solutions
   - Successive approximations method

---

## EXAMPLES IN PAPER

### Example 4.1: Wildly Discontinuous q

**Definition:**
```
q(z) = Σ_{m,k=1}^∞ (2 + ⌊k^{1/m}z⌋ - k^{1/m}z)·(2 + sin(...))

Discontinuity points: n/k^{1/m} for n ∈ ℤ, k,m = 1,2,...
EVERYWHERE DISCONTINUOUS! (dense set of jumps)

But: 1 ≤ q(z) ≤ 4π/6 for all z
Still bounded and satisfies condition (q)!
```

**Paired with g from equation (4.2):**
```
g satisfies (g0)-(g2) and (g3) with h ≡ 0
IVP has unique solution for each x₀ ∈ ℝ
Solution increases with x₀
```

**Significance:**
Shows Heikkila's theory handles GENUINELY DISCONTINUOUS functions, not just "nice" discontinuities.

### Example 5.1: Monotone Iteration Example

```
Same q as Example 4.1
Different g that is INCREASING in second variable
IVP solved by successive approximations
y_n converges uniformly to solution x
```

---

## COMPLETE POSITION IN FRAMEWORK

**Heikkila's role: Monotone iterative techniques for very general discontinuities**

```
Theoretical Foundations
    ├─ Cooper (Distributions)
    └─ Multi-valued / Single-valued approaches
         ├─ Graef (Filippov, multivalued)
         ├─ Hassan (Angular continuity, single-valued)
         └─ Heikkila (Monotone iterations, very general) ← HERE
         ↓
Computational / Applied
    ├─ Gear, Datta
    └─ Haddad, etc.
```

---

## SUMMARY

**Heikkila et al. provide the most general lower/upper solution framework** because:

✓ **Very weak continuity** — Only measurable q, left-discontinuous g  
✓ **Multiplicative form** — x' = q(x)g(t,x) enables decomposition  
✓ **Generalized uniqueness** — One-sided Lipschitz conditions (g3-g9)  
✓ **Classical theorems recovered** — Bompiani, Osgood, Lipschitz are special cases  
✓ **Monotone dependence** — Solutions increase with parameters  
✓ **Right-continuity** — Decreasing sequences converge  
✓ **Successive approximations** — When g is increasing in second variable  
✓ **Wildly discontinuous examples** — q can be discontinuous everywhere!  

**Why Heikkila matters for discontinuous systems:**

Heikkila & Kumpulainen provide the **most practical monotone iterative framework** for discontinuous ODEs. Unlike Graef (requires multivalued theory) or Hassan (requires cone structure), Heikkila's approach:

1. Uses elementary monotone iterative techniques
2. Handles VERY general discontinuities
3. Enables successive approximations
4. Shows monotone convergence
5. Generalizes classical uniqueness conditions

**Three complementary research approaches:**

1. **Filippov (Graef)**: Rigorous, uses regularization, multifunction framework
2. **Angular continuity (Hassan)**: Elegant, geometric, single-valued
3. **Monotone iterations (Heikkila)**: Practical, constructive, most general discontinuities

Heikkila is the **most applied-friendly** because:
- No measure theory required
- Constructive (successive approximations)
- Handles wild discontinuities (dense jump points)
- Monotone dependence is verifiable
