# 1 - Newton's Laws of Motion

```admonish textbook
John R. Taylor's _Classical Mechanics_ (2005)

---

Material used on this page:
- Chapter 1 - Newton's Laws of Motion
```

## Problems & Solutions

```admonish problem title="Problem 1.1"
{{#header title="Problem 1.1" level=3 hidden=true}}

Given the two vectors $\vec{b} = \hat{x} + \hat{y}$ and $\vec{c} = \hat{x} + \hat{z}$ find

**(a).** $\vec{b} + \vec{c}$

**(b).** $5\vec{b} + 2\vec{c}$

**(c).** $\vec{b}\cdot\vec{c}$

**(d).** $\vec{b}\times\vec{c}$.
```
```admonish solution
**(a).** $\vec{b} + \vec{c} = \boxed{2\hat{x} + \hat{y} + \hat{z}}$

**(b).** $5\vec{b} + 2\vec{c} = \boxed{7\hat{x} + 5\hat{y} + 2\hat{z}}$

**(c).** $\vec{b}\cdot\vec{c} = (\hat{x} + \hat{y})\cdot(\hat{x} + \hat{z}) = \hat{x}\cdot\hat{x} = \boxed{1}$

**(d).**
$$
\begin{align}
\vec{b}\times\vec{c} &= (\hat{x} + \hat{y})\times(\hat{x} + \hat{z}) \\\\
                     &= \hat{x}\times\hat{z} + \hat{y}\times\hat{x} + \hat{y}\times\hat{z} \\\\
                     &= (-1)\hat{y} + (-1)\hat{z} + (1)\hat{x} \\\\
                     &= \boxed{\hat{x} - \hat{y} - \hat{z}}
\end{align}
$$
```

```admonish problem title="Problem 1.2"
{{#header title="Problem 1.2" level=3 hidden=true}}

Two vectors are given as $\vec{b} = \hat{x} + 2\hat{y} + 3\hat{z}$ and $\vec{c} = 3\hat{x} + 2\hat{y} + \hat{z}$. Find

**(a).** $\vec{b} + \vec{c}$

**(b).** $5\vec{b} - 2\vec{c}$

**(c).** $\vec{b}\times\vec{c}$.
```
```admonish solution
**(a).** $\vec{b} + \vec{c} = \boxed{4\hat{x} + 4\hat{y} + 4\hat{z}}$

**(b).** $5\vec{b} - 2\vec{c} = 5(\hat{x} + 2\hat{y} + 3\hat{z}) - 2(3\hat{x} + 2\hat{y} + \hat{z}) = \boxed{-\hat{x} + 6\hat{y} + 13\hat{z}}$

**(c).**
$$
\begin{align}
\vec{b}\times\vec{c} &= (\hat{x} + 2\hat{y} + 3\hat{z})\times(3\hat{x} + 2\hat{y} + \hat{z}) \\\\
                     &= (1 * 2)\hat{x}\times\hat{y} + (1 * 1)\hat{x}\times\hat{z} + (2 * 3)\hat{y}\times\hat{x} \\\\
                     &\phantom{=} + (2 * 1)\hat{y}\times\hat{z} + (3 * 3)\hat{z}\times\hat{x} + (3 * 2)\hat{z}\times \hat{y} \\\\
                     &= (2)\hat{z} + (1)(-\hat{y}) + (6)(-\hat{z}) + (2)\hat{x} + (9)\hat{y} + (6)(-\hat{x}) \\\\
                     &= \boxed{-4\hat{x} + 8\hat{y} - 4\hat{z}}
\end{align}
$$
```

