## Literature Review: Solution of Linear ODEs with Delta Function as Load

**Denis Pleshkov**
<std.approach@gmail.com>
August 2026

### Abstract
This literature review examines how linear time-invariant (LTI) ordinary differential equations (ODEs) with impulsive forcing (represented by the Dirac delta function and its derivatives) are treated across differential equations, vibration theory, and control theory. Motivated by the practical need to find proper solution approaches and closed-form formulas for such systems, we surveyed 100+ sources. 3 critical gaps in the literature are identified—the absence of general $n$-th order proofs, limited treatment of derivatives of delta, and lack of unified computational frameworks.

### Keywords
Literature review, delta function, linear ODE, impulse response

### Introduction
The dynamics of evolving processes are often subject to abrupt changes, such as: impact of a hammer on a beam, a bat striking a ball, a bolt of lightning striking a tower.

Such short-term perturbations are frequently treated as instantaneous events, often modeled as "impulses." According to Rao (p. 381), an impulsive force is characterized by a large magnitude acting over a very short duration. The system's response to such a force is termed the impulse response function (IRF). Mathematically, an impulse can be represented within an initial value problem (IVP) by incorporating the Dirac delta function as the external forcing term. IVP means following: You have an ODE describing a system, plus the values of the system's state at some initial time. The goal is to find the unique solution satisfying both.  The impulse response of a system is defined as its output in response to an input $\delta(t)$, assuming the system is initially at rest. As Cohen (p. 13) notes, "The impulse function is useful when we are trying to model physical situations, such as the case of two billiard balls impinging, whemake re we have a large force acting for a short time which produces a finite change of momentum."

We're searching the literature providing the solution for LTI ODE with discontinious right hand, including delta-function and it's derivatives. The Dirac delta function is a well-known generalized function (distribution) used to model impulsive phenomena. Its properties are discussed extensively in the literature, including Bottega (p. 233), Chasnov (p. 62), Finan (p. 53), Nagy (p. 185), Rao (p. 381), Weber (p. 86), Zill (p. 292).

While seeking a general method to solve such systems, we found that existing literature primarily offers solutions for specific first- and second-order ODEs and almost no books presented the common (closed form) solution.

### Preliminary info about IFR
Many books related to Control Theory has tought us about Impulse Response Function (IRF) which is the solution of LTI ODE with zero IC and impulse delta function as load, we've parsed by eye more than 100 control Theory book, such as (This list could be used as starting point for studying Control Theory):

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
17. Franklin, Gene F. - Digital Control (3ed)
18. Franklin, Gene F. - Feedback Control of Dynamic Systems (7ed)
19. Gazi - Principles of Signals and Systems
20. Ghosh - Control Systems Theory and Applications
21. Gupta - Automatic Control Engineering
22. Guzman - Automatic Control with Interactive Tools
23. HARRIS - Stability of Input-Output Dynamical Systems
24. HESPANHA, João P. - Linear Systems Theory
25. Haidekker, Mark A. - Linear Feedback Controls: The Essentials (2ed)
26. Hallauer, Arthur C. - Linear Time-Invariant Dynamic Systems
27. Heaston, Richard - Modern Control Theory
28. Häaglund, Tore - Automatic Control: Lecture Notes
29. Jagan, S. - Control Systems
30. KAMARAJU, K. - Linear Systems (2ed): Analysis and Applications
31. Kani, S. - Control System Engineering (second edition)
32. Keviczky, László - Control Engineering
33. Khalil, Hassan K. - Control Systems: An Introduction
34. Koppel, David B. - Introduction to Control Theory
35. Krishnaveni, V. - Signals and Systems
36. Larminat, Philippe de - Analysis and Control of Linear Systems
37. Lathi, B. P. - Linear Systems and Signals (3ed)
38. Luna, Maria P. - Advances in Dynamical Systems Theory, Models, Algorithms and Applications
39. Narasimham, S. - Analysis of Linear Control System
40. Ogata, Katsuhiko - Modern Control Engineering (5ed)
41. Oppenheim, Alan V. - Signals and Systems (2ed)
42. Padmanabhan, A. - Control Systems
43. Paraskevopoulos, P. N. - Modern Control Engineering
44. Qiu, Li - Introduction to Feedback Control
45. Rawlings, James B. - Model Predictive Control (2ed)
46. Sivanandam, S. N. - Control Systems Engineering using MATLAB (2)
47. Skogestad, Sigurd - Multivariable Feedback Control: Analysis and Design
48. TRIPATHI, A. - Control System Analysis and Design (2ed)
49. Truxal, John G. - Automatic Feedback Control System Synthesis
50. Tymerski, Robert - Classical and Modern Control Design with examples from power electronics
51. Vinagre, Blas M. - Time in Control Theory: On Concepts, Measures and Uses
52. Williams, Robert L. - Linear State Space Control Systems
53. Zabczyk, Jerzy - Mathematical Control Theory: An Introduction (2ed)
54. Zerz, Eva - Introduction to Systems and Control Theory
55. Zhang, Qingsheng - Quantitative Process Control Theory

