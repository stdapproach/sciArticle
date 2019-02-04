#Apendix B
## Examples
#####Example1 [Oliveira and Cortes, p.3]
$$
\begin{cases}
y''+ay'=\delta(t),\\
y(0)=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=\frac{1}{a}(1-e^{-at})
$$
#####Example2 [Finan, pp.57-58]
$$\begin{cases}
2y''+4y'+10y=\delta(t),\\
y_0=y(0)=0\\
y_1=y'(0)=0
\end{cases}
$$
Solution (! there was a typo at original book, here's the proper formula which we've checked by MathCad14 and WolframAlfa!):
$$
y(t)=\frac{1}{4}e^{-t}sin(2t)
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
y''+2y'+2y=\delta(t-c),\\
y(0)=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=H(t-c)e^{-(t-c)}sin(t-c)
$$
#####Example5 [Chasnov, p.65]
$$\begin{cases}
2y''+y'+2y=\delta(t-5),\\
y(0)=y'(0)=0
\end{cases}
$$
Solution:
$$
y(t)=\frac{2}{\sqrt{15}}H(t-5)e^{-(t-5)/4}sin(\sqrt{15}(t-5)/4)
$$
#####Example6 [Zill, p.293]
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
#####Example7 [Zill, p.293]
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
#####Example8 [Nagy p.190]
$$\begin{cases}
y''+4y=\delta(t-\pi)-\delta(t-2\pi),\\
y(0)=y'(0)=0
\end{cases}$$
Solution:
$$y(t)=\frac{1}{2}\left[H(t-\pi)-H(t-2\pi)\right]sin(2t)
$$
#####Example9
$$\begin{cases}
y'''+2y''+2y=\delta(t),\\
y(0)=y'(0)=y''(0)=0
\end{cases}$$

Solution, getting from WolframAlfa
$$
y(t)=\frac{1}{2}-\frac{1}{2}e^{-t}\left(sin(t)+cos(t)\right)
$$

#####Example10 [Ogata p.163]
$$ C(s)=\frac{1}{Ts+1} $$
Impulse Response:
$$g(t)=\frac{1}{T}e^{-t/T}$$

#####Example11 [Xue p.380]
$$
L^{-1}\left\{\frac{s}{(s+a)(s+b)}\right\}=\frac{1}{a-b}\left[ae^{-at}-be^{-bt}\right]
$$
#####Example12 [Xue p.380]
$$
L^{-1}\left\{\frac{s+d}{(s+a)(s+b)}\right\}=\frac{1}{b-a}\left[(d-a)e^{-at}-(d-b)e^{-bt}\right]
$$
#####Example13 [Xue p.380]
$$
L^{-1}\left\{\frac{s+d}{s(s+a)(s+b)}\right\}=\frac{1}{ab}\left[d-\frac{b(d-a)}{b-a}e^{-at}+\frac{a(d-b)}{b-a}e^{-bt}\right]
$$
#####Example14 [Xue p.380]
$$
L^{-1}\left\{\frac{s+a}{s^2+\omega^2}\right\}=\frac{\sqrt{a^2+\omega^2}}{\omega}sin(\omega t+tan^{-1}(\frac{\omega}{a}))
$$