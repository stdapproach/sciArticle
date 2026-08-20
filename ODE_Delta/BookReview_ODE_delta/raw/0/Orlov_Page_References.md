# Orlov Book - Exact Page References
## Impulse Response, Delta Functions, and Initial Condition Changes

---

## TOPIC 1: Impulse Response
### Section 2.1.2: "Instantaneous Impulse Response in a Nonlinear Setting"

**PAGES: 14-20** (Section runs until Section 2.1.3 starts on page 21)

**Key Content Location:**
- Page 14: Section 2.1.2 title and begins with affine system model
  ```
  ẋ(t) = f(x,t) + b(x,t)u, x(0) = x₀
  ```
- Pages 14-20: Detailed treatment of impulse response in nonlinear setting
- Discusses handling of impulse δ-wise inputs u(t)
- Generalized solutions via limiting approximations
- Concept of "vibrocorrectness" (unique impulse response)

**Related Discussion:**
- Pages 2-3: Introduction to impulsive systems (Section 1.1)
- Page 21+: Section 2.1.3 on Vibroimpact Solutions

---

## TOPIC 2: Delta Function as Load (Load / Forcing)
### Multiple Locations Discussing Dirac Delta in Coefficients

**PRIMARY REFERENCE - PREFACE:**
**PAGE: vii-viii** (Preface, second-to-last page of Preface)

**Exact Quote Location:**
> "While allowing Dirac functions in the coefficients, the equations admit instantaneous jumps of the state of the system. The instantaneous impulse response of the system is adequately defined according to Schwartz' distribution theory in a nonlinear setting."

**SECONDARY REFERENCE - CHAPTER 2 SECTION 2.1.2:**
**PAGES: 14-20**

Mathematical treatment of delta function in input gain:
- b(x,t)u(t) where u(t) contains δ terms
- "an ill-posed product of the Dirac function δ(t − τ), localized at a time instant τ"
- Solution via Schwartz distribution theory
- Limiting approximations to handle ill-posed products

---

## TOPIC 3: Change in Initial Condition as Result of Delta Function

### Three Key Locations:

#### Location 1: PREFACE
**PAGE: vii-viii**

Discussion of restitution rules and state jumps:
> "Whenever the system trajectory hits a switching surface, the continuous state makes a jump, specified by a restitution rule."

**PAGE: vi-vii (Preface)**
> "A discontinuous system is typically viewed as a simple model of hybrid systems, consisting of a finite family of continuous-time subsystems, equipped with a rule of switching between them. Whenever the system trajectory hits a switching surface, the continuous state makes a jump, specified by a restitution rule."

---

#### Location 2: CHAPTER 1 (Introduction) - SECTION 1.1
**PAGES: 1-3** (Section 1.1 "Impulsive Systems")

Discusses:
- State jumps x(τ⁻) → x(τ⁺)
- Restitution rule U(τ, x(τ⁻)) [Equation 1.3]
- Impact systems and discontinuous behavior
- Initial state modifications due to impulses

**Key paragraph on page 1-2:**
"In a particular case where b(x,t) is a state-independent function, solutions of (1.10) subject to an impulse input are defined in the mild sense..."

---

#### Location 3: CHAPTER 2 - SECTION 2.1.2
**PAGES: 14-20** ("Instantaneous Impulse Response in a Nonlinear Setting")

Mathematical formulation of impulse-IC equivalence:
- System equation: ẋ(t) = f(x,t) + b(x,t)u(t)
- Impulse input: u(t) = amplitude·δ(t - τ)
- Result: x(τ⁺) = x(τ⁻) + Δx where Δx is determined by b and impulse amplitude
- Equivalent to modified initial condition for x(0) in homogeneous system

---

## Summary Table

| Topic | Primary Pages | Secondary Pages | Chapter/Section |
|-------|---|---|---|
| **Impulse Response** | 14-20 | 2-3, 21+ | 2.1.2, 1.1, 2.1.3 |
| **Delta Function as Load** | vii-viii | 14-20 | Preface, 2.1.2 |
| **Initial Condition Change** | vii-viii, 1-3 | 14-20 | Preface, 1.1, 2.1.2 |

---

## Document Structure

```
Front Matter (pages i-xi)
  - Preface (v-x) ← Contains Overview of All Three Topics
  - Acknowledgements (xi)

Chapter 1: Introduction (pages 1-12)
  - 1.1 Impulsive Systems (pages 1-3) ← State Jumps & Restitution Rules
  - 1.2 Variable-structure Systems (pages 4-7)
  - 1.3 Hybrid Systems (pages 7-9)
  - 1.4 Sliding Modes (pages 9-12)

Chapter 2: Mathematical Models (pages 13-42)
  - 2.1 Nonlinear Differential Equations in Distributions (pages 13-22)
    - 2.1.1 Preliminaries (page 13)
    - 2.1.2 Instantaneous Impulse Response in Nonlinear Setting (pages 14-20) ← PRIMARY
    - 2.1.3 Vibroimpact Solutions (pages 21-23)
  - 2.2 Differential Equations with Piece-wise Continuous RHS (pages 23-32)
  - 2.3 Modeling Electromechanical Phenomena (pages 33-42)
```

---

## Quick Reference

**For comprehensive understanding of all three topics in one place:**
- **Start:** Page vii-viii (Preface overview)
- **Theory:** Pages 1-3 (Chapter 1.1 - Impulsive Systems)
- **Rigorous treatment:** Pages 14-20 (Section 2.1.2 - Instantaneous Impulse Response)

**Reading sequence:**
1. Preface (vii-viii) - 5 minutes overview
2. Chapter 1.1 (pages 1-3) - 15 minutes conceptual foundation
3. Section 2.1.2 (pages 14-20) - 30-45 minutes detailed mathematics

---

*Analysis Date: 2026-08-20*
*File: Orlov discontinuous-systems-lyapunov-analysis-and-robust-synthesis.pdf*
*Total Pages: ~800*