### 0 Preliminary data from Impulsive DE.
Most books we've found, discussed the property of impulse differential equations (IDE), as DE + rule to jump IC disregards of impulse function (like Dirac delta and it's derivative). This list could be used as starting point for studying IDE.

Benchohra, Mouffak; Henderson, Johnny; Ntouyas, Sotiris K. *Impulsive Differential Equations and Inclusions*. Hindawi Publishing, 2006.

Filippov A. Differential Equations with Discontinuous Righthand Sides ISBN 978-90-481-8449-1 DOI 10.1007/978-94-015-7793-9

Lakshmikantham, V., et al. Theory of Impulsive Differential Equations. World Scientific, 1989. Series in Modern Applied Mathematics, vol. 6. ISBN 978-9971-50-970-5, DOI: 10.1142/0906.

Perestyuk, Nikolai A., Viktor A. Plotnikov, Anatolii M. Samoilenko, and Natalia V. Skripnik. 2011. Differential Equations with Impulse Effects: Multivalued Right-hand Sides with Discontinuities. De Gruyter Studies in Mathematics, Vol. 40. Berlin: De Gruyter. https://doi.org/10.1515/9783110218176.

Samoilenko, A. M., & Perestyuk, N. A. (1995). Impulsive differential equations (World Scientific Series on Nonlinear Science. Series A, Monographs and Treatises, Vol. 14). World Scientific. https://doi.org/10.1142/2892

Orlov, Yury V. *Discontinuous Systems: Lyapunov Analysis and Robust Synthesis Under Uncertainty Conditions*. Springer, 2009.


### 1 Preliminary review: equivalence through initial condition modification

Several textbooks provide analytical solutions for first/second order LTI ODEs with a Dirac delta forcing function. Examples include Finan (p. 57), Nagy (pp. 189–190), Ogata (p. 190), Oliveira and Cortes (p. 3), Rao (p. 381), and Zill (p. 293).

Other authors explicitly note that the solution of an IVP with a delta load coincides with the solution of the corresponding homogeneous ODE subject to modified initial conditions. A brief survey of such observations follows.

Genta (p. 180) gives a formula for adjusting zero initial conditions in a second‑order ODE under delta loading.
Rao (p. 407) states the equivalence for 1st order system

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

Weber (p. 733) notes the analogous result

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

Balachandran (p. 301), Beards (p. 66), Bottega (pp. 235–236), Genta (p. 179), Kelly (p. 315), Meirovitch (pp. 160–161), Schiff (p. 83) and Schmitz (p. 118), all remarked that

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

Chasnov (p. 63) provides a formula for changing the initial conditions of a second‑order LTI ODE, while Oliveira and Cortes (p. 2) give a similar treatment for particular systems with zero initial conditions.

The above examples suggest a general pattern (though a formal proof appears to be missing in the literature): an IVP forced by a delta function may be equivalent to a homogeneous IVP with a shifted initial condition.

The LTI IVP with discontinious right side can also be viewed as a special case of an impulsive differential equation (see Benchohra, Henderson, and Ntouyas, *Impulsive Differential Equations and Inclusions*).

### 2 Detailed literature classification

