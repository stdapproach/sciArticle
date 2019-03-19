
####2.4 Eigenvalues and Eigenvectors

Eigenvalues and Eigenvectors arise in many situations, for example: calculating the natural frequencies of oscillation of a vibrating system; finding principal axes of stress and strain; calculating oscillations of an electrical circuit; image processing; data mining (web search engines); etc. [Malham, p.75]

Geometrically, an eigenvector, corresponding to a real nonzero eigenvalue, points in a direction that is stretched by the (linear) transformation and the eigenvalue is the factor by which it is stretched. If the eigenvalue is negative, the direction is reversed (https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).

Algebraically, an eigenvector $v_i$ (which is non-null) and an eigenvalue $\lambda_i$ satisfied following equation:
$$
Av_i=\lambda v_i
$$

Eigenvalues of symmetric real matrix all are real, Eigenvalues of symmetric positive definite matrix are positive number (at Vibration theory this case corresponds to the fact that all eigen frequency are square root of eigenvalues).
Eigenvalues of skew-symmetric matrices (which arised at Vibration of rotor) could be complex value.

There are a lot of tutorial regarding Eigenvalues and Eigenvectors:
* Antsaklis, p.121
* Balachandran, p.369
* Beezer, p.415
* Blanchard, p.262
* Bottega, p.341
* Cook, p.120
* Garvan, p.207
* Genta, p.99
* Golub, p.347, p.439
* Hirsh, p.32, p.83, p.95, p.119
* Jack, 20.8
* Kelly, p.388
* Kwon, p.7
* Lay, p.265
* Luenberger, p.77
* Malham pp.75
* Meirovich, p.220, p.301, p.323
* Nagy, p.318
* Ogata, p.652
* Paraskevopoulus, p.51
* Petersen, p.30
* Preumont, p.18
* Rao, p.481, p.515, p.594, p.1006
* Riley, p.272
* Robinson, p.259, p.382
* Saad, p.237
* Sen, p.283
* Schmitz, p.136, p.153
* Skogestad, p.534
* Underdown, p.105
* Zill, p.201, p.312
* Derivatives of Eigenvalues: Petersen p.10

Algorithm solving Eigenvalues and Eigenvectors could be found at  [Wilkinson, p.303]


Proof following statement:
==

Petersen (p.10) provides interesting formulae regarding eigenvalue:
==
$$
\frac{\partial }{\partial X}\sum{eig(X)}=\frac{\partial }{\partial X}Tr(X)=I\\
\frac{\partial }{\partial X}\prod{eig(X)}=\frac{\partial }{\partial X}det(X)=det(X)X^{-T}\\
$$
For A is real and symmetric, $\lambda_i$ and $v_i$ are distinct eigenvalue and eigenvectors of A with $v_i^{\intercal}v_i=1$, then:
$$
\partial\lambda_i=v_i^{\intercal}\partial(A)v_i\\
\partial v_i=(\lambda_iI-A)^{+}\partial(A)v_i
$$

----Examples of:
* +Beezer p.416, pp.420-422, 423, 425, 428, 429 (complex Egenvalue), 431
* -Bottega p.341
* +Garvan, p.207
* +Genta, p.104, -108
* +Hirsh, p.31, p.85, p.97, p.98
* --Jack, 20.8
* +Kwon, p.7
* --Lay p.266, p.267, p.270
* +Malham p.77-81
* -Meirovich, p.221, p.301
* +Nagy, p.220, -222, -224
* Ogata, p.652--
* +Paraskevopoulus, p.52
* -Rao p.515, p.594
* +Riley, p.280, 282
* -Robinson, p.-262, 265, 266
* Sen, p.-285, 287, 288, 289, 291
* Underdown, p.106
* Zill p.313

#####Example [Beezer, p.416]
$$
A=\left[
    \begin{matrix}
    204 & 98 & -26 & -10 \\
    -280 & -134 & 36 & 14 \\
    716 & 348 & -90 & -36 \\
    -472 & -232 & 60 & 28
    \end{matrix}\right]
$$
Check these vectors are eigenvector:
$$
x=\left[
    \begin{matrix}
    1 \\
    -1 \\
    2 \\
    5
    \end{matrix}\right],\space
y=\left[\begin{matrix}
-3 \\
4 \\
-10 \\
4
\end{matrix}\right],\space
z=\left[\begin{matrix}
-3 \\
7 \\
0 \\
8
\end{matrix}\right],\space
w=\left[\begin{matrix}
1 \\
-1 \\
4 \\
0
\end{matrix}\right],\space
$$

