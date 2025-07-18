# 1 - Special Relativity and Flat Spacetime

```admonish textbook
Carroll, S. _Spacetime and Geometry: An Introduction to Special Relativity_ (2019)

---

Material used on this page:
- Chapter 1 - Special Relativity and Flat Spacetime
```

---

{{#header title="Problem 1.1" level=2 hidden=true}}

```admonish problem title="Problem 1.1"
Consider an inertial frame $S$ with coordinates $x^\mu = (t, x, y, z)$, and a frame $S'$ with coordinates $x^{\mu'}$ related to $S$ by a boost with velocity parameter $v$ along the $y$-axis.
Imagine we have a wall at rest in $S'$, lying along the line $x' = -y'$.

(a). From the point of view of $S$, what is the relationship between the incident angle of a ball hitting the wall (traveling in the $x$-$y$ plane) and the reflected angle?

(b). What about the speed[^1] before and after?
```

[^1]: In the original problem, the word 'velocity' was used here.
      However, I believe the question intended to ask about the ball's _speed_ (magnitude of velocity) before and after.

```admonish solution

[//]: # (WLOG, we will assume the ball hits the wall at the origin in $S'$ and $S$ &#40;meaning when the ball hits the wall, the wall is intersecting the origin of $S$&#41;.)

[//]: # (There are two scenarios to consider: &#40;1&#41; the ball hitting the moving wall from the region _behind_ the wall &#40;e.g. $x'_b < -y'_b$&#41;, and &#40;2&#41; the ball hitting the moving wall from the region _in front of_ the wall &#40;e.g. $x'_b > -y'_b$&#41;.)

[//]: # ()
[//]: # (The general approach we will use to solve this problem is the same for both scenarios:)

[//]: # (1. Start with the speed &#40;$v_b$&#41; and angle of incidence &#40;$\theta_b$&#41; of the ball in $S$ before hitting the wall.)

[//]: # (2. Apply the Lorentz boost of $+v$ in the $y$ direction to get the speed &#40;$v_b'$&#41; and angle of incidence &#40;$\theta_b'$&#41; of the ball in $S'$ before hitting the wall.)

[//]: # (   In $S'$, the speed &#40;$v_a'$&#41; and angle of reflection &#40;$\theta_a$&#41; of the ball after hitting the wall are equal to speed and the angle of incidence before hitting the wall &#40;but reflected across $x' = y'$&#41;.)

[//]: # (3. Apply the Lorentz boost of $-v$ in the $y$ direction to get the speed &#40;$v_a$&#41; and angle of reflection &#40;$\theta_a$&#41; of the ball in $S$ after hitting the wall.)

[//]: # (4. Identify and simplify the relationships between $\theta_b$ and $\theta_a$, and between $v_b$ and $v_a$.)

[//]: # ()
[//]: # (<h3><a>Scenario 1</a></h3>)

[//]: # ()
[//]: # (Let $v_b$ be the speed of the ball before hitting the wall, and $\theta_b$ be the angle of incidence of the ball before hitting the wall.)

[//]: # (We define the angle of incidence as the angle counter-clockwise from the line $)

[//]: # ()
[//]: # (Let ${v_b}'$ be the speed of the ball and ${\theta_b}'$ be the angle of incidence of the ball.)

[//]: # (We define the angle of incidence as the angle counter-clockwise from the vector $-\hat{x}' - \hat{y}'$ centered at the origin in $S'$.)

[//]: # (For clarity, this would mean that, if the angle of incidence is $\pi/4$, then the velocity of the ball in $S'$ would be ${\vec{v}_b}' = {v_b}'\hat{x}'$.)

[//]: # ()
[//]: # (In terms of ${v_b}'$ and ${\theta_b}'$, the velocity of the ball in $S'$ is )

[//]: # ()
[//]: # ($$)

[//]: # ({\vec{v}_b}' = {v_b}'\cos&#40;\theta + \pi/4&#41;\hat{x}' + {v_b}'\sin&#40;\theta + \pi/4&#41;\hat{y}')

[//]: # ($$)

[//]: # ()
[//]: # (To get the velocity of the ball in $S$, we apply the Lorentz boost of $v$ in the $-\hat{y}'$ direction:)

[//]: # ()
[//]: # ($$)

[//]: # (\vec{v}_b = {v_b}'\cos&#40;\theta + \pi/4&#41;\hat{x}')

[//]: # ($$)
```

{{#header title="Problem 1.2" level=2 hidden=true}}

```admonish problem title="Problem 1.2"
Imagine that space (not spacetime) is actually a finite box, or in more sophisticated terms, a three-torus of size $L$.
By this we mean that there is a coordinate system $x^\mu = (t, x, y, z)$ such that every point with coordinates $(t, x, y, z)$ is identified with every point with coordinates $(t, x + L, y, z)$, $(t, x, y + L, z)$, and $(t, x, y, z + L)$.
Note that the time coordinate is the same.
Now consider two observers; observer $A$ is at rest in this coordinate system (constant spatial coordinates), while observer $B$ moves in the $x$-direction with constant speed $v$.
$A$ and $B$ begin at the same event, and while $A$ remains still, $B$ moves once around the universe and comes back to intersect the worldline of $A$ without ever having to accelerate (since the universe is periodic).

(a). What are the relative proper times experienced in this interval by $A$ and $B$? 

(b). Is this consistent with your understanding of Lorentz invariance?
```

{{#header title="Problem 1.3" level=2 hidden=true}}

```admonish problem title="Problem 1.3"
Three events, $A$, $B$, $C$, are seen by observer $\mathcal{O}$ to occur in the order $ABC$. 
Another observer, $\bar{\mathcal{O}}$, sees the events to occur in the order $CBA$. 
Is it possible that a third observer sees the events in the order $ACB$?
```

{{#header title="Problem 1.4" level=2 hidden=true}}

```admonish problem title="Problem 1.4"
Projection effects can trick you into thinking that an astrophysical object is moving "superluminally".
Consider a quasar that ejects gas with speed $v$ at an angle $\theta$ with respect to the line-of-sight of the observer.
Projected onto the sky, the gas appears to travel perpendicular to the line of sight with angular speed $v_{\text{app}}/D$, where $D$ is the distance to the quasar and $v_{\text{app}}$ is the apparent speed.

(a). Derive an expression for $v_{\text{app}}$ in terms of $v$ and $\theta$.

(b). Show that, for appropriate values of $v$ and $\theta$, $v_{\text{app}}$ can be greater than $1$.
```

{{#header title="Problem 1.5" level=2 hidden=true}}

```admonish problem title="Problem 1.5"
Particle physicists are so used to setting $c = 1$ that they measure mass in units of energy.
In particular, they tend to use electron voltes ($\pu{1 eV} = \pu{1.6\times10^{-12} erg} = \pu{1.8\times10^{-33} g}$), or more commonly, $\pu{keV}$, $\pu{MeV}$, and $\pu{GeV}$ ($\pu{10^3 eV}$, $\pu{10^6 eV}$, and $\pu{10^9 eV}$, respectively).
The muon has been measured to have a mass of $\pu{0.106 GeV}$ and a rest frame lifetime of $2.19\times10^{-6}$ seconds.
Imagine that such a muon is moving in the circular storage ring of a particle accelerator, $1$ kilometer in diameter, such that the muon's total energy is $\pu{1000 GeV}$.

(a). How long would it appear to live from the experimenter's point of view?

(b). How many radians would it travel around the ring?
```

{{#header title="Problem 1.6" level=2 hidden=true}}

```admonish problem title="Problem 1.6"
In Euclidean three-space, let $p$ be the point with coordinates $(x, y, z) = (1, 0, -1)$.
Consider the following curves that pass through $p$:
\begin{align*}
      x^i(\lambda) &= (\lambda, (\lambda - 1)^2, -\lambda) \n
      x^i(\mu) &= (\cos\mu, \sin\mu, \mu - 1) \n
      x^i(\sigma) &= (\sigma^2, \sigma^3 + \sigma^2, \sigma).
\end{align*}

(a). Calculate the components of hte tangent vectors to these curves at $p$ in the coordinate basis $\{\partial_x, \partial_y, \partial_z\}$.

(b). Let $f = x^2 + y^2 - yz$. Calculate $\dd f/\dd\lambda$, $\dd f/\dd\mu$, and $\dd f/\dd\sigma$.
```

{{#header title="Problem 1.7" level=2 hidden=true}}

```admonish problem title="Problem 1.7"
Imagine we have a tensor $X^{\mu\nu}$ and a vector $V^\mu$, with components
\begin{equation*}
X^{\mu\nu} = \mqty(
  2 & 0 & 1 & -1 \n
  -1 & 0 & 3 & 2 \n
  -1 & 1 & 0 & 0 \n
  -2 & 1 & 1 & -2
) \qc V^\mu = (-1, 2, 0, -2).
\end{equation*}
Find the components of[^2]:

(a). $X^\mu_{\phantom{\mu}\nu}$

(b). $X_\mu^{\phantom{\mu}\nu}$

(c). $X^{(\mu\nu)}$

(d). $X_{[\mu\nu]}$

(e). $X^\lambda_{\phantom{\lambda}\lambda}$

(f). $V^\mu V_\mu$

(g). $V_\mu X^{\mu\nu}$
```

[^2]: The original problem doesn't state this, but it is implied the metric $\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$ is used when converting between upper and lower indices.

{{#header title="Problem 1.8" level=2 hidden=true}}

```admonish problem title="Problem 1.8"
If $\partial_\nu T^{\mu\nu} = Q^\mu$, what physically does the spatial vector $Q^i$ represent? Use the dust energy momentum tensor to make your case.
```

{{#header title="Problem 1.9" level=2 hidden=true}}

```admonish problem title="Problem 1.9"
For a system of discrete point particles the energy-momentum tensor takes the form
\begin{equation*}
T_{\mu\nu} = \sum_a \frac{p_\mu^{(a)}p_\nu^{(a)}}{p^{0(a)}}\delta^{(3)}(\vb{x} - \vb{x}^{(a)}),
\end{equation*}
where the index $a$ labels the different particles.
Show that, for a dense collection of particles with isotropically distributed velocities, we can smooth over the individual particle worldlines to obtain the perfect-fluid energy-momentum tensor:
\begin{equation*}
T^{\mu\nu} = (\rho + p)U^\mu U^\nu + p\eta^{\mu\nu}.
\end{equation*}
```

{{#header title="Problem 1.10" level=2 hidden=true}}

```admonish problem title="Problem 1.10"
Using the tensor transformation law applied to $F_{\mu\nu}$, show how the electric and magnetic field $3$-vectors $\vb{E}$ and $\vb{B}$ transform under

(a). a rotation about the $y$-axis,

(b). a boost along the $z$-axis.
```

{{#header title="Problem 1.11" level=2 hidden=true}}

```admonish problem title="Problem 1.11"
Verify that
\begin{equation*}
\partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} + \partial_\lambda F_{\mu\nu} = 0
\end{equation*}
is indeed equivalent to
\begin{equation*}
\partial_{[\mu}F_{\nu\lambda]} = 0,
\end{equation*}
and that they are both equivalent to the two equations:
\begin{align*}
\tilde\epsilon^{ijk}\partial_jE_k + \partial_0B^i &= 0 \n
                                    \partial_iB^i &= 0.
\end{align*}
```

{{#header title="Problem 1.12" level=2 hidden=true}}

```admonish problem title="Problem 1.12"
Consider the two field theories we explicitly discussed, Maxwell's electromagnetism (let $J^\mu = 0$) and the scalar field theory defined by
\begin{equation*}
\mathcal{L} = -\frac{1}{2}\eta^{\mu\nu}(\partial_\mu\phi)(\partial_\nu\phi) - V(\phi).
\end{equation}

(a). Express the components of the energy-momentum tensors of each theory in three-vector notation, using the divergence, gradient, curl, electric, and magnetic fields, and an overdot to denote time derivatives.

(b). Using the equations of motion, verify (in any notation you like) that the energy-momentum tensors are conserved.
```

{{#header title="Problem 1.13" level=2 hidden=true}}

```admonish problem title="Problem 1.13"
Consider adding to the Lagrangian for electromagnetism an additional term of the form $\mathcal{L}' = \tilde\epsilon_{\mu\nu\rho\sigma}F^{\mu\nu}F^{\rho\sigma}.

(a). Express $\mathcal{L}'$ in terms of $\vb{E}$ and $\vb{B}$.

(b). Show that including $\mathcal{L}'$ does not affect Maxwell's equations.
Can you think of a deep reason for this?
```
