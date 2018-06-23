###3 Problem Type 1
Let's  name the following system as Problem Type 1.1:
Find
$$
\{z\}_0=\{z_0,z'_0,\ldots ,z^{(n-1)}_0\}\\
$$
which delivers for the system
$$
\begin{cases}
    z(t)=IVP(\{a\}, 0, t=0,\{z\}_0),\\
    \{a\} = \{a_0,a_1,\ldots a_n\}\\
    \{z\}_0=\{z_0,z'_0,\ldots ,z^{(n-1)}\}\\
\end{cases}
$$
the equivalence of next one:
$${\begin{cases}
    y(t)=IVP(\{a\}, b\delta(t), t=0,\{y\}_0),\\
    \{a\} = \{a_0,a_1,\ldots a_n\}\\
    \{y\}_0=\{y_0,y'_0,\ldots ,y^{(n-2)} , y^{(n-1)}_0\}\\
\end{cases}}
$$
At this case 'equivalence' means:
$$
z(t)=y(t), \forall t\ge  t_0=0
$$
Let's perform Laplas Transform (LT) for y(t) with respect to non-null initial condition.
$$
L\{y(t)\}=Y(s)
$$
$$
Y(s)=L\{\sum_{i=0}^n \left( a_iy^{(n-i)}-b\delta(t)\right)\}=\sum_{i=0}^n \left( a_iL\{y^{(n-i)\}}\right)-bL\{\delta(t)\}
$$
$$
L\{a_0y^{(n-0)}\}=a_0\left[s^nY-s^{n-1}y(0)-s^{n-2}y'(0)-s^{n-3}y''(0)- ...-s^1y^{(n-2)}(0)-y^{(n-1)}(0)\right]\\
L\{a_1y^{(n-1)}\}=a_1\left[s^{(n-1)}Y-s^{n-2}y(0)-s^{n-3}y'(0)-s^{n-2}y''(0)- ...-s^1y^{(n-3)}-y^{(n-2)}(0)\right]\\
L\{a_2y^{(n-2)}\}=a_2\left[s^{(n-2)}Y-s^{n-3}y(0)-s^{n-4}y'(0)-s^{n-5}y''(0)- ...-s^1y^{(n-4)}(0)-y^{(n-3)}(0)\right]\\
...\\
L\{a_{n-1}y'\}=a_{n-1}\left[s'Y-y(0) \right]\\
L\{a_{n}y\}=a_{n}\left[Y\right]\\
-bL\{\delta(t)\}=-be^{(-s)0}=-b
$$
Let's treat IC as a vector and use following notation:
$$
y^{(i)}(0)=y_i
$$
And rewrite in this way:
$$\begin{equation}\begin{aligned}
L\{y(t)\} = &s^n\left(a_0Y\right)+\\
  & s^{n-1}\left(a_1Y-a_0y_0\right)+\\
  & s^{n-2}\left(a_2Y-a_1y_0-a_0y_1\right)+\\
  & s^{n-3}\left(a_3Y-a_2y_0-a_1y_1-a_0y_2\right)+\\
  & ...\\
  & s^1\left(a_{n-1}Y-\sum_{i=0}^{n-2} a_{n-2-i}y_i\right)+\\
  & s^0\left(a_{n}Y-\sum_{i=0}^{n-1} a_{n-1-i}y_i+b\right)=\\
  & =\sum_{i=0}^{n} s^{n-i}a_iY-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b
\end{aligned}\end{equation}$$
Let's perform LT for z(t) with respect to non-null initial condition.
$$
L\{z(t)\}=Z(s)
$$
$$\begin{equation}\begin{aligned}
L\{z(t)\} = \sum_{i=0}^{n} s^{n-i}a_iZ-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)
\end{aligned}\end{equation}$$
$$
y(t)=z(t)\implies Y(s)=Z(s)\implies\\
\sum_{i=0}^{n} s^{n-i}a_iY-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b=\sum_{i=0}^{n} s^{n-i}a_iZ-\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)
$$
Due to
$$
s^{n-i}a_iY=s^{n-i}a_iZ
$$
as a result:
$$
\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}y_j\right)-b=\sum_{i=1}^{n}\left(s^{n-i}\sum_{j=0}^{i-1}a_{(i-1)-j}z_j\right)\implies
$$
following equations:
$$
i=1,s^{n-1}:a_0y_0=a_0z_0\\
i=2,s^{n-2}:\sum_{j=0}^{1}a_{1-j}y_j=\sum_{j=0}^{1}a_{1-j}z_j\\
...
i=n,s^{n-0}:\sum_{j=0}^{n-1}a_{n-1-j}y_j+b=\sum_{j=0}^{n-1}a_{n-1-j}z_j
$$
Rewrite it at this way:
$$

$$
q	wert
qwer
qwe
