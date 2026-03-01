## Appendix B: Reference Examples

This appendix collects the analytical solutions used throughout the main text to verify the proposed method. Examples are numbered consistently with the verification sections.

### Type 0 Examples (Single Delta Function)

##### Example 1 [Oliveira and Cortes, p. 3]
$
\begin{cases}
y'' + a y' = \delta(t), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = \frac{1}{a}\bigl(1 - e^{-a t}\bigr)
$

##### Example 2 [Finan, pp. 57–58]
$
\begin{cases}
2y'' + 4y' + 10y = \delta(t), \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
$

**Solution:** The original book contains a typographical error; the correct formula (verified with Mathcad 14 and WolframAlpha) is
$
y(t) = \frac{1}{4} e^{-t} \sin(2t)
$

##### Example 3 [Nagy, p. 189]
$
\begin{cases}
y'' + 2y' + 2y = \delta(t), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = e^{-t} \sin(t)
$

##### Example 4 [Nagy, p. 189]
$
\begin{cases}
y'' + 2y' + 2y = \delta(t - c), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = H(t - c)\, e^{-(t - c)} \sin(t - c)
$

##### Example 5 [Chasnov, p. 65]
$
\begin{cases}
2y'' + y' + 2y = \delta(t - 5), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) = \frac{2}{\sqrt{15}}\, H(t - 5)\, e^{-(t - 5)/4} \sin\!\left(\frac{\sqrt{15}}{4}(t - 5)\right)
$

##### Example 6 [Zill, p. 293]
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 0,\; y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) =
\begin{cases}
0, & 0 \le t < 2\pi \\[4pt]
4\sin(t), & t \ge 2\pi
\end{cases}
$

##### Example 7 [Zill, p. 293]
$
\begin{cases}
y'' + y = 4\delta(t - 2\pi), \\[2pt]
y(0) = 1,\; y'(0) = 0
\end{cases}
\quad\Longrightarrow\quad
y(t) = \cos(t) + 4H(t - 2\pi)\sin(t)
$

##### Example 8 [Nagy, p. 190] (Two impulses)
$
\begin{cases}
y'' + 4y = \delta(t - \pi) - \delta(t - 2\pi), \\[2pt]
y(0) = y'(0) = 0
\end{cases}
$
$
\Longrightarrow\quad
y(t) = \frac{1}{2}\bigl[H(t - \pi) - H(t - 2\pi)\bigr]\sin(2t)
$

##### Example 9 (Third‑order system)
$
\begin{cases}
y''' + 2y'' + 2y' = \delta(t), \\[2pt]
y(0) = y'(0) = y''(0) = 0
\end{cases}
$
**Solution:** obtained from WolframAlpha,
$
y(t) = \frac{1}{2} - \frac{1}{2}e^{-t}\bigl(\sin(t) + \cos(t)\bigr)
$

### Type 1 Examples (Derivatives of Delta)

##### Example 10 [Ogata, p. 163] (First‑order system)
Transfer function:
$
C(s) = \frac{1}{Ts + 1}
\qquad\Longrightarrow\qquad
g(t) = \frac{1}{T}\, e^{-t/T}
$

##### Example 11 [Xue, p. 380]
Inverse Laplace transform:
$
\mathcal{L}^{-1}\!\left\{\frac{s}{(s+a)(s+b)}\right\}
 = \frac{1}{a-b}\bigl[ a e^{-a t} - b e^{-b t} \bigr]
$

##### Example 12 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+d}{(s+a)(s+b)}\right\}
 = \frac{1}{b-a}\bigl[ (d-a)e^{-a t} - (d-b)e^{-b t} \bigr]
$

##### Example 13 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+d}{s(s+a)(s+b)}\right\}
 = \frac{1}{ab}\left[ d - \frac{b(d-a)}{b-a}e^{-a t} + \frac{a(d-b)}{b-a}e^{-b t} \right]
$

##### Example 14 [Xue, p. 380]
$
\mathcal{L}^{-1}\!\left\{\frac{s+a}{s^2+\omega^2}\right\}
 = \frac{\sqrt{a^2+\omega^2}}{\omega}\,
   \sin\!\left(\omega t + \tan^{-1}\!\left(\frac{\omega}{a}\right)\right)
$