#####Example [Beezer, p.423, 425]
$$
A=\left[
    \begin{matrix}
    -13 & -8 & -4 \\
    12 & 7 & 4 \\
    24 & 16 & 7 \\
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\lambda_1=3, v_1=\left[\begin{matrix}
1 \\
-1 \\
2
\end{matrix}\right],
\lambda_{2,3}=-1, v_{2,3}=\left[\begin{matrix}
-2 \\
3 \\
0
\end{matrix}\right],
\left[\begin{matrix}
-1 \\
0 \\
3
\end{matrix}\right]
$$

#####Example [Garvan, p.207]
$$
A=\left[
    \begin{matrix}
    177 & 77 & -28 \\
    -546 & -236 & 84 \\
    -364 & -154 & 51 \\
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\lambda_{1,2,3}=\left[\begin{matrix}
2 \\
-5 \\
-5
\end{matrix}\right],
V=\left[\begin{matrix}
1 & 1 & 0 \\
-3 & 0 & 1 \\
-2 & 13/2 & 11/4
\end{matrix}\right]
$$

#####Example [Genta, p.104]
$$
A=\left[
    \begin{matrix}
    20 & -10 & 0 \\
    -2.5 & 3.5 & -1 \\
    0 & -8 & 8 \\
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\lambda_{1,2,3}=\left[\begin{matrix}
1.0166 \\
3.0042 \\
4.6305
\end{matrix}\right],
V=\left[\begin{matrix}
0.45913 & 0.11677 & 1 \\
0.87081 & 0.12815 & -0.14412 \\
1 & -1 & 0.08578
\end{matrix}\right]
$$

#####Example [Hirsch, p.31]
$$
A=\left[
    \begin{matrix}
    1 & 3 \\
    1 & -1
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
2 \\
-2
\end{matrix}\right],
V=\left[\begin{matrix}
3 & 1 \\
1 & -1
\end{matrix}\right]
$$

#####Example [Hirsch, p.85]
$$
A=\left[
    \begin{matrix}
    1 & 2 & -1 \\
    0 & 3 & -2 \\
    0 & 2 & -2
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
2 \\ 1 \\ -1
\end{matrix}\right],
V=\left[\begin{matrix}
3 & 1 & 0 \\
2 & 0 & 1 \\
1 & 0 & 2
\end{matrix}\right]
$$

#####Example [Hirsch, p.97]
$$
A=\left[
    \begin{matrix}
    2 & 0 & -1 \\
    0 & 2 & 1 \\
    -1 & -1 & 2
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
2 \\ 2 \\ 2
\end{matrix}\right],
V=\left[\begin{matrix}
1 & 0 & 1 \\
-1 & 0 & 0 \\
0 & -1 & 0
\end{matrix}\right]
$$

#####Example [Kwon, p.7]
$$
A=\left[
    \begin{matrix}
    5 & 3 & 2 \\
    1 & 4 & 6 \\
    9 & 7 & 2
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
12.5361 \\ 1.7486 \\ -3.2847
\end{matrix}\right],
V=\left[\begin{matrix}
0.4127 & 0.5992 & 0.0459 \\
0.5557 & -0.7773 & -0.6388 \\
0.7217 & 0.1918 & 0.7680
\end{matrix}\right]
$$

#####Example [Malham, p.77]
$$
A=\left[
    \begin{matrix}
    3 & -2 \\
    4 & -3
    \end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
1 \\ -1
\end{matrix}\right],
V=\left[\begin{matrix}
1 & 1 \\
1 & 2
\end{matrix}\right]
$$

#####Example [Malham, p.77]
$$
A=\left[\begin{matrix}
2 & -2 & 2 \\
1 & 1 & 1 \\
1 & 3 & -1
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
-2 \\ 2 \\ 2
\end{matrix}\right],
V=\left[\begin{matrix}
-4/7 & 0 & ? \\
-1/7 & 1 & ? \\
1 & 1 & ?
\end{matrix}\right]
$$

#####Example [Malham, p.80]
$$
A=\left[\begin{matrix}
-2 & 2 & -3 \\
2 & 1 & -6 \\
-1 & -2 & 0
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
5 \\ -3 \\ -3
\end{matrix}\right],
V=\left[\begin{matrix}
-1 & 3 & -2 \\
-2 & 0 & 1 \\
1 & 1 & 0
\end{matrix}\right]
$$

#####Example [Nagy, p.220]
$$
A=\left[\begin{matrix}
1 & 2\\
2 & 1
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
3 \\ -1
\end{matrix}\right],
V=\left[\begin{matrix}
1 & -1 \\
1 & 1
\end{matrix}\right]
$$

#####Example [Paraskkevopoulos, p.52]
$$
A=\left[\begin{matrix}
-1 & 1\\
0 & -2
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
-1 \\ -2
\end{matrix}\right],
V=\left[\begin{matrix}
1 & -1 \\
0 & 1
\end{matrix}\right]
$$

#####Example [Riley, p.280]
$$
A=\left[\begin{matrix}
1 & 1 & 3 \\
1 & 1 & -3 \\
3 & -3 & -3
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
2 \\ 3 \\ -6
\end{matrix}\right],
V=\left[\begin{matrix}
1/\sqrt{2} & 1/\sqrt{3} & 1/\sqrt{6} \\
1/\sqrt{2} & -1/\sqrt{3} & -1/\sqrt{6} \\
0 & 1/\sqrt{3} & -2/\sqrt{6}
\end{matrix}\right]
$$

#####Example [Riley, p.282]
$$
A=\left[\begin{matrix}
1 & 0 & 3 \\
0 & -2 & 0 \\
3 & 0 & 1
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
4 \\ -2 \\ -2
\end{matrix}\right],
V=\left[\begin{matrix}
1/\sqrt{2} & 0 & -1/\sqrt{2} \\
0 & 1 & 0 \\
1/\sqrt{2} & 0 & 1/\sqrt{2}
\end{matrix}\right]
$$

#####Example [Sen, p.287]
$$
A=\left[\begin{matrix}
0 & -2 \\
2 & 0
\end{matrix}\right]\\
Find Eigenvalues and Eigenvectors\\
\Lambda=\left[\begin{matrix}
2i \\ -2i
\end{matrix}\right],
V=\left[\begin{matrix}
i & -i\\
1 & 1
\end{matrix}\right]
$$

qq
qq
qq
qq