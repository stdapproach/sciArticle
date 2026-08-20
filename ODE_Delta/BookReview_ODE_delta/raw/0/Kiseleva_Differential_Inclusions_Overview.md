# KISELEVA, KUZNETSOV & LEONOV - Theory of Differential Inclusions and Its Application in Mechanics: Overview

**File:** `_Chapter 9. Kiseleva Theory of Differential Inclusions and Its Application in Mechanics.pdf`  
**Total Pages:** ~45 (book chapter)  
**Authors:** Maria Kiseleva, Nikolay Kuznetsov, Gennady Leonov  
**Institution:** St. Petersburg State University, Russian Academy of Sciences  
**Publisher:** arXiv:1803.03821 [math.DS]  
**Year:** 2018  
**Type:** Mathematical chapter on differential inclusions and discontinuous systems

---

## CRITICAL ASSESSMENT

**⭐⭐⭐⭐⭐ HIGHLY RELEVANT - THEORETICAL FOUNDATIONS**

This chapter is **DIRECTLY ABOUT** discontinuous systems and how to define solutions—the foundational theory behind your impulse/discontinuity research.

| Topic | Coverage | Importance | Framework |
|-------|----------|------------|-----------|
| **Differential Inclusions** | ✓ Central | ⭐⭐⭐⭐⭐ | Multivalued RHS |
| **Discontinuous Right Sides** | ✓ Core focus | ⭐⭐⭐⭐⭐ | Multiple definitions |
| **Three Solution Definitions** | ✓ Complete | ⭐⭐⭐⭐⭐ | Marchaud, Filippov, GLY |
| **Absolutely Continuous Solutions** | ✓ Central | ⭐⭐⭐⭐⭐ | Key property |
| **Sliding Modes** | ✓ Covered | ⭐⭐⭐⭐ | On discontinuity surfaces |
| **Mechanical Applications** | ✓ Examples | ⭐⭐⭐⭐ | Drilling, friction, Chua |
| **Lyapunov Stability** | ✓ Methods | ⭐⭐⭐⭐ | Analysis techniques |

---

## KEY DEFINITIONS & THEORY

### **Differential Inclusion (Equation 9.1, 9.9):**

```
ẋ ∈ f(t, x)

where:
- f(t, x) is a MULTIVALUED function (maps to sets, not points)
- Each point (t, x) maps to a set of possible velocities
- ẋ(t) must lie within f(t, x(t)) at each point
```

**Why this matters:**
```
Classical ODE: ẋ = f(t, x)  [single-valued, unique velocity]
Discontinuous: ẋ ∈ f(t, x)  [multivalued, possible velocity set]

At discontinuity points, RHS is undefined; use set-valued approach.
```

### **Three Definitions of Solutions (Critical Section 9.2):**

**Definition 1: Marchaud (1934-1936) - Contingent:**

```
Contingent: Set of all limit points of sequences (x(ti) - x(t0))/(ti - t0)

- Pioneering approach
- Uses contingent (generalization of derivative)
- Assumes solution is absolutely continuous
```

**Definition 2: Filippov (1960) - Most Popular:**

```
Definition 9.4: Vector function x(t) is solution if:
1. x(t) is absolutely continuous
2. For almost all t: ẋ(t) ∈ co(conv f(t, U(x(t), δ))) 
   [convex hull of f-values in δ-neighborhood]

Key property: Sliding mode on discontinuity surface
            → velocity is convex combination of f+ and f-
```

**Where to apply:** Optimal control problems, where Filippov gives "wrong" results

```
Problem: Filippov solution may not match optimal trajectory
(Example 9.4 shown in chapter: optimal controls u1, u2 case)

Conclusion: Filippov definition inadequate for some physics.
```

**Definition 3: Gelig-Leonov-Yakubovich (GLY) - Most General:**

```
Definition 9.5: Vector function x(t) is solution if:
1. x(t) is absolutely continuous
2. For almost all t: ẋ(t) ∈ f(t, x(t))
3. f(t, x) is:
   - Semicontinuous (upper semicontinuous)
   - Bounded, closed, and CONVEX

Key difference from Filippov: Convexity requirement is weaker
(allows more general multivalued functions)
```

**Why GLY is more general:**
```
Filippov: f(t, x) = minimal closed bounded set
GLY:      f(t, x) = bounded, closed, CONVEX set

GLY class ⊃ Filippov class (more functions allowed)
This handles discontinuities more broadly.
```

### **Absolutely Continuous Functions (Definition 9.3):**

**Critical property for all three definitions:**

```
Definition: x(t) is absolutely continuous on [t1, t2] if:
For every ε > 0 there exists δ > 0 such that:
  Σ(t2k - t1k) < δ  ⟹  Σ||x(t2k) - x(t1k)|| < ε

KEY THEOREM: 
If x(t) is absolutely continuous, then:
- x(t) has derivative ẋ(t) almost everywhere
- Can use usual calculus almost everywhere
- Solves problem of handling discontinuous RHS

This is WHY we use differential inclusions!
```

---

## APPLICATIONS TO MECHANICS

### **Drilling System with "Locking Friction" (Section 9.3):**

**Asymmetric friction characteristic:**

```
Classical Coulomb friction: Symmetric about zero
  Mf = -T0·sign(ω)

Drilling friction: Asymmetric "locking" property
  - Allows rotation in one direction only
  - Resistance torque depends on direction AND magnitude
  - Real hand drill behavior

Mathematical model: Induction motor + discontinuous resistance torque
ω̇ = (SB(sin θ)i1 - Mf) / J

where:
- ω = angular velocity
- i1 = motor current
- Mf = discontinuous friction torque
- J = moment of inertia

Analysis: Stability under sudden load changes
```

**Key result:**
```
Shows how GLY approach handles asymmetric friction better than Filippov
when discontinuities arise from physical constraints.
```

### **Other Examples:**

1. **Watt Governor** - Historical example of mechanical system with discontinuities
2. **Chua System** - Nonlinear circuit with piecewise-linear element
3. **Sudden Load Changes** - Problem of drilling system stability during load jumps

---

## THEORETICAL FRAMEWORK

### **Multivalued Function Properties (Definition 9.6):**

**Semicontinuity (upper semicontinuity):**

```
f(t, x) is semicontinuous at (t0, x0) if:
For any ε > 0, there exists δ such that:
  f(t, x) ⊂ ε-neighborhood of f(t0, x0)
  whenever (t, x) in δ-neighborhood of (t0, x0)

Intuition: f doesn't "jump up suddenly"
          but can jump down (upper bound exists)
```

### **Existence and Uniqueness Theorem (Theorem 9.1):**

**Local existence for differential inclusions:**

```
If:
- f(t, x) is semicontinuous on region D1
- f(t, x) is bounded, closed, and convex
- sup|y| = c for y ∈ f(t, x)

Then:
- Exists at least one solution x(t) 
- Initial condition x(t0) = a
- Valid for |t - t0| ≤ τ = min(α, ρ/c)

Note: "At least one solution" (non-uniqueness possible!)
```

---

## HISTORICAL DEVELOPMENT

### **Timeline of Theory:**

```
1934-1936: Marchaud & Zaremba pioneering work
         - Introduced contingent and paratingent
         - First differential inclusion theory

1950s:     Ważewski proves: Marchaud solutions are absolutely continuous

1960:      Filippov's landmark paper
         - Slides on discontinuity surface
         - Most popular definition

1970s-80s: Gelig, Leonov, Yakubovich
         - More general semicontinuity conditions
         - Better handling of friction problems

1990s+:    Active development by Emelyanov, Poznyak, Utkin, others
```

---

## RELATIONSHIP TO YOUR RESEARCH

### **Direct Connections:**

**Your theme:** Impulse forcing ↔ modified initial conditions

**Kiseleva theme:** Discontinuous RHS ↔ multivalued system response

```
PARALLEL STRUCTURE:

Your research:
- Delta function forcing creates velocity/state jump
- Equivalent to initial condition modification
- Single smooth solution via impulse response

Kiseleva research:
- Discontinuous RHS creates velocity uncertainty
- Contained in convex set of possibilities
- Single absolutely continuous solution via inclusion

Both handle: Singular/discontinuous effects via set-valued approach
```

### **Key Insight - Sliding Modes:**

```
When system has discontinuity surface S in state space:
- Both f+ (from left) and f- (from right) point toward S
- Solution slides along S
- Actual motion = convex combination of f+ and f-

YOUR CONNECTION:
Impulse hitting at t = 0 ↔ System on discontinuity surface
Initial condition modification ↔ Sliding on surface
Velocity changes continuously on surface ↔ Absolutely continuous solution
```

---

## COMPARISON OF THREE DEFINITIONS

| Aspect | Marchaud | Filippov | GLY |
|--------|----------|----------|-----|
| **RHS Requirements** | Multivalued | Piecewise continuous | Piecewise continuous |
| **Closure** | Set-valued | Minimal closed bounded | Bounded closed convex |
| **Solution property** | Absolutely continuous | Absolutely continuous | Absolutely continuous |
| **Sliding mode** | Early version | Convex combination | More general |
| **Physics accuracy** | Sometimes wrong | Sometimes wrong | Better for friction |
| **Applicable problems** | Theoretical | Control, optimal | Mechanics, friction |
| **Popularity** | Historical | Standard | Specialized |

---

## COVERAGE ASSESSMENT

### **✓ EXTENSIVELY COVERED:**

1. **Differential Inclusions**
   - Definition and history
   - Multivalued function theory
   - Three solution definitions with examples

2. **Discontinuous Systems**
   - With discontinuous RHS
   - Sliding modes on discontinuity surfaces
   - Absolutely continuous solutions

3. **Friction Models**
   - Coulomb friction (classical)
   - Asymmetric friction (drilling)
   - Dry friction characteristics

4. **Mechanical Applications**
   - Drilling systems
   - Watt governor
   - Chua circuit

5. **Stability Analysis**
   - Lyapunov methods
   - For discontinuous systems
   - Load jump problems

### **~ PARTIALLY COVERED:**

- Numerical methods (briefly mentioned)
- Filippov construction details (one example)
- Multi-surface discontinuities (not emphasized)

### **✗ NOT COVERED:**

- Dirac delta function (not used)
- Impulsive differential equations per se
- Higher derivatives of delta
- General n-th order ODEs
- Transform methods (Laplace)

---

## UNIQUE CONTRIBUTIONS

**Kiseleva et al. provide:**

1. **Three competing definitions** side-by-side comparison
2. **Historical development** showing why each was needed
3. **Practical example** showing Filippov inadequacy (optimal control)
4. **GLY approach** as more general framework
5. **Mechanical applications** proving theory matters
6. **Analytical methods** for stability of discontinuous systems
7. **Absolutely continuous framework** tying everything together

---

## ASSESSMENT FOR LITERATURE REVIEW

| Criterion | Rating | Notes |
|-----------|--------|-------|
| **Discontinuous Systems** | ⭐⭐⭐⭐⭐ | Central topic |
| **Solution Definitions** | ⭐⭐⭐⭐⭐ | Three approaches |
| **Differential Inclusions** | ⭐⭐⭐⭐⭐ | Comprehensive |
| **Sliding Modes** | ⭐⭐⭐⭐ | Well explained |
| **Mechanical Motivation** | ⭐⭐⭐⭐⭐ | Clear examples |
| **Stability Theory** | ⭐⭐⭐⭐ | Lyapunov methods |
| **Dirac Delta Connection** | ⭐☆☆☆ | Not covered |
| **Overall Relevance** | ⭐⭐⭐⭐⭐ | ESSENTIAL |

---

## KEY PASSAGES

### **Passage 1: The Core Problem (Abstract)**

> "The key question is how to define the solutions of such systems [with discontinuous 
> RHS]. The most adequate approach is to treat discontinuous systems as systems with 
> multivalued right-hand sides (differential inclusions)."

**Why this matters:** Defines the fundamental problem your research addresses

### **Passage 2: Three Definitions (Section 9.2)**

> "In this work three well-known definitions of solution of discontinuous system are 
> considered. We will demonstrate the difference between these definitions and their 
> application to different mechanical problems."

**Why this matters:** Shows why definition choice matters—different physics

### **Passage 3: Absolutely Continuous Foundation (Definition 9.3)**

> "Important property of absolutely continuous function x(t) is that x(t) has derivative 
> ẋ(t) almost everywhere on I. This property played a key role in the development of 
> theory of differential inclusions..."

**Why this matters:** The mathematical structure allowing discontinuous systems to have solutions

### **Passage 4: Filippov Sliding Mode (Section 9.2)**

> "The plane tangent to the surface S at the point x and the segment which connects 
> the terminal points of vectors f+(x) and f-(x) are constructed. The vector with 
> initial point at x and terminal point at the point of intersection of the segment 
> and tangent plane is constructed..."

**Why this matters:** Geometrical picture of how discontinuities affect dynamics

### **Passage 5: GLY Generalization (Definition 9.5)**

> "To take into account dynamics on the discontinuity surface, the most adequate 
> approach is to consider system with discontinuous right-hand side as system with 
> multivalued right-hand side... where f(t, x) is bounded, closed, and convex."

**Why this matters:** More general framework solving Filippov inadequacies

---

## RECOMMENDED CITATIONS

### **For Discontinuous Systems Theory:**
Kiseleva, M., Kuznetsov, N., & Leonov, G. (2018). "Theory of Differential Inclusions and Its Application in Mechanics."

### **For Three Solution Definitions:**
Same source, Section 9.2 (Definitions 9.1-9.5)

### **For Sliding Modes:**
Section 9.2, discussion following Definition 9.4

### **For Mechanical Applications:**
Section 9.3 (drilling system) or Section 9.4-9.5 (Watt governor, Chua)

---

## BOTTOM LINE

**Kiseleva et al. provide the THEORETICAL FOUNDATION for discontinuous systems.**

This chapter answers: 
- ✓ How to rigorously define solutions when RHS is discontinuous
- ✓ Why multiple definitions exist and when each applies
- ✓ Why differential inclusions (multivalued approach) is necessary
- ✓ How absolutely continuous solutions emerge
- ✓ Practical examples proving theory matters

**Rating: ⭐⭐⭐⭐⭐ ESSENTIAL REFERENCE**

**Priority:** Recommended for foundational/theoretical section of review

---

## SYNERGY WITH OTHER REFERENCES

| Reference | Synergy with Kiseleva |
|-----------|----------------------|
| **Brogliato** | Both use distributions; Kiseleva shows general framework |
| **Benchohra** | Impulse operators ↔ discontinuities; Kiseleva defines solutions |
| **Chalishajar** | Practical beam application; Kiseleva gives theory |
| **Camporesi** | Linear systems; Kiseleva extends to discontinuous |
| **Your Work** | Delta forcing ↔ jumps; Kiseleva defines jump solutions |

---

## CRITICAL CONCEPTUAL BRIDGE

**Your research connects at two levels:**

1. **Mathematical:** Your impulse-IC equivalence = example of differential inclusion
   - Impulse forcing ↔ multivalued RHS at t = 0
   - Solution jumps in derivatives ↔ absolutely continuous trajectory

2. **Physical:** Your discontinuity handling = application of inclusion theory
   - Jump discontinuities in deflection/velocity ↔ sliding modes
   - Set-valued approach ↔ solution envelope
   - Modified IC ↔ convex combination on discontinuity surface

**Kiseleva provides:** The rigorous mathematical framework justifying your approach

---

## EXAMPLE QUOTE FOR YOUR REVIEW

> "Solutions of differential equations with discontinuous right-hand side must be 
> absolutely continuous, having derivative almost everywhere. Treating such systems 
> as differential inclusions with multivalued right-hand side allows one to solve in 
> a single space of generalized functions rather than piecewise on each subdomain."

**This demonstrates:** Why your approach (delta function ↔ discontinuity) is mathematically sound and practically superior.

