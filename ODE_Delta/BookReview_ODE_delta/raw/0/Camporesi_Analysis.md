# Camporesi: An Introduction to Linear ODEs with Constant Coefficients Using the Impulsive Response Method

## Reference
**Paper**: An Introduction to Linear Ordinary Differential Equations with Constant Coefficients Using the Impulsive Response Method and Factorization  
**Author**: Roberto Camporesi (Politecnico di Torino)  
**Date**: June 4, 2019  
**Key Feature**: Elementary presentation avoiding distribution theory, Laplace transform, and linear systems theory

---

## Central Concept: The Impulsive Response

### Definition

The **impulsive response** g(x) is the unique solution of the homogeneous differential equation with **special initial conditions**:

**For First-Order System (n=1):**
```
y' - λy = 0
y(0) = 1
```
Solution: **g(x) = e^(λx)**

**For Second-Order System (n=2):**
```
y'' + ay' + by = 0
y(0) = 0,  y'(0) = 1     ← KEY: Zero position, unit velocity jump
```

Solution obtained from integration:
```
         1          λ₁x    λ₂x
g(x) = ―――― (e    - e    )   if λ₁ ≠ λ₂  (Case 1)
       λ₁-λ₂

g(x) = x e^(λx)            if λ₁ = λ₂   (Case 2)
```

**General Pattern (n-th Order):**
```
y^(n) + a₁y^(n-1) + ... + aₙy = 0
y(0) = 0, y'(0) = 0, ..., y^(n-2)(0) = 0, y^(n-1)(0) = 1
```

---

## **KEY EQUIVALENCE: Impulsive Response ↔ Initial Velocity Jump**

### The Fundamental Decomposition (Theorems 3.1-3.2)

For the **non-homogeneous equation**:
```
y'' + ay' + by = f(x)
y(x₀) = y₀,  y'(x₀) = y₀'
```

**General Solution (Theorem 3.3, Equation 3.28):**
```
              ∫ˣ
y(x) =        g(x-t)f(t)dt  + (y₀' + ay₀)g(x-x₀) + y₀g'(x-x₀)
              x₀
              \_____________  ____________________  ________________/
                 particular      homogeneous part (IVP with y₀, y₀')
                 solution
```

**Crucially**: The particular solution comes from convolving the input f(t) with the **impulsive response g(x)**, which is defined with **unit velocity jump initial condition**.

### The Decomposition Explained

**Part 1: Particular Solution (with zero initial conditions)**
```
           ∫ˣ
yₚ(x) =    g(x-t)f(t)dt
           x₀

where:  yₚ(x₀) = 0,  y'ₚ(x₀) = 0
```

This solves the **non-homogeneous equation with zero initial conditions**.

**Part 2: Homogeneous Solution (free vibration)**
```
yₕ(x) = (y₀' + ay₀)g(x-x₀) + y₀g'(x-x₀)

where: yₕ(x₀) = y₀,  y'ₕ(x₀) = y₀'
```

This is the **free vibration** (homogeneous equation) with the **given initial conditions**.

### The Bridge to Initial Conditions

**Key insight from Theorem 3.1 and 3.2:**

The impulsive response g(x) has the property:
```
g(0) = 0          ← position is CONTINUOUS at initial "impulse"
g'(0) = 1         ← velocity JUMPS by amount 1
```

