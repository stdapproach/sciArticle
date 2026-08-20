# Gear & Østerby: Solving Ordinary Differential Equations with Discontinuities

## Reference
**Paper**: Solving Ordinary Differential Equations with Discontinuities  
**Authors**: Charles William Gear (University of Illinois at Urbana-Champaign), Ole Østerby (Aarhus University, Denmark)  
**Journal**: ACM Transactions on Mathematical Software  
**Date**: Vol. 10, No. 1, pp. 23–44, March 1984  
**Impact**: Seminal work on automatic detection and handling of discontinuities in ODE solvers

---

## CENTRAL MISSION: Automatic Detection and Numerical Handling of Discontinuities

### The Problem They Solved

**Context in 1984:**
- Standard ODE solvers (like LSODE, GEAR codes) were inefficient at discontinuities
- Solvers would reject steps repeatedly (see Figure 1 in paper: 97 steps with 18 rejections just to pass one discontinuity!)
- Users had to manually specify discontinuity locations or use ad-hoc techniques
- No systematic method for automatic detection, location, and passing of discontinuities

**Contribution**: Develop a systematic, automatic procedure to:
1. **Detect** discontinuities
2. **Locate** them precisely
3. **Characterize** their order and magnitude
4. **Pass** them with error control
5. **Restart** the integration smoothly

---

## FOUR-STAGE ALGORITHM

### Stage 1: Detection (Very Inexpensive)

**Key insight**: Discontinuities cause large local error estimates.

**Detection method:**
```
At each rejected step, check if:
h_new << h_old

Specifically: if h_new < h_old/2, assume discontinuity present

Why it works:
- Smooth f → stepsize halving manageable
- Discontinuous f → stepsize must reduce by much more
- Ratio h_new/h_old indicates severity

Cost: Minimal (already computed in any variable-step code)
```

**Implementation:**
```
Standard error control formula:
h_new = (E / error_estimate)^(1/(p+1)) × h_old

If h_new < h_old/2 → discontinuity suspected
```

### Stage 2: Locating and Characterizing the Discontinuity

**Key theoretical result** (Equations 2.14, 2.19 in paper):

For discontinuity of order q at x = ξ:
```
Local error estimate ~ O(h^q)
Actual local error ~ O(h^q)

Error is controlled by:
- Jump magnitude K_q
- Discontinuity order q
- Position θ = (x_{n+k} - ξ)/h ∈ (0,1)
```

**Discontinuity order definition:**
```
Order q means:
- f has continuous derivatives through order q-2
- First finite jump appears in q-1 th derivative of f

Examples:
q = 1: Jump in f itself (step function)
q = 2: Jump in f_x (or f_y) (ramp function)
q = 3: Jump in f_xx or f_yy, etc.
```

#### Determining Order via Divided Differences

**First divided difference (detect q = 1):**
```
d_1 = (F_R - F_L) / h

where F_R, F_L = function values at right, left of interval

Behavior when halving stepsize:
- If q = 1: d_1 doubles (discontinuity moves to one side)
- If q ≥ 2: d_1 decreases (discontinuity span increases)

See Figures 4-5 in paper
```

**Second divided difference (detect q = 2):**
```
d_2 = (F_R - 2F_M + F_L) / (2h²)

where F_M = function value at midpoint

After two halvings, Table I in paper shows:
- If q = 2: d_2 multiplied by 4 (or by interval, see table)
- If q ≥ 3: d_2 multiplied by smaller factors

Can distinguish q = 2 from q ≥ 3 with confidence
```

#### Estimating Jump Magnitude K_q

**Formula (Equation 2.21 in paper):**
```
Passing stepsize:
h_pass = [(q-1)! × E / K_q]^(1/q)

For q = 1 (simplest case):
h_pass = E / K_1

where K_1 = |F_R - F_L| (magnitude of jump in f)
```

**Use of K_q:**
```
Knowing K_q and q, can predict stepsize needed
to maintain error < tolerance E when crossing discontinuity
```

### Stage 3: Passing the Discontinuity

**Strategy**:
```
Once q and K_q known:
1) Step right up to discontinuity location ξ
2) Use stepsize h < h_pass to ensure error control
3) Step over the discontinuity
4) Continue with normal stepping

With known ξ: ~1 extra step sufficient
With bisection:  ~log₂(1/tolerance) steps needed
Without method: 97 steps + 18 rejections!
```

