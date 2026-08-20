# Chen: Linear System Theory and Design - Complete Response Analysis

## Reference
**Book**: Linear System Theory and Design, Third Edition  
**Author**: Chi-Tsong Chen (State University of New York at Stony Brook)  
**Publisher**: Oxford University Press  
**Date**: 1999  
**Key Sections**: 
- Chapter 2: Mathematical Descriptions of Systems (Impulse Response, Transfer Functions)
- Chapter 4: State-Space Solutions and Realizations (Complete Response Formula)
- Chapter 3: Linear Algebra (Matrix Functions, Exponential)

---

## CENTRAL CONTRIBUTION: Complete Response Decomposition

### The Fundamental Problem

**How to describe and solve linear systems when:**
1. Initial conditions are non-zero
2. Inputs are applied (continuous or discontinuous)
3. Need understanding of system's response structure

**Chen's Answer**: Decompose complete response into:
1. **Zero-input response** (response to initial conditions only)
2. **Zero-state response** (response to inputs only)

---

## MATHEMATICAL FRAMEWORK: Complete Solution Formula (Equation 4.5)

### The State Equation
```
ẋ(t) = Ax(t) + Bu(t)    (4.2)
y(t) = Cx(t) + Du(t)    (4.3)
```

### The Complete Solution (Equation 4.5)

**State response:**
```
x(t) = e^(At) x(0) + ∫₀ᵗ e^(A(t-τ)) B u(τ) dτ
```

**Output response (Equation 4.7):**
```
y(t) = C e^(At) x(0) + C ∫₀ᵗ e^(A(t-τ)) B u(τ) dτ + D u(t)
```

### Three-Part Decomposition

**Part 1: Zero-Input Response (Natural Response)**
```
y_zi(t) = C e^(At) x(0)

- Depends ONLY on initial state x(0)
- Independent of input u(t)
- Solution of homogeneous equation with initial conditions
```

**Part 2: Zero-State Response (Forced Response)**
```
y_zs(t) = C ∫₀ᵗ e^(A(t-τ)) B u(τ) dτ + D u(t)

- Depends ONLY on input u(t)
- Assumes zero initial state x(0) = 0
- Convolution of impulse response with input
```

**Part 3: Complete Response**
```
y(t) = y_zi(t) + y_zs(t)

- Linear combination of both components
- Zero-input + Zero-state
```

---

## HOW CHEN ADDRESSES DISCONTINUOUS RIGHT-HAND SIDES

### Key Insight: Transfer Function and Impulse Response

**Theorem 1 (Chapter 2)**: Every linear causal system can be described by impulse response:
```
y(t) = ∫_{t₀}^t g(t,τ) u(τ) dτ    (2.4)
```

**Definition (Section 2.3.1)**: For **time-invariant** systems:
```
g(t,τ) = g(t - τ) = g(t - τ) = g(t - τ)
```

Thus the convolution integral becomes:
```
y(t) = ∫₀ᵗ g(t-τ) u(τ) dτ    (2.8)

(pure convolution - translation invariant)
```

### How Impulse Response Captures Discontinuities

**Key Concept**: The impulse response g(t) is **the response to a unit impulse** at t=0.

**With Dirac Delta Input:**
```
u(t) = δ(t)   (unit impulse, discontinuous in sense of distributions)

y(t) = ∫₀ᵗ g(t-τ) δ(τ) dτ = g(t)   (by sifting property)
```

**Critical Property (Equation 2.8)**:
- The convolution integral equation (2.8) handles **discontinuous inputs** automatically
- Works for inputs including Dirac deltas
- No explicit mention of distributions needed in the framework
- The formula implicitly encodes the relationship

**Example 2.3 (Page 13)**: Feedback system with unit time-delay
```
Input: Dirac impulse δ(t)
Impulse response: g_f(t) = aδ(t-1) + a²δ(t-2) + a³δ(t-3) + ...
                           = Σ a^i δ(t-i)
```

This is an **infinite series of Dirac deltas** captured in one formula!

---

## STATE-SPACE PERSPECTIVE: Exponential Solution

### The Key: Matrix Exponential e^(At)

**Definition (via power series, Equation 3.51)**:
```
e^(At) = I + tA + (t²A²)/2! + (t³A³)/3! + ... = Σ(k=0 to ∞) (t^k A^k)/k!
```

**Critical Property (Equation 3.55)**:
```
d/dt e^(At) = A e^(At) = e^(At) A
```

**This is why the formula works**: The state transition matrix e^(At) automatically captures:
1. System's natural modes (eigenvalues of A)
2. How initial conditions evolve
3. How forcing affects state trajectory

### Response to Initial Condition Jump

**Scenario 1: Pure Initial Condition (u=0)**
```
ẋ = Ax,  x(0) = x₀

Solution: x(t) = e^(At) x₀
```

