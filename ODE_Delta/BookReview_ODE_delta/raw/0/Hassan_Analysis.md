# Hassan & Rzymowski: On the Cauchy Problem for Ordinary Differential Equations with Discontinuous Right-Hand Sides

## Reference
**Paper**: On the Cauchy Problem for Ordinary Differential Equations with Discontinuous Right-Hand Sides  
**Authors**: Nizar Hassan and Witold Rzymowski, Instytut Matematyki UMCS, Lublin, Poland  
**Journal**: Journal of Mathematical Analysis and Applications  
**Volume/Issue**: 152, pp. 1-5  
**Date**: 1990  
**Scope**: Existence theorem for Cauchy problem with discontinuous right-hand sides via angular continuity concept

---

## CENTRAL MISSION: Alternative Theory for Discontinuous ODEs via Angular Continuity

### The Research Problem

**Classical Cauchy problem:**
```
Initial value problem:
  x' = f(t, x)
  x(t₀) = x₀

Standard assumption: f is continuous

Question posed: What if f is discontinuous?
  Classical solutions may not exist
  Need generalized solution concept
```

**Hassan & Rzymowski's approach:**

Instead of Filippov regularization (used by Graef), they introduce **angular continuity (a-continuity)** as a weaker condition allowing discontinuous functions to have solutions.

---

## KEY INNOVATION: ANGULAR CONTINUITY (AC)

### Definition 1: a-Continuity on Cone K

**Problem setup:**
```
K = {(t,x) ∈ ℝ² : t > 0, a·t < x < b·t}
  (cone in R² with angle determined by a, b)

f: K → [a, b]  (scalar function on cone)
```

**Definition of angular continuity:**
```
f is a-continuous if:
  For any (t,x) ∈ K and any ε > 0,
  ∃ δ > 0 such that:
  
  IF  t < s < t + δ  (time increases)
  AND (s-t)a < y - x < (s-t)b  (y stays in cone relative to x)
  AND (s-t)(f(t,x) - ε) < y - x < (s-t)(f(t,x) + ε)
  
  THEN |f(s,y) - f(t,x)| < ε
```

**What this means intuitively:**
```
Standard continuity:
  If (s,y) → (t,x), then f(s,y) → f(t,x)
  
Angular continuity:
  If (s,y) approaches (t,x) ALONG the cone direction,
  specifically along the "direction" (1, f(t,x)),
  then f(s,y) → f(t,x)
  
Key difference:
  Only requires continuity along SPECIFIC directions
  Not along all paths → weaker condition
  Allows discontinuities in other directions!
```

### Why This Works

**Comparison to other approaches:**

```
Filippov regularization (Graef):
  Replace f(t,x) with convex hull co f(t,x)
  Adds multivalued complexity
  
Measure differential equations (Brogliato):
  Use Lebesgue-Stieltjes measures
  Requires measure theory background
  
Angular continuity (Hassan):
  Directional continuity along cone
  Preserves single-valued form
  More geometric/intuitive
```

### Example of a-Continuous Function

**Non-trivial discontinuous example (Example 1 in paper):**
```
K = {(t,x) ∈ ℝ² : t > 0, 0 < x < t}
W = {wₙ : n ∈ ℕ} = set of interior points with rational coordinates

For (t,x) ∈ K:
  C(t,x) = cone emanating from (t,x)
  f(t,x) = (1+t+x)⁻¹ Σ 2⁻ⁿ  (sum over indices in specific cone)

Result:
  f is a-continuous everywhere in K
  BUT f is NEITHER r-continuous NOR d-continuous at any w ∈ W
  (These are other continuity concepts from literature)
```

**Significance:**
Shows a-continuity is strictly weaker than r-continuity or d-continuity, allowing genuinely discontinuous functions.

---

## MAIN THEOREM 1: Existence for Scalar Case

### Theorem Statement

**For scalar ODEs on cone:**
```
K = {(t,x) ∈ ℝ² : t > 0, a·t < x < b·t}
f: K → [a,b] a-continuous

Then ∃ absolutely continuous x: [0,∞) → ℝ such that:
  1. (t, x(t)) ∈ K  for t > 0  (stays in cone)
  2. Dx(t) = f(t, x(t))  for t > 0  (satisfies ODE with right-hand derivative)
  3. x(0) = 0  (initial condition)
  4. Dx is continuous from the right
```

### Solution Concept: Right-Hand Derivative

**Key difference from classical ODE:**
```
Classical: x'(t) exists (two-sided derivative)

Hassan & Rzymowski: Dx(t) = right-hand derivative only
  Dx(t) = lim_{h→0⁺} [x(t+h) - x(t)]/h
  
This is weaker than classical derivative!
  One-sided instead of two-sided
  Allows more discontinuities
```

**Why right-hand derivative?**
```
With discontinuous f, two-sided derivative may not exist
But right-hand derivative (from forward direction) can be defined
Still allows solution to satisfy ODE in forward time sense
```

