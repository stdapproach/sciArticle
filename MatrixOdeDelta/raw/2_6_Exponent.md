
####2.6 Matrix exponent
The matrix exponential is a matrix function on square matrices analogous to the ordinary exponential function.
The exponential of $X$ ($n \times n$ real or complex matrix), denoted by $e^X$ or $exp(X)$, is the $n \times n$ matrix given by the power series
$$
e^A=\sum_{k=0}^{\infty}\frac{1}{k!}A^k=I+\sum_{k=1}^{\infty}\frac{A^k}{k!},
$$
where $A^0$ is defined to be the identity matrix $I$ with the same dimension as $A$ (https://en.wikipedia.org/wiki/Matrix_exponential).

This power series converges for any matrix $A$ [Agarwal, p.100].

Prove the following formulae [Petersen p.59]:
$$
e^{-A}=I-A+\frac{1}{2}A^2-\dots\\
e^{tA}=\sum_{k=0}^{\infty}\frac{1}{k!}(tA)^k=I+tA+\frac{1}{2}t^2A^2+\dots \\
ln(I+A)=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}A^k=A-\frac{1}{2}A^2+\frac{1}{3}A^3+\dots\\
e^Ae^B=e^{A+B}\space \text{ if }\space AB=BA\\
(e^A)^{-1}=e^{-A}\\
\frac{d}{dt}e^{tA}=Ae^{tA}=e^{tA}A,\space t\in \Bbb{R}\\
\frac{d}{dt}Tr(e^{tA})=e^{Tr(A)}\\
det(e^A)=e^{Tr(A)}
$$
Prove this one [Finan, p.125]
$$
e^{P^{-1}AP}=P^{-1}e^AP,
$$
for any invertible $n \times n$ matrix $P$ and any $n \times n$ matrix $A$.

The similar statement [Sen, p.393] is very useful for finding the solution of matrix differential equations. If $A=S\Lambda S^{-1}$
$$
e^{At}=S\cdot e^{\Lambda t}\cdot S^{-1}
$$

There are a lot of tutorial regarding matrix exponent: Astrem (p.136), Golub (p.530), Laub (pp.109-112), Sen (p.391). Especially we recommend Moler's and Van Loan's article "Nineteen Dubious Ways to Compute the Exponential of a Matrix, Twenty-Five Years Later" (SIAM REVIEW, Vol. 45, No. 1, pp. 3–000)

#####Example 40 [Moler, p.8]
$$
A=\left[\begin{matrix}
-49 & 24 \\
-64 & 31
\end{matrix}\right],\\
e^A=\left[\begin{matrix}
-0.735759 &  0.551819 \\
-1.471518 & 1.103638
\end{matrix}\right]
$$

Script la_ex40.py delivers following output:
$$
\mathtt { {
exp(A)= \text{[[-0.73575876  0.5518191 ]}\\
\text{ [-1.4715176   1.10363824]]}\\
delta= \text{[[2.41855256e-07 9.96580909e-08]}\\
\text{ [4.00911758e-07 2.40715559e-07]]}
}}
$$

#####Example 41 [Kwon, p.6]
$$
A=\left[\begin{matrix}
0.2190 & 0.6793 & 0.5194 \\
0.0470 & 0.9347 & 0.8310 \\
0.6789 & 0.3835 & 0.0346
\end{matrix}\right]
$$
Calculate matrix exponent and compare with book's result, Wolfram Alfa's result (https://www.wolframalpha.com/examples/mathematics/algebra/matrices/) and output of script la_ex41.py

qq
qq
qq

