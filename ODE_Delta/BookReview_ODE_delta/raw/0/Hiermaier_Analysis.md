# Hiermaier: Structures Under Crash and Impact — Treatment of Discontinuities via Shock Waves

## Reference
**Book**: Structures Under Crash and Impact: Continuum Mechanics, Discretization and Experimental Characterization  
**Author**: Stefan Josef Hiermaier, Fraunhofer Institut für Kurzzeitdynamik (Ernst-Mach-Institut), Freiburg, Germany  
**Publisher**: Springer  
**Date**: 2008  
**Pages**: ~500+  
**Scope**: Comprehensive treatment of dynamic loading conditions (crash, impact, blast) with emphasis on shock waves, nonlinear constitutive equations, and numerical methods (hydrocodes)

---

## CENTRAL MISSION: Shock Waves as Mathematical Discontinuities in Impact Mechanics

### The Research Problem

Hiermaier's book addresses a fundamentally different class of discontinuities than the purely mathematical frameworks (Graef, Hassan, Heikkila) or classical state-space approaches (Hespanha, Chen):

**Impact and Crash Loading Context:**
```
Automotive crash:  10-50 m/s (strain rates: 10^-2 to 10^2 s^-1)
Hypervelocity impact: km/s range (strain rates: >10^6 s^-1)

Under such extreme dynamic loading:
- Elastic wave speeds increase with pressure
- Pressure waves "steepen" as they propagate
- Nonlinear compression behavior creates discontinuous shock fronts
```

**The Discontinuity Arises Physically:**
Unlike theoretical frameworks treating discontinuities as mathematical artifacts, Hiermaier derives shock waves from first principles:
1. Nonlinear constitutive behavior (pressure-dependent moduli)
2. Wave propagation in dispersive media
3. Superposition of wave components → wave steepening
4. Limit process creates discontinuous shock front

---

## KEY INSIGHT: Discontinuities from Dispersion (Section 4.3.1)

### Wave Propagation in Nonlinear Media

**Classical elastic wave speed:**
```
c_elastic = c₀ = √(-1/ρ₀ · ∂p/∂V)|_S
```

**Problem when material is nonlinear:**
Different pressure levels have different sound speeds because the adiabatic compression modulus (∂p/∂V) varies with pressure.

**Figure 4.6 Pattern (Conceptual):**
```
Pressure p
    ↑
    │     Elastic region (steep slope = fast wave)
    │    /
    │   /
    │  /  Elastic-plastic (moderate slope = medium speed)
    │ /
    │/   Plastic region (shallow slope = slow speed)
    └─────────────────→ Volume V
    
For rapid compression from (p₀,V₀) to (p₃,V₃):
- Higher pressure waves propagate faster
- Lower pressure waves propagate slower
- Faster waves catch up to slower waves
- Wave fronts steepen → discontinuity forms
```

**Mathematical Result:**
```
Dispersion (variation of sound speed with pressure)
  ↓
Wave steepening during propagation
  ↓
Limit: Discontinuous shock front with infinitesimal thickness
```

This is the **continuous-to-discontinuous transition** arising from physical nonlinearity.

---

## THEORETICAL FRAMEWORK: Rankine-Hugoniot Equations (Section 4.4.3)

### Jump Conditions Across Shock Front

For a shock wave propagating through a medium, Rankine-Hugoniot relations establish the **discontinuous jump** in state variables:

**State variables jump:**
```
At shock front (moving with velocity V_shock):

Property         | Before shock | After shock | Jump
─────────────────────────────────────────────────────
Density         | ρ₁           | ρ₂          | Δρ
Particle velocity| v₁           | v₂          | Δv  
Pressure        | p₁           | p₂          | Δp
Internal energy | e₁           | e₂          | Δe
```

### Mass Conservation Across Shock:
```
ρ₁(V_shock - v₁) = ρ₂(V_shock - v₂)
```

### Momentum Conservation:
```
p₁ + ρ₁(V_shock - v₁)v₁ = p₂ + ρ₂(V_shock - v₂)v₂
```

### Energy Conservation (Energy Dissipation):
```
e₁ + ½(V_shock - v₁)v₁² + p₁V₁ 
  = e₂ + ½(V_shock - v₂)v₂² + p₂V₂ + D_dissipation
```

