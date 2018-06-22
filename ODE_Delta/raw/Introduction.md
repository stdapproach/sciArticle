###2 Introduction
Lets take a look at first order system:
$$
{\begin{cases}
x'=Ax+Bu(t),\\
x(t_0)=x_0
\end{cases}
}\tag1
$$
Solution of (1) is a function
$$
{
x(t)=e^{A(t-t_0)}+\int_{t_0}^t e^{A(t-\tau)}Bu(\tau)d\tau
}\tag2
$$
The expression (2) delivers solution for the equation (1), which could be rewritten in short form
$$
x(t)=IVP\left(A,Bu(t),t_0,x_0\right)
$$
And substitute the Dirac delta function as load, so the system (1) becomes as
$$
{\begin{cases}
x'=Ax+B\delta(t),\\
x(t_0)=x_0
\end{cases}
}\tag3
$$
The solution is:
$$
x(t)=x_0e^{A(t-t_0)}+\int_{t_0}^t e^{A(t-\tau)}B\delta(\tau)d\tau
$$
Using integration by parts get:
$$
x(t)=x_0e^{A(t-t_0)}+B\int_{t_0}^t e^{A(t-\tau)}\delta(\tau)d\tau
$$
## Stash
Order
The orderof a differential equation is the largest derivative present in the differential equation.
Ordinary and Partial Differential Equations
A differential equation is called an ordinary differential equation, abbreviated by ode,if it has 
ordinary derivatives in it. Likewise, a differential equation is called a partial differential 
equation, abbreviated by pde,if it has differential derivatives in it. In the differential equations 
above (3) - (7) are ode’s and (8) - (10) are pde’s. 
//
###Where arise ODE with delta from:
####Balakumar
All of these excitations are characterized by sudden changes
in their respective profiles of amplitude with time. When transformed to the
frequency domain the responses to such transient excitations can also provide
a basis for determining the characteristics of a system. The resulting displacement response, and several design criteria are established based on this
information. In the systems considered in this chapter, the inertia element or
the base of the system is subjected to a transient forcing.
//
In this chapter, we shall show how to:
• Analyze single degree-of-freedom systems subjected to abruptly changing forces, such as shocks, pulses, step functions, and ramps that are applied to the inertia element and to the base of the system.
• Study the significance of the ratio of the duration of a time-varying force
to the period of free oscillation of the system.
• Relate the duration of a shock to its frequency content and study how this
affects the system response.
• Determine the spectral energy of the input disturbance and the response.
//
####Benchora
Since the late 1990s, the authors have produced an extensive portfolio of results on
differential equations and differential inclusions undergoing impulse effects. Both
initial value problems and boundary value problems have been dealt with in their
work.
//
The dynamics of evolving processes is often subjected to abrupt changes such
as shocks, harvesting, and natural disasters. Often these short-term perturbations
are treated as having acted instantaneously or in the form of “impulses.”
//
For well over a century, differentialequationshavebeenusedinmodelingthedynamics of changing processes. A great deal of the modeling development has been
accompanied by a rich theory for differential equations.
//
The dynamics of many evolving processes are subject to abrupt changes, such
as shocks, harvesting and natural disasters. These phenomena involve short-term
perturbations from continuous and smooth dynamics, whose duration is negligible in comparison with the duration of an entire evolution. In models involving such perturbations, it is natural to assume these perturbations act instantaneously or in the form of “impulses.” As a consequence, impulsive differential
equations have been developed in modeling impulsive problems in physics, population dyamics, ecology, biological systems, biotechnology, industrial robotics,
pharmcokinetics, optimal control, and so forth. Again, associated with this development, a theory of impulsive differential equations has been given extensive
attention. Works recognized as landmark contributions include [29,30,180,217],
with [30] devoted especially to impulsive periodic systems of differential equations.
Some processes, especially in areas of population dynamics, ecology, and pharmacokinetics, involve hereditary issues. The theory and applications addressing
such problems have heavily involved functional differentialequationsaswellas
impulsive functional differential equations.
//
####Bottega
Engineering systems are often subjected to forces of very large magnitude that act 
over very short periods of time. Examples include forces produced by impact, explosions or shock. In this section we examine the response of single degree of freedom 
systems to such loading. It will be seen that the response to impulse loading provides 
a fundamental solution from which the response to more general loading types may 
be based. Toward these ends, we first classify forces into two fundamental types. 
//
Time dependent forces may be classifiedas impulsive or nonimpulsive. Impulsive 
forces are those that act over very short periods of time but possess very large magnitudes, such as the forces associated with explosions and impact. Nonimpulsive forces 
are those that are well behaved over time, such as the gravitational force, the elastic 
spring force and the viscous damping force. Impulsive and nonimpulsive forces are 
defined formally in what follows. With the qualitative descriptions of these two types 
of forces established we now proceed to formally define impulsive and nonimpulsive 
forces mathematically. 
Impulsive Forces 
Forces that act over very short periods of time, such as those due to explosions or 
impact, may be difficult to measure directlyor to quantify mathematically. However, 
their impulses can be measured and quantified. In this light, an impulsive force is 
defined as a force that imparts a finite (nonvanishing) impulse over an infinitesimal 
time interval. Formally, an impulsive force F(t) is a force for which 
####Dawkins - nothing
####De Silva - nothing
####Finan
In applications, we are often encountered with linear systems, originally at
rest, excited by a sudden large force (such as a large applied voltage to an
electrical network) over a very short time frame. In this case, the output
corresponding to this sudden force is referred to as the "impulse response".
Mathematically, an impulse can be modeled by an initial value problem with
a special type of function known as the Dirac delta function as the external
force, i.e., the nonhomogeneous term. To solve such IVP requires nding the
Laplace transform of the delta function which is the main topic of this section.
####Genta
When a large force acts on the system for a short time, as in the case
of shock loads, the impulsive model that assumes that a force tending to
infinity acts for a time tending to zero can be used. This model is based on
the unit-impulse functionδ(t)(orDirac’sδ), defined by the relationships
//
The response to an impulse excitationis easily computed: It is sufficient
to observe that in the infinitely short period of time in which the impulsive
force acts, all other forces are negligible compared to it. The momentum
theorem can be applied to compute the conditions of the system just after
the impulsive force has been applied from those related to the instant before
its application.
The positionx0 after the impulse is equal to that before the impulse,
while the velocityv0is equal to the one before the impulse plus an increment
due to an increase of momentum equal to the impulse. Assuming that before
the impulse the system with a single degree of freedom is at rest in the
origin, it follows that
####Kelly - nothing
####Nagy - nothing
####Ogata - nothing
####Rao- nothing
####Weber- nothing
####Zill
UNIT IMPULSE Mechanical systems are often acted on by an external force (or
electromotive force in an electrical circuit) of large magnitude that acts only for a
very short period of time. For example, a vibrating airplane wing could be struck by
lightning, a mass on a spring could be given a sharp blow by a ball peen hammer, and
a ball (baseball, golf ball, tennis ball) could be sent soaring when struck violently by
some kind of club (baseball bat, golf club, tennis racket). See Figure 7.5.1. The graph
of the piecewise-defined function
#### Articles
#####Dylan Zwick
Consider a force f (t) that acts only during a very short time interval, a ≤
t ≤ b, with f (t) = 0 outside this interval. A bat striking a ball or a bolt of
lightning striking a tower, for example. Typically, the effect of this force
depends only on the integral
//
The time interval ǫ over which the impulse acts is frequently very small,
and it’s difficult to get a good measure of what it is. So, we can try to model
an instantaneous impulse that occurs preciesely at the time t = a. We call
this instantaneous impulse the Dirac delta funciton, and we represent it as:
//
where t is time and x(t) is the displacement of the mass from equilibrium. Now suppose
that for t · 0 the mass is at rest in its equilibrium position, so x
0
(0) = x(0) = 0. At
t = 0 the mass is struck by an “instantaneous” hammer blow. This situation actually occurs
frequently in practice—a system sustains an forceful, almost-instantaneous input. Our goal
is to model the situation mathematically and determine how the system will respond.
//
Physically such a di§erential equation might
arise if an oscillatory system were given an initial push, or a recurrent push. But what happens when an
oscillatory system is struck by a hammer?
//
Theimpulse response of a system is its response to the input ∂(t) when the system
is initially at rest. The impulse response is usually denoted h(t). Sometimes it's
called Green's function.
In other words, if the input to an initially—at—rest system is ∂(t) then the output
is named h(t).
//






