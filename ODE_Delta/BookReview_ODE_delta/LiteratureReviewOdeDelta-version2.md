## Literature Review: Solution of Linear Time-Invariant ODEs with Dirac Delta Function and Its Derivatives

**Denis Pleshkov**
<std.approach@gmail.com>
August 2026

### Abstract
This literature review examines how linear time-invariant (LTI) ordinary differential equations (ODEs) with impulsive forcing—represented by the Dirac delta function and its derivatives—are treated across differential equations, vibration theory, and control theory. Motivated by the practical need to find proper solution approaches and closed-form formulas for such systems, we surveyed 100+ sources and identified a unifying principle: delta-forced nonhomogeneous ODEs are equivalent to homogeneous systems with modified initial conditions. 3 critical gaps in the literature are identified—the absence of general $n$-th order proofs, limited treatment of derivatives of delta, and lack of unified computational frameworks.

### Keywords
Literature review, delta function, linear ODE, impulsive differential equations

### Introduction
The dynamics of evolving processes are often subject to abrupt changes, such as: impact of a hammer on a beam, a bat striking a ball, a bolt of lightning striking a tower.

Such short-term perturbations are frequently treated as instantaneous events, often modeled as "impulses." According to Rao (p. 381), an impulsive force is characterized by a large magnitude acting over a very short duration. The system's response to such a force is termed the impulse response function (IRF). Mathematically, an impulse can be represented within an initial value problem (IVP) by incorporating the Dirac delta function as the external forcing term. IVP means following: You have an ODE describing a system, plus the values of the system's state at some initial time. The goal is to find the unique solution satisfying both.  The impulse response of a system is defined as its output in response to an input $\delta(t)$, assuming the system is initially at rest. As Cohen (p. 13) notes, "The impulse function is useful when we are trying to model physical situations, such as the case of two billiard balls impinging, whemake re we have a large force acting for a short time which produces a finite change of momentum."

We're searching the literature providing the solution for LTI ODE with discontinious right hand, including delta-function and it's derivatives. The Dirac delta function is a well-known generalized function (distribution) used to model impulsive phenomena. Its properties are discussed extensively in the literature, including Balachandran (p. 287), Bottega (p. 233), Chasnov (p. 62), Finan (p. 53), Nagy (p. 185), Rao (p. 381), Weber (p. 86), Zill (p. 292).

While seeking a general method to solve such systems, we found that existing literature primarily offers solutions for specific first- and second-order ODEs and almost no books presented the common (closed form) solution.

### 1 Preliminary review: equivalence through initial condition modification

Several textbooks provide analytical solutions for first/second order LTI ODEs with a Dirac delta forcing function. Examples include Finan (p. 57), Nagy (pp. 189–190), Ogata (p. 190), Oliveira and Cortes (p. 3), Rao (p. 381), and Zill (p. 293).

Other authors explicitly note that the solution of an IVP with a delta load coincides with the solution of the corresponding homogeneous ODE subject to modified initial conditions. A brief survey of such observations follows.

Genta (p. 180) gives a formula for adjusting zero initial conditions in a second‑order ODE under delta loading.
Rao (p. 407) states the equivalence

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

Balachandran (pp. 287–288), Beards (p. 66), Bottega (pp. 235–236), Genta (p. 179), Kelly (p. 315), Meirovitch (pp. 160–161), Schiff (p. 83) and Schmitz (p. 118), all remarked that

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


### REFERENCES
[1] Adkins, W. A., & Davidson, M. G. (2012). *Ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4614-3618-8

[2] Agarwal, R. P., & O'Regan, D. (2008). *An introduction to ordinary differential equations*. Springer Science+Business Media. https://doi.org/10.1007/978-0-387-71276-5

[3] Alam, J., Hu, G., Babu, H. M. H., & Xu, H. (2023). *Control engineering: Theory and applications*. CRC Press. https://doi.org/10.1201/9781003293859