For the purposes of this article we have surveyed a wide range of sources dealing with LTI ODEs subject to impulsive loads (the Dirac delta and its derivatives). The books and articles examined fall into five categories:

1. **Provide a solution without mentioning the equivalence**
   Asadi, Agarwal (IRF for state‑space systems), Alam (p. 219 1st order, p. 270 2nd order), Benaroya (p. 147 IRF 2nd order), Boyce (p. 346 2nd order with time shift), Brandt, Campbell, Dobrushkin (pp. 341–342, 348, 688), Dorf (pp. 123, 208), Duffy (pp. 93, 166, 284), Etkin (pp. 74, 76), Goode (pp. 708–709), Gupta (pp. 72, 86, 116), Holmes, Jack (p. 575), Kani, Korman (p. 160), Kreyszig (p. 227, 230–231), Liu (p. 50), McOwen (p. 98), Ram (pp. 845, 847), Ricardo, Jain.

2. **Mention the change of initial condition without giving an explicit formula**
   Adkins (p. 319, using momentum / Laplace transform), Anderson (p. 8, 2nd order, momentum argument), Angeles (pp. 115–119, 132, 136, 144), Balachandran (p. 301), Baruh (pp. 259, 303), Campos (p. 166, oscillator with one derivative of delta), Chopra (pp. 121, 489, 604, 616–626), Esfandiari (pp. 57, 351–359, 365, 394, 485), Franklin (pp. 110, 115, 144–149, 589), Howell (p. 560), Inman (pp. 220–225, 557–571), Iyengar (p. 87), James (pp. 345–353, 365–367), Jazar (pp. 173, 188–189), Kabe (pp. 149, 234, 300–302, 469–474), Kausel (p. 82), Lathi (p. 88), Logan (pp. 168–173, 344), Luintel (pp. 215, 507), MacCluer (pp. 373–375), Meirovitch (pp. 161, 181, 371, 463, 615), Nagle (pp. 407–408), Nielsen (pp. 24, 63), Palm (pp. 128, 134), Peterson (p. 363), Polking (pp. 231–232), Shabana (p. 206), Thorby (pp. 50–51), Trench (pp. 478–480), Tse (p. 54).

3. **Provide an explicit formula for changing initial conditions for specific equations**
   Edwards (p. 500, 2nd order with time shift), Klee (pp. 169–187).

4. **Supply a full formula for the case where the load contains only the delta function (and possibly its derivatives) for general $n$**
   Angeles (p. 144, state‑space IRF as a changed initial condition), Beneš (article, closed‑form using Laplace transform), Filippov (pp. 18–29, recurrence for IRF with one distribution on the right‑hand side, also delta in coefficients).

5. **Provide a closed‑form solution for an LTI ODE with a sum of derivatives of the Dirac delta as the forcing function**
   To the best of our knowledge, the present work appears to be the only one offering such a general treatment.

## Aux.Detail from REFERENCES2
1. Akhmet, Marat. *Principles of Discontinuous Dynamical Systems*. LAter, as Akhmet.
Akhmet's book is highly relevant to impulsive systems and discontinuous ODEs:
Extensive treatment of: impulsive differential equations with fixed and variable moments of impulses
Initial condition modifications: Chapter 2 & 5 discuss continuous dependence on initial conditions
Discontinuous right-hand sides: Chapters 8-9 address this topic specifically
What's missing: There is no result of equality with free vibration with changed IC as solution of discontinuous system.
2. Antsaklis, Panos J.; Michel, Anthony N. *A Linear Systems Primer*. Birkhäuser, 2007. ISBN: 9780817644604. Later as Antsaklis. On page 67 "the impulse response of a linear, time-invariant, continuoustime system with integral representation is equal to the kernel of the integral
representation of the system". On page 73 there is a direct formaulae how to calculate impulse response. There is no any hint how it related with free vibration.

Benaroya: p.19 due to "principle of conservation of linear momentum" governs the change the velocity via impulse 'During collisions large forces act resulting in
almost instantaneous changes in velocity and therefore
in linear momentum'. No mentioned about changes IC due to right side discontinuity.

