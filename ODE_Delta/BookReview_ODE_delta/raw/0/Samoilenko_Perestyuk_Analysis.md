# Samoilenko & Perestyuk: Impulsive Differential Equations (1995)

## Analysis Summary

**Central Mission and Unique Contribution:**
Samoilenko and Perestyuk present the **comprehensive mathematical theory of impulsive differential equations** developed by the Kiev School of Nonlinear Mechanics. This is the definitive monograph treating impulsive systems with rigorous mathematical foundations, systematic methods, and extensive applications. The unique contribution is the **unified framework for three classes of impulsive systems** (fixed impulses, variable impulses on surfaces, discontinuous dynamics) with complete treatment of existence, uniqueness, stability, periodicity, and optimal control.

---

## Treatment of Discontinuities

**Foundational Framework (Chapter 1, Section 1.1: "Description of Mathematical Model"):**

The textbook establishes impulsive systems through a general mechanism:

$$\frac{dx}{dt} = f(t,x), \quad (t,x) \notin \mathcal{T}_t$$
$$\Delta x|_{(t,x) \in \mathcal{T}_t} = A_t x - x$$

where:
- **System (1.1):** Differential equations between impulses
- **Set $\mathcal{T}_t$:** Surfaces/times where discontinuities occur
- **Operator $A_t$:** Maps state before impulse to state after impulse

**The Solution Concept:**

A solution of the impulsive system is a **piecewise continuous function** $x = \phi(t)$ that:
1. Satisfies $\frac{dx}{dt} = f(t,x)$ for all $t \notin \{t_i\}$ (the impulse times)
2. Has **discontinuities of the first kind** at impulse times $t_i$
3. Satisfies the jump condition: $\Delta x = \phi(t_i^+) - \phi(t_i^-) = I_i(\phi(t_i^-))$

**Key Distinction: Three Classes of Systems**

1. **Systems with Impulses at Fixed Times (Section 1.2):**
$$\frac{dx}{dt} = f(t,x), \quad t \neq T_i$$
$$\Delta x|_{t=T_i} = I_i(x)$$

where $\{T_i\}$ is a predetermined sequence of times.

2. **Systems with Impulses at Variable Times (Section 1.3):**

Impulses occur when trajectory meets a surface defined by $\Phi(t,x) = 0$ or $t = \tau_i(x)$, where $\tau_i$ depends on state.

3. **Discontinuous Dynamical Systems (Section 1.4):**

The operator $A_t$ or the differential equation itself may be discontinuous in state or time.

**Critical Mathematical Conditions:**

The textbook carefully specifies four essential properties for solutions of system (1.1):

1. **Non-extensibility:** Solutions exist on intervals $(a,b)$ and diverge to infinity at boundaries
2. **Locality:** Local behavior determines global solutions
3. **Solvability of Cauchy problem:** Existence guaranteed for all initial conditions
4. **Local compactness:** Solution set depends continuously on initial conditions

When combined with assumptions on operators $A_t$ (upper semicontinuity), these ensure **well-posed impulsive systems**.

---

## Treatment of Impulse Response

**Impulse as Discontinuous Forcing:**

Unlike classical impulse response theory via Laplace transforms, Samoilenko-Perestyuk treat impulses as **state jumps through operator action**:

$$x(t_i^+) = A_i[x(t_i^-)] = x(t_i^-) + I_i(x(t_i^-))$$

**Key Features:**

1. **Nonlinear Dependence:** Impulse response $I_i(x)$ can depend nonlinearly on pre-impulse state $x(t_i^-)$
2. **Non-uniqueness:** If $A_i$ is multivalued, impulse can produce multiple post-impulse states
3. **Possible "death":** If $A_i x = \emptyset$ (empty set), the solution cannot be extended beyond the impulse

**Trajectory Mapping:**

The evolution of trajectories is described by trajectory translation operator:

$$G(t,t_0)M = g(t,T_j)A_j \circ g(t,T_{j-1}) \circ A_{j-1} \circ \cdots \circ A_i \circ g(t,t_0)M$$

This composition shows:
- Solutions flow according to system (1.1) between impulses via $g(t,t_0)$
- At each impulse time $T_i$, the operator $A_i$ acts, potentially creating new trajectories or causing them to merge/split

**Pulsation Phenomenon:**

A remarkable feature is **pulsation**: trajectories can intersect the impulse set $\mathcal{T}_t$ infinitely many times in finite time, creating accumulation points. Example: solution may undergo countably many impulses as $t \to t_*^-$, making the trajectory un-extensible beyond $t_*$.

---

## Connection: Discontinuous Forcing ↔ Discontinuous Initial Condition

**The Fundamental Equivalence:**

Samoilenko-Perestyuk make explicit that:

$$\text{Impulsive forcing at } t = T_i \Leftrightarrow \text{Instantaneous state jump } \Delta x|_{t=T_i} = I_i(x(T_i^-))$$

