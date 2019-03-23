
####2.5 Decomposition
In linear algebra, a matrix decomposition or matrix factorization is a factorization of matrix into product of matrices. Each kind of decompozition finds use amons a particular class of problems (https://en.wikipedia.org/wiki/Matrix_decomposition).

#####Singular Value Decomposition (SVD) [Petersen p.31]
Any $n\times m$ matrix $[A]$ can be written as
$$
A=UDV^{\intercal}
$$
where
$$
U=\text{eigenvectors of }AA^{\intercal}\space n\times n\\
D=\sqrt{diag(eig(AA^{\intercal}))}\space n\times m\\
V=\text{eigenvectors of }AA^{\intercal}\space m\times m
$$

#####Symmetric Square decomposed into squares [Petersen p.31]
Assume $[A]$ to be $n \times n$ and symmetric. Then
$$
[A]=[V][D][V^{\intercal}],
$$
where $[D]$ is diagonal with the eigenvalues of $[A]$, and $[V]$ is orthogonal and the eigenvectors of $[A]$ (https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix).

#####Square decomposed into squares [Petersen p.31]
Assume $A\in \Bbb{R}^{n \times n}$. Then
$$
[A]=[V][D][U^{\intercal}],
$$
where $[D]$ is diagonal with the square root of the eigenvalues of $[A][A^{\intercal}]$, $[V]$ is the eigenvectors of $[A][A^{\intercal}]$, and $[U]^{\intercal}$ is the eigenvectors of $[A^{\intercal}][A]$.

#####LU decomposition [Petersen p.32]
Assume $[A]$ is a symmetric positive definite square matrix, then
$$
[A]=[L][U]
$$
where $[U]$ is a unique upper triangular matrix and $[L]$ is a lower triangular matrix (https://en.wikipedia.org/wiki/LU_decomposition).

#####Cholesky-decomposition [Petersen p.32]
Assume $[A]$ is a symmetric positive definite square matrix, then
$$
[A]=[U]^{\intercal}[U]=[L][L]^{\intercal},
$$
where $[U]$ is a unique upper triangular matrix and $[L]$ is a lower triangular matrix (https://en.wikipedia.org/wiki/Cholesky_decomposition).

#####QR decomposition [https://en.wikipedia.org/wiki/QR_decomposition]
Any real $[A]$ is a square matrix (there is a more general version for rectangular matrix ) may be decomposed as
$$
[A]=[Q][R],
$$
where $[Q]$ is an orthogonal matrix and $[R]$ is an upper triangular matrix. If $[A]$ is invertible, then the factorization is unique if we require the diagonal elements of $[R]$ to be positive.

There are a lot of tutorial regarding matrix decomposition: Golub (p.76, 111, 246, 385, 486), Laub (p.35), Lay (p.123, 127, 359, 398, 406, 414, 420, 432), Petersen (p.28), Sen (p.362), Skogestat (p.79, 537), Wilkinson (contributions I.1, I.10, II.3, II.4, II.8)

Examples decomposition:
* SVD
	* Laub p.37
* LDU
	* Lay p.126, 418, 419
	* Sen p.363, 364, 366, 370, 374, 380, 381, 382, 384, 385
	* Skogestat p.81
* Cholesky
	* Sen p.366
* QR
	* Sen p.370, 371

#####Example 28 [Laub, p.37]
SVD decomposition
$$
A=\left[    \begin{matrix}
    1 & 1 \\
    2 & 2 \\
    1 & 2
\end{matrix}\right]=
\left[    \begin{matrix}
1/3 \\
2/3  \\
2/3
\end{matrix}\right]
3\sqrt{2}
\left[    \begin{matrix}
\sqrt{2}/2 & \sqrt{2}/2
\end{matrix}\right]
$$

#####Example 29 [Lay, p.418]
SVD decomposition
$$
A=\left[    \begin{matrix}
4 & 11 & 14 \\
8 & 7 & -2
\end{matrix}\right]
$$
$$
\begin{array}&
A=
&
\left[\begin{matrix}
3/\sqrt{10} & 1/\sqrt{10} \\
1/\sqrt{10} & -3/\sqrt{10}
\end{matrix}\right]
&
\left[\begin{matrix}
6/\sqrt{10} & 0 & 0 \\
0 & 3\sqrt{10} & 0
\end{matrix}\right]
&
\left[\begin{matrix}
1/3 & 2/3 & 2/3 \\
-2/3 & -1/3 & 2/3 \\
2/3 & -2/3 & 1/3
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} &  {\color{blue}\uparrow} & \\ & {\color{blue}U} & {\color{blue}\Sigma} & {\color{blue}{V^\intercal}} & \end{array}
$$

#####Example 30 [Lay, p.419]
SVD decomposition
$$
A=\left[    \begin{matrix}
1 & -1 \\
-2 & 2 \\
2 & -2
\end{matrix}\right]
$$
$$
\begin{array}&
A=
&
\left[\begin{matrix}
1/3 & 2/\sqrt{5} & -2/\sqrt{45} \\
-2/3 & 1/\sqrt{5} & 4/\sqrt{45} \\
2/3 & 0 & 5/\sqrt{45}
\end{matrix}\right]
&
\left[\begin{matrix}
3\sqrt{2} & 0 \\
0 & 0 \\
0 & 0
\end{matrix}\right]
&
\left[\begin{matrix}
1/\sqrt{2} & -1/\sqrt{2} \\
1/\sqrt{2} & 1/\sqrt{2}
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} &  {\color{blue}\uparrow} & \\ & {\color{blue}U} & {\color{blue}\Sigma} & {\color{blue}{V^\intercal}} & \end{array}
$$

#####Example 31 [Skogestad, p.81]
SVD decomposition
$$
A=\left[    \begin{matrix}
5 & 4 \\
3 & 2
\end{matrix}\right]
$$
$$
\begin{array}&
A=
&
\left[\begin{matrix}
0.872 & 0.490 \\
0.490 & -0.972
\end{matrix}\right]
&
\left[\begin{matrix}
7.343 & 0 \\
0 & 0.272
\end{matrix}\right]
&
\left[\begin{matrix}
0.794 & -0.608 \\
0.608 & 0.794
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} &  {\color{blue}\uparrow} & \\ & {\color{blue}U} & {\color{blue}\Sigma} & {\color{blue}{V^\intercal}} & \end{array}
$$

#####Example 32 [Lay, p.126]
LU factorization
$$
A=\left[    \begin{matrix}
    2 & 4 & -1 & 5 & -2 \\
    -4 & -5 & 3 & -8 & 1 \\
    2 & -5 & -4 & 1 & 8 \\
    -6 & 0 & 7 & -3 & 1
\end{matrix}\right]=
\left[    \begin{matrix}
    1 & 0 & 0 & 0 \\
    -2 & 1 & 0 & 0 \\
    1 & -3 & 1 & 0 \\
    -3 & 4 & 2 & 1
\end{matrix}\right]
\left[    \begin{matrix}
    2 & 4 & -1 & 5 & -2 \\
    0 & 3 & 1 & 2 & -3 \\
    0 & 0 & 0 & 2 & 1 \\
    0 & 0 & 0 & 0 & 5 \\
\end{matrix}\right]
$$

#####Example 33 [Sen, p.363]
LDU decomposition
$$
A=\left[    \begin{matrix}
-5 & 4 & 9 \\
-22 & 14 & 18 \\
16 & -8 & -6
\end{matrix}\right]
$$
$$
\begin{array}&
A=
&
\left[\begin{matrix}
1 & 0 & 0 \\
22/5 & 1 & 0 \\
-16/5 & -4/3 & 1
\end{matrix}\right]
&
\left[\begin{matrix}
-5 & 0 & 0 \\
0 & -18/5 & 0 \\
0 & 0 & -6
\end{matrix}\right]
&
\left[\begin{matrix}
1 & -4/5 & -9/5 \\
0 & 1 & 6 \\
0 & 0 & 1
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} &  {\color{blue}\uparrow} & \\ & {\color{blue}L} & {\color{blue}D} & {\color{blue}{U}} & \end{array}
$$

#####Example 34 [Sen, p.364]
LDU decomposition
$$
A=\left[    \begin{matrix}
0 & 1 & 2 \\
1 & 1 & 1 \\
1 & 0 & 0
\end{matrix}\right]
$$
$$
\begin{array}&
A=&
\left[\begin{matrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{matrix}\right]
&
\left[\begin{matrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{matrix}\right]
&
\left[\begin{matrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{matrix}\right]
&
\left[\begin{matrix}
1 & 0 & 0 \\
0 & 1 & 1 \\
0 & 0 & 1
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & {\color{blue}\uparrow} &  {\color{blue}\uparrow} & \\ & {\color{blue}{P^{-1}}} & {\color{blue}L} & {\color{blue}{D}} & {\color{blue}{U}}& \end{array}
$$

#####Example 35 [Sen, p.366]
Cholesky decomposition
$$
A=\left[    \begin{matrix}
5 & 4i \\
-4i & 5
\end{matrix}\right]
\\
\begin{array}&
A=U^{H}U=&
\left[\begin{matrix}
\sqrt{5} & 0 \\
-4i/\sqrt{5} & 3/\sqrt{5}
\end{matrix}\right]
&
\left[\begin{matrix}
\sqrt{5} & 4i/\sqrt{5} \\
0 & 3/\sqrt{5}
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & \\
& {\color{blue}{U^{H}}} & {\color{blue}U} & \end{array}
$$
Second option:
$$
\begin{array}&
A=\widehat{U}^{H}D\widehat{U}=&
\left[\begin{matrix}
1 & 0 \\
-4i/5 & 1
\end{matrix}\right]
&
\left[\begin{matrix}
5 & 0 \\
0 & 9/5
\end{matrix}\right]&
\left[\begin{matrix}
1 & 4i/5 \\
0 & 1
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & {\color{blue}\uparrow} \\
& {\color{blue}{\widehat{U}^{H}}} & {\color{blue}D} & {\color{blue}{\widehat{U}}} \end{array}
$$

#####Example 36 [Sen, p.370]
QR decomposition
$$
A=\left[    \begin{matrix}
-5 & 4 & 9 \\
-22 & 14 & 18 \\
16 & -8 & -6
\end{matrix}\right]
\\
\begin{array}&
A=Q \cdot R=&
\left[\begin{matrix}
-0.1808 & -0.4982 & 0.8480 \\
-0.7954 & -0.4331 & -0.4240 \\
0.5785 & -0.7512 & -0.3180
\end{matrix}\right]
&
\left[\begin{matrix}
27.6786 & -16.4867 & -19.4153 \\
0 & -2.0465 & -7.7722 \\
0 & 0 & -1.9080
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & \\
& {\color{blue}{Q}} & {\color{blue}R} & \end{array}
$$

#####Example 37 [Sen, p.370]
QR decomposition
$$
A=\left[    \begin{matrix}
2 & -3 & 2 \\
2 & 0 & 3
\end{matrix}\right]
\\
\begin{array}&
A=Q \cdot R=&
\left[\begin{matrix}
0.4472 & -0.8944 \\
0.8944 & 0.4472  \\
\end{matrix}\right]
&
\left[\begin{matrix}
2.2361 & -1.3416 & 3.577 \\
0 & 2.6833 & -0.4472
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & \\
& {\color{blue}{Q}} & {\color{blue}R} & \end{array}
$$

#####Example 39[Sen, p.370]
QR decomposition
$$
A=\left[    \begin{matrix}
0 & -1 \\
1 &-1
\end{matrix}\right]
\\
\begin{array}&
A=Q \cdot R=&
\left[\begin{matrix}
0 & -1 \\
1 & 0  \\
\end{matrix}\right]
&
\left[\begin{matrix}
1 & -1 \\
0 & 1
\end{matrix}\right]\\
& {\color{blue}\uparrow} & {\color{blue}\uparrow} & \\
& {\color{blue}{Q}} & {\color{blue}R} & \end{array}
$$

