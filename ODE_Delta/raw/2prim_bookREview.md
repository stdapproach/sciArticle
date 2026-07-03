### 2.2 Literature review: equivalence through initial condition modification

Several textbooks provide analytical solutions for LTI ODEs with a Dirac delta forcing function. Examples include Finan (p. 57), Nagy (pp. 189–190), Ogata (p. 190), Oliveira and Cortes (p. 3), Rao (p. 381), and Zill (p. 293).

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

Kelly (p. 315) observes

$
\begin{cases}
m x'' + c x' + k x = \delta(t), \\
x(0) = 0, \\
x'(0) = 0
\end{cases}
\;\equiv\;
\begin{cases}
m x'' + c x' + k x = 0, \\
x(0) = 0, \\
x'(0) = 1/m
\end{cases}
$

Balachandran (pp. 287–288), Beards (p. 66), Bottega (pp. 235–236), Genta (p. 179), Meirovitch (pp. 160–161), Schiff (p. 83) and Schmitz (p. 118) all remark that

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

The above examples suggest a general pattern (though a formal proof appears to be missing in the literature): an IVP forced by a delta function may be equivalent to a homogeneous IVP with a shifted initial condition. Specifically, for an $n$-th order system one might conjecture

$$
\begin{cases}
L_n(\{a\}, y) = b \delta(t) \\[2pt]
IC|_{t_0} = \mathbf{IC}_0
\end{cases}
\;\equiv\;
\begin{cases}
L_n(\{a\}, y) = 0 \\[2pt]
IC|_{t_0} = \mathbf{IC}_0 + \bigl(0,0,\ldots, b/a_0\bigr)^{\!T}
\end{cases}
\tag{2.7}
$$

### 2.3 Detailed literature classification

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
