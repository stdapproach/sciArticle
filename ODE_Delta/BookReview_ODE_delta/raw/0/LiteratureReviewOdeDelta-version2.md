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

## REFERENCES2

1. Camporesi, R., 2019. An Introduction to Linear Ordinary Differential Equations with Constant Coefficients Using the Impulsive Response Method and Factorization. arXiv preprint.
 
2. Camporesi, R., 2010. Linear ordinary differential equations. Revisiting the impulsive response method using factorization. arXiv preprint.
 
3. Brogliato, B., 2016. Nonsmooth Mechanics: Models, Dynamics and Control. 3rd edn. Berlin: Springer.
 
4. Dishliev, A., Dishlieva, K. & Nenov, S., 2012. Specific Asymptotic Properties of the Solutions of Impulsive Differential Equations. Methods and Applications. Sofia: Academic Publications, Ltd.
 
5. Gear, C.W. & Østerby, O., 1984. Solving Ordinary Differential Equations with Discontinuities. ACM Transactions on Mathematical Software, 10(1), pp. 23-44.
 
6. Graef, J.R. & Ouahab, A., 2008. First Order Impulsive Differential Inclusions with Periodic Conditions. Electronic Journal of Qualitative Theory of Differential Equations, (31), pp. 1-40.
 
7. Graef, J.R., Henderson, J. & Ouahab, A., 2013. Impulsive Differential Inclusions: A Fixed Point Approach. Berlin: De Gruyter.
 
8. Hassan, N. & Rzymowski, W., 1990. On the Cauchy Problem for Ordinary Differential Equations with Discontinuous Right-Hand Sides. Journal of Mathematical Analysis and Applications, 136(1), pp. 134-157.
 
9. Heikkila, S., Kumpulainen, M. & Seikkala, S., 1996. Existence, Uniqueness, and Comparison Results for a Differential Equation with Discontinuous Nonlinearities. Journal of Mathematical Analysis and Applications, 198(1), pp. 66-78.
 
10. Benchohra, M., Henderson, J. & Ntouyas, S.K., 2006. Impulsive Differential Equations and Inclusions. New York: Hindawi Publishing.
 
11. Jones, N., 1989. Structural Impact. Cambridge: Cambridge University Press.
 
12. d'Andréa-Novel, B. & De Lara, M., 2013. Control Theory for Engineers: A Primer. Berlin: Springer.
 
13. Samoilenko, A.M. & Perestyuk, N.A., 1995. Impulsive Differential Equations. Singapore: World Scientific Publishing.
 
14. Chicurel-Uziel, E. & Godínez-Rojano, F.A., 2013. Parametric Dirac Delta to Simplify the Solution of Linear and Nonlinear Problems with an Impulsive Forcing Function. Journal of Applied Mathematics and Physics, 1(2), pp. 30-53.
 
15. Lakshmikantham, V., Bainov, D.D. & Simeonov, P.S., 1989. Theory of Impulsive Differential Equations. Singapore: World Scientific Publishing.
 
16. Samoilenko, A.M. & Perestyuk, N.A., 1995. Impulsive Differential Equations. Singapore: World Scientific Publishing.
 
17. Datta, B.N., 2003. Numerical Methods for Linear Control Systems Design and Analysis. Philadelphia: SIAM (Society for Industrial and Applied Mathematics).
 
18. Fairman, F.W., 1998. Linear Control Theory: The State Space Approach. New York: John Wiley & Sons. ISBN: 0-471-02328-0.
 
19. Haddad, W.M., Chellaboina, V.S. & Hui, Q., 2010. Nonnegative and Compartmental Dynamical Systems. Princeton: Princeton University Press.
 
20. Chalishajar, D., States, A. & Lipscomb, B., 2016. On Applications of Generalized Functions in the Discontinuous Beam Bending Differential Equations. Applied Mathematics, 7(1), pp. 35-52.
 
21. Hassan, N. & Rzymowski, W., 1990. On the Cauchy Problem for Ordinary Differential Equations with Discontinuous Right-Hand Sides. Journal of Mathematical Analysis and Applications, 136(1), pp. 134-157.
 