### Proof Technique: Dini Derivatives

**Novel method using Dini derivatives:**

```
Upper Dini derivative: D⁺x(t) = lim sup_{h→0⁺} [x(t+h)-x(t)]/h
Lower Dini derivative: D⁻x(t) = lim inf_{h→0⁺} [x(t+h)-x(t)]/h

Key lemma (Lemma 1):
  If f is a-continuous, then we can approximate by absolutely continuous functions
  Using this approximation and Dini calculus:
  x(t) = inf{z(t) : z ∈ ℐ}  where ℐ is special function class
  
This infimum satisfies ODE with D⁻x(t) = D⁺x(t) = f(t,x(t))
```

**Proof strategy:**
```
1. Define comparison class ℐ of functions satisfying certain inequalities
2. Take infimum x(t) = inf{z(t) : z ∈ ℐ}
3. Show x satisfies Dx = f using Dini derivative properties
4. Use a-continuity to ensure smoothness of solution
```

---

## THEOREM 2: Autonomous Systems in ℝ²

### Extension to Multivariate Systems

**Problem:**
```
Autonomous system in ℝ²:
  y'(t) = g(y(t))
  y(0) = 0
  
where g: K → K is potentially discontinuous
and K is closed convex cone in ℝ²
```

### Definition 2: a-Continuity in ℝ²

**Cone structure:**
```
For e ∈ ℝ² and μ ∈ (0,1]:
  S(e,μ) = {x ∈ ℝ² : (x,e) > (1-μ)|x||e|}  (cone sector)
  
g is a-continuous if:
  For any x ∈ K and ε > 0, ∃ r > 0 such that
  if y ∈ x + S(g(x), ε) and |y-x| ≤ r
  then g(y) ∈ S(g(x), ε)  and |g(y) - g(x)| < Lε
```

**Connection between definitions:**
```
Remark 2 in paper:
  If f: K → [a,b] is a-continuous (Def 1),
  then g(t,x) = (1, f(t,x)) is a-continuous (Def 2)
  
This shows scalar theorem implies vector result
```

### Theorem 2 Statement

```
K ⊂ ℝ² closed convex cone with vertex at origin
g: K → K\{0} is:
  - a-continuous
  - bounded
  - inf{|g(x)| : x ∈ K} > 0  (away from zero)

Then ∃ absolutely continuous y: [0,∞) → K satisfying:
  Dy(t) = g(y(t))
  y(0) = 0
  Dy continuous from the right
```

### Proof: Coordinate Transformation

**Key technique:**
```
1. Decompose g(y) = (g₁(y), g₂(y)) in suitable coordinates
   Arrange: inf{g₁(y) : y ∈ K} > 0  (positive first component)

2. Set f(u,z) = g₂(u,z)/g₁(u,z)  (projection onto cone)
   
3. Apply Theorem 1 to get solution z(u)

4. Solve auxiliary ODE Du = h(u) where h(u) = g₁(u, z(u))
   (This is scalar, bounded away from 0, so solvable)

5. Reconstruct: y₁(t) = u(t), y₂(t) = z(u(t))
   Then Dy = g(y)
```

---

## COMPARISON TO OTHER DISCONTINUOUS ODE THEORIES

| Framework | Method | Assumptions | Solution Type |
|-----------|--------|-------------|-----------------|
| **Filippov** (Graef) | Convex hull regularization | Measurable | Multi-valued |
| **Measure theory** (Brogliato) | Lebesgue-Stieltjes measures | BV measures | Generalized |
| **Angular continuity** (Hassan) | Directional continuity | Cone structure | Single-valued, Dx only |
| **Classical** | None | Continuity | x' (two-sided) |

**Hassan & Rzymowski's unique features:**

1. **Single-valued solutions** — Not multi-valued like Filippov
2. **Weaker continuity** — a-continuity < r-continuity < standard continuity
3. **Right-derivative only** — Not full derivative (weaker requirement)
4. **Cone-based** — Works on specific cone geometry (limitation but also structure)
5. **Dini derivative methods** — Elegant use of one-sided derivatives

---

## LIMITATIONS AND SCOPE

### Restrictions vs. Graef

**Hassan & Rzymowski's limitations:**
```
1. Scalar case only (Theorem 1) or autonomous systems (Theorem 2)
   Cannot handle general time-dependent f(t,x) in ℝⁿ

2. Cone structure required
   K = {(t,x) : t > 0, at < x < bt}
   Not general domain

3. f must map into [a,b] (bounded range)
   Restricts applicability

4. Right-hand derivative Dx only
   Not classical derivative x'
   Solution smoother but less standard
```

**Graef's advantages:**
```
1. General set-valued inclusions
   Can handle y' ∈ F(t,y) (multifunction)
   
2. Any measurable space
   Not restricted to cones
   
3. Classical Lipschitz conditions
   Standard theory framework
   
4. Impulsive systems (Chapter 10)
   Handles jumps, not just discontinuities
```

