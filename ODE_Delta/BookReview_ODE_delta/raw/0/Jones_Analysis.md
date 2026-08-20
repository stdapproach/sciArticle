# Jones: Structural Impact — Treatment of Discontinuities via Impulsive Loading

## Reference
**Book**: Structural Impact  
**Author**: Norman Jones, A.A. Griffith Professor of Mechanical Engineering, University of Liverpool  
**Publisher**: Cambridge University Press  
**Date**: 1989 (reprinted 1997)  
**Pages**: ~500+  
**Scope**: Comprehensive treatment of dynamic plastic response of structures (beams, plates, shells) under impact and impulsive loading

---

## CENTRAL MISSION: Discontinuous Forces as Impulsive Loading

### The Research Problem

Jones addresses a critical class of discontinuities: **impulsive forces with infinite magnitude and infinitesimal duration**.

**Definition (Section 3.5.1):**
```
External pressure loadings having:
  - Finite impulse (∫F dt = constant)
  - Infinitely large magnitude (F → ∞)
  - Infinitesimally short duration (T → 0)

These are known as impulsive loads (Dirac delta function).

Mathematical expression:
p = p₀  for 0 ≤ t ≤ T
p = 0  for t > T

Limit: As T → 0 and p₀ → ∞ with p₀·T = I (constant impulse)
Result: Instantaneous velocity change without displacement change
```

**Physical Motivation:**
Unlike Hiermaier (shock waves from continuous nonlinear propagation), Jones studies:
- Impact of a falling mass (discrete event)
- Pressure pulses with finite impulse but variable duration
- Limit case: impulsive loading (instantaneous momentum transfer)

---

## KEY INSIGHT: Conservation of Linear Momentum (Section 3.5.1)

### Newton's Second Law for Impulsive Loading

**Standard form:**
```
F = d(mv)/dt
```

**Integrated form (impulse-momentum theorem):**
```
∫F dt = Δ(mv) = m·Δv

or

I = m(v₂ - v₁)
```

where **I** is the total impulse.

**For impulsive loading:**
```
Given: Finite impulse I = p₀·T  (area under force-time curve)
       As T → 0 and p₀ → ∞ with p₀·T = I (constant)

Result: Instantaneous velocity jump
        V₀ = I/m = p₀·T/m

Discontinuity equation:
v(0⁺) - v(0⁻) = V₀ = I/m
```

**Critical distinction:**
```
Continuous pressure pulse:
  p(t) defined for 0 ≤ t ≤ T
  ∫₀ᵀ p(t) dt = impulse = m·V₀
  Velocity rises gradually from 0 to V₀

Impulsive loading (T → 0):
  Velocity jumps discontinuously from 0 → V₀ at t = 0
  No time for structure to move (w(0⁺) = 0, but ẇ(0⁺) = V₀)
```

---

## GOVERNING EQUATIONS FOR DYNAMIC PLASTIC BEHAVIOR (Section 3.2)

### Equations of Motion

**For beam under dynamic loading:**
```
Q = dM/dx                    ... (3.1) [shear-moment relation]

dQ/dx = -p + m(d²w/dt²)      ... (3.2) [dynamic equilibrium]

K = -d²w/dx²                 ... (3.3) [curvature relation]
```

**Key feature:** Inertia term m(d²w/dt²) appears explicitly in momentum balance.

### Plastic Deformation Constraint

```
|M(x,t)| ≤ M₀     (bending moment bounded by plastic limit)
K(x,t) = -d²w/dx² (curvature from deflection)
```

### Initial Conditions for Impulsive Loading

**Before impact (t < 0):**
```
w(x,0⁻) = 0       (no deflection)
ẇ(x,0⁻) = 0       (no velocity)
```

**After impact (t = 0⁺):**
```
w(x,0⁺) = 0       (no displacement change during impulse)
ẇ(x,0⁺) = V₀(x)   (velocity jump from impulse-momentum conservation)
```

**This is the discontinuous initial condition change caused by impulsive loading.**

---

## SIMPLE EXAMPLE: Simply Supported Beam Under Impulse (Section 3.5)

### Problem Setup

**Beam properties:**
```
Length: 2L
Mass per unit length: m
Plastic limit moment: M₀
Static collapse pressure: p_c = 2M₀/L²
```

**Impulsive loading:**
```
Uniformly distributed impulse: I = ∫₀^∞ p(t) dt
Instantaneous velocity distribution: V₀(x) = I/(2mL)  (uniform)
```

### Analysis via Momentum Conservation

**Newton's second law integrated over impulse duration:**
```
∫₀^T p(t) dt = ∫₀^{2L} m·ẇ(x,0⁺) dx

For uniform velocity distribution:
I = 2mL·V₀

Therefore:
V₀ = I/(2mL)
```

### Phase 1: Free Vibration After Impulse (t > 0)

**Initial conditions for ODE:**
```
w(x,0⁺) = 0
ẇ(x,0⁺) = V₀   (discontinuous jump)
```

**Equations of motion:** (p = 0 for t > 0)
```
d²w/dt² = (1/m)[dQ/dx]
```

**Velocity field ansatz:**
```
ẇ(x,t) = W(t)·(1 - |x|/L)

where W(t) is the midspan velocity (continuous in time, but discontinuous at t = 0)
W(0⁺) = V₀
W(0⁻) = 0
ΔW = V₀  (discontinuity)
```

### Connection: Impulsive Force = Discontinuous Velocity IC

```
Before impulse:  Beam at rest
                 Dynamics: ẇ = 0, ẏ = 0

Impulse occurs:  Momentum transferred to structure
                 ∫F dt = m·V₀

After impulse:   Beam vibrates freely with new IC
                 Dynamics: ẇ = V₀, ÿ = (acceleration from internal forces)
                 
Equivalence:     Impulsive input F = I·δ(t)
                 ⟺ Instantaneous velocity change ẇ(0⁺) = V₀
```

---

## IMPULSIVE LOADING PARAMETER (Section 3.5)

### Dimensionless Representation

**Definition:**
```
η = p₀/p_c    (dynamic load factor for finite pulse)

In the impulsive limit:
I = p₀·T = m·V₀
η → ∞ as T → 0 with I constant
```

**Parameter for impulsive case:**
```
Κ = μV₀²L²/M₀

where:
μ = mass per unit length
V₀ = initial velocity (from impulse-momentum)
L  = beam half-length
M₀ = plastic limit moment
```

This nondimensional parameter contains all information about:
- Magnitude of impulse (via V₀)
- Structure size and mass (L, μ)
- Plastic resistance (M₀)

---

## COMPARISON: PRESSURE PULSE vs. IMPULSIVE LOADING

### Rectangular Pressure Pulse (Section 3.3)

**Applied load:**
```
p(t) = p₀  for 0 ≤ t ≤ T
p(t) = 0   for t > T
```

**Structure response:**
- **Phase 1 (0 ≤ t ≤ T):** Acceleration under applied force, plastic hinges form
- **Phase 2 (T ≤ t ≤ T_final):** Coasting after force removed, plastic hinges propagate
- **Final:** Structure comes to rest with permanent deformation

**Governing ODE (Phase 1):**
```
d²W/dt² = [p₀ - p_c]/m  (approximately constant acceleration)

W(0) = 0
Ẇ(0) = 0  (smooth start)
```

### Impulsive Loading (Section 3.5)

**Applied load:**
```
F(t) = I·δ(t)  (Dirac delta)

Limit: T → 0, p₀ → ∞ with p₀·T = I (constant)
```

