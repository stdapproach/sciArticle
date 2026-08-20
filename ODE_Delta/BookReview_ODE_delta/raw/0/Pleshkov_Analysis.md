# Pleshkov: An Efficient Method to Solve ODEs with the Delta Function (2019–2026)

## Analysis Summary

**Central Mission and Unique Contribution:**
Denis Pleshkov develops a **direct algorithmic method** to transform nonhomogeneous linear time-invariant (LTI) ODEs with Dirac delta function forcing into equivalent homogeneous ODEs with modified initial conditions. The unique contribution is the **systematic formulation of the impulse-to-initial-condition equivalence** as an algorithmic procedure: a general transformation that works for any order n-th system with delta forcing (or sums of delta derivatives), supported by both rigorous mathematical derivation and extensive verification against classical literature examples.

---

## Treatment of Discontinuities

**Mathematical Formulation (Section 1.2: "The Dirac Delta Function"):**

The Dirac delta δ(t) is treated as a **generalized function (distribution)** with the defining property:

$$\int_{-\infty}^{\infty} \delta(t-a) f(t) dt = f(a)$$

**Physical Interpretation (Introduction):**

Discontinuities arise from **short-duration, high-magnitude forcing**:
- Impact of a hammer on a beam (impulsive load)
- A bat striking a ball (collision)
- Lightning striking a tower (electrical impulse)

These are "instantaneous events" creating abrupt changes in system state.

**Forcing Function Categories (Section 3: "Problem Type 0"):**

Three classes of problems with delta forcing:

1. **Type 0a:** Single impulse at t=0
$$L_n(y) = b\delta(t), \quad \text{IC}_0, \quad n \geq 1$$

2. **Type 0b:** Time-delayed impulse
$$L_n(y) = b\delta(t-c), \quad \text{IC}_0, \quad n \geq 1$$

3. **Type 0c:** Multiple impulses (sum of delta functions)
$$L_n(y) = \sum_{i=0}^k b_i\delta(t-c_i), \quad \text{IC}_0, \quad n \geq 1$$

**Key Insight on Discontinuity Treatment:**

Unlike frameworks that use advanced mathematics (distribution theory, measure theory, operator methods), Pleshkov's approach **eliminates the discontinuity entirely** through algebraic transformation. The delta function disappears; it becomes an adjustment to initial conditions.

---

## Treatment of Impulse Response

**Foundational Definition (Section 1.4: "Impulse Response Function"):**

$$\text{Impulse response } g(t) = \text{System output when input is } \delta(t) \text{ with all IC = 0}$$

**Frequency Domain Connection (Section 1.4):**

$$H(s) = \mathcal{L}\{g(t)\}$$
$$g(t) = \mathcal{L}^{-1}\{H(s)\}$$

The impulse response is simply the **inverse Laplace transform of the transfer function**.

**Concrete Mechanism (Section 2.1: "First Glimpse"):**

For first-order system: $x' + Ax = B\delta(t)$ with $x(0) = x_0$

Applying Laplace transform:
$$sX(s) - x_0 + AX(s) = B$$

Solving: $X(s) = \frac{x_0 + B}{s+A}$

Inverse: $x(t) = e^{-At}(x_0 + B)$

This solution is identical to solving the **homogeneous system** $x' + Ax = 0$ with modified initial condition $x(0) = x_0 + B$.

**Control Theory Connection (Section 5.2: "Connection with Control Theory"):**

For linear time-invariant systems:
- Transfer function: $W(s) = Y(s)/U(s)$ (with zero IC)
- Impulse response: $g(t) = \mathcal{L}^{-1}\{W(s)\}$
- The impulse response **completely characterizes** the system dynamics

---

## Connection: Discontinuous Forcing ↔ Discontinuous Initial Condition

**The Central Equivalence (Section 2: "Literature Review: Equivalence through Initial Condition Modification"):**

**Literature Survey Finding:**

Pleshkov systematically surveys 30+ classical sources (Genta, Rao, Weber, Kelly, Balachandran, Beards, Bottega, Chasnov, Cortes, and others) and documents that they all observe:

$$\boxed{\begin{cases} L_n(y) = b\delta(t) \\ \text{IC}_0 \end{cases} \equiv \begin{cases} L_n(z) = 0 \\ \text{IC}_{\text{modified}} \end{cases}}$$

**Specific Examples from Literature:**

1. **Rao (p. 407):** 
$$\begin{cases} y' + ay = F\delta(t) \\ y(0) = 0 \end{cases} \equiv \begin{cases} y' + ay = 0 \\ y(0) = F \end{cases}$$

2. **Weber (p. 733):**
$$\begin{cases} mx'' = P\delta(t) \\ x(0) = 0, x'(0) = 0 \end{cases} \equiv \begin{cases} mx'' = 0 \\ x(0) = 0, x'(0) = P/m \end{cases}$$

3. **Kelly (p. 315):**
$$\begin{cases} mx'' + cx' + kx = \delta(t) \\ x(0) = 0, x'(0) = 0 \end{cases} \equiv \begin{cases} mx'' + cx' + kx = 0 \\ x(0) = 0, x'(0) = 1/m \end{cases}$$