**Hassan & Rzymowski's advantages:**
```
1. Simpler approach
   No measure theory background required
   
2. Single-valued solutions
   More concrete than multivalued
   
3. Geometric intuition
   Angular continuity is directional (visual)
   
4. Elegant proof technique
   Dini derivatives + inf over comparison class
```

---

## RESEARCH CONTEXT AND CITATIONS

### Referenced Work Cited

**[5] Peetre & Persson (1971):**
```
"The Peano Existence Theorem under Weaker Assumptions"
Earlier work on existence with weaker conditions
Hassan builds on this tradition
```

**[1] Binding (1979):**
```
"The differential equation x' = f(x)"
Autonomous case where f is discontinuous
Hassan extends this to time-dependent case
```

**[3] Giuntini & Pianigiani (1974):**
```
"Equazioni differenziali ordinarie con secondo membro discontinuo"
(Ordinary differential equations with discontinuous right-hand side)
Direct predecessor to Hassan's work
```

### Motivation from Peetre & Persson

The paper explicitly references Lakshmikantham's question (Submitted by V. Lakshmikantham) as motivation:
```
"These results can be treated as a very particular answer to the question
raised in [5, Sect. 16.5, p. 113]"

Question: Can Peano's existence theorem hold under weaker continuity assumptions?

Hassan's Answer: YES, via angular continuity on cones
```

---

## MATHEMATICAL TECHNIQUES AND INSIGHT

### Key Lemma 1: Approximation by Absolutely Continuous Functions

**The crucial step:**
```
Lemma 1: If f is a-continuous on K, then for any (t₀,x₀) ∈ K and ε > 0,
∃ absolutely continuous y: [t₀,∞) → ℝ such that:
  - y(t₀) = x₀
  - (t, y(t)) ∈ K
  - 0 < Dy(t) - f(t,y(t)) < ε

Meaning:
  Can approximate discontinuous function with smooth function y
  Approximation error measured by ε
  Allows passage to limit
```

### Key Technique: Infimum of Comparison Class

**Define comparison class ℐ:**
```
ℐ = {z: [0,∞) → ℝ | 
     z(0)=0,
     a(s-t) ≤ z(s)-z(t) ≤ b(s-t)  (stays in cone cone),
     D⁻z(t) > f(t,z(t))  (lower Dini derivative condition)
}

Class ℐ is nonempty (contains z(t) = bt)

Take x(t) = inf{z(t) : z ∈ ℐ}  (pointwise infimum)

This infimum function x:
  - Is absolutely continuous
  - Satisfies ODE exactly: Dx(t) = f(t,x(t))
  - Is minimal (smallest function in class)
```

**Why this works:**
```
Classical approach: Find z satisfying ODE
Comparison approach: Define class of functions ABOVE solution
Take infimum to get solution itself

Elegant: Turns existence into optimization problem
```

---

## COMPLETE POSITION IN FRAMEWORK

**Hassan's role: Alternative rigorous theory for discontinuous scalar ODEs**

```
Theoretical Foundations
    ├─ Cooper (Distributions)
    └─ Graef (Multi-valued, Filippov) ← Main framework
         ↓
Alternative Approaches
    ├─ Hassan (Angular continuity) ← HERE
    ├─ Brogliato (Measure theory)
    └─ Dishliev (Asymptotic analysis)
```

---

## SUMMARY

**Hassan & Rzymowski's contribution is uniquely elegant for scalar discontinuous ODEs** because:

✓ **Angular continuity** — Weaker than standard continuity, still sufficient  
✓ **Single-valued solutions** — Not multi-valued like Filippov  
✓ **Right-hand derivative** — Sufficient for forward-time analysis  
✓ **Geometric intuition** — Directional continuity along cone is visual  
✓ **Elementary proof technique** — Dini derivatives + inf over comparison class  
✓ **Elegant existence theorem** — From optimization principle  
✓ **Autonomous systems** — Extension to ℝ² via coordinate transformation  
✓ **Historical context** — Answer to Peetre-Persson's question via Lakshmikantham  

**Why Hassan matters for discontinuous systems:**

Hassan & Rzymowski provide an **alternative to Filippov's approach** that:
1. Avoids multivalued complexity
2. Works with weaker continuity assumptions
3. Uses elegant comparison class technique
4. Answers fundamental existence question for discontinuous ODEs

**Comparison:**
- **Graef**: General, powerful, comprehensive (Filippov approach)
- **Hassan**: Specialized, elegant, geometric (angular continuity approach)

For the **scalar discontinuous ODE case**, Hassan's approach is often simpler and more intuitive than Filippov's multivalued regularization.

**Critical insight from paper:**
The existence of solutions to x' = f(t,x) with discontinuous f doesn't require f to be nearly continuous everywhere. It suffices that f is "angularly continuous"—continuous along the natural direction determined by the solution itself. This is a profound relaxation of standard continuity requirements.
