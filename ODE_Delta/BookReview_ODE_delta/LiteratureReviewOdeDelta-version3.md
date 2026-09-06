## The Impulse–Initial Condition Equivalence in Linear ODEs: A Literature Review

**Denis Pleshkov**
<std.approach@gmail.com>
September 2026

### Abstract

This literature review examines how linear time-invariant (LTI) ordinary differential equations (ODEs) with impulsive forcing (represented by the Dirac delta function and its derivatives) are treated across differential equations, vibration theory, and control theory. Motivated by the practical need to find proper solution approaches and closed-form formulas for such systems, we surveyed 100+ sources and classified them by how explicitly each addresses the equivalence between an impulse-forced initial value problem and a homogeneous one with modified initial conditions. While this equivalence is well established for specific low-order equations, a fully general, explicit, closed-form, and invertible formula for an arbitrary finite combination of derivatives of the Dirac delta at a single point turns out to already exist in the literature: a classical operational-calculus result found in Popov (1962, §2.16), predating nearly every other source surveyed here. This result, and the closely related but individually incomplete counterparts also identified (Brigola & Singer, 2009; Filippov, 1988, tracing to Aizerman & Gantmakher, 1956; Ahuja & Arya, 2019; Kavaja & Piazzi, 2019; Nedeljkov & Oberguggenberger, 2012, among others), remain fragmented across at least three largely non-cross-referencing literatures — classical Soviet/Russian control engineering, generalized-function/distribution theory, and behavioral systems theory — with no single, unified, explicit treatment covering both an arbitrary combination of delta derivatives and multiple impulses at distinct points. The central finding of this review is therefore not the outright absence of a general closed-form result, but its historical fragmentation, and the surveyed modern literature's apparent unawareness of Popov's much earlier, fully general single-point solution.

### Keywords

Literature review, delta function, differential equation, ODE, impulse response, initial condition, equivalence

### Introduction

The dynamics of evolving processes are often subject to abrupt changes, such as: impact of a hammer on a beam, a bat striking a ball, a bolt of lightning striking a tower.

Such short-term perturbations are frequently treated as instantaneous events, often modeled as "impulses" (see also Cohen, p. 13, for an analogous billiard-ball example). Logan (p.166) "Many physical and biological processes have source terms that act at a single instant of time. For example, we can idealize an injection of medicine (a "shot") into the blood stream as occurring at a single instant; a mechanical system, for example, a damped spring–mass system in a shock absorber on a car can be given an impulsive force by hitting a bump in the road; the switch in an electrical circuit can be closed only for an instant, which leads to an impulsive, applied voltage". According to Rao (p. 381) "The simplest form is the impulsive force a force that has a large magnitude F and acts for a very short time". The system's response to such a force is termed the impulse response function (IRF). Mathematically, an impulse can be represented within an initial value problem (IVP) by incorporating the Dirac delta function as the external forcing term. An IVP consists of an ODE together with the system's state at some initial time; its solution is the unique function satisfying both. The impulse response of a system is defined as its output in response to an input $\delta(t)$, assuming the system is initially at rest. A recurring pattern across this literature is that such an impulse-forced problem is equivalent to the corresponding homogeneous problem — the same ODE without forcing — with its initial condition shifted to account for the impulse. This impulse–initial condition equivalence is the central relationship this review investigates.

We are searching the literature for solutions to LTI ODEs with a discontinuous right-hand side, including the delta function and its derivatives. The Dirac delta function is a well-known generalized function (distribution) used to model impulsive phenomena. Its properties are discussed extensively in the literature, including Arfken (pp.76-79), Bottega (p. 233), Chasnov (p. 58), Nagy (p. 196-201), Weber (p. 86-90), Zill (p. 328-330).

While seeking a general method to solve such systems, we found that existing literature primarily offers solutions for specific first- and second-order ODEs, with the general n-th order, arbitrary-combination case treated only rarely, and, it turns out, largely in isolation from itself. General distributional solution mechanisms exist in principle (via fundamental solutions and convolution); closely related rigorous treatments exist in the generalized-function and behavioral-systems literatures (Brigola & Singer, 2009, §2.7; Nedeljkov & Oberguggenberger, 2012, §2.6; Kavaja & Piazzi, 2019, §2.11; Ahuja & Arya, 2019, §2.10; Filippov, 1988, §2.15); and a fully explicit, general, invertible, closed-form formula for the single-point case — the exact direction and form used in this review — was in fact published decades earlier, in the classical control-engineering literature, by Popov (1962, §2.16). None of these sources, however, cites or appears aware of any of the others, and none extends to multiple impulses at distinct points within a single unified framework.

The sources reviewed here were identified through a manual survey of over 100 textbooks and articles in differential equations, vibration theory, and control theory, selected for their treatment of impulsive or discontinuous forcing in linear time-invariant systems. Section 1 establishes the equivalence pattern observed across this literature; Section 2 classifies the surveyed sources into five categories based on how explicitly they state this equivalence; Section 3 draws conclusions and identifies the resulting gaps.

### 1 Equivalence through initial condition's modification

Several textbooks provide analytical solutions for first/second order LTI ODEs with a Dirac delta forcing function. Examples include Nagy (pp. 203-209: "The Impulse Response Function"), Ogata (p. 163: "Unit-Impulse Response of First-Order Systems"; p.178: "Impulse Response of Second-Order Systems"), Rao (p. 382: "4.5.1 Response to an Impulse"), Tewari (pp. 109-113: "3.2.1 Impulse Response", deriving $g(t)=\mathcal L^{-1}\{G(s)\}$ via partial-fraction expansion, worked for both real and complex-conjugate poles), and Zill (p. 330: "Two Initial-Value Problems").

Baruh (p.9): "Impulsive forces cause sudden changes in velocity with very little (or negligible) change in position"

Other authors explicitly note that the solution of an IVP with a delta load coincides with the solution of the corresponding homogeneous ODE subject to modified initial conditions (IC). A brief survey of such observations follows.

Rao (p. 407: "Unit Impulse Response of a First-Order System") states the equivalence for 1st order system

