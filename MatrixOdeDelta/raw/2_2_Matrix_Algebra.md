
####2.2 Matrix Algebra
Square matrix with n rows and n cols could be denoted as follow:
$$
[A]\\
    n\times n
$$

For square matrix with the same size following opeartion are defined:
$$
A+B \space (A+B = B+A, \text{why?}),\\
AB \space(AB \ne BA, \text{why?}),\\
aB =Ba
$$
where $A, B$ are matrises ($n\times n$), $a$ - scalar.

There are a lot of tutorial regarding Matrix Algebra:
* Balachandran, p.676
* Beezer, p.125
* Dukkipati, p.37
* Golub, p.2
* Karris, Appendix C
* Kelly, p.835
* Kwon, p.4
* Laub, p.3
* Lay, p.92
* Logan, p.709
* Luenberger, p.56
* Nagy, p.308
* Meirovich, p.770
* Rao, p.1046
* Riley, p.250
* Sen, p.325
* Shmaliy, p.594
* Weber, p.175
* Williams, p.409
* Zill, Appendix II
* https://en.wikipedia.org/wiki/Matrix_(mathematics)

#####Example 4 [Lay, p.95]
$$
A=\left[
    \begin{matrix}
    2 & 3 \\
    1 & -5 \\
    \end{matrix}\right],\space
B=\left[
    \begin{matrix}
    4 & 3 & 6\\
    1 & -2 & 3 \\
    \end{matrix}\right]
$$

According to the source [Lay, p.95]:
$$
[A]\cdot [B]=\left[
    \begin{matrix}
    11 & 0 & 21 \\
    -1 & 13 & -9 \\
    \end{matrix}\right],\space
$$

Script la_ex4.py delivers following output:
$$
\mathtt { \text{
x= [[11  0 21]
 [-1 13 -9]] 
 testVal= [[11  0 21]
 [-1 13 -9]]}\\
{delta= [[0 0 0]
 [0 0 0]]
}}
$$

#####Example 5 [Beezer, p.192]
$$
A=\left[
    \begin{matrix}
    2 & -3 & 4 \\
    1 & 0 & -7 \\
    \end{matrix}\right],\space
B=\left[
    \begin{matrix}
    6 & 2 & -4\\
    3 & 5 & 2 \\
    \end{matrix}\right]
$$
According to the source [Beezer, p.192]:
$$
[A] + [B]=\left[
    \begin{matrix}
    8 & -1 & 0 \\
    4 & 5 & -5 \\
    \end{matrix}\right],\space
$$

#####Matrix Inversion
There are a lot of tutorial regarding Inverse Matrix:
* Balachandran, p.677
* Beezer, p.223
* Dukkipati, p.38
* Josephs, p.40
* Kelly, p.837
* Lay, p.102
* Logan, p.718
* Luenberger, p.66
* Malham, p.71
* Meirovich, p.774
* Nagy, p.312
* Paraskevopoulos, p.51
* Petersen, p.17
* Rao, p.682
* Riley, p.263
* Sen, p.332
* Silva, 3-49
* Skogestad, p.532
* Underdown, p.57
* Weber, p.184
* Williams, p.414
* Derivatives of inverse: Petersen p.10
* https://en.wikipedia.org/wiki/Invertible_matrix

There are 2 special classes of square matrix:
Null matrix:
$$
[0]_{n \cdot n}=[\Omega]_{n \cdot n}=\left[
    \begin{matrix}
    0 & 0 & 0 &\cdots & 0 \\
     0 & 0 & 0 &\cdots & 0 \\
     0 & 0 & 0 &\cdots & 0 \\
    \vdots & \vdots & \vdots &\ddots & 0 \\
     0 & 0 & 0 &\cdots & 0 \\
    \end{matrix}\right]
$$

Identity matrix:
$$
[I]_{n \cdot n}=\left[
    \begin{matrix}
    1 & 0 & 0 &\cdots & 0 \\
     0 & 1 & 0 &\cdots & 0 \\
     0 & 0 & 1 &\cdots & 0 \\
    \vdots & \vdots & \vdots &\ddots & 0 \\
     0 & 0 & 0 &\cdots & 1 \\
    \end{matrix}\right]
