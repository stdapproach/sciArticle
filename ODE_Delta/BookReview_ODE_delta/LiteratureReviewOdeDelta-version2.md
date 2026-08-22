## Literature Review: Solution of Linear ODEs with Delta Function as Load

**Denis Pleshkov**
<std.approach@gmail.com>
August 2026

### Abstract

This literature review examines how linear time-invariant (LTI) ordinary differential equations (ODEs) with impulsive forcing (represented by the Dirac delta function and its derivatives) are treated across differential equations, vibration theory, and control theory. Motivated by the practical need to find proper solution approaches and closed-form formulas for such systems, we surveyed 100+ sources. Critical gaps in the literature are identified — limited treatment of derivatives of delta, and lack of unified computational frameworks.

### Keywords

Literature review, delta function, differential equation, ODE, impulse response

### Introduction

The dynamics of evolving processes are often subject to abrupt changes, such as: impact of a hammer on a beam, a bat striking a ball, a bolt of lightning striking a tower.

Such short-term perturbations are frequently treated as instantaneous events, often modeled as "impulses". As Cohen (p. 13) notes, "The impulse function is useful when we are trying to model physical situations, such as the case of two billiard balls impinging, where we have a large force acting for a short time which produces a finite change of momentum". Logan (p.166) "Many physical and biological processes have source terms that act at a single instant of time. For example, we can idealize an injection of medicine (a "shot") into the blood stream as occurring at a single instant; a mechanical system, for example, a damped spring–mass system in a shock absorber on a car can be given an impulsive force by hitting a bump in the road; the switch in an electrical circuit can be closed only for an instant, which leads to an impulsive, applied voltage". According to Rao (p. 381) "The simplest form is the impulsive force a force that has a large magnitude F and acts for a very short time". The system's response to such a force is termed the impulse response function (IRF). Mathematically, an impulse can be represented within an initial value problem (IVP) by incorporating the Dirac delta function as the external forcing term. An IVP consists of an ODE together with the system's state at some initial time; its solution is the unique function satisfying both. The impulse response of a system is defined as its output in response to an input $\delta(t)$, assuming the system is initially at rest.  

We are searching the literature for solutions to LTI ODEs with a discontinuous right-hand side, including the delta function and its derivatives. The Dirac delta function is a well-known generalized function (distribution) used to model impulsive phenomena. Its properties are discussed extensively in the literature, including Arfken (pp.76-79), Bottega (p. 233), Chasnov (p. 58), Nagy (p. 196-201), Weber (p. 86-90), Zill (p. 328-330).

While seeking a general method to solve such systems, we found that existing literature primarily offers solutions for specific first- and second-order ODEs and almost no books present the common (closed form) solution.

Beyond the sources analyzed in detail below, a broader survey of the Control Theory literature identified more than fifty additional textbooks that discuss the Impulse Response Function (IRF) — the solution of an LTI ODE with zero Initial Condition (IC) and an impulse delta function as load — without engaging the equivalence question directly. This broader bibliography is provided in the Supplementary Bibliography following the References, for readers seeking a starting point for further study of Control Theory.

### 1 Equivalence through initial condition's modification

Several textbooks provide analytical solutions for first/second order LTI ODEs with a Dirac delta forcing function. Examples include Nagy (pp. 203-209: "The Impulse Response Function"), Ogata (p. 163: "Unit-Impulse Response of First-Order Systems"; p.178: "Impulse Response of Second-Order Systems"), Rao (p. 382: "4.5.1 Response to an Impulse"), and Zill (p. 330: "Two Initial-Value Problems").

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

Weber (p. 733: "Impulsive Force") notes the analogous result

$
\begin{cases}
m x'' = P \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' = 0, \\
x(0) = 0, \\
x'(0) = P/m
\end{cases}
$

Balachandran (p. 301: "Similarity to Response to Initial Velocity"), Bottega (pp. 235–236: "problem of interest becomes equivalent to the problem of free vibrations with the initial conditions"), Genta (p. 179-180: "The position x0 after the impulse is equal to that before the impulse,
while the velocity v0 is equal to the one before the impulse plus an increment"), Meirovitch (pp. 160–161: "we conclude that the effect of a unit impulse at t = 0 is to produce an equivalent initial velocity"), Schiff (p. 83: "indicating the instantaneous jump in velocity at t=0, from a rest state to the value v0"), all remarked that

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
The LTI IVP with discontinuous right side can also be viewed as a special case of an impulsive differential equation (see Benchohra, Henderson, and Ntouyas).

The above examples suggest a general pattern (though a formal proof appears to be missing in the literature): an IVP forced by a delta function may be equivalent to a homogeneous IVP with a shifted IC.

### 2 Detailed literature classification

Here is the list of books we split into those 5 groups:

1. **Solution without mentioning the equivalence (i.e. unit impulse is equal to change IC)**
   Alam (p. 218 1st order, pp. 270-274 2nd order), Asadi (pp. 62-73), Benaroya (p. 147 IRF 2nd order), Boyce (p.272), Campbell (p.263), Dorf (p.327), Etkin (pp. 73-76), Goode (pp. 708–710), Gupta (pp. 72, 86), Holmes (p.179), Jack (p. 575), Jeffrey (p.412), Korman (p. 160), Kreyszig (pp. 227–230), Neil (pp.102-104), Ricardo (pp.215-216).

2. **Mention the change of initial condition without giving an explicit formula**
   Anderson (p. 8: momentum argument for 2nd order), Antsaklis (p. 67: "the impulse response of a linear, time-invariant, continuous time system with integral representation is equal to the kernel of the integral representation of the system"), Benaroya (p.19 due to "principle of conservation of linear momentum" governs the change the velocity via impulse 'During collisions large forces act resulting in almost instantaneous changes in velocity and therefore in linear momentum'), Brogliato (p.2: "impulsive forces imply a discontinuity in the velocity while positions remain continuous"; p.7: in mechanical systems, continuous positions and discontinuous velocities are produced by impulsive forces, and vice versa"), Howell (p. 560: "Observe that using a delta function force leads to the velocity changing instantly from one constant to another"), James (p.345, p.365), Kausel (p. 82: " the impulse imparted on a mass m abruptly changes its velocity from zero to V = 1/m"), Logan (pp.169-170, p.172), MacCluer (p.374: "Notice that the solution in equation ... doesn't actually satisfy the initial condition"), McOwen (pp. 98-99), Peterson (p. 363: "discontinuous forcing function causes a jump in the velocity of the mass"), Ram (p. 22-5), Shabana (p. 40: "This result indicates that the effect of the impulsive force, which acts over a very short time duration on a system which is initially at rest, can be accounted for by considering the motion of the system with initial velocity 11m and zero initial displacement.")

3. **Provide an explicit formula for changing initial conditions for specific equations**
   Angeles (p.115: "consequence, the ball undergoes a finite change in its velocity", p.116: change IC for IRF for 1st order system, p.119: change IC for IRF for 2nd order system, pp.132/136: derivative of delta as load), Balachandran (p. 301: IRF for 2nd order system), Baruh (p.259: change IC for 2nd order system due to impulse load), Beards (p.66: "the impulse F, acting on a body will result in a sudden change in its velocity without an appreciable change in its displacement. Thus the motion of a single degree of freedom system excited by an impulse F, corresponds to free vibration with initial conditions x = 0 and v0, = F/m at t = 0"), Chopra (Demonstrates that discontinuous forcing via impulse is mathematically equivalent to modified initial conditions; p.121 exact formulae for change IC for linear oscillator (from zero IC); p.616 example of impulse response for MDOF), Cooper (Provides explicit formula for piecewise smooth derivatives showing jump ↔ delta connection. Foundational reference proving mathematically that impulses (delta forces) arise naturally from discontinuities; p.5 change IC for pendulum was in rest), Duffy (p.93 "This avoids the problem of the Green's function not satisfying all of the initial conditions." + (3.1.7) provide the initial condition delivers the IRF as free motion., p.166, p.284), Edwards (p. 500, 2nd order with time shift), Esfandiari (p. 57: change IC for IRF for 2nd order system/"when impulsive forces are present in the system, initial values and initial conditions are indeed different", p.343: "Impulse Response of First-Order Systems",  p.351/359: "Impulse Response of Second-Order Systems"), Fairman (page 31, In addition we see from (1.81) that the zero-input response equals the impulse response when the initial state is x(0) = B (IRF is equal to some non-zero IC)), Franklin (p.110: change IC on 1st order system), Haddad (p.50 "we can always reproduce the impulsive response with the free response by setting x(0) = Bv"), Hallauer (p. 158 change IC for 1st order system), Inman p.219: "impulsive load for the system initially at rest is calculated by recalling from physics that an impulse imparts a change in momentum to a body", p.557: IRF for PDE/string), Iyengar (p. 87: change IC for SDOF whilst delta load, p.121 IRF for MDOF), Jazar (pp. 173, p.188: "Impulse will only change the initial conditions, and hence, the response of a multi-DOF system will be the transient response to a new set of initial conditions"), Kabe (pp.149-150: "it would appear that applying a unit impulse at t = 0 is equivalent to giving the system an initial velocity", p.163), Klee (p.170: change IC for 1st order system), Lathi (pp.164-165: "Find the impulse response h(t) for a system specified by (D^2 +5D+6)y(t) = (D+1)x(t)"), Luintel (p.215: "velocity of the system immediately after the application of impulse I is I/m", 507), Meirovitch (p.161: "effect of a unit impulse at t = 0 is to produce an equivalent initial velocity"), Nielsen (p.24: "Consequently, an impulsive load causes a discontinuous change of the velocity", p.63: solution for IRF for MDOF system), Palm (p.96: change IC for 1st/2nd order system, p.116: "Impulse Response of Second-Order Models"), Polking (p.231: IRF for 2nd order system), Schiff (p.82-83 2nd order system with impulse is equal to free vibration of the same system but changed IC), Silva (p.87 for 2nd order system for IRF mentioned change IC, "The Riddle of Zero Initial Conditions"), Sinha (p.69 mentioned changing IC for solution of 1st order ODE with unit impulse as load), Thorby (p.50: "unit impulse of force is applied to it ... that if dv is the change in velocity, then dv=1/m, but the change in isplacement is negligible"), Trench (pp. 478–480: solution some 2nd order system with impulse load), Tse (p. 54: change IC for 2nd order system with delta load)

4. **Supply a formulae for the case where the load contains only the delta function (or its derivatives) for general $n$**

   - Adkins (p. 319: provide formulae for changing IC to calculate IRF as free response for LTI ODE n-th order)
   - Beneš (article; for LTI ODE with delta load, provided the whole formula for changing IC - (9); the authors were very close to provide the whole formula for LTI ODE with the delta and its derivatives as load)
   - Camporesi (p.2: for n-th order equation in the form giving a formulae for changing IC to get IRF as free vibration, p.5: example for 1st order system)
   - Campos (p. 166: change IC for oscillator with first derivative of delta, p.167: exact solution for oscillator with odd/even derivative of delta as load)
   - Filippov (the authors used the approach from Beneš; p.20: author provided the trick how to convert original ODE with delta and its derivatives as right side into system of 1st order ODE with changed right side that contains only regular function, not general ones. BUT the conversion formula missed the important part "how to change IC to solve the changed system". We need to conclude that Filippov's result is not usable for engineering tasks)

5. **Closed-form solution for an LTI ODE with a sum of derivatives of the Dirac delta as the forcing function**
   To the best of our knowledge, no such solution exists in the literature (see Conclusion).

### 3 Conclusion

Across the sources surveyed, a consistent pattern emerges: the solution of an LTI ODE driven by a Dirac delta forcing term coincides with the solution of the corresponding homogeneous equation under a shifted initial condition (Section 1). The literature treats this equivalence unevenly, however. As the classification in Section 2 shows, most sources either use the equivalence implicitly, without stating it (category 1), or mention it qualitatively without an explicit formula (category 2); a smaller subset derive an explicit formula for a specific order of equation (category 3); and fewer still address the general case of an n-th order equation forced by the delta function alone (category 4). None of the surveyed sources provide a closed-form solution for the most general case — an LTI ODE forced by a sum of derivatives of the Dirac delta (category 5).

This gap points to two open needs in the literature: a treatment of derivatives of the delta function as forcing terms that is as thorough as the treatment of the delta function itself, and a unified computational framework that covers the full range of derivative and equation orders within a single formula, rather than the equation-by-equation formulas found in category 3.

### REFERENCES

<div style="font-size: 0.85em; line-height: 1.5; column-count: 2; column-gap: 2em;">

[1] Adkins, W. A., & Davidson, M. G. (2012). *Ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4614-3618-8

[2] Alam, J., Hu, G., Babu, H. M. H., & Xu, H. (2023). *Control engineering: Theory and applications*. CRC Press. https://doi.org/10.1201/9781003293859

[3] Anderson, B., & Rufer, S. (2018, August 13). *Control theory: A brief introduction*. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

[4] Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4419-1027-1

[5] Antsaklis, Panos J.; Michel, Anthony N. *A Linear Systems Primer*. Birkhäuser, 2007. ISBN: 9780817644604

[6] Arfken, G. B., Weber, H. J., & Harris, F. E. (2011). Mathematical methods for physicists: A comprehensive guide (7th ed.). Academic Press / Elsevier. Print ISBN: 978-0-12-384654-9

[7] Asadi, F., Bolanos, R. E., & Rodríguez, J. (2019). *Feedback control systems: The MATLAB®/Simulink® approach* (Synthesis Lectures on Control and Mechatronics, Lecture #5). Morgan & Claypool Publishers. https://doi.org/10.2200/S00909ED1V01Y201903CRM005

[8] Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781108615839

[9] Baruh, H. (2015). *Applied dynamics*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-0734-7) https://doi.org/10.1201/b18272

[10] Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press. (ISBN: 0340645806, 9780340645802, 0470235861, 9780470235867)

[11] Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-5265-7) https://doi.org/10.1201/b22347

[12] Benchohra, Mouffak; Henderson, Johnny; Ntouyas, Sotiris K. *Impulsive Differential Equations and Inclusions*. Hindawi Publishing, 2006.

[13] Beneš, K. (1978). On modelling dynamic systems excited by the Dirac function. *Sborník prací Přírodovědecké fakulty University Palackého v Olomouci. Matematika, 17*(1), 123–129. http://dml.cz/dmlcz/120062

[14] Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

[15] Boyce, W. E., & DiPrima, R. C. (2017). *Elementary differential equations and boundary value problems* (11th ed.). John Wiley & Sons, Inc. (ISBN: 978-1-119-37792-4)

[16] Brogliato, Bernard. *Nonsmooth Mechanics: Models, Dynamics and Control* (3rd ed.). Springer, 2015.

[17] Campbell, S. L., & Haberman, R. (2008). Introduction to differential equations with dynamical systems. Princeton University Press. ISBN: 978-0-691-12474-2 (hardcover)

[18] Camporesi, Carlo. *An Introduction to Linear Ordinary Differential Equations Using the Impulsive Response Method and Factorization*. 2019.

[19] Campos, L. M. B. C. (2020). *Linear differential equations and oscillators* (Vol. 4). CRC Press, Taylor & Francis Group. (ISBN: 978-0-367-13718-2) https://doi.org/10.1201/9780429028984

[20] Chasnov, J. R. (2009–2016). *Introduction to differential equations: Lecture notes for MATH 2351/2352*. The Hong Kong University of Science and Technology.

[21] Chopra, A. K. (2020). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed., SI units). Pearson Education Limited. (ISBN: 978-1-292-24918-6)

[22] Cohen, A. M. (2007). *Numerical methods for Laplace transform inversion*. Springer Science+Business Media. (ISBN: 9780387282619, 0387282610) https://doi.org/10.1007/978-0-387-68855-8

[23] Cooper, David. *Distribution Theory*. 2000.

[24] Dorf, R. C., & Bishop, R. H. (2008). *Modern control systems: Solution manual* (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

[25] Duffy, D. G. (2015). *Green's functions with applications* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-5103-6) https://doi.org/10.1201/b17973

[26] Edwards, C. H., Penney, D. E., & Calvis, D. (2016). *Differential equations and boundary value problems: Computing and modeling* (5th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-10877-3)

[27] Esfandiari, R. S., & Lu, B. (2014). *Modeling and analysis of dynamic systems* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3) https://doi.org/10.1201/b16443

[28] Etkin, B. (2005). *Dynamics of atmospheric flight*. Dover Publications, Inc. (ISBN: 0-486-44522-4) (Original work published 1972)

[29] Fairman, Frederick W. *Linear Control Theory: The State Space Approach*. John Wiley & Sons, 1998. ISBN: 0-471-97489-7

[30] Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

[31] Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

[32] Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media, LLC. (ISBN: 978-0-387-79579-9, 9780387795805) https://doi.org/10.1007/978-0-387-79580-5

[33] Goode, S. W., & Annin, S. A. (2015). *Differential equations and linear algebra* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-321-96467-0)

[34] Gupta, A., & Verma, Y. P. (2020). *Automatic control engineering*. I.K. International Pvt. Ltd. (ISBN: 978-93-89583-74-8)

[35] Haddad, Wassim M.; Chellaboina, Vijaysekhar; Hui, Qing. *Nonnegative and Compartmental Dynamical Systems*. Oxford University Press, 2009. ISBN: 978-0-691-14411-5

[36] Hallauer, William L. *Linear Time-Invariant Dynamic Systems*. John Wiley & Sons, 2016.

[37] Holmes, M. H. (2023). Introduction to differential equations (3rd ed.). XanEdu. ISBN: 978-1-71147-191-4

[38] Howell, K. B. (2020). *Ordinary differential equations: An introduction to the fundamentals* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-138-60583-1) https://doi.org/10.1201/9780429347429

[39] Inman, Daniel J. *Engineering Vibration* (4th ed.). Pearson Education, Inc., 2014. ISBN: 978-0-13-287169-3

[40] Iyengar, R. N. (2019). *Elements of mechanical vibration*. I.K. International Pvt. Ltd. (ISBN: 978-93-89633-34-4)

[41] Jack, H. (2015). *Dynamic system modeling and control*. Hugh Jack. (ISBN: 978-1-5089-9525-8)