$
\begin{cases}
y' + a y = F \delta(t), \\
y(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
y' + a y = 0, \\
y(0) = F
\end{cases}
$

Balachandran (p. 301: "Similarity to Response to Initial Velocity"), Bottega (pp. 235–236: "problem of interest becomes equivalent to the problem of free vibrations with the initial conditions"), Genta (p. 179-180: "The position x0 after the impulse is equal to that before the impulse,
while the velocity v0 is equal to the one before the impulse plus an increment"), Meirovitch (pp. 160–161: "we conclude that the effect of a unit impulse at t = 0 is to produce an equivalent initial velocity"), Schiff (p. 83: "indicating the instantaneous jump in velocity at t=0, from a rest state to the value v0"), Weber (p. 733: "Impulsive Force") notes the analogous result; all remarked that

$
\begin{cases}
m x'' + c x' + k x = f_0 \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' + c x' + k x = 0, \\
x(0) = 0, \\
x'(0) = f_0/m
\end{cases}
$

Chasnov (p. 61) provides a formula for changing the IC of a second-order LTI ODE.
The LTI IVP with discontinuous right side can also be viewed as a special case of an impulsive differential equation (see Benchohra, Henderson, and Ntouyas); for the broader qualitative theory of such systems — existence, uniqueness, stability, and periodicity, built directly from jump conditions $\Delta x|_{t=\tau_i}=J_i(x)$ rather than derived from distributional forcing — see also the foundational monograph of Lakshmikantham, Bainov, and Simeonov (1989) — whose Notes trace the jump-condition formalism to Mil'man and Myshkis, and point to Halanay and Wexler (1968) as an alternative treatment — as well as Samoilenko and Perestyuk (1995), Akhmet (2010), and Perestyuk, Plotnikov, Samoilenko, and Skripnik (2011), none of which — including Benchohra, Henderson, and Ntouyas themselves (whose book was checked in full for this review across its first 147 pages, covering existence theory for ordinary, functional, semilinear, and multivalued impulsive problems) — formulates or uses the Dirac delta, its derivatives, or the Laplace transform.

The above examples suggest a general pattern (though a formal proof appears to be missing in the literature): an IVP forced by a delta function may be equivalent to a homogeneous IVP with a shifted IC.

A particularly clear illustration of this pattern, worked out in careful detail rather than merely asserted, is given by Lundberg, Miller, and Trumper (2007) for an idealized automobile-suspension model $m\ddot y = b(\dot x - \dot y) + k(x-y)$ driven by a step input $x(t)=u(t)$: a step in the wheel position produces a force impulse $b\delta(t)$ from the damper, which instantaneously shifts the pre-initial velocity $\dot y(0^-)$ by $b/m$ while leaving the position continuous — exactly the impulse–initial-condition shift this review documents, worked through explicitly with the (correctly defined) unilateral Laplace transform rather than left as a qualitative remark (see §2.8).

### 2 Detailed literature classification

We surveyed the following sources and classified each by how explicitly it addresses the equivalence between an impulse-forced IVP and a homogeneous IVP with modified initial conditions.

| Category | Criterion | Count | Representative authors |
|---|---|---|---|
| 1 | Solves the impulse-forced system without stating the equivalence | 16 | Alam, Boyce, Kreyszig, Ricardo |
| 2 | Mentions the change of IC qualitatively, without a formula | 12 | Antsaklis, Brogliato, Logan, Shabana |
| 3 | Gives an explicit formula for specific equation orders | 32 | Angeles, Chopra, Meirovitch, Trench |
| 4 | Gives a formula for a general n-th order equation, delta-only load | 6 | Adkins, Beneš, Camporesi, Filippov |
| 5 | Closed-form solution for a sum of derivatives of delta | 1 | Popov (§2.16) — *not counted:* closely related but individually incomplete counterparts Brigola & Singer (§2.7), Filippov (§2.15) |

#### 2.1 Solution without mentioning the equivalence (i.e. unit impulse is equal to change IC)
   Alam (p. 218 1st order, pp. 270-274 2nd order), Asadi (pp. 62-73), Benaroya (p. 147 IRF 2nd order), Boyce (p.272), Campbell (p.263), Dorf (p.327; the same textbook, later edition, is also cited by Brigola & Singer, 2009 — see §2.7), Etkin (pp. 73-76), Goode (pp. 708–710), Gupta (pp. 72, 86), Holmes (p.179), Jack (p. 575), Jeffrey (p.412), Korman (p. 160), Kreyszig (pp. 227–230), Neil (pp.102-104), Ricardo (pp.215-216).

#### 2.2 Mention the change of initial condition without giving an explicit formula
   Antsaklis (p. 67: "the impulse response of a linear, time-invariant, continuous time system with integral representation is equal to the kernel of the integral representation of the system"), Benaroya (p.19 due to "principle of conservation of linear momentum" governs the change the velocity via impulse 'During collisions large forces act resulting in almost instantaneous changes in velocity and therefore in linear momentum'), Brogliato (p.2: "impulsive forces imply a discontinuity in the velocity while positions remain continuous"; p.7: in mechanical systems, continuous positions and discontinuous velocities are produced by impulsive forces, and vice versa"), Howell (p. 560: "Observe that using a delta function force leads to the velocity changing instantly from one constant to another"), James (p.345, p.365), Kausel (p. 82: " the impulse imparted on a mass m abruptly changes its velocity from zero to V = 1/m"), Logan (pp.169-170, p.172), MacCluer (p.374: "Notice that the solution in equation ... doesn't actually satisfy the initial condition"), McOwen (pp. 98-99), Peterson (p. 363: "discontinuous forcing function causes a jump in the velocity of the mass"), Ram (p. 22-5), Shabana (p. 40: "This result indicates that the effect of the impulsive force, which acts over a very short time duration on a system which is initially at rest, can be accounted for by considering the motion of the system with initial velocity 11m and zero initial displacement.")

#### 2.3 Provide an explicit formula for changing initial conditions for specific equations
   Anderson and Rufer (pp. 7-10: for the linearized pendulum $\ddot\theta+\theta=\delta(t)$, initially at rest, derive the new initial conditions $\theta(0^+)=0$, $\dot\theta(0^+)=1$ by directly integrating the ODE across the discontinuity at $t=0$, then independently re-derive the identical result via the Laplace transform ($L\{\delta(t)\}=1$), explicitly verifying the two methods agree; also formalize the unit impulse response $h(t)=x(t)=L^{-1}\{H(s)\}$ as a system-identification tool), Ruderman (2017, eqs. 12-17: for a second-order motion system $m\ddot x+d(t)\dot x+Kx=u+v$ with an impulsive control term, derives the state trajectory via $x(t)=\exp(At)x_0+\int_{t_0}^t\exp(A(t-\tau))B\,\mathrm{sign}(\dot x)(-2\alpha)\delta(\tau)\,d\tau$ and takes the limit $t\to t_0$ to obtain an explicit jump map $x^+=x-2B\alpha\,\mathrm{sign}(\dot x)$, then inverts it to design impulsive control gains from a prescribed state jump — a hybrid-control application of the same impulse-to-jump principle), Angeles (p.115: "consequence, the ball undergoes a finite change in its velocity", p.116: change IC for IRF for 1st order system, p.119: change IC for IRF for 2nd order system, pp.132/136: derivative of delta as load), Balachandran (p. 301: IRF for 2nd order system), Baruh (p.259: change IC for 2nd order system due to impulse load), Beards (p.66: "the impulse F, acting on a body will result in a sudden change in its velocity without an appreciable change in its displacement. Thus the motion of a single degree of freedom system excited by an impulse F, corresponds to free vibration with initial conditions x = 0 and v0, = F/m at t = 0"), Chopra (Demonstrates that discontinuous forcing via impulse is mathematically equivalent to modified initial conditions; p.121 exact formulae for change IC for linear oscillator (from zero IC); p.616 example of impulse response for MDOF, multi-degree-of-freedom, systems), Cooper (Provides explicit formula for piecewise smooth derivatives showing jump ↔ delta connection. Foundational reference proving mathematically that impulses (delta forces) arise naturally from discontinuities; p.5 change IC for pendulum was in rest), Duffy (p.93 "This avoids the problem of the Green's function not satisfying all of the initial conditions." + (3.1.7) provide the initial condition delivers the IRF as free motion., p.166, p.284), Edwards (p. 500, 2nd order with time shift), Esfandiari (p. 57: change IC for IRF for 2nd order system/"when impulsive forces are present in the system, initial values and initial conditions are indeed different", p.343: "Impulse Response of First-Order Systems",  p.351/359: "Impulse Response of Second-Order Systems"), Fairman (page 31, In addition we see from (1.81) that the zero-input response equals the impulse response when the initial state is x(0) = B (IRF is equal to some non-zero IC)), Franklin (p.110: change IC on 1st order system), Haddad (p.50 "we can always reproduce the impulsive response with the free response by setting x(0) = Bv"), Hallauer (p. 158 change IC for 1st order system), Inman p.219: "impulsive load for the system initially at rest is calculated by recalling from physics that an impulse imparts a change in momentum to a body", p.557: IRF for PDE/string), Iyengar (p. 87: change IC for SDOF, single-degree-of-freedom, systems whilst delta load, p.121 IRF for MDOF systems), Jazar (pp. 173, p.188: "Impulse will only change the initial conditions, and hence, the response of a multi-DOF system will be the transient response to a new set of initial conditions"), Kabe (pp.149-150: "it would appear that applying a unit impulse at t = 0 is equivalent to giving the system an initial velocity", p.163), Klee (p.170: change IC for 1st order system), Lathi (pp.164-165: "Find the impulse response h(t) for a system specified by (D^2 +5D+6)y(t) = (D+1)x(t)"), Luintel (p.215: "velocity of the system immediately after the application of impulse I is I/m", 507), Meirovitch (p.161: "effect of a unit impulse at t = 0 is to produce an equivalent initial velocity"), Nielsen (p.24: "Consequently, an impulsive load causes a discontinuous change of the velocity", p.63: solution for IRF for MDOF system), Palm (p.96: change IC for 1st/2nd order system, p.116: "Impulse Response of Second-Order Models"), Polking (p.231: IRF for 2nd order system), Schiff (p.82-83 2nd order system with impulse is equal to free vibration of the same system but changed IC), Silva (p.87 for 2nd order system for IRF mentioned change IC, "The Riddle of Zero Initial Conditions"), Sinha (p.69 mentioned changing IC for solution of 1st order ODE with unit impulse as load), Thorby (p.50: "unit impulse of force is applied to it ... that if dv is the change in velocity, then dv=1/m, but the change in displacement is negligible"), Trench (pp. 478–480: solution some 2nd order system with impulse load), Tse (p. 54: change IC for 2nd order system with delta load)

#### 2.4 Supply a formula for the case where the load contains only the delta function (or its derivatives) for general $n$

   - Adkins (p. 319: provide formulae for changing IC to calculate IRF as free response for LTI ODE n-th order)
   - Ahuja and Arya (2019: a general "singular-nonsingular decomposition" algorithm for exactly the setup $\sum a_i y^{(n-i)} = \sum b_j x^{(m-j)}$, $n\ge m$, of the present review's own Type 1 equations, applied in particular to an impulsive input $x(t)=M\delta(t)$; see §2.10)
   - Beneš (1978; for an LTI ODE with a single Dirac-delta forcing term of general order $n$, derives via Laplace-transform coefficient matching — the same method used in the present article — the modified initial conditions of the homogeneous equation, his eq. (9): $y_1^{(k)}(0)=y^{(k)}(0)$ for $k<n-1$ and $y_1^{(n-1)}(0)=1+y^{(n-1)}(0)$, exactly the pure-delta special case of the present article's formula. The paper does not address delta derivatives or sums thereof; the remainder of the paper concerns the realizability of $\delta(t)$ on analog computers, not a further mathematical result)
   - Camporesi (2019; Theorem 4.2, eq. (4.13): an explicit triangular formula, built purely by factorization and convolution, for the coefficients of the impulsive-response basis $\{g,g',\dots,g^{(n-1)}\}$ needed to match arbitrary initial data for general $n$ — see §2.9 for a detailed comparison with the present work)
   - Campos (p. 166: change IC for oscillator with first derivative of delta, p.167: exact solution for oscillator with odd/even derivative of delta as load)
   - Filippov (p.20-21: gives a regularization method converting an ODE with a delta-derivative right-hand side into a system with a regular right-hand side, and, on the following page, an explicit recursive jump formula, eqs. (17)-(18), attributed to Aizerman and Gantmakher (1956), that does supply the missing initial-condition change for a single term $b_iz^{(i)}$, verified in this review as equivalent to the present article's method on a worked example; see §2.15 for the full treatment and the caveat that distinguishes it from a genuine category-5 result)

#### 2.5 Closed-form solution for an LTI ODE with a sum of derivatives of the Dirac delta as the forcing function
   A fully general, explicit, invertible closed-form formula in precisely the direction used in this review — yielding the shifted initial-condition vector directly from an arbitrary finite linear combination of delta derivatives, for a scalar n-th order LTI ODE at a single point — was in fact located in this survey: Popov (1962; §2.16), a classical automatic-control-theory textbook using operational calculus rather than distribution theory. Several further closely related results should also be noted: a general, inverse-direction correspondence of the same underlying linear-algebraic type (Brigola & Singer, 2009; §2.7), a nonlinear, regularization-based treatment of delta-derivative forcing (Nedeljkov & Oberguggenberger, 2012; §2.6), and a verified-equivalent (though differently parametrized) recursive formula tracing to Aizerman and Gantmakher, 1956 (Filippov, 1988; §2.15). See the Conclusion for how this reframes the claim of this review: the surveyed literature is not silent on this problem, but Popov's solution and the modern generalized-function/behavioral-systems literature discussed throughout this section appear never to cite one another, and none of these sources — Popov included — extends to multiple impulses at distinct points within a single unified framework. It is also worth noting that the earliest source found in this survey to use essentially the same method as the present article — Laplace-transform coefficient matching — for a single Dirac-delta forcing term is Beneš (1978; §2.4).

#### 2.6 A related distributional treatment (regularization-based, nonlinear)

A rigorous distributional treatment of ODEs forced by delta-function terms, including derivatives of the delta function, is given by Nedeljkov and Oberguggenberger (2012), who study the nonlinear first-order equation $y'(t) = f(t, y(t)) + g(y(t))\delta^{(s)}(t)$ by regularizing the delta term ($\varphi_\varepsilon \to \delta$) and passing to the limit $\varepsilon \to 0$. In the additive case ($g \equiv \alpha$ constant) with sublinear $f$, their Theorem 1.1(a) shows that the regularized solutions converge to $y(t) = \bar y(t) + \alpha\delta^{(s-1)}(t)$: a genuine distribution whenever $s \ge 1$, since their setting is restricted to first-order ($n=1$) equations. Only for $s = 0$ does the classical initial-condition-shift picture emerge (their Example 2.1, equivalent to the $n=1$ case of formula (3.3) of the main article). Their multiplicative case (Propositions 2.1–2.2, state-dependent $g(y)\delta(t)$) similarly yields a nonlinear jump condition expressed via an invertible primitive $G$.

This work — together with the classical fact that a general distributional solution to $P(D)y = \sum_j b_j \delta^{(j)}$ always exists via convolution with the fundamental solution of $P(D)$ — confirms that delta-derivative-forced ODEs are well understood *as distributions*, and that the restriction $m<n$ used in the main article is exactly the condition under which the response remains a genuine (non-distributional) function rather than one contaminated by a leftover $\delta^{(s-1)}$ term. It does not, however, provide an explicit finite-dimensional formula relating an arbitrary combination $\sum b_j\delta^{(j)}$ of several derivative orders, possibly at several points, to a shifted initial-condition (or jump) vector for a general $n$-th order **scalar LTI** equation — nor is that its aim, since its scope is nonlinear first-order equations with a single impulsive term. This distinction is what the present review's gap (category 5 above) refers to. A related but distinct nonlinear treatment is given by Orlov (2010, §2.1), who studies a single $\gamma\delta(t-t_0)$-forcing term (no derivatives) for a nonlinear affine system $\dot x=f(x,t)+b(x,t)u$ and, via Schwartz' distribution theory, shows that the resulting "instantaneous impulse response" is in general non-unique — it depends on how the delta is approximated — deriving conditions (his Theorem 2.1, citing Miller, 1994, 1996) under which it is nonetheless well defined; this confirms well-posedness of delta-forced responses is an active concern in the nonlinear literature, but neither addresses delta *derivatives* nor supplies a closed-form formula, so it does not narrow the category-5 gap.

#### 2.7 Brigola and Singer (2009): a general n-th order correspondence between initial conditions and delta derivatives

An even closer counterpart to the result that this review finds missing (category 5) is provided by Brigola and Singer (2009), who work entirely within the linear, causal, generalized-function framework of Zemanian and Schwartz. For the general LTI equation $P(D)y = Q(D)f$ with $f = f_r + f_g$ decomposed into a regular and a generalized part, their Theorem 2 (equations 6–8) shows that a classical initial value problem with data $y^{(q)}(0^-) = c_q$, $q = 0,\dots,n-1$, is equivalent, on the causal half-line, to the purely distributional equation

$$
P(D)T = Q(D)f + \sum_{k=1}^{n} a_k \sum_{q=0}^{k-1} c_q\,\delta^{(k-1-q)},
$$

obtained from the standard distributional identity for the derivative of a Heaviside-cut function, $(zu)^{(k)} = z^{(k)}u + \sum_{q=0}^{k-1} c_q\,\delta^{(k-1-q)}$. Collecting the coefficients of each $\delta^{(j)}$, $j=0,\dots,n-1$, on the right-hand side reproduces exactly the linear map given by matrix $A$ of the main article (its Section 3): the vector of $\delta^{(j)}$-coefficients equals $A\mathbf c$ in that notation. Their worked Example 5 demonstrates the mechanics directly: a fourth-order equation with nonzero classical initial data $c_0,\dots,c_3$ is rewritten as $P(D)y = 2\delta + 3u + (\delta''' + 5\delta' - 7\delta)$ and solved by the (ordinary, one-sided) Laplace transform with no correction term in the differentiation rule, because the initial data have already been absorbed into the delta-derivative terms on the right-hand side.

This is, in effect, the same linear correspondence as formula (3.2)–(3.3)/(5.4) of the main article, applied in the opposite direction: Brigola and Singer start from a prescribed classical initial-condition vector $\mathbf c$ and construct the equivalent delta-derivative forcing $A\mathbf c$ that reproduces it under zero pre-history; the main article starts from a prescribed delta-derivative forcing $\mathbf b$ and *inverts* the same triangular map to obtain the equivalent shifted initial-condition vector $\mathbf c = \mathbf c_0 + A^{-1}\mathbf b$, with the explicit closed form $A^{-1}\mathbf b = (0,\dots,0,b_0/a_0)^T$ in the single-delta case. Brigola and Singer do not carry out this inversion explicitly, do not isolate the simple closed form for a pure-delta load, and do not address multiple impulses at distinct points (the main article's Type 0c) — but the underlying linear-algebraic correspondence they establish for a general scalar $n$-th order LTI equation is, to our knowledge, the closest existing counterpart to the category-5 gap identified in this review. The claim of an outright absence of *any* related result should be read in light of this closely related, inverse-direction, and less explicit formula.

A secondary point of interest for the classification in this review: Brigola and Singer cite Dorf and Bishop, *Modern Control Systems*, as a standard reference on transfer-system modeling — the same textbook (a later edition) appears in our own survey under category 1 (§2.1), illustrating how a single widely used engineering textbook can sit at very different levels of explicitness relative to different treatments of the same underlying equivalence.

#### 2.8 Lundberg, Miller and Trumper (2007): a live methodological dispute at the foundation of the topic

A further source worth incorporating, although it does not itself supply a general n-th order formula, is Lundberg, Miller, and Trumper (2007), a widely read IEEE Control Systems Magazine article devoted entirely to how the unilateral Laplace transform should be defined and taught in the immediate neighborhood of $t=0$. Its relevance to this review is threefold.

First, it documents, independently of our own survey, exactly the kind of inconsistency that motivates this review: the authors show that many otherwise-excellent control and differential-equations textbooks are inconsistent or simply wrong about how $\delta(t)$ interacts with the initial-value theorem and the derivative rule, some using a transform $L^+$ under which $\mathcal L\{\delta(t)\}=0$ (an unphysical result students rightly find puzzling), others leaving the treatment of $0^-$, $0$, and $0^+$ unspecified. Their extensive survey of the textbook literature (their references [32]–[58]) overlaps substantially with our own survey — Boyce and DiPrima, Edwards and Penney (and Calvis), Franklin, Powell and Emami-Naeini, Ogata, Dorf (and Bishop), and Zill all appear on both lists — and their independent finding of widespread inconsistency corroborates the motivation behind the classification carried out in this review.

Second, their worked automobile-suspension example (cited in Section 1 above) is a concrete, fully-derived instance of the impulse–initial-condition equivalence for a second-order system, obtained via their advocated $L^-$ transform with the derivative rule $L^-\{f'(t)\} = sF(s) - f(0^-)$ — a useful addition to the pattern of worked examples collected in Section 1.

Third, and most interesting for the present review, this article stands in direct methodological tension with Brigola and Singer (2009, §2.7). Brigola and Singer explicitly cite Lundberg, Miller, and Trumper's $L^-$ transform (their equation (3), integrating from $0^-$) and argue that it fails the convolution theorem and does not admit a unique primitive for a given transformed derivative — defects they attribute to allowing nonzero pre-initial values not intrinsic to the transform itself. Brigola and Singer instead advocate the classical causal Laplace transform $L$ acting on generalized functions with support strictly in $[0,\infty)$, in the sense of Zemanian and Schwartz, under which the convolution theorem holds and initial data are absorbed into explicit delta-derivative source terms (their equation (6), discussed in §2.7) rather than into the differentiation rule. Both frameworks reach correct, consistent results in the worked examples of their respective articles, but they disagree on which convention is the mathematically sound and pedagogically preferable foundation for the class of problems this review is concerned with. This live disagreement between two rigorous, peer-reviewed treatments — one aimed at engineering education, the other at generalized-function foundations — is itself evidence that the foundational treatment of initial conditions, generalized functions, and delta-derivative forcing has not fully converged in the literature, reinforcing rather than undermining the case for the unified, explicit, closed-form approach developed in the main article.

#### 2.9 Camporesi (2019): an elementary, general n-th order confirmation via factorization

A third, independently motivated line of work arrives at essentially the same linear-algebraic structure as the present review's category-5 target, this time by entirely elementary means. Camporesi (2019) develops the "impulsive response" $g = g_{\lambda_1\cdots\lambda_n}$ of the operator $L = (D-\lambda_1)\cdots(D-\lambda_n)$ purely by recursive convolution of first-order pieces (his eq. 4.8), explicitly avoiding distribution theory, the Laplace transform, and variation of parameters. His Theorem 4.1 shows that this $g$ reproduces the solution of $Ly=f(x)$ with continuous forcing $f$ and zero initial data via the convolution $y(x) = \int_0^x g(x-t)f(t)\,dt$, and his Theorem 4.2 extends this to arbitrary initial data $y^{(k)}(0)=b_k$, $k=0,\dots,n-1$, giving the general solution as

$$
y(x) = \int_0^x g(x-t)f(t)\,dt + c_0 g(x) + c_1 g'(x) + \cdots + c_{n-1}g^{(n-1)}(x),
$$

where the coefficients $c_k$ needed to express the initial data in the impulsive-response basis $\{g,g',\dots,g^{(n-1)}\}$ are given explicitly (his eq. 4.13) by the triangular combination $c_{n-1-j} = b_j + a_1 b_{j-1} + \cdots + a_j b_0$, $j=0,\dots,n-1$ — a Toeplitz-triangular map built from the same coefficients $a_1,\dots,a_{n-1}$ of the operator $L$ that populate the matrix $A$ of the main article's Section 3. This is, in effect, a third independent derivation — via factorization and convolution rather than Laplace-transform coefficient matching (as in the main article) or generalized-function calculus (as in Brigola and Singer, §2.7) — of the same underlying triangular linear correspondence between a shifted-initial-condition vector and a fixed basis tied to the operator's coefficients.

Tellingly, Camporesi is himself aware of the connection to delta-derivative forcing, even though his stated goal is to avoid it: in a remark on the distributional interpretation of his results (his Remark 5, for the second-order case $L=D^2+aD+b$), he writes that if $y$ solves $Ly=f(x)$ with $y(0)=y_0$, $y'(0)=y_0'$, then, in the convolution algebra $D_+'$ of distributions with support in $[0,\infty)$,
$$
L(\theta y) = \theta f + (y_0' + a y_0)\,\delta + y_0\,\delta',
$$
where $\theta$ is the Heaviside function — precisely the $n=2$ instance of Brigola and Singer's equation (6) (§2.7), obtained independently and by a different route. Camporesi cites L. Schwartz's *Théorie des Distributions* for this distributional viewpoint, the same foundational reference underlying Brigola and Singer's treatment — a directly verifiable point of convergence between two of the three closely related works discussed in this section, despite arising from unconnected research communities (elementary ODE pedagogy versus generalized-function foundations).

As with Brigola and Singer, however, Camporesi's treatment does not extend beyond a single point of nonsmoothness encoded through the initial-condition basis: continuous forcing $f(x)$ is handled in full generality, but an explicit right-hand side consisting of a finite sum of delta derivatives $\sum_j b_j\delta^{(j)}(t)$, let alone impulses at several distinct points, is — by the author's own account — "mentioned but not developed." The present review's category-5 gap therefore now has three closely related, mutually reinforcing but individually incomplete counterparts: a nonlinear regularization-based treatment (Nedeljkov & Oberguggenberger, §2.6), a general but inverse-direction linear correspondence via generalized functions (Brigola & Singer, §2.7), and an elementary, factorization-based confirmation of the same triangular structure for continuous forcing and a single set of initial data (Camporesi, this section) — none of which supplies the explicit, invertible, closed-form map from an arbitrary combination of delta derivatives to modified initial/jump data for a scalar $n$-th order LTI equation that this review and its companion article address.

#### 2.10 Ahuja and Arya (2019): a fourth, general algorithmic route, and direct confirmation of the citation cluster

A fourth closely related source is Ahuja and Arya (2019), a chemical-engineering paper that addresses, in essentially the same generality as the main article's Type 1 setup, the equation

$$
y^{(n)}(t) + a_1 y^{(n-1)}(t) + \cdots + a_n y(t) = b_0 x^{(m)}(t) + b_1 x^{(m-1)}(t) + \cdots + b_m x(t), \qquad n \ge m \ge 0,
$$

with $x(t)$ an input that may itself be discontinuous or impulsive — in their worked example, $x(t) = p(0^-) + M\delta(t)$, which, once differentiated up to order $m$, produces exactly a finite linear combination $\sum_j b_j\,\delta^{(m-j)}(t)$ of delta and its derivatives on the right-hand side, the same forcing this review's category 5 is concerned with. Their method — a "singular-nonsingular decomposition" — splits both $y$ and $x$ into a regular (piecewise-smooth) part and a singular (generalized-function) part, integrates the full equation successively $n$ times to obtain a triangular system relating the singular parts of $y,y',\dots,y^{(n)}$ to those of $x,x',\dots,x^{(m)}$ (their eqs. 11-12), solves this system backward in an "algebraic manner," and then reads off the post-initial jump values $y^{(k)}(0^+)-y^{(k)}(0^-)$ directly from the singular part via $\int_0^\infty y_s^{(k+1)}(t)\,dt = y^{(k)}(0^+)-y^{(k)}(0^-)$ (their eq. 14), since the integral of $\delta^{(j)}(t)$ vanishes for $j\ge1$ and equals one for $j=0$. This is, in effect, a fourth independent route — general recursive integration and back-substitution, rather than Laplace-coefficient matching (main article), generalized-function convolution (Brigola & Singer, §2.7), or operator factorization (Camporesi, §2.9) — to a procedure that, for a pure delta-derivative right-hand side, produces exactly the shifted post-initial conditions this review's category 5 asks for. Notably, the authors do not collapse their procedure into a single closed-form matrix expression analogous to the main article's $A^{-1}\mathbf b$: it remains a step-by-step recursive algorithm, verified case-by-case (their worked example, a second-order U-tube manometer system driven by a pressure impulse, is a further concrete illustration of the pattern in Section 1) rather than an explicit, general, symbolically inverted formula.

This paper is also directly useful for confirming, rather than merely inferring, the citation cluster this review has been tracing: Ahuja and Arya explicitly discuss and cite both Lundberg, Miller, and Trumper (2007, §2.8, their ref. [7]) and Brigola and Singer (2009, §2.7, their ref. [9]) as two of the competing approaches to consistent initialization of the Laplace transform, alongside Mäkilä (2006, their ref. [10]) — the same paper that motivated Brigola and Singer's own response. Ahuja and Arya side with neither the $L^-$ convention of Lundberg et al. nor the generalized-function reformulation of Brigola and Singer, proposing instead their own modified $L^+$ approach; this three-way (now four-way, counting the present review) engagement with the same underlying question — how to pass consistently from $0^-$ to $0^+$ in the presence of delta-derivative forcing — confirms that this is an active, unsettled methodological cluster in the literature rather than an isolated disagreement between two papers.

With this fourth counterpart, the present review's category-5 gap can now be stated with full awareness of four closely related, mutually reinforcing but individually incomplete treatments: a nonlinear, regularization-based treatment (Nedeljkov & Oberguggenberger, §2.6); a general, inverse-direction, generalized-function correspondence (Brigola & Singer, §2.7); an elementary, factorization-based confirmation for continuous forcing and a single set of initial data (Camporesi, §2.9); and a general recursive-integration algorithm covering the exact Type 1 setup, but without an explicit closed-form matrix formula (Ahuja & Arya, §2.10). A fifth, presented next, arrives at the same triangular structure by a route that avoids distributions altogether.

#### 2.11 Kavaja and Piazzi (2019): a fifth route via behavioral systems theory, and further confirmation of the citation cluster

A fifth closely related treatment, and arguably the cleanest closed-form analog to the main article's matrix $A$ found among the sources surveyed, is Kavaja and Piazzi (2019). Working entirely within behavioral systems theory (Polderman & Willems, 1997) rather than distribution theory, they consider a scalar LTI system of order $n$ and relative degree $r=n-m$ with transfer function $H(s)=b(s)/a(s)$, and define its *behavior* as the set of input-output pairs $(u,y)$ that are *weak solutions* of $\sum_i a_i D^i y = \sum_i b_i D^i u$ — signal pairs satisfying an equivalent integral equation everywhere, so that jump discontinuities in $u$ and $y$ are permitted without ever invoking a generalized derivative or the Dirac delta. Their central result, the input-output jump relations (Proposition 11, vector form in eq. (4), restated via Markov parameters $h_i$ in Corollary 14, eq. (10)), is a lower-triangular Toeplitz matrix, built from the system's own coefficients, that maps the vector of jump discontinuities of $u,u',\dots,u^{(m-1)}$ at *any* time $t$ directly to the vector of jump discontinuities of $y,y',\dots,y^{(n-1)}$ at that same time — structurally the same triangular linear map as the main article's matrix $A$ (and Brigola & Singer's eq. 6, §2.7), but derived without generalized functions and valid at any instant, not only $t=0$.

They then apply this machinery to exactly the problem this review is concerned with (their Problem 17): given a system evolution $(u_0,y_0)$ known for $t<0$, and a new input $u_1(t)$ applied for $t\ge0$, find the output $y_1(t)$, $t\ge0$. The solution decomposes as $y_1 = y_{1a}+y_{1e}$, a forced response (the usual zero-state convolution) plus a free response $y_{1e}$ built from the system's pole modes; Corollary 18 gives the free response's initial conditions at $0^+$ directly from the pre-initial data at $0^-$ via the same triangular matrix of Markov parameters (their eqs. 15-16) — a general, explicit, closed-form answer to "what are the modified initial conditions caused by a jump at $t=0$," for general order $n$ and relative degree $r$, obtained without distributions.

Kavaja and Piazzi's introduction also explicitly extends the citation cluster this review has been tracing: they cite Lundberg, Miller, and Trumper (2007, §2.8) for illustrating the $0^-/0^+$ pitfalls of the classic treatment, and remark that "the use of generalized derivatives as done in this context appears somewhat unsatisfactory or convolute," citing Grizzle (2004) — the same critical book review that Lundberg et al. themselves cite and rebut — Mäkilä (2006) — the paper that prompted Brigola and Singer's response, §2.7 — and Ahuja and Arya (2018, the conference precursor to the 2019 paper in §2.10). Their behavioral approach is offered as a further, sixth-counted-from-Lundberg alternative to the ones already surveyed. As with the other closely related sources, however, the input-output jump relations are stated for jump discontinuities of otherwise continuous (or piecewise-$C^\infty$) signals; the case of an explicit forcing term consisting of a finite sum of delta derivatives $\sum_j b_j\delta^{(j)}(t)$ — this review's category 5 — is not the language in which their result is expressed, even though the underlying triangular structure coincides. The category-5 gap therefore now sits alongside five mutually reinforcing but individually distinct treatments of essentially the same triangular linear structure, obtained by five different routes: nonlinear regularization (§2.6), generalized-function convolution (§2.7), operator factorization (§2.9), recursive integration (§2.10), and behavioral weak solutions (this section) — none of which casts the result as an explicit, invertible, closed-form map from an arbitrary combination of delta derivatives to modified initial/jump data for a scalar $n$-th order LTI equation, in the specific terms this review and its companion article use.

#### 2.12 Tvrdý (1994): a sixth route via the Kurzweil-Stieltjes generalized differential equation, for a variable-coefficient second-order equation with delta forcing at multiple points

A sixth, methodologically quite different route to a closely related result is Tvrdý (1994), who works within the theory of generalized (Kurzweil-Stieltjes) differential equations in the space of regulated functions, using the Perron-Stieltjes integral rather than the Laplace transform or Schwartz distribution theory. Generalizing existence-uniqueness results of Atkinson, Ligeza, Pfaff, and Mingarelli, Tvrdý treats the linear second-order equation $(pu')'+q'u=f''$ with possibly distributional coefficients $p,q$ and solutions that are merely regulated (one-sided limits everywhere, jumps permitted).

Section 4 of the paper works out an explicit example directly relevant to this review's subject: the boundary value problem $u''+qu=\sum_{j=1}^N g_j(t)\delta_{\tau_j}$, $u(0)=u_0$, $u(T)=u_T$ — a (possibly variable-coefficient) scalar second-order LTI-type equation forced by a finite sum of Dirac deltas located at several interior points $\tau_1,\dots,\tau_N\in(0,T)$, each with its own (possibly time-varying) weight $g_j(t)$. Using a fundamental system of solutions $\{u_1,u_2,v_1,v_2\}$ of the homogeneous equation, Tvrdý derives a closed-form solution formula (his eqs. 4.5-4.7) together with explicit jump relations at each impulse point: $\Delta u(\tau_k)=0$ (continuity of $u$ itself) and $\Delta u'(\tau_k)=g_k(\tau_k)$ (the jump in the derivative equals the delta's weight) — the same underlying triangular impulse-to-jump principle documented throughout this review, but derived through measure-theoretic generalized differential equations rather than the Laplace-transform coefficient matching used in the present article, and, unlike the main article's formula, allowing variable coefficients and multiple impulse locations rather than a single impulse at $t=0$. As with the other closely related sources surveyed, however, the forcing here is a sum of plain Dirac deltas, not their derivatives, and the order is fixed at two rather than general $n$; the category-5 gap for a sum of delta *derivatives* at general order therefore remains open.

Tvrdý's bibliography also independently confirms two leads relevant to this review's broader picture of the field: Zavalishchin and Sesekin's *Impulse Processes: Models and Applications* (Nauka, Moscow, 1991) — the same monograph flagged via Perestyuk et al. (2011, §1) as a possible direct treatment of generalized-function-based impulsive systems — and R. Pfaff's "Gewöhnliche lineare Differentialgleichungen $n$-ter Ordnung mit Distributionskoeffizienten" (*Proc. Roy. Soc. Edinburgh* 85A, 1980), whose title ("Ordinary linear $n$-th order differential equations with distribution coefficients") suggests it may address general-order equations with distributional data directly, making it a priority candidate for future review.

#### 2.13 Appell, Hien, Petrova, and Pryadko (2021): a seventh route via Stieltjes variation-of-constants, from the Russian/Ukrainian dynamic-impulse-systems tradition

A seventh, independently arising route is found in Section 3.5 ("Linear systems with non-smooth action") of Appell, Hien, Petrova, and Pryadko (2021), a monograph otherwise devoted to hysteresis operators (relays, stops, plays) and their "nonlinear differentials" framework. There the authors consider a linear, generally time-varying, vector system $\Delta x(t)=A(t)x(t)+\Delta B(t)+o(dt+J_B(t))$, where $B$ is a left-continuous function of bounded variation — so that $dB$ may consist of countably many Dirac-delta-weighted jumps, each with a possibly time-varying weight. Their Theorem 3.5.2 gives an explicit, general closed-form solution via a Riemann-Stieltjes variation-of-constants formula,
$$x(t)=\Phi(t)\Big[x_0+\int_{t_0}^{t}\Phi^{-1}(s)\,dB(s)\Big],$$
where $\Phi(t)$ is the fundamental matrix of the homogeneous system $\dot x=A(t)x$ — a rigorous existence-and-uniqueness result (via the Martynenko lemma) together with an explicit worked example (§3.5.3). Since any scalar $n$-th order LTI equation can be cast in companion form, this formula covers, as a special case, a scalar constant-coefficient equation driven by an arbitrary finite (or countable) sum of plain Dirac deltas at arbitrary times — broader than the main article's formula in allowing time-varying coefficients and multiple, arbitrarily located impulses, but narrower in that it is restricted to jumps of $B$ itself (plain deltas) rather than the *derivatives* of the delta function; the category-5 gap for a sum of delta derivatives at general order therefore again remains open.

Bibliographically, this section belongs to a different lineage than the Laplace-transform-based cluster documented in §§2.6-2.12: its citations (Miller and Rubinovich, 2003, §2.14 below; Samojlenko and Perestyuk, *Differential Equations with Impulse Actions*, Kiev, 1987; and Zavalishchin and Sesekin) trace to the Soviet/Russian and Ukrainian "dynamic impulse systems" tradition rather than the Western control-theory or distribution-theory literature. Notably, this source supplies a precise bibliographic identification for a lead flagged earlier in this review (§2.12): Zavalishchin, S. T., and Sesekin, A. N. (1997), *Dynamic Impulse Systems: Theory and Applications*, Kluwer, Dordrecht — an English-language edition of the 1991 Russian monograph, now confirmed as a concrete, locatable reference for future investigation of the category-4/5 gap from within this tradition.

#### 2.14 Miller and Rubinovich (2003): an eighth, earlier route via measure-differential-equation calculus

An eighth route, chronologically earlier than both Tvrdý (1994, §2.12, in the specific delta/BVP sense used there) and Appell et al. (2021, §2.13), and likely one of that section's own sources, is found in the mathematical appendix (Chapter 8, "Differential equations with measures") of Miller and Rubinovich (2003), a monograph otherwise devoted to optimal impulsive control of nonlinear discrete-continuous (hybrid) systems and containing no mention of the Dirac delta, its derivatives, or the Laplace transform in its main text (Chapters 1-7). Working entirely in the language of Lebesgue-Stieltjes measures rather than distributions, §8.2 defines a linear differential equation with a measure $X(t)=X(t_0^-)+\int_{t_0}^t A(s)X(s^-)\,d\mu(s)+b(t)$ (their eq. 8.26), where $b(t)$ is a right-continuous function of bounded variation whose jumps play exactly the role of Dirac-delta forcing terms. For the scalar case, Theorem 8.16/Corollary 8.2 gives an explicit closed-form solution as a product integral, $\varphi(t)=X_0\exp\big(\int_{t_0}^t A\,d\mu^c(s)\big)\prod_{\tau\in D_\mu\cap[t_0,t]}(1+A(\tau)\Delta\mu(\tau))$ (their eqs. 8.35-8.36); for the general $m$-dimensional (hence, via companion form, general scalar $n$-th order) case, Theorem 8.18 gives the variation-of-constants formula $\varphi(t)=\mathcal E(t,t_0)X_0+\int_{[t_0,t]}\mathcal E(t,s^+)\,db(s)$ (their eq. 8.41-8.42's fundamental solution $\mathcal E$, established via a contraction-mapping existence-uniqueness argument rather than an explicit closed form in the multi-dimensional case).

This is structurally the same result as Appell, Hien, Petrova, and Pryadko's (2021, §2.13) $\Delta x(t)=A(t)x(t)+\Delta B(t)+o(dt+J_B(t))$ and its variation-of-constants solution — likely not a coincidence, since Appell et al. cite Miller (among others) as part of the same tradition (§2.13, discussed above) — and shares the same limitation: the forcing is a jump in $b(t)$ itself (i.e., a plain Dirac delta, possibly at several points, with a possibly time-varying matrix $A(t)$), not a derivative of the delta function, so it neither addresses nor closes the category-5 gap for a sum of delta *derivatives*. Its main historical interest for this review is as a candidate common source for the measure/Stieltjes route later used by Tvrdý and by Appell et al., and its acknowledgements explicitly credit discussions with Zavalishchin and Sesekin (Ekaterinburg) — independently confirming, from a primary source, the citation cluster this review has been tracing through the Soviet/Russian "dynamic impulse systems" tradition.

#### 2.15 Filippov (1988): a ninth, verified-equivalent route tracing to Aizerman and Gantmakher (1956)

A ninth route, and the earliest verified in this review, is found in Section 2 ("Equations with Distributions Involved as Summands") of Filippov's classic monograph *Differential Equations with Discontinuous Right-Hand Sides*. For the general scalar $n$-th order linear equation $y^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_0y=b_mz^{(m)}+\cdots+b_0z$, $m\le n$, where $z(t)$ is a known function or distribution (Filippov explicitly allows $z$ to be a Dirac delta itself, motivating this via impulsive forcing $v\delta(t-t_1)$, his eqs. 6-8), he gives two methods for finding the response vanishing for $t<0$: a successive-integration/regularization method (integrate $z$ enough times to make the right-hand side Lebesgue-integrable, solve the resulting ordinary equation, then differentiate the result back down, his eq. 13), and an explicit closed recursive formula for the jumps of the solution and its derivatives at a point $\tau$ in terms of the jumps of $z,z',\dots,z^{(m)}$ there (his eqs. 17-18): $[y^{(k)}]=c_0[z^{(k)}]+c_1[z^{(k-1)}]+\cdots+c_k[z]$, with coefficients $c_0=b_n,\ c_i=b_{n-i}-c_0a_{n-i}-c_1a_{n-i+1}-\cdots-c_{i-1}a_{n-1}$ determined recursively from the equation's own coefficients — a genuinely general, explicit, and (by its recursive, triangular construction) invertible formula. Filippov attributes this jump formula to Aizerman and Gantmakher (1956), pushing the traceable origin of this line of results back to the mid-1950s, decades before every other source surveyed in this review.

To check whether this closes the category-5 gap, this review verified Filippov's method against the worked example $\ddot y+\omega^2y=\delta'(t)$, $y\equiv0$ for $t<0$ (i.e., $n=2$, $m=1$, $b_1=1$, $b_0=0$, $a_1=0$, $a_0=\omega^2$): regularizing $z=\delta(t)$ by two integrations, solving $\ddot x+\omega^2x=H(t)$ with $x(0)=\dot x(0)=0$, and differentiating the result twice recovers $y(t)=\cos(\omega t)$ for $t\ge0$ — matching exactly both the standard Laplace-transform computation ($Y(s)=s/(s^2+\omega^2)$) and the jump values $y(0^+)=b_1=1$, $\dot y(0^+)=b_0-a_1b_1=0$ predicted by formula (18). Filippov's method is therefore verified as mathematically equivalent, for this case, to the triangular matrix of the main article and of Brigola & Singer (§2.7).

The gap remains open, however, for the same reason as with Ahuja and Arya (§2.10): Filippov's formula (17)-(18) is parametrized by the jumps $[z],[z'],\dots,[z^{(m)}]$ of a *single* underlying function $z$ appearing in the equation's own right-hand side, not directly by an arbitrary, independently-assigned set of coefficients $(\beta_0,\dots,\beta_m)$ on a sum $\sum_j\beta_j\delta^{(j)}(t)$ of delta and its derivatives. Translating between the two parametrizations (as done above for the worked example) is possible via linearity, but Filippov never carries this out explicitly, nor collapses it into a single closed matrix formula acting on an arbitrary delta-derivative combination in the form this review and its companion article use. As with several of the counterparts already discussed, this is a verified mathematical equivalent rather than an explicit statement of the category-5 result — and, via Aizerman and Gantmakher (1956), by far the earliest one found in this survey.

#### 2.16 Popov (1962): a full, general, explicit closed-form answer to the single-point category-5 problem

A tenth source, and the one that most directly answers the category-5 question as posed in this review, is found in Section 6 (pp. 44-48) of Popov's classical textbook *The Dynamics of Automatic Control Systems* (English translation, Pergamon Press, 1962, of an earlier Russian original). For the general scalar $n$-th order equation $L(p)x=S(p)f(t)$, written in Heaviside operational notation with $L(p)=a_0p^n+a_1p^{n-1}+\cdots+a_n$ and an arbitrary polynomial $S(p)=b_0p^m+b_1p^{m-1}+\cdots+b_m$, $m<n$, Popov first derives the initial-condition-transformation formulas for a unit step $f(t)=1(t)$ (his eq. 6.23), then observes that "the impulse is the derivative of the step with regard to time" and substitutes $S(p)\,1'(t)\to S(p)p\,1(t)$ to obtain, for a unit impulse $f(t)=\delta(t)$ — i.e., a right-hand side $S(p)\delta(t)=b_0\delta^{(m)}(t)+b_1\delta^{(m-1)}(t)+\cdots+b_m\delta(t)$, an *arbitrary* finite polynomial combination of the delta function and its derivatives up to order $m$ — his eq. 6.26:
$$x_{+0}=x_{-0},\ \dot x_{+0}=\dot x_{-0},\dots,x_{+0}^{(n-m-2)}=x_{-0}^{(n-m-2)},$$
$$x_{+0}^{(n-m-1)}-x_{-0}^{(n-m-1)}=\frac{b_0}{a_0},\qquad x_{+0}^{(n-m)}-x_{-0}^{(n-m)}=\frac{b_1}{a_0}-\frac{a_1}{a_0}\Big(x_{+0}^{(n-m-1)}-x_{-0}^{(n-m-1)}\Big),$$
and so on recursively down to $x_{+0}^{(n-1)}-x_{-0}^{(n-1)}=\tfrac{b_m}{a_0}-\tfrac{a_m}{a_0}(\cdots)-\cdots-\tfrac{a_1}{a_0}(\cdots)$.

This review verified formula (6.26) against the same worked example used to check Filippov (§2.15), $\ddot y+\omega^2y=\delta'(t)$, $y\equiv0$ for $t<0$ ($n=2$, $m=1$, $a_0=1$, $a_1=0$, $b_0=1$, $b_1=0$): the formula gives $x_{+0}-x_{-0}=b_0/a_0=1$ and $\dot x_{+0}-\dot x_{-0}=b_1/a_0-(a_1/a_0)(1)=0$ — exactly $y(0^+)=1$, $\dot y(0^+)=0$, matching the Laplace-transform computation and Filippov's method.

Unlike Filippov (§2.15) and Ahuja and Arya (§2.10), Popov's formula is parametrized directly by the coefficients $b_0,\dots,b_m$ of an *arbitrary, independently assigned* polynomial $S(p)$ — precisely the parametrization category 5 asks for — rather than by the jumps of a single auxiliary function. For a single impulse point (the main article's basic setup), formula (6.26) therefore appears to be a genuine, general-$n$, explicit, invertible closed-form solution to the category-5 problem, some three to four decades before every other closely related source surveyed in this review (Nedeljkov & Oberguggenberger, 2012; Brigola & Singer, 2009; Camporesi, 2019; Ahuja & Arya, 2019; Kavaja & Piazzi, 2019; Tvrdý, 1994; Appell et al., 2021; Miller & Rubinovich, 2003; Filippov, 1988). It is derived entirely within classical Heaviside operational calculus, without reference to Schwartz distribution theory, and the book shows no citation link to, and appears wholly unconnected with, the generalized-function and behavioral-systems literatures discussed throughout §§2.6-2.15 — nor is it, in turn, cited by any of them. Its one clear limitation relative to the main article and its companion is scope: Popov addresses a single impulse at $t=0$ only, not the main article's Type 0c case of multiple impulses at several distinct points within one unified formula.

### 3 Conclusion

Across the sources surveyed, a consistent pattern emerges: the solution of an LTI ODE driven by a Dirac delta forcing term coincides with the solution of the corresponding homogeneous equation under a shifted initial condition (Section 1). The literature treats this equivalence unevenly, however. As the classification in Section 2 shows, most sources either use the equivalence implicitly, without stating it (category 1), or mention it qualitatively without an explicit formula (category 2); a smaller subset derive an explicit formula for a specific order of equation (category 3); and fewer still address the general case of an n-th order equation forced by the delta function alone (category 4). For the most general case considered here — a scalar n-th order LTI ODE forced by an arbitrary finite sum of derivatives of the Dirac delta, translated directly into an equivalent modified initial/jump condition vector (category 5) — this review initially found no source providing such a formula among the modern (post-1970s) distribution-theory, behavioral-systems, and vibration/control-engineering textbook literature that dominates its bibliography. Extending the search to classical control-engineering sources overturned this: Popov (1962; §2.16), in a widely used Soviet-era textbook derived through operational calculus rather than distribution theory, gives precisely such a formula for a single impulse point — general in the equation order $n$ and in the polynomial combination of delta derivatives, explicit, and, by its triangular recursive construction, invertible — verified in this review against a worked example and matching the main article's own single-point results exactly.

This finding substantially narrows, without eliminating, the gap this review set out to identify. What remains open is not the existence of any general closed-form result, but its consolidation: Popov's formula, like the closely related results independently obtained via generalized-function theory (Brigola & Singer, 2009, §2.7; Nedeljkov & Oberguggenberger, 2012, §2.6), measure-theoretic and Kurzweil-Stieltjes calculus (Filippov, 1988, tracing to Aizerman & Gantmakher, 1956, §2.15; Tvrdý, 1994, §2.12; Miller & Rubinovich, 2003, §2.14; Appell et al., 2021, §2.13), and behavioral systems theory (Kavaja & Piazzi, 2019, §2.11; Ahuja & Arya, 2019, §2.10), was arrived at independently by unconnected research communities spanning at least three decades and several countries' worth of engineering and mathematical traditions, with essentially no cross-citation between the classical control-engineering result and the modern distribution-theory/behavioral-systems debate that this review otherwise documents in detail (§§2.6-2.11). Nor does Popov's formula, any more than the others, extend to multiple impulses at distinct points within a single unified computational framework — the case the main article's Type 0c addresses and its companion article treats in full generality.

This reframes, rather than closes, the two open needs this review identifies: not a treatment of derivatives of the delta function as forcing terms — which, per Popov (1962) and the other counterparts documented in §§2.6-2.15, has in fact existed since at least the 1950s — but its consolidation into a single, cross-referenced, widely known treatment, and its extension to multiple impulses at distinct points within one unified computational framework, rather than the disconnected, single-point, or equation-by-equation formulas found across categories 3-5. That this foundation is still unsettled even at the level of which Laplace-transform convention to use is illustrated by the live methodological disagreement between Lundberg, Miller, and Trumper (2007) and Brigola and Singer (2009) discussed in §2.8 — a disagreement that itself shows no awareness of Popov's much earlier operational-calculus solution to the same underlying problem.

---

**Acknowledgements** We are grateful to Dr. Ricardo Felipe Torres Naranjo for carefully reading the manuscript and making a number of valuable suggestions for improvement.


### REFERENCES

<div style="font-size: 0.85em; line-height: 1.5; column-count: 2; column-gap: 2em;">

Adkins, W. A., & Davidson, M. G. (2012). *Ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4614-3618-8

Ahuja, S., & Arya, R. K. (2019). Consistent initialization of the Laplace transform. *arXiv preprint* arXiv:1909.07813v1.
Akhmet, M. (2010). *Principles of discontinuous dynamical systems*. Springer. https://doi.org/10.1007/978-1-4419-6581-3

Alam, J., Hu, G., Babu, H. M. H., & Xu, H. (2023). *Control engineering: Theory and applications*. CRC Press. https://doi.org/10.1201/9781003293859

Anderson, B., & Rufer, S. (2018, August 13). *Control theory: A brief introduction*. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4419-1027-1

Antsaklis, Panos J.; Michel, Anthony N. *A Linear Systems Primer*. Birkhäuser, 2007. ISBN: 9780817644604

Arfken, G. B., Weber, H. J., & Harris, F. E. (2011). Mathematical methods for physicists: A comprehensive guide (7th ed.). Academic Press / Elsevier. Print ISBN: 978-0-12-384654-9

Appell, J., Hien, N. T., Petrova, L., & Pryadko, I. (2021). *Systems with non-smooth inputs: Mathematical models of hysteresis phenomena, biological systems, and electric circuits*. De Gruyter. https://doi.org/10.1515/9783110709865

Asadi, F., Bolanos, R. E., & Rodríguez, J. (2019). *Feedback control systems: The MATLAB®/Simulink® approach* (Synthesis Lectures on Control and Mechatronics, Lecture #5). Morgan & Claypool Publishers. https://doi.org/10.2200/S00909ED1V01Y201903CRM005

Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781108615839

Baruh, H. (2015). *Applied dynamics*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-0734-7) https://doi.org/10.1201/b18272

Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press. (ISBN: 0340645806, 9780340645802, 0470235861, 9780470235867)

Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-5265-7) https://doi.org/10.1201/b22347

Benchohra, Mouffak; Henderson, Johnny; Ntouyas, Sotiris K. *Impulsive Differential Equations and Inclusions*. Hindawi Publishing, 2006.

Beneš, K. (1978). On modelling dynamic systems excited by the Dirac function. *Sborník prací Přírodovědecké fakulty University Palackého v Olomouci. Matematika, 17*(1), 123–129. http://dml.cz/dmlcz/120062

Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

Boyce, W. E., & DiPrima, R. C. (2017). *Elementary differential equations and boundary value problems* (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-37792-4)

Brigola, R., & Singer, P. (2009). On initial conditions, generalized functions and the Laplace transform. *Electrical Engineering*, 91(1), 9–13. https://doi.org/10.1007/s00202-009-0110-5

Brogliato, Bernard. *Nonsmooth Mechanics: Models, Dynamics and Control* (3rd ed.). Springer, 2015.

Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. ISBN: 978-0-691-12474-2 (hardcover)

Camporesi, R. (2019). *An introduction to linear ordinary differential equations with constant coefficients using the impulsive response method and factorization*. Lecture notes, Politecnico di Torino.

Campos, L. M. B. C. (2020). *Linear differential equations and oscillators* (Vol. 4). CRC Press, Taylor & Francis Group. (ISBN: 978-0-367-13718-2) https://doi.org/10.1201/9780429028984

Chasnov, J. R. (2009–2016). *Introduction to differential equations: Lecture notes for MATH 2351/2352*. The Hong Kong University of Science and Technology.

Chopra, A. K. (2020). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed., SI units). Pearson Education Limited. (ISBN: 978-1-292-24918-6)

Cohen, A. M. (2007). *Numerical methods for Laplace transform inversion*. Springer Science+Business Media. (ISBN: 9780387282619, 0387282610) https://doi.org/10.1007/978-0-387-68855-8

Cooper, David. *Distribution Theory*. 2000.

Dorf, R. C., & Bishop, R. H. (2008). *Modern control systems: Solution manual* (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

Duffy, D. G. (2015). *Green's functions with applications* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-5103-6) https://doi.org/10.1201/b17973

Edwards, C. H., Penney, D. E., & Calvis, D. (2016). *Differential equations and boundary value problems: Computing and modeling* (5th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-10877-3)

Esfandiari, R. S., & Lu, B. (2014). *Modeling and analysis of dynamic systems* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3) https://doi.org/10.1201/b16443

Etkin, B. (2005). *Dynamics of atmospheric flight*. Dover Publications, Inc. (ISBN: 0-486-44522-4) (Original work published 1972)

Fairman, Frederick W. *Linear Control Theory: The State Space Approach*. John Wiley & Sons, 1998. ISBN: 0-471-97489-7

Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media, LLC. (ISBN: 978-0-387-79579-9, 9780387795805) https://doi.org/10.1007/978-0-387-79580-5

Goode, S. W., & Annin, S. A. (2015). *Differential equations and linear algebra* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-321-96467-0)

Gupta, A., & Verma, Y. P. (2020). *Automatic control engineering*. I.K. International Pvt. Ltd. (ISBN: 978-93-89583-74-8)

Haddad, Wassim M.; Chellaboina, Vijaysekhar; Hui, Qing. *Nonnegative and Compartmental Dynamical Systems*. Oxford University Press, 2009. ISBN: 978-0-691-14411-5

Hallauer, William L. *Linear Time-Invariant Dynamic Systems*. John Wiley & Sons, 2016.

Holmes, M. H. (2023). Introduction to differential equations (3rd ed.). XanEdu. ISBN: 978-1-71147-191-4

Howell, K. B. (2020). *Ordinary differential equations: An introduction to the fundamentals* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-138-60583-1) https://doi.org/10.1201/9780429347429

Inman, Daniel J. *Engineering Vibration* (4th ed.). Pearson Education, Inc., 2014. ISBN: 978-0-13-287169-3

Iyengar, R. N. (2019). *Elements of mechanical vibration*. I.K. International Pvt. Ltd. (ISBN: 978-93-89633-34-4)

Jack, H. (2015). *Dynamic system modeling and control*. Hugh Jack. (ISBN: 978-1-5089-9525-8)

James, G., Dyke, P., Burley, D., Clements, D., Craven, M., Reis, T., Searl, J., Stander, J., Steele, N., & Wright, J. (2018). *Advanced modern engineering mathematics* (5th ed.). Pearson Education Limited. (ISBN: 978-1-292-17434-1)

Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG. (ISBN: 978-3-031-43485-3) https://doi.org/10.1007/978-3-031-43486-0

Jeffrey, A. (2002). Advanced engineering mathematics. Harcourt/Academic Press. ISBN-10: 0-12-382592-X

Kabe, A. M., & Sako, B. H. (2020). *Structural dynamics: Fundamentals and advanced applications* (Vol. 1). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-821614-9) https://doi.org/10.1016/C2019-0-00137-8

Kausel, Eduardo. *Advanced Structural Dynamics*. Cambridge University Press, 2017. ISBN: 978-1-107-17151-0. https://doi.org/10.1017/9781316761403

Kavaja, J., & Piazzi, A. (2019). Input-output jumps of scalar linear systems. *IFAC-PapersOnLine*, 52(17), 13-18. https://doi.org/10.1016/j.ifacol.2019.11.019

Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

Lakshmikantham, V., Bainov, D. D., & Simeonov, P. S. (1989). *Theory of impulsive differential equations*. World Scientific. (ISBN: 9971-50-970-9)

Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

Lundberg, K. H., Miller, H. R., & Trumper, D. L. (2007). Initial conditions, generalized functions, and the Laplace transform: Troubles at the origin. *IEEE Control Systems Magazine*, 27(1), 22–35. https://doi.org/10.1109/MCS.2007.284511

McOwen, R. (2012). Worldwide differential equations with linear algebra (1st ed.). Worldwide Center of Mathematics, LLC.  ISBN-10: 0-9842071-2-0

Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

Miller, B. M., & Rubinovich, E. Ya. (2003). *Impulsive Control in Continuous and Discrete-Continuous Systems*. Kluwer Academic/Plenum Publishers. https://doi.org/10.1007/978-1-4615-0095-7

Nagy, G. (n.d.). *Ordinary differential equations*. Mathematics Department, Michigan State University.

Nedeljkov, M., & Oberguggenberger, M. (2012). Ordinary differential equations with delta function terms. *Publications de l'Institut Mathématique*, 91(105), 125–135. https://doi.org/10.2298/PIM1205125N

Nielsen, S. R. K. (2004). *Vibration theory, Vol. 1: Linear vibration theory* (3rd ed.). Department of Civil Engineering, Aalborg University. (U/ Vol. U2004-1)

O'Neil, Peter V. Advanced Engineering Mathematics, SI. SI ed., 8th ed., Cengage Learning, 2018. ISBN-13: 978-1-337-27452-4

Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-615673-4)

Orlov, Y. (2010). *Discontinuous systems: Lyapunov analysis and robust synthesis under uncertainty conditions*. Springer. https://doi.org/10.1007/978-1-84882-800-9

Palm, W. J., III. (2010). *System dynamics* (2nd ed.). McGraw-Hill. (ISBN: 978-0-07-352927-1)

Peterson, G. L., & Sochacki, J. S. (2014). *Linear algebra & differential equations* (Pearson New International ed.). Pearson Education Limited. (ISBN: 978-1-269-37450-7)
Perestyuk, N. A., Plotnikov, V. A., Samoilenko, A. M., & Skripnik, N. V. (2011). *Differential equations with impulse effects: Multivalued right-hand sides with discontinuities*. De Gruyter. https://doi.org/10.1515/9783110218176

Polderman, J. W., & Willems, J. C. (1997). *Introduction to the mathematical theory of systems and control*. Springer. (ISBN: 978-0-387-98266-3)

Polking, J., Boggess, A., & Arnold, D. (2006). *Differential equations with boundary value problems* (2nd ed.). Pearson Prentice Hall. (ISBN: 0-13-186236-7)

Popov, E. P. (1962). The dynamics of automatic control systems (A. D. Booth, Trans.). Pergamon Press. (Note: the translator/editor credit could not be independently confirmed from the title page; A. D. Booth is the name associated with this edition in available library and commercial listings, but his exact role is not fully verified.)

Ram, B. (2009). *Engineering mathematics*. Pearson Education. (ISBN: 978-81-317-2691-4)

Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-212819-3)

Ricardo, H. J. (2020). A modern introduction to differential equations (3rd ed.). Academic Press. https://doi.org/10.1016/C2018-0-02231-8 Print ISBN-13: 978-0-12-823417-4

Ruderman, M. (2017). Impulse-based hybrid motion control. *arXiv:1704.04372 [cs.SY]*. https://arxiv.org/abs/1704.04372

Schiff, Joel L. (1999). *The Laplace transform: Theory and applications*. Springer-Verlag New York, Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

Shabana, A. A. (1997). Vibration of discrete and continuous systems (2nd ed.). Springer-Verlag. https://doi.org/10.1007/978-1-4612-4036-5 Print ISBN-13: 978-1-4612-8474-1

Samoilenko, A. M., & Perestyuk, N. A. (1995). *Impulsive differential equations*. World Scientific. (ISBN: 981-02-2416-8)

Sinha, N.K., & Ananthkrishnan, N. (2022). *Elementary flight dynamics with an introduction to bifurcation and continuation methods* (2nd ed.). CRC Press. https://doi.org/10.1201/9781003096801

Tewari, A. (2011). *Automatic control of atmospheric and space flight vehicles: Design and analysis with MATLAB and Simulink*. Birkhauser. https://doi.org/10.1007/978-0-8176-4864-6

Thorby, D. (2008). *Structural dynamics and vibration in practice: An engineering handbook*. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

Trench, W. F. (2024). *Elementary differential equations with boundary values problems*. LibreTexts. Retrieved December 19, 2024, from https://LibreTexts.org
Tvrdý, M. (1994). Linear distributional differential equations of the second order. *Mathematica Bohemica, 119*(4), 415-436. http://dml.cz/dmlcz/126120

Tse, F. S., Morse, I. E., & Hinkle, R. T. (2018). *Mechanical vibrations: Theory and applications* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-879-6458-7)

Weber, H. J., & Arfken, G. B. (2003). *Essential mathematical methods for physicists*. Academic Press. (ISBN: 978-0-12-059877-9) https://doi.org/10.1016/B978-0-12-059877-9.X5000-7

Zill, D. G. (2023). A first course in differential equations with modeling applications (12th ed.). Cengage Learning. Hardcover ISBN: 978-0-357-76019-2
</div>
