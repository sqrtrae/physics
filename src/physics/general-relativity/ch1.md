# 1 - Special Relativity and Flat Spacetime

```admonish textbook
Carroll, S. _Spacetime and Geometry: An Introduction to Special Relativity_ (2019)

---

Comments:
- This textbook is the source for all notes and problems in this topic.
```

## 1.1 - Prelude

### 1.1.1 - Newtonian Gravity

```admonish remark
The Newtonian theory of gravity has two basic elements: (1) an equation for the gravitational field response to matter, and (2) an equation for matter's response to the gravitational field.
The conventional statement of these two elements is in terms of forces between particles, with the equation for the gravitational field written in terms of a force between two objects:

$$
\vec{F} = -\frac{GMm}{r^2}\hat{e}_{(r)},
$$

and the equation for matter's response being Newton's second law:

$$
\vec{F} = m\vec{a}.
$$

An equivalent statement of these two elements can be formulated in terms of the gravitational potential $\Phi$; the potential and mass density $\rho$ are related by Poisson's equation:

$$
\nabla^2\Phi = 4\pi G\rho,
$$

and the acceleration is given by:

$$
\vec{a} = -\nabla\Phi
$$
```

### 1.1.2 - General Relativity

```admonish remark
In GR, the two elements of Newtonian Gravity are formulated in terms of the curvature of spacetime.
The response of spacetime curvature to the presence of matter and energy is governed by Einstein's equation:

$$
R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = 8\pi GT_{\mu\nu}.
$$

In turn, the response of matter to spacetime curvature is governed by the geodesic equation:

$$
\frac{d^2x^\mu}{d\lambda^2} + \Gamma_{\rho\sigma}^\mu\frac{dx^\rho}{d\lambda}\frac{dx^\sigma}{d\lambda} = 0,
$$

where $x^\mu(\lambda)$ is the parameterized path of free particles in curved spacetime.
```

## 1.2 - Space and Time, Separately and Together

```admonish definition
**_Spacetime_** is a four-dimensional set, with elements labeled by three dimensions of space and one dimension of time.
A point in spacetime is called an **_event_**.
The path of a particle is a curve through spacetime called a **_worldline_**.
```

```admonish definition
The **_spacetime interval_** between two events is defined:
$$
(\Delta s)^2 = -(c\Delta t)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2.
$$
The spacetime interval is invariant under changes of inertial coordinates.
```