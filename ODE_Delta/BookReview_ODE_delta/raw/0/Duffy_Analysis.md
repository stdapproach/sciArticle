# Duffy, Dean G. - "Green's Functions with Applications" (2nd Edition, 2015)

## Framework Classification
**Framework 44 - Classical Green's Functions Theory for ODE and PDE**

**Type**: Comprehensive Textbook
**Author**: Dean G. Duffy (Former Instructor, US Naval Academy)
**Publisher**: CRC Press (Taylor & Francis Group)
**ISBN**: 978-1-4822-5103-6
**Publication Year**: 2015 (2nd Edition)
**Total Pages**: 672

---

## 1. CENTRAL MISSION AND UNIQUE CONTRIBUTION

Duffy's "Green's Functions with Applications" provides a comprehensive and rigorous treatment of Green's function methods for solving linear differential equations (both ODE and PDE). The book serves as both a theoretical foundation and a practical guide for engineers and applied mathematicians.

**Core Mission**:
- Establish a unified mathematical framework for solving nonhomogeneous linear differential equations via Green's function methods
- Bridge pure mathematical theory (distribution theory, Schwartz test functions) with practical engineering applications
- Provide systematic techniques for constructing Green's functions for initial-value and boundary-value problems
- Demonstrate the equivalence between impulse response (delta-function forcing) and the fundamental solution concept

**Unique Approach**:
- Rigorous treatment of the Dirac delta function using distribution theory (Chapter 2.5)
- Clear connection between circuit theory, statics, and integral equations through Green's function framework
- Emphasis on the impulse response as the most direct route to Green's function computation
- Systematic classification of Green's functions: "one-sided" (for initial-value problems) vs. "two-sided" (for boundary-value problems)

---

## 2. TREATMENT OF DISCONTINUITIES ON THE RIGHT-HAND SIDE

### 2.1 Theoretical Framework for Discontinuities

**Duffy's treatment is foundational**: He addresses discontinuities through **distribution theory** and the **Dirac delta function**, providing rigorous mathematical underpinnings.

**Key Reference: Chapter 2, Section 2.5 - "The Dirac Delta Function"**

#### Distribution Theory Approach (Pages 66-94)

Duffy introduces distributions as the mathematical object that encompasses functions like the Dirac delta:

**Definition (Page 92-93)**:
> "A distribution g(x) is a 'function' associated with a weakly convergent sequence of admissible functions for which the symbolic integral... means ∫_{-∞}^{∞} g(x)ϕ(x)dx = lim_{n→∞} ∫_{-∞}^{∞} g_n(x)ϕ(x)dx."

**Test Functions and Admissible Functions**:
- Test functions ϕ(x): infinitely differentiable, bounded support
- Admissible functions: infinitely differentiable over the entire domain, arbitrary behavior at infinity
- The Dirac delta δ(x) is defined through weak convergence: ∫_{-∞}^{∞} δ_n(x)ϕ(x)dx → ϕ(0)

#### The Delta Function as Right-Hand Side (Example 2.5.6, Page 93)

**Exemplary Differential Equation with Delta Forcing**:
```
dg/dt + ag = δ(t - τ)
```

**Duffy's Treatment**:
1. Multiply the equation by a test function ϕ(t) and integrate:
   ∫_{-∞}^{∞} [dg/dt + ag]ϕ(t)dt = ∫_{-∞}^{∞} δ(t - τ)ϕ(t)dt = ϕ(τ)

