# 1 - Newton's Laws of Motion

```admonish textbook
John R. Taylor's _Classical Mechanics_ (2005)

---

Material used on this page:
- Chapter 1 - Newton's Laws of Motion
```

## 1.1 - Classical Mechanics

The first formulation—Newton's three laws of motion—of classical mechanics was developed from the works of Galileo (1564 - 1642) and Newton (1642 - 1727). 
Two alternative formulations—Lagrangian mechanics and Hamiltonian mechanics—were developed by Lagrange (1736 - 1813) and Hamilton (1805 - 1865) respectively.

## 1.2 - Space and Time

### 1.2.1 - Space

Each point $P$ of three-dimensional space can be labeled by a position vector $\vec{r}$.
The position vector $\vec{r}$ is most naturally expanded using Cartesian coordinates:

$$\vec{r} = x\hat{x} + y\hat{y} + z\hat{z},$$

where $\hat{x}, \hat{y}, \hat{z}$ are orthonormal unit vectors and $x, y, z$ are the components of $\vec{r}$ along these unit vectors, respectively.
On occasion, an alternative indexed notation, where $(x, y, z) = (r_1, r_2, r_3)$ and $(\hat{x}, \hat{y}, \hat{z}) = (\hat{e}_1, \hat{e}_2, \hat{e}_3)$, will be used:

$$\vec{r} = r_1\hat{e}_1 + r_2\hat{e}_2 + r_3\hat{e}_3 = \sum _{i=1}^3 r_i\hat{e}_i.$$

### 1.2.2 - Vector Operations

```admonish definition
The **_sum_** of two vectors $\vec{r}$ and $\vec{s}$ is found by summing their corresponding components:

$$\vec{r} + \vec{s} = (r_1 + s_1)\hat{e}_1 + (r_2 + s_2)\hat{e}_2 + (r_3 + s_3)\hat{e}_3 = \sum _{i=1}^3 (r_i + s_i)\hat{e}_i.$$
```

```admonish definition
The **_magnitude_** of a vector $\vec{r}$—denoted $|\vec{r}|$, or alternatively just $r$—is defined:

$$r = \sqrt{(r_1)^2 + (r_2)^2 + (r_3)^2}.$$
```

```admonish definition
The **_dot product_** of two vectors—denoted $\vec{r}\cdot\vec{s}$—is defined:

$$\vec{r}\cdot\vec{s} = rs\cos\theta = r_1s_1 + r_2s_2 + r_3s_3 = \sum _{i=1}^3 r_is_i$$
```

```admonish definition
The **_cross product_** of two vectors $\vec{r}$ and $\vec{s}$—denoted $\vec{r}\times\vec{s}$—is defined:

$$
\begin{align}
\vec{r}\times\vec{s} &= (r_2s_3 - r_3s_2)\hat{e}_1 + (r_3s_1 - r_1s_3)\hat{e}_2 + (r_1s_2 - r_2s_1)\hat{e}_3 \\\\
&= \text{det}\begin{bmatrix}
  \hat{e}_1 & \hat{e}_2 & \hat{e}_3 \\\\
  r_1 & r_2 & r_3 \\\\
  s_1 & s_2 & s_3
\end{bmatrix}
\end{align}
$$

```

### 1.2.3 - Differentiation of Vectors

Let $\vec{r}(t)$ be the position of a particle as a function of time. 
The derivative of $\vec{r}(t)$ is the velocity of the particle, denoted $\vec{v}(t)$. 
Further, the derivative of $\vec{v}(t)$ is the acceleration of the particle, denoted $\vec{a}(t)$.
In Cartesian coordinates, the derivative of $\vec{r}(t)$ is simply the vector formed from the derivative of its components:

$$\vec{v} := \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{x} + \frac{dy}{dt}\hat{y} + \frac{dz}{dt}\hat{z}.$$

Because of how often the time derivative comes up, there exists an abbreviated dot notation:

$$\dot{x} := \frac{dx}{dt}, \\quad \dot{\vec{r}} = \dot{x}\hat{x} + \dot{y}\hat{y} + \dot{z}\hat{z}$$

The dot notation for time derivatives will generally be used going forward.

### 1.2.4 - Time

In the domain of classical mechanics, time is considered to be a single universal parameter $t$, which all observers agree on.
This domain, which is highly accurate at speeds much lower than the speed of light, will be assumed throughout these notes.

### 1.2.5 - Reference Frames

```admonish definition
A **_reference frame_** is a choice of spatial origin and axes to label positions and a choice of temporal origin to measure times.
Reference frames that are moving relative to one another are not, generally speaking, physically equivalent.
There are certain, special frames called **_inertial frames_**, where Newton's laws hold true in their standard, simple form.
Frames which are accelerating relative to inertial frames are called **_noninertial frames_**, and are frames where Newton's laws do not hold in their standard form.
```

## 1.3 - Mass and Force



```admonish todo title="TODO"
Finish chapter 
```