$$

Obviously, 
$$[\Omega]_{n \cdot n} \cdot [A]_{n \cdot n}=[A]_{n \cdot n}
\cdot [\Omega]_{n \cdot n}=[\Omega]_{n \cdot n}\\
[I]_{n \cdot n} \cdot [A]_{n \cdot n}=[A]_{n \cdot n}
\cdot [I]_{n \cdot n}=[A]_{n \cdot n}
$$

Sometimes (when?) for $[A]_{n \cdot n}$ could be found inverse matrix $[A]^{-1}_{n \cdot n}$ which is delivers following equality:
$$
[A]_{n \cdot n} \cdot [A]^{-1}_{n \cdot n} = [I]_{n \cdot n}
$$
Shortly it could be written as: $[A][A]^{-1}=[I]$

Proof foloowing statements:
$$
([A]^{-1})^{-1}=[A]\\
([A][B])^{-1}=[B]^{-1}[A]^{-1}\\
([A]^{\intercal})^{-1}=([A]^{-1})^{\intercal}\\
[A]\{x\}=\{b\} \Rightarrow \{x\}=[A]^{-1}\{b\}
$$

Petersen (pp.18-19 and p.9) provides interesting formulae regarding matrix inversion:
$$
([A]+[U][B][V])^{-1}=[A]^{-1}-[A]^{-1}[U]([B]^{-1}+[V][A]^{-1}[U])^{-1}[V][A]^{-1}\\
([A]+\{b\}\{c\}^{\intercal})^{-1}=[A]^{-1}-\frac{[A]^{-1}\{b\}\{c\}^{\intercal}[A]^{-1}}{1+\{c\}^{\intercal}[A]^{-1}{b}}\\
([I]+[A]^{-1})^{-1}=[A]([A]+[I])^{-1}\\
[A]^{-1}+[B]^{-1}=[A]^{-1}([A]+[B])[B]^{-1}\\
([I]+[A][B])^{-1}=[I]-[A]([I]+[B][A])^{-1}[B]\\
([I]+[A][B])^{-1}A=[A]([I]+[B][A])^{-1}\\
\frac{\partial [Y]^{-1}}{\partial x}=-[Y]^{-1}\frac{\partial [Y]}{\partial x}[Y]^{-1}\\
\frac{\partial ([X]^{-1})_{k,l}}{\partial [X]_{i,j}}=-([X]^{-1})_{k,i}([X]^{-1})_{j,l}
$$

#####Example 6 [Lay, p.103]
$$
A=\left[
    \begin{matrix}
    2 & 5 \\
    -3 & -7 \\
    \end{matrix}\right],\space
C=\left[
    \begin{matrix}
    -7 & -5\\
    3 & 2 \\
    \end{matrix}\right]
$$
Need to be proven that $C=A^{-1}$

According to the source [Lay, p.103]:
$$
[A]\cdot [C]=\left[
    \begin{matrix}
    1 & 0 \\
    0 & 1 \\
    \end{matrix}\right],\space
$$
and

$$
[C]\cdot [A]=\left[
    \begin{matrix}
    1 & 0 \\
    0 & 1 \\
    \end{matrix}\right],\space
$$

Script la_ex6.py delivers following output:
$$
\mathtt { \text{
ac= [[1 0]
 [0 1]]
ca= [[1 0]
 [0 1]]
}}
$$

#####Example 7 [Malham, p.71]
$$
[A]=\left[
    \begin{matrix}
    1 & 1 & 3 \\
    2 & 1 & 1\\
    1 & 3 & 5\\
    \end{matrix}\right],\space
$$

According to the source [Malham, p.71]:
$$
[A]^{-1}=\left[
    \begin{matrix}
    1/4 & 1/2 & -1/4 \\
    -9/8 & 1/4 & 5/8\\
    5/8 & -1/4 & -1/8\\
    \end{matrix}\right],\space
$$

qq
qq
qq