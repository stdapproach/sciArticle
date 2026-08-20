# Framework 48: Benaroya, Nagurka & Seon-Han - Mechanical Vibration Analysis, Uncertainties, and Control (4th Edition)

**Authors:** Haym Benaroya, Mark Nagurka, Seon Han  
**Publisher:** CRC Press (Taylor & Francis Group)  
**Publication Year:** 2017  
**Edition:** Fourth Edition  
**ISBN:** 978-1-4987-5294-7  
**Total Pages:** 602  

---

## CENTRAL MISSION AND UNIQUE CONTRIBUTION

The Benaroya/Nagurka/Seon-Han textbook (4th edition, 2017) is a comprehensive engineering reference on mechanical vibration analysis that systematically bridges discrete single-degree-of-freedom (SDOF) and continuous multi-degree-of-freedom systems. Its primary organizational strategy is pedagogical: move from simple harmonic forcing through damping, then expand to general loading (impulse, step, arbitrary) via Laplace transforms and convolution integrals, and finally extend to continuous beam/distributed-parameter models and random forcing.

**Unique Contribution to Discontinuous/Impulsive Analysis:**

The textbook's strength lies in its **dual treatment of impulse response via Laplace transforms AND convolution integrals**. Unlike purely theoretical mathematics texts (e.g., Zabczyk) or specialized control systems texts (e.g., Williams), Benaroya et al. provides:

1. **Concrete engineering examples** throughout (hammer blows, airplane landings, ship wave impacts)
2. **Multiple equivalent mathematical formulations** (frequency domain, time domain, convolution)
3. **Explicit treatment of causality** via Laplace transform poles and ROCs (region of convergence)
4. **Practical numerical computation** with MATLAB integration for every major example
5. **Industrial orientation** toward vibration testing, impact analysis, and condition monitoring

The textbook positions itself as **Level 1-2 Bridge Framework** (Introductory-Intermediate): accessible to engineering undergraduates yet rigorous enough for practicing engineers.

---

## TREATMENT OF DISCONTINUITIES ON THE RIGHT-HAND SIDE

### Chapter 3: Damped Vibration with Harmonic Forcing

**Section 3.7: Forced Harmonic Vibration with Viscous Damping**

The governing equation for single degree-of-freedom systems:
$$\ddot{x} + 2\zeta\omega_n\dot{x} + \omega_n^2 x = \frac{F(t)}{m}$$

Benaroya et al. treat harmonic forcing systematically, establishing the frequency response function:
$$H(i\omega) = \frac{1}{m(\omega_n^2 - \omega^2 + i 2\zeta\omega_n\omega)}$$

**Key observation on discontinuous right-hand sides:**

The textbook does NOT explicitly formalize discontinuous right-hand sides (e.g., piecewise constant forces or sliding modes). Instead, it:
- Treats periodic non-harmonic loading via Fourier series decomposition
- Uses superposition principle for each harmonic component
- Approximates discontinuous loading as square waves or sawtooth functions, then decomposes via Fourier coefficients
- **Does not engage with Filippov regularization, differential inclusions, or multivalued systems**

---

### Chapter 4: General Loading and Advanced Topics - THE CRITICAL SECTION

**Section 4.3: Impulsive Excitation**

This is where the discontinuous forcing analysis becomes explicit. The unit impulse (Dirac delta function) is introduced as the mathematical model for "very large forces acting over very short time intervals":

$$\delta(t - t_0) \text{ such that } \int_{-\infty}^{\infty} \delta(t - t_0) dt = 1$$

**Units and meaning:** $\delta(t)$ has units of $s^{-1}$. The integral $\int f(t)\delta(t) dt = f(0)$ (sifting property).

**Impulse response function definition:**

For the governing equation:
$$\ddot{h} + 2\zeta\omega_n\dot{h} + \omega_n^2 h = \frac{\delta(t)}{m}$$

The impulse response function $h(t)$ equals the system's time-domain response to a unit impulse at $t=0$ with zero initial conditions.

**Key relationship (Equation 4.22):**
$$\mathcal{L}[\delta(t)] = H(s) \quad \text{(Laplace transform pair)}$$

The impulse response and transfer function form a Laplace transform pair:
- Forward: $\mathcal{L}[h(t)] = H(s)$
- Inverse: $h(t) = \mathcal{L}^{-1}[H(s)]$

**Explicit damping cases:**

1. **Underdamped System** ($0 \le \zeta < 1$):
$$h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t) H(t)$$
where $\omega_d = \omega_n\sqrt{1-\zeta^2}$ (damped natural frequency), $H(t)$ is unit step function.