**Error control formula (Equation 2.21):**
```
h_pass = [(q-1)! × E / K_q]^(1/q)

Ensures local error in passing ≤ E
```

**Location estimate (Equation 4.6):**
```
For q = 2, can extrapolate to estimate ξ:
ξ ≈ x_M - F_M × (x_R - x_M)/(F_R - F_M)

This gives location without full bisection
```

### Stage 4: Restarting

**Critical issue**: After discontinuity, previous solution history is invalid.

**Actions required:**
```
1) Cannot use stored history of y and f
2) Must either:
   - Restart with fresh history
   - Reduce order of multistep method
3) May need to reinitialize internal corrector

Reason: Multistep methods assume smooth solution
        Discontinuity breaks this assumption
```

---

## THEORETICAL FOUNDATIONS

### Local Truncation Error Analysis

**For smooth f:**
```
LTE = C_{p+1} h^{p+1} y^{(p+1)}(x_n) + O(h^{p+2})
```

**At discontinuity of order q:**
```
Local error estimate ~ γ h^q K_q + smooth term

When q ≤ p:
  Leading term = O(h^q) from discontinuity
  Smooth term = O(h^{p+1}) becomes negligible
  
When q > p+1:
  Method may NOT detect discontinuity!
  (Smooth term dominates)
```

### Error Estimate vs. Actual Error

**Key insight** (Equations 2.14, 2.19):

Milne's device error estimate:
```
Error_estimate ~ γ × β_k × (θ^{q-1}/(q-1)!) × h^q K_q
```

Actual error:
```
Error_actual ~ (θ^q - β_k × θ^{q-1}/(q-1)!) × h^q K_q
```

**Problem**: γ and β_k are different!
```
For Adams' methods: γ negative, |γ| ≤ 0.1
This means:
  Error_estimate could be order of magnitude SMALLER
  than actual error!

Solution:
- Use corrector-predictor difference directly
- Or reduce tolerance when discontinuity detected
```

---

## PRACTICAL ALGORITHM

### Pseudocode (Simplified from Paper)

```
PROCEDURE Handle_Discontinuity()
  
  Stage1: DETECT
    IF h_new < 0.5 × h_old THEN
      discontinuity_suspected = TRUE
      q ← 1  [worst case]
      K_1 ← |f_R - f_L|
      h_pass ← E / K_1
    END IF
  
  Stage2: CHARACTERIZE
    Halve stepsize, switch to PEC mode
    
    REPEAT
      Take step
      IF failed THEN
        Compute d_1
        IF d_1 ≥ 2 × d_1_old THEN
          q ← 1  [confirmed]
        ELSE
          q ← 2  [higher order]
        END IF
        Halve h again
      ELSE
        IF h < h_pass THEN
          Break [can pass now]
        ELSE
          Halve h again
        END IF
      END IF
    UNTIL ready_to_pass
  
  Stage3: LOCATE
    IF q = 2 AND have_two_halvings THEN
      ξ ← extrapolate from divided differences
      Step to x = ξ - ε
    ELSE
      Use bisection method
      (halve step until x_{n+k} just passes ξ)
    END IF
  
  Stage4: RESTART
    Reduce order OR restart integration
    Continue with normal method
    
END PROCEDURE
```

---

## EXAMPLE: Simple Discontinuity

**Problem** (from Figure 1):
```
y' = { 0        if x < 40.33
     { 100      if x ≥ 40.33
y(0) = 40.33

Known discontinuity location: x = 40.33
```

**Performance comparison:**

| Method | Function Calls | Steps | Rejections |
|--------|---|---|---|
| **Standard code** | 118 | 97 | 18 |
| **With known location** | ~20 | ~3 | 0 |
| **With bisection** | ~50 | ~25 | ~2 |

**Why standard code struggles:**
```
At x < 40.33: Method works fine, stepsize increases
At x ≈ 40.33: Suddenly y' jumps to 100
             Error estimate explodes
             Step rejected, h halved drastically
At x > 40.33: Smooth solution exists, h should increase
             But memory of discontinuity still in method
             
Result: Many failed attempts before recovery
```

---

## HANDLING DIFFERENT DISCONTINUITY TYPES

### Type 1: Jump in f Itself (q = 1)

**Example:**
```
y' = { f₁(x,y)   if x < ξ
     { f₂(x,y)   if x ≥ ξ

Jump magnitude: K₁ = |f₂(ξ,y) - f₁(ξ,y)|
```