4. Benchohra *Impulsive Differential Equations and Inclusions*, later Benchora. Benchohra is THE reference for impulsive differential equations theory. While other books provide context (Antsaklis: linear systems, Babitsky: vibro-impact applications), Benchohra provides the rigorous mathematical foundation for your core research topic on jump discontinuities and impulse effects in ODEs. There is no solution how to address delta function in right side.

5. d'Andréa-Novel, Brigitte; De Lara, Michel. *Control Theory for Engineers, later as  d'Andréa-Novel. p. 116 gave a formulae for "The impulse response of the time-continuous state-space system (5.1) with zero initial condition is given by". No connection with change initial conditions.

7. Brogliato, Bernard. *Nonsmooth Mechanics: Models, Dynamics and Control* (3rd ed.), later as Brogliato. on p.2 "One of the main consequences of such an approach is that the impulsive forces
imply a discontinuity in the velocity while positions remain continuous". on p.7 "This brief analysis shows that in mechanical systems, continuous positions and discontinuous velocities are produced by impulsive forces, and vice versa". This is the most relevant book reviewed so far—it provides rigorous mathematical treatment of impulsive forces, state discontinuities (position continuous, velocity discontinuous), Dirac measures, and measure differential equations. The core concept matches your research exactly: impulses create velocity jumps equivalent to modified initial conditions.

8. Camporesi, Carlo. *An Introduction to Linear Ordinary Differential Equations Using the Impulsive Response Method and Factorization*. 2019., later as Camporesi.  Elementary treatment of the impulsive response method for general n-th order ODEs. It explicitly shows how the IR solves the homogeneous equation with special initial conditions, then decomposes general solutions into forcing (via convolution) and IC (via homogeneous part). This directly demonstrates your core equivalence theme at any order. In this article the Author hiddenly uses impulse response function for creating a solution of ODE. And uses changed IC to find freee vbration, which are actually is IRF (page 3). There is no solution in case of derivative of delta-function. p.25 has a very interested LE with upper-sym matrix of coefficient of LTI ODE and coeffitient of right side. No connection between IRF and free vibrstion with changed IC.

[20] Chopra. Premier structural dynamics textbook proving your impulse-IC equivalence rigorously and practically. Section 4.1 defines impulse response h(t) from Dirac delta; Section 4.2 derives Duhamel's integral explicitly stating zero-IC assumption; Sections 4.7-4.9 analyze pulse responses via two-phase method (forced vibration during pulse + free vibration after, driven by initial conditions at pulse-end). Demonstrates that discontinuous forcing via impulse is mathematically equivalent to modified initial conditions. Essential reference combining theory and practical structural engineering applications. p.121 exact formulae for changeIC for linear oscillator (from zeroIC). p.616 example of impulse response for MDOF

15. Cooper, David. *Distribution Theory*, later Cooper. Rigorous mathematical foundations of distribution theory. Defines Dirac delta as distributional derivative of Heaviside function. Key theorem: jump discontinuities in functions produce delta terms in distributional derivatives. Provides explicit formula for piecewise smooth derivatives showing jump ↔ delta connection. Based on Schwartz theory. Foundational reference proving mathematically that impulses (delta forces) arise naturally from discontinuities, justifying your impulse-IC equivalence principle. p.5 change IC for pendulum was in rest

[*21]. Duffy, Dean G. *Green's Functions with Applications* (2nd ed.), later as Duffy. p.93 "This avoids the problem of the Green’s function not satisfying all of the initial
conditions." + (3.1.7) provide the initial condition delivers the IRF as free motion.

22. Fairman, Frederick W. *Linear Control Theory: The State Space Approach*, later as Fairman. page 31, In addition we see from (1.81) that the zero-input response equals the impulse response when the initial
state is x(0) = B (IRF is equal to some non-zero IC)

28. Haddad, Wassim M.; Chellaboina, Vijaysekhar; Hui, Qing. *Nonnegative and Compartmental Dynamical Systems*, later as Haddad, p.50 "we can always reproduce the impulsive response with the free response by setting x(0) = Bv".

30. Haidekker, Mark A. *Linear Feedback Controls: The Essentials* (2nd ed.), later as Haidekker in p.36 clearly states "the initial condition is valid only for
an infinitesimally short moment at the start of the experiment and can therefore be interpreted as a δ-pulse, scaled with the magnitude ... "

