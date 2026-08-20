# Haidekker: Linear Feedback Controls — The Essentials (2nd Edition)

## Reference
**Book**: Linear Feedback Controls: The Essentials, Second Edition  
**Author**: Mark A. Haidekker, College of Engineering, University of Georgia  
**Publisher**: Elsevier  
**Date**: 2020  
**Pages**: ~380  
**Scope**: Essential practical and theoretical foundations of linear feedback control systems with emphasis on practical implementation and design examples

---

## CENTRAL MISSION: Essentials-Focused Practical Control Engineering

### The Textbook Philosophy

**Goal**: Provide essential (non-comprehensive) treatment bridging theory and practical control implementation:

1. **Mathematical Foundations** (Chapters 1-4) — Laplace, z-transforms, signals
2. **Practical Examples** (Chapters 5-6) — Temperature control, positioning system
3. **Design Tools** (Chapters 7-13) — State-space, block diagrams, stability, Bode, root locus
4. **Real-World Implementation** (Chapters 14-17) — Circuits, microcontrollers, PID, applications

**Target audience**: Undergraduate and graduate engineering students needing practical control knowledge without encyclopedic breadth.

**Unique approach**: **Two parallel tracks** showing continuous and discrete-time solutions for same problem.

---

## TREATMENT OF DISCONTINUITIES AND NONLINEARITIES

### Chapter 9: Linearization of Nonlinear Components

**Critical for practical systems:**
```
Real systems are nonlinear:
- Saturation (amplifiers, motors, actuators)
- Friction (nonlinear damping)
- Hysteresis (magnetic systems)
- Dead zones (relay systems)

But control tools (Laplace, frequency response) assume linearity!
```

**Section 9.1: Analytical Linearization**
```
Nonlinear function: y = f(x)

Taylor series around operating point x₀:
  f(x) ≈ f(x₀) + f'(x₀)(x - x₀)
  
Define perturbations:
  Δx = x - x₀
  Δy = y - f(x₀)
  
Linearized model:
  Δy = K·Δx,  where K = f'(x₀) = gain at operating point
```

**Example: Motor speed control**
```
Nonlinear actuator: τ_motor = K_m·i^2  (current squared!)

Linearization at operating point i₀:
  dτ/di|_{i₀} = 2K_m·i₀ = K_linearized
  
Linearized model: τ ≈ τ₀ + K_linearized·(i - i₀)

Valid only near operating point!
Far from i₀, linearization breaks down
```

**Section 9.5: Saturation Effects**

**Practical discontinuity:**
```
Actuator saturation:
         ┌─────────── U_max
        ╱
  y = U  (linear region)
        ╲
         └─────────── U_min

Hard discontinuity at U_max, U_min
Controller can't increase output beyond limits
```

**How it manifests:**
```
Control signal from controller: u(t)
Actual input to system: u_sat(t) = clip(u(t), [U_min, U_max])

If u(t) > U_max:  u_sat = U_max (not u(t))
If u(t) < U_min:  u_sat = U_min (not u(t))
If U_min ≤ u(t) ≤ U_max:  u_sat = u(t)

Results in:
- Loss of control authority
- Integral windup in PID (Chapter 15)
- Nonlinear behavior near limits
```

**Section 9.2: Multiple Input Variables**

**Linearization in higher dimension:**
```
Nonlinear system: y = f(x₁, x₂, x₃)

Operating point: (x₁₀, x₂₀, x₃₀)

Jacobian matrix:
       ┌                        ┐
       │ ∂f/∂x₁  ∂f/∂x₂  ∂f/∂x₃ │
  K =  │                        │
       └                        ┘
       evaluated at (x₁₀, x₂₀, x₃₀)

Perturbation model:
  Δy = K₁₁Δx₁ + K₁₂Δx₂ + K₁₃Δx₃

Each partial derivative shows coupling
```

---

## HOW HAIDEKKER ADDRESSES DISCONTINUITIES

### Implicit Treatment (Not Direct)

**Haidekker does NOT explicitly cover:**
- Impulse functions δ(t)
- Jump discontinuities in differential equations
- Filippov solutions
- Measure differential equations

**Haidekker DOES implicitly address via:**

1. **Linearization (Chapter 9)**
   - Handles discontinuous nonlinearities
   - Provides systematic approach to saturation
   - Shows how to approximate around operating point

2. **Integral Windup (Chapter 15, Section 15.6)**
   - Practical consequence of saturation
   - Anti-windup strategies
   - Direct address of discontinuous behavior

3. **Two-Point Control (Chapter 1, Section 1.4)**
   - Simplest discontinuous controller
   - On/off switching based on threshold
   - Introduction to bang-bang control

4. **Step Response Analysis (Chapters 2-3, 5-6)**
   - Step input is essentially jump discontinuity
   - Transfer function approach handles step
   - Laplace: L[u_step] = 1/s

### Chapter 15: PID Controller and Integral Windup

**Section 15.6: Integral Windup Problem**

```
PID controller:
  u = K_p·e + K_i·∫e dt + K_d·de/dt

Problem when actuator saturates:
  Controller calculates u_desired
  But actuator outputs only u_sat = clip(u_desired, [U_min, U_max])
  
While saturated:
  Error e might still be nonzero
  Integral term ∫e dt keeps increasing (windup!)
  Then when saturation releases:
    Huge overshoot occurs
    System oscillates badly
```

**Anti-Windup Strategies:**

1. **Saturation Detection**
   ```
   if u_desired > U_max:
     Stop integrating (set de_integral/dt = 0)
     Freeze integral term at current value
   ```

2. **Back-Calculation**
   ```
   If saturated, apply feedback to reduce integral:
     de_integral/dt = e - (u_desired - u_sat)/K_i
   ```

3. **Conditional Integration**
   ```
   Only integrate when not saturated:
     if |u_desired| ≤ U_max:
       de_integral/dt = e
   ```

**Why this matters for discontinuities:**
```
Saturation IS a discontinuity in the actuator!
Integral windup is consequence of discontinuous behavior
Anti-windup is practical approach to handling discontinuity
```

---

## PARALLEL TREATMENT: CONTINUOUS VS. DISCRETE

### Two-Track Pedagogical Approach

**Haidekker's strength: Shows both formulations**

**Example from Chapter 5: Temperature-Controlled Water Bath**

```
CONTINUOUS-TIME
  Differential equation (Section 5.1):
    dT/dt + T/τ = K·u(t)
  
  Transfer function (Section 5.3):
    G(s) = K/(τs + 1)
  
  Step response:
    T(t) = K(1 - e^(-t/τ))
  
  PI controller (Section 5.6):
    u(t) = K_p·e + K_i∫e dt

DISCRETE-TIME
  Difference equation (Section 5.7):
    T[n+1] = T[n] + Δt/τ(K·u[n] - T[n])
  
  Z-transform (Section 5.7):
    G(z) = K·Δt/(z - (1 - Δt/τ))
  
  Sampled response:
    T[n] = K(1 - (1 - Δt/τ)^n)
  
  Digital PI (Section 5.8):
    u[n] = K_p·e[n] + K_i·Σe[k]·Δt

Both approaches solve SAME problem
Shows students when each is appropriate
```

### Chapter 4: Time-Discrete Systems

**Section 4.1: Zero-Order Hold**

**Discontinuity at sampling times:**
```
Continuous signal: x_c(t)  (changes smoothly)
Sampled signal:    x[n] = x_c(n·T)  (discrete points)
Zero-order hold:   x_hold(t) = x[n] for t ∈ [nT, (n+1)T)

Between samples:   x_hold is constant (discontinuous jumps!)

This is EXACTLY an impulsive/hybrid system:
  Continuous evolution between samples
  Discrete jumps at sample times
  Zero-order hold = nearest discrete value
```

**Why important for discontinuities:**
```
Digital control inherently has jumps at sample times!
Every digital controller is a hybrid system
Zero-order hold models practical DAC behavior
```

---

## PRACTICAL ELECTRONICS AND IMPLEMENTATION

### Chapter 14: Building Blocks of Linear Systems

**Section 14.2: Time-Continuous Building Blocks**

**Op-amp circuits with practical nonlinearities:**
```
Ideal op-amp (textbook model):
  Δv_out = A(v+ - v-)  with A → ∞
  Unlimited output range

Real op-amp (practical):
  v_out limited to [V_sat-, V_sat+]
  Saturation is sharp discontinuity
  Slew rate limited: |dv_out/dt| ≤ S_rate
```

**Integrator circuit:**
```
V_out = -1/(RC) ∫ V_in dt

Practical reality:
  Initial condition v_out(0) is discontinuous jump
  Can be set via reset switch (also discontinuity)
  Slew rate causes rounding of discontinuities
```

### Section 14.3-14.4: Digital Control with Microcontroller

**Sampling creates discrete times:**
```
Real-time control loop:
  1. Sample sensor at t = nT (discrete time jump)
  2. Compute control law
  3. Output to DAC
  4. Wait until next sample time T_next = (n+1)T (discrete jump)
  5. Repeat

This is fundamentally hybrid:
  Continuous plant dynamics between samples
  Discrete controller updates at sample times
  Zero-order hold creates step discontinuities in control input
```

---

## COMPARISON TO OTHER PEDAGOGICAL TEXTS

| Aspect | Haidekker | Ghosh | Hägglund | Chen |
|--------|-----------|-------|----------|------|
| **Level** | Undergrad/grad essentials | Comprehensive grad | Concise essentials | Advanced grad |
| **Pages** | ~380 | ~800+ | ~136 | ~200 |
| **Practical focus** | HIGH (circuits, code) | Medium | Medium | Low |
| **Linearization chapter** | YES (Ch. 9) | Brief | Not explicit | Not explicit |
| **Saturation/windup** | Detailed (Ch. 15.6) | Not covered | Not covered | Not covered |
| **Discrete time** | Parallel throughout | Chapters 14+ | Brief | Not separate |
| **Application examples** | Extensive (Ch. 17) | Moderate | Few | Few |
| **Design methodology** | Detailed (Ch. 16) | Moderate | Not detailed | Not covered |

**Haidekker's unique contributions:**
1. **Essentials focus** — No fluff, no exhaustive coverage
2. **Linearization chapter** — Systematic approach to nonlinearities
3. **Integral windup** — Practical PID issue with saturation
4. **Parallel discrete/continuous** — Shows both formulations
5. **Circuit implementation** — Op-amps, microcontrollers
6. **Design process** — Chapter 16 on practical design workflow
7. **Real case studies** — Chapter 17 with actual measured data

---

## TREATMENT OF STEP INPUTS (DISCONTINUITIES)

### Chapter 2-3: Systems and Signals

**Step input as discontinuity:**
```
Unit step function:
  u(t) = 0,  t < 0
  u(t) = 1,  t ≥ 0
  
Discontinuity at t = 0!
Graphically: vertical jump from 0 to 1

Laplace transform:
  L[u_step] = 1/s
```

**Step response of first-order system (Section 2.2-2.3):**

```
System: dx/dt + x/τ = Ku(t),  x(0) = 0

Step response:
  x(t) = K(1 - e^(-t/τ))
  
Behavior:
  t = 0⁻: x = 0 (pre-step)
  t = 0⁺: x = 0 (no instantaneous jump for this system)
  t → ∞: x → K (steady state)
  
But if direct feedthrough (D matrix ≠ 0):
  y(t) = Cx(t) + Du(t)
  y(0⁺) = C·0 + D·1 = D (INSTANTANEOUS JUMP!)
```

### Chapter 6: Dynamic Response Performance Metrics

**How to measure response to discontinuity:**