2. **Critically Damped System** ($\zeta = 1$):
$$h(t) = \frac{1}{m} t e^{-\omega_n t} H(t)$$

3. **Overdamped System** ($\zeta > 1$):
$$h(t) = \frac{1}{m}\left(e^{-\lambda_1 t} + e^{-\lambda_2 t}\right) H(t)$$
where $\lambda_1, \lambda_2 = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2-1}$ (real, distinct roots).

**Causality enforcement:**

Benaroya et al. explicitly enforce $h(t) = 0$ for $t < 0$ via the Heaviside step function $H(t)$. This causality is automatic in Laplace transform formulation (integral from $0$ to $\infty$) but becomes crucial when converting back to time domain via inverse Laplace transform or residue calculus.

---

### Section 4.4: Arbitrary Loading and the Convolution Integral

**The Duhamel Integral (Equation 4.26):**

For arbitrary deterministic loading $F(t)$, the forced response with zero initial conditions is:
$$x_{\text{forced}}(t) = \int_0^t h(t-\tau) F(\tau) d\tau$$

This is the **convolution integral**, also known as the **Duhamel integral** (after Jean-Marie Constant Duhamel, 1797-1872).

**Physical interpretation:**

The arbitrary load $F(t)$ is decomposed into infinitesimal impulses $F(\tau)d\tau$ at each prior time $\tau$. Each impulse produces a response contribution $h(t-\tau) F(\tau) d\tau$. The total response is the superposition (sum) of all such contributions.

**Two equivalent decompositions shown:**

1. **Vertical impulses** (Figure 4.10 top):
   - Approximate load as series of rectangular pulses with vertical heights
   - Each pulse of area $F(\tau)\Delta\tau$ at time $\tau$ produces response $h(t-\tau)F(\tau)\Delta\tau$
   - In limit $\Delta\tau \to 0$: convolution integral

2. **Horizontal steps** (Figure 4.10 bottom):
   - Approximate load as series of rectangular pulses with horizontal widths
   - Each step change $\Delta F(\tau)$ at time $\tau$ contributes to subsequent response via unit step response $u(t-\tau)$
   - Integration by parts leads to same Duhamel integral

**Key property of Duhamel integral with discontinuous forcing:**

When $F(t)$ is **discontinuous** (piecewise continuous with jump discontinuities), the integral must be evaluated over each continuous segment separately:

**Example 4.12 (Discontinuous Loading):**
For piecewise forcing:
$$F(t) = \begin{cases} F_1(t) & 0 \le t \le t_1 \\ 0 & t_1 \le t \le t_2 \\ F_3(t) & t_2 \le t \le t_3 \\ 0 & t \ge t_3 \end{cases}$$

The convolution is split:
$$x(t) = \int_0^{t_1} h(t-\tau) F_1(\tau) d\tau + \int_0^{t_2} h(t-\tau) \cdot 0 \, d\tau + \int_{t_2}^{t_3} h(t-\tau) F_3(\tau) d\tau$$

"At each time instant, all the loads from earlier time spans up to the present must be added. Due to the discontinuities of the loading function, the convolution integral is evaluated for each continuous segment."

This is a direct, pragmatic treatment of how impulse response methods handle discontinuous forcing: **split into continuous pieces and apply superposition**.

---

## CONNECTION BETWEEN DISCONTINUOUS FORCING AND INITIAL CONDITION JUMPS

### Unit Impulse Response = Time Derivative of Unit Step Response

**Equation 4.23** (critical bridge between impulse and initial conditions):
$$h(t) = \frac{du(t)}{dt}$$

where $u(t)$ is the unit step response.

**Physical meaning:**

If a system is subjected to a unit step input $U(t) = H(t)$ (sudden jump of magnitude 1 at $t=0$), the response $u(t)$ evolves smoothly. The derivative $\dot{u}(t)$ gives the "speed" at which the system responds to that step input.

Since the step input itself has a discontinuity (jump from 0 to 1 at $t=0$), and the impulse is the mathematical derivative of the step, the impulse response $h(t)$ captures how the system responds to the most extreme discontinuity: instantaneous transfer of all energy at a single time instant.

**Momentum-Impulse Principle (illustrated implicitly):**

For an underdamped system with $h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t)$:

At $t = 0^+$ (just after impulse):
- The impulse $J$ (momentum change) produces **instantaneous velocity jump**:
$$v(0^+) = \frac{J}{m}$$

This connects to initial conditions: an impulsive force $F(t) = J\delta(t)$ is **equivalent to** specifying a non-zero initial velocity $\dot{x}(0) = v_0 = J/m$ with zero applied forcing afterward.