**General Pattern (Conjecture 2.7):**

For n-th order system with impulse magnitude b on RHS:

$$\begin{cases} L_n(\{a\}, y) = b\delta(t) \\ \text{IC}|_{t_0} = \mathbf{IC}_0 \end{cases} \equiv \begin{cases} L_n(\{a\}, y) = 0 \\ \text{IC}|_{t_0} = \mathbf{IC}_0 + (0,0,\ldots,0, b/a_0)^T \end{cases}$$

**Rigorous Justification (Section 3.1.3: "Solution of Type 0a"):**

Using Laplace transform, prove the equivalence algebraically. The key step is recognizing that the lower-triangular matrix structure of the system (after Laplace transformation) makes the correction vector simplify dramatically:

$$A^{-1}\mathbf{d} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ b/a_0 \end{bmatrix}$$

Only the last initial condition is affected by the impulse.

**Physical Meaning:**

- **Impulse magnitude** b = total momentum/energy imparted by instantaneous event
- **Jump in initial condition** Δy = b/a₀ = impulse divided by leading coefficient
- **System evolution after jump** follows homogeneous dynamics with new initial state

---

## Algorithmic Framework

**Three Problem Types and Solutions:**

**Type 0a (Single impulse at t=0):**

Formula (3.3):
$$\begin{cases} L_n(\{a\}, y) = b\delta(t) \\ \text{IC}_0 \end{cases} \equiv \begin{cases} L_n(\{a\}, y) = 0 \\ \text{IC}_0 + (0,0,\ldots,0, b/a_0)^T \end{cases}$$

**Type 0b (Delayed impulse at t=c):**

Use time-shifting property of Laplace transform. The solution on [0,c] is homogeneous with IC₀. At t=c, apply the impulse to create a jump. Continue on [c,∞) with modified initial conditions.

**Type 0c (Multiple impulses):**

Apply superposition principle. Each impulse at time cᵢ with magnitude bᵢ creates a jump Δyᵢ = bᵢ/a₀ in the highest derivative. Treat each interval separately, using final values from previous interval as initial conditions for the next.

**Type 1 (Delta derivatives on RHS):**

When forcing is $\sum_{j=0}^m b_j\delta^{(m-j)}(t)$ (sum of delta derivatives):

$$\begin{cases} \sum_i a_i y^{(n-i)}(t) = \sum_j b_j\delta^{(m-j)}(t), \quad m < n \\ \text{IC}_0 \end{cases} \equiv \begin{cases} \sum_i a_i y^{(n-i)}(t) = 0 \\ \text{IC}_0 + A^{-1}\mathbf{d} \end{cases}$$

where the correction vector $\mathbf{d}$ contains the coefficients b₀, b₁, ..., bₘ in its last m+1 entries.

---

## Verification and Validation

**Systematic Examples (Section 4: "Verification of Type 0 by Examples"):**

Nine detailed examples demonstrating the method:

1. **Example 1 [Oliveira & Cortes, p. 3]** — Second-order system with analytical solution y(t) = (1/a)(1-e^(-at))

2. **Example 2 [Finan, pp. 57-58]** — Analytical: y(t) = (1/4)e^(-t)sin(2t)

3. **Example 3 [Nagy, p. 189]** — Analytical: y(t) = e^(-t)sin(t)

4. **Example 4 [Nagy, p. 189]** — Delayed impulse at t=2; Analytical: y(t) = H(t-2)e^(-(t-2))sin(t-2)

5. **Example 5 [Chasnov, p. 65]** — Delayed impulse; Analytical: y(t) = (2/√15)H(t-2)e^(-(t-2)/4)sin(√15(t-2)/4)

6. **Example 6 [Zill, p. 293]** — Analytical: y(t) = 4H(t-2π)sin(t)

7. **Example 7 [Zill, p. 293]** — Non-zero initial conditions; Analytical: y(t) = cos(t) + 4H(t-2π)sin(t)

8. **Example 8 [Nagy, p. 190]** — Two impulses (Type 0c); Analytical: y(t) = (1/2)[H(t-π) - H(t-2π)]sin(2t)

9. **Example 9 [Nagy, p. 190]** — Third-order system; Analytical: y(t) = (1/2 - 1/2)e^(-t)(sin(t) + cos(t))

**Computational Verification:**

Each example verified using:
- Analytical solution from references
- Numerical solution via modified homogeneous system
- Error analysis (typically 1e-8 to 1e-14 relative error)
- Phase diagrams showing system trajectory

**Python Implementation:**

Complete scripts provided at https://github.com/stdapproach/sciArticle/tree/develop/ODE_Delta/raw

All computational results match analytical solutions to machine precision.

---

## Position Within 30+ Framework Hierarchy

**Framework Type: Algorithmic/Pedagogical with Complete Unification**

