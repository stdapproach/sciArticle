# Chicurel-Uziel: Parametric Dirac Delta to Simplify Solution of Impulsive Problems

## Reference
**Paper**: Parametric Dirac Delta to Simplify the Solution of Linear and Nonlinear Problems with an Impulsive Forcing Function  
**Authors**: Enrique J. Chicurel-Uziel, Francisco A. Godínez-Rojano  
**Institution**: Instituto de Ingeniería, Universidad Nacional Autónoma de México  
**Journal**: Journal of Applied Mathematics and Physics  
**Date**: 2013  
**Key Innovation**: Parametric representation of Dirac delta that works for **both linear AND nonlinear** differential equations

---

## CENTRAL INNOVATION: Parametrization Eliminates Distributions

### The Core Problem

**Traditional approaches fail for nonlinear problems:**
- Laplace transform works for linear systems but not nonlinear
- Distribution theory requires advanced mathematics
- Need intuitive, elementary-level approach

**Chicurel-Uziel's solution**: Use **parametric representation** of Dirac delta
```
Replace discontinuous time t with continuous parameter w
- Dirac delta naturally emerges from differentiation
- Works for linear AND nonlinear equations
- Uses only elementary calculus
- Geometrically visualizable
```

---

## MATHEMATICAL FRAMEWORK: Parametric Representation

### Step 1: Unit Step with Riser (HR)

**Traditional Heaviside has discontinuity at t=0:**
```
H(t) = 0  for t < 0
H(t) = ?  for t = 0  (undefined)
H(t) = 1  for t > 0
```

**Chicurel-Uziel's innovation**: Replace jump with finite vertical line (riser)
```
HR(t) = continuous function with finite-slope riser instead of jump
```

**Why this helps**: Can be parameterized smoothly

### Step 2: Approximate Unit Step with Near-Vertical Riser

**The approximation (Equation 4):**
```
HR_a(t) = λ(t - a) - 0 + [λ(t - a) - λ(t - a - δ)] · (t - a + δ/2)/δ

where:
- λ is a switching function
- δ → 0 limit gives the riser width
- t parameterized as function of w (parameter)
```

**Parametric representation (Equations 5-6):**
```
HR_a(w) = λ(w - 0) - [w/(1 - δ²)]  (unit step with parameter)

t_a(w) = [1 - λ(w - 0)] · w + λ(w - 0) · (w + δ + δ²/2)  (time with parameter)

where:
- w is arc length along the riser
- When δ → 0: single point t=0 expands to interval 0 ≤ w ≤ 1
```

### Step 3: Differentiate to Get Dirac Delta

**Key property (Equation 3)**:
```
dH_R/dt = lim(δ→0) dH_Ra/dt
```

**Taking derivatives with respect to parameter (Equations 17-18)**:
```
δ(t - 0) = [λ(w - 0) - λ(w - 1)] / [1 - λ(w - 0) - λ(w - 1)]

t(w) = [1 - λ(w - 0)] · w + λ(w - 1) · w + [1 - λ(w - 1)]
```

### Step 4: Simplified Impulse Function (Equations 23-28)

**For physical impulse at t=0, the ABBREVIATED parametric form:**
```
t(w) = w · [1 - λ(w - 1)]  (Equation 23)

H_R(w) = λ(w - 0) + w · λ(w - 1) · [1 - λ(w - 1)]  (Equation 24)

Dirac delta: δ(t - 0) = [λ(w - 1)] / [1 - λ(w - 1)]  (Equation 28)

where λ(w - 1) = {0 if w < 1
                  {1 if w ≥ 1
```

**Remarkable result**: **Single point t=0 becomes interval 0 ≤ w ≤ 1 in parametric form!**

---

## HOW IT SOLVES DIFFERENTIAL EQUATIONS

### Key Strategy: Split into Two Problems

**Original differential equation with impulsive forcing:**
```
dy/dt = f(y) + g·δ(t)    y(0) = y₀
```

**Parametric method splits into:**

**1. IMPULSE INSTANT (0 ≤ w ≤ 1, t = 0):**
- Finite interval in parameter space
- No ordinary time progression
- Contains jump dynamics