31. Hallauer, William L. *Linear Time-Invariant Dynamic Systems*, later as Hallauer. p. 158 (8-5) changeIC for 1st order system

52. Schiff, Joel L. *The Laplace Transform: Theory and Applications*, later as Schiff at p.82-83 mentioned that 2nd order system with impulse is equal to free vibration of the same system but changed IC.

54. Silva, Clarence W. *Vibration Fundamentals and Practice*, later as Silve_Vibration. p.87 for 2nd orser system for IRF mentioned change IC

60. Sinha, N.K., & Ananthkrishnan, N. (2022). Elementary flight dynamics with an introduction to bifurcation and continuation methods, later as Sinha. Sinha p.69 mentioned changinIC for solution of 1st order ODE with unit impulse as load.


## REFERENCES2

1. Akhmet, Marat. *Principles of Discontinuous Dynamical Systems*. Springer, 2010. ISBN: 978-1-4419-6580-6. DOI: 10.1007/978-1-4419-6581-3

2. Antsaklis, Panos J.; Michel, Anthony N. *A Linear Systems Primer*. Birkhäuser, 2007. ISBN: 9780817644604

4. Benchohra, Mouffak; Henderson, Johnny; Ntouyas, Sotiris K. *Impulsive Differential Equations and Inclusions*. Hindawi Publishing, 2006.

5. d'Andréa-Novel, Brigitte; De Lara, Michel. *Control Theory for Engineers: 
A Primer*. Springer, 2013. ISBN: 978-3-642-34323-0. 
DOI: 10.1007/978-3-642-34324-7

6. Westervelt, Eric R.; Grizzle, Jessy W.; Chevallereau, Christine; Choi, Jun Ho; Morris, Benjamin. *Feedback Control of Dynamic Bipedal Robot Locomotion*. CRC Press, 2007. ISBN: 978-1-4200-5372-2

7. Brogliato, Bernard. *Nonsmooth Mechanics: Models, Dynamics and Control* (3rd ed.). Springer, 2015.

8. Camporesi, Carlo. *An Introduction to Linear Ordinary Differential Equations Using the Impulsive Response Method and Factorization*. 2019.

15. Cooper, David. *Distribution Theory*. 2000.

22. Fairman, Frederick W. *Linear Control Theory: The State Space Approach*. John Wiley & Sons, 1998. ISBN: 0-471-97489-7

24. Filippov, A. F. *Differential Equations with Discontinuous Right-Hand Sides*. Kluwer Academic Publishers, 1988. ISBN: 978-90-481-8449-1

28. Haddad, Wassim M.; Chellaboina, Vijaysekhar; Hui, Qing. *Nonnegative and Compartmental Dynamical Systems*. Oxford University Press, 2009. ISBN: 978-0-691-14411-5

30. Haidekker, Mark A. *Linear Feedback Controls: The Essentials* (2nd ed.). Elsevier, 2020. ISBN: 978-0-12-818778-4

31. Hallauer, William L. *Linear Time-Invariant Dynamic Systems*. John Wiley & Sons, 2016.

35. Inman, Daniel J. *Engineering Vibration* (4th ed.). Pearson, 2014.

39. Kausel, Eduardo. *Advanced Structural Dynamics*. MIT Press, 2001. ISBN: 9781107171510

52. Schiff, Joel L. *The Laplace Transform: Theory and Applications*. Springer, 2019.

60. Sinha, N.K., & Ananthkrishnan, N. (2022). Elementary flight dynamics with an introduction to bifurcation and continuation methods (2nd ed.). CRC Press. https://doi.org/10.1201/9781003096801


### REFERENCES

[1] Adkins, W. A., & Davidson, M. G. (2012). *Ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4614-3618-8

[2] Agarwal, R. P., & O'Regan, D. (2008). *An introduction to ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-0-387-71276-5

[3] Alam, J., Hu, G., Babu, H. M. H., & Xu, H. (2023). *Control engineering: Theory and applications*. CRC Press. https://doi.org/10.1201/9781003293859

[4] Anderson, B., & Rufer, S. (2018, August 13). *Control theory: A brief introduction*. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