[42] James, G., Dyke, P., Burley, D., Clements, D., Craven, M., Reis, T., Searl, J., Stander, J., Steele, N., & Wright, J. (2018). *Advanced modern engineering mathematics* (5th ed.). Pearson Education Limited. (ISBN: 978-1-292-17434-1)

[43] Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG. (ISBN: 978-3-031-43485-3) https://doi.org/10.1007/978-3-031-43486-0

[44] Jeffrey, A. (2002). Advanced engineering mathematics. Harcourt/Academic Press. ISBN-10: 0-12-382592-X

[45] Kabe, A. M., & Sako, B. H. (2020). *Structural dynamics: Fundamentals and advanced applications* (Vol. 1). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-821614-9) https://doi.org/10.1016/C2019-0-00137-8

[46] Kausel, Eduardo. *Advanced Structural Dynamics*. Cambridge University Press, 2017. ISBN: 978-1-107-17151-0. https://doi.org/10.1017/9781316761403

[47] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

[48] Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

[49] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

[50] Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

[51] Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

[52] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

[53] McOwen, R. (2012). Worldwide differential equations with linear algebra (1st ed.). Worldwide Center of Mathematics, LLC.  ISBN-10: 0-9842071-2-0

[54] Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

[55] Nagy, G. (n.d.). *Ordinary differential equations*. Mathematics Department, Michigan State University.

[56] Nielsen, S. R. K. (2004). *Vibration theory, Vol. 1: Linear vibration theory* (3rd ed.). Department of Civil Engineering, Aalborg University. (U/ Vol. U2004-1)

[57] O'Neil, Peter V. Advanced Engineering Mathematics, SI. SI ed., 8th ed., Cengage Learning, 2018. ISBN-13: 978-1-337-27452-4

[58] Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-615673-4)

[59] Palm, W. J., III. (2010). *System dynamics* (2nd ed.). McGraw-Hill. (ISBN: 978-0-07-352927-1)

[60] Peterson, G. L., & Sochacki, J. S. (2014). *Linear algebra & differential equations* (Pearson New International ed.). Pearson Education Limited. (ISBN: 978-1-269-37450-7)

[61] Polking, J., Boggess, A., & Arnold, D. (2006). *Differential equations with boundary value problems* (2nd ed.). Pearson Prentice Hall. (ISBN: 0-13-186236-7)

[62] Ram, B. (2009). *Engineering mathematics*. Pearson Education. (ISBN: 978-81-317-2691-4)

[63] Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-212819-3)

[64] Ricardo, H. J. (2020). A modern introduction to differential equations (3rd ed.). Academic Press. https://doi.org/10.1016/C2018-0-02231-8 Print ISBN-13: 978-0-12-823417-4

[65] Schiff, Joel L. (1999). *The Laplace transform: Theory and applications*. Springer-Verlag New York, Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

[66] Shabana, A. A. (1997). Vibration of discrete and continuous systems (2nd ed.). Springer-Verlag. https://doi.org/10.1007/978-1-4612-4036-5 Print ISBN-13: 978-1-4612-8474-1

[67] Sinha, N.K., & Ananthkrishnan, N. (2022). *Elementary flight dynamics with an introduction to bifurcation and continuation methods* (2nd ed.). CRC Press. https://doi.org/10.1201/9781003096801

[68] Thorby, D. (2008). *Structural dynamics and vibration in practice: An engineering handbook*. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

[69] Trench, W. F. (2024). *Elementary differential equations with boundary values problems*. LibreTexts. Retrieved December 19, 2024, from https://LibreTexts.org