**Critical Property:**
The entropy INCREASES across shock front (Section 4.4.5):
```
s₂ > s₁  (irreversible energy dissipation)
```

This **irreversibility distinguishes shock waves from elastic waves** — it's an inherent mathematical consequence of the jump conditions.

---

## SHOCK THERMODYNAMICS: From Dispersion to Discontinuity (Section 4.4)

### Precondition for Shock Wave Evolution:

**Dispersion Effect (necessary):**
```
Sound speed c = √(∂p/∂ρ)|_s must vary with pressure
```

This variation enables faster waves to catch slower ones, creating steepening.

**Shock Front Dimensions (Section 4.3.2):**
```
Shock thickness: ~10-100 molecular mean free paths
(Extremely sharp discontinuity at macroscopic scale)
```

### Thermodynamic Conditions Upon Shock Transit:

**Temperature rise:**
```
During shock compression, kinetic energy of bulk motion
converts to thermal (random microscopic motion)
Result: T₂ > T₁ (always)
```

**Pressure-volume relationship on Hugoniot curve:**
```
For elastic material: smooth p-V curve
For shock: curve exhibits kink (change in slope)
at shock initiation point
```

---

## NONLINEAR EQUATIONS OF STATE: Mathematical Framework for Shocks (Chapter 4.5)

### Why Standard Linear EOS Fails:

**Linear equation (isothermal):**
```
p = K(ρ - ρ₀)/ρ₀
```
**Problem:** Doesn't account for energy changes → can't describe temperature/internal energy effects in shocks.

### Generalized Mie-Grüneisen EOS (Section 4.5.1):

**Free energy decomposition:**
```
ψ = ψ_cold(V) + ψ_th(V,T) + ψ_e(V,T)

where:
- ψ_cold    : 0K potential energy (interatomic forces)
- ψ_th      : Thermal vibration contribution
- ψ_e       : Electron excitation contribution
```

**Pressure formulation:**
```
p = -∂ψ/∂V = p_cold(V) + Γ(V)·ρ·c_v·T
```

where **Γ(V)** is the Grüneisen parameter (material-dependent).

**Key Feature:** Energy-dependent (unlike linear EOS).

### Polynomial Nonlinear EOS (Section 4.5.2):

**General form (practical for hydrocodes):**
```
p = K₁μ + K₂μ² + K₃μ³ + (B₀ + B₁μ)ρ₀e
```

where:
```
μ = (ρ/ρ₀) - 1     (compression measure)
e                  (specific internal energy)
K_i, B_i          (material constants, different for compression/expansion)
```

**Significance:**
- Accounts for **pressure dependence of sound speed**
- Energy term (B₀ + B₁μ)ρ₀e enables **entropy increase** across shocks
- Multiple parameters capture nonlinear behavior across wide pressure/energy range

### Calibration from Shock Experiments (Section 4.5.2):

**Standard procedure:**
1. Conduct shock impact experiments (plate impact tests)
2. Measure: impact velocity, shock velocity, particle velocity
3. Apply Rankine-Hugoniot equations → extract state pairs (p₁,ρ₁,e₁) and (p₂,ρ₂,e₂)
4. Multiple experiments at different pressures give **Hugoniot curve** in p-V-e space
5. Fit polynomial EOS parameters K_i to this experimental data

---

## POSITION IN THE 24-FRAMEWORK HIERARCHY

**Hiermaier's Unique Role: Physical Discontinuities from Nonlinear Continuum Mechanics**

```
Theoretical Foundations (Pure Mathematics)
    ├─ Cooper (Distributions)
    ├─ Graef (Filippov, multivalued)
    ├─ Hassan (Angular continuity)
    └─ Heikkila (Monotone iterations)
         ↓
Classical State-Space Theory (Linear Systems)
    ├─ Hespanha (Transfer functions, impulse response)
    ├─ Chen (State-space fundamentals)
    ├─ d'Andréa-Novel (Transfer functions)
    └─ Dahleh (Classical control theory)
         ↓
Nonlinear Mechanics & Discontinuities (Physical Origin)
    └─ Hiermaier (Shock waves, impact, crash) ← HERE
         ↑
         Bridges from pure math to physical reality
         Shows HOW mathematical discontinuities arise naturally
```