```
Performance metrics for step response:

1. Rise time (t_r):
   Time to go from 10% to 90% of final value
   Measures speed of response to jump

2. Overshoot (OS):
   Max value exceeds steady state
   Results from oscillatory modes

3. Settling time (t_s):
   Time for oscillations to decay to ±5% band
   Measures how long discontinuity disturbs system

4. Steady-state error (e_ss):
   Final offset from desired value
   Measure of accuracy to discontinuous step
```

---

## LINEARIZATION AS DISCONTINUITY HANDLING

### Why Chapter 9 Matters

**Haidekker's approach to discontinuous nonlinearities:**

```
Real nonlinear system with discontinuity:
  Saturation, hysteresis, dead zone, etc.

Step 1: Linearize around operating point
  Model as linear + perturbation
  Discontinuity approximated by smooth nonlinearity

Step 2: Design linear controller
  All classical tools apply

Step 3: Validate on real (nonlinear) system
  Check robustness to nonlinearity
  Verify linearization assumption

This is pragmatic engineering approach!
Not mathematically rigorous (like Graef)
But practical and implementable
```

**Limitation acknowledged:**
```
Valid only near linearization point
Far from operating point, approximation fails
Designer must check ranges and consider saturation
Chapter 15 anti-windup strategies for when saturation happens
```

---

## POSITION IN PEDAGOGICAL HIERARCHY

**Haidekker's role: Practical essentials without overwhelming breadth**

```
Mathematical Foundations
    ├─ Cooper (Distributions)
    └─ Graef (Multi-valued)
         ↓
Pedagogical Texts (Varying Scope)
    ├─ Chen (Advanced, rigorous)
    ├─ Ghosh (Comprehensive, broad)
    ├─ Hägglund (Concise, European)
    └─ Haidekker (Practical, essentials) ← HERE
         ↓
Specialized Theoretical
    ├─ Dishliev (Impulsive asymptotic)
    └─ Brogliato (Measure theory)
         ↓
Applied Specialized + Control Design
    ├─ Haddad (Compartmental, large-scale)
    ├─ Chicurel-Uziel (Nonlinear)
    └─ Falsone, Chalishajar (Beams)
```

---

## SUMMARY

**Haidekker's contribution is uniquely practical** because:

✓ **Essentials-focused** — Covers core topics without encyclopedic breadth  
✓ **Linearization chapter** — Systematic treatment of nonlinearities  
✓ **Saturation/windup** — Practical consequence of discontinuous actuators  
✓ **Parallel discrete/continuous** — Shows both formulations for same problem  
✓ **Circuit implementation** — Op-amps, microcontrollers, practical electronics  
✓ **Anti-windup strategies** — Engineering solutions to saturation discontinuities  
✓ **Design methodology** — Chapter 16 on practical design workflow  
✓ **Real case studies** — Chapter 17 with measured data from actual systems  
✓ **Scilab examples** — All examples in executable code  

**Why Haidekker matters for discontinuous systems:**

While Haidekker doesn't explicitly address impulse functions or mathematical discontinuities, it provides:

1. **Practical linearization** — How to handle discontinuous nonlinearities in design
2. **Saturation treatment** — Inherent discontinuity in all real actuators
3. **Integral windup** — Direct consequence of saturation discontinuity
4. **Hybrid dynamics** — Digital control with zero-order hold is inherently hybrid
5. **Engineering pragmatism** — Linearize + validate approach rather than theoretical rigor

**Positioning:**
- **Graef/Dishliev**: Mathematical rigor for discontinuous systems
- **Haddad**: Control design with constraints (nonnegative or large-scale)
- **Haidekker**: Practical linearization and saturation handling

Haidekker is the **bridge from theory to practice**—showing students how to work with discontinuous actuators and nonlinear components using linear control theory and practical design strategies.

**Critical insight from Chapter 15.6 (Integral Windup):**
Every practical control system encounters discontinuities through actuator saturation. Haidekker shows this is not a rare edge case but a **fundamental practical reality** that good controllers must handle explicitly.
