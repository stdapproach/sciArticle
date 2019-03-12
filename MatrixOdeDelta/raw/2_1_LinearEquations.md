
####2.1 Linear Equations

Dealing with vibration analisys we often met the systems of linear equation with the amount of equations is the same as the amount of variables (unknown values). This systems could be written in the forms, which are equivalent:

$$
\begin{cases}
a_{11}x_1+a_{12}x_2+...+a_{1,n-1}x_{n-1}+a_{1n}x_n=b_1\\
a_{21}x_1+a_{22}x_2+...+a_{2,n-1}x_{n-1}+a_{2n}x_n=b_2\\
...\\
a_{n-1,1}x_1+a_{n-1,2}x_2+...+a_{n-1,n-1}x_{n-1}+a_{n-1,n}x_n=b_{n-1}\\
a_{n,1}x_1+a_{n,2}x_2+...+a_{n,n-1}x_{n-1}+a_{n,n}x_n=b_{n}
\end{cases}\tag{2.1.1}
$$

$$
[A]\{x\}=\{b\}\\
A=\left[
    \begin{matrix}
    a_{11} & a_{12} & a_{13} &\cdots & a_{1n} \\
    a_{21} & a_{22} & a_{23} &\cdots & a_{2n} \\
    a_{31} & a_{32} & a_{33} &\cdots & a_{33} \\
    \vdots & \vdots & \vdots &\ddots & 0 \\
    a_{n,1} & a_{n,2} & a_{n,3} &\cdots & a_{n,n} \\
    \end{matrix}\right],
    \{x\}=\left\{
    \begin{matrix} x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_{n-1}\\x_n\\ \end{matrix}
    \right\},
    \{b\}=\left\{
    \begin{matrix} b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_{n-1}\\b_n\\ \end{matrix}
    \right\}\tag{2.1.2}
$$

There are a lot of tutorial explaining how to solve such systems:
* Lay, p.4
* Malham, p.57
* Petersen, p.29 provides Cramer's rule (brilliant but useless thing)
* https://en.wikipedia.org/wiki/Linear_equation

#####Examples of linear equations
Examples for LE: 36Lay p.5; 41Malham p.58, 63;
#####Example 1 [Lay, p.5]
$$
\begin{cases}
x_1-2x_2+x_3=0\\
2x_2-8x_3=8 \\
-4x_1+5x_2+9x_3=-9
\end{cases}\tag{2.1.3}
$$

$$
\Rightarrow
A=\left[
    \begin{matrix}
    1 & -2 & 1 \\
    0 & 2 & -8 \\
    -4 & 5 & 9 \\
    \end{matrix}\right],
    \{x\}=\left\{
    \begin{matrix} x_1 \\ x_2 \\ x_3 \end{matrix}
    \right\},
    \{b\}=\left\{
    \begin{matrix} 0 \\ 8 \\ -9  \end{matrix}
    \right\}\\
    [A]\{x\}=\{b\}
    \tag{2.1.4}
$$

According to the source [Lay, p.6]:
$$
\begin{cases}
x_1=29\\
x_2=16\\
x_3=3
\end{cases}\tag{2.1.5}
$$

Script la_ex1.py delivers following output:
$$
\mathtt { \text{
x= [29. 16.  3.]  testVal= [29 16  3]
delta= [0. 0. 0.]
}}
$$

#####Example 2 [Malham, p.58]
$$
\begin{cases}
2x+3y-z=5\\
4x+4y-3z=3 \\
2x-3y+z=-1
\end{cases}
$$

According to the source [Malham, p.58]:
$$
\begin{cases}
x=1\\
y=2\\
z=3
\end{cases}
$$

#####Example 3 [Malham, p.62]
$$
\begin{cases}
3x+2y+z=3\\
2x+1y+z=0 \\
6x+2y+4z=6
\end{cases}
$$