**2. POST-IMPULSE TIME (w ≥ 1, t > 0):**
- Regular time evolution
- Homogeneous equation (forcing becomes initial condition)

### The Split Transformation

**For differential equation with Dirac delta:**
```
Original:  dy/dt = f(y) + g·δ(t)
```

**Becomes parametric form:**
```
dy/dw · (dw/dt) = f(y) + g·δ(t - 0) · (dw/dt)
```

**Substituting dw/dt from parametric relations:**
```
At impulse instant (0 ≤ w < 1):
dy/dw = [g - 0·f(y)] · [dt/dw]

At post-impulse (w ≥ 1):
dy/dw = [0 - f(y)] · [dt/dw] = -f(y)·dt/dw
```

**Critical simplifications:**
- Dirac delta converts to **constant** in impulse equation
- Terms involving **slow processes vanish** during impulse
- Post-impulse becomes **homogeneous**

---

## EXAMPLE 1: Heat Conduction with Impulse (Linear, PDE)

### The Problem (Equation 30)

**Parabolic PDE with impulsive heating:**
```
c ∂T/∂t = k ∂²T/∂x² + q·δ(t - 0)

with:
- Initial condition: T(x,0) = 0
- Boundary conditions: T(0,t) = T(L,t) = 0
- c = heat capacity, k = conductivity, q = heat energy
```

### Traditional Solution Issues

**Standard approach gives initial temperature:**
```
T(x,0) = q/c  (WRONG - violates initial condition!)
```

**Gibbs phenomenon**: Spurious oscillations at discontinuity

### Parametric Solution

#### Impulse Instant Equation (0 ≤ w ≤ 1)

**After substitution (Equation 37):**
```
dJ/dw = -[c·F·dH_R/dw]/k · (dt/dw) - f(d²F/dx²)

Simplifies (conduction term vanishes during impulse!):

c·F·dJ/dw = I·[λ(w - 1)]  (Equation 38)
```

**Physical insight**: **No time for heat conduction during instantaneous impulse**
- Conduction term vanishes automatically
- Heating is pure energy increase
- Temperature evolves as:  T_i(w) = (q/c)·w  (Equation 45)

**At end of impulse (w=1):**
```
Initial temperature for post-impulse: T_i(w=1) = q/c
```

#### Post-Impulse Equation (w ≥ 1)

**Standard homogeneous PDE:**
```
c ∂T/∂t = k ∂²T/∂x²  (Equation 53)

With initial condition T(x,0⁺) = q/c (from impulse instant)
```

**Well-known solution (Equation 56):**
```
T_p(x,t) = (2q/c) Σ [sin(nπx/L) / n] · exp(-n²π²kt/(L²c))
```

#### Complete Parametric Solution (Equation 57)

```
T(x,w) = (q/c)·w·[λ(w - 1)]  +  (2q/c)·[1 - λ(w - 1)]·
         Σ [sin(nπx/L)/n] · exp(-n²π²k[t(w)]/(L²c))

where t(w) = w·[1 - λ(w - 1)]
```

**Two-piece structure:**
- **First term**: Instantaneous heating during impulse (0 ≤ w ≤ 1)
- **Second term**: Subsequent cooling/conduction (w > 1)

### Comparison: Parametric vs. Conventional (Figures 10-11)

**Parametric solution advantages:**
```
✓ Shows initial condition T(x,0) = 0 correctly
✓ Displays instantaneous "wall" of temperature rise
✓ Smooth representation from start
✓ NO Gibbs phenomenon oscillations
✓ Clear physical picture of impulse process
```

**Conventional solution problems:**
```
✗ Shows T(x,0) = q/c (violates specification!)
✗ Misses instantaneous rise
✗ Plagued by Gibbs oscillations
✗ Misleading pseudo-initial condition
```

---

## EXAMPLE 2: Nonlinear Duffing Oscillator (Nonlinear ODE)

### The Problem (Equation 59)