**Practical example (Example 4.8):**

"A 10,000 N force applied for 0.0002 seconds at $t=0$. What is the response at $t=0.1$ s?"

The impulse is:
$$J = F \cdot \Delta t = 10,000 \text{ N} \times 0.0002 \text{ s} = 2 \text{ N·s}$$

Instead of solving:
$$m\ddot{x} + c\dot{x} + kx = F(t) = \begin{cases} 10,000 & 0 \le t \le 0.0002 \\ 0 & t > 0.0002 \end{cases}$$

The textbook models it as:
$$m\ddot{x} + c\dot{x} + kx = J\delta(t) = 2\delta(t)$$

with zero initial conditions, then evaluates:
$$x(0.1) = h(0.1) \cdot (J/m) = h(0.1) \cdot (2/1) = 2h(0.1)$$

**The equivalence:**

An impulsive forcing $F(t) = J\delta(t)$ with initial conditions $x(0)=0, \dot{x}(0)=0$ produces the identical response to:

**Continuous forcing** over a small time interval with corresponding initial condition jump:
- Apply $F(t)$ over $[0, \Delta t]$ starting from $x(0) = 0, \dot{x}(0) = 0$
- After time $\Delta t$, the velocity changes by $\Delta v \approx (J/m)$ due to impulse-momentum theorem
- For $t > \Delta t$, the system continues with $x(\Delta t) = \epsilon$ (small), $\dot{x}(\Delta t) = J/m + O(\epsilon)$

In the limit $\Delta t \to 0$: position remains zero $x(0^+) = 0$ but velocity jumps $\dot{x}(0^+) = J/m$.

---

## HIERARCHICAL POSITION RELATIVE TO OTHER FRAMEWORKS

### Placement in the 48-Framework Taxonomy

**Mathematical Rigor Level:** Intermediate (Level 1-2 Bridge)
- More rigorous than purely phenomenological mechanics texts (e.g., Timoshenko 1974)
- Less mathematically abstract than distribution theory texts (e.g., Cooper 1978: Distribution Theory)
- Comparable to Rao's "Mechanical Vibrations, 5th Edition" (Framework 47)

**Scope and Generality:**
- **Finite-dimensional:** Single degree-of-freedom systems in Chapters 2-4; multi-DOF in Chapters 5-6; continuous models (beams, shafts) in Chapter 7
- **Linear systems:** Assumes linearity throughout; damping is viscous (linear)
- **Does not treat:** Nonlinear damping, sliding modes, differential inclusions, discontinuous right-hand sides in the generalized sense

**Solution Methodologies Employed:**

1. **Laplace Transform (Chapter 4.1):** Transforms ODE to algebraic equations in $s$-domain, enabling straightforward inverse transforms for step, impulse, and arbitrary responses
2. **Transfer Function/Frequency Response:** Emphasizes system characterization via poles and zeros; Bode plots for frequency-domain analysis
3. **Convolution Integral (Section 4.4):** Time-domain perspective via superposition of impulse responses
4. **Fourier Series (Section 3.8):** Decomposes periodic non-harmonic forcing into harmonic components, solved individually via superposition

**Connections to Other Frameworks:**

- **Rao (Framework 47):** Nearly identical in scope and pedagogy; Rao slightly more emphasis on applications (condition monitoring, wear), Benaroya slightly more emphasis on theoretical foundations (Lagrange's equation, variational principles in Chapter 5)

- **Kausel (Framework 46):** Structural dynamics perspective; similar treatment of impulse response via Green's functions and contour integration; Kausel emphasizes wave propagation and infinite-dimensional systems

- **Williams II (Framework 36):** "Linear State-Space Control Systems" - Benaroya's Chapter 4 on transfer functions/frequency response connects to state-space representation; Williams emphasizes control feedback, Benaroya emphasizes open-loop response analysis

- **Yang (Framework 37):** "Impulsive Control Theory" - Yang systematizes discontinuous dynamics via impulsive control laws; Benaroya stops at describing response to impulsive inputs, not impulsive control synthesis

- **Zabczyk (Framework 38):** "Mathematical Control Theory: An Introduction" - Abstract measure-theoretic framework; Benaroya provides concrete engineering instantiation

**Treatment of Discontinuities:** Pragmatic vs. Axiomatic

Benaroya et al. adopt a **pragmatic engineering approach** to discontinuous systems:
- Discontinuous forcing is approximated via Fourier series or handled piecewise via convolution integrals
- No formal theory of differential inclusions or Filippov solutions
- Focus on numerical computation and physical examples rather than existence/uniqueness theorems

This contrasts with:
- **Filippov (Framework 28):** Axiomatic treatment via differential inclusions
- **Kamachkin (Framework 41):** Solutions that explicitly reject existence on discontinuity manifolds
- **Kiseleva (Framework 43):** Measure-theoretic approach to differential inclusions

**Sliding Modes and Nonsmooth Mechanics:**

Benaroya et al. do not treat:
- Dry friction (Coulomb damping) as leading to sliding modes or set-valued forces
- Multivalued dynamics via differential inclusions
- Filippov regularization or regularized systems
- Utkin equivalence control

This puts Benaroya at a lower complexity tier than Brogliato (Framework 3: "Nonsmooth Mechanics: Models, Dynamics and Control") on nonsmooth phenomena, though Benaroya Chapter 3 does discuss Coulomb damping as a linear alternative to viscous damping.

---

## SPECIFIC ANALYTICAL STRENGTHS AND LIMITATIONS

### Strengths:

1. **Pedagogical clarity:** Each concept introduced via concrete examples (hammer impact, airplane landing, vibration isolation); MATLAB code for numerical solutions
2. **Multiple equivalent formulations:** Same problem solved via time domain, frequency domain, Laplace transforms, and convolution integrals; student gains intuition from different perspectives
3. **Causality made explicit:** Heaviside step functions $H(t)$, ROC for Laplace transforms, and pole locations all emphasize physical causality
4. **Industrial relevance:** Applications to bearing failures, vibration testing, machinery condition monitoring
5. **Comprehensive scope:** Single DOF (Chapters 2-4) → Multi-DOF (Chapters 5-6) → Continuous systems (Chapter 7) → Random forcing (Chapter 9)

### Limitations:

1. **No discontinuous right-hand sides (formal theory):** Piecewise loading treated ad hoc via splitting integrals; no Filippov or inclusion-theoretic framework
2. **Linear only:** Viscous damping dominates; Coulomb damping discussed but not integrated into the main framework
3. **No impulsive control:** Describes response to impulsive inputs but not control via impulsive forces
4. **Limited discontinuity beyond impulses:** No jump discontinuities in state (e.g., inelastic collisions, lost contact dynamics)
5. **Frequency domain assumes harmonic:** Arbitrary forcing requires Fourier decomposition or convolution; no general nonlinear treatment

---

## SUMMARY OF MATHEMATICAL FRAMEWORK

### Canonical Problem Class:

$$m\ddot{x}(t) + c\dot{x}(t) + kx(t) = F(t), \quad x(0) = x_0, \dot{x}(0) = v_0$$

### Solution Representation:

**Total response = Free response + Forced response:**
$$x(t) = x_{\text{free}}(t; x_0, v_0) + x_{\text{forced}}(t; F(\cdot))$$

**Free response** (homogeneous ODE with initial conditions):
$$x_{\text{free}}(t) = e^{-\zeta\omega_n t}\left[x_0\cos(\omega_d t) + \frac{v_0 + \zeta\omega_n x_0}{\omega_d}\sin(\omega_d t)\right]$$

**Forced response** (particular solution via convolution):
$$x_{\text{forced}}(t) = \int_0^t h(t-\tau) \frac{F(\tau)}{m} d\tau$$

where impulse response:
$$h(t) = \frac{1}{m\omega_d} e^{-\zeta\omega_n t} \sin(\omega_d t) H(t)$$

### Special Cases:

1. **Harmonic forcing** $F(t) = F_0\cos(\omega t)$:
   - Laplace transform approach yields steady-state amplitude and phase
   - Frequency response function $H(i\omega)$ characterizes magnitude and phase shift

2. **Step forcing** $F(t) = F_0 H(t)$:
   - Unit step response $u(t) = \frac{F_0}{k}[1 - e^{-\zeta\omega_n t}(\cos(\omega_d t) + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin(\omega_d t))]$

3. **Impulse forcing** $F(t) = J\delta(t)$:
   - Response equal to $\frac{J}{m}h(t)$
   - Impulse $J$ produces instantaneous velocity jump $v(0^+) = J/m$

4. **Arbitrary piecewise loading:**
   - Split into continuous segments
   - Apply Duhamel integral separately over each segment
   - Ensure continuity of position and velocity at segment boundaries

---

## QUANTITATIVE EXAMPLE: IMPACT ANALYSIS

**Framework 48's treatment of impact (Example 4.8 equivalent):**

A 10 kg mass on a spring ($k = 1000$ N/m) with damping ($c = 50$ N-s/m) is hit by a hammer delivering an impulse of $J = 2$ N·s.

**Step 1: Characterize system**
- Natural frequency: $\omega_n = \sqrt{k/m} = 10$ rad/s
- Damping ratio: $\zeta = c/(2\sqrt{km}) = 0.7906$
- Damped frequency: $\omega_d = \omega_n\sqrt{1-\zeta^2} = 5.944$ rad/s

**Step 2: Compute impulse response**
$$h(t) = \frac{1}{10 \times 5.944} e^{-0.7906 \times 10 \times t} \sin(5.944t) = 0.0168 e^{-7.906t} \sin(5.944t) \text{ m·s}^{-1}$$

**Step 3: Apply impulse boundary condition**
Initial velocity after impact: $v(0^+) = J/m = 2/10 = 0.2$ m/s

**Step 4: Compute response**
$$x(t) = (0.2) \times h(t) = 0.00336 e^{-7.906t} \sin(5.944t) \text{ m}$$

At $t = 0.1$ s:
$$x(0.1) = 0.00336 e^{-0.791} \sin(0.594) = 0.00336 \times 0.453 \times 0.559 = 0.000845 \text{ m} = 0.845 \text{ mm}$$

---

## POSITION IN LITERATURE REVIEW TAXONOMY

**Hierarchical Tier:** Level 1-2 Bridge (Introductory-Intermediate with Industrial Rigor)

**Primary Contribution to Discontinuous/Impulsive Differential Equations:**

- **Strengths:** Concrete engineering treatment of impulse response, convolution integrals, and frequency response; explicit causality via Laplace transforms; extensive examples
- **Scope:** Continuous linear systems with time-dependent forcing; no singularities, measure-theoretic treatment, or inclusions
- **Relation to core question:** Directly addresses equivalence between impulsive forcing $F(t) = J\delta(t)$ and initial condition jump $\dot{x}(0) = J/m$; demonstrates via Duhamel integral

**Comparison Matrix:**

| Framework | Impulse Response | Convolution | Discontinuous RHS | Differential Inclusions | Laplace Transform |
|-----------|------------------|-------------|-------------------|-------------------------|-------------------|
| **Benaroya-48** | ✓ Explicit | ✓ Central | ✗ Piecewise only | ✗ No | ✓ Central |
| Rao-47 | ✓ Explicit | ✓ Central | ✗ Piecewise | ✗ No | ✓ Central |
| Kausel-46 | ✓ Green's fn | ✓ Via contour | ✗ No | ✗ No | ✓ Residue theorem |
| Williams II-36 | ✓ State-space | ✓ Implied | ✗ No | ✗ No | ✓ Pole-zero |
| Yang-37 | ✓ Via control | ✓ Synthesis | ✗ No | ✓ Implicit | ~ Implicit |
| Zabczyk-38 | ✓ Abstract | ✓ Abstract | ✓ Measure-theoretic | ✓ Central | ✗ No |
| Brogliato-3 | ✓ Nonsmooth | ✓ Nonsmooth | ✓ Filippov | ✓ Filippov inclusions | ~ Via Laplace relaxation |

---

## CONCLUSION

The Benaroya/Nagurka/Seon-Han textbook (4th edition, 2017) provides a **canonical engineering treatment of impulsive systems and convolution-based response analysis** for linear mechanical systems. It occupies a central, widely-taught position in mechanical engineering curricula and serves as a bridge from undergraduate vibration analysis to graduate control systems and structural dynamics.

The framework's treatment of the **equivalence between impulsive forcing and initial condition jumps** is explicit, concrete, and accessible: an impulse $J\delta(t)$ produces an instantaneous velocity change $\Delta v = J/m$ detectable via the impulse response function $h(t)$. This equivalence, formalized via the derivative relationship $h(t) = du(t)/dt$, illustrates why discontinuous forcing (impulses) naturally appears alongside discontinuous state trajectories (velocity jumps) in mechanical systems.

Its limitations—absence of Filippov regularization, differential inclusions, and multivalued dynamics—reflect its engineering pedagogical mission: to teach practicing engineers how to analyze real impacts and vibration transients, not to develop axiomatic mathematical frameworks for discontinuous systems. For those axiomatic frameworks, one must turn to Zabczyk, Cooper, or Brogliato.

**Key Position in Framework Hierarchy:**
- **Level 1-2 Bridge** (comparable to Rao Framework 47)
- **Highly accessible** to engineering students and practitioners
- **Central to industrial applications** of impact analysis, vibration testing, and structural health monitoring
- **Complements but does not replace** abstract mathematical treatments (Filippov, distribution theory, differential inclusions)

