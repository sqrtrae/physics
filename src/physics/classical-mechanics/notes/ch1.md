# 1 - Newton's Laws of Motion

Notes taken from chapter 1 of John R. Taylor's _Classical Mechanics_ (2005).

## 1.1 - Classical Mechanics

The first formulation—Newton's three laws of motion—of classical mechanics was developed from the works of Galileo (1564 - 1642) and Newton (1642 - 1727). 
Two alternative formulations—Lagrangian mechanics and Hamiltonian mechanics—were developed by Lagrange (1736 - 1813) and Hamilton (1805 - 1865) respectively.

## 1.2 - Space and Time

### 1.2.1 - Space

Each point $P$ of three-dimensional space can be labeled by a position vector $\vec{r}$. The position vector $\vec{r}$ is most naturally expanded by giving its components $(x, y, z)$ in the direction of three perpendicular axes; we define the three unit vectors $\hat{x}, \hat{y}, \hat{z}$ to lie along these axes such that:

$$\vec{r} = x\hat{x} + y\hat{y} + z\hat{z}.$$

Alternative notation, where $(x, y, z) = (r_1, r_2, r_3)$ and $(\hat{x}, \hat{y}, \hat{z}) = (\hat{e}_1, \hat{e}_2, \hat{e}_3)$:

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

```admonish todo title="TODO"
Finish chapter
```
