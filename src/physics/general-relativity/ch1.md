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

```admonish definition
**_Spacetime_** is a four-dimensional set, with elements labeled by three dimensions of space and one dimension of time.
A point $p = (t, x, y, z)$ in spacetime is called an **_event_**.
The path of a particle is a curve through spacetime called a **_worldline_**.
A **_light cone_** at an event is the locus of paths that could be taken by light rays passing through the event.

Worldlines through an event can either be **_timelike_** (inside the light cone), **_spacelike_** (outside the light cone), or **_light-like_** (on the light cone).
The set of all events inside the light cone of an event $p$ are called **_timelike separated_** from $p$.
The set of all events outside the light cone of an event $p$ are called **_spacelike separated_** from $p$.
The set of all events on the light cone of an event $p$ are called **_light-like separated_** from $p$.
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

where $(t, x, y, z)$ and $(t', x', y', z')$ are two sets of inertial coordinates.
```

```admonish note title="Einstein Notation"
Einstein notation uses greek indices as shorthand for spacetime coordinates and four-vectors:

\begin{equation}
x^\mu : \mqty{
  x^0 = ct \\\\
  x^1 = x \\\\
  x^2 = y \\\\
  x^3 = z.
}
\end{equation}

When only the spatial components of a four-vector are referred to, Latin indices are instead used:

\begin{equation}
x^i : \mqty{
  x^1 = x \\\\
  x^2 = y \\\\
  x^3 = z.
}
\end{equation}

The spacetime interval can also be written more concisely using this notation, by introducing a $4\cross4$ matrix called the **_metric_**:

\begin{equation}
\eta_{\mu\nu} = \mqty(\dmat{-1,1,1,1}).
\end{equation}

We then have:

\begin{equation}
(\Delta s)^2 = \eta_{\mu\nu}\Delta x^\mu \Delta x^\nu.
\end{equation}

The above equation uses the summation convention, which is an implied summation over indices appearing both as subscripts and superscripts.
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

where $x^\mu(\lambda)$ is a parameterized, smooth curve. The spacetime interval and propert time are then:

\begin{equation}
\Delta s = \int \sqrt{\eta_{\mu\nu}\dv{x^\mu}{\lambda}\dv{x^\nu}{\lambda}\dd\lambda}, \qq{and} \Delta\tau = \int \sqrt{-\eta_{\mu\nu}\dv{x^\mu}{\lambda}\dv{x^\nu}{\lambda}\dd\lambda}.
\end{equation}
```

## 1.3 - Lorentz Transformations
