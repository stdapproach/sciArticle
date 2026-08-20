# Camporesi: Linear ODE - Revisiting the Impulsive Response Method Using Factorization

## Reference
**Paper**: Linear ordinary differential equations. Revisiting the impulsive response method using factorization  
**Author**: Roberto Camporesi (Politecnico di Torino)  
**Date**: August 19, 2010  
**Key Innovation**: Extends impulsive response method from **constant coefficients to variable coefficients** using Polya-Mammana factorization

---

## Major Contribution: Extension to Variable Coefficients

### The Central Innovation

**For constant coefficients** (as in the first paper):
```
Differential operator can be factored as:
L = (d/dx - λ₁)(d/dx - λ₂)...(d/dx - λₙ)

where λⱼ are the characteristic roots (constant)
```

**For variable coefficients** (NEW in this paper):
```
Differential operator can STILL be factored as:
L = (d/dx - α₁(x))(d/dx - α₂(x))...(d/dx - αₙ(x))

where αⱼ(x) are NOW VARIABLE FUNCTIONS!
```

**The Mammana Result** (1926, 1931): Any real linear differential operator with continuous real coefficients can be factored in this form globally over any interval I, with generally complex-valued functions αⱼ.

**The Generalization** (Camporesi & Di Scala, 2010): This extends to complex-valued coefficients as well.

### Why This Matters

The factorization shows that **even variable-coefficient systems have an "impulsive response" structure** — there's a fundamental kernel g(x,t) that encodes:
- The response to impulses (discontinuous forcing)
- The free vibration modes
- The general solution structure

---

## Mathematical Framework: Impulsive Response Kernel

### Definition for Variable Coefficients (Theorem 3.1-3.2)

For system:
```
Ly = y⁽ⁿ⁾ + a₁(x)y⁽ⁿ⁻¹⁾ + ... + aₙ(x)y = f(x)
```

The **impulsive response kernel** g(x,t) is defined as:

**At t (parametrically)**:
```
For any fixed t ∈ I, define x → gₜ(x) as the unique solution of:
Ly = 0  with initial conditions
y(t) = y'(t) = ... = y⁽ⁿ⁻²⁾(t) = 0
y⁽ⁿ⁻¹⁾(t) = 1
```

Then:
```
g(x,t) = gₜ(x)
```

### Recursive Definition (Equation 1.3)

**For n=1:**
```
         ∫ˣ
gₐ(x,t) = e  ᵃ⁽ʳ⁾ ᵈʳ
         ᵗ
```

**For n ≥ 2:**
```
         ∫ˣ
g_{α₁...αₙ}(x,t) =  gₐₙ(x,s)·g_{α₁...αₙ₋₁}(s,t) ds
         ᵗ
```

This is **remarkably elegant**: The kernel is built by composing single-factor responses g_{αⱼ} via integration.

### Key Properties

**Particular Solution (Theorem 3.1):**
```
         ∫ˣ
yₚ(x) =  g(x,t)f(t)dt
         ₓ₀
```

This solves the non-homogeneous equation with **zero initial conditions**.

**Boundary Conditions (Equation 3.2):**
```
∂ʲ g/∂xʲ |ₓ₌ₜ = 0    for j = 0,1,...,n-2
∂⁽ⁿ⁻¹⁾g/∂xⁿ⁻¹|ₓ₌ₜ = 1
```

This is the **variable-coefficient version** of the impulsive response definition.

---

## Homogeneous Solution: The Green's Function Structure

### Theorem 3.3: General Solution via Partial Derivatives

**For variable-coefficient homogeneous equation Ly = 0:**

```
         n-1
y(x) =   Σ   c̃ⱼ(-1)ʲ ∂ʲg/∂tʲ(x,t)     (for any t ∈ I)
         j=0
```

**Critical insight**: The general solution is a **linear combination of partial derivatives of g with respect to t**, not x!

**Fundamental System (Equation 3.11):**
```
The n functions:
g(x,t),  -∂g/∂t(x,t),  ...,  (-1)ⁿ⁻¹ ∂ⁿ⁻¹g/∂tⁿ⁻¹(x,t)

form a fundamental system for ANY t ∈ I
```

This is remarkable: **The impulsive response kernel g(x,t) generates all solutions through differentiation in the second variable!**

### Coefficients in Terms of Initial Data (Equation 3.18)

```
c̃ⱼ = Σ (-1)ᵏ⁻ʲ (k choose j) aₖ₍ₖ₋ⱼ₎(t) bₙ₋ₖ₋₁
     k≥j

where: bⱼ = y⁽ʲ⁾(t) are the initial conditions at x = t
```