**Structure response:**
- **Instantaneous jump (t = 0):** All momentum transferred
- **Phase 1 (0 < t ≤ T'):** Identical to Phase 2 of pulse case
- **Final:** Same permanent deformation as pulse with η → ∞

**Governing ODE (Phase 1):**
```
d²W/dt² = [0 - p_c]/m = -p_c/m  (deceleration from internal forces only)

W(0) = 0
Ẇ(0⁺) = V₀  (discontinuous jump)  ← KEY DISCONTINUITY
```

**Relationship between two cases:**
```
Rectangular pulse (finite T):    Impulse = p₀·T = m·V_end
Impulsive loading (T → 0):      Impulse = I = m·V₀

As T → 0 in pulse case:
- Acceleration phase vanishes (p₀ → ∞ to maintain impulse)
- Initial condition becomes discontinuous jump
- Final result identical for same impulse I
```

---

## IMPACT OF FALLING MASS (Section 3.8)

### Problem: Fully Clamped Beam Struck at Mid-Span

**Setup:**
```
Beam length: 2L
Mass striking at mid-span: M
Initial velocity of mass: V_m (before impact)
```

### Collision Mechanics

**At impact (t = 0⁺):**

Assuming mass remains in contact with beam:
```
Momentum before:  p_before = M·V_m + m_beam·0 = M·V_m

Momentum after:   p_after = (M + m_equiv)·V_0

Conservation: M·V_m = (M + m_equiv)·V_0

Therefore: V_0 = M·V_m/(M + m_equiv)
```

**Discontinuity in velocity:**
```
Striking mass:    V_m → V_0  (decelerates)
Beam mid-span:    0 → V_0    (accelerates)
Structure:        "Free vibration" begins from initial condition ẇ(0⁺) = V_0
```

### Two Phases of Impact Response (Figure 3.15)

**Phase 1 (0 ≤ t ≤ t₁):**
- Plastic hinge forms at impact point
- Two traveling hinges propagate toward supports
- Beam accelerates then decelerates under plastic resistance

**Phase 2 (t₁ ≤ t ≤ T_final):**
- Hinges reach supports and become stationary
- Remaining kinetic energy dissipated
- Final permanent deformation reached

**Analogy to impulsive loading:**
```
Falling mass impact = Impulsive force on structure
Impulse: I = ∫F dt = M·V_m (momentum transfer)
Initial condition: Discontinuous velocity jump = M·V_m/(M + m_equiv)
```

---

## ENERGY DISSIPATION THROUGH PLASTIC DEFORMATION

### Energy Balance

**Initial kinetic energy (before impact):**
```
KE_initial = (1/2)·M·V_m²  (striking mass)
```

**After impact (all energy transferred to structure):**
```
KE_after = (1/2)·(M + m_equiv)·V_0²
         < KE_initial  (some lost in collision)
```

**Plastic dissipation:**
```
Work by plastic hinges during deformation
W_plastic = ∫ M·|K̇| dt

Final equilibrium reached when:
KE_after + W_plastic_remaining = 0
```

**Permanent deformation:**
```
w_final = result of plastic hinge motion

Computed from ODEs with initial condition:
w(0) = 0, ẇ(0⁺) = V_0
```

---

## POSITION IN THE 25-FRAMEWORK HIERARCHY

**Jones's Unique Role: Structural Dynamics Under Impulsive Loading**

```
Pure Mathematics (Discontinuous ODEs)
    ├─ Cooper (Distributions)
    ├─ Graef (Filippov multivalued)
    ├─ Hassan (Angular continuity)
    └─ Heikkila (Monotone iterations)
         ↓
Physical Origins of Discontinuities
    ├─ Hiermaier (Shock waves from nonlinear propagation)
    └─ Jones (Impulsive forces from collisions/impacts) ← HERE
         ↓
         Both show: Discontinuities arise from physical mechanisms
         Different mechanisms:
         - Hiermaier: Nonlinear wave steepening
         - Jones: Momentum transfer to initially stationary structure
         ↓
Applied State-Space & Control Theory
    ├─ Hespanha (Transfer functions, impulse response)
    ├─ Chen (State-space fundamentals)
    └─ Others (Classical control)
```

**Distinction from Hiermaier:**
- **Hiermaier:** Discontinuity develops gradually in space-time via dispersion
- **Jones:** Discontinuity instantaneous at single point (collision)
- **Both:** Governed by conservation laws (momentum in Jones, mass/momentum/energy in Hiermaier)

---

## SUMMARY OF DISCONTINUITY TREATMENT

**Jones addresses discontinuities in three ways:**

### 1. Finite Pressure Pulses (Section 3.3-3.7)
```
Force defined over finite duration T
Continuous initial conditions (w=0, ẇ=0 at t=0)
Smooth transition from rest to acceleration
Plastic hinges develop and propagate
```

### 2. Impulsive Loading Limit (Section 3.5)
```
T → 0, p₀ → ∞ with p₀·T = I (constant impulse)
Discontinuous velocity condition at t=0
w(0⁺) = 0 (no displacement during impulse)
ẇ(0⁺) = V₀ = I/m (instantaneous velocity jump)
Same long-term response as finite pulse with η → ∞
```

### 3. Impact of Falling Mass (Section 3.8-3.9)
```
Discrete event: Mass strikes structure at specific point
Collision time: negligible
Momentum transfer: M·V_m → (M+m_equiv)·V_0
Discontinuous IC: ẇ(0⁺) = M·V_m/(M+m_equiv)
Subsequent deformation: Free vibration from new IC
```

**Unifying principle:**
```
All three cases reduce to same governing equations with
appropriate initial conditions.

General form:
ẇ(x,0⁺) = V₀(x)  [from impulse-momentum conservation]
w(x,0⁺) = 0      [no time for displacement during impulse]

Then solve dynamics for t > 0 with these ICs.
```

---

## KEY EQUATIONS

### Impulsive Loading (Section 3.5)

**Momentum conservation:**
```
p₀·T = m·V₀  → V₀ = p₀·T/m
```

**Response duration (simple supported beam, uniform load):**
```
τ = m·V₀/p_c
```

**Permanent deflection (simple supported beam):**
```
w_f/H = Λ/6  where Λ = μ·V₀²·L²/M₀·H
```

### Falling Mass Impact (Section 3.8)

**Momentum transfer:**
```
M·V_m = (M + m_beam)·V_0
V_0 = M·V_m/(M + m_beam)  [approximately M·V_m/m_beam for heavy beam]
```

**Response duration (fully clamped):**
```
T = m·V_0·L²/(4M₀)
```

**Permanent deflection:**
```
w_f = 6M₀·(v - 1)·τ²/(μ·L⁴)  where v = η (appropriate loading factor)
```

---

## WHY JONES MATTERS FOR DISCONTINUOUS SYSTEMS

**Jones provides the engineering perspective** on how discontinuities arise from impacts and collisions.

Where Hiermaier shows shock waves as continuous limit process of nonlinear waves, Jones shows:
1. **Discrete events** (impact, collision) create discontinuities instantaneously
2. **Impulse-momentum conservation** governs the discontinuous jump
3. **Initial condition discontinuity** ≡ instantaneous velocity change
4. **Subsequent evolution** from new IC via standard dynamics

**Three-tier understanding of discontinuities:**

1. **Mathematical (Graef/Hassan/Heikkila):** "How do we solve ODEs with discontinuous RHS?"
2. **Physical (Hiermaier/Jones):** "Why do discontinuities form, and what governs them?"
   - Hiermaier: Gradual steepening via dispersion
   - Jones: Instantaneous momentum transfer via collision
3. **Computational (Hydrocodes/Finite Elements):** "How do we simulate shocks and impacts?"

Jones shows that impulsive loading naturally produces discontinuous initial conditions, which then evolve via standard ODEs.

---

## COMPLETE POSITION IN 26-FRAMEWORK HIERARCHY

```
Theoretical Mathematics (Pure discontinuous analysis)
    ├─ Cooper (Distributions — foundations)
    ├─ Graef (Filippov — multivalued solutions)
    ├─ Hassan (Angular continuity — geometric approach)
    └─ Heikkila (Monotone iterations — constructive)
         ↓
Physical Mechanisms Producing Discontinuities
    ├─ Hiermaier (Shock waves — continuous limit of dispersion)
    └─ Jones (Impacts — instantaneous momentum transfer) ← FRAMEWORK 25
         ↓
         Both satisfy conservation laws:
         Both create discontinuous states
         Different mechanisms, same mathematical structure
         ↓
Applied State-Space & Control (Linear systems)
    ├─ Hespanha (Impulse response from discontinuous input)
    ├─ Chen (State-space representation)
    ├─ d'Andréa-Novel (Transfer functions)
    └─ Dahleh (Classical control)
         ↓
Specialized & Applied (Nonlinear, large-scale, etc.)
    └─ Many others (15+ frameworks)
```

**Jones's unique contribution:**

Bridges physics and mathematics by showing:
- **Physical impact** (falling mass) → **Discontinuous force** F(t) = I·δ(t)
- **Discontinuous force** → **Discontinuous initial condition** ẇ(0⁺) = V₀  
- **Discontinuous IC** → **Standard ODE evolution** with new initial state

This completes the picture: discontinuities arise not just mathematically, but from real physical phenomena (impacts, collisions, shocks).
