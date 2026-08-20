# Framework 50: Benchohra & Boutefal - Impulsive Hyperbolic System of PDE of Fractional Order with Delay

**Authors:** Mouffak Benchohra, Zohra Boutefal  
**Journal:** Commentationes Mathematicae  
**Volume/Issue:** Vol. 54, No. 2  
**Publication Year:** 2014  
**Pages:** 179–189  
**Institutions:** Laboratory of Mathematics, University of Sidi Bel-Abbès, Algeria; Department of Mathematics, Faculty of Science, King Abdulaziz University, Saudi Arabia  

---

## CENTRAL MISSION AND UNIQUE CONTRIBUTION

The Benchohra & Boutefal (2014) paper extends the theory of impulsive systems from finite-dimensional ODEs to **infinite-dimensional hyperbolic partial differential equations (PDEs) with fractional-order derivatives and time delays**. 

**System Studied:**

$$\begin{cases}
^c D^r u(t,x) = f(t,x,u_{(t,x)}) & (t,x) \in J_k, \quad k=0,1,\ldots,m \\
u(t_k^+, x) = u(t_k^-, x) + I_k(u(t_k^-, x)) & x \in [0,b], \quad k=1,\ldots,m \\
u(t,x) = \phi(t,x) & (t,x) \in \widetilde{J} \\
u(t,0) = \phi(t), \quad u(0,x) = \psi(x) & \text{boundary conditions}
\end{cases}$$

**Unique Contributions:**

1. **Fractional hyperbolic systems:** Uses Caputo fractional derivatives of order $r = (r_1, r_2) \in (0,1]^2$ applied to mixed partial derivatives
2. **Fixed impulse times with state jumps:** Discontinuities at predetermined times $0 = t_0 < t_1 < \cdots < t_m < t_{m+1} = a$, with state jumps via impulse functions $I_k$
3. **Finite delay in space:** Incorporates delay in the spatial coordinate through the delayed-argument function $u_{(t,x)}$
4. **Fixed point existence:** Uses **Krasnoselskii fixed point theorem** to prove existence of solutions without requiring contraction mapping conditions
5. **Generalized Grönwall inequality:** Employs Grönwall lemma for two independent variables with singular kernel to handle fractional derivatives

**Mathematical Significance:**

This paper bridges three major areas:
- **Impulsive ODEs** (Lakshmikantham, Samoilenko, Perestyuk)
- **Fractional calculus** (Caputo derivatives)
- **Hyperbolic PDEs** (distributed-parameter systems)

It extends the **impulse response/convolution integral** framework from finite-dimensional systems to infinite-dimensional Banach spaces via functional analytic methods.

---

## TREATMENT OF DISCONTINUITIES ON THE RIGHT-HAND SIDE

### Type 1: Discontinuities in the Dynamics (Spatial Discontinuities)

**Equation (1) - Core Dynamics:**
$$^c D^r u(t,x) = f(t,x, u_{(t,x)})$$

where $^c D^r$ is the **Caputo fractional-order derivative** of order $r = (r_1, r_2)$ with:

$$\text{Definition 2.2: } (^c D^r u)(t,x) = (I^{1-r} u)(t,x) \Big|_{\partial^2/\partial t \partial x}$$

where $I^{1-r}$ is the **left-sided mixed Riemann-Liouville integral** (Definition 2.1):

$$(I^r u)(t,x) = \frac{1}{\Gamma(r_1)\Gamma(r_2)} \int_0^t \int_0^x (t-s)^{r_1-1}(x-\tau)^{r_2-1} u(s,\tau) d\tau ds$$

**Spatial delays:** The dependence on $u_{(t,x)} = u(t+s, x+\tau)$ for $(s,\tau) \in [-\alpha, 0] \times [-\beta, 0]$ introduces **state dependence on delayed (or advanced in history) states**, not discontinuity in the classical sense, but a form of **functional dependence**.

---

### Type 2: Discontinuities via Impulsive Jumps (Temporal Discontinuities)

**Equation (2) - Impulse Conditions:**
$$u(t_k^+, x) = u(t_k^-, x) + I_k(u(t_k^-, x)), \quad k = 1, \ldots, m$$