**Distinction from prior frameworks:**
- **Graef/Hassan/Heikkila**: "How do we solve ODEs with discontinuous RHS?"
- **Hespanha/Chen**: "How do linear systems respond to impulses?"
- **Hiermaier**: "Why do discontinuities form physically? What are the governing equations?"

---

## TREATMENT OF DISCONTINUITIES IN PRACTICE: Hydrocodes (Chapter 5)

### The Computational Challenge:

**The Paradox:**
```
Shock waves are mathematically discontinuous (jump in p, ρ, v, T)
But numerical methods use finite differences on discrete grids
→ Must represent discontinuity using finite element/finite volume
```

### Solution Strategy (Section 5.7.7: "Finite Element Methodologies for Discontinuities"):

**Artificial viscosity approach:**
```
Add small viscous term to momentum equation:
ρ(dv/dt) = -∂p/∂x - ∂(ρν_artificial·∂v/∂x)/∂x
```

**Effect:**
- Spreads shock over several grid cells (not ideal, but computational necessity)
- Creates smooth transition instead of true discontinuity
- Width of artificial shock ≈ grid spacing

**Alternative: Adaptive Mesh Refinement**
```
Automatically refine grid wherever gradients are large
→ Sharper shock representation as resolution increases
→ Limit: discontinuity recovered
```

### Shock Simulation in Hydrocodes (Section 5.10):

**Key aspects:**
1. **Lagrangian description**: Grid moves with material (follow particles)
   - Tracks material interfaces clearly
   - Problem: grid distortion under large deformations
   
2. **Eulerian description**: Grid fixed in space (material flows through)
   - Handles large deformations naturally
   - Problem: material interfaces blur
   
3. **ALE (Arbitrary Lagrangian-Eulerian)**: Hybrid approach
   - Uses Lagrangian tracking where smooth
   - Switches to Eulerian where discontinuities develop
   - Balances accuracy and stability

---

## COMPARISON TO OTHER FRAMEWORKS IN 24-PAPER ECOSYSTEM

| Aspect | Hiermaier | Graef | Hassan | Heikkila | Hespanha |
|--------|-----------|-------|---------|----------|----------|
| **Discontinuity Source** | Physical (shock formation) | Mathematical (Filippov) | Mathematical (angular continuity) | Mathematical (monotone iteration) | Mathematical (impulse) |
| **Equations** | PDE (conservation laws) | ODE (smooth/multivalued) | ODE (single-valued) | ODE (monotone) | ODE (linear state-space) |
| **Nonlinearity** | Constitutive (σ=f(ε,ε̇,...)) | Incorporated (multivalued) | Implicit (cone structure) | General (via monotone techniques) | Linear |
| **Shock/Jump** | Yes (Rankine-Hugoniot) | Yes (Filippov solution) | No (continuous along cone) | No (monotone paths) | Yes (impulse response) |
| **Entropy/Energy** | Explicit (dissipation across shock) | Implicit (convex hull) | Not primary | Not primary | Not addressed |
| **Equation of State** | Nonlinear (Mie-Grüneisen, polynomial) | Not needed | Not needed | Not needed | Linear (implicit) |
| **Application Domain** | Impact/crash/blast | Switched systems | Scalar ODE analysis | General discontinuous ODE | Control theory |

---

## SPECIFIC TREATMENT: How Hiermaier Connects Discontinuity to Initial Condition Jump

### Shock-Induced State Changes:

**Before shock arrival (uniform initial state):**
```
ρ₁, v₁=0, p₁=p₀, T₁=T₀
(Material at rest, ambient pressure/temperature)
```

**Shock impact (discontinuous jump at shock front):**
```
Across infinitesimal shock thickness:
ρ  jumps from ρ₁ → ρ₂  (compression)
v  jumps from v₁ → v₂  (material suddenly accelerated)
p  jumps from p₁ → p₂  (pressure spike)
T  jumps from T₁ → T₂  (heating via shock)
```

**This is equivalent to an instantaneous initial condition change:**
```
For particle initially in state 1, shock transforms it to state 2
From particle perspective: "free vibration" in state 2 begins
Exactly as if initial condition x(0) changed discontinuously
```