22. Haddad, W.M. & Nersesov, S.G., 2011. Stability and Control of Large-Scale Dynamical Systems: A Vector Dissipative Systems Approach. Princeton: Princeton University Press.
 
23. Hallauer Jr., W.L., 2016. Introduction to Linear, Time-Invariant, Dynamic Systems for Students of Engineering. Blacksburg: Virginia Polytechnic Institute. [Self-published, Creative Commons License]
 
24. Hägglund, T., 2021. Automatic Control: Lecture Notes. Lund: Lund University. [Copyright 2009]
 
25. Kamaraju, K. & Narasimham, G.S.V., 2002. Linear Systems: Analysis and Applications. 2nd edn. Oxford: Oxford University Press.
 
26. Keviczky, L., Bars, R., Hetthéssy, J. & Bányász, C., 2019. Control Engineering. Berlin: Springer. ISBN: 978-981-10-8296-2.
 
27. Antsaklis, P.J. & Michel, A.N., 2007. A Linear Systems Primer. Boston: Birkhäuser. ISBN: 978-0-8176-4460-4.
 
28. d'Andréa-Novel, B. & De Lara, M., 2013. Control Theory for Engineers: A Primer. Berlin: Springer.
 
29. Chen, C.-T., 1999. Linear System Theory and Design. 3rd edn. New York: Oxford University Press.
 
30. Dahleh, M., Dahleh, M.A. & Verghese, G., 2011. Dynamic Systems and Control. MIT OpenCourseWare, 6.241J Spring 2011 Lecture Notes.
 
31. Ghosh, S., 2007. Control Systems: Theory and Applications. New Delhi: Pearson Education.
 
32. Golnaraghi, F. & Kuo, B.C., 2017. Automatic Control Systems. 10th edn. New York: McGraw-Hill Education. ISBN: 978-1-25-964384-2.
 
33. Hespanha, J.P., 2009. Linear Systems Theory. Princeton: Princeton University Press. ISBN: 978-0-691-14021-6.
 
34. Haidekker, M.A., 2020. Linear Feedback Controls: The Essentials. 2nd edn. Oxford: Elsevier.
 
35. Qiu, L., 2010. Introduction to Feedback Control. 2nd edn. Upper Saddle River, NJ: Pearson Education. ISBN: 0-13-235396-2.
 
36. Williams II, R.L. & Lawrence, D.A., 2007. Linear State-Space Control Systems. New York: John Wiley & Sons. ISBN: 978-0-471-73555-7.
 
37. Yang, T., 2001. Impulsive Control Theory. Berlin: Springer. ISBN: 3-540-42296-X.
 
38. Zabczyk, J., 2020. Mathematical Control Theory: An Introduction. 2nd edn. Berlin: Springer. ISBN: 978-3-030-44776-2.
 
39. Falsone, G., 2002. The Use of Generalised Functions in the Discontinuous Beam Bending Differential Equations. International Journal of Engineering Education, 18(3), pp. 337-343.
 
40. Cooper, J.B., 1978. Distribution Theory. Cambridge, MA: Academic Press.
 
41. Kamachkin, A.M. & Yevtushenko, D.K., 2014. Solution to Second-Order Differential Equations with Discontinuous Right-Hand Side. Electronic Journal of Differential Equations, 2014(221), pp. 1-6. ISSN: 1072-6691.
 
42. Danca, M.-F., 2001. On a class of discontinuous dynamical systems. Miskolc Mathematical Notes, 2(2), pp. 103-116. DOI: 10.18514/MMN.2001.41.
 
43. Kiseleva, M., Kuznetsov, N. & Leonov, G., 2013. Theory of Differential Inclusions and Its Application in Mechanics. In: Edited volume on differential equations and mechanical systems.
 

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

[29] Filippov, A. F. (1988). *Differential equations with discontinuous righthand sides* (F. M. Arscott, Ed.). Springer-Science+Business Media, B.V. (ISBN: 978-90-481-8449-1) https://doi.org/10.1007/978-94-015-7793-9 (Original work published 1988)

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