This is the **explicit state jump mechanism** at impulse times $t_k$:

- **Before impulse:** $u(t_k^-, x)$ (limit from the left)
- **After impulse:** $u(t_k^+, x) = u(t_k^-, x) + I_k(\cdot)$ (limit from the right)
- **Discontinuous state transition:** The difference $\Delta u(t_k, x) = I_k(u(t_k^-, x))$ is the **impulse magnitude**

**Causal Structure:**

Each impulse is an instantaneous perturbation applied at a fixed time, modeled as:
$$u(t,x) = \begin{cases}
u_k(t,x) & t_k < t \le t_{k+1} \\
u_k(t,x) + I_k(u_k(t_k^-, x)) & \text{at } t = t_k^+
\end{cases}$$

where $u_k$ is the solution in the $k$-th interval $J_k = (t_k, t_{k+1}]$.

---

### Type 3: Discontinuity Handling via Fixed Point Formulation

The paper **does not use differential inclusions or Filippov solutions**. Instead, it reformulates the impulsive system as an **integral equation** (Lemma 3.2), avoiding explicit handling of distributional derivatives.

**Reformulated Problem (Equation 5):**

$$u(t,x) = \begin{cases}
\phi(t,x) & (t,x) \in \widetilde{J} \\
\mu(t,x) + \sum_{t_k < t} I_k(u(t_k^-, x)) + \sum_{t_k < t} [I_k(u(t_k^-, x)) - I_k(u(t_k^-, 0))] \\
\quad + \frac{1}{\Gamma(r_1)\Gamma(r_2)} \int_{t_k}^t \int_0^x (t-s)^{r_1-1}(x-\tau)^{r_2-1} f(s,\tau,u_{(s,\tau)}) d\tau ds & (t,x) \in J
\end{cases}$$

**Key observation:** The jumps $I_k(\cdot)$ are **incorporated as Volterra-type integral operators**, transformed away from singular differential form to regular integral form.

---

## CONNECTION BETWEEN DISCONTINUOUS FORCING AND INITIAL CONDITION JUMPS

### Analogy to Finite-Dimensional Theory

In finite-dimensional ODEs with impulses:
$$\dot{x}(t) = f(t,x), \quad x(t_k^+) = x(t_k^-) + I_k(x(t_k^-))$$

The impulse $I_k$ is a **functional perturbation** that instantaneously changes state. Equivalently, this can be viewed as:
- A discontinuous **input forcing** applied exactly at $t = t_k$
- Manifesting as a **discontinuous state change**

### Extension to PDEs with Fractional Derivatives

In the Benchohra-Boutefal framework, the spatial domain $x \in [0,b]$ introduces **distributed parameters**. The state $u(t,x)$ is now a function of both time and space:

1. **Between impulse times** ($t \in (t_k, t_{k+1}]$), the system evolves according to fractional hyperbolic dynamics
2. **At impulse times** ($t = t_k$), the state **jumps** by a spatially-varying amount $I_k(u(t_k^-, x))$
3. **After the jump**, evolution resumes from the new initial condition $u(t_k^+, x) = u(t_k^-, x) + I_k(u(t_k^-, x))$

**No explicit conversion between discontinuous forcing and initial condition jumps** is stated in this paper, as it focuses on **existence of solutions** via fixed point theorems, not on the equivalence relationship. However, the structure suggests:

**Impulsive forcing at $t=t_k$** (in generalized sense) $\iff$ **Discontinuous state jump** $\Delta u(t_k, x) = I_k(u(t_k^-, x))$

---

## SOLUTION METHODOLOGY: KRASNOSELSKII FIXED POINT THEOREM

The paper avoids direct integration of the differential system. Instead:

### Step 1: Operator Decomposition

Define operators $F, G : \Omega \to \Omega$ on the Banach space:
$$\Omega = \{u : [-\alpha, a] \times [-\beta, b] \to \mathbb{R}^n : u|_{[-\alpha,0] \times [-\beta,0]} \in C, u|_{[0,a] \times [0,b]} \in PC\}$$

where $PC$ denotes piecewise continuous functions with jumps at impulse times $t_k$.