[4] Anderson, B., & Rufer, S. (2018, August 13). *Control theory: A brief introduction*. Bruin Racing, Baja SAE, University of California, Los Angeles. https://doi.org/10.13140/RG.2.2.14805.17129

[5] Angeles, J. (2011). *Dynamic response of linear mechanical systems: Modeling, analysis and simulation*. Springer Science+Business Media. https://doi.org/10.1007/978-1-4419-1027-1

[6] Asadi, F., Bolanos, R. E., & Rodríguez, J. (2019). *Feedback control systems: The MATLAB®/Simulink® approach* (Synthesis Lectures on Control and Mechatronics, Lecture #5). Morgan & Claypool Publishers. https://doi.org/10.2200/S00909ED1V01Y201903CRM005

[7] Balachandran, B., & Magrab, E. B. (2009). *Vibrations* (2nd ed., International SI ed.). Cengage Learning. (ISBN: 9780534552060, 0495411256)

[8] Balachandran, B., & Magrab, E. B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781108615839

[9] Baruh, H. (2015). *Applied dynamics*. CRC Press, Taylor & Francis Group. (ISBN: 978-1-4822-0734-7) https://doi.org/10.1201/b18272

[10] Beards, C. F. (1996). *Structural vibration: Analysis and damping*. Arnold; Halsted Press. (ISBN: 0340645806, 9780340645802, 0470235861, 9780470235867)

[11] Benaroya, H., Nagurka, M., & Han, S. (2017). *Mechanical vibration: Analysis, uncertainties, and control* (4th ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4987-5265-7) https://doi.org/10.1201/b22347

[12] Benchohra, M., Henderson, J., & Ntouyas, S. (2006). *Impulsive differential equations and inclusions*. Hindawi Publishing Corporation. (ISBN: 977-5945-50-X)

[13] Beneš, K. (1978). On modelling dynamic systems excited by the Dirac function. *Sborník prací Přírodovědecké fakulty University Palackého v Olomouci. Matematika, 17*(1), 123–129. http://dml.cz/dmlcz/120062

[14] Bottega, W. J. (2006). *Engineering vibrations*. CRC Press. (ISBN: 9780849334207, 0849334209)

[15] Boyce, W. E., & DiPrima, R. C. (2012). *Elementary differential equations and boundary value problems* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45831-0)

[16] Brandt, A. (2023). *Noise and vibration analysis: Signal analysis and experimental procedures* (2nd ed.). John Wiley & Sons Ltd. (ISBN: 978-1-118-96120-1) https://doi.org/10.1002/9781118961232

[17] Butcher, J. C. (2008). *Numerical methods for ordinary differential equations* (2nd ed.). John Wiley & Sons, Ltd. (ISBN: 978-0-470-72335-7) https://doi.org/10.1002/9780470753767

[18] Campbell, S. L., & Haberman, R. (2008). *Introduction to differential equations with dynamical systems*. Princeton University Press. (ISBN: 978-0-691-12474-6)

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

[29] Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

[30] Finan, M. B. (n.d.). *Laplace transforms: Theory, problems, and solutions*. Arkansas Tech University.

[31] Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). *Feedback control of dynamic systems* (7th ed., Global ed.). Pearson Education Limited. (ISBN: 978-1-292-06890-9)

[32] Genta, G. (2009). *Vibration dynamics and control*. Springer Science+Business Media, LLC. (ISBN: 978-0-387-79579-9, 9780387795805) https://doi.org/10.1007/978-0-387-79580-5

[33] Goode, S. W., & Annin, S. A. (2015). *Differential equations and linear algebra* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-321-96467-0)

[34] Gupta, A., & Verma, Y. P. (2020). *Automatic control engineering*. I.K. International Pvt. Ltd. (ISBN: 978-93-89583-74-8)

[35] Holmes, M. H. (2023). *Introduction to differential equations* (3rd ed.). Mark H. Holmes. (ISBN: 978-1-71147-191-4)

[36] Howell, K. B. (2020). *Ordinary differential equations: An introduction to the fundamentals* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-138-60583-1) https://doi.org/10.1201/9780429347429