Therefore:
- **Convolving with g** captures the system's response to discontinuous velocity conditions
- The coefficients (y₀' + ay₀) and y₀ in front of g(x) and g'(x) encode the **initial velocity and position**
- The solution structure reflects: **smooth forced response + free vibration from jumped initial state**

---

## Mathematical Framework: Factorization of Differential Operators

### Factorization Property (Section 3, Equation 3.5)

The second-order operator factors as:
```
       d           d
L = (―― - λ₁)(―― - λ₂)
       dx         dx
```

This **reveals the structure**: Two first-order operators composed together.

**Why this matters for impulsive response:**
1. The characteristic roots λ₁, λ₂ determine the eigenstructure
2. The impulsive response is built from the first-order solutions e^(λᵢx)
3. The "jump" in initial conditions (y'(0) = 1, y(0) = 0) is the natural boundary condition for this factorization

### General Factorization (Higher Order)

For n-th order system:
```
L = (d/dx - λ₁)(d/dx - λ₂)...(d/dx - λₙ)
```

The impulsive response is defined **recursively**:
```
                    ∫ˣ
g_{λ₁...λₙ}(x) = e^(λₙx) e^(-λₙt) g_{λ₁...λₙ₋₁}(t) dt    (1.3)
                    0
```

This shows how to **build up the solution from first-order pieces**, each with its own "impulse response" structure.

---

## First-Order Case: Prototype (Section 2)

### Simple First-Order Equation
```
y' + ay = f(x)
```

**General solution (Equation 2.3):**
```
         ∫ˣ
y(x) =   g(x-t)f(t)dt + c·g(x)
         0

where: g(x) = e^(-ax)   (impulsive response)
       c ∈ R             (arbitrary constant from homogeneous solution)
```

**Particular solution (with y(0)=0):**
```
         ∫ˣ
yₚ(x) =  e^(-a(x-t))f(t)dt
         0
```

**Key observation**: The impulsive response e^(-ax) is exactly the **free decay** of the system. Convolving with f captures how external forcing is "colored" by the system's natural dynamics.

### Solution with Arbitrary Initial Condition
```
If y(x₀) = y₀, the solution is:

           ∫ˣ
y(x) =     g(x-t)f(t)dt + y₀·g(x-x₀)
           x₀
```

The term y₀·g(x-x₀) is **the free solution** starting from initial condition y₀.

---

## Second-Order Case: The Key Example (Section 3)

### The Complete Solution Structure (Theorem 3.2, Equation 3.24)

```
y'' + ay' + by = f(x)
y(0) = y₀,  y'(0) = y₀'
```

**Solution:**
```
         ∫ˣ
y(x) =   g(x-t)f(t)dt + (y₀' + ay₀)g(x) + y₀g'(x)
         0
         \_____________  ____________________________/
           particular      homogeneous (free vibration)
           solution        with initial conditions
```

### Explicit Formula for Impulsive Response

**Case 1: Distinct roots (λ₁ ≠ λ₂)**
```
         1    λ₁x    λ₂x
g(x) = ――――(e    - e    )
       λ₁-λ₂
```

**Case 2: Repeated roots (λ₁ = λ₂ = λ)**
```
g(x) = x e^(λx)
```

**Case 3: Complex roots (λ = α ± iβ)**
```
              1    αx
g(x) = ――― e    sin(βx)        (underdamped oscillation)
             β
```

### Physical Interpretation

Equation (3.31) shows the complete solution for homogeneous equation (f=0):

**Underdamped (Δ < 0, complex roots α ± iβ):**
```
yₕ(x) = y₀·e^(α(x-x₀))cos(β(x-x₀)) + (y₀'/β - αy₀/β)·e^(α(x-x₀))sin(β(x-x₀))
        |                             |
        response from position jump   response from velocity jump
```

The **two initial conditions** (y₀ and y₀') are **linearly combined** with g(x) and g'(x):
- g(x) carries the "position impulse" response
- g'(x) carries the "velocity impulse" response

---

## Convolution Interpretation

### The Convolution Product (Remark 1, Pages 5-6)

For continuous forcing f(t):
```
         ∫ˣ
yₚ(x) =  g(x-t)f(t)dt  =  (g * f)(x)
         0
```

This is the **convolution of the impulsive response g with the input f**.

**Key property**: Convolution is associative and commutative, which is used crucially in proving the formula (Theorem 3.1, Equation 3.12-3.13).

### Why Convolution Works

The impulsive response g(x) is the system's **fundamental solution** to the equation:
- When multiplied by an impulse-like forcing term (represented via convolution)
- It gives the accumulated effect of all past forcing

---

## Method of Undetermined Coefficients (Section 6)

### Connection to Impulsive Response

For forcing term of special form: **f(x) = P(x)e^(λ₀x)**

The method of undetermined coefficients is proven directly using formula (1.6):
```
         k
g(x) = Σ Gⱼ(x)e^(λⱼx)
        j=1
```

where Gⱼ(x) are polynomials whose degrees relate to root multiplicities.

**Result**: When f(x) = P(x)e^(λ₀x), the particular solution has form:
```
yₚ(x) = Q(x)e^(λ₀x)  or  yₚ(x) = x^m·Q(x)e^(λ₀x)
```

depending on whether λ₀ is a root of the characteristic polynomial.

---

## Critical Comparison: Elementary vs. Rigorous Approaches

### Camporesi's Approach (Elementary)

**Advantages:**
- ✓ Avoids distribution theory entirely
- ✓ Uses only basic calculus and linear algebra
- ✓ Gives **explicit formulas** for solutions
- ✓ Constructive proofs via factorization
- ✓ Suitable for first course on differential equations

**Method:**
- Define impulsive response via initial condition (not via impulse/delta)
- Use factorization of differential operator into first-order pieces
- Build solutions via composition/convolution

### Rigorous Approaches (for comparison)

**Brogliato's approach:**
- Uses distribution theory (Dirac measures)
- Formalizes what "impulsive force" means mathematically
- Treats discontinuous right-hand side explicitly

**d'Andréa-Novel's approach:**
- Uses Laplace transform and transfer functions
- Transfer matrix H(s) = C(sI-A)^(-1)B encodes impulsive response

**Benchohra's approach:**
- Uses measure differential equations (MDEs)
- Jump characterization: x(tₖ⁺) = ΦG(1; x(tₖ⁻), Δu)

### The Unity

All approaches agree:
- **The impulsive response g(x)** is central
- **Initial condition jumps** (especially in velocity) drive the response
- **Convolution with g** gives the particular solution
- **Linear combination of g and its derivatives** gives the general solution

---

## Key Insight: Why Initial Conditions Encode Impulses

### Theorem 3.2 and Theorem 3.3 Show

The solution of:
```
y'' + ay' + by = f(x)
y(x₀) = y₀,  y'(x₀) = y₀'
```

**Equals:**
```
y(x) = ∫ g(x-t)f(t)dt + (y₀' + ay₀)g(x-x₀) + y₀g'(x-x₀)
```

**The structure reveals:**
1. The **particular solution** (first integral) captures the forced response
2. The **homogeneous solution** (linear combination of g and g') captures free vibration
3. **The coefficients of g and g' are NOT arbitrary** — they're determined by the initial conditions y₀ and y₀'
4. **The specific form (y₀' + ay₀) in front of g** shows how the initial velocity y₀' gets "mixed" with position y₀ by the system dynamics (coefficient a)

### Physical Meaning

In a mechanical system (mass-spring-damper):
- An **impulse** creates a **velocity jump** with zero position change
- The impulsive response g(x) with initial conditions g(0)=0, g'(0)=1 models exactly this: **velocity impulse**
- The homogeneous solution then evolves this "velocity memory" through time

---

## Summary: Elementary Path to Understanding Discontinuous RHS

### Why Camporesi Avoids Distributions

**The key insight**: You don't need to explicitly invoke the Dirac delta to understand impulsive response!

Instead:
1. **Define** the impulsive response as the solution to homogeneous equation with special initial conditions
2. **Compute** convolution of this response with the forcing term
3. **Combine** with homogeneous solution weighted by actual initial conditions
4. **Observe** that the structure naturally incorporates "impulse-like" effects

### The Elementary Framework Captures

✓ How impulsive forcing (discontinuous RHS) affects the system  
✓ Why the response depends on both position and velocity jumps  
✓ How to compute explicit solutions  
✓ Why convolution is the right tool  
✓ The complete solution decomposition (particular + homogeneous)  

**Without needing** distribution theory, Laplace transforms, or linear systems theory.

---

## Relevance to Discontinuous Right-Hand Side Research

**HIGHLY RELEVANT** — Camporesi provides:

✓ **Elementary introduction** to impulsive response method  
✓ **Concrete examples** showing how velocity jumps encode impulses  
✓ **Explicit formulas** for system response to discontinuous forcing  
✓ **Pedagogical approach** suitable for teaching the concepts  
✓ **Rigorous proofs** using only basic calculus (no distribution theory)  
✓ **Connection between** discontinuous RHS (impulses) and initial condition jumps (velocity)  
✓ **General n-th order framework** via factorization  

This paper is **ideal for building intuition** about how discontinuous forcing relates to state jumps, **without the mathematical machinery** of distribution theory needed by Brogliato or the Laplace theory in d'Andréa-Novel.

---

## Pedagogical Value

### Three Levels of Understanding

**Level 1 (Camporesi - Elementary):**
- Impulsive response = special initial condition solution
- General solution = particular + homogeneous
- Works by direct calculation, convolution, factorization

**Level 2 (d'Andréa-Novel - Engineering):**
- Impulse response = system transfer function in time domain
- Convolution becomes multiplication in frequency domain (Laplace)
- Fits into control engineering framework

**Level 3 (Brogliato/Benchohra - Mathematical):**
- Impulsive force = Dirac measure distribution
- Discontinuous RHS = equality of measures
- Jump conditions = state transitions via measure theory

**Camporesi provides the bridge from Level 1 → Levels 2 & 3.**
