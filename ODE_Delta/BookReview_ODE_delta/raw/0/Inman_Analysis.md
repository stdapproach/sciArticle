# Framework 49: Inman - Engineering Vibration, Fourth Edition

**Author:** Daniel J. Inman  
**Publisher:** Pearson Education  
**Publication Year:** 2014  
**Edition:** Fourth Edition  
**Total Pages:** 720  

---

## CENTRAL MISSION AND UNIQUE CONTRIBUTION

Daniel J. Inman's "Engineering Vibration, Fourth Edition" (2014) is a comprehensive pedagogical text designed for first courses in vibrations/structural dynamics for undergraduates and practicing engineers. Its organizational strategy progresses systematically from free response (Chapter 1) through harmonic excitation (Chapter 2) to **general forced response via impulse response and convolution** (Chapter 3), then extends to multi-DOF systems (Chapter 4), design for vibration suppression (Chapter 5), continuous systems (Chapter 6), experimental modal analysis (Chapter 7), and finite element methods (Chapter 8).

**Unique Contribution:**

Inman's textbook excels in making the **equivalence between impulsive loading and initial velocity jumps** pedagogically transparent and concrete:

1. **Physical motivation first:** Opens Chapter 3 with real engineering examples (aircraft landing, bird strikes on cameras, impact testing with instrumented hammers)
2. **Momentum-impulse principle:** Explicitly derives that impulse $F\Delta t$ produces instantaneous velocity change $v_0 = F\Delta t / m$ with zero displacement change
3. **Impulse response as fundamental tool:** Treats the impulse response $h(t)$ not as an abstract mathematical construct but as the response to initial velocity condition $\dot{x}(0) = 1/m$ with zero initial displacement
4. **Practical algorithms:** Provides step-by-step procedures for computing response to arbitrary (including piecewise discontinuous) loading via Duhamel integral
5. **Extensive examples:** 3.1.1–3.1.3 demonstrate bird strikes, impact testing, double impacts (showing superposition with time delays)
6. **Numerical integration methods:** Section 3.9 covers practical computational algorithms for complex loading

**Hierarchical Position:** Level 1 Bridge Framework (Introductory with Strong Industrial Grounding)

Comparable to **Benaroya** (Framework 48) and **Rao** (Framework 47) in scope and pedagogy; positioned as a textbook that multiple generations of engineering students have learned from.

---

## TREATMENT OF DISCONTINUITIES ON THE RIGHT-HAND SIDE

### Chapter 3: General Forced Response

**Central Governing Equation:**
$$m\ddot{x}(t) + c\dot{x}(t) + kx(t) = F(t), \quad x(0) = 0, \dot{x}(0) = 0$$

**Section 3.1: Impulsive Excitation**

The unit impulse (Dirac delta function) is introduced as the mathematical model for forces acting "with large magnitude for a very short period of time":

**Mathematical Definition (Equation 3.4-3.5):**
$$F(t - \tau) = \begin{cases} 0 & t \neq \tau \\ \infty & t = \tau \end{cases}, \quad \int_{-\infty}^{\infty} F(t-\tau) dt = F_n$$

For unit impulse (impulse magnitude = 1): $\delta(t)$ such that $\int_{-\infty}^{\infty} \delta(t) dt = 1$

**Physical Interpretation via Momentum-Impulse Theorem:**

For a mass at rest just prior to impulse application (denoted $t = 0^-$): $x(0^-) = 0, \dot{x}(0^-) = 0$

Just after impulse (denoted $t = 0^+$):
- **Position:** $x(0^+) = 0$ (unchanged during infinitesimal impulse duration)
- **Velocity:** $\dot{x}(0^+) = v_0 \neq 0$ (velocity jumps instantaneously)

By momentum-impulse principle:
$$m\dot{x}(0^+) - m\dot{x}(0^-) = m v_0 = F_n = F\Delta t$$

Therefore:
$$v_0 = \frac{F\Delta t}{m} = \frac{F_n}{m}$$