**Handling:**
```
h_pass = E / K₁

Easy to detect and locate (largest jumps)
```

### Type 2: Jump in Derivative (q = 2)

**Example:**
```
y' = f(x,y) where ∂f/∂x or ∂f/∂y jumps at x = ξ
y remains C¹ (continuous and differentiable)
```

**Handling:**
```
h_pass = √(E / K₂)

Harder to detect (second-order effect)
Requires divided difference d₂
```

### Type 3: Higher-Order Discontinuities (q ≥ 3)

**Handling:**
```
h_pass = (E / K_q)^(1/q)

Smaller stepsize needed
But easier to pass (error ~ O(h^q) with q ≥ 3)
```

### Type 4: State-Dependent Discontinuities

**Example:**
```
Discontinuity triggered by g(x, y(x)) = 0
(collision, phase transition, switch, etc.)

NOT known in advance
```

**Strategy:**
```
User provides switching function:
  h_trigger = x_value where discontinuity occurs

Can use:
- Inverse interpolation to find zero
- Event location methods (Shampine-Gordon)
- Root finding on g(x, y(x)) = 0

Gear-Østerby methods apply AFTER detection
```

---

## CONNECTION TO DISCONTINUOUS RHS AND INITIAL CONDITIONS

### Jump Discontinuity in Solution

**Scenario:**
```
Imposed jump at x = ξ:
  y(ξ⁻) ≠ y(ξ⁺)
  Δy = y(ξ⁺) - y(ξ⁻)

This corresponds to q = 4 discontinuity in the sense that:
  y⁽⁴⁾ has a jump
```

**Numerical handling:**
```
Same procedure: detect, locate, characterize, pass
Stepsize: h_pass = (E / K₄)^(1/4)

Or treat as special boundary condition at ξ
```

### Change in Initial Condition

**Equivalent formulation:**
```
Discontinuous initial condition at x₀:
  y(x₀⁺) - y(x₀⁻) = Δy
  
Can be handled as:
  1) Internal discontinuity at x₀
  2) Or simply restart integration with y(x₀⁺) as new initial condition

Gear-Østerby framework applies
```

---

## COMPARISON TO OTHER FRAMEWORKS

### Gear-Østerby vs. Other Approaches

| Approach | Method | Advantage | Limitation |
|----------|--------|-----------|-----------|
| **Gear-Østerby** | Automatic detection & stepping | General, automatic | Requires understanding of error control |
| **Event location** (Shampine) | User-supplied event function | Precise location | Requires knowing trigger condition |
| **Bisection** | Manual subdivision | Simple | Manual work |
| **Analytical** (Falsone) | Generalized functions | Exact solution | Only for special cases |
| **Dishliev** | Impulsive theory | Asymptotic properties | Not numerical |

### Why Gear-Østerby Was Revolutionary

**Before 1984:**
- User had to know where discontinuities occur
- Or manually tune solver parameters
- Or accept inefficiency

**After 1984:**
- Automatic detection
- Systematic location (bisection or extrapolation)
- Error control through h_pass formula
- No user intervention needed

**Modern impact:**
- Basis for event handling in MATLAB ODE solvers
- Foundation for hybrid system simulators
- Incorporated into LSODA, LSODE, CVODE codes

---

## PRACTICAL WORKFLOW

### Implementing Gear-Østerby Method

**Step 1: Hook into existing ODE solver**
```
Modify step acceptance/rejection logic:
  IF step_rejected AND h_new < 0.5*h_old THEN
    Call discontinuity_handler()
  END IF
```

**Step 2: Estimate discontinuity order**
```
Use first divided difference test:
  IF d_1 ≥ 2*d_1_prev THEN q = 1
  ELSE compute d_2
    IF d_2 shows factor ~4 THEN q = 2
    ELSE q ≥ 3
  END IF
```

**Step 3: Determine location strategy**
```
IF q = 2 AND confident in location estimate THEN
  Use linear extrapolation (Eq. 4.6)
ELSE
  Use bisection:
    Halve h repeatedly until just passing
END IF
```

**Step 4: Set passing stepsize**
```
h_pass = [(q-1)! × E / K_q]^(1/q)

Ensure next step uses h ≤ h_pass
```

