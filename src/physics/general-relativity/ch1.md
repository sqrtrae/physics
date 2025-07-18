# 1 - Special Relativity and Flat Spacetime

```admonish textbook
Carroll, S. _Spacetime and Geometry: An Introduction to Special Relativity_ (2019)

---

Material used on this page:
- Chapter 1 - Special Relativity and Flat Spacetime
```

## 1.1 - Prelude

```admonish note title="Newtonian Gravity"
The Newtonian theory of gravity has two basic elements: (1) an equation for the gravitational field response to matter, and (2) an equation for matter's response to the gravitational field.
The conventional statement of these two elements is in terms of forces between particles, with the equation for the gravitational field written in terms of a force between two objects:

\begin{equation}
\vec{F} = -\frac{GMm}{r^2}\hat{e}_{(r)},
\end{equation}

and the equation for matter's response being Newton's second law:

\begin{equation}
\vec{F} = m\vec{a}.
\end{equation}

An equivalent statement of these two elements can be formulated in terms of the gravitational potential $\Phi$; the potential and mass density $\rho$ are related by Poisson's equation:

\begin{equation}
\laplacian\Phi = 4\pi G\rho,
\end{equation}

and the acceleration is given by:

\begin{equation}
\vec{a} = -\grad\Phi.
\end{equation}
```

```admonish note title="General Relativity"
In GR, the two elements of Newtonian Gravity are formulated in terms of the curvature of spacetime.
The response of spacetime curvature to the presence of matter and energy is governed by Einstein's equation:

\begin{equation}
R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = 8\pi GT_{\mu\nu}.
\end{equation}

In turn, the response of matter to spacetime curvature is governed by the geodesic equation:

\begin{equation}
\dv[2]{x^\mu}{\lambda} + \Gamma_{\rho\sigma}^\mu\dv{x^\rho}{\lambda}\dv{x^\sigma}{\lambda} = 0,
\end{equation}

where $x^\mu(\lambda)$ is the parameterized path of free particles in curved spacetime.
```

## 1.2 - Space and Time, Separately and Together

```admonish note title="Einstein Notation"
Einstein notation uses greek indices as shorthand for vectors and one-forms, e.g.:

\begin{equation}
x^\mu := (x^0, x^1, x^2, x^3)\qc x_\mu := (x_0, x_1, x_2, x_3)
\end{equation}

It is convention that the first component of vectors/one-forms is the temporal component, and the rest are the spatial components.
When referring to only the spatial components of a vector/one-form, latin indices are used instead, e.g.:

\begin{equation}
x^i := (x^1, x^2, x^3)\qc x_i := (x_1, x_2, x_3)
\end{equation}

The notation is naturally extended to higher order tensors.
For example, the shorthand under Einstein notation for a generic linear transformation tensor is:

\begin{equation}
A^\mu_{\phantom\mu\nu} = \mqty(
  A^0_{\phantom{0}0} & A^0_{\phantom{0}1} & A^0_{\phantom{0}2} & A^0_{\phantom{0}3} \n
  A^1_{\phantom{1}0} & A^1_{\phantom{1}1} & A^1_{\phantom{1}2} & A^1_{\phantom{1}3} \n
  A^2_{\phantom{2}0} & A^2_{\phantom{2}1} & A^2_{\phantom{2}2} & A^2_{\phantom{2}3} \n
  A^3_{\phantom{3}0} & A^3_{\phantom{3}1} & A^3_{\phantom{3}2} & A^3_{\phantom{3}3}
)
\end{equation}

When denoting the sum over products of components of compatible tensors, a summation convention is used: if the same index appears twice—once "upstairs" and once "downstairs"—then that index is implicitly summed over in the term. For example:

\begin{equation}
x^\mu y_\mu := \sum_{\mu=0}^3 x_\mu y^\mu.
\end{equation}

When the index is a latin index, only the spatial components are summed over:

\begin{equation}
x^i y_i := \sum_{i=1}^3 x_i y^i.
\end{equation}
```

```admonish definition
**_Spacetime_** is a four-dimensional set, with elements labeled by three dimensions of space and one dimension of time.
A point $x^\mu = (ct, x, y, z)$ in spacetime is called an **_event_**.
The path of a particle is a curve through spacetime called a **_worldline_**.
A **_light cone_** at an event is the locus of paths that could be taken by light rays passing through the event.

Worldlines through an event can either be **_timelike_** (inside the light cone), **_spacelike_** (outside the light cone), or **_light-like_** (on the light cone).
The set of all events inside the light cone of an event $x^\mu$ are called **_timelike separated_** from $x^\mu$.
The set of all events outside the light cone of an event $x^\mu$ are called **_spacelike separated_** from $x^\mu$.
The set of all events on the light cone of an event $x^\mu$ are called **_light-like separated_** from $x^\mu$.
```

```admonish definition
An **_inertial frame_**, or **_inertial coordinates_**, is a coordinate system which is not accelerating.

We can check whether a coordinate system is inertial via a simple test: send a light ray at speed $c$ in a straight line from any point 1 to any other point 2, then send it back from point 2 to point 1 at the same speed $c$.
Then, if and only if the frame is inertial, an observer at point 1 will observe the light reaching point 2 halfway between the time the light ray left point 1 and the time it arrived back at point 1, regardless of the locations of point 1 and 2 and regardless of the speed $c$ of the light ray.
```

```admonish definition
The **_spacetime interval_** between two events is defined:

\begin{equation}
(\Delta s)^2 = -(c\Delta t)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2.
\end{equation}

The spacetime interval between two events is invariant under changes of inertial coordinates:

\begin{equation}
-(c\Delta t)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2 = -(c\Delta t')^2 + (\Delta x')^2 + (\Delta y')^2 + (\Delta z')^2,
\end{equation}

where $(t, x, y, z)$ and $(t', x', y', z')$ are two sets of inertial coordinates. By introducing the $4\times4$ matrix $\eta_{\mu\nu} := \text{diag}(-1, 1, 1, 1)$ called the **_metric_**, we can simplify this equation:

\begin{equation}
(\Delta s)^2 = -\eta_{\mu\nu}\Delta x^\mu \Delta x^\nu
\end{equation}
```

```admonish definition
The **_proper time_** $\tau$ is defined:

\begin{equation}
(\Delta \tau)^2 = -(\Delta s)^2 = -\eta_{\mu\nu}\Delta x^\mu \Delta x^\nu.
\end{equation}

The proper time between two events is the time elapsed by an observer moving on a straight line between the two events.

For more general, smooth paths between two events, the **_line element_** is used:

\begin{equation}
\dd s^2 = \eta_{\mu\nu} \dd x^\mu \dd x^\nu,
\end{equation}

where $x^\mu(\lambda)$ is a parameterized, smooth curve. The spacetime interval and proper time are then:

\begin{equation}
\Delta s = \int \sqrt{\eta_{\mu\nu}\dv{x^\mu}{\lambda}\dv{x^\nu}{\lambda}\dd\lambda}, \qq{and} \Delta\tau = \int \sqrt{-\eta_{\mu\nu}\dv{x^\mu}{\lambda}\dv{x^\nu}{\lambda}\dd\lambda}.
\end{equation}
```

## 1.3 - Lorentz Transformations

```admonish definition
There are two main classes of coordinate transformations: (1) 
```