**Operator $F$ (Impulse part):**
$$F(u)(t,x) = \begin{cases}
\phi(t,x) & (t,x) \in \widetilde{J} \\
\mu(t,x) + \sum_{t_k < t} I_k(u(t_k^-, x)) - I_k(u(t_k^-, 0)) & (t,x) \in J
\end{cases}$$

**Operator $G$ (Fractional integral part):**
$$G(u)(t,x) = \frac{1}{\Gamma(r_1)\Gamma(r_2)} \int_0^t \int_0^x (t-s)^{r_1-1}(x-\tau)^{r_2-1} f(s,\tau, u_{(s,\tau)}) d\tau ds$$

### Step 2: Krasnoselskii Theorem

**Theorem 2.4 (Burton-Kirk):**

If:
- $F$ is a **contraction** with constant $l$ (from hypothesis H3)
- $G$ is **completely continuous** (continuous + compact)
- The set $E_\lambda = \{u \in C : u = \lambda F(u) + \lambda G(u), \lambda \in (0,1)\}$ is bounded

Then $F + G$ has a fixed point in $\Omega$.

### Step 3: Main Theorem

**Theorem 3.3:**

Assume hypotheses (H1)-(H3) hold. If:
$$(8) \quad 2ml < 1$$

then the IVP (1)-(4) has at least one solution on $J$, where $m$ is the number of impulses and $l$ is the Lipschitz constant for $I_k$.

**Why this works:**
- Hypothesis (H3) makes $F$ a **strict contraction** if $2ml < 1$ (the factor of 2 comes from two boundary conditions)
- Operator $G$ (involving fractional integrals) maps bounded sets to bounded sets, hence is **relatively compact**
- The **a priori bounds** (via generalized Grönwall inequality) ensure the solution set doesn't escape to infinity
- **Krasnoselskii theorem** then guarantees existence without requiring $F$ to be a full contraction on the entire space

---

## MATHEMATICAL FRAMEWORK DETAILS

### Fractional Calculus Treatment

**Caputo Fractional Derivative** (Definition 2.2):

For $r = (r_1, r_2) \in (0,1]^2$:

$$^c D^r u = (I^{1-r} u)|_{\partial^2/\partial t \partial x}$$

This means:
1. First apply mixed partial derivative $\frac{\partial^2 u}{\partial t \partial x}$
2. Then apply fractional integral of order $(1-r_1, 1-r_2)$

**Advantages of Caputo over Riemann-Liouville:**
- Initial conditions are specified at classical derivatives
- Better suited to physical applications (memory effects decay)
- Integral representation avoids derivative of the input function

### Generalized Grönwall Inequality (Lemma 2.3)

**Two-variable fractional version:**

If $\upsilon : J \to [0, \infty)$ and $\omega$ nonnegative, locally integrable, with $0 < r_1, r_2 < 1$:

$$\upsilon(t,x) \le \omega(t,x) + c \int_0^t \int_0^x \frac{\upsilon(s,\tau)}{(t-s)^{r_1}(x-\tau)^{r_2}} d\tau ds$$

Then there exists $\delta = \delta(r_1, r_2)$ such that:

$$\upsilon(t,x) \le \omega(t,x) + \delta c \int_0^t \int_0^x \frac{\omega(s,\tau)}{(t-s)^{r_1}(x-\tau)^{r_2}} d\tau ds$$

**Role:** Bounds solutions even with fractional singularities in the kernel, essential for proving boundedness of the solution set $E_\lambda$.

---

## CONCRETE EXAMPLE: SCALAR FRACTIONAL HYPERBOLIC SYSTEM

**Problem (9)-(12) - Test Case:**

$$^c D^r u(t,x) = \frac{1}{(10e^{t+x}+2)(1+|u|)}$$

$$I_k(u(t_k^-, x)) = \frac{1}{(6e^{t+x}+4)(1+|u(t_k^-, x)|)}$$

**Verification:**
- Hypothesis (H1): $f$ is continuous (satisfied)
- Hypothesis (H2): Linear growth in $u$ (satisfied)
- Hypothesis (H3): Lipschitz constant $l = \frac{1}{6e^4}$ for $I_k$