**Mass-spring system with cubic restoring force and impulse:**
```
m·d²x/dt² + x³ = I·δ(t - 0)

Initial conditions: x(0) = 0, dx/dt(0) = 0
I = impulse magnitude
```

**This is NONLINEAR** — Laplace transform doesn't work!

### Parametric Solution Strategy

#### Convert to First-Order System (Equation 61)

**State variables:**
```
dx/dt = v
m·dv/dt = -x³ + I·δ(t - 0)
```

**Parametric form (Equation 64):**
```
dx/dw · (dw/dt) = v
m·dv/dw · (dw/dt) = -x³ + I·λ(w - 1)
```

#### Impulse Instant (0 ≤ w ≤ 1)

**Elimination of spring force!**
```
At impulse: m·dv_i/dw = I  (Equation 65a)
At impulse: dx_i/dw = 0    (Equation 65b)

Physical meaning: "No time for displacement during impulse"
Therefore: x_i(w) = 0  (remains zero!)
But:       v_i(w) = (I/m)·w

At w=1: v_i(1) = I/m  (velocity jump)
        x_i(1) = 0    (no position change)
```

**Impulse-momentum principle automatically applied!**
```
Δv = I/m  (change in momentum from impulse)
```

#### Post-Impulse Time (w ≥ 1)

**Regular nonlinear ODE with initial conditions from impulse:**
```
m·d²x_p/dt² = -x_p³  (Equation 73)

Initial conditions (Equation 74):
x_p(0) = 0
v_p(0) = I/m
```

**Phase-plane solution (Equation 75):**
```
v_p² + (2/m)·x_p⁴/4 = (I/m)²

This is an elliptic integral — closed-form expression uses hypergeometric function
```

#### Complete Parametric Solution (Equations 78-82)

```
x(w) = [1 - λ(w - 1)]·0 + λ(w - 1)·x_p(t)
v(w) = [1 - λ(w - 1)]·(I/m)·w + λ(w - 1)·v_p(t)

where solutions of post-impulse use hypergeometric functions
```

**Rendered as graphical solution (Figure 13):** Time-displacement and time-velocity plots show smooth connection from impulse instant to post-impulse evolution.

---

## CRITICAL ADVANTAGES OF PARAMETRIC METHOD

### 1. Works for Nonlinear Systems

**Paradigm shift:**
```
Traditional Laplace Transform:  FAILS for nonlinear
Parametric Dirac Delta:        WORKS for nonlinear
```

### 2. Automatic Physics Simplification

**During impulse instant, slow processes vanish:**
- Heat conduction → absent (Example 1)
- Spring force → absent (Example 2)
- Only fast processes remain

**Emerges naturally from parametrization** — no ad-hoc modeling!

### 3. Separates Timescales

**Parameter w makes explicit:**
- **Instantaneous processes** (0 ≤ w ≤ 1, real time t=0)
- **Subsequent evolution** (w > 1, real time t > 0)

**Solves "singularity at t=0" problem:** Single point becomes resolvable interval in parameter space

### 4. Elementary Mathematics

```
✓ No distribution theory needed
✓ Only elementary calculus
✓ Geometrically visualizable
✓ Easily taught at undergraduate level
✓ No Gibbs phenomenon artifacts
```

### 5. Correct Initial Conditions

**Parametric solution uses ACTUAL initial conditions:**
```
T(x,0) = 0  ✓  (correctly shown)

vs. conventional that shows:
T(x,0) = q/c  ✗  (violates specification)
```

---

## MATHEMATICAL FOUNDATION

### Why Parametrization Works

**The key insight:**
```
Single discontinuity at t=0 
  ↓
Expand into finite interval 0 ≤ w ≤ 1 in parameter space
  ↓
Now differentiable within interval
  ↓
Delta emerges from differentiation of parametric step
  ↓
No distribution theory needed!
```

### Comparison of Frameworks

| Feature | Distribution Theory | Parametric Method |
|---------|-------------------|-------------------|
| **Impulse representation** | Dirac measure | Parameter interval w ∈ [0,1] |
| **Mathematical level** | Advanced (functionals) | Elementary (calculus) |
| **Linear problems** | ✓ Works | ✓ Works |
| **Nonlinear problems** | ✗ Fails | ✓ Works |
| **Visualization** | Abstract | Geometric (parameter space) |
| **Initial conditions** | Issues with jumps | Naturally handled |
| **Gibbs phenomenon** | Present | Absent |
| **Physics simplification** | Manual reasoning | Automatic in equations |

---

## CONNECTION TO DISCONTINUOUS RHS

### How Parametrization Handles Discontinuities

**Problem:** Discontinuous right-hand side
```
dy/dt = f(y,t) + g·δ(t)
```

**Traditional approaches:**
- Distribution theory: Treat as generalized function
- Laplace transform: Works for linear only
- Jump conditions: Require careful bookkeeping

**Parametric approach:**
- Parameter w replaces time t in impulse region
- Singularity at t=0 becomes resolvable interval 0 ≤ w ≤ 1
- Two separate equations with smooth right-hand sides
- Automatic extraction of impulse-driven changes

### Why This Differs from Other Papers

| Paper | Handles Discontinuity | Approach |
|-------|----------------------|----------|
| **Camporesi** | Elementary | Special initial conditions |
| **Chen** | Implicit | Convolution integral |
| **d'Andréa-Novel** | Frequency domain | Transfer functions |
| **Brogliato** | Distribution theory | Explicit measures |
| **Chalishajar** | Generalized functions | Dirac deltas in RHS |
| **Chicurel-Uziel** | Parametrization | Transform to parameter space |

**Chicurel-Uziel is unique:** Makes impulsive processes explicitly **observable** in parameter space rather than implicit in distributions.

---

## PRACTICAL IMPLICATIONS

### Advantages for Problem Solving

1. **Transparent process**: See exactly what happens during impulse
2. **Automatic simplification**: Irrelevant terms vanish naturally
3. **Correct boundary behavior**: No artificial initial conditions
4. **Nonlinear capability**: Extends beyond Laplace domain
5. **No spurious artifacts**: No Gibbs oscillations
6. **Elementary teaching**: Can present to undergraduates

### Limitations

- Requires numerical integration for post-impulse solutions (in general)
- Hypergeometric functions appear for nonlinear cases
- Graphical solutions more useful than closed-form for nonlinear

---

## RELEVANCE TO DISCONTINUOUS RHS RESEARCH

**HIGHLY RELEVANT** — Chicurel-Uziel provides:

✓ **Nonlinear extension** when other methods fail  
✓ **Parametric insight** into discontinuous forcing  
✓ **Automatic physics** — irrelevant terms vanish  
✓ **Separates timescales** — impulse vs. evolution  
✓ **Elementary framework** — no distributions needed  
✓ **Correct initial conditions** — not replaced by substitutes  
✓ **No artifacts** — Gibbs phenomenon eliminated  
✓ **Visual geometry** — parameter space visualization  

**Key innovation**: Makes the instantaneous impulse process explicit and resolvable, avoiding the mathematical singularities of distribution theory while maintaining physical fidelity.

---

## COMPLETE FRAMEWORK: All Seven Papers

| # | Paper | Key Method | Best For |
|---|-------|-----------|----------|
| 1 | **Camporesi (1)** | Elementary IC | Intuition building |
| 2 | **Camporesi (2)** | Factorization | Variable coefficients |
| 3 | **Chen** | State-space | Classical control |
| 4 | **d'Andréa-Novel** | Transfer functions | Frequency domain |
| 5 | **Brogliato** | Measure theory | Mathematical rigor |
| 6 | **Chalishajar** | Generalized functions | Engineering mechanics |
| 7 | **Chicurel-Uziel** | Parametrization | Nonlinear problems |

**Hierarchy of understanding:**
- **Elementary**: Camporesi — visualize impulse response
- **Classical**: Chen — state-space framework
- **Frequency**: d'Andréa-Novel — transfer functions
- **Nonlinear**: Chicurel-Uziel — parametric method
- **Rigorous**: Brogliato — distribution theory
- **Applied**: Chalishajar — physical problems
- **Variable**: Camporesi (2) — general coefficient case
