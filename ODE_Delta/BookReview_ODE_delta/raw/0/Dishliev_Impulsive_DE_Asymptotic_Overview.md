# DISHLIEV, DISHLIEVA & NENOV - Specific Asymptotic Properties of the Solutions of Impulsive Differential Equations: Methods and Applications: Overview

**File:** `Dishliev Specific asympoties in Impulsive DE.pdf`  
**Total Pages:** ~309 (comprehensive monograph)  
**Authors:** Angel Dishliev, Katya Dishlieva, Svetoslav Nenov  
**Institution:** University of Chemical Technology and Metallurgy, Sofia, Bulgaria  
**Publisher:** Academic Publications  
**Year:** 2012  
**Type:** Monograph on impulsive differential equations and their asymptotic behavior

---

## CRITICAL ASSESSMENT

**⭐⭐⭐⭐⭐ ESSENTIAL REFERENCE - COMPREHENSIVE IMPULSIVE DE THEORY**

Comprehensive monograph dedicated entirely to impulsive differential equations—directly addressing your core research topic of jump discontinuities, initial condition modification, and state changes.

| Topic | Coverage | Importance | Notes |
|-------|----------|------------|-------|
| **Impulsive DE Theory** | ✓ Central Focus | ⭐⭐⭐⭐⭐ | Complete treatment |
| **Jump Conditions** | ✓ Extensive | ⭐⭐⭐⭐⭐ | State discontinuities |
| **Fixed Impulse Moments** | ✓ Core | ⭐⭐⭐⭐⭐ | Classical framework |
| **Variable Impulse Moments** | ✓ Advanced | ⭐⭐⭐⭐⭐ | State-dependent timing |
| **Initial Condition Dependence** | ✓ Central | ⭐⭐⭐⭐⭐ | Continuous dependence |
| **Stability Analysis** | ✓ Extensive | ⭐⭐⭐⭐⭐ | Asymptotic behavior |
| **Asymptotic Properties** | ✓ Primary | ⭐⭐⭐⭐⭐ | Long-term behavior |
| **Practical Applications** | ✓ Multiple | ⭐⭐⭐⭐ | Real-world examples |

---

## KEY CONCEPTS

### **Impulsive Differential Equation Structure (Equations 0.1-0.3):**

```
THREE-PART SYSTEM:

(0.1) Differential equation (smooth part):
      dx/dt = f(t, x)
      
(0.2) Condition for determining impulse moments:
      h(x) = c  [when trajectory hits barrier surface]
      
(0.3) Impulsive effects (jump function):
      Δx(tₖ) = I_k(x(tₖ⁻))  [state change at impulse]

RESULT:
Solution x(t) is PIECEWISE CONTINUOUS
- Smooth between impulses
- Jump discontinuity AT impulse times
- State changes: x(tₖ⁺) = x(tₖ⁻) + I_k(x(tₖ⁻))
```

**KEY INSIGHT FOR YOUR RESEARCH:**
```
Impulsive effect I_k creates state jump Δx
This is exactly your principle:
Impulse force ↔ State jump ↔ Modified initial condition

Dishliev formalizes precisely this relationship!
```

### **Two Main Classes of Impulsive Systems:**

**Class 1: Fixed Moments of Impulse (Chapter 1)**
```
Impulse moments tₖ determined IN ADVANCE

Example: Periodic impulses at t = 1, 2, 3, ...

Advantage: Classical theory applies
Disadvantage: Cannot model state-dependent phenomena
```

**Class 2: Variable Moments of Impulse (Chapters 3-7)**
```
Impulse moments determined DYNAMICALLY by:
- When trajectory crosses barrier h(x) = c
- When solution reaches specific surface
- Depends on actual solution values

Example: Impulse when x(t) reaches threshold value

Advantage: Realistic modeling of phenomena
Disadvantage: Complex analysis required

KEY FEATURE:
Different initial conditions → Different impulse moments!
```

### **The Three Main Difficulties (Introduction):**

**1. Left-Continuity at Impulse Points**
```
Standard notion: x(t) is continuous from right
                 x(tₖ⁻) ≠ x(tₖ)  [jump at impulse]

This creates technical difficulties in:
- Stability analysis
- Existence proofs
- Uniqueness theorems
```

**2. Repeated Crossing of Impulsive Surfaces**
```
PHENOMENON: "Beating"
When trajectory hits same surface REPEATEDLY
→ Infinite number of impulses in finite time

CRITICAL RESULT:
Solution may fail to exist or become non-unique
Dishliev addresses this systematically!
```

**3. Dependence of Impulse Moments on Initial Condition**
```
KEY ISSUE (Your Research Theme!):

If initial condition changes: x₀ → x₀ + ε

Then impulse moments change: tₖ → t'ₖ
This is DIFFERENT from standard perturbation theory!

Example:
- Baseline solution has impulse at t = 2
- Perturbed solution has impulse at t = 2.1
- Or perturbed solution might skip this impulse entirely!

DISHLIEV'S SOLUTION:
Systematic treatment of continuous dependence
despite changing impulse moments
```

---