**Solution existence condition:**
$$2ml = 2(1) \cdot \frac{1}{6e^4} = \frac{1}{3e^4} < 1 \quad \checkmark$$

For $a = b = 1, m = 1, r_1, r_2 \in (0,1]$, the system has a solution on $[-1,1] \times [-2,1]$.

---

## HIERARCHICAL POSITION IN FRAMEWORK TAXONOMY

### Mathematical Sophistication Level

**Level 3-4:** Intermediate-Advanced Theoretical Mathematics
- Requires knowledge of Banach spaces, fixed point theorems, fractional calculus
- Not accessible to typical engineering students
- Targeted at applied mathematics/mathematical analysis researchers

### Scope and Generality

**Dimension:** Infinite (distributed-parameter systems in Banach space)
- PDEs (two independent variables $t, x$)
- General $n$-dimensional state space $u : J \to \mathbb{R}^n$

**Operator Type:** Nonlinear hyperbolic PDEs
- Mixed partial derivatives $\frac{\partial^2}{\partial t \partial x}$
- Fractional order $r \in (0,1]^2$ (singular kernels)
- Functional dependence on delayed/history states

**Forcing/Disturbances:**
- Continuous forcing $f(t,x,u_{(t,x)})$ in intervals
- Discrete impulses $I_k$ at fixed times

### Comparison to Other Frameworks

| Framework | System | Dynamics | Impulses | Fractional | Existence Method |
|-----------|--------|----------|----------|-----------|------------------|
| **Benchohra-50** | Hyperbolic PDE | Nonlinear, fractional | Fixed times with jumps | ✓ Caputo | Krasnoselskii FPT |
| Benaroya-48 | SDOF ODE | Linear, viscous damping | Via initial conditions | ✗ No | Analytical (Duhamel) |
| Inman-49 | SDOF ODE | Linear, viscous damping | Via initial conditions | ✗ No | Analytical (Laplace) |
| Lakshmikantham-15 | SDOF ODE | Nonlinear impulsive | Fixed times | ✗ No | Fixed point theorems |
| Yang-37 | General ODE | Nonlinear, impulsive control | Via control input | ✗ No | Lyapunov methods |
| Zabczyk-38 | Infinite-dim ODE | Nonlinear, abstract | Via operator perturbations | ~ Sometimes | Measure-theoretic |
| Brogliato-3 | Multi-DOF, nonsmooth | Nonlinear, friction-induced | Sliding modes, impacts | ✗ No | Measure-differential inclusions |

**Closest Relatives:**
- **Lakshmikantham et al. (Framework 15):** ODE impulsive systems; Benchohra extends to PDEs
- **Benchohra's own work (Framework 10, referenced):** General impulsive differential inclusions; this paper specializes to fractional hyperbolic systems

---

## KEY TECHNICAL CONTRIBUTIONS

### 1. Handling Fractional Derivatives in Impulsive Context

The paper shows that **fractional derivatives can coexist with discontinuous jumps** provided:
- The jumps occur at **discrete times** (measure zero in the temporal domain)
- The integro-differential formulation (Lemma 3.2) treats jumps as boundary conditions, not as distributional terms

### 2. Piecewise Continuous Function Spaces

Solution space:
$$\Omega = \{u : u|_{[-\alpha,0] \times [-\beta,0]} \in C, \; u|_{[0,a] \times [0,b]} \in PC\}$$

where $PC$ consists of functions continuous on each $J_k = (t_k, t_{k+1}] \times [0,b]$ with right-limits at impulse times.

**Norm:**
$$\|u\|_{\Omega} = \sup_{(t,x) \in [-\alpha, a] \times [-\beta, b]} |u(t,x)|$$

This is a **Banach space**, enabling fixed point theorem application.

### 3. Conditions for Contraction

Hypothesis (H3): $I_k$ are Lipschitz with constant $l$:
$$\|I_k(u) - I_k(v)\|_{\mathbb{R}^n} \le l \|u - v\|_{\mathbb{R}^n}$$

Combined with **$m$ impulses** over time interval $[0,a]$, the contraction condition becomes:
$$2ml < 1$$

(Factor of 2 accounts for both spatial and temporal boundary effects.)