[5] Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4419-1027-1

[6] Asadi, F., Bolanos, R. E., & Rodríguez, J. (2019). *Feedback control systems: The MATLAB®/Simulink® approach* (Synthesis Lectures on Control and Mechatronics, Lecture #5). Morgan & Claypool Publishers. https://doi.org/10.2200/S00909ED1V01Y201903CRM005

[8] Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781108615839

[9] Baruh, H. (2015). *Applied dynamics*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-0734-7) https://doi.org/10.1201/b18272

[10] Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press. (ISBN: 0340645806, 9780340645802, 0470235861, 9780470235867)

[11] Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-5265-7) https://doi.org/10.1201/b22347

[13] Beneš, K. (1978). On modelling dynamic systems excited by the Dirac function. *Sborník prací Přírodovědecké fakulty University Palackého v Olomouci. Matematika, 17*(1), 123–129. http://dml.cz/dmlcz/120062

[14] Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

[15] Boyce, W. E., & DiPrima, R. C. (2012). *Elementary differential equations and boundary value problems* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45831-0)

[19] Campos, L. M. B. C. (2020). *Linear differential equations and oscillators* (Vol. 4). CRC Press, Taylor & Francis Group. (ISBN: 978-0-367-13718-2) https://doi.org/10.1201/9780429028984

[20] Chasnov, J. R. (2009–2016). *Introduction to differential equations: Lecture notes for MATH 2351/2352*. The Hong Kong University of Science and Technology.

[21] Chopra, A. K. (2020). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed., SI units). Pearson Education Limited. (ISBN: 978-1-292-24918-6)

[22] Cohen, A. M. (2007). *Numerical methods for Laplace transform inversion*. Springer Science+Business Media. (ISBN: 9780387282619, 0387282610) https://doi.org/10.1007/978-0-387-68855-8

[23] Dobrushkin, V. A. (2015). *Applied differential equations: The primary course*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-2835-5) https://doi.org/10.1201/b17886

[24] Dorf, R. C., & Bishop, R. H. (2008). *Modern control systems: Solution manual* (11th ed.). Pearson Education, Inc. (ISBN: 0-13-227029-3)

[25] Duffy, D. G. (2015). *Green's functions with applications* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-5103-6) https://doi.org/10.1201/b17973

[26] Edwards, C. H., Penney, D. E., & Calvis, D. (2016). *Differential equations and boundary value problems: Computing and modeling* (5th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-10877-3)

[27] Esfandiari, R. S., & Lu, B. (2014). *Modeling and analysis of dynamic systems* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4665-7495-3) https://doi.org/10.1201/b16443

[28] Etkin, B. (2005). *Dynamics of atmospheric flight*. Dover Publications, Inc. (ISBN: 0-486-44522-4) (Original work published 1972)

[29] ?Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

[30] Finan, M. B. (n.d.). *Laplace transforms: Theory, problems, and solutions*. Arkansas Tech University.

[31] Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

[32] Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media, LLC. (ISBN: 978-0-387-79579-9, 9780387795805) https://doi.org/10.1007/978-0-387-79580-5

[33] Goode, S. W., & Annin, S. A. (2015). *Differential equations and linear algebra* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-321-96467-0)

[34] Gupta, A., & Verma, Y. P. (2020). *Automatic control engineering*. I.K. International Pvt. Ltd. (ISBN: 978-93-89583-74-8)

[36] Howell, K. B. (2020). *Ordinary differential equations: An introduction to the fundamentals* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-138-60583-1) https://doi.org/10.1201/9780429347429

[37] Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-13-287169-3)

[38] Iyengar, R. N. (2019). *Elements of mechanical vibration*. I.K. International Pvt. Ltd. (ISBN: 978-93-89633-34-4)

[39] Jack, H. (2015). *Dynamic system modeling and control*. Hugh Jack. (ISBN: 978-1-5089-9525-8)

[41] James, G., Dyke, P., Burley, D., Clements, D., Craven, M., Reis, T., Searl, J., Stander, J., Steele, N., & Wright, J. (2018). *Advanced modern engineering mathematics* (5th ed.). Pearson Education Limited. (ISBN: 978-1-292-17434-1)

