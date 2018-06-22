#Examples
#####Example1 [Ogata, p.190]
$$\begin{cases}
Ty'+y=\delta(t),\\
y(0)=0
\end{cases}$$
Solution:
$$y(t)=\frac{1}{T}e^{-t/T}
$$
#####Example2 [Finan, p.57]
$$\begin{cases}
2y''+4y'+10y=\delta(t),\\
y_0=y(0)=0\\
y_1=y'(0)=0
\end{cases}
$$
Solution:
$$
x(t)=\frac{1}{4}e^{-2t}sin(2t)
$$
#####Example3 [Nagy, p.189]
$$\begin{cases}
y''+2y'+2y=\delta(t),\\
y(0)=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=e^{-t}sin(t)
$$
#####Example4 [Nagy, p.189]
$$\begin{cases}
y''+2y'+2y=\delta(t-a),\\
y(0)=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=H(t-a)e^{-(t-a)}sin(t-a)
$$
#####Example5 [Zill, p.293]
$$
\begin{cases}
y''+y=4\delta(t-2\pi),\\
y_0=y(0)=0\\
y_1=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=\begin{cases}
0, &0\le t <2\pi \\
4sin(t), & t\ge2\pi
\end{cases}
$$
#####Example6 [Zill, p.293]
$$\begin{cases}
y''+y=4\delta(t-2\pi),\\
y_0=y(0)=1\\
y_1=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=cos(t)+4H(t,2\pi)sin(t)
$$
#####Example7 [Nagy p.190]
$$\begin{cases}
y''+4y=\delta(t-\pi)-\delta(t-2\pi),\\
y(0)=y'(0)=0
\end{cases}$$
Solution:
$$y(t)=\frac{1}{2}\left[H(t-\pi)-H(t-2\pi)\right]
$$
#####Example8 [Dawkins, p.234]
$$\begin{cases}
y''+2y'-15y=6\delta(t-9),\\
y_0=y(0)=-5\\
y_1=y'(0)=7
\end{cases}
$$
Solution:
$$
f(t)=\frac{1}{8}e^{3t}-\frac{1}{8}e^{-5t},\text{ }g(t)=\frac{9}{4}e^{3t}+\frac{11}{4}e^{-5t}\\
y(t)=6H(t,9)f(t-9)-g(t)
$$