### 4. Grönwall Inequality for Singular Kernels

Standard Grönwall inequality doesn't apply directly because the fractional integral has **singular kernels** $(t-s)^{r_1-1}(x-\tau)^{r_2-1}$ with $r_1, r_2 \in (0,1)$.

The generalized version (Lemma 2.3) provides:
- **Existence of constant $\delta$** depending only on $(r_1, r_2)$
- **Uniform bounds** on solutions despite singularities
- **A priori estimates** ensuring $E_\lambda$ is bounded, closing the Krasnoselskii argument

---

## STRENGTHS AND LIMITATIONS

### Strengths

1. **Extends impulsive ODE theory to PDEs:** Bridges finite and infinite-dimensional systems
2. **Fractional calculus integration:** Handles memory effects and long-range interactions
3. **Rigorous existence proof:** Fixed point methods with a priori bounds
4. **General framework:** Applies to systems with arbitrary impulse functions $I_k$, not restricted to linear systems
5. **Spatial delay handling:** Incorporates functional dependence on history states

### Limitations

1. **Existence only:** Does NOT construct solutions; no uniqueness, stability, or regularity results
2. **No discontinuous right-hand side theory:** Does not employ Filippov solutions or differential inclusions
3. **Fixed impulse times:** Impulses occur at predetermined times, not data-dependent
4. **Lipschitz requirement on impulses:** Condition (H3) assumes Lipschitz continuity; cannot handle more singular impulse laws
5. **Contraction condition restrictive:** Condition (8) $2ml < 1$ becomes harder to satisfy with many impulses ($m$ large) or large Lipschitz constants ($l$ large)
6. **No numerical methods:** Paper provides no algorithms for computing solutions
7. **Limited practical examples:** Single test case with specific functional forms

---

## POSITION IN LITERATURE HIERARCHY

**Tier:** Level 3-4 Theoretical Mathematical Framework (Advanced)

**Role in Literature Review:**

Benchohra & Boutefal bridges three major mathematical traditions:
1. **Impulsive systems theory** (Lakshmikantham, Samoilenko, Perestyuk) → finite-dimensional ODEs
2. **Fractional calculus** (Caputo, Riemann-Liouville) → memory and hereditary effects
3. **Distributed-parameter systems** (PDE theory, Sobolev spaces) → infinite-dimensional dynamics

The paper demonstrates that the **impulse-as-state-jump mechanism** is not limited to finite-dimensional systems but extends to infinite-dimensional Banach spaces with fractional derivative operators.

### Contrast with Engineering Frameworks

| Aspect | Benchohra-50 | Inman/Benaroya/Rao (49,48,47) |
|--------|--------------|------------------------------|
| **System dimension** | Infinite (PDEs) | Finite (ODEs) |
| **Derivative type** | Fractional (Caputo) | Integer order |
| **Forcing** | Continuous + impulsive | Harmonic, periodic, arbitrary |
| **Proof method** | Fixed point theorems | Analytical solutions |
| **Audience** | Applied mathematicians | Engineers, practitioners |
| **Computability** | Existence only | Explicit formulas, numerical codes |

---

## CONCLUSION

Benchohra & Boutefal (2014) represents a **theoretical pinnacle** of impulsive system theory, extending the finite-dimensional impulse-response framework to infinite-dimensional fractional hyperbolic PDEs.

While it does **not explicitly formalize the equivalence between impulsive forcing and initial condition jumps** (as the engineering texts do), the paper's integral equation formulation (Lemma 3.2) implicitly assumes this equivalence: the jumps $I_k(\cdot)$ are treated as state perturbations modifying initial/boundary conditions for subsequent evolution.

For the broader literature review on discontinuous differential equations, this paper exemplifies:
1. **Generalization to fractional operators:** Impulsive systems survive fractional differentiation
2. **Functional analysis perspective:** Fixed point theorems replace explicit solution formulas
3. **Existence without explicit solutions:** Krasnoselskii theorem guarantees solutions exist, even if they cannot be written in closed form

This framework is essential for understanding the **theoretical foundations** of impulsive systems in infinite-dimensional spaces, complementing the engineering-oriented treatments in Frameworks 47–49.