2. Integrate by parts (using boundary conditions):
   ∫_{-∞}^{∞} g(t)[aϕ(t) - ϕ'(t)]dt = ϕ(τ)

3. This equation holds for all test functions ϕ(t), defining g(t) as a distribution

**Key Insight**: The delta function on the RHS generates a distribution-type solution that may not be classically differentiable everywhere.

#### Multidimensional Delta Functions (Page 94)

Duffy extends the delta function to multiple dimensions with careful handling of coordinate systems:

**Three-Dimensional Definition**:
```
f(r_0)  if r_0 is inside V
∫∫∫_V f(r)δ(r - r_0)dV = 
0       otherwise
```

**Representation in Various Coordinates** (Table 2.5.2):
- **Cartesian**: δ(x - ξ)δ(y - η)δ(z - ζ)
- **Cylindrical**: δ(r - ρ)δ(ϕ - ϕ₀)δ(z - ζ) / r
- **Spherical**: δ(r - ρ)δ(θ - θ₀)δ(ϕ - ϕ₀) / (r² sin θ)

---

### 2.2 Delta Function Properties and Extensions

**Properties Utilized** (Table 2.5.1, referenced):
1. **Sifting property**: ∫_{-∞}^{∞} f(x)δ(x - a)dx = f(a)
2. **Scaling**: δ(ax) = δ(x) / |a|
3. **Composition**: δ[f(x)] = Σ δ(x - x_n) / |f'(x_n)| (over zeros of f)

**Examples from Duffy**:

**Example 2.5.4 - Scaled Delta**:
δ(at) = δ(t) / |a|

**Example 2.5.5 - Delta of Trigonometric Function**:
δ[sin(t)] = Σ_{n=-∞}^{∞} δ(t - nπ) / |cos(nπ)|

**Key Point**: These properties show how the delta function encodes information about where and how the RHS becomes discontinuous or impulsive.

---

## 3. IMPULSE RESPONSE AND TRANSFER FUNCTIONS

### 3.1 Green's Function as Impulse Response

**Duffy's Definition** (Chapter 3.1, Page 92):

> "Given a linear ordinary differential equation... the Green's function g(t|τ) for this equation is the solution to the differential equation:
> 
> d^n g/dt^n + a_1 d^(n-1)g/dt^(n-1) + ... + a_(n-1) dg/dt + a_n g = δ(t - τ), 0 < t,τ
>
> The forcing occurs at time t = τ..."

**Fundamental Insight**: 
The Green's function IS the impulse response. It is obtained by forcing the system with a Dirac delta function (unit impulse) at time τ and observing the response g(t|τ).

### 3.2 Impulse Response in Circuit Theory (Pages 99-101)

**Example: RL Circuit**

**Governing Equation**:
```
L di/dt + Ri = v(t)
```

where:
- L = inductance
- R = resistance  
- v(t) = applied voltage
- i(t) = current

**Step 1: Single Impulse Response**

When voltage is applied as impulse V₀/Δτ during interval τ < t < τ + Δτ:
```
0                           if t < τ
i(t) = 
(V₀/L)e^(-R(t-τ)/L)        if τ ≤ t
```

**Step 2: Multiple Impulses**

With N impulses of amplitude V_i/Δτ at times τ_i:
```
        N
i(t) = Σ (V_i/L)e^(-R(t-τᵢ)/L)  for t ≥ τ_i
       i=0
```

**Step 3: Continuous Forcing**

Over each infinitesimal interval dτ, voltage impulse is v(τ)dτ. Response becomes:
```
        t
i(t) = ∫ v(τ)g(t|τ)dτ  (Superposition Integral)
       0

where g(t|τ) = (e^(-R(t-τ)/L))/L, τ < t
```

**Key Result (Equation 2.7.11-2.7.12)**:
The impulse response is g(t|τ) = (e^(-R(t-τ)/L))/L, and any system response equals the convolution of the forcing with this impulse response.

### 3.3 Direct Computation of Green's Function via Laplace Transform

**Reference**: Chapter 3.1, Example 3.1.1, Pages 111-112

**Problem**:
```
y'' - 3y' + 2y = f(t),  with y(0) = y'(0) = 0
```

**Solution via Delta-Function Forcing**:

Replace f(t) with δ(t - τ):
```
g'' - 3g' + 2g = δ(t - τ),  with g(0|τ) = g'(0|τ) = 0
```

**Laplace Transform**:
```
[s² - 3s + 2]G(s|τ) = e^(-sτ)

G(s|τ) = e^(-sτ) / (s² - 3s + 2) = e^(-sτ) / [(s-1)(s-2)]
```

**Inverse Laplace Transform**:
```
g(t|τ) = [e^(2(t-τ)) - e^(t-τ)] H(t - τ)
```

where H(t - τ) is the Heaviside step function.

**Causality**: g(t|τ) = 0 for t < τ (impulse cannot have effect before it occurs).

### 3.4 Damped Harmonic Oscillator (Pages 113-115)

**Governing Equation**:
```
my'' + cy' + ky = f(t),  y(0) = y'(0) = 0
```

**Green's Function Differential Equation**:
```
mg'' + cg' + kg = δ(t - τ),  g(0|τ) = g'(0|τ) = 0
```

**Transfer Function** (via Fourier transform, Equation 3.1.18):
```
G(ω|τ) = e^(-iωτ) / (mω² - ω₀² + icω/m)

where ω₀² = k/m (natural frequency)
```

**Poles of G(ω|τ)**:
```
ω₁,₂ = ±√(ω₀² - γ²) + iγ

where γ = c/(2m) > 0 (damping rate)
```

**Green's Function** (Equation 3.1.22):
```
g(t|τ) = -(i/(ω₁ - ω₂))[e^(iω₁(t-τ)) - e^(iω₂(t-τ))]

with ω₁,₂ = ±√(ω₀² - γ²) + iγ
```

**Key Features**:
- **Causality**: g(t|τ) = 0 for t < τ (enforced by residue theory)
- **Damping**: Exponential decay factor e^(-γ(t-τ)) ensures bounded response
- **Oscillation**: Real part of ω₁,₂ produces oscillatory response at frequency √(ω₀² - γ²)

---

## 4. EQUIVALENCE: DISCONTINUOUS FORCING ↔ INITIAL CONDITION JUMPS

### 4.1 The Fundamental Equivalence Principle

Duffy does not explicitly state this equivalence in the classical sense (Pleshkov's Formula 3.3), but the mathematical framework supporting it is fully present:

**Key Remark** (Chapter 3.1, Page 112):
> "Although we will use Equation 3.1.5 as the fundamental definition of the Green's function... we can also find it by solving the initial-value problem:
>
> d^n u/dt^n + a_1 d^(n-1)u/dt^(n-1) + ... + a_n u = 0,  τ < t
>
> with initial conditions:
> u(τ) = u'(τ) = ... = u^(n-2)(τ) = 0,  and u^(n-1)(τ) = 1"
>
> "The Green's function is related to u(t) via g(t|τ) = u(t - τ)H(t - τ)."

### 4.2 Initial Conditions and Green's Functions

**Structural Equivalence**:

For an n-th order ODE, the Green's function is obtained by:
1. Setting RHS = δ(t - τ) (impulsive forcing), OR
2. Solving homogeneous ODE with "artificial" jump in (n-1)-th derivative: u^(n-1)(τ⁺) - u^(n-1)(τ⁻) = 1

Both approaches yield identical Green's function g(t|τ).

**Physical Interpretation**:
- **Impulsive Forcing**: System receives sudden impulse of "unit strength"
- **Jump Condition**: System's highest-order derivative undergoes unit jump at t = τ

These are **mathematically equivalent** because:
- A unit impulse ∫ δ(t - τ) dt = 1 equals the integral of the jump condition
- The n-fold time integration from forcing to state variables converts the impulse into an n-fold derivative jump, which reverse-translates to initial condition jumps

### 4.3 Superposition Integral: Connecting Forcing to Response

**Duffy's Superposition Principle** (Equation 3.1.8, Page 112):

```
        t
y(t) = ∫ g(t|τ)f(τ)dτ
       0
```

**Derivation Logic** (Pages 112-113):
1. Compute y'(t), y''(t), ..., y^(n)(t) using Leibniz rule
2. Require g(t|τ) to satisfy: g(t|τ) = g'(t|τ) = ... = g^(n-2)(t|τ) = 0 at t = τ, and g^(n-1)(t|τ) = 1
3. Substitute into the ODE:
   ```
   d^n y/dt^n + ... + a_n y = f(t) + ∫₀^t [L{g(t|τ)}]f(τ)dτ
   ```
4. The bracketed term vanishes because g(t|τ) satisfies L{g} = δ(t - τ)

**Key Insight**: 
- The superposition integral shows that the overall response is a weighted superposition of impulse responses
- Each infinitesimal forcing element f(τ)dτ produces an impulse response g(t|τ) at time t
- The total response is the integral of all such responses

---

## 5. HIERARCHICAL POSITION RELATIVE TO OTHER APPROACHES

### 5.1 Duffy's Scope and Limitations

**Strengths**:
1. **Rigorous Mathematical Foundation**: Uses distribution theory, test functions, admissible functions
2. **Unified Framework**: Covers ODE and PDE through same Green's function methodology
3. **Extensive Practical Examples**: Circuit theory, structural mechanics, integral equations
4. **Transfer Function Connection**: Links impulse response to Laplace and Fourier transforms
5. **Causality Analysis**: Rigorous treatment via contour integration and residue theory (Pages 113-115)

**Limitations**:
1. **Assumes Linear Systems**: All differential operators are linear
2. **Smooth Coefficients**: No treatment of discontinuous or piecewise smooth coefficients
3. **No Sliding Modes**: Does not address multivalued solutions or Filippov sliding behavior
4. **No Nonsmooth Theory**: Differential inclusions and nonsmooth analysis not covered
5. **Classical Differential Equations**: Assumes RHS can be interpreted in distributional sense; does not go to measure-theoretic setting

### 5.2 Relationship to Other Frameworks

**Compared to Samoilenko-Perestyuk (Framework 32)**:
- **Samoilenko-Perestyuk**: Impulsive differential equations with discontinuous dynamics, sliding modes
- **Duffy**: Classical Green's functions for smooth differential equations with impulsive forcing
- **Hierarchy**: Samoilenko-Perestyuk is MORE GENERAL (includes Duffy as special case of continuous impulses)

**Compared to Filippov (Framework 6)**:
- **Filippov**: Differential equations with discontinuous RHS; multiple solution concepts
- **Duffy**: Solves equations with delta-function RHS via Green's functions
- **Hierarchy**: Filippov's discontinuous RHS includes delta functions as measure-theoretic limit; Duffy uses distributional approach

**Compared to Kiseleva (Framework 40 - Differential Inclusions)**:
- **Kiseleva**: Multivalued RHS f(t,x) ∈ F(t,x); three solution concepts
- **Duffy**: Single-valued, distributional RHS
- **Hierarchy**: Kiseleva is more general (multivalued > single-valued)

**Compared to Pleshkov (Framework 33 - Algorithmic Synthesis)**:
- **Pleshkov**: Formula 3.3 shows impulse ↔ IC jump equivalence algorithmically
- **Duffy**: Demonstrates this equivalence mathematically through Green's function definition
- **Relationship**: Complementary - Duffy provides theoretical basis, Pleshkov provides algorithmic implementation

**Compared to Camporesi (Frameworks 11-12 - Impulsive Response Method)**:
- **Camporesi**: Focused specifically on impulse response method via factorization
- **Duffy**: Impulse response is one technique among many for finding Green's functions
- **Relationship**: Duffy's Chapter 2.7 (Circuit Theory) and Section 3.1 align with Camporesi's approach

**Compared to Yang (Framework 37 - Impulsive Control)**:
- **Yang**: Impulsive control with state jumps x(τ⁺) = x(τ⁻) + U(k, x(τ⁻))
- **Duffy**: Green's functions for linear systems with impulsive forcing
- **Hierarchy**: Yang is more applied (control synthesis), Duffy is theoretical foundations

### 5.3 Position in Hierarchical Framework

**Proposed Classification Level**: 
- **Level 3 (Theoretical Foundations)**

**Justification**:
- Duffy provides the mathematical rigorous treatment of distribution theory, delta functions, and Green's functions
- These are foundational concepts that underpin more specialized approaches (Samoilenko-Perestyuk, Filippov, Yang, Kiseleva)
- The book bridges classical ODE theory with impulsive systems through the Green's function framework
- Widely cited reference for graduate-level mathematical treatment of impulse response

---

## 6. DIRAC DELTA FUNCTION VS. GENERAL FORCING

### 6.1 Duffy's Treatment of Delta vs. Smooth Forcing

**Both Delta and Smooth Forcing Uses Same Framework**:

For smooth f(t):
```
y(t) = ∫₀^t g(t|τ)f(τ)dτ
```

For delta forcing f(t) = δ(t - t₀):
```
y(t) = ∫₀^t g(t|τ)δ(τ - t₀)dτ = g(t|t₀)H(t - t₀)
```

**Key Observation**:
The same Green's function g(t|τ) works for both because the superposition integral naturally "filters" the delta function via the sifting property.

### 6.2 Step Function (Heaviside) Forcing

**Connection to Delta Function**:
```
H(t - τ) = ∫_{-∞}^t δ(s - τ)ds
```

**Response to Step Forcing**:
If f(t) = H(t - t₀) (unit step at t = t₀), then:
```
y(t) = ∫_{t₀}^t g(t|τ)dτ  (integral of Green's function)
```

**Example**: For RL circuit with step voltage V₀:
```
i(t) = (V₀/R)[1 - e^(-Rt/L)]  (response asymptotes to V₀/R)
```

This is the integral of the impulse response g(t|τ) = (e^(-R(t-τ)/L))/L.

---

## 7. MATHEMATICAL RIGOR AND LIMITATIONS

### 7.1 Rigorous Elements

**Distribution Theory Foundation**:
- Test functions and admissible functions properly defined (Page 92)
- Weak convergence and distribution definition explicit (Pages 92-93)
- Properties of delta function derived, not merely stated
- Multidimensional delta functions with proper scale factors (Table 2.5.2)

**Green's Formulas**:
- Green's First and Second Formulas rigorously proved (Pages 76-77)
- Connection to boundary-value problems and eigenvalue problems established (Pages 79-87)

**Causality**:
- Causality enforced via contour integration (Pages 113-115)
- Poles of transfer function must lie in upper half-plane
- Physical interpretation: impulse effects cannot precede the impulse

### 7.2 Limitations

**1. Linear Systems Only**:
- All treatment assumes linear differential operators L{·}
- Nonlinear forcing or coefficients not addressed

**2. Smooth Coefficients**:
- Coefficients a₁, a₂, ..., a_n assumed constant (or smooth functions of x)
- Discontinuous coefficients not treated
- Piecewise smooth systems not systematically addressed

**3. Measure-Theoretic vs. Distributional**:
- Uses Schwartz distributions (not Borel measures)
- Does not discuss measure-theoretic impulses (Dirac measure)
- Connection to absolutely continuous measures not made explicit

**4. No Multivalued RHS**:
- Only single-valued f(t) or δ(t - τ) considered
- Differential inclusions not covered (unlike Kiseleva)

**5. Steady-State Analysis**:
- Initial conditions assumed zero
- For nonzero initial conditions, must superpose homogeneous solution
- No unified treatment of general initial conditions with impulses

---

## 8. COMPARISON TABLE: DUFFY VS. RELATED FRAMEWORKS

| Aspect | Duffy | Samoilenko-Perestyuk | Filippov | Kiseleva |
|--------|-------|---------------------|----------|----------|
| **Distribution Theory** | Yes (rigorous) | Implicit | Implicit | Implicit |
| **Delta Function RHS** | Central | Part of classification | Measure-theoretic | Limit case |
| **Discontinuous RHS** | No | Yes (3 types) | Yes (central) | Multivalued RHS |
| **Sliding Modes** | No | Yes | Yes | Yes |
| **Linear Operators** | Yes (only) | Both linear & nonlinear | Both | Both |
| **Initial Conditions** | Zero assumed | General | General | General |
| **Impulse ↔ IC Jump** | Mathematical | Explicit equivalence | Implicit | Not addressed |
| **Green's Functions** | Central | Component | Not primary tool | Not primary tool |
| **Practical Applications** | Circuit, structures | Mechanics, control | Control, mechanics | Mechanics |

---

## 9. RELEVANCE TO LITERATURE REVIEW

### 9.1 HIGH RELEVANCE

**Strong Connection to Core Topics**:
1. **Impulse Response**: Chapter 2.7 and 3.1 provide foundational definition and computation
2. **Delta Function**: Chapter 2.5 offers rigorous distribution-theoretic treatment
3. **Linear Systems**: Comprehensive coverage of LTI systems via Green's functions
4. **Superposition Integral**: Central to understanding convolution and impulse response equivalence

### 9.2 MODERATE RELEVANCE

**Secondary Connections**:
1. **Connection to Transfer Functions**: Laplace and Fourier transforms link impulse response to frequency domain
2. **Causality**: Rigorous analysis via contour integration
3. **Boundary-Value Problems**: Different framework than impulse response, but uses same Green's function formalism

### 9.3 LIMITED RELEVANCE

**Not Directly Addressing**:
1. **Discontinuous Coefficients**: Book assumes smooth coefficients
2. **Multivalued RHS**: Only single-valued forcing considered
3. **Filippov Sliding Modes**: Not addressed
4. **Impulsive Control**: Control synthesis not covered (reference Yang for this)

---

## 10. CITATIONS AND REFERENCES

**Key Chapters for Literature Review**:
- **Chapter 2, Section 2.5**: "The Dirac Delta Function" (Pages 66-94) — Distributional theory
- **Chapter 2, Section 2.7**: "What Is a Green's Function?" (Pages 79-108) — Foundational examples
- **Chapter 3, Section 3.1**: "Initial-Value Problems" (Pages 91-113) — Impulse response for ODE
- **Chapter 3, Section 3.2**: "The Superposition Integral" (Pages 97-108) — Convolution formula
- **Examples 2.7.1-3**: Circuit theory, statics, integral equations (Pages 99-105)
- **Examples 3.1.1-2**: Damped harmonic oscillator (Pages 111-115)

**Additional Resources**:
- Chapter 4-6: Green's functions for Wave, Heat, and Helmholtz equations (extensive PDE treatment)
- Appendix references Figueiredo Camargo et al. (2013) on "one-sided" vs. "two-sided" Green's functions

---

## 11. CONCLUSION

**Duffy's "Green's Functions with Applications"** is a **foundational reference** for understanding impulse response and the mathematical theory of Dirac delta functions in the context of linear differential equations. The book provides:

1. **Rigorous distributional framework** for discontinuous forcing
2. **Clear definition** of Green's functions as impulse responses
3. **Practical techniques** for computing impulse responses via Laplace/Fourier transforms
4. **Bridge between** classical ODE theory and modern impulsive systems

**Position in Hierarchy**:
- **Level 3 (Theoretical Foundations)** — Provides mathematical underpinning for impulse response theory
- **Prerequisite for**: Samoilenko-Perestyuk, Filippov, Yang frameworks
- **Complementary to**: Pleshkov (algorithmic synthesis), Camporesi (impulse response method)

**Recommended Use**:
- Reference for **rigorous treatment of distributions and delta functions**
- Foundation for understanding **impulse response as Green's function**
- Background for **linear systems theory with impulsive forcing**

---

**Document created**: August 17, 2026
**Analysis focus**: Impulse response, discontinuous forcing, initial conditions, Dirac delta function, Green's functions
