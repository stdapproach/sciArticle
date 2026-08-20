# Literature Review: Linear ODEs with Dirac Delta Function Forcing

**Denis Pleshkov**  
std.approach@gmail.com  
August 2026

---

## Executive Summary

This literature review examines approaches to solving linear time-invariant (LTI) ordinary differential equations (ODEs) subject to impulsive forcing represented by the Dirac delta function and its derivatives. The review synthesizes findings from differential equations, vibration theory, and control theory domains, identifies methodological gaps in the literature, and contextualizes the equivalence principle (transforming delta-forced nonhomogeneous ODEs into homogeneous systems with modified initial conditions) as a unifying framework across these disciplines.

---

## 1. Introduction

### 1.1 Problem Domain: Impulsive Phenomena in Dynamical Systems

Abrupt perturbations—impacts, collisions, lightning strikes, and sudden force application—are ubiquitous in engineering and physics. Classical approaches represent these as continuous forcing functions, but the shortness and intensity of impulsive events motivate an idealized representation: the **Dirac delta function** $\delta(t)$.

Mathematically, an impulse is modeled within an initial value problem (IVP) as:
$$
\begin{cases}
L_n(y) = b \cdot \delta(t) \\
\text{with initial conditions } \mathbf{IC}_0
\end{cases}
$$

where $L_n$ is a linear differential operator of order $n$ with constant coefficients.

The practical significance lies in two areas:
- **Vibration theory**: Understanding how structures respond to impacts (machinery, seismic events, mechanical testing)
- **Control theory**: The impulse response function $g(t)$ characterizes the entire input-output behavior of an LTI system, from which the transfer function $W(s)$ is derived via Laplace transform

### 1.2 Scope and Organization

This review addresses the following questions:
1. How have different textbooks and research domains handled ODEs with delta forcing?
2. What common patterns emerge across these treatments?
3. Where do significant gaps exist in the literature?
4. How does the equivalence principle unify disparate approaches?

The review is organized into four themes:
- **Historical and foundational treatments** (basic differential equations texts)
- **Specialized applications** (vibration, control, structural dynamics)
- **Methodological evolution** (from specific cases to general formulations)
- **Gaps and synthesis** (missing proofs and generalizations)

---

## 2. Theme 1: Foundational Treatments and Basic Solutions

### 2.1 State of Standard Textbooks

The vast majority of differential equations textbooks provide analytical solutions for specific first- and second-order LTI ODEs with delta forcing but do not explicitly frame the results in terms of initial condition modification. This category dominates the literature.

**Sources providing direct solutions without equivalence discussion:**
- Asadi, Agarwal
- Boyce & DiPrima (standard text, 2nd order)
- Dobrushkin, Goode, Kreyszig (1st and 2nd order systems)
- Zill (well-known text with multiple examples)

**Representative example:**
A second-order system $y'' + ay' = \delta(t)$ with zero initial conditions receives direct Laplace transform solution, yielding $y(t) = \frac{1}{a}(1 - e^{-at})$. However, these texts rarely highlight that this coincides with the solution to the homogeneous system $z'' + az' = 0$ with modified initial conditions $z(0)=0, z'(0)=1/a$.

**Assessment:** While comprehensive and reliable, these treatments remain procedural and do not reveal the underlying principle.

### 2.2 Implicit Recognition of the Equivalence

A substantial subset of textbooks and monographs implicitly recognize that delta forcing modifies initial conditions but lack an explicit formula or formal proof.

**Key observations from literature:**
- **Rao (2011), p. 407:** States the equivalence for first-order systems without proof
  $$\begin{cases} y' + ay = F\delta(t) \\ y(0)=0 \end{cases} \equiv \begin{cases} y' + ay = 0 \\ y(0)=F \end{cases}$$

- **Weber (2003), p. 733:** Notes analogous result for second-order mass-spring systems under impulse

- **Kelly (2012), p. 315; Balachandran & Magrab (2009, 2019):** Observe the pattern for damped oscillators

**Common approach:** These works invoke conservation of momentum or impulse-momentum arguments to justify the initial condition shift, particularly in mechanical systems:
$$\Delta p = \int F \, dt = F_0 \cdot \delta(t) \Rightarrow \text{velocity jump} = F_0/m$$

**Limitation:** The arguments remain informal and are not systematized into a general $n$-th order formula.

---

## 3. Theme 2: Domain-Specific Applications

### 3.1 Vibration Theory and Mechanical Dynamics

Vibration theory extensively employs impulse response functions for characterizing mechanical systems. The impulse response $g(t)$ directly enters design calculations for:
- Shock absorption in machinery
- Seismic response analysis
- Structural health monitoring

**Key contributors:**
- **Meirovitch (1986, 2001):** Frames impulse response within matrix formulation of structural dynamics
- **Genta (2009):** Provides formulas for second-order systems with zero initial conditions, noting the equivalence but limiting scope
- **Beards (1996), Benaroya et al. (2017):** Apply impulse response to practical vibration problems
- **Luintel (2024), Jazar & Marzbani (2024):** Modern treatments emphasizing numerical integration of the equivalent homogeneous system