[47] Kelly, S. G. (2012). *Mechanical vibrations: Theory and applications*. Cengage Learning. (ISBN-13: 978-1-4390-6212-8)

[48] Klee, H., & Allen, R. (2011). *Simulation of dynamic systems with MATLAB® and Simulink®* (2nd ed.). CRC Press, Taylor & Francis Group. (ISBN: 978-1-4398-3674-3) https://doi.org/10.1201/b10495

[49] Korman, P. L. (2019). *Lectures on differential equations*. MAA Press, an imprint of the American Mathematical Society. (ISBN: 978-1-4704-5173-8)

[50] Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). John Wiley & Sons, Inc. (ISBN: 978-0-470-45836-5)

[51] Lathi, B. P., & Green, R. A. (2018). *Linear systems and signals* (3rd ed.). Oxford University Press. (ISBN: 978-0-19-020017-6)

[52] Liu, X. (2018). *Systems control theory*. Walter de Gruyter GmbH; Science Press. (ISBN: 978-3-11-057494-4) https://doi.org/10.1515/9783110574951

[53] Logan, J. D. (2015). *A first course in differential equations* (3rd ed.). Springer-Verlag. (ISBN: 978-3-319-17851-6) https://doi.org/10.1007/978-3-319-17852-3

[54] Luintel, M. C. (2024). *Textbook of mechanical vibrations*. Springer Nature Singapore Pte Ltd. (ISBN: 978-981-99-3613-7) https://doi.org/10.1007/978-981-99-3614-4

[57] Meirovitch, L. (1986). *Elements of vibration analysis* (Subsequent ed.). McGraw-Hill College. (ISBN: 978-0-07-041342-9)

[58] Meirovitch, L. (2001). *Fundamentals of vibrations* (International ed.). McGraw-Hill. (ISBN: 0-07-118174-1)

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

## REFERENCES_NOT_USED

[12] Benchohra, M., Henderson, J., & Ntouyas, S. (2006). *Impulsive differential equations and inclusions*. Hindawi Publishing Corporation. (ISBN: 977-5945-50-X)

[16] Brandt, A. (2023). *Noise and vibration analysis: Signal analysis and experimental procedures* (2nd ed.). John Wiley & Sons Ltd. (ISBN: 978-1-118-96120-1) https://doi.org/10.1002/9781118961232

[17] Butcher, J. C. (2008). *Numerical methods for ordinary differential equations* (2nd ed.). John Wiley & Sons, Ltd. (ISBN: 978-0-470-72335-7) https://doi.org/10.1002/9780470753767

[18] Campbell, S. L., & Haberman, R. (2008). *Introduction to differential equations with dynamical systems*. Princeton University Press. (ISBN: 978-0-691-12474-6)

[35] Holmes, M. H. (2023). *Introduction to differential equations* (3rd ed.). Mark H. Holmes. (ISBN: 978-1-71147-191-4)

[40] Jain, S. (2011). *Modeling & simulation using MATLAB®-Simulink®*. Wiley India Pvt. Ltd. (ISBN: 978-81-265-3005-2)

[44] Karris, S. T. (2003). *Signals and systems with MATLAB® applications* (2nd ed.). Orchard Publications. (ISBN: 9780970951168, 0970951167)

[55] MacCluer, B. D., Bourdon, P. S., & Kriete, T. L. (2019). *Differential equations: Techniques, theory, and applications*. American Mathematical Society. (ISBN: 978-1-4704-4797-7)

[56] McOwen, R. (2012). *Worldwide differential equations with linear algebra*. Worldwide Center of Mathematics, LLC. (ISBN: 978-0-9842071-2-1)

[60] Nagoor Kani, A. (2019). *Control systems engineering* (2nd ed.). CBS Publishers & Distributors Pvt. Ltd. (eISBN: 978-93-892-6199-8)

[64] Oliveira, M. de, & Cortes, J. (2011, January 24). *Computing the impulse response*. http://control.ucsd.edu/mauricio/courses/mae143a/lectures/computingImpulseResponse.pdf