**Mathematical Representation:**
```
Before shock:  x₁(t) = solution to ẋ = f(x) with x(0) = state₁
After shock:   x₂(t) = solution to ẋ = f(x) with x(0) = state₂  
Discontinuity: state₂ = shock_transformation(state₁)
               (given by Rankine-Hugoniot relations)
```

---

## EXAMPLE: Shock in an Elastic-Plastic Material

### Free Vibration Before Shock:
```
Initial state: ρ = ρ₀, v = 0, σ = 0, εᵖ = 0

Free response (no input):
dσ/dt = E(dε/dt) = E·v      (elastic behavior)
```

### Shock Passage:
```
Rankine-Hugoniot jump:
Δρ = ρ₂ - ρ₁
Δv = v₂ - v₁  
Δp = p₂ - p₁  (shock-induced compression)
Δe = e₂ - e₁  (internal energy increase from shock heating)
```

### After-Shock Evolution:
```
New initial condition:
ρ(0⁺) = ρ₂
v(0⁺) = v₂  
Shock heating causes T(0⁺) = T₂ > T₁

Now material continues from this new state:
dσ/dt = E(T₂)·(dε/dt) + thermal_softening_term

Evolution depends on:
- New state variables (ρ₂, v₂, e₂)
- Modified material properties (E depends on T)
- Subsequent wave reflections
```

**Key insight:** The shock is the **discontinuous transformation** between two equilibrium states. After shock passes, "free vibration" resumes with a new initial condition.

---

## SUMMARY

**Hiermaier's contribution is uniquely phenomenological** because:

✓ **Physical Origin** — Derives discontinuities from nonlinear constitutive behavior  
✓ **Wave Steepening** — Shows HOW dispersion creates shock fronts  
✓ **Jump Conditions** — Rankine-Hugoniot relations for discontinuous jumps  
✓ **Energy Dissipation** — Entropy increase across shocks (irreversibility)  
✓ **Nonlinear EOS** — Mie-Grüneisen and polynomial forms capture shock behavior  
✓ **Computational Treatment** — Artificial viscosity, adaptive mesh for shock representation  
✓ **Experimental Calibration** — Shock experiments measure EOS parameters  

**Why Hiermaier matters for discontinuous systems:**

Hiermaier bridges the gap between **pure mathematical frameworks** (Graef, Hassan, Heikkila) and **applied mechanics**. Rather than asking "how do we solve ODEs with discontinuous RHS," Hiermaier shows:

1. **Discontinuities arise naturally** from nonlinear propagation in solids
2. **Rankine-Hugoniot equations** govern the jump (analogous to impulse response)
3. **Thermodynamic constraints** (entropy increase) determine allowable shock states
4. **Numerical methods** must carefully represent discontinuities via artificial viscosity or adaptive refinement

**Three-tier understanding of discontinuities:**

1. **Mathematical (Graef/Hassan)**: "These ODEs have solutions despite discontinuous RHS"
2. **Physical (Hiermaier)**: "Here's why discontinuities form, and what governs them"
3. **Computational (Hydrocodes)**: "Here's how to calculate shocks with finite methods"

Hiermaier provides **layer 2** — the physical justification for why mathematical frameworks exist at all.

---

## COMPLETE POSITION IN FRAMEWORK

**Hiermaier's unique role: Physical discontinuities from nonlinear continuum mechanics**

```
Theoretical Mathematics
    ├─ Cooper (Distributions — axioms)
    ├─ Graef (Filippov — multivalued solutions)
    ├─ Hassan (Angular continuity — weaker conditions)
    └─ Heikkila (Monotone iterations — constructive)
         ↓
Applied Mathematics (State-space & impulse response)
    ├─ Hespanha (Transfer functions — impulse convolution)
    ├─ Chen (State-space — foundational)
    ├─ d'Andréa-Novel (Frequency domain)
    └─ Others (Classical control)
         ↓
Physical Nonlinear Mechanics (WHERE discontinuities originate)
    └─ Hiermaier (Shock waves from dispersion, Rankine-Hugoniot) ← UNIQUE ROLE
         ↓
         Shows: Why discontinuities form physically
         Shows: How to represent them computationally
         Shows: How thermodynamics constrains solutions
```

This is the **25th framework** — not purely mathematical, not purely control-theoretic, but the **physical foundation** for all the others.