[70] Tse, F. S., Morse, I. E., & Hinkle, R. T. (2018). *Mechanical vibrations: Theory and applications* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-879-6458-7)

[71] Weber, H. J., & Arfken, G. B. (2003). *Essential mathematical methods for physicists*. Academic Press. (ISBN: 978-0-12-059877-9) https://doi.org/10.1016/B978-0-12-059877-9.X5000-7

[72] Zill, D. G. (2023). A first course in differential equations with modeling applications (12th ed.). Cengage Learning. Hardcover ISBN: 978-0-357-76019-2

</div>

### Supplementary Bibliography

Many additional books related to Control Theory discuss the IRF, the solution of an LTI ODE with zero IC and an impulse delta function as load, without directly addressing the equivalence question examined in this review. Here is a short list of such books, which could be used as a starting point for further studying Control Theory:

<div style="font-size: 0.9em; line-height: 1.4; column-count: 2; column-gap: 2em;">

1. Abdallah - Feedback Control Systems MATLAB Simulink Approach
2. Alam, Jahangir - Control Engineering Theory and Applications
3. Anderson - Control Theory: A Brief Introduction
4. Antsaklis - Linear Systems Primer
5. Asadi - Feedback Control Systems MATLAB Simulink Approach
6. BURGHES - Control and Optimal Control Theories with Applications
7. Babu - Control Systems
8. Baillieul - Encyclopedia of Systems and Control (2ed)
9. Bavafa-Toosi - Introduction to Linear Control Systems
10. Bishop - Teaching Modern Control System Analysis and Design
11. Bubnicki - Modern Control Theory
12. D'Azzo - Linear Control System Analysis and Design (5ed)
13. Diana - Control of Mechanical Systems
14. Douglas - Fundamentals of Control Theory
15. Doyle - Feedback Control Theory
16. Frank - Control Theory Tutorial Basic Concepts
17. Franklin, Gene F. - Feedback Control of Dynamic Systems (7ed)
18. Gazi - Principles of Signals and Systems
19. Ghosh - Control Systems Theory and Applications
20. Gupta - Automatic Control Engineering
21. Guzman - Automatic Control with Interactive Tools
22. HARRIS - Stability of Input-Output Dynamical Systems
23. HESPANHA, João P. - Linear Systems Theory
24. Haidekker, Mark A. - Linear Feedback Controls: The Essentials (2ed)
25. Hallauer, Arthur C. - Linear Time-Invariant Dynamic Systems
26. Heaston, Richard - Modern Control Theory
27. Häaglund, Tore - Automatic Control: Lecture Notes
28. Jagan, S. - Control Systems
29. KAMARAJU, K. - Linear Systems (2ed): Analysis and Applications
30. Kani, S. - Control System Engineering (second edition)
31. Keviczky, László - Control Engineering
32. Khalil, Hassan K. - Control Systems: An Introduction
33. Koppel, David B. - Introduction to Control Theory
34. Krishnaveni, V. - Signals and Systems
35. Larminat, Philippe de - Analysis and Control of Linear Systems
36. Lathi, B. P. - Linear Systems and Signals (3ed)
37. Luna, Maria P. - Advances in Dynamical Systems Theory, Models, Algorithms and Applications
38. Narasimham, S. - Analysis of Linear Control System
39. Ogata, Katsuhiko - Modern Control Engineering (5ed)
40. Oppenheim, Alan V. - Signals and Systems (2ed)
41. Padmanabhan, A. - Control Systems
42. Paraskevopoulos, P. N. - Modern Control Engineering
43. Qiu, Li - Introduction to Feedback Control
44. Rawlings, James B. - Model Predictive Control (2ed)
45. Sivanandam, S. N. - Control Systems Engineering using MATLAB (2)
46. Skogestad, Sigurd - Multivariable Feedback Control: Analysis and Design
47. TRIPATHI, A. - Control System Analysis and Design (2ed)
48. Truxal, John G. - Automatic Feedback Control System Synthesis
49. Tymerski, Robert - Classical and Modern Control Design with examples from power electronics
50. Vinagre, Blas M. - Time in Control Theory: On Concepts, Measures and Uses
51. Williams, Robert L. - Linear State Space Control Systems
52. Zabczyk, Jerzy - Mathematical Control Theory: An Introduction (2ed)
53. Zerz, Eva - Introduction to Systems and Control Theory
54. Zhang, Qingsheng - Quantitative Process Control Theory

</div>