[70] Ricardo, H. J. (2021). *A modern introduction to differential equations* (3rd ed.). Academic Press, an imprint of Elsevier. (ISBN: 978-0-12-823417-4) https://doi.org/10.1016/C2020-0-00717-2

[74] Silva, C. W. de. (2000). *Vibration: Fundamentals and practice*. CRC Press LLC. (ISBN: 0-8493-1808-4) https://doi.org/10.1201/9781420052510

[75] Strang, G. (2016). *Introduction to linear algebra: Manual for instructors* (5th ed.). Wellesley-Cambridge Press. (ISBN: 978-0-9802327-7-6)

[80] Williams, R. L., II, & Lawrence, D. A. (2007). *Linear state-space control systems*. John Wiley & Sons, Inc. (ISBN: 978-0-471-73555-7) https://doi.org/10.1002/9780470117873

[81] Xue, D., Chen, Y., & Atherton, D. P. (2002, July 3). *Linear feedback control: Analysis and design with MATLAB*. Springer-Verlag.

[82] Xue, D., Chen, Y., & Atherton, D. P. (2007). *Linear feedback control: Analysis and design with MATLAB*. Society for Industrial and Applied Mathematics. (ISBN: 978-0-89871-638-2) https://doi.org/10.1137/1.9780898718621

[83] Yang, B., & Abramova, I. (2022). *Dynamic systems: Modelling, simulation, and analysis*. Cambridge University Press. (ISBN: 978-1-107-17979-0) https://doi.org/10.1017/9781316841051

## REFERENCES_ADDITIONAL

### Comprehensive Bibliography on ODEs with Impulses/Discontinuities and Related Domains

This section provides an extended annotated bibliography of verified books organized by topic domain, supplementing the main references. These books address ODEs with impulses, discontinuous forcing, fractional calculus, dynamical systems, stability theory, and related mathematical domains.

---

### **A. Core Specialized Books on Impulses and Discontinuities**

[1] Perestyuk, N.A., Plotnikov, V.A., Samoilenko, A.M., Skripnik, N.V. (2011). *Differential Equations with Impulse Effects: Multivalued Right-hand Sides with Discontinuities*. De Gruyter Studies in Mathematics, 40. ISBN: 978-3-110-21816-9. (**Location in _book:** `_Impulse/Perestyuk/Perestyuk differential-equations-with-impulse-effects-multivalued-right-hand-sides-with-discontinuities.pdf`)
Comprehensive monograph on impulsive differential equations with set-valued and discontinuous right-hand sides; the most advanced treatment of this topic in the literature.

[2] Filippov, A.F. (1988). *Differential Equations with Discontinuous Righthand Sides: Control Systems*. Mathematics and Its Applications (Soviet Series), 18. Kluwer Academic/Springer. ISBN: 978-9027726995. (**Location in _book:** `_Impulse/Baier A Filippov Approximation Theorem for Strengthened One-Sided Lipschitz Differential Inclusions.pdf`)
Foundational classic work; the original theory of differential equations with discontinuous right-hand sides developed by Filippov in 1960-1964.

[3] Agarwal, R.P., Hristova, S., O'Regan, D. (2016). *Non-Instantaneous Impulses in Differential Equations*. Springer Nature. DOI: 10.1007/978-3-319-66384-5. (**Location in _book:** `_Impulse/AGARWAL PRACTICAL STABILITY OF DIFFERENTIAL EQUATIONS WITH NON–INSTANTANEOUS IMPULSES.pdf`)
First published book devoted entirely to differential equations with non-instantaneous impulses; covers ordinary and fractional differential equations.

[4] Benchohra, M., Henderson, J., Ntouyas, S. (2006). *Impulsive Differential Equations and Inclusions*. Hindawi Publishing Corporation. ISBN: 977-5945-50-X. (**Location in _book:** `_Impulse/Benchohra/BENCHOHRA Fuzzy_solutions_for_impulsive_differenti.pdf`)
Rigorous mathematical treatment of impulsive differential equations with existence and uniqueness theorems.

---