[37] Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson Education, Inc. (ISBN: 978-0-13-287169-3)

[38] Iyengar, R. N. (2019). *Elements of mechanical vibration*. I.K. International Pvt. Ltd. (ISBN: 978-93-89633-34-4)

[39] Jack, H. (2015). *Dynamic system modeling and control*. Hugh Jack. (ISBN: 978-1-5089-9525-8)

[40] Jain, S. (2011). *Modeling & simulation using MATLAB®-Simulink®*. Wiley India Pvt. Ltd. (ISBN: 978-81-265-3005-2)

[41] James, G., Dyke, P., Burley, D., Clements, D., Craven, M., Reis, T., Searl, J., Stander, J., Steele, N., & Wright, J. (2018). *Advanced modern engineering mathematics* (5th ed.). Pearson Education Limited. (ISBN: 978-1-292-17434-1)

[42] Jazar, R. N., & Marzbani, H. (2024). *Vehicle vibrations: Linear and nonlinear analysis, optimization, and design*. Springer Nature Switzerland AG. (ISBN: 978-3-031-43485-3) https://doi.org/10.1007/978-3-031-43486-0

[43] Kabe, A. M., & Sako, B. H. (2020). *Structural dynamics: Fundamentals and advanced applications* (Vol. 1). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-821614-9) https://doi.org/10.1016/C2019-0-00137-8

[44] Karris, S. T. (2003). *Signals and systems with MATLAB® applications* (2nd ed.). Orchard Publications. (ISBN: 9780970951168, 0970951167)

[45] Kausel, E. (2017). *Advanced structural dynamics*. Cambridge University Press. (ISBN: 978-1-107-17151-0) https://doi.org/10.1017/9781316761403

[46] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications, SI*. Cengage Learning. (ISBN: 9781439062142)

[47] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications*. Cengage Learning. (ISBN-13: 978-1-4390-6212-8)

[48] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

[49] Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

[50] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

[51] Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

[52] Liu, X. (2018). *Systems control theory*. Walter de Gruyter GmbH; Science Press. (ISBN: 978-3-11-057494-4) https://doi.org/10.1515/9783110574951

[53] Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

[54] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

[55] MacCluer, B. D., Bourdon, P. S., & Kriete, T. L. (2019). *Differential equations: Techniques, theory, and applications*. American Mathematical Society. (ISBN: 978-1-4704-4797-7)

[56] McOwen, R. (2012). *Worldwide differential equations with linear algebra*. Worldwide Center of Mathematics, LLC. (ISBN: 978-0-9842071-2-1)

[57] Meirovitch, L. (1986). *Elements of vibration analysis* (Subsequent ed.). McGraw-Hill College. (ISBN: 978-0-07-041342-9)

[58] Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

[59] Nagle, R. K., Saff, E. B., & Snider, A. D. (2018). *Fundamentals of differential equations* (9th ed.). Pearson Education, Inc. (ISBN: 978-0-321-97706-9)

[60] Nagoor Kani, A. (2019). *Control systems engineering* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-892-6199-8)

[61] Nagy, G. (n.d.). *Ordinary differential equations*. Mathematics Department, Michigan State University.

[62] Nielsen, S. R. K. (2004). *Vibration theory, Vol. 1: Linear vibration theory* (3rd ed.). Department of Civil Engineering, Aalborg University. (U/ Vol. U2004-1)

[63] Ogata, K. (2010). *Modern control engineering* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-615673-4)

[64] Oliveira, M. de, & Cortes, J. (2011, January 24). *Computing the impulse response*. http://control.ucsd.edu/mauricio/courses/mae143a/lectures/computingImpulseResponse.pdf

[65] Palm, W. J., III. (2010). *System dynamics* (2nd ed.). McGraw-Hill. (ISBN: 978-0-07-352927-1)

[66] Peterson, G. L., & Sochacki, J. S. (2014). *Linear algebra & differential equations* (Pearson New International ed.). Pearson Education Limited. (ISBN: 978-1-269-37450-7)