**Step 5: Restart cleanly**
```
After passing discontinuity:
  Clear multistep history (or reduce order)
  Continue with normal stepping
```

---

## RELEVANCE TO DISCONTINUOUS RHS RESEARCH

**Gear-Østerby's contribution is foundational** because:

✓ **First systematic automatic method** — For handling discontinuities in general ODE solvers  
✓ **Rigorous error analysis** — Links discontinuity order to stepsize control  
✓ **Practical algorithms** — Detection, location, characterization, passing, restart  
✓ **Divided difference techniques** — Distinguishes discontinuity orders automatically  
✓ **Error control formulas** — h_pass ensures error bounds despite discontinuities  
✓ **State-dependent discontinuities** — Framework applies to collision, switching, phase transitions  
✓ **Industry standard** — Basis for all modern ODE solvers' event handling  

**Connection to theoretical frameworks:**
- **Dishliev**: Analyzes what happens asymptotically; Gear-Østerby handles numerical computation
- **Falsone**: Analytical solution for special cases; Gear-Østerby numerical general method
- **Cooper**: Theoretical distributions; Gear-Østerby practical numerical treatment
- **Brogliato**: Theory of nonsmooth systems; Gear-Østerby implements numerically

---

## COMPLETE HIERARCHY: All Fourteen Frameworks

| # | Author | Level | Method | Best For |
|---|--------|-------|--------|----------|
| 1 | **Camporesi (1)** | Elementary | Initial conditions | Intuition |
| 2 | **Camporesi (2)** | Elementary | Factorization | Variable coeff |
| 3 | **Chen** | Classical | State-space | Foundational |
| 4 | **d'Andréa-Novel** | Classical | Transfer functions | Frequency domain |
| 5 | **Brogliato** | Rigorous | Measures | Nonsmooth mech |
| 6 | **Chalishajar** | Applied | Generalized functions | Beams (advanced) |
| 7 | **Chicurel-Uziel** | Novel | Parametrization | Nonlinear |
| 8 | **Cooper** | Foundation | Distribution theory | Math rigor |
| 9 | **Dahleh** | Practice | Systems theory | Engineering |
| 10 | **Datta** | Computation | Numerical algorithms | Implementation |
| 11 | **Dishliev** | Qualitative | Impulsive theory | Asymptotic |
| 12 | **Fairman** | Design | Control synthesis | Design |
| 13 | **Falsone** | Applied | Generalized functions | Beams (pedagogy) |
| 14 | **Gear** | Computational | Automatic methods | Numerical ODE solving |

**The complete ecosystem:**

```
Cooper: Mathematical foundations
   ↓
Classical: How to analyze (Chen, Dahleh, Fairman, d'Andréa-Novel)
   ↓
Computational: How to compute
   ├─ Datta: Traditional numerical methods
   └─ Gear-Østerby: Automatic discontinuity handling
   ↓
Practical applications
   ├─ Brogliato: Nonsmooth mechanics
   ├─ Falsone: Beam problems (pedagogy)
   └─ Chalishajar: Beam problems (advanced)
   ↓
Theory specialization
   ├─ Dishliev: Asymptotic behavior
   └─ Chicurel-Uziel: Nonlinear extension
```

---

## SUMMARY

**Gear & Østerby's contribution is revolutionary** because:

✓ **Automatic detection** — No user specification needed  
✓ **Order determination** — Distinguish q=1, q=2, q≥3 automatically  
✓ **Location estimation** — Bisection or extrapolation methods  
✓ **Error control** — h_pass formula ensures tolerance compliance  
✓ **Restart procedures** — Handle history corruption from discontinuity  
✓ **Practical algorithms** — Implemented in modern ODE solvers  
✓ **Efficiency gains** — From 97 steps (18 rejections) to 3-25 steps  

**Why Gear & Østerby matters:**

This paper transformed ODE solver practice by showing that:
1. Discontinuities CAN be handled automatically
2. Order and magnitude can be estimated numerically
3. Error control is possible despite discontinuities
4. Efficiency gains are enormous (~10×)

**Modern impact:**
- All MATLAB ODE solvers (ode45, ode23, etc.) have event detection
- Based on Gear-Østerby principles
- Hybrid system simulators (Simulink, Ptolemy) use these methods
- CVODE and other production solvers implement this

**Gear & Østerby showed that automatic detection and handling of discontinuities is not only possible, but practical and efficient—foundational for all modern numerical ODE solving.**