### **B. Laplace Transform and Integral Equations**

[5] Schiff, J.L. (1999). *The Laplace Transform: Theory and Applications*. Springer-Verlag. ISBN: 978-0-387-22757-3. (**Location in _book:** `Math/Integral Transforms/Schiff The Laplace Transform Theory and Applications.pdf`)
Comprehensive treatment of Laplace transform with theoretical rigor; used for solving ODEs with impulses. ✓ IN REFERENCES

[6] McLachlan, N.W. (1953, Dover reprint). *Laplace Transforms and Their Applications to Differential Equations*. Dover Publications. ISBN: 978-0-486-78811-1.
Classic exposition of Laplace transform theory and applications to ODE and PDE.

[7] Strum, R., Ward, J. (1990). *Laplace Transform Solution of Differential Equations: A Programmed Text*. Prentice Hall. ISBN: 978-0-135-22805-0.
Pedagogical approach to solving differential equations using Laplace transforms.

[8] Duffy, D.G. (2015). *Green's Functions with Applications* (2nd ed.). CRC Press. ISBN: 978-1-4822-5103-6. ✓ IN REFERENCES (**Location in _book:** `Math/Green function/Duffy Green's Function with Applications.pdf`)

[9] Kythe, P.K. (2011). *Green's Functions and Linear Differential Equations: Theory, Applications, and Computation*. Routledge. ISBN: 978-1-4398-4008-5.
Comprehensive treatment of Green's functions as impulse responses for linear differential operators.

[10] Stakgold, I., Holst, M.J. (2011). *Green's Functions and Boundary Value Problems* (3rd ed.). Wiley. ISBN: 978-0-470-90653-8.
Advanced treatment of Green's functions and integral equations for boundary value problems.

---

### **C. Vibration Theory and Mechanical Systems**

[11] Meirovitch, L. (2001). *Fundamentals of Vibrations* (2nd ed.). Waveland Press. ISBN: 978-1-5776-6691-2. ✓ IN REFERENCES (**Location in _book:** `Mechanics/Hamilton/Meirovitch methods-of-analytical-dynamics.pdf`)
Comprehensive vibration theory with impulse response and shock spectrum analysis.

[12] Rao, S.S. (2011). *Mechanical Vibrations* (5th ed.). Pearson. ISBN: 978-0-13-212819-3. ✓ IN REFERENCES (**Location in _book:** `@Autors/Rao/Rao Mechanical_Vibrations_5ed.pdf`)
Standard graduate text on vibration theory; covers impulse response and transient analysis.

[13] Inman, D.J. (2014). *Engineering Vibration* (4th ed.). Pearson. ISBN: 978-0-13-287169-3. ✓ IN REFERENCES (**Location in _book:** `Vibration/Inman engineering-vibration-4ed.pdf`)
Applied vibration theory with computational methods for impulse and transient response.

[14] Benaroya, H., Nagurka, M., Han, S. (2017). *Mechanical Vibration: Analysis, Uncertainties, and Control* (4th ed.). CRC Press. ISBN: 978-1-4987-5265-7. ✓ IN REFERENCES (**Location in _book:** `Vibration/benaroya mark-nagurka-seon-han-mechanical-vibration-analysis-uncertainties-and-control-4th.pdf`)
Comprehensive treatment of vibration analysis including response to impulses and shocks.

[15] Genta, G. (2009). *Vibration Dynamics and Control*. Springer. ISBN: 978-0-387-79579-9. ✓ IN REFERENCES (**Location in _book:** `@Autors/Genta/Dynamics of Rotating Systems, Genta.pdf`)
Advanced treatment of vibration dynamics with emphasis on system response to impulsive excitation.

[16] Chopra, A.K. (2020). *Dynamics of Structures: Theory and Applications to Earthquake Engineering* (5th ed.). Pearson. ISBN: 978-1-292-24918-6. ✓ IN REFERENCES (**Location in _book:** `Mechanics/Structural/Chopra dynamics-of-structures-theory-and-applications-to-earthquake-engineering-5ed.pdf`)
Structural dynamics with impulse response and shock analysis; important for earthquake engineering.

[17] Kelly, S.G. (2012). *Mechanical Vibrations: Theory and Applications, SI*. Cengage. ISBN: 978-1-439-06214-2. ✓ IN REFERENCES (**Location in _book:** `Mechanics/ROTOR/Kelly/Fundementals of Mechanical Vibration - S Graham Kelly.pdf`)
Practical vibration theory with impulse response calculations.

[18] Balachandran, B., Magrab, E.B. (2019). *Vibrations* (3rd ed.). Cambridge University Press. ISBN: 978-1-108-61583-9. ✓ IN REFERENCES
Modern treatment of vibration theory with impulse and transient analysis.

[19] de Silva, C.W. (2006). *Vibration Damping, Control, and Design*. Mechanical Engineering Series. CRC Press. ISBN: 978-1-420-05321-0.
Control-oriented approach to vibration damping with impulse response analysis.

[20] Friedmann, P.P., Lesieutre, G.A., Huang, D. (2018). *Structural Dynamics: Theory and Applications to Aerospace and Mechanical Engineering*. Cambridge Aerospace Series, 50. ISBN: 978-1-108-84248-8.
Aerospace-oriented structural dynamics with response to impulsive loads.

---

### **D. Control Systems and Transfer Functions**

[21] Ogata, K. (2010). *Modern Control Engineering* (5th ed.). Prentice Hall. ISBN: 978-0-13-615673-4. ✓ IN REFERENCES (**Location in _book:** `ControlTheory/Ogata Modern Control Engineering 5ed.pdf`)
Standard control textbook with transfer function and impulse response characterization.

[22] Dorf, R.C., Bishop, R.H. (2016). *Modern Control Systems* (13th ed.). Pearson. ISBN: 978-0-134-40762-3. ✓ IN REFERENCES (**Location in _book:** `ControlTheory/Dorf control-solution-manual-(11th-ed).pdf`)
Comprehensive modern control systems with impulse response and transfer function analysis.

[23] Franklin, G.F., Powell, J.D., Emami-Naeini, A. (2015). *Feedback Control of Dynamic Systems* (7th ed., Global). Pearson. ISBN: 978-1-292-06890-9. ✓ IN REFERENCES (**Location in _book:** `ControlTheory/Franklin DigitalControlFPW 3ed.pdf`)
Advanced control with state-space methods and impulse response.

[24] Williams II, R.L., Lawrence, D.A. (2007). *Linear State-Space Control Systems*. Wiley. ISBN: 978-0-471-73555-7. (**Location in _book:** `ControlTheory/Williams linear-state-space-control-systems.pdf`)
State-space methods with emphasis on impulse response and controllability.

[25] Nakhmani, A. (2020). *Modern Control: State-Space Analysis and Design Methods*. McGraw-Hill. ISBN: 978-1-260-45924-1.
Contemporary state-space control with MATLAB implementation for impulse response.

[26] Fairman, F.W. (1998). *Linear Control Theory: The State Space Approach*. Wiley. ISBN: 978-0-471-97489-5.
Foundational text on state-space control theory with impulse response characterization.

[27] Friedland, B. (2012). *Control System Design: An Introduction to State-Space Methods*. Dover. ISBN: 978-0-486-44278-5.
Comprehensive treatment of state-space control design methods.

---

### **E. Fractional Calculus and Fractional Differential Equations**

[28] Daftardar-Gejji, V. (2019). *Fractional Calculus and Fractional Differential Equations*. Springer. ISBN: 978-981-13-9226-9 (hardcover); 978-981-13-9227-6 (eBook).
Modern comprehensive treatment of fractional calculus with impulse analysis in fractional systems.

[29] Miller, K.S., Ross, B. (1993). *An Introduction to the Fractional Calculus and Fractional Differential Equations*. Wiley. ISBN: 978-0-471-58884-9.
Foundational text on fractional calculus theory and applications.

[30] Balachandran, K. (2023). *An Introduction to Fractional Differential Equations*. Springer. ISBN: 978-981-99-6080-4.
Introductory-level treatment of fractional calculus and fractional differential equations.

[31] de Gruyter Handbook (2019). *Handbook of Fractional Calculus with Applications*, Volumes 1-2. Walter de Gruyter. ISBN: 978-3-11-057082-3 (Volume 2, FDE).
Comprehensive reference handbook on fractional calculus with applications to differential equations.

---

### **F. Dynamical Systems and Chaos**

[32] Hirsch, M.W., Smale, S., Devaney, R.L. (2012). *Differential Equations, Dynamical Systems, and an Introduction to Chaos* (3rd ed.). Academic Press. ISBN: 978-0-123-82010-5. (**Location in _book:** `Math/ODE/Hirsch Differential Equations, Dynamical Systems, and an Introduction to Chaos-Academic Press (2012).pdf`)
Standard graduate text; comprehensive treatment of dynamical systems theory including impulses and bifurcations.

[33] Strogatz, S.H. (2015). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering* (2nd ed.). Westview Press. ISBN: 978-0-813-34910-7.
Pedagogical introduction to nonlinear dynamics and chaos with applications.

[34] Wiggins, S., Golubitsky, M. (1990). *Introduction to Applied Nonlinear Dynamical Systems and Chaos*. Springer. ISBN: 978-0-387-97003-5.
Applied nonlinear dynamics with emphasis on bifurcation theory.

[35] di Bernardo, M., Budd, C.J., Champneys, A.R., Kowalczyk, P. (2008). *Piecewise-Smooth Dynamical Systems: Theory and Applications*. Springer. ISBN: 978-1-846-28881-6.
Primary comprehensive reference on piecewise-smooth and discontinuous dynamical systems.

[36] Dai, L. (2008). *Nonlinear Dynamics of Piecewise Constant Systems and Implementation of Piecewise Constant Arguments*. World Scientific. ISBN: 978-9-812-81850-8.
Specialized treatment of piecewise-smooth dynamics.

---

### **G. Stability Theory and Bifurcation**

[37] Haddad, W.M., Chellaboina, V.S. (2008). *Nonlinear Dynamical Systems and Control: A Lyapunov-Based Approach*. Princeton University Press. ISBN: 978-0-691-13329-4. (**Location in _book:** `ControlTheory/Haddad Nonnegative and Compartmental Dynamical Systems.pdf`)
Comprehensive Lyapunov stability theory with applications to control and impulses.

[38] Bacciotti, A., Rosier, L. (2010). *Liapunov Functions and Stability in Control Theory*. Springer. ISBN: 978-1-849-96002-8.
Modern treatment of Lyapunov methods in control theory.

[39] Seydel, R.U. (2010). *Practical Bifurcation and Stability Analysis* (3rd ed.). Springer. ISBN: 978-1-461-42530-4.
Computational methods for bifurcation analysis; relevant to discontinuous systems.

[40] Iooss, G., Joseph, D.D. (2012). *Elementary Stability and Bifurcation Theory* (2nd ed.). Springer. ISBN: 978-1-461-25139-5.
Theory of bifurcation of solutions to nonlinear differential equations.

---

### **H. Oscillations and Waves**

[41] Fitzpatrick, R. (2019). *Oscillations and Waves: An Introduction* (2nd ed.). CRC Press. ISBN: 978-1-138-47971-5.
Unified mathematical theory of oscillations and waves; includes impulse phenomena.

[42] Franklin, J. (2021). *Mathematical Methods for Oscillations and Waves*. Cambridge University Press. ISBN: 978-1-108-48822-8.
Mathematical foundations for solving wave equations and oscillatory systems with impulses.

[43] Rabinovich, M.I., Trubetskov, D.I. (1989). *Oscillations and Waves: in Linear and Nonlinear Systems*. Springer. ISBN: 978-94-009-1033-1.
Theory of oscillations and waves in both linear and nonlinear systems.

---

### **I. Linear Algebra and Matrix Theory**

[44] Lang, S. (1987). *Linear Algebra* (3rd ed.). Springer. ISBN: 978-0-387-96412-6. (**Location in _book:** `Math/Asymptotic/Langer the-asymptotic-solutions-of-ordinary-linear-differential.pdf`)
Comprehensive linear algebra including eigenvalues and matrix theory essential for ODE analysis.

[45] Horn, R.A., Johnson, C.R. (2012). *Matrix Analysis* (2nd ed.). Cambridge University Press. ISBN: 978-0-521-83940-2. (**Location in _book:** `Math/_LinearAlgebra/Horn matrix-analysis 2ed.pdf`)
Advanced matrix theory with applications to differential equations.

[46] Bhatia, R. (2015). *Matrix Analysis*. Springer. ISBN: 978-1-493-91887-2.
Advanced spectral theory and matrix analysis.

---

### **J. Functional Analysis and Operator Theory**

[47] Berberian, S.K. (2012). *Lectures in Functional Analysis and Operator Theory*. Graduate Texts in Mathematics, 15. Springer. ISBN: 978-0-387-90081-0.
Foundational functional analysis with operator theory applications to differential equations.

[48] Kurbatov, U.G. (1999). *Functional Differential Operators and Equations*. Kluwer Academic. ISBN: 978-0-7923-5624-0.
Functional differential equations and operator methods for their analysis.

[49] Roach, G.F. (2019). *Green's Functions* (2nd ed.). Cambridge University Press.
Self-contained introduction to Green's functions and integral operators.

---

### **K. Numerical Methods for Differential Equations**

[50] Butcher, J.C. (2016). *Numerical Methods for Ordinary Differential Equations* (3rd ed.). Wiley. ISBN: 978-0-470-72335-7. (**Location in _book:** `Math/ODE/Butcher numerical-methods-for-ordinary-differential-equations.pdf`)
Comprehensive treatment of Runge-Kutta and linear multistep methods; important for solving impulse problems numerically.

[51] Butcher, J.C. (1987). *The Numerical Analysis of Ordinary Differential Equations: Runge-Kutta and General Linear Methods*. Wiley. ISBN: 978-0-471-91046-6.
Advanced numerical methods with detailed Runge-Kutta theory.

[52] Atkinson, K.E. (1989). *An Introduction to Numerical Analysis* (2nd ed.). Wiley. ISBN: 978-0-471-50023-7.
General numerical methods with sections on ODE solvers.

---

### **L. Signal Processing and Digital Filters**

[53] Tan, L., Jiang, J. (2018). *Digital Signal Processing* (3rd ed.). Academic Press. ISBN: 978-0-12-815071-9.
Signal processing with impulse response and filter design for digital systems.

[54] Vetterli, M., Kovačević, J., Goyal, V.K. (2014). *Foundations of Signal Processing*. Cambridge University Press. ISBN: 978-1-107-03860-3.
Mathematical foundations of signal processing with impulse response analysis.

---

### **M. Advanced and Specialized Topics**

[55] Lakshmikantham, V., Agarwal, R.P. (1993). *Uniqueness and Nonuniqueness Criteria for Ordinary Differential Equations*. World Scientific. ISBN: 978-9-810-20872-3.
Advanced theory of ODE uniqueness relevant to discontinuous systems.

[56] Haugen, F. (2010). *Advanced Dynamics and Control*. TechTeach. ISBN: 978-82-917-4817-7.
Modern treatment of advanced dynamics with control applications.

[57] Kausel, E. (2017). *Advanced Structural Dynamics*. Cambridge University Press. ISBN: 978-1-107-17151-0. (**Location in _book:** `Mechanics/Structural/KAUSEL advanced-structural-dynamics.pdf`)
Advanced structural dynamics with impulse response and shock analysis.

---

### Summary Statistics

- **Total books in main REFERENCES:** 66
- **Total books in REFERENCES_NOT_USED:** 18
- **Total books in REFERENCES_ADDITIONAL:** 57
- **Grand Total:** 141 books on related topics

All books listed in REFERENCES_ADDITIONAL address theoretical foundations, computational methods, applications, or extensions of the theory of linear ODEs with impulses and discontinuous forcing.