[67] Polking, J., Boggess, A., & Arnold, D. (2006). *Differential equations with boundary value problems* (2nd ed.). Pearson Prentice Hall. (ISBN: 0-13-186236-7)

[68] Ram, B. (2009). *Engineering mathematics*. Pearson Education. (ISBN: 978-81-317-2691-4)

[69] Rao, S. S. (2011). *Mechanical vibrations* (5th ed.). Pearson Education, Inc. (ISBN-13: 978-0-13-212819-3)

[70] Ricardo, H. J. (2021). *A modern introduction to differential equations* (3rd ed.). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-823417-4) https://doi.org/10.1016/C2020-0-00717-2

[71] Schiff, J. L. (1999). *The Laplace transform: Theory and applications*. Springer-Verlag New York, Inc. (ISBN: 0-387-98698-7) https://doi.org/10.1007/978-0-387-22757-3

[72] Schmitz, T. L., & Smith, K. S. (2012). *Mechanical vibrations: Modeling and measurement*. Springer Science+Business Media, LLC. (ISBN: 978-1-4614-0459-0; e-ISBN: 978-1-4614-0460-6) https://doi.org/10.1007/978-1-4614-0460-6

[73] Shabana, A. A. (1996). *Theory of vibration: An introduction* (2nd ed.). Springer-Verlag. (ISBN: 978-1-4612-8456-7) https://doi.org/10.1007/978-1-4612-3976-5 (Reprinted from *Theory of vibration: An introduction*, by A. A. Shabana, 1991, Springer-Verlag)

[74] Silva, C. W. de. (2000). *Vibration: Fundamentals and practice*. CRC Press LLC. (ISBN: 0-8493-1808-4) https://doi.org/10.1201/9781420052510

[75] Strang, G. (2016). *Introduction to linear algebra: Manual for instructors* (5th ed.). Wellesley-Cambridge Press. (ISBN: 978-0-9802327-7-6)

[76] Thorby, D. (2008). *Structural dynamics and vibration in practice: An engineering handbook*. Butterworth-Heinemann, an imprint of Elsevier. (ISBN: 978-0-7506-8002-8) https://doi.org/10.1016/B978-0-7506-8002-8.X0001-1

[77] Trench, W. F. (2024). *Elementary differential equations with boundary values problems*. LibreTexts. Retrieved December 19, 2024, from https://LibreTexts.org

[78] Tse, F. S., Morse, I. E., & Hinkle, R. T. (2018). *Mechanical vibrations: Theory and applications* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-879-6458-7)

[79] Weber, H. J., & Arfken, G. B. (2003). *Essential mathematical methods for physicists*. Academic Press. (ISBN: 978-0-12-059877-9) https://doi.org/10.1016/B978-0-12-059877-9.X5000-7

[80] Williams, R. L., II, & Lawrence, D. A. (2007). *Linear state-space control systems*. John Wiley & Sons, Inc. (ISBN: 978-0-471-73555-7) https://doi.org/10.1002/9780470117873

[81] Xue, D., Chen, Y., & Atherton, D. P. (2002, July 3). *Linear feedback control: Analysis and design with MATLAB*. Springer-Verlag.

[82] Xue, D., Chen, Y., & Atherton, D. P. (2007). *Linear feedback control: Analysis and design with MATLAB*. Society for Industrial and Applied Mathematics. (ISBN: 978-0-89871-638-2) https://doi.org/10.1137/1.9780898718621

[83] Yang, B., & Abramova, I. (2022). *Dynamic systems: Modelling, simulation, and analysis*. Cambridge University Press. (ISBN: 978-1-107-17979-0) https://doi.org/10.1017/9781316841051

[84] Zill, D. G. (2009). *A first course in differential equations with modeling applications* (9th ed.). Brooks/Cole, Cengage Learning. (ISBN-13: 978-0-495-10824-5) https://doi.org/10.1017/9781316841051