**Examples:**
- **n=2**: c̃₀ = b₁ + a₁(t)b₀,  c̃₁ = b₀
- **n=3**: c̃₀ = b₂ + a₁(t)b₁ + (a₂(t) - a₁'(t))b₀,  etc.

**Key observation**: Derivatives of the coefficients aⱼ(x) start appearing as soon as n≥3!

---

## Connection to Wronskians and Variation of Parameters

### The Fundamental Identity (Equation 3.22)

```
g(x,t) = y₁(x)(W(t)⁻¹)₁ₙ + y₂(x)(W(t)⁻¹)₂ₙ + ... + yₙ(x)(W(t)⁻¹)ₙₙ
```

Where:
- y₁(x), ..., yₙ(x) = any fundamental system of solutions
- W(t) = Wronskian matrix
- (W(t)⁻¹)ⱼₙ = entry of the inverse matrix

**This connects the impulsive response kernel to the classical variation of parameters method!**

### Wronskian Determinant of the Fundamental System

```
         ∂ⁿ⁻¹g
w̃(t,t) = det(∂ˣʲ ∂ᵗᵏ g)|ₓ₌ₜ  has special structure:
         j,k=0

w̃(t,t) = (-1)ⁿ⁽ⁿ⁻¹⁾/²
```

This shows the fundamental system is indeed **linearly independent**.

---

## Case Study: n=2 (Second-Order Variable-Coefficient Equations)

### The Riccati Equation Connection

For:
```
L = d²/dx² + a₁(x)d/dx + a₂(x)
```

Factorization requires solving:
```
d/dx = (d/dx - α₁(x))(d/dx - α₂(x))
```

Expanding and comparing coefficients leads to a **Riccati equation**:
```
β' + β² + a₁β + a₂ = 0    (3.5)
```

Where:
```
β = α₁ + α₂
```

**Physical meaning**: The Riccati equation encodes the coupling between the two first-order factors that compose the second-order operator.

### Solution Formula

When β is complex-valued with β(x) = Re β(x) + i Im β(x):

```
General solution of Ly = 0:
                    ∫ˣ              ∫ˣ
y(x) = e^{η(x)}(c₁ cos ω(x) + c₂ sin ω(x))

where:  η(x) = ∫ Re β(t) dt
               ₓ₀

        ω(x) = ∫ Im β(t) dt
               ₓ₀
```

**This generalizes the constant-coefficient case!** When β has constant components, this reduces to the familiar exponentially modulated oscillations.

---

## Regularity Conditions for Variable Coefficients

### Theorem 3.3 Conditions

For the general solution formula (3.10) to hold:

```
aⱼ ∈ C^{n-j-1}(I)    for j = 1, ..., n-1
aₙ ∈ C⁰(I)

(C^k denotes k-times continuously differentiable)
```

**Minimal regularity**: These are the **weakest conditions** under which the formula makes sense.

**Stronger regularity**: If we require aⱼ ∈ C^{n-j}, then:
- The kernel g has n partial derivatives w.r.t. t
- g satisfies an adjoint equation in the t variable
- The solution is even more regular

### Regularity of the Factors

These conditions translate to requirements on the factorization functions:

```
From constant coefficient case:   aⱼ → αⱼ conditions
Minimal: αₙ ∈ C^{n-1},  αⱼ ∈ C^{n-2}  (j = 1,...,n-1)
Stronger: αⱼ ∈ C^{n-1}  for all j
```

---

## Physical Interpretation: From Constant to Variable Systems

### Constant Coefficient Case (Earlier Paper)

```
λⱼ = characteristic roots (constants)
g(x,t) = g(x-t)         [translation invariant]
Solution = g(x) derivative basis + convolution forcing
```

### Variable Coefficient Case (This Paper)

```
αⱼ(x) = factors (functions of x)
g(x,t) = kernel dependent on BOTH x and t separately
Solution = g derivatives w.r.t. t basis + convolution forcing
```

**Key difference**: The translation invariance is broken, so:
- Cannot simply take x-derivatives of g
- Instead, must use **t-derivatives** as the fundamental system
- Coefficients in the solution mix with derivatives of aⱼ(x)

### Why the Factorization Still Works

**Remarkably**, the factorization:
```
L = (d/dx - α₁(x))(d/dx - α₂(x))...(d/dx - αₙ(x))
```

**still allows**:
1. Building solutions layer by layer via the recursive formula
2. Using convolution with g to handle forcing
3. Generating the fundamental system from partial derivatives of g

This is because **the factorization structure is independent of whether the αⱼ are constant or variable**.

---

## Connection to Discontinuous Right-Hand Sides

### The Impulsive Response as General Kernel

The key insight: **The impulsive response kernel g(x,t) is defined via zero initial conditions plus a unit "impulse" in the (n-1)-th derivative.**

This means:
1. g encodes how the system responds to **discontinuous forcing**
2. For variable coefficients, this response **varies with position** (through α(x))
3. But the **structure remains**: it's still a convolution kernel

### Generalization to Measure Equations

For variable-coefficient systems:
```
dx = f(x,t)dt + G(x,t)du    (measure differential equation)
```

The state jump at discontinuities would be:
```
x(tₖ⁺) = ΦG(1; x(tₖ⁻), u(tₖ⁺) - u(tₖ⁻))
```

Camporesi's factorization shows this **can still be computed** even with variable coefficients, through the variable-coefficient version of the integrating factors.

---

## Complete Solution Formula: Constant vs Variable Coefficients

### Constant Coefficients (Camporesi Paper 1, Theorem 3.3)

```
           ∫ˣ
y(x) =     g(x-t)f(t)dt + (y₀' + ay₀)g(x-x₀) + y₀g'(x-x₀)
           ₓ₀
```

- Particular solution via convolution
- Homogeneous solution via g and g'
- **Translation invariant**: g(x,t) = g(x-t)

### Variable Coefficients (This Paper, Theorems 3.1-3.3)

**For zero initial conditions:**
```
           ∫ˣ
yₚ(x) =    g(x,t)f(t)dt
           ₓ₀
```

**For arbitrary initial conditions:**
```
                 n-1
y(x) = yₚ(x) +  Σ   c̃ⱼ(-1)ʲ ∂ʲg/∂tʲ(x,t)
                j=0

where c̃ⱼ determined by initial conditions via (3.18)
```

- Particular solution still convolution-based
- Homogeneous solution via **t-derivatives** of g (not x-derivatives!)
- **NOT translation invariant**: g(x,t) ≠ g(x-t)

---

## Pedagogical Value: Understanding Discontinuities Systematically

### Why This Matters for Discontinuous RHS Research

Camporesi (both papers) demonstrates:

1. **Elementary framework** avoids distribution theory while still capturing impulse effects
2. **Factorization** is the **unifying principle** whether coefficients are constant or variable
3. **The impulsive response kernel** g(x,t) is the **fundamental object** encoding:
   - System's response to discontinuous forcing
   - Free vibration structure
   - Relationship between initial conditions and later evolution

4. **No Dirac deltas needed** to understand the mechanism — just:
   - Initial conditions with unit "kick" in highest derivative
   - Convolution with forcing
   - Linear combinations of derivatives

### Connection to Three Mathematical Frameworks

**Level 1 (Camporesi - Elementary):**
- Impulsive response = special initial condition solution
- Factorization → layer-by-layer construction
- Works for constant AND variable coefficients

**Level 2 (Control Theory - d'Andréa-Novel):**
- Impulse response = transfer function in time domain
- Convolution becomes multiplication (frequency domain)
- Constant coefficients only

**Level 3 (Mathematical Foundation - Brogliato/Benchohra):**
- Impulsive force = Dirac measure distribution
- Discontinuous RHS = equality of measures
- Full mathematical rigor

**Camporesi provides the bridge**: It shows the impulsive response method works **fundamentally** through factorization, independent of whether you invoke distributions.

---

## Key Theorems Summary

### Theorem 2.2 (Constant Coefficients)
Constructive proof: MDE solutions exist uniquely via recursive formula (2.7)

### Theorem 3.2 (Variable Coefficients)  
Same structure with variable αⱼ(x) factors

### Theorem 3.3 (Variable Coefficients)
General solution via **t-derivatives** of kernel: equation (3.10)

### Theorem 3.1 (General Principle)
Kernel g(x,t) defined by zero ICs + unit jump in (n-1)-th derivative

---

## Relevance to Discontinuous Right-Hand Side Research

**CRITICALLY RELEVANT** — This paper shows:

✓ **Impulsive response method extends beyond constant coefficients**  
✓ **Factorization is the universal principle** for handling impulses  
✓ **Green's kernel encodes discontinuity response** for variable systems  
✓ **No distribution theory needed** for understanding the mechanism  
✓ **Wronskian connection bridges to variation of parameters**  
✓ **Partial derivative structure (3.11) generalizes fundamental theorem**  
✓ **Riccati equation (3.5) connects factor theory to specific structure**  

This is the **most general elementary framework** for understanding how systems respond to discontinuous forcing, applicable even when coefficients vary in space/time.