```admonish problem title="Problem 1.3"
{{#header title="Problem 1.3" level=3 hidden=true}}

By applying Pythagorean's theorm (the usual two-dimensional version) twice over, prove that the length $r$ of a three-dimensional vector $\vec{r} = (x, y, z)$ satisfies $r^2 = x^2 + y^2 + z^2$
```
```admonish solution
The vector $\vec{r}$ is the sum of the three vectors: $x\hat{x}$, $y\hat{y}$, and $z\hat{z}$.
These three vectors are all orthogonal to one another and have lengths $|x|$, $|y|$, and $|z|$ respectively.
Let $\vec{s} := x\hat{x} + y\hat{y}$.
Because $x\hat{x}$ and $y\hat{y}$ are orthogonal, we can use the Pythagorean theorm to find the length of $\vec{s}$:

$$
|s| := \sqrt{|x|^2 + |y|^2} = \sqrt{x^2 + y^2} \implies s^2 = x^2 + y^2.
$$

Similarly, because $\vec{r} = \vec{s} + z\hat{z}$ and $\vec{s}$, $z\hat{z}$ are orthogonal, the length of $\vec{r}$ is:

$$
|r| = \sqrt{|s|^2 + |z|^2} = \sqrt{s^2 + z^2} = \sqrt{(x^2 + y^2) + z^2} \implies \boxed{r^2 = x^2 + y^2 + z^2}.
$$
```

```admonish problem title="Problem 1.4"
{{#header title="Problem 1.4" level=3 hidden=true}}

One of the many uses of the dot product is to find the angle between two given vectors.
Find the angle between the vectors $\vec{b} = (1, 2, 4)$ and $\vec{c} = (4, 2, 1)$ by evaluating their dot product.
```
```admonish solution
We note $\vec{b}\cdot\vec{c} = |b| |c|\cos\theta$, where $\theta$ is the angle between $\vec{b}$ and $\vec{c}$.
Then

$$
\vec{b}\cdot\vec{c} = (1, 2, 4) \cdot (4, 2, 1) = 4 + 2(2) + 4 = 12,
$$

and

$$
|b||c|\cos\theta = \sqrt{1^2 + 2^2 + 4^2}\sqrt{4^2 + 2^2 + 1^2}\cos\theta = (1 + 4 + 16)\cos\theta = 21\cos\theta.
$$

Solving for $\theta$:

$$
\theta = \cos^{-1}\left(\frac{12}{21}\right) = \boxed{\cos^{-1}\left(\frac{4}{7}\right) \approx 55^\circ}
$$
```

```admonish problem title="Problem 1.5"
{{#header title="Problem 1.5" level=3 hidden=true}}

Find the angle between a body diagonal of a cube and any one of its face diagonals.
```

```admonish problem title="Problem 1.6"
{{#header title="Problem 1.6" level=3 hidden=true}}

By evaluating their dot product, find the values of the scalar $s$ for which the two vectors $\vec{b} = \hat{x} + s\hat{y}$ and $\vec{c} = \hat{x} - s\hat{y}$ are orthogonal.
```

```admonish problem title="Problem 1.7"
{{#header title="Problem 1.7" level=3 hidden=true}}

Prove that the two definitions of the dot product $\vec{r}\cdot\vec{s}$ as $rs\cos\theta$ and $\sum r_is_i$ are equal.
One way to do this is to choose your $x$ axis along the direction of $\vec{r}$.
```

```admonish problem title="Problem 1.8"
{{#header title="Problem 1.8" level=3 hidden=true}}

**(a).** Use the definition $\vec{r}\cdot\vec{s} = \sum r_is_i$ to prove that the dot product is distributive, that is, $\vec{r}\cdot(\vec{u} + \vec{v}) = \vec{r}\cdot\vec{u} + \vec{r}\cdot\vec{v}$.

**(b).** If $\vec{r}$ and $\vec{s}$ are vectors that depend on time, prove that the product rule for differentiating products applies to $\vec{r}\cdot\vec{s}$, that is, that

$$
\frac{d}{dt}(\vec{r}\cdot\vec{s}) = \vec{r}\cdot\frac{d\vec{s}}{dt} + \frac{d\vec{r}}{dt}\cdot\vec{s}.
$$
```

```admonish problem title="Problem 1.?"
{{#header title="Problem 1.?" level=3 hidden=true}}
```