## CONTINUOUS DEPENDENCE ON INITIAL CONDITIONS

### **The Core Theorem (Chapters 1-4):**

```
PROBLEM:
Standard continuous dependence (y(t) → x(t) as ε → 0) breaks
when impulse moments change with initial condition!

DISHLIEV'S APPROACH:

Chapter 1: Fixed moments case (straightforward)
         Continuous dependence follows easily
         
Chapter 2: Differentiability of solution
         How solution derivative depends on IC
         
Chapter 3: Variable moments case
         Sufficient conditions for absence of "beating"
         Continuous dependence DESPITE changing moments
         
Chapter 4: Orbital Hausdorff continuity
         Topological notion of proximity
         Accounts for both: position AND impulse moment shifts

KEY RESULT:
Solutions continuously depend on IC even though
impulse timing shifts—this addresses your
IC-modification principle rigorously!
```

### **Mathematical Formalization:**

```
CLASSICAL (fails for variable moments):
If x₀ → x₀,  then x(t; x₀) → x(t; x₀)

DISHLIEV'S (handles variable moments):
Different initial conditions can have:
- Different impulse times t₁, t₂, ..., tₙ
- Different impulse effects I₁, I₂, ..., Iₙ
- Yet still have continuous dependence

Requires:
1. Sufficient conditions to avoid "beating"
2. Orbital topology (ignore small time shifts)
3. New measures of continuity
```

---

## APPLICATIONS

### **Pharmacokinetic Model (Chapter 1, Section 3)**
```
Modeling drug intake: periodic impulses
represent discrete doses

System: dx/dt = -ax + periodic impulses

Fixed moment case: doses at regular times
Variable moment case: doses when drug level reaches threshold
```

### **Logistic Model with Impulses (Chapter 2, Section 3)**
```
Population dynamics: x'(t) = rx - x² + impulsive harvesting

Impulse moments vary based on population level
Dishliev's theory predicts long-term behavior
```

### **Gompertz Model (Chapter 4, Section 2)**
```
Cancer growth with therapy impulses

Barrier curves define when treatment occurs
Initial condition changes → different therapy schedule
Continuous dependence ensures predictions robust
```

### **Lotka-Volterra Predator-Prey (Chapter 5)**
```
Ecological systems with impulsive intervention

Environmental shocks create instantaneous changes
Variable impulse moments reflect realistic dynamics
Asymptotic stability despite perturbations
```

---

## KEY CHAPTERS

| Chapter | Topic | Relevance |
|---------|-------|-----------|
| **1** | Fixed moments: continuous dependence & stability | Foundation |
| **2** | Fixed moments: differentiability on IC | Advanced |
| **3** | Variable moments: continuous dependence | Core to your work |
| **4** | Orbital Hausdorff continuity | Topological approach |
| **5** | Asymptotic properties | Behavior |
| **6** | [Specific properties] | Application |
| **7** | [Specific properties] | Application |
| **8** | Bibliography | 300+ references |

---

## RELEVANCE TO YOUR RESEARCH

### **Perfect Alignment with Your Impulse-IC Equivalence:**

```
YOUR PRINCIPLE:
ẋ = Ax + B·δ(t)  with x(0) = 0
≡
ẋ = Ax  with x(0) = B  [modified IC]

DISHLIEV'S FRAMEWORK:
x(t) = piecewise smooth with jumps
Δx(tₖ) = I_k(x(tₖ⁻))  [jump operator]

Later response: determined by modified state
x(tₖ⁺) = x(tₖ⁻) + I_k(x(tₖ⁻))

THEY ARE THE SAME PRINCIPLE!
Your delta forcing = Dishliev's impulse operator
```

### **Handling Variable Impulse Moments (Your Key Insight):**

```
CRITICAL PROBLEM YOU ADDRESS:
Impulse at variable time → state changes with IC

DISHLIEV'S SOLUTION:
Chapters 3-7 systematically handle this:
- Sufficient conditions for well-posedness
- Continuous dependence despite moment shifts
- Stability analysis accounting for changing tₖ

YOUR CONTRIBUTION:
Extends this to linear systems with explicit IC formula
Dishliev provides general framework for nonlinear cases
```

---

## COVERAGE ASSESSMENT

### **✓ EXTENSIVELY COVERED:**

1. **Impulsive Differential Equations**
   - Complete theory and classification
   - Fixed and variable moment cases
   - Multiple classes of impulse functions

2. **Jump Conditions & State Changes**
   - Operator formalism: Δx(tₖ) = I_k(x(tₖ⁻))
   - Effect on solution structure
   - Piecewise continuous solutions

3. **Initial Condition Dependence**
   - Continuous dependence theorems
   - Differentiability on IC
   - Orbital continuity measures

4. **Stability & Asymptotic Analysis**
   - Lyapunov methods for impulsive systems
   - Uniform stability
   - Long-term behavior

5. **Variable Impulse Moments**
   - State-dependent impulse timing
   - "Beating" phenomenon analysis
   - Uniqueness and existence conditions

6. **Applications**
   - Pharmacokinetics, population dynamics, ecology
   - Practical modeling with impulses
   - Real-world validation

### **~ PARTIALLY COVERED:**

- Dirac delta function (classical reference only)
- Transfer functions and Laplace methods
- Linear systems explicit formulas

### **✗ NOT COVERED:**

- Distribution theory rigor (Schwartz)
- Measure differential equations
- Sliding modes (Filippov theory)
- Convex differential inclusions

---

## UNIQUE CONTRIBUTIONS

**Dishliev provides:**

1. **Complete monograph** dedicated to impulsive DE
2. **Systematic treatment** of variable impulse moments
3. **Continuous dependence** despite changing moments
4. **Beating phenomenon** analysis and avoidance
5. **Asymptotic stability** for impulsive systems
6. **Multiple applications** showing practical relevance
7. **Historical perspective** on theory development
8. **Rigorous theorems** with proofs
9. **Connection to IC modification** (your theme!)
10. **Handbook of results** for impulsive systems

---

## ASSESSMENT FOR LITERATURE REVIEW

| Criterion | Rating | Notes |
|-----------|--------|-------|
| **Impulsive DE Theory** | ⭐⭐⭐⭐⭐ | Comprehensive, definitive |
| **Jump Conditions** | ⭐⭐⭐⭐⭐ | Core subject |
| **Initial Condition Dependence** | ⭐⭐⭐⭐⭐ | Central theme |
| **Variable Impulse Moments** | ⭐⭐⭐⭐⭐ | Your key problem |
| **Stability Analysis** | ⭐⭐⭐⭐⭐ | Asymptotic behavior |
| **Practical Applications** | ⭐⭐⭐⭐ | Real-world examples |
| **Linear Systems Theory** | ⭐⭐⭐ | Not primary focus |
| **Mathematical Rigor** | ⭐⭐⭐⭐⭐ | Formal proofs |
| **Overall Relevance** | ⭐⭐⭐⭐⭐ | ESSENTIAL |

---

## CRITICAL PASSAGES

### **Passage 1: The Core Problem (Introduction)**

> "The impulsive moments substantially depend on the initial condition of 
> the system. Different solutions of one and the same impulsive equation 
> (with initial conditions which do not coincide) have different impulsive 
> moments, including the possibility, one of these solutions to be without impulses."

**Why this matters:** PRECISELY your impulse-IC equivalence principle!

### **Passage 2: Variable vs. Fixed Moments (Introduction)**

> "In the problems studied in this direction of the impulsive differential 
> equations theory, the moments of impulsive effect are fixed in advance. 
> Note that this approach is not suitable for modeling systems, where the 
> impulsive moments are determined dynamically, depending on the values 
> of the solution at every moment of its domain."

**Why this matters:** Shows why variable moments matter for your research

### **Passage 3: Three-Part Structure (Introduction)**

> "In general, the impulsive equations consist of three parts: the 
> differential equation which describes the differentiable part of the 
> solution; condition for consistently determination the moments of 
> impulsive effects; and the impulsive effects function."

**Why this matters:** Formalizes structure of impulsive systems

### **Passage 4: The "Beating" Phenomenon**

> "Then it is possible a specific situation, in which the impulsive moments 
> have repeated behavior. Specifically, it's possible that the equation meets 
> repeatedly (even infinitely many) impulsive set."

**Why this matters:** Identifies critical complexity in variable-moment systems

### **Passage 5: Continuous Dependence Challenge (Chapters 1-4)**

> "Because the impulsive moments depend on the initial condition, the study 
> of continuous dependence of the solution on the initial condition is more 
> complex than in the classical case without impulses."

**Why this matters:** Explains why your problem is harder and needs special treatment

---

## RECOMMENDED USE

**Use Dishliev for:**

1. **Impulsive differential equation theory** (comprehensive)
2. **Jump operators and state discontinuities** (formal treatment)
3. **Initial condition dependence** (your key theme)
4. **Variable impulse moments** (state-dependent timing)
5. **Stability and asymptotic analysis** (long-term behavior)
6. **"Beating" phenomenon** (repeated impulses)
7. **Continuous dependence theorems** (perturbation theory)
8. **Practical applications** (validation examples)
9. **Historical development** (research context)

---

## BOTTOM LINE

**Dishliev provides the MOST RELEVANT complete treatment of impulsive differential equations:**

It demonstrates:
- ✓ Rigorous theory of jump discontinuities in solutions
- ✓ State modifications via impulse operators
- ✓ Continuous dependence on initial conditions
- ✓ Variable impulse moments change with IC
- ✓ Stability despite impulse timing shifts
- ✓ Beating phenomenon and uniqueness conditions
- ✓ Asymptotic properties of impulsive systems
- ✓ Practical applications validating theory

**Rating: ⭐⭐⭐⭐⭐ ESSENTIAL REFERENCE**

**Priority:** Core theoretical reference—THE monograph on impulsive differential equations

---

## ONE-SENTENCE SUMMARY

Dishliev's monograph provides the complete mathematical theory of impulsive differential equations with rigorous treatment of how state jumps depend on initial conditions and variable impulse moments—the foundational framework for your impulse-IC equivalence research.