**Characteristic limitation:** While these texts handle multiple-DOF systems via state-space formulation, they do not extend to general $n$-th order ODEs with derivatives of delta functions.

### 3.2 Control Theory Perspective

In control theory, the impulse response is the inverse Laplace transform of the transfer function $W(s)$, making it central to system characterization.

**Standard formulation:**
$$W(s) = \frac{Y(s)}{X(s)} \quad \Rightarrow \quad g(t) = \mathcal{L}^{-1}\{W(s)\} = \text{Solution of } \begin{cases} L_n(y) = \delta(t) \\ \mathbf{IC} = \mathbf{0} \end{cases}$$

**Key sources:**
- **Ogata (2010):** Defines impulse response; emphasizes numerical implementation
- **Dorf & Bishop (2008):** Modern control systems perspective
- **Franklin, Powell, & Emami-Naeini (2015):** Feedback control context with emphasis on transfer functions

**Significance:** Control theory naturally deals with derivatives of delta on the right-hand side (e.g., when the transfer function numerator has degree $m < n$). However, standard texts do not systematically address this general case.

---

## 4. Theme 3: Evolution Toward General Formulations

### 4.1 Explicit Formulas for Special Cases

A small number of sources provide explicit formulas for modifying initial conditions in specific problem types:

- **Edwards, Penney, & Calvis (2016):** Formula for second-order systems with time shift: $\delta(t - c)$
- **Klee & Allen (2011):** Detailed treatment of initial condition modification for second-order cases
- **Chasnov (2009–2016):** Lecture notes with explicit formula (limited to second order)

**Pattern:** These sources progress beyond narrative justification to algebraic procedure but typically restrict scope to second-order problems.

### 4.2 State-Space and Transfer Function Approaches

Some authors address the problem via state-space representation, which naturally generalizes to higher orders:

- **Angeles (2011):** Dynamic response of linear systems; notes IRF as changed initial condition in state-space form
- **Esfandiari & Lu (2014):** Modeling and analysis of dynamic systems; extensive treatment of impulse response via state-space

**Advantage:** State-space methods scale to arbitrary order and naturally accommodate derivatives of delta.

**Limitation:** These treatments remain tied to numerical implementation; formal algebraic proof of the general equivalence principle is absent.

### 4.3 Theoretical Foundations: Distributions and Differential Equations

**Filippov (1988):** Differential equations with discontinuous right-hand sides
- Provides rigorous treatment of impulses and derivatives of distributions as forcing terms
- Discusses recurrence relations for impulse response functions
- Allows delta functions in coefficients (more advanced than typical texts)
- **Limitation:** Very advanced; not connected to practical impulse response calculation

**Benchohra, Henderson, & Ntouyas (2006):** Impulsive differential equations and inclusions
- Frames impulse response problems within broader impulsive DE theory
- Provides existence and uniqueness theorems
- **Limitation:** Abstract; pedagogical gap between theory and practical computation

---

## 5. Theme 4: Critical Gaps and the Role of Systematic Unification

### 5.1 Identified Gaps in the Literature

**Gap 1: Missing General Proof**
Despite numerous textbooks noting the equivalence for first- and second-order systems, a formal proof for arbitrary $n$-th order ODEs is absent from standard references. Section 2.3 of the original article's survey of 100+ sources reveals this absence explicitly.

**Gap 2: Derivatives of Delta Function (Type 1 Problems)**
Only Filippov (1988), Beneš (1978), and Angeles (2011, p. 144) provide treatments of systems with $\delta^{(m)}(t)$ on the right-hand side. No standard textbook supplies a closed-form algorithm combining derivatives of delta with the equivalence principle.

**Gap 3: Pedagogical Bridge**
Theoretical texts (distributions, impulsive DEs) and computational texts (numerical methods, control systems) remain disconnected. A student seeking both rigor and applicability finds few resources.

**Gap 4: Unified Computational Framework**
While individual approaches (Laplace inversion, state-space integration, impulse-momentum arguments) work, no single algorithmic framework unified them until recent work.

### 5.2 The Equivalence Principle as Unifying Framework

The core insight—that an IVP forced by $\sum b_j \delta^{(m-j)}(t)$ with initial conditions $\mathbf{IC}_0$ is equivalent to the homogeneous system with initial conditions $\mathbf{IC}_0 + A^{-1}\mathbf{d}$—provides:

1. **Generality:** Works for any order $n$ and any distribution $L_m(\{b\}, \delta)$ with $m < n$
2. **Computational efficiency:** No Laplace inversion needed; integrate the homogeneous system
3. **Pedagogical clarity:** Single principle explains examples across vibration, control, and dynamics
4. **Theoretical rigor:** Rooted in Laplace transform algebra, not informal momentum arguments

---

## 6. Connection to Contemporary Research Domains

### 6.1 Vibration Theory Extensions

Contemporary work extends classical impulse response to:
- **Fractional-order derivatives:** Time-fractional wave equations with impulse excitation (Springer, Qualitative Theory of Dynamical Systems, 2025)
- **Viscoelastic media:** Optimal control of mechanical structures in viscoelastic environments (post-2020)
- **Neural network approximations:** Learning impulse response from data (ScienceDirect, post-2015)