**Key Insight (Inman's pedagogy):** "An impulse applied to a single-degree-of-freedom spring–mass–damper system is the same as applying the initial conditions of zero displacement and an initial velocity of $v_0 = F\Delta t / m$."

---

### Section 3.1: Impulse Response Function

**Definition:** The response $h(t)$ of the system to a unit impulse at $t=0$ with zero initial conditions:

$$\ddot{h} + 2\zeta\omega_n\dot{h} + \omega_n^2 h = \delta(t), \quad h(0) = 0, \dot{h}(0) = 0$$

**Solution for Underdamped System** ($0 \le \zeta < 1$):

From physical reasoning (impulse $\delta(t)$ is equivalent to initial velocity $\dot{h}(0) = 1/m$), the impulse response is:

$$h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t) \quad \text{(Equation 3.9)}$$

where $\omega_d = \omega_n\sqrt{1-\zeta^2}$ is the damped natural frequency.

**Critical Properties:**
- $h(t) = 0$ for $t < 0$ (causality: no response before impulse)
- $h(0^+) = 0$ (impulse doesn't immediately displace the mass)
- $\dot{h}(0^+) = 1/m$ (impulse produces velocity jump)
- $h(t) \to 0$ as $t \to \infty$ (exponential decay envelope $e^{-\zeta\omega_n t}$)

**Explicitly Marked Causality in Practice (Example 3.1.1):**

"A 1000 N force acting over 0.01 s provides an impulse of 10 N·s. For a 100 kg mass with natural frequency $\omega_n = 4.47$ rad/s and damping $\zeta = 0.1$, the initial velocity is $v_0 = 10/100 = 0.1$ m/s. Maximum amplitude: $X = v_0 / \omega_d = 0.088$ m."

Response explicitly enforces:
- Initial displacement remains zero: $x(0) = 0$
- Velocity jumps: $\dot{x}(0^+) = 0.1$ m/s
- Subsequent motion governed by $h(t)$ with this initial condition

---

### Section 3.2: Response to Arbitrary Input via Duhamel Integral

**Physical Decomposition:**

Arbitrary loading $F(t)$ is decomposed into infinitesimal impulses $F(\tau)d\tau$ at each prior time $\tau$. Each impulse produces response contribution $h(t-\tau)F(\tau)d\tau$. Superposition yields total response:

$$x(t) = \int_0^t h(t-\tau) F(\tau) d\tau \quad \text{(Equation 3.12, Duhamel Integral)}$$

**Explicit Treatment of Discontinuous Forcing:**

When $F(t)$ is **piecewise continuous with jump discontinuities**, the integral must be split by time intervals:

**Example 3.2.2 (Square Pulse):**

For pulse: $F(t) = \begin{cases} F_0 & 0 \le t \le t_1 \\ 0 & t > t_1 \end{cases}$

Split the convolution:
$$x(t) = \int_0^t h(t-\tau) F(\tau) d\tau = \int_0^{t_1} h(t-\tau) F_0 d\tau + \int_{t_1}^t h(t-\tau) \cdot 0 \, d\tau$$

Result: Two transient phases, each governed by exponentially damped oscillation starting at $\tau=0$ and $\tau=t_1$ respectively. At $t=t_1$, the response exhibits a "sharp change" because the forcing abruptly transitions.

**Example 3.2.3 (Multiple Impacts via Superposition):**

For "double impact" at $t=0$ and $t=\tau$:
$$F(t) = F_1\delta(t) + F_2\delta(t-\tau)$$

Response:
$$x(t) = \frac{F_1}{m}h(t) + \frac{F_2}{m}h(t-\tau)H(t-\tau)$$

where $H(t-\tau)$ is the Heaviside step function ensuring causality (second impulse doesn't affect response before $t=\tau$).

"Note the sharp change in the response as the second impact is applied." The two damped oscillations from each impulse either reinforce (in-phase impacts) or interfere (out-of-phase impacts), demonstrating superposition principle for linear systems.

---

### Explicit Causality via Heaviside Functions

Throughout Chapter 3, responses to piecewise loading are written using the **Heaviside step function** $H(t-t_0)$ or unit step $\Phi(t)$ to enforce causality:

$$x(t) = \frac{F_0}{k}\left[1 - e^{-\zeta\omega_n t}\cos(\omega_d t - \theta)\right] H(t) \quad \text{(Step response, zero for } t < 0\text{)}$$

For delayed step at $t=t_0$:
$$x(t) = \frac{F_0}{k}\left[1 - e^{-\zeta\omega_n(t-t_0)}\cos(\omega_d(t-t_0) - \theta)\right] H(t-t_0)$$

This ensures the response "starts" only after the stimulus is applied.

---

## CONNECTION BETWEEN DISCONTINUOUS FORCING AND INITIAL CONDITION JUMPS

### Central Equivalence

**Inman's explicit formulation:**

An impulsive force:
$$F(t) = F_n\delta(t)$$

with zero initial conditions ($x(0)=0, \dot{x}(0)=0$) produces **identical response** to:

**Continuous problem** with initial condition jump:
$$\text{No applied force, but initial velocity: } x(0)=0, \dot{x}(0)=v_0 = \frac{F_n}{m}$$

**Proof via Impulse Response:**

The impulse response function $h(t)$ is derived by solving:
$$\ddot{h} + 2\zeta\omega_n\dot{h} + \omega_n^2 h = \delta(t), \quad h(0)=0, \dot{h}(0)=0$$

Yet Inman shows (Section 3.1) that this is **mathematically equivalent** to:
$$\ddot{h} + 2\zeta\omega_n\dot{h} + \omega_n^2 h = 0, \quad h(0)=0, \dot{h}(0)=\frac{1}{m}$$

The second form is simply the **free response** (homogeneous equation) with the specified initial conditions. Thus:

$$h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t)$$

is the **free vibration** of an underdamped system with unit initial velocity.

### Practical Significance: Impact Analysis

**Example 3.1.1 (Concrete Impact Application):**

A camera mounted on a bracket is hit by a bird at 72 km/h (20 m/s). The bird has mass $m_b = 1$ kg.

Option 1 (Impulsive force approach):
- Force during impact: $F(t) = 10,000$ N for $\Delta t = 0.002$ s
- Impulse: $F_n = 10,000 \times 0.002 = 20$ N·s
- Solve $m\ddot{x} + c\dot{x} + kx = F(t)$ with time-dependent forcing

Option 2 (Initial condition equivalence):
- **No** external force
- Initial velocity (from momentum conservation): $\dot{x}(0) = \frac{F_n}{m} = \frac{20}{1} = 20$ m/s (approximately)
- Solve free vibration: $m\ddot{x} + c\dot{x} + kx = 0$ with $x(0)=0, \dot{x}(0)=20$ m/s

Both give the same response. The second approach is simpler for engineering analysis: calculate impulse from impact dynamics (particle physics), convert to initial condition (mechanics), solve linear free vibration.

### Discontinuous Velocity Discontinuities vs. Continuous Position

The key distinction Inman emphasizes:

- **Position $x(t)$ remains continuous** at impulse time (no mathematical discontinuity in displacement)
- **Velocity $\dot{x}(t)$ jumps discontinuously** (step change at $t=0$)
- **Acceleration $\ddot{x}(t)$ contains delta function** (singular at $t=0$)

This is reflected in the equation of motion:
$$m\ddot{x}(t) + c\dot{x}(t) + kx(t) = F_n\delta(t)$$

The right-hand side is a **distribution** (delta function), not a classical function.

---

## HIERARCHICAL POSITION RELATIVE TO OTHER FRAMEWORKS

### Placement in 49-Framework Taxonomy

**Mathematical Rigor Level:** Level 1 Bridge (Introductory-Intermediate Engineering)
- Accessible to sophomore/junior undergraduates
- Emphasizes physical meaning over mathematical abstraction
- Uses Heaviside and delta functions pragmatically (not via Schwartz distributions)

**Scope:**
- **Finite-dimensional:** Single DOF (Chapters 1-3), multi-DOF (Chapter 4), continuous (Chapter 6)
- **Linear systems:** Viscous and Coulomb damping
- **General loading:** Harmonic, periodic (Fourier series), arbitrary (Duhamel integral), random (Chapter 3.5)
- **Causality:** Explicit via impulse response (zero for $t < 0$) and Heaviside functions

**Does NOT treat:**
- Differential inclusions or Filippov regularization
- Sliding modes or nonsmooth mechanics
- Measure-theoretic approaches to distributions
- Impulsive control synthesis (only response to impulsive inputs)

### Comparison to Contemporary Frameworks

**vs. Benaroya (Framework 48):**
- **Inman:** Slightly more emphasis on practical applications (bird strikes, impact testing, machinery shock spectra)
- **Benaroya:** Slightly more emphasis on variational principles (Chapter 5 Lagrange's equation)
- **Both:** Nearly identical treatment of Duhamel integral, Laplace transforms, frequency response

**vs. Rao (Framework 47):**
- **Inman:** Similar overall scope; Inman has more extensive random vibration (Section 3.5, power spectral density, autocorrelation)
- **Rao:** More extensive multi-DOF systems and numerical methods
- **Both:** Standard engineering vibration texts with industrial applications

**vs. Kausel (Framework 46 - Structural Dynamics):**
- **Inman:** Audience is broader (general mechanical engineers, students)
- **Kausel:** Specialized for structural/wave dynamics; emphasizes Green's functions and frequency-domain analysis
- **Overlap:** Both treat impulse response rigorously via Laplace/Fourier transforms

**vs. Williams II (Framework 36 - Control Systems):**
- **Inman:** Analysis-focused (given system, find response)
- **Williams:** Synthesis-focused (design controllers)
- **Overlap:** Transfer functions, frequency response, stability

**vs. Yang (Framework 37 - Impulsive Control):**
- **Inman:** Describes response to impulsive disturbances
- **Yang:** Uses impulsive forces as control inputs
- **Inman does NOT:** Optimize impulsive controls or analyze discontinuous state feedback

**vs. Zabczyk (Framework 38 - Mathematical Control Theory):**
- **Zabczyk:** Abstract, measure-theoretic, infinite-dimensional
- **Inman:** Concrete, finite-dimensional, engineering-oriented
- **Zabczyk framework** encompasses Inman's examples but in more general/rigorous language

### Nonsmooth Mechanics Boundary

Unlike **Brogliato (Framework 3 - Nonsmooth Mechanics)**, Inman does NOT address:
- Friction-induced discontinuities (Coulomb friction leading to sliding modes)
- Impact dynamics with restitution coefficients
- Multivalued set-valued systems
- Filippov solutions to regularized systems

---

## QUANTITATIVE FRAMEWORK

### Canonical Problems and Solutions

**Problem 1: Unit Impulse Response**

Impulse response function for underdamped SDOF ($0 \le \zeta < 1$):
$$h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t) H(t)$$

where $\omega_d = \omega_n\sqrt{1-\zeta^2}$, $H(t)$ is unit step.

**Problem 2: Step Response**

Unit step response (Equation 3.17):
$$u(t) = \frac{1}{k}\left[1 - e^{-\zeta\omega_n t}\left(\cos(\omega_d t) + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin(\omega_d t)\right)\right]$$

Steady-state: $u_{\infty} = 1/k$ (static deflection under unit force).

**Relationship:** $h(t) = \frac{du(t)}{dt}$ (impulse response is time derivative of step response)

**Problem 3: Arbitrary Forcing via Duhamel Integral**

$$x(t) = \int_0^t h(t-\tau) \frac{F(\tau)}{m} d\tau$$

For piecewise $F(t)$, split integral by discontinuity times.

**Problem 4: Periodic Forcing via Fourier Series**

For periodic $F(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n \cos(n\omega_T t) + b_n \sin(n\omega_T t)]$:

Response by superposition:
$$x(t) = x_{\text{DC}} + \sum_{n=1}^{\infty} x_n(t)$$

where $x_n(t)$ is the response to the $n$-th harmonic component (from Chapter 2).

**Problem 5: Shock Spectrum Analysis**

For transient input $F(t)$, compute maximum response over all frequencies $\omega_n$:
$$\text{Shock Spectrum: } \text{Plot } x_{\max}(\omega_n) \text{ vs. } \omega_n$$

Used in seismic design and equipment drop testing.

### Numerical Integration Algorithms (Section 3.9)

Inman provides practical algorithms for problems where analytical solutions (via Duhamel integral or Laplace transforms) are unavailable:

1. **Runge-Kutta method:** 4th-order for accuracy
2. **Central difference scheme:** For piecewise forcing with sharp discontinuities
3. **MATLAB integration:** Detailed code examples for each problem type

---

## ORGANIZATIONAL STRENGTHS AND LIMITATIONS

### Strengths:

1. **Pedagogical clarity:** Each concept introduced via concrete examples (impact testing, bird strikes, machinery transients, vibration isolation)
2. **Physical intuition:** Momentum-impulse principle makes impulse-to-initial-condition equivalence transparent
3. **Multiple solution methods:** Time domain (Duhamel), frequency domain (Laplace), modal superposition (Fourier series)
4. **Practical algorithms:** Numerical integration for complex real-world loading
5. **Causality made explicit:** Heaviside functions, impulse responses zero for $t < 0$, ROC for Laplace transforms
6. **Industrial applications:** Vibration testing, shock spectra, condition monitoring, rotating machinery
7. **Comprehensive scope:** Single/multi-DOF, continuous systems, nonlinear effects, experimental modal analysis, FEM

### Limitations:

1. **No discontinuous right-hand sides (formal theory):** Piecewise loading treated ad hoc; no Filippov or differential inclusions
2. **Linear only:** Viscous damping dominates; Coulomb friction discussed but not integrated
3. **No sliding modes:** Discontinuous control feedback not addressed
4. **No impulsive control:** Describes response to impulsive disturbances but not control via impulsive forces
5. **Limited state discontinuities:** No restitution coefficients, inelastic collisions, or multivalued maps

---

## SUMMARY AND POSITION

**Hierarchical Tier:** Level 1 Bridge Framework (Introductory-Intermediate with Strong Industrial Grounding)

**Central Contribution to Discontinuous/Impulsive ODE Theory:**

Inman's textbook provides a **canonical engineering treatment** of the equivalence:
$$\text{Impulsive forcing } F(t) = F_n\delta(t) \iff \text{ Initial velocity jump } \dot{x}(0) = \frac{F_n}{m}$$

via:
1. Physical momentum-impulse principle
2. Impulse response as free vibration with specified initial velocity
3. Duhamel integral for arbitrary (including piecewise discontinuous) loading
4. Explicit causality enforced by Heaviside functions and impulse response properties
5. Practical examples and algorithms for real-world engineering applications

**Why It Matters:**

Engineering students worldwide learn from Inman (or comparable texts like Benaroya, Rao) that discontinuous forcing naturally produces continuous position but discontinuous velocity, governed by the impulse response function. This foundation is essential before encountering more abstract mathematical treatments (Zabczyk, Filippov, distribution theory).

**Comparison Matrix with Other Frameworks:**

| Aspect | Inman | Benaroya | Rao | Kausel | Williams | Yang | Zabczyk |
|--------|-------|----------|-----|--------|----------|------|---------|
| Impulse Response | ✓ Explicit | ✓ Explicit | ✓ Explicit | ✓ Green's fn | ✓ Transfer fn | ✓ Implicit | ✓ Abstract |
| Duhamel Integral | ✓ Central | ✓ Central | ✓ Central | ✓ Contour | ~ Implied | ~ Synthesis | ✓ Abstract |
| Discontinuous RHS | ✗ Piecewise | ✗ Piecewise | ✗ Piecewise | ✗ No | ✗ No | ✗ No | ✓ Measure-theory |
| Causality Explicit | ✓ H(t) | ✓ H(t) | ✓ H(t) | ✓ ROC | ✓ Poles | ~ Control | ✓ Formal |
| Real Applications | ✓ High | ✓ High | ✓ High | ✓ Structures | ✓ Controls | ✓ Medium | ~ Theory |
| Student Accessibility | ✓ High | ✓ High | ✓ High | ~ Medium | ~ Medium | ~ Low | ✗ Low |

---

## CONCLUSION

Inman's "Engineering Vibration, Fourth Edition" occupies a **central pedagogical role** in mechanical engineering education, providing the first rigorous (yet accessible) treatment of impulsive systems, impulse response, and the Duhamel integral that most engineering students encounter.

Its strength lies in making **transparent the physical equivalence** between impulsive forcing and initial condition jumps: a bird strike is not merely a time-dependent force profile but a momentum transfer that can be reduced to an instantaneous velocity change, governed thereafter by free vibration of the structure.

For practitioners of the broader discontinuous ODE literature (Filippov, distributions, differential inclusions), Inman's textbook provides the **concrete engineering instantiation** upon which more abstract frameworks build. It is a bridge from industrial problems to mathematical theory, and as such occupies an indispensable position in the literature review.