[42] Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG. (ISBN: 978-3-031-43485-3) https://doi.org/10.1007/978-3-031-43486-0

[43] Kabe, A. M., & Sako, B. H. (2020). *Structural dynamics: Fundamentals and advanced applications* (Vol. 1). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-821614-9) https://doi.org/10.1016/C2019-0-00137-8

[45] Kausel, E. (2017). *Advanced structural dynamics*. Cambridge University Press. (ISBN: 978-1-107-17151-0) https://doi.org/10.1017/9781316761403

[46] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications, SI*. Cengage Learning. (ISBN: 9781439062142)

[47] ?Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications*. Cengage Learning. (ISBN-13: 978-1-4390-6212-8)

[48] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

[49] Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

[50] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

[51] Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

[52] Liu, X. (2018). *Systems control theory*. Walter de Gruyter GmbH; Science Press. (ISBN: 978-3-11-057494-4) https://doi.org/10.1515/9783110574951

[53] Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

[54] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

[57] ?Meirovitch, L. (1986). *Elements of vibration analysis* (Subsequent ed.). McGraw-Hill College. (ISBN: 978-0-07-041342-9)

[58] ?Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

[59] Nagle, R. K., Saff, E. B., & Snider, A. D. (2018). *Fundamentals of differential equations* (9th ed.). Pearson Education, Inc. (ISBN: 978-0-321-97706-9)

[61] Nagy, G. (n.d.). *Ordinary differential equations*. Mathematics Department, Michigan State University.

[62] Nielsen, S. R. K. (2004). *Vibration theory, Vol. 1: Linear vibration theory* (3rd ed.). Department of Civil Engineering, Aalborg University. (U/ Vol. U2004-1)

[63] Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-615673-4)

[65] Palm, W. J., III. (2010). *System dynamics* (2nd ed.). McGraw-Hill. (ISBN: 978-0-07-352927-1)

[66] Peterson, G. L., & Sochacki, J. S. (2014). *Linear algebra & differential equations* (Pearson New International ed.). Pearson Education Limited. (ISBN: 978-1-269-37450-7)

[67] Polking, J., Boggess, A., & Arnold, D. (2006). *Differential equations with boundary value problems* (2nd ed.). Pearson Prentice Hall. (ISBN: 0-13-186236-7)

[68] Ram, B. (2009). *Engineering mathematics*. Pearson Education. (ISBN: 978-81-317-2691-4)

[69] Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-212819-3)

[71] Schiff, J. L. (1999). *The Laplace transform: Theory and applications*. Springer-Verlag New York, Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

[72] Schmitz, T. L., & Smith, K. S. (2012). *Mechanical vibrations: Modeling and measurement*. Springer Science+Business Media, LLC. (ISBN: 978-1-4614-0459-0; e-ISBN: 978-1-4614-0460-6) https://doi.org/10.1007/978-1-4614-0460-6

[73] Shabana, A. A. (1996). *Theory of vibration: An introduction* (2nd ed.). Springer-Verlag. (ISBN: 978-1-4612-8456-7) https://doi.org/10.1007/978-1-4612-3976-5 (Reprinted from *Theory of vibration: An introduction*, by A. A. Shabana, 1991, Springer-Verlag)

[76] Thorby, D. (2008). *Structural dynamics and vibration in practice: An engineering handbook*. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

[77] Trench, W. F. (2024). *Elementary differential equations with boundary values problems*. LibreTexts. Retrieved December 19, 2024, from https://LibreTexts.org

[78] Tse, F. S., Morse, I. E., & Hinkle, R. T. (2018). *Mechanical vibrations: Theory and applications* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-879-6458-7)

[79] Weber, H. J., & Arfken, G. B. (2003). *Essential mathematical methods for physicists*. Academic Press. (ISBN: 978-0-12-059877-9) https://doi.org/10.1016/B978-0-12-059877-9.X5000-7

[84] Zill, D. G. (2009). *A first course in differential equations with modeling applications* (9th ed.). Brooks/Cole, Cengage Learning. (ISBN-13: 978-0-495-10824-5) https://doi.org/10.1017/9781316841051