**Implication:** The classical equivalence principle provides a foundation for these extensions; understanding the standard case is prerequisite.

### 6.2 Control Theory and Stability

- Transfer functions and impulse response characterization remain central to robust control design
- Model predictive control and adaptive systems rely on accurate impulse response models
- The equivalence principle enables rapid numerical impulse response computation for high-order systems

---

## 7. Synthesis and Summary of Findings

### 7.1 State of the Field

| Aspect | Current State | Evidence |
|--------|---------------|----------|
| **First/second-order solutions** | Comprehensive | 100+ textbooks |
| **Explicit equivalence formula (n-th order)** | Absent from literature | Survey of 100+ sources; only post-2019 appearance |
| **Derivatives of delta** | Rarely treated | Only Filippov, Beneš, Angeles explicitly |
| **Pedagogical integration** | Fragmented | Theory, vibration, and control texts rarely cross-reference |
| **Computational efficiency** | Recognized but not systematized | Implicit in state-space methods; not algorithmicized |

### 7.2 Role of the Equivalence Principle

The equivalence principle—transforming delta-forced nonhomogeneous ODEs into homogeneous systems with modified initial conditions—:
- Unifies isolated observations across 50+ years of literature
- Enables computation without specialized knowledge of Laplace transforms
- Extends naturally to derivatives of delta (Type 1 problems)
- Provides a framework for teaching ODEs across vibration and control contexts

---

## 8. Research Implications and Future Directions

### 8.1 For ODE Theory

The systematic treatment of delta-forced ODEs through the equivalence principle suggests:
- Pedagogical revision of ODE textbooks to present the general principle early
- Extension to time-varying coefficients (nonhomogeneous $a_i(t)$)
- Connection to Green's function formalism and integral equations

### 8.2 For Vibration and Control

- Rapid numerical impulse response computation for model-based design
- Foundation for robust control design with impulsive disturbances
- Extension to nonlinear systems via linearization + equivalence principle

### 8.3 For Advanced Topics

- Fractional-order ODEs with delta forcing
- Impulses in systems with constraints (differential-algebraic equations)
- Stochastic differential equations with delta processes

---

## 9. Conclusion

The literature on linear ODEs with delta forcing reveals a mature empirical understanding but a fragmented theoretical presentation. Standard textbooks solve first- and second-order cases via routine Laplace methods. Specialized texts (vibration, control) recognize the equivalence principle informally through momentum or transfer function arguments. Rigorous mathematical treatments (distributions, impulsive DEs) remain disconnected from computational practice.

The **equivalence principle**—that delta-forced nonhomogeneous systems reduce to homogeneous systems with shifted initial conditions—bridges these domains. Its systematic proof for $n$-th order ODEs and extension to derivatives of delta unifies scattered observations and provides a pedagogically transparent, computationally efficient framework.

Future work should integrate this principle into:
1. Undergraduate and graduate ODE curricula
2. Vibration and control theory courses as a primary tool
3. Numerical methods for impulse response computation
4. Extensions to fractional and nonlinear systems

---

## References

### Primary Mathematical Texts

[1] Boyce, W. E., & DiPrima, R. C. (2012). *Elementary differential equations and boundary value problems* (10th ed.). John Wiley & Sons.

[2] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons.

[3] Zill, D. G. (2009). *A first course in differential equations with modeling applications* (9th ed.). Brooks/Cole, Cengage Learning.

### Vibration Theory

[4] Balachandran, B., & Magrab, E. B. (2009). *Vibrations* (2nd ed., International SI ed.). Cengage Learning.

[5] Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press.

[6] Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press.

[7] Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press.

[8] Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media.

[9] Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson Education.

[10] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore.

[11] Meirovitch, L. (1986). *Elements of vibration analysis* (Subsequent ed.). McGraw-Hill College.

[12] Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill.

[13] Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education.

### Control Theory

[14] Dorf, R. C., & Bishop, R. H. (2008). *Modern control systems: Solution manual* (11th ed.). Pearson Education.

[15] Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited.

[16] Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education.

### Advanced and Theoretical Treatments

[17] Benchohra, M., Henderson, J., & Ntouyas, S. (2006). *Impulsive differential equations and inclusions*. Hindawi Publishing Corporation.

[18] Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides*. Springer-Science+Business Media.

[19] Duffy, D. G. (2015). *Green's functions with applications* (2nd ed.). CRC Press.

### Related Specialized Works

[20] Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media.

[21] Esfandiari, R. S., & Lu, B. (2014). *Modeling and analysis of dynamic systems* (2nd ed.). CRC Press.

[22] Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG.

[23] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications, SI*. Cengage Learning.

[24] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press.

[25] Williams, R. L., II, & Lawrence, D. A. (2007). *Linear state-space control systems*. John Wiley & Sons.

---

**Note:** This literature review synthesizes 100+ sources referenced in the original article's detailed classification (Section 2.3). The references listed above represent the most significant contributions to each theme. For the complete taxonomy of sources by category (solutions without equivalence discussion, implicit recognition, explicit formulas, etc.), refer to the original article's Section 2.3.