**Characteristics:**
1. **Approach:** Direct algebraic transformation via Laplace domain
2. **Scope:** Linear time-invariant systems, any order n, any delay structure
3. **Problem Class:** ODEs with Dirac delta and delta derivatives as forcing
4. **Uniqueness:** Only framework providing systematic algorithmic procedure applicable to ALL cases

**Key Distinguishing Features:**

| Aspect | Pleshkov |
|---|---|
| **Impulse Definition** | Δ functional impact on system = jump in highest derivative initial condition |
| **Discontinuity Treatment** | Eliminates it entirely via transformation; no need for distribution theory |
| **Solution Method** | Laplace transform + matrix inversion (simple, programmable) |
| **Impulse Response** | H(s) ↔ h(t) via Laplace; impulse response = inverse Laplace of transfer function |
| **Equivalent Problem** | Always reduces to homogeneous ODE with modified IC |
| **Computational Complexity** | O(n³) for matrix inversion; tractable for arbitrary order |
| **Generality** | Works for delayed impulses, multiple impulses, delta derivatives |
| **Mathematical Rigor** | Algebraic/Laplace domain; avoids measure theory complications |

**Relationship to Other Frameworks:**

- **Compared to Kamaraju (Framework 27):** Both use Laplace transforms; Pleshkov adds explicit algorithm for delta forcing transformation
- **Compared to Orlov (Framework 29):** Orlov uses distribution theory rigorously; Pleshkov uses distributions pragmatically (as Laplace pairs)
- **Compared to Paraskevopoulos (Framework 31):** Both emphasize practical method; Pleshkov focuses on delta forcing, Paraskevopoulos on control design
- **Compared to Samoilenko-Perestyuk (Framework 32):** Both comprehensive; S-P is pure theory, Pleshkov is applied algorithm
- **Compared to Macaulay (Framework 28):** Macaulay shows physical origin (wave propagation); Pleshkov shows how to solve it mathematically
- **Unique Contribution:** First framework to systematically present the **algorithm** for the impulse equivalence that all others discovered piecemeal

---

## Summary: The Core Algorithm

**The Transformation (Formulas 3.3 and 5.4):**

**Original Problem (Type 0):**
$$\begin{cases} L_n(\{a\}, y) = b\delta(t) \text{ or } \sum b_i\delta^{(m-i)}(t) \\ \text{IC}_0 = \{y(0), y'(0), \ldots, y^{(n-1)}(0)\} \end{cases}$$

**Equivalent Problem (Homogeneous):**
$$\begin{cases} L_n(\{a\}, z) = 0 \\ \text{IC}_{\text{new}} = \text{IC}_0 + A^{-1}\mathbf{d} \end{cases}$$

**where:**
- A is the lower-triangular matrix from Laplace domain algebra
- d is the vector of impulse coefficients
- $A^{-1}\mathbf{d}$ simplifies dramatically due to triangular structure

**Why This Works:**

The Laplace transform converts the impulsive differential equation into an algebraic equation. The solution in the Laplace domain already "knows" about the impulse. When we equate Laplace transforms of the original (nonhomogeneous) and equivalent (homogeneous) systems, the impulse forcing is precisely captured by the modified initial conditions.

**Practical Advantage:**

Once the initial conditions are modified, any standard ODE solver (Runge-Kutta, etc.) works. No need for special handling of distributions or delta functions. The "hard" discontinuity problem is solved once at the transformation stage; the computational phase is standard.

---

## Literature Synthesis Achievement

**What Pleshkov Accomplishes:**

By systematically surveying 30+ classical textbooks (Finan, Nagy, Rao, Weber, Kelly, Balachandran, Beards, Bottega, Genta, Meirovich, Schiff, Schmitz, and others), the analysis **documents and unifies** observations scattered across the literature.

**The Key Finding:**

Every textbook that examined ODE + delta function discovered the same equivalence independently. Pleshkov's contribution is:
1. **Systematic organization** of these scattered results
2. **Rigorous proof** using Laplace domain algebra
3. **General formula** (3.3) valid for arbitrary order n
4. **Algorithmic procedure** applicable to all three problem types
5. **Complete verification** via 14+ examples with analytical solutions
6. **Software implementation** enabling numerical solution by transformation

---

## Hierarchical Position: Framework 33 (Algorithmic Synthesis and Unification)

**This framework represents the synthesis point** in the entire 30+ framework collection:

- **Earlier frameworks** (Kamaraju, Paraskevopoulos, Hespanha, Chen) use impulse response pragmatically without explicit equivalence
- **Mathematical frameworks** (Orlov, Samoilenko-Perestyuk, Benchohra) prove equivalence rigorously but not algorithmically
- **Physical frameworks** (Macaulay, Jones, Brogliato) show where impulses come from physically
- **Pedagogical frameworks** (various textbooks) demonstrate equivalence through examples

**Pleshkov's unique role:** Provides the **algorithm** that **all other frameworks** use implicitly.

The impulse response equivalence is not merely a mathematical curiosity—it is the **operational principle** underlying every application of impulse forcing in dynamics, control, and signal processing.

