
####2.3 Determinants

Examples of det: Lay p.165, Beezer p.395.

Geometrically, Determinant of matrix (denoted as $det(A)$ or $\Delta(A)$) can be viewed as the volume scaling factor of the linear transformation described by the matrix. This is also the signed volume of the n-dimensional parallelepiped spanned by the column or row vectors of the matrix (https://en.wikipedia.org/wiki/Determinant). To cut the story off: Determinant is a digit describing particular square matrix. Whether determinant isn't null there is inverse matrix for orignal one.

There are a lot of tutorial regarding Determinants:
* Agarwal, p.92
* Beezer, p.389, p.402
* Dawkins, p.251
* Karris, C-9
* Kelly, p.834
* Lay, p.162
* Logan, p.716
* Nagy, p.314
* Ogata, p.874
* Paraskevopoulos, p.50
* Rao, p.1043
* Riley, p.259
* Saad, p.2
* Sen, p.324
* Skogestad, p.533
* Underdown, p.58
* Weber, p.159
* Williams, p.412
* Zill, Appendix II
* Derivatives of Determinant: Petersen pp.6, 8, 10.

Proof following statement:
$$
det(A^n)=det(A)\space \text{[Beezer, p.397], which is probably incorrrect}
$$

Petersen (p.6, p.8 and p.10) provides interesting formulae regarding determinant:
$$
det(A)=\prod_i\lambda_i, \lambda_i=eig(A), \text{eigenvalue}\\
det(cA_{n\times n})=c^ndet(A)\\
det(A^{\intercal})=det(A)\\
det(AB)=det(A)det(B)\\
det(A^{-1})=1/det(A)\\
det(A^n)=(det(A))^n\\
det(I+\{u\}\{v\}^{\intercal})=1+\{u\}^{\intercal}\{v\}\\
\frac{\partial det(Y)}{\partial x}=det(Y)Tr(Y^{-1}\frac{\partial Y}{\partial x})\\
\frac{\partial det(X^{-1})}{\partial X}=-det(X^{-1})(X^{-1})^{\intercal}
$$


#####Example 8 [Lay, p.165]
$$
A=\left[
    \begin{matrix}
    1 & 5 & 0 \\
    2 & 4 & -1 \\
    0 & -2 & 0 \\
    \end{matrix}\right]
$$
According to the source [Lay, p.95], $det(A)=-2$

Script la_ex8.py delivers following output:
$$
\mathtt { \text{
det= -1.9999999999999998 
 testVal= -2}<br>\\
 {
delta= 2.220446049250313e-16
}}
$$

#####Example 9 [Beezer, p.395]
$$
A=\left[
    \begin{matrix}
    3 & 2 & -1 \\
    4 & 1 & 6 \\
    -3 & -1 & 2 \\
    \end{matrix}\right], \space det(A)=-27
$$

