# 1 - Newton's Laws of Motion

```admonish textbook
Carroll, S. _Spacetime and Geometry: An Introduction to Special Relativity_ (2019)

---

Material used on this page:
- Chapter 1 - Special Relativity and Flat Spacetime
```

## Problems & Solutions

{{#header title="Problem 1.1" level=3 hidden=true}}

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

{{#header title="Problem 1.2" level=3 hidden=true}}

```admonish problem title="Problem 1.2"
Imagine that space (not spacetime) is actually a finite box, or in more sophisticated terms, a three-torus of size $L$.
By this we mean that there is a coordinate system $x^\mu = (t, x, y, z)$ such that every point with coordinates $(t, x, y, z)$ is identified with every point with coordinates $(t, x + L, y, z)$, $(t, x, y + L, z)$, and $(t, x, y, z + L)$.
Note that the time coordinate is the same.
Now consider two observers; observer $A$ is at rest in this coordinate system (constant spatial coordinates), while observer $B$ moves in the $x$-direction with constant speed $v$.
$A$ and $B$ begin at the same event, and while $A$ remains still, $B$ moves once around the universe and comes back to intersect the worldline of $A$ without ever having to accelerate (since the universe is periodic).

(a). What are the relative proper times experienced in this interval by $A$ and $B$? 

(b). Is this consistent with your understanding of Lorentz invariance?
```

{{#header title="Problem 1.3" level=3 hidden=true}}

```admonish problem title="Problem 1.3"
Three events, $A$, $B$, $C$, are seen by observer $\mathcal{O}$ to occur in the order $ABC$. 
Another observer, $\bar{\mathcal{O}}$, sees the events to occur in the order $CBA$. 
Is it possible that a third observer sees the events in the order $ACB$?
```
