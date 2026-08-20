# DIECI & LOPEZ - Sliding Motion in Filippov Differential Systems: Theoretical Results and Computational Approach: Overview

**File:** `DIECI SLIDING MOTION IN FILIPPOV DIFFERENTIAL SYSTEMS THEORETICAL RESULTS AND A COMPUTATIONAL APPROACH.pdf`  
**Total Pages:** ~40 (journal article)  
**Authors:** Luca Dieci, Luciano Lopez  
**Type:** Theoretical and numerical methods for piecewise-smooth (PWS) systems  
**Topic:** Filippov theory, sliding modes, discontinuous dynamics

---

## CRITICAL ASSESSMENT

**⭐⭐⭐⭐⭐ ESSENTIAL REFERENCE - FILIPPOV THEORY & SLIDING MODES**

This paper directly addresses discontinuous dynamical systems via Filippov theory and sliding modes—the rigorous mathematical framework for your impulse/discontinuity research.

| Topic | Coverage | Importance | Notes |
|-------|----------|------------|-------|
| **Filippov Theory** | ✓ Central | ⭐⭐⭐⭐⭐ | Complete treatment |
| **Discontinuous RHS** | ✓ Core Focus | ⭐⭐⭐⭐⭐ | Piecewise-smooth systems |
| **Convex Differential Inclusion** | ✓ Explicit | ⭐⭐⭐⭐⭐ | Set-valued approach |
| **Sliding Modes** | ✓ Central | ⭐⭐⭐⭐⭐ | Motion on discontinuity |
| **Numerical Methods** | ✓ Extensive | ⭐⭐⭐⭐⭐ | Computational algorithms |
| **Second-Order Corrections** | ✓ Novel | ⭐⭐⭐⭐ | Improvements to theory |
| **Multi-surface Discontinuities** | ✓ Covered | ⭐⭐⭐⭐ | Intersecting surfaces |

---

## KEY CONCEPTS

### **Piecewise-Smooth (PWS) System Definition (Equation 2.1):**

```
x'(t) = f(x(t)) = {  f₁(x(t))  if x ∈ S₁
                  {  f₂(x(t))  if x ∈ S₂

where:
- S₁ = {x | h(x) < 0}  [region 1]
- S₂ = {x | h(x) > 0}  [region 2]
- Σ = {x | h(x) = 0}   [discontinuity surface]

KEY CHALLENGE:
f(x) is undefined on Σ!
Need mathematical framework to extend vector field.
```

### **Filippov Convex Extension (Equations 2.4-2.5):**

```
THE SOLUTION: Convex Differential Inclusion

x'(t) ∈ F(x(t)) = {  f₁(x(t))                    x ∈ S₁
                   {  co{f₁(x), f₂(x)}           x ∈ Σ  ← Convex hull!
                   {  f₂(x(t))                    x ∈ S₂

where co{f₁, f₂} = {(1-α)f₁ + αf₂ : α ∈ [0,1]}

KEY INSIGHT:
On discontinuity surface Σ, solution can take ANY
direction in the convex hull of boundary values.
This generalizes single-valued systems!
```

### **Filippov First-Order Theory (Equations 2.6-2.10):**

**Let n = normal to surface Σ, and Aᵢ = nᵀfᵢ (component normal to Σ)**

**Case (a): Transversal Intersection**
```
Condition: A₁ · A₂ > 0  [same sign]
Result: Trajectory CROSSES discontinuity surface
        Continues smoothly on other side
Uniqueness: YES
```

**Case (b): Sliding Mode (Attracting)**
```
Condition: A₁ · A₂ < 0  [opposite signs]
           Specifically: A₁ > 0, A₂ < 0

Result: Trajectory STAYS ON Σ
        Moves along surface in sliding mode
        
Sliding velocity (Equation 2.9-2.10):
fF(x) = (1-α(x))f₁ + α(x)f₂

where α is chosen so nᵀfF = 0
(velocity tangent to discontinuity surface)

Uniqueness: YES (attractive sliding)
```

**Case (c): Repulsive Sliding (Not Covered Here)**
```
Condition: A₁ < 0, A₂ > 0  [opposite signs, repulsive]

Result: Ill-posed problem—non-uniqueness
        (not addressed by Dieci)
```

---

## DIECI'S CONTRIBUTIONS: Second-Order Corrections

### **Problem with First-Order Filippov Theory:**

```
WHEN IT FAILS:
1. Sliding on intersection of multiple surfaces
   (not properly defined in classic theory)
2. When first-order conditions violated
   (A₁ = 0, A₂ ≠ 0, or A₁ ≠ 0, A₂ = 0)

DIECI'S SOLUTION:
Propose second-order corrections to Filippov theory
- Reinterpret 1st order theory
- Provide systematic definition on multi-surface intersections
- Ensure well-posed problem when conditions change
```

### **Key Practical Concern:**

```
ISSUE:
Filippov extension not uniquely defined when:
- Trajectory exits one sliding mode
- Must transition to another sliding mode
- Conditions (2.8) no longer satisfied

DIECI'S APPROACH:
Second-order analysis to determine:
- Which mode to enter next
- How to extend definitions consistently
- When ill-posedness occurs
```

---

## NUMERICAL METHOD

### **Computational Challenge:**

```
PROBLEM:
Numerical methods often "miss" sliding surface
- Integration passes through Σ without detecting slide
- Solution becomes inaccurate
- Need special handling of discontinuities

DIECI'S ADVANTAGE:
"A main feature of our numerical approach is its ability 
to reach the sliding surface(s) from one side only."

Specifically detects and handles sliding events
```

### **Algorithm Features:**

```
1. Event Detection
   - Identify when trajectory reaches Σ
   - Determine transversal vs. sliding

2. Sliding Mode Handling
   - Project onto discontinuity surface
   - Use Filippov extension to compute velocity
   - Stay ON surface (don't cross)

3. Multi-surface Transitions
   - Handle when sliding moves to intersection
   - Apply second-order corrections as needed
```

---

## RELEVANCE TO YOUR RESEARCH

### **Direct Parallels:**

**Your Theme:**
```
Impulse forcing ↔ Velocity jump ↔ Modified IC
Delta function creates state discontinuity
```

**Dieci's Theme:**
```
Discontinuous RHS ↔ Sliding mode on surface
Convex hull of boundary values determines motion
Trajectory discontinuous in velocity (continuous position)
```

### **Mathematical Parallel:**

```
YOUR STRUCTURE:
ẋ = Ax + B·δ(t)
    ↓
Creates jump: ẋ(0⁺) ≠ ẋ(0⁻)
Position continuous: x(0⁺) = x(0⁻)

DIECI'S STRUCTURE:
ẋ ∈ co{f₁, f₂}  when on Σ
  ↓
Velocity from convex combination of f₁, f₂
Position continuous along Σ (sliding mode)

INSIGHT:
Both use convex structures to handle discontinuities!
Both keep position continuous, velocity discontinuous!
```

### **Key Connection - Convex Hull as Impulse Response:**

```
Dieci: On discontinuity, velocity ∈ co{f₁, f₂}
       This is the SET of possible responses

Your principle: Impulse creates JUMP in velocity
               Which is ONE POINT on boundary

Filippov convex hull = SET including your impulse response!
```

---

## COVERAGE ASSESSMENT

### **✓ EXTENSIVELY COVERED:**

1. **Filippov Theory**
   - Classical first-order theory
   - Transversal vs. sliding classification
   - Convex differential inclusion formulation

2. **Sliding Modes**
   - Definition and properties
   - Attracting sliding motion
   - Vector field on discontinuity

3. **Discontinuous Systems**
   - Piecewise-smooth (PWS) systems
   - Multiple discontinuity surfaces
   - Switching dynamics

4. **Theoretical Issues**
   - Non-uniqueness (repulsive case)
   - Multi-surface intersections
   - Second-order corrections

5. **Numerical Methods**
   - Event detection algorithms
   - Sliding mode computation
   - Handling transitions

### **~ PARTIALLY COVERED:**

- Stability analysis of sliding modes
- Bifurcations at discontinuities
- Applications (mentioned but not detailed)

### **✗ NOT COVERED:**

- Dirac delta function formally
- Measure theory rigor
- Impulsive differential equations (jump-type)
- Distribution theory
- Laplace transforms

---

## UNIQUE CONTRIBUTIONS

**Dieci & Lopez provide:**

1. **Clear exposition** of Filippov theory
2. **Second-order corrections** to classical theory
3. **Systematic treatment** of multi-surface intersections
4. **Numerical algorithm** for PWS systems
5. **Rigorous sliding mode** analysis
6. **Event detection** and handling
7. **Practical implementation** guidance
8. **Examples** showing various cases

---

## ASSESSMENT FOR LITERATURE REVIEW

| Criterion | Rating | Notes |
|-----------|--------|-------|
| **Filippov Theory** | ⭐⭐⭐⭐⭐ | Complete exposition |
| **Sliding Modes** | ⭐⭐⭐⭐⭐ | Central to paper |
| **Discontinuous RHS** | ⭐⭐⭐⭐⭐ | Core topic |
| **Convex Inclusions** | ⭐⭐⭐⭐⭐ | Rigorous treatment |
| **Second-Order Theory** | ⭐⭐⭐⭐ | Novel contributions |
| **Numerical Methods** | ⭐⭐⭐⭐⭐ | Practical algorithms |
| **Multi-surface Cases** | ⭐⭐⭐⭐ | Important extension |
| **Mathematical Rigor** | ⭐⭐⭐⭐⭐ | Formal definitions |
| **Overall Relevance** | ⭐⭐⭐⭐⭐ | ESSENTIAL |

---

## CRITICAL PASSAGES

### **Passage 1: PWS System Definition (Section 1)**

> "Differential equations with discontinuous right-hand side of Filippov type... 
> the right-hand side (the vector field) varies discontinuously as the solution 
> trajectory reaches one or more surfaces, called discontinuity or switching 
> surfaces."

**Why this matters:** Defines the class of systems you're studying

### **Passage 2: The Core Problem (Section 1)**

> "The vector field f(x) is not defined if x(t) is on Σ. There is freedom on 
> how to extend the vector field on Σ, and the way that this freedom is 
> resolved must ultimately be weighted against our ability to model situations 
> of practical interest."

**Why this matters:** Explains why Filippov extension is necessary—your situation exactly!

### **Passage 3: Filippov's Solution (Equation 2.4-2.5)**

> "The extension (or convexification) of a discontinuous system into a convex 
> differential inclusion is known as Filippov convex method."

**Why this matters:** The mathematical tool for handling discontinuities rigorously

### **Passage 4: Sliding Mode (Equation 2.9-2.10)**

> "During the sliding motion the solution will continue along Σ with time 
> derivative fF given by fF(x) = (1-α(x))f₁ + α(x)f₂, where α(x) is chosen 
> so that the velocity lies in the tangent plane (n^T fF = 0)."

**Why this matters:** Shows how motion determined on discontinuity surface

### **Passage 5: Dieci's Motivation (Section 1)**

> "Precisely these two points, sliding on intersection of several surfaces and 
> violation of the first order Filippov theory, have motivated our work, whose 
> main goals are: to reinterpret the 1st order theory of Filippov and to 
> propose second order corrections."

**Why this matters:** Shows limitations of classical theory motivating extensions

---

## RECOMMENDED USE

**Use Dieci for:**

1. **Filippov theory exposition** (clear, rigorous)
2. **Sliding mode mathematics** (complete treatment)
3. **Convex differential inclusions** (set-valued framework)
4. **Discontinuous RHS handling** (theoretical foundation)
5. **Numerical algorithms** (practical implementation)
6. **Second-order corrections** (extensions to theory)
7. **Multi-surface discontinuities** (complex cases)
8. **Event detection** (computational techniques)

---

## BOTTOM LINE

**Dieci & Lopez provide RIGOROUS THEORETICAL FOUNDATION for discontinuous systems:**

It demonstrates:
- ✓ Filippov convex extension handles discontinuous RHS
- ✓ Sliding modes keep position continuous, velocity discontinuous
- ✓ Convex hull of boundary values determines motion on surface
- ✓ Set-valued framework generalizes single-valued systems
- ✓ Second-order corrections extend theory to complex cases
- ✓ Numerical methods can reliably detect and track discontinuities
- ✓ Multi-surface intersections require careful theoretical treatment

**Rating: ⭐⭐⭐⭐⭐ ESSENTIAL REFERENCE**

**Priority:** Core theoretical reference for Filippov systems and sliding modes

---

## SYNERGY WITH YOUR RESEARCH

**Your impulse-IC equivalence principle** fits naturally into Filippov framework:

```
Your approach: Delta forcing → velocity jump → modified IC
Dieci's approach: Discontinuous RHS → sliding mode → convex velocity set

Both:
- Keep position continuous
- Allow velocity discontinuity
- Use mathematical framework to extend RHS
- Deterministic despite discontinuity
```

---

## ONE-SENTENCE SUMMARY

Dieci & Lopez provide rigorous Filippov theory showing that discontinuous right-hand sides define motion via convex differential inclusions where trajectories stay continuous but velocities may jump—the complete mathematical framework for your impulse/discontinuity equivalence principle.