**Mathematical Formulation:**

The solution can be expressed as:

$$x(t,t_0,x_0) = x_0 + \sum_{t_0 < T_i < t} I_i(x(T_i^-)) + \int_{t_0}^t f(s,x(s,t_0,x_0))ds$$

This decomposition shows:
1. Initial condition $x_0$ contributes directly
2. Each impulse contributes a discrete jump $I_i(x(T_i^-))$
3. Continuous forcing $f(t,x)$ acts between impulses

**State Jump Mechanics:**

The operator $A_t$ encodes the state transformation at impulse time:
- **Single-valued $A_t$:** Deterministic jump $x(T_i^+) = A_t[x(T_i^-)]$
- **Multivalued $A_t$:** Non-deterministic; multiple possible post-impulse states
- **Non-injective $A_t$:** Trajectories can merge (different pre-impulse states → same post-impulse state)
- **Non-surjective $A_t$:** Trajectories can split or die (some post-impulse values unreachable)

**Comparison with Initial Conditions:**

Unlike standard ODE where initial condition is fixed, impulsive systems have:
- **Initial jump:** $x(t_0^+) = A_j[x(t_0^-)]$ if $t_0$ is an impulse time
- **Accumulated jumps:** Multiple impulses create accumulated state changes
- **Continuous component:** Between impulses, evolution follows ordinary differential equation

This makes impulsive systems equivalent to **piecewise-continuous trajectories with discontinuous initial condition jumps**.

---

## Three Classes in Detail

### Class 1: Fixed Impulses (Section 1.2)

**Model:**
$$\frac{dx}{dt} = f(t,x), \quad t \neq T_i$$
$$\Delta x|_{t=T_i} = I_i(x(T_i^-))$$

**Properties:**
- $\{T_i\}$ are fixed times: $T_0 < T_1 < T_2 < \cdots$
- Solutions are continuous between impulses
- Jumps occur at predetermined moments
- Operator can be multivalued: $A_i: \mathbb{R}^n \to 2^{\mathbb{R}^n}$

**Existence and Uniqueness (Theorem 1-2):**
- Existence guaranteed if system (1.1) satisfies Caratheodory conditions
- Uniqueness requires single-valued operators $A_i$ and unique solutions to (1.1)
- Solutions can split (if $A_i$ is multivalued) or merge (if trajectories reach same point)

**Applications:** Clock models, impact systems, switching circuits

### Class 2: Variable Impulses (Section 1.3)

**Model:**
Impulses occur when trajectories meet a surface:
$$\Phi(t,x) = 0 \quad \text{or} \quad t = \tau_i(x)$$

**Complexity:**
- Impulse times depend on state via $\tau_i(x)$
- Can have sliding motion along impulse surface
- Possible chattering (infinitely many impulses in finite time)
- Requires more sophisticated analysis of discontinuities

**Example from text:**
The system with impulse set $\mathcal{T}_t = \{(t,x) | x = \arctan(\tan(x))\}$ exhibits multiple types of trajectories:
- Stationary (never reach impulse set)
- Finite-time impulse (hit set finitely many times, then leave forever)
- Infinite-time impulse (countably many hits, accumulating to boundary)

### Class 3: Discontinuous Dynamical Systems (Section 1.4)

**Characteristics:**
- The differential equation itself may be discontinuous
- The operator $A_t$ may be discontinuous
- Neither the domain nor the operator assumes continuity

**Example - "Death" Trajectories:**
$$\frac{dx}{dt} = 1, \quad t \neq T_i$$
$$\Delta x|_{t=T_i} = \ln(2-x)$$

with $T_i = i$. A solution starting at $x_0 = 0$ evolves as $x(t) = t$ until $t = 2$. At $t = 2$, the impulse operator $\ln(2-x)$ is undefined at $x = 2$, so the trajectory "dies"—cannot be extended beyond $t = 2$.

---

## Stability Analysis

**Direct Lyapunov Method (Chapter 3, Section 3.4):**

Samoilenko-Perestyuk extend the classical Lyapunov method to impulsive systems. A function $V(t,x)$ is a Lyapunov function if:

1. $\frac{\partial V}{\partial t} + \nabla V \cdot f(t,x) \leq 0$ along solutions between impulses
2. $V(t,T_i^+,x^+) - V(t,T_i^-,x^-) \leq 0$ at impulse times (or satisfies relaxed condition)

The key innovation is handling **both continuous and discontinuous components** of the system simultaneously.

**Characteristic Exponents:**

For linear systems, stability is characterized by Lyapunov exponents $\lambda_i$:
$$\lambda_i = \limsup_{t \to \infty} \frac{1}{t}\ln|x_i(t)|$$

System is asymptotically stable if all $\lambda_i < 0$.

---

## Position Within 24+ Framework Hierarchy

**Framework Type: Comprehensive Mathematical Theory with Full Rigor**

**Characteristics:**
1. **Scope:** Most general treatment—includes all three impulse classes
2. **Mathematical level:** Highest rigor with measure theory, operator theory, functional analysis
3. **Generality:** Multivalued operators, discontinuous systems, abstract spaces
4. **Applications:** Extensive worked examples from mechanics, oscillations, control

**Distinguishing Features:**

| Aspect | Samoilenko-Perestyuk |
|---|---|
| **Impulse Definition** | Operator action $A_t$: state jump via $I_i(x)$ |
| **Discontinuities** | General discontinuous dynamical systems (not just on RHS) |
| **Solutions** | Piecewise continuous with first-kind discontinuities |
| **Uniqueness** | Requires conditions on operators (multivalued theory) |
| **Fixed vs. Variable** | Both treated systematically (separate chapters) |
| **Pulsation** | Explicitly addresses countable impulses in finite time |
| **Death Trajectories** | Recognizes solutions cannot extend if operator unmapped |
| **Stability** | Direct Lyapunov method for discontinuous systems |
| **Periodicity** | Almost-periodic, periodic systems in detail |
| **Optimal Control** | Impulsive optimal control problems solved |

**Relationship to Other Frameworks:**

- **Compared to Orlov (Framework 29):** Orlov uses distributions rigorously; Samoilenko-Perestyuk use operator-theoretic approach (more general for multivalued systems)
- **Compared to Kamaraju (Framework 27):** Kamaraju uses Laplace transforms for linear systems; Samoilenko-Perestyuk handle nonlinear systems and variable impulse times
- **Compared to Pandit-Deo (Framework 30):** Pandit-Deo attempted distributional approach (flawed); Samoilenko-Perestyuk avoid distributions entirely
- **Compared to Benchohra (Framework 1):** Benchohra focuses on existence/uniqueness theorems; Samoilenko-Perestyuk add stability, periodicity, and control
- **Unique:** Most comprehensive—only framework treating all three impulse classes with full mathematical rigor

---

## Advanced Topics

**Periodic and Almost-Periodic Systems (Chapter 4):**

Extends Floquet theory to impulsive systems. For linear periodic impulsive system:
$$\dot{x} = A(t)x, \quad t \neq T_i$$
$$\Delta x|_{t=T_i} = B_i x$$

with period $T$, the monodromy operator is $\Phi(T,0) \circ B_k \circ \cdots \circ B_1 \circ \Phi(T_1,0)$.

Characteristic multipliers $\mu_i$ (eigenvalues of monodromy operator) determine stability.

**Integral Sets (Chapter 5):**

Studies bounded solutions and existence of invariant sets. For hyperbolic systems, uses roughness theory to show integral sets persist under perturbations.

**Optimal Control (Chapter 6):**

Pontryagin maximum principle extended to impulsive systems. Necessary conditions for optimality include:
1. Adjoint equation: $\dot{p} = -\nabla_x H$
2. Maximum condition: $H(t,x,u^*,p) = \max_u H(t,x,u,p)$
3. Jump conditions: $p(T_i^+) = B_i^T p(T_i^-)$ (modified adjoint at impulses)

**Asymptotic Methods (Chapter 7):**

Averaging methods for impulsive systems: approximate solution of rapidly-oscillating impulsive system by simpler averaged system. Includes substantiation (rigorous error bounds) for non-resonant and resonant cases.

---

## Summary: Samoilenko-Perestyuk Unified Framework

**The Complete Picture:**

$$\boxed{\text{Impulsive System} = \text{ODE between impulses} + \text{Operator jumps at impulses} + \text{Discontinuous dynamics}}$$

**Key Mathematical Insights:**

1. **Piecewise Continuity:** Solutions are continuous between impulses, discontinuous at impulses
2. **Operator Composition:** Evolution = $g(t) \circ A_i \circ g(t) \circ A_{i-1} \circ \cdots$
3. **Multivalued Dynamics:** Operators can split, merge, or kill trajectories
4. **Pulsation:** Can have countably many impulses in finite time
5. **Lyapunov Stability:** Classical method extends to impulsive systems
6. **Universality:** Direct method is universal (works for discontinuous systems beyond ODE)

**Hierarchy Position:** Framework 32 (Comprehensive Mathematical Theory)

This is the **most complete and rigorous** treatment in the collection. While Orlov provides control synthesis, and Macaulay shows physical origins, Samoilenko-Perestyuk present the definitive mathematical edifice—the reference against which all other approaches are measured.

**Legacy of Kiev School:**

The textbook represents 30+ years of development by Ukraine's leading nonlinear mechanics researchers. It demonstrates that **impulsive systems are not pathological extensions of ODE theory, but a rich and natural generalization with its own methods, theorems, and applications**—equivalent in depth and breadth to classical ODE theory itself.