**Scenario 2: Impulse at t=0 (discontinuous input)**
```
ẋ = Ax + B δ(t),  x(0) = 0

Equivalent to: ẋ = Ax,  x(0⁺) = B

Solution: x(t) = e^(At) B   (for t > 0)
```

**Equivalence**: These two scenarios produce **identical output** for t > 0!

---

## TRANSFER FUNCTION AND FREQUENCY DOMAIN (Section 2.3 & 3.6)

### State-Space to Transfer Function

**From Laplace Transform of State Equation**:
```
Applying L to ẋ = Ax + Bu:
s x̂(s) - x(0) = A x̂(s) + B û(s)

(sI - A) x̂(s) = x(0) + B û(s)

x̂(s) = (sI - A)⁻¹ x(0) + (sI - A)⁻¹ B û(s)
```

**With zero initial condition (x(0)=0)**:
```
ŷ(s) = C(sI - A)⁻¹ B û(s) + D û(s)

        ↓
        
Transfer Function: Ĝ(s) = C(sI - A)⁻¹ B + D    (Equation 2.16)
```

**Important**: Transfer function **represents only zero-state response**

### Inverse Relationship (Equation 3.58)

**The Laplace transform connects state and impulse response**:
```
L[e^(At)] = (sI - A)⁻¹

(matrix transfer function)

L[g(t)] = G(s)

(scalar transfer function)
```

---

## COMPLETE RESPONSE WITH DISCONTINUOUS INITIAL CONDITIONS

### The Full Picture: Four Components

**Complete system description:**
```
ẋ(t) = Ax(t) + Bu(t),  x(0⁻) = x₀
y(t) = Cx(t) + Du(t)
```

**If initial state jumps at t=0** (from 0 to x₀):
```
This is EQUIVALENT to:
- No jump: ẋ(t) = Ax(t) + B δ(t) x₀
- With jump: Initial condition x(0⁺) = x₀
```

**Complete response:**
```
y(t) = C e^(At) x₀ + C ∫₀ᵗ e^(A(t-τ)) B u(τ) dτ + D u(t)
       ↑              ↑
    zero-input    zero-state
    (jump effect)  (input effect)
```

---

## PRACTICAL IMPLICATION: Handling Discontinuous Inputs

### Example 4.2 (Page 90): System with Jump

**Given system:**
```
ẋ = [0  -1] x + [0] u
    [1  -2]     [1]
```

**If u(t) contains impulse at t=0 (Dirac delta)**:
```
The convolution formula handles it:

∫₀ᵗ e^(A(t-τ)) B δ(τ) dτ = e^(At) B  (for t > 0)

This automatically gives the jump in state at t=0⁺
```

### No Need for Explicit Distribution Theory

**Chen's Framework**:
- Uses convolution integral (equation 2.8)
- Works for ANY input including Dirac deltas
- No explicit mention of distributions
- Transfer function Ĝ(s) captures everything

**Alternative Frameworks**:
- Brogliato: Explicitly writes impulse as Dirac measure
- Camporesi: Models impulse via special initial conditions
- Chen: Uses convolution integral that implicitly handles both

---

## STATE TRANSITION MATRIX: The Key to Understanding

### Structure of e^(At)

**For system with eigenvalue λ and multiplicity n**:
```
e^(At) = e^(λt) I + t e^(λt) (A - λI) + (t²/2!) e^(λt) (A - λI)² + ...

(when A is in Jordan form)
```

**For Jordan block (Equation 3.48)**:
```
e^(Jt) = [e^(λt)    t e^(λt)    t²e^(λt)/2!   ...]
         [0         e^(λt)      t e^(λt)      ...]
         [0         0           e^(λt)        ...]
         [...       ...         ...           ...]
```

**Key Property**:
- Each entry is **analytic** (infinitely differentiable)
- Can be **expanded in Taylor series**
- Shows **explicit time dependence**

### Connection to Continuity

**Zero-input response at t=0**:
```
y(0⁺) = C e^(A·0) x(0) = C x(0)  (continuous)

dy/dt|_{t=0⁺} = C A e^(A·0) x(0) = C A x(0)  (may be discontinuous)
```

**Physical meaning**:
- Position remains continuous under impulses
- Velocity can jump instantaneously
- Acceleration becomes singular (Dirac delta)

---

## COMPARISON TO OTHER FRAMEWORKS

| Framework | Key Object | Right-Hand Side | Initial Condition |
|-----------|-----------|-----------------|-------------------|
| **Chen** | Transfer function G(s) | Implicit in convolution | Explicit in formula |
| **Camporesi** | Impulse response g(x) | Special initial conditions | Direct substitute |
| **Brogliato** | Measure equation | Explicit Dirac measures | Jump map Φ_G |
| **Chalishajar** | Generalized functions | Dirac delta in RHS | Auxiliary beam method |

**Chen's Unique Strength**: 
- Unified framework for continuous AND discontinuous inputs
- Works without explicitly invoking distribution theory
- Transfer functions naturally encode impulse behavior
- Laplace domain clearly shows structure

---

## WHY THIS MATTERS FOR DISCONTINUOUS SYSTEMS

### The Three Levels Again

**Level 1 (Camporesi - Elementary)**
- Impulse response via special initial conditions
- g(0)=0, g'(0)=1
- Factorization builds structure

**Level 2 (Chen - Engineering/Classical)**
- Impulse response via convolution integral
- Transfer function encodes all behavior
- Works automatically for Dirac delta inputs
- No distribution theory needed

**Level 3 (Brogliato - Mathematical Rigor)**
- Impulse as explicit Dirac measure
- Measure differential equations
- Full mathematical foundation

**Chen bridges the gap**: Classical control theory perspective that works for discontinuities without explicitly invoking distributions.

---

## KEY THEOREMS AND PROPERTIES

### Theorem 1: Complete System Representation

**Every lumped linear system can be described by**:
```
1. Input-output (external): y(t) = ∫ g(t,τ) u(τ) dτ
2. State-space (internal):  ẋ = Ax + Bu; y = Cx + Du
3. Frequency domain (transfer): ŷ(s) = Ĝ(s) û(s)
```

**All three are equivalent and complementary.**

### Theorem 2: Response Decomposition

**For any initial condition and input**:
```
y(t) = y_zi(t) + y_zs(t)

where:
y_zi(t) = C e^(At) x(0)                                (zero-input)
y_zs(t) = C ∫₀ᵗ e^(A(t-τ)) B u(τ) dτ + D u(t)        (zero-state)
```

### Theorem 3: Impulse Response from State Equations

**For g(t) = impulse response (with zero initial condition)**:
```
g(t) = C e^(At) B + D δ(t)

- First term: smooth response for t > 0
- Second term: direct feedthrough (if D ≠ 0)
- D δ(t) appears if there is direct term
```

### Theorem 4: Transfer Function-Impulse Response Relationship

```
Ĝ(s) = L[g(t)] = C(sI - A)⁻¹ B + D

g(t) = L⁻¹[Ĝ(s)]
```

---

## MATHEMATICAL TECHNIQUES

### Computing e^(At) (Section 3.6, Theorem 3.5)

**Method 1: Eigenvalue decomposition**
```
If A has distinct eigenvalues, find h(λ) such that:
e^(λt) = h(λ) on spectrum of A

Then: e^(At) = h(A)
```

**Method 2: Jordan form**
```
If A = Q Â Q⁻¹ where Â is Jordan form:
e^(At) = Q e^(Ât) Q⁻¹
```

**Method 3: Power series (Equation 3.51)**
```
e^(At) = Σ (t^k A^k)/k!

(convergent for all finite t)
```

**Method 4: Laplace inversion**
```
e^(At) = L⁻¹[(sI - A)⁻¹]
```

---

## DISCRETE-TIME ANALOGUE (Section 4.2.2)

### Discrete Complete Response Formula

**For discrete system:**
```
x[k+1] = A x[k] + B u[k]
```

**Solution (Equation 4.20-4.21):**
```
x[k] = A^k x[0] + Σ(m=0 to k-1) A^(k-1-m) B u[m]

y[k] = C A^k x[0] + Σ(m=0 to k-1) C A^(k-1-m) B u[m] + D u[k]
```

**Zero-input response**: A^k x[0]  
**Zero-state response**: Σ term (discrete convolution)

---

## RELEVANCE TO DISCONTINUOUS RHS RESEARCH

**HIGHLY RELEVANT** — Chen provides:

✓ **Classical framework** that naturally handles discontinuous inputs  
✓ **Complete response decomposition** showing zero-input and zero-state  
✓ **Transfer functions** that encode impulse behavior  
✓ **State transition matrix** showing smooth evolution  
✓ **Convolution integral** that works for Dirac delta inputs  
✓ **Laplace domain** perspective on frequency response  
✓ **No distribution theory** needed for engineering understanding  

**Chen's approach is the industry standard** for control engineering, showing that discontinuous forcing and initial condition jumps are naturally captured in classical linear systems theory without explicit distributions.

---

## SUMMARY: The Five-Paper Perspective

| Paper | Method | Perspective | Best For |
|-------|--------|-------------|----------|
| **Camporesi (1)** | Elementary | Impulsive response via IC | Understanding mechanism |
| **Camporesi (2)** | Factorization | Variable coefficients | General theory |
| **Chen** | State-space | Classical control | Engineering applications |
| **d'Andréa-Novel** | Transfer function | Frequency domain | Control design |
| **Brogliato** | Distributions | Mathematical rigor | Theoretical foundations |
| **Chalishajar** | Generalized functions | Applied mechanics | Practical problems |

**All six frameworks are mathematically equivalent, just different perspectives on the same phenomenon.**
