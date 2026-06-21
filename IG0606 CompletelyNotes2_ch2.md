# IGCSE 0606 Additional Mathematics Comprehensive Notes — Second Edition

These notes are strictly written in accordance with the **Cambridge IGCSE Additional Mathematics (0606) 2028–2030 syllabus**. The Additional Mathematics course builds upon IGCSE Ordinary Mathematics, aiming to deepen understanding in algebra, functions, geometry, trigonometry, and calculus, laying a solid foundation for AS/A Level Further Mathematics, AP Calculus BC, and IB AA HL Mathematics.

Each chapter follows the structure: **Concept Definition → Formula Derivation → Worked Examples**. The examples are drawn from the style of past exam papers, with difficulty aligned to examination requirements.

> **Note**: Some formulas (e.g., sum formulas for arithmetic/geometric progressions, binomial expansion formula) are provided in the exam formula sheet, but these notes still present complete derivations to aid understanding rather than rote memorisation. In the exam, **understanding when to use which formula** is more important than memorising formulas.

---
> These notes are based on the Cambridge IGCSE Additional Mathematics (0606) 2025–2027 syllabus, arranged in a logical cognitive order, covering all topics. They include derivations, worked examples, and common pitfalls. Suitable for self-study.
- These notes are compiled and maintained by **LG-leo**. If you find them helpful, feel free to follow me or leave a ⭐ on GitHub — it helps me continue producing more free learning resources.
- My other course notes: https://github.com/LG-leo?tab=repositories

- This note is maintained by LG-leo. If you find it helpful, feel free to follow me or leave a ⭐ on GitHub. It helps me keep producing more free study resources. Check out my other notes: https://github.com/LG-leo?tab=repositories

---

## Table of Contents

- [Chapter 1: Sequences, Permutations, Combinations, and the Binomial Theorem](#chapter-1-sequences-permutations-combinations-and-the-binomial-theorem)
- [Chapter 2: Vectors and Rates of Change](#chapter-2-vectors-and-rates-of-change)
- [Chapter 3: Quadratic Functions (Including Polynomial Factors)](#chapter-3-quadratic-functions-including-polynomial-factors)
- [Chapter 4: Functions (Linear, Cubic, Exponential, Logarithmic)](#chapter-4-functions-linear-cubic-exponential-logarithmic)
- [Chapter 5: Differentiation (Derivatives)](#chapter-5-differentiation-derivatives)
- [Chapter 6: Equations and Inequalities (Graphical Methods)](#chapter-6-equations-and-inequalities-graphical-methods)
- [Chapter 7: Integration (Indefinite and Definite Integrals)](#chapter-7-integration-indefinite-and-definite-integrals)
- [Chapter 8: Trigonometry (Including Radians)](#chapter-8-trigonometry-including-radians)
- [Chapter 9: Geometry (Straight Lines and Circles)](#chapter-9-geometry-straight-lines-and-circles)
- [Chapter 10: Comprehensive Applications](#chapter-10-comprehensive-applications)

---

# Chapter 2: Vectors and Rates of Change

## Syllabus Mapping

This chapter covers the following sections of the Cambridge IGCSE Additional Mathematics (0606) 2028–2030 syllabus:

| Syllabus Ref | Content | Description |
|---------|------|------|
| **13.1** | Understand and use vector notation | Column vectors, $\mathbf{i}$-$\mathbf{j}$ form, $\overrightarrow{AB}$, $p$ form |
| **13.2** | Position vectors and unit vectors | Find unit vectors $\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$ |
| **13.3** | Magnitude, addition, subtraction and scalar multiplication of vectors | Including equal vectors, vector geometry problems (given diagrams) |
| **13.4** | Composition and resolution of velocities | Find resultant vectors, use velocity vectors to find position, collision problems |
| **14.1** | The idea of the derivative (introduction to rates of change) | Intuitive understanding of limits; differentiation from first principles is not required |

---

## Introduction

In the real world, many quantities have not only magnitude but also direction. From correcting for wind speed when flying an aeroplane, to determining whether two ships at sea might collide, to analysing the trajectory of a projectile — the mathematical language for all these problems is **vectors**.

This chapter builds a complete knowledge system for two-dimensional vectors from the ground up. We first learn the basic representation of vectors and rules of operation (including how to determine perpendicular vectors). Then we apply these tools to geometry problems and kinematics problems (composition of velocities, collision detection). Finally, we shift perspective from "static vectors" to "dynamic rates of change" — when a position vector changes over time, its rate of change is velocity, and the rate of change of velocity is acceleration. Conversely, given acceleration, we can find velocity and position through integration. This idea directly leads to differentiation in Chapter 5 and integration in Chapter 7.

---

## 2.1 Fundamentals of Two-Dimensional Vectors

### 2.1.1 What is a Vector?

A **vector** is a quantity that has both **magnitude** and **direction**. In contrast, a **scalar** has only magnitude, not direction. For example:

- **Vectors**: displacement, velocity, force
- **Scalars**: distance, speed, mass, temperature

In a two-dimensional plane, vectors can be represented in several equivalent ways.

#### Representation 1: Column Vector

$$
\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}
$$

where $x$ is the horizontal component and $y$ is the vertical component. This representation is very convenient for solving systems of equations, as we can operate directly on the components.

#### Representation 2: $\mathbf{i}$-$\mathbf{j}$ Form

Define two fundamental unit vectors:

$$
\mathbf{i} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \mathbf{j} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

$\mathbf{i}$ points in the positive $x$-axis direction (to the right), and $\mathbf{j}$ points in the positive $y$-axis direction (upwards). Then any vector can be written as:

$$
\mathbf{v} = x\mathbf{i} + y\mathbf{j}
$$

**Equivalence of the two representations**:

$$
x\mathbf{i} + y\mathbf{j} = \begin{pmatrix} x \\ y \end{pmatrix}
$$

For example, the vector $3\mathbf{i} - 2\mathbf{j}$ is the same vector as the column vector $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$.

#### Representation 3: Directed Line Segment

The vector from point $A$ to point $B$ is denoted by $\overrightarrow{AB}$. It equals the position of the endpoint minus the position of the starting point:

$$
\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A
$$

> **Why "endpoint minus starting point"?** Suppose you want to walk from home $A$ to school $B$. Your displacement (from $A$ to $B$) is your final position (the school's position) minus your starting position (home's position). If $A$ is at $(1,1)$ and $B$ is at $(4,5)$, then you need to go 3 units right and 4 units up, i.e., $\overrightarrow{AB} = (3,4)$.

---

### 2.1.2 Position Vectors

Let $O$ be the origin. The **position vector** of any point $P(x, y)$ is:

$$
\mathbf{r} = \overrightarrow{OP} = \begin{pmatrix} x \\ y \end{pmatrix} = x\mathbf{i} + y\mathbf{j}
$$

The position vector tells us where point $P$ is located relative to the origin. The key distinction here is: a **point** $P(x, y)$ is a location in space, while the **vector** $\mathbf{r} = (x, y)$ is a directed line segment from the origin to that point — it contains the information of displacement.

> **Difference between a point and a vector**: A point is a location, like a coordinate on a map. A vector is a displacement, like "3 steps right, 2 steps up." The same vector can start from any point, but the same point can only be at one location.

---

### 2.1.3 Magnitude of a Vector

The magnitude (or length, or size) of the vector $\mathbf{v} = x\mathbf{i} + y\mathbf{j}$ is given by the Pythagorean theorem:

$$
|\mathbf{v}| = \sqrt{x^2 + y^2}
$$

The magnitude is always a non-negative real number. It is zero if and only if the vector is the zero vector $\mathbf{0} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

> **Why $\sqrt{x^2 + y^2}$?** Consider the vector $\mathbf{v}$ as the line segment from the origin $(0,0)$ to the point $(x,y)$. This segment is the hypotenuse of a right-angled triangle whose legs have lengths $|x|$ and $|y|$. By the Pythagorean theorem, the length of the hypotenuse $= \sqrt{x^2 + y^2}$.

---

### 2.1.4 Unit Vectors

A **unit vector** is a vector with magnitude 1. Given any non-zero vector $\mathbf{v}$, we can construct a unit vector $\hat{\mathbf{v}}$ in the same direction:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}
$$

That is, we divide the original vector by its own magnitude. This operation is called **normalisation**.

> **Why is this defined this way?** Let $\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}$. Then
> $$
> |\hat{\mathbf{v}}| = \frac{|\mathbf{v}|}{|\mathbf{v}|} = 1
> $$
> The direction remains unchanged because we are dividing the original vector by a positive scalar.
>
> **Analogy**: It's like cutting a rope into unit-length pieces. If you have a 5-metre rope and cut it into 5 equal pieces, each piece is 1 metre long, with the same direction as the original.

---

### 2.1.5 Vector Addition and Subtraction

To add two vectors, we add their corresponding components separately:

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}
$$

Subtraction is similar:

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} - \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} = \begin{pmatrix} x_1 - x_2 \\ y_1 - y_2 \end{pmatrix}
$$

**Geometric meaning — Why the "parallelogram rule"?**

Imagine two people pulling a box at the same time. One person pulls with force $\mathbf{a}$ eastwards, and the other pulls with force $\mathbf{b}$ northwards. The resultant force actually experienced by the box is $\mathbf{a} + \mathbf{b}$.

- **Addition — Parallelogram Rule**: Using the two vectors as adjacent sides, construct a parallelogram. The diagonal starting from the common origin is their sum.
- **Subtraction — Triangle Rule**: $\mathbf{a} - \mathbf{b}$ is the vector from the tip of $\mathbf{b}$ to the tip of $\mathbf{a}$.

**Useful mnemonics**:
- For displacement vectors: **endpoint minus starting point**. The vector from $A$ to $B$ is $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$
- For addition: connect head to tail, from the first start to the last end

#### Geometric Derivation of the Parallelogram Rule

Why is vector addition defined by adding components? Let's prove the equivalence between the algebraic and geometric definitions.

**Theorem**: Let $\mathbf{a} = \begin{pmatrix} a_x \\ a_y \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} b_x \\ b_y \end{pmatrix}$. Then the diagonal of the parallelogram formed by $\mathbf{a}$ and $\mathbf{b}$ is $\mathbf{a} + \mathbf{b}$.

**Proof**:

Place $\mathbf{a}$ starting from the origin $O(0,0)$, so its endpoint is $A(a_x, a_y)$.
Place $\mathbf{b}$ also starting from $O$, so its endpoint is $B(b_x, b_y)$.

Now construct the parallelogram $OACB$:
- $OA$ is $\mathbf{a}$, so $A = (a_x, a_y)$
- $OB$ is $\mathbf{b}$, so $B = (b_x, b_y)$
- Since $OACB$ is a parallelogram, $\overrightarrow{AC} = \overrightarrow{OB} = \mathbf{b}$
- Therefore $C = A + \mathbf{b} = (a_x + b_x, a_y + b_y)$

Alternatively, $\overrightarrow{BC} = \overrightarrow{OA} = \mathbf{a}$, so $C = B + \mathbf{a} = (b_x + a_x, b_y + a_y)$, same result.

The diagonal $\overrightarrow{OC}$ from the origin to $C$ is:
$$
\overrightarrow{OC} = \begin{pmatrix} a_x + b_x \\ a_y + b_y \end{pmatrix} = \mathbf{a} + \mathbf{b}
$$

This proves that the diagonal of the parallelogram equals the component-wise sum. ✓

**Triangle Rule (alternative geometric view)**:
Place the tail of $\mathbf{b}$ at the head of $\mathbf{a}$. The vector from the tail of $\mathbf{a}$ to the head of $\mathbf{b}$ is $\mathbf{a} + \mathbf{b}$. This is equivalent to the parallelogram rule — the triangle formed is exactly half of the parallelogram.

**Commutativity of vector addition**:
$$
\mathbf{a} + \mathbf{b} = \begin{pmatrix} a_x + b_x \\ a_y + b_y \end{pmatrix} = \begin{pmatrix} b_x + a_x \\ b_y + a_y \end{pmatrix} = \mathbf{b} + \mathbf{a}
$$
So vector addition is commutative — the order does not matter.

**Associativity**: $(\mathbf{a} + \mathbf{b}) + \mathbf{c} = \mathbf{a} + (\mathbf{b} + \mathbf{c})$, because each component adds associatively.

**Subtraction as a special case of addition**:
$$
\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b}) = \mathbf{a} + (-1)\mathbf{b}
$$
Geometrically, $-\mathbf{b}$ is $\mathbf{b}$ reversed (rotated by $180^\circ$). So $\mathbf{a} - \mathbf{b}$ is the vector from the tip of $\mathbf{b}$ to the tip of $\mathbf{a}$ when both start from the same point.

**Proof**: Let both $\mathbf{a}$ and $\mathbf{b}$ start from $O$. Then the vector from the tip of $\mathbf{b}$ (point $B$) to the tip of $\mathbf{a}$ (point $A$) is:
$$
\overrightarrow{BA} = \mathbf{a} - \mathbf{b}
$$
So $\mathbf{a} - \mathbf{b}$ is the vector that, when added to $\mathbf{b}$, gives $\mathbf{a}$: $(\mathbf{a} - \mathbf{b}) + \mathbf{b} = \mathbf{a}$. ✓

---

### 2.1.6 Scalar Multiplication

Multiplying a vector by a scalar $c$ is equivalent to multiplying each component by $c$:

$$
c \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} cx \\ cy \end{pmatrix}
$$

Geometric effect of scalar multiplication:
- If $c > 0$, the vector is stretched ($c > 1$) or compressed ($0 < c < 1$) along its original direction
- If $c < 0$, the vector reverses direction

Magnitude after scalar multiplication:

$$
|c\mathbf{v}| = |c| \cdot |\mathbf{v}|
$$

> **Why does the magnitude multiply by $|c|$ instead of $c$?** Because if $c = -2$, the length of the vector becomes 2 times the original, and the direction reverses. Length is always positive, so we take $|c| = 2$.

---

### 2.1.7 Equal Vectors

Two vectors are equal if and only if their corresponding components are equal respectively. That is:

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} \iff x_1 = x_2 \quad \text{and} \quad y_1 = y_2
$$

This is called the **principle of equating like vectors** — it is the core tool for solving vector equations.

> **Why is this principle so useful?** A single vector equation actually contains two independent scalar equations (one for the $x$-component, one for the $y$-component). This allows us to solve for unknowns from two directions separately.

---

### 2.1.8 Perpendicular Vectors (Orthogonal Vectors)

#### What is Perpendicular?

Two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are perpendicular (or orthogonal) if and only if the angle between them is $90^\circ$.

#### How to Determine Perpendicularity? — The Dot Product

The **dot product (inner product)** of two vectors is defined as:

$$
\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y
$$

The dot product yields a **scalar** (not a vector), hence it is also called the "scalar product."

**Condition for perpendicularity**:

$$
\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0
$$

> **Why does a zero dot product imply perpendicularity?**
>
> From a geometric perspective, the dot product has an alternative equivalent definition:
> $$
> \mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos\theta
> $$
> where $\theta$ is the angle between the two vectors.
>
> Derivation of this equivalence: using the Law of Cosines. Let the angle between $\mathbf{u}$ and $\mathbf{v}$ be $\theta$. Then the magnitude of $\mathbf{u} - \mathbf{v}$ satisfies:
> $$
> |\mathbf{u} - \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2|\mathbf{u}||\mathbf{v}|\cos\theta
> $$
> Meanwhile, expanding the left side:
> $$
> |\mathbf{u} - \mathbf{v}|^2 = (u_x - v_x)^2 + (u_y - v_y)^2 = (u_x^2 + u_y^2) + (v_x^2 + v_y^2) - 2(u_x v_x + u_y v_y)
> $$
> Comparing the two expressions, we get:
> $$
> |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2|\mathbf{u}||\mathbf{v}|\cos\theta = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2(u_x v_x + u_y v_y)
> $$
> Therefore $u_x v_x + u_y v_y = |\mathbf{u}||\mathbf{v}|\cos\theta$.
>
> When $\theta = 90^\circ$, $\cos 90^\circ = 0$, so the dot product is zero.

#### Horizontal and Vertical Vectors

A special case: a **horizontal vector** has zero $y$-component, i.e., $\mathbf{h} = (h_x, 0)$ ($h_x \neq 0$), and its direction is parallel to the $x$-axis. A **vertical vector** has zero $x$-component, i.e., $\mathbf{v} = (0, v_y)$ ($v_y \neq 0$), and its direction is parallel to the $y$-axis.

A horizontal vector is always perpendicular to a vertical vector. Verification using the dot product:

$$
(h_x, 0) \cdot (0, v_y) = h_x \cdot 0 + 0 \cdot v_y = 0
$$

#### Determining Perpendicularity Using Slope

If two non-zero vectors are not parallel to the axes (i.e., neither $x$ nor $y$ components are zero), we can also use slopes to determine perpendicularity. Let the slope of vector $\mathbf{u}$ be $k_1 = \frac{u_y}{u_x}$ and the slope of vector $\mathbf{v}$ be $k_2 = \frac{v_y}{v_x}$. Then:

$$
\mathbf{u} \perp \mathbf{v} \iff k_1 \cdot k_2 = -1
$$

> **Derivation**: From the condition for a zero dot product:
> $$
> u_x v_x + u_y v_y = 0 \implies u_x v_x = -u_y v_y \implies \frac{u_y}{u_x} \cdot \frac{v_y}{v_x} = -1
> $$
> i.e., $k_1 \cdot k_2 = -1$.

> **Note on the zero vector**: The zero vector $\mathbf{0} = (0, 0)$ has no fixed direction. By convention, in technical discussions it is considered to be both parallel and perpendicular to all vectors, but in practical problem-solving we generally exclude it.

#### Dot Product Properties — A Deeper Look

The dot product has several important algebraic properties (for any vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}$ and scalar $c$):

| Property | Formula |
|:---|:---|
| Commutativity | $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ |
| Distributivity | $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$ |
| Scalar multiplication | $(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v})$ |
| Self dot product | $\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2$ |

**Derivation of commutativity**:
$$
\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y = v_x u_x + v_y u_y = \mathbf{v} \cdot \mathbf{u}
$$

**Derivation of self dot product**:
$$
\mathbf{u} \cdot \mathbf{u} = u_x^2 + u_y^2 = |\mathbf{u}|^2
$$
This provides a quick way to compute the squared magnitude: $|\mathbf{u}|^2 = \mathbf{u} \cdot \mathbf{u}$.

#### Finding the Angle Between Two Vectors

From the geometric definition $\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$, we can solve for $\theta$:

$$
\boxed{\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}||\mathbf{v}|}}
$$

This formula is extremely useful:
- If $\cos\theta = 0$, then $\theta = 90^\circ$ (perpendicular)
- If $\cos\theta = 1$, then $\theta = 0^\circ$ (same direction, parallel)
- If $\cos\theta = -1$, then $\theta = 180^\circ$ (opposite direction, parallel)
- If $\cos\theta > 0$, the angle is acute ($< 90^\circ$)
- If $\cos\theta < 0$, the angle is obtuse ($> 90^\circ$)

> **Why does the sign of the dot product tell us about the angle?** Since $|\mathbf{u}||\mathbf{v}| > 0$ (for non-zero vectors), the sign of $\mathbf{u} \cdot \mathbf{v}$ is the same as the sign of $\cos\theta$. So:
> - $\mathbf{u} \cdot \mathbf{v} > 0 \iff$ acute angle
> - $\mathbf{u} \cdot \mathbf{v} = 0 \iff$ right angle
> - $\mathbf{u} \cdot \mathbf{v} < 0 \iff$ obtuse angle

#### Projection of One Vector onto Another

The **scalar projection** of $\mathbf{u}$ onto $\mathbf{v}$ (i.e., the length of the "shadow" of $\mathbf{u}$ on the line of $\mathbf{v}$) is:

$$
\text{proj}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{v}|}
$$

**Derivation**: From the right triangle, the adjacent side length is $|\mathbf{u}|\cos\theta$. Using $\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$:
$$
|\mathbf{u}|\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{v}|}
$$

---

### 📌 Worked Examples 2.1: Basic Vector Operations

**Example 1** (Vector representation, magnitude, and unit vector)

Given two points $A(1, 2)$ and $B(5, -1)$.

(a) Find the vector $\overrightarrow{AB}$ in $\mathbf{i}$-$\mathbf{j}$ form.
(b) Find $|\overrightarrow{AB}|$.
(c) Find the unit vector in the same direction as $\overrightarrow{AB}$.

**Solution approach**:
- The vector from $A$ to $B$ = position of $B$ minus position of $A$
- Magnitude = square root of the sum of squares of the components
- Unit vector = original vector divided by its magnitude

**Solution**:

(a)
$$
\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A = (5\mathbf{i} - \mathbf{j}) - (\mathbf{i} + 2\mathbf{j}) = (5-1)\mathbf{i} + (-1-2)\mathbf{j} = 4\mathbf{i} - 3\mathbf{j}
$$

(b)
$$
|\overrightarrow{AB}| = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

(c) The unit vector in the same direction is:

$$
\hat{\mathbf{v}} = \frac{4\mathbf{i} - 3\mathbf{j}}{5} = \frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}
$$

Verification of magnitude: $\sqrt{(4/5)^2 + (-3/5)^2} = \sqrt{16/25 + 9/25} = \sqrt{25/25} = 1$. ✓

---

**Example 2** (Vector addition, scalar multiplication, and equal vectors — solving systems of equations)

Given $\mathbf{a} = 2\mathbf{i} + 3\mathbf{j}$, $\mathbf{b} = -\mathbf{i} + 2\mathbf{j}$. Find:

(a) $\mathbf{a} + \mathbf{b}$
(b) $2\mathbf{a} - 3\mathbf{b}$
(c) Real numbers $p$ and $q$ such that $p\mathbf{a} + q\mathbf{b} = 7\mathbf{i} + 8\mathbf{j}$

**Solution approach**:
- Addition and scalar multiplication operate on components separately
- For part (c), first expand the left side, then use the principle of equating like vectors (coefficients of $\mathbf{i}$ and $\mathbf{j}$ must be equal respectively) to set up a system of equations

**Solution**:

(a)
$$
\mathbf{a} + \mathbf{b} = (2\mathbf{i} + 3\mathbf{j}) + (-\mathbf{i} + 2\mathbf{j}) = (2-1)\mathbf{i} + (3+2)\mathbf{j} = \mathbf{i} + 5\mathbf{j}
$$

(b)
$$
2\mathbf{a} - 3\mathbf{b} = 2(2\mathbf{i} + 3\mathbf{j}) - 3(-\mathbf{i} + 2\mathbf{j}) = (4\mathbf{i} + 6\mathbf{j}) + (3\mathbf{i} - 6\mathbf{j}) = 7\mathbf{i} + 0\mathbf{j} = 7\mathbf{i}
$$

(c) Let $p\mathbf{a} + q\mathbf{b} = 7\mathbf{i} + 8\mathbf{j}$, i.e.:

$$
p(2\mathbf{i} + 3\mathbf{j}) + q(-\mathbf{i} + 2\mathbf{j}) = 7\mathbf{i} + 8\mathbf{j}
$$

First expand the brackets:

$$
2p\mathbf{i} + 3p\mathbf{j} - q\mathbf{i} + 2q\mathbf{j} = 7\mathbf{i} + 8\mathbf{j}
$$

Combine the coefficients of $\mathbf{i}$ and $\mathbf{j}$:

$$
(2p - q)\mathbf{i} + (3p + 2q)\mathbf{j} = 7\mathbf{i} + 8\mathbf{j}
$$

Using the principle of equating like vectors, the coefficients of $\mathbf{i}$ must be equal, and the coefficients of $\mathbf{j}$ must be equal:

$$
\begin{cases}
2p - q = 7 \quad \text{(① equate }\mathbf{i}\text{ coefficients)} \\[4pt]
3p + 2q = 8 \quad \text{(② equate }\mathbf{j}\text{ coefficients)}
\end{cases}
$$

Solve this system. From ①, $q = 2p - 7$. Substituting into ②:

$$
3p + 2(2p - 7) = 8 \implies 3p + 4p - 14 = 8 \implies 7p = 22 \implies p = \frac{22}{7}
$$

Then $q = 2 \times \frac{22}{7} - 7 = \frac{44}{7} - \frac{49}{7} = -\frac{5}{7}$.

Therefore $p = \frac{22}{7}$, $q = -\frac{5}{7}$. ✓

---

**Example 3** (Position vectors, displacement, and determining perpendicular vectors)

Three points $P$, $Q$, $R$ have position vectors $\mathbf{p} = 3\mathbf{i} + \mathbf{j}$, $\mathbf{q} = 5\mathbf{i} - 2\mathbf{j}$, $\mathbf{r} = -2\mathbf{i} + 4\mathbf{j}$ respectively.

(a) Find $\overrightarrow{PQ}$ and $\overrightarrow{PR}$.
(b) Given $\overrightarrow{PS} = 2\overrightarrow{PQ}$, find the position vector of $S$.
(c) Determine whether $\overrightarrow{PQ}$ is perpendicular to $\overrightarrow{PR}$.

**Solution approach**:
- $\overrightarrow{PQ} = \mathbf{q} - \mathbf{p}$ (endpoint minus starting point)
- $\overrightarrow{PS} = \mathbf{s} - \mathbf{p}$, substitute the given condition to solve for $\mathbf{s}$
- Perpendicularity check: compute the dot product; if zero, they are perpendicular

**Solution**:

(a)
$$
\overrightarrow{PQ} = \mathbf{q} - \mathbf{p} = (5\mathbf{i} - 2\mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = 2\mathbf{i} - 3\mathbf{j}
$$

$$
\overrightarrow{PR} = \mathbf{r} - \mathbf{p} = (-2\mathbf{i} + 4\mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = -5\mathbf{i} + 3\mathbf{j}
$$

(b) Let the position vector of $S$ be $\mathbf{s}$. Since $\overrightarrow{PS} = \mathbf{s} - \mathbf{p}$ and $\overrightarrow{PS} = 2\overrightarrow{PQ}$:

$$
\mathbf{s} - \mathbf{p} = 2(2\mathbf{i} - 3\mathbf{j}) = 4\mathbf{i} - 6\mathbf{j}
$$

Therefore:

$$
\mathbf{s} = \mathbf{p} + (4\mathbf{i} - 6\mathbf{j}) = (3\mathbf{i} + \mathbf{j}) + (4\mathbf{i} - 6\mathbf{j}) = 7\mathbf{i} - 5\mathbf{j}
$$

So $S$ has coordinates $(7, -5)$.

(c) Compute the dot product:

$$
\overrightarrow{PQ} \cdot \overrightarrow{PR} = (2)(-5) + (-3)(3) = -10 - 9 = -19 \neq 0
$$

Since the dot product is non-zero, $\overrightarrow{PQ}$ and $\overrightarrow{PR}$ are **not perpendicular**.

> **Verification using the slope method**:
> $k_{PQ} = \dfrac{-3}{2} = -1.5$
> $k_{PR} = \dfrac{3}{-5} = -0.6$
> $k_{PQ} \cdot k_{PR} = (-1.5)(-0.6) = 0.9 \neq -1$
> This also shows they are not perpendicular. ✓

---

**Example 4** (Finding the angle between two vectors using dot product)

Given $\mathbf{a} = 3\mathbf{i} + 4\mathbf{j}$ and $\mathbf{b} = \mathbf{i} - 2\mathbf{j}$. Find:

(a) $\mathbf{a} \cdot \mathbf{b}$
(b) The angle $\theta$ between $\mathbf{a}$ and $\mathbf{b}$, correct to the nearest $0.1^\circ$
(c) The scalar projection of $\mathbf{a}$ onto $\mathbf{b}$

**Solution approach**:
- Dot product = sum of products of corresponding components
- Angle: use $\cos\theta = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}$
- Projection: $\dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}$

**Solution**:

(a)
$$
\mathbf{a} \cdot \mathbf{b} = (3)(1) + (4)(-2) = 3 - 8 = -5
$$

(b) First compute the magnitudes:
$$
|\mathbf{a}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$
$$
|\mathbf{b}| = \sqrt{1^2 + (-2)^2} = \sqrt{1 + 4} = \sqrt{5}
$$

Then:
$$
\cos\theta = \frac{-5}{5 \times \sqrt{5}} = \frac{-5}{5\sqrt{5}} = -\frac{1}{\sqrt{5}} = -\frac{\sqrt{5}}{5} \approx -0.4472
$$

$$
\theta = \arccos\left(-\frac{\sqrt{5}}{5}\right) \approx 116.6^\circ
$$

Since $\cos\theta < 0$, the angle is obtuse ($> 90^\circ$), which makes sense — the dot product was negative.

(c) Scalar projection of $\mathbf{a}$ onto $\mathbf{b}$:
$$
\text{proj}_{\mathbf{b}}\mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|} = \frac{-5}{\sqrt{5}} = -\sqrt{5} \approx -2.236
$$

The negative sign means the projection points in the opposite direction to $\mathbf{b}$ — which is consistent with the obtuse angle.

---

**Example 5** (Finding an unknown component to satisfy a perpendicular condition)

Given $\mathbf{u} = 2\mathbf{i} + k\mathbf{j}$ and $\mathbf{v} = 3\mathbf{i} - 4\mathbf{j}$. Find the value of $k$ such that:

(a) $\mathbf{u}$ is perpendicular to $\mathbf{v}$
(b) $\mathbf{u}$ is parallel to $\mathbf{v}$

**Solution approach**:
- Perpendicular: $\mathbf{u} \cdot \mathbf{v} = 0$
- Parallel: components must be proportional, i.e., $\dfrac{u_x}{v_x} = \dfrac{u_y}{v_y}$

**Solution**:

(a) For perpendicularity:
$$
\mathbf{u} \cdot \mathbf{v} = (2)(3) + (k)(-4) = 6 - 4k = 0
$$
$$
4k = 6 \implies k = \frac{3}{2}
$$

**Verification**: When $k = \frac{3}{2}$, $\mathbf{u} = 2\mathbf{i} + \frac{3}{2}\mathbf{j}$.
Using slopes: $k_u = \dfrac{3/2}{2} = \dfrac{3}{4}$, $k_v = \dfrac{-4}{3}$, product $= \dfrac{3}{4} \times \dfrac{-4}{3} = -1$. ✓

(b) For parallelism, the ratio of components must be equal:
$$
\frac{2}{3} = \frac{k}{-4}
$$

Cross-multiply:
$$
2(-4) = 3k \implies -8 = 3k \implies k = -\frac{8}{3}
$$

**Verification**: When $k = -\frac{8}{3}$, $\mathbf{u} = 2\mathbf{i} - \frac{8}{3}\mathbf{j} = \frac{2}{3}(3\mathbf{i} - 4\mathbf{j}) = \frac{2}{3}\mathbf{v}$. ✓

---

**Example 6** (Complex system of vector equations — finding unknown coefficients)

Given $\mathbf{p} = \mathbf{i} + 2\mathbf{j}$ and $\mathbf{q} = 3\mathbf{i} - \mathbf{j}$. Find scalars $\alpha$ and $\beta$ such that:
$$
\alpha(\mathbf{p} + \mathbf{q}) + \beta(\mathbf{p} - \mathbf{q}) = 5\mathbf{i} + 11\mathbf{j}
$$

**Solution approach**:
1. First compute $\mathbf{p} + \mathbf{q}$ and $\mathbf{p} - \mathbf{q}$
2. Substitute into the equation and expand
3. Equate $\mathbf{i}$ and $\mathbf{j}$ coefficients to form a system
4. Solve for $\alpha$ and $\beta$

**Solution**:

First:
$$
\mathbf{p} + \mathbf{q} = (\mathbf{i} + 2\mathbf{j}) + (3\mathbf{i} - \mathbf{j}) = 4\mathbf{i} + \mathbf{j}
$$
$$
\mathbf{p} - \mathbf{q} = (\mathbf{i} + 2\mathbf{j}) - (3\mathbf{i} - \mathbf{j}) = -2\mathbf{i} + 3\mathbf{j}
$$

Substitute:
$$
\alpha(4\mathbf{i} + \mathbf{j}) + \beta(-2\mathbf{i} + 3\mathbf{j}) = 5\mathbf{i} + 11\mathbf{j}
$$

Expand:
$$
(4\alpha - 2\beta)\mathbf{i} + (\alpha + 3\beta)\mathbf{j} = 5\mathbf{i} + 11\mathbf{j}
$$

Equate coefficients:
$$
\begin{cases}
4\alpha - 2\beta = 5 \quad \text{(① } \mathbf{i} \text{ coefficients)} \\[4pt]
\alpha + 3\beta = 11 \quad \text{(② } \mathbf{j} \text{ coefficients)}
\end{cases}
$$

From ②: $\alpha = 11 - 3\beta$. Substitute into ①:
$$
4(11 - 3\beta) - 2\beta = 5 \implies 44 - 12\beta - 2\beta = 5 \implies -14\beta = -39 \implies \beta = \frac{39}{14}
$$

Then:
$$
\alpha = 11 - 3 \times \frac{39}{14} = 11 - \frac{117}{14} = \frac{154}{14} - \frac{117}{14} = \frac{37}{14}
$$

Therefore $\alpha = \dfrac{37}{14}$, $\beta = \dfrac{39}{14}$. ✓

**Verification**:
$4\alpha - 2\beta = 4 \times \frac{37}{14} - 2 \times \frac{39}{14} = \frac{148}{14} - \frac{78}{14} = \frac{70}{14} = 5$ ✓
$\alpha + 3\beta = \frac{37}{14} + 3 \times \frac{39}{14} = \frac{37 + 117}{14} = \frac{154}{14} = 11$ ✓

---

## 2.2 Practical Applications of Vectors

### 2.2.1 Vector Geometry — In-Depth Analysis

Vectors are a powerful tool for solving plane geometry problems. By converting geometric relationships into vector equations, we can use algebraic methods to obtain precise solutions, avoiding the imprecision of drawing diagrams.

#### Core Idea

**The essence of vector geometry**: using vector operations (addition, subtraction, scalar multiplication) to represent geometric relationships.

| Geometric Relationship | Vector Expression |
|:---|:---|
| Line segment from $A$ to $B$ | $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$ |
| Midpoint $M$ of $A$ and $B$ | $\mathbf{r}_M = \dfrac{\mathbf{r}_A + \mathbf{r}_B}{2}$ |
| $P$ divides $AB$ in the ratio $m:n$ | $\mathbf{r}_P = \dfrac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}$ |
| $AB \parallel CD$ | $\overrightarrow{AB} = k \cdot \overrightarrow{CD}$ |
| $AB \perp CD$ | $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$ |
| $A,B,C$ are collinear | $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$ (there exists $k$) |

#### Midpoint Formula — Why Does It Work?

Let $M$ be the midpoint of $AB$. The displacement from $A$ to $M$ is half of $\overrightarrow{AB}$:

$$
\mathbf{r}_M = \mathbf{r}_A + \frac{1}{2}\overrightarrow{AB} = \mathbf{r}_A + \frac{1}{2}(\mathbf{r}_B - \mathbf{r}_A) = \frac{2\mathbf{r}_A + \mathbf{r}_B - \mathbf{r}_A}{2} = \frac{\mathbf{r}_A + \mathbf{r}_B}{2}
$$

#### Section Formula — Detailed Derivation

Let point $P$ divide segment $AB$ in the ratio $AP:PB = m:n$ (i.e., from $A$ towards $B$, $AP$ occupies $m$ parts and $PB$ occupies $n$ parts).

This means $P$ is located at $\dfrac{m}{m+n}$ of the way from $A$ to $B$ (counting from $A$). Therefore:

$$
\begin{aligned}
\mathbf{r}_P &= \mathbf{r}_A + \frac{m}{m+n}\overrightarrow{AB} \\
&= \mathbf{r}_A + \frac{m}{m+n}(\mathbf{r}_B - \mathbf{r}_A) \\
&= \frac{(m+n)\mathbf{r}_A + m\mathbf{r}_B - m\mathbf{r}_A}{m+n} \\
&= \frac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}
\end{aligned}
$$

> **Memory tip**: In the section formula, the coefficient of $A$ is $n$ (the ratio on the opposite side), and the coefficient of $B$ is $m$ (the ratio on the opposite side). Cross-multiply!
>
> For example, if $AP:PB = 2:3$ ($m=2, n=3$), then:
> $$ \mathbf{r}_P = \frac{3\mathbf{r}_A + 2\mathbf{r}_B}{5} $$
> The coefficient of $A$ is $3$ (the opposite side $PB$ is $3$ parts), and the coefficient of $B$ is $2$ (the opposite side $AP$ is $2$ parts).

#### Parallel Vectors

Two non-zero vectors $\mathbf{a}$ and $\mathbf{b}$ are parallel (i.e., have the same or opposite direction) if and only if there exists a real number $k$ such that:

$$
\mathbf{a} = k\mathbf{b}
$$

That is, one vector is a scalar multiple of the other.

> **How to check for parallelism?** Check if the corresponding components of the two vectors are proportional:
> If $\mathbf{a} = (a_x, a_y)$ and $\mathbf{b} = (b_x, b_y)$, and $\frac{a_x}{b_x} = \frac{a_y}{b_y}$ (denominator non-zero), then they are parallel.
> Note that this ratio can be negative (indicating opposite directions).

#### Testing for Collinearity of Three Points

Three points $A$, $B$, $C$ are collinear if and only if $\overrightarrow{AB}$ is parallel to $\overrightarrow{AC}$ (or $\overrightarrow{AB}$ is parallel to $\overrightarrow{BC}$).

**Why?** If three points are collinear, then the displacements from $A$ to $B$ and from $A$ to $C$ are in the same or opposite direction, i.e., there exists a scalar $k$ such that $\overrightarrow{AC} = k \cdot \overrightarrow{AB}$.

---

### 📌 Worked Examples 2.2: Vector Geometry Applications

**Example 1** (Parallelogram and Midpoint — illustrated)

In parallelogram $ABCD$, the position vectors of $A$, $B$, $C$ are $\mathbf{a} = \mathbf{i} + 2\mathbf{j}$, $\mathbf{b} = 4\mathbf{i} + 3\mathbf{j}$, $\mathbf{c} = 6\mathbf{i} + \mathbf{j}$ respectively. Find:

(a) The position vector of $D$
(b) The position vector of $M$, the intersection point of the diagonals $AC$ and $BD$

**Solution approach**:

> First understand the structure of the parallelogram. The vertices are arranged in order $A \to B \to C \to D \to A$.
>
> **Key property of a parallelogram**: Opposite sides are parallel and equal.
> - $AB \parallel DC$ and $AB = DC$
> - $AD \parallel BC$ and $AD = BC$
>
> This means $\overrightarrow{AD} = \overrightarrow{BC}$ or $\overrightarrow{AB} = \overrightarrow{DC}$.
>
> Additionally, the diagonals of a parallelogram **bisect each other**, i.e., the midpoint of $AC$ = the midpoint of $BD$.

**Solution**:

(a) In parallelogram $ABCD$, opposite sides $AD$ and $BC$ are parallel and equal, so $\overrightarrow{AD} = \overrightarrow{BC}$.

First find $\overrightarrow{BC} = \mathbf{c} - \mathbf{b}$:

$$
\overrightarrow{BC} = (6\mathbf{i} + \mathbf{j}) - (4\mathbf{i} + 3\mathbf{j}) = 2\mathbf{i} - 2\mathbf{j}
$$

Since $\overrightarrow{AD} = \overrightarrow{BC} = 2\mathbf{i} - 2\mathbf{j}$, and $\overrightarrow{AD} = \mathbf{d} - \mathbf{a}$:

$$
\mathbf{d} = \mathbf{a} + \overrightarrow{AD} = (\mathbf{i} + 2\mathbf{j}) + (2\mathbf{i} - 2\mathbf{j}) = 3\mathbf{i}
$$

So $D$ has coordinates $(3, 0)$.

**Verification**: We can also use $\overrightarrow{AB} = \overrightarrow{DC}$.
$\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (4\mathbf{i} + 3\mathbf{j}) - (\mathbf{i} + 2\mathbf{j}) = 3\mathbf{i} + \mathbf{j}$
$\overrightarrow{DC} = \mathbf{c} - \mathbf{d}$, so $\mathbf{c} - \mathbf{d} = 3\mathbf{i} + \mathbf{j}$, giving $\mathbf{d} = \mathbf{c} - (3\mathbf{i} + \mathbf{j}) = (6\mathbf{i} + \mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = 3\mathbf{i}$, consistent. ✓

(b) The diagonals of a parallelogram bisect each other. Therefore $M$ is both the midpoint of $AC$ and the midpoint of $BD$.

Using the midpoint of $AC$:

$$
\mathbf{m} = \frac{\mathbf{a} + \mathbf{c}}{2} = \frac{(\mathbf{i} + 2\mathbf{j}) + (6\mathbf{i} + \mathbf{j})}{2} = \frac{7\mathbf{i} + 3\mathbf{j}}{2} = 3.5\mathbf{i} + 1.5\mathbf{j}
$$

Verification using the midpoint of $BD$: $\frac{\mathbf{b} + \mathbf{d}}{2} = \frac{(4\mathbf{i} + 3\mathbf{j}) + 3\mathbf{i}}{2} = \frac{7\mathbf{i} + 3\mathbf{j}}{2}$, consistent. ✓

---

**Example 2** (Collinearity test and ratio — how to prove three points are collinear)

Three points $A$, $B$, $C$ have position vectors $\mathbf{a} = 2\mathbf{i} + \mathbf{j}$, $\mathbf{b} = 5\mathbf{i} + 4\mathbf{j}$, $\mathbf{c} = 8\mathbf{i} + 7\mathbf{j}$ respectively.

(a) Prove that $A$, $B$, $C$ are collinear.
(b) Find the ratio $AB:BC$.

**Solution approach**:

> Standard method for proving three points are collinear:
> 1. Compute $\overrightarrow{AB}$ and $\overrightarrow{BC}$ (or $\overrightarrow{AB}$ and $\overrightarrow{AC}$)
> 2. Determine whether they are parallel (i.e., whether there exists a scalar $k$ such that one equals the other multiplied by $k$)
> 3. If they are parallel and share a common point ($B$ is the common point of $\overrightarrow{AB}$ and $\overrightarrow{BC}$), then the three points are collinear

**Solution**:

(a) Compute the vectors:

$$
\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 4\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 3\mathbf{i} + 3\mathbf{j}
$$

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (8\mathbf{i} + 7\mathbf{j}) - (5\mathbf{i} + 4\mathbf{j}) = 3\mathbf{i} + 3\mathbf{j}
$$

Observe that $\overrightarrow{BC} = \overrightarrow{AB}$, i.e., $\overrightarrow{BC} = 1 \cdot \overrightarrow{AB}$. There exists a scalar $k = 1$ such that $\overrightarrow{BC} = k\overrightarrow{AB}$, so $\overrightarrow{AB} \parallel \overrightarrow{BC}$. Since both vectors pass through point $B$, $A$, $B$, $C$ are collinear.

> **Note**: We can also verify the relationship between $\overrightarrow{AC}$ and $\overrightarrow{AB}$.
> $\overrightarrow{AC} = \mathbf{c} - \mathbf{a} = (8\mathbf{i} + 7\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 6\mathbf{i} + 6\mathbf{j} = 2(3\mathbf{i} + 3\mathbf{j}) = 2\overrightarrow{AB}$
> This also leads to the same conclusion of collinearity.

(b) Since $\overrightarrow{BC} = \overrightarrow{AB}$ and they have the same direction, $\overrightarrow{AB}$ and $\overrightarrow{BC}$ have equal lengths. That is, $AB = BC$, therefore $AB:BC = 1:1$.

In other words, $B$ is the midpoint of segment $AC$.

---

**Example 3** (Section formula + perpendicularity check — comprehensive application)

In $\triangle OAB$, $C$ lies on $OA$ such that $OC:CA = 2:1$, and $D$ lies on $AB$ such that $AD:DB = 3:1$. Let $\overrightarrow{OA} = \mathbf{a}$, $\overrightarrow{OB} = \mathbf{b}$.

(a) Express $\overrightarrow{OD}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.
(b) Express $\overrightarrow{CD}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.
(c) Given that $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$ and $\mathbf{b} = \mathbf{i} + 6\mathbf{j}$, determine whether $\overrightarrow{OC}$ is perpendicular to $\overrightarrow{OD}$.

**Solution approach**:

> This is a classic "express vectors in terms of a basis" problem. $\mathbf{a}$ and $\mathbf{b}$ are the basis vectors; all other vectors must be expressed in terms of them.
>
> Key steps:
> 1. Determine the position of point $C$ on $OA$: $OC:CA = 2:1$ means $OC = \frac{2}{3}OA$
> 2. Determine the position of point $D$ on $AB$: $AD:DB = 3:1$ means $AD = \frac{3}{4}AB$
> 3. Use the section formula or direct addition/subtraction to express the vectors
> 4. Perpendicularity check: substitute the numerical values and compute the dot product

**Solution**:

(a) First, express the position of $D$.

Method 1 (Section formula): $D$ divides $AB$ in the ratio $AD:DB = 3:1$, i.e., from $A$ towards $B$, $D$ is located at $\frac{3}{4}$ of the way.

Using the section formula ($m=3, n=1$):

$$
\mathbf{r}_D = \frac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n} = \frac{1 \cdot \mathbf{a} + 3 \cdot \mathbf{b}}{3+1} = \frac{\mathbf{a} + 3\mathbf{b}}{4}
$$

Method 2 (Direct approach): Starting from $A$, go $\frac{3}{4}$ of the way to $B$.

$$
\overrightarrow{OD} = \overrightarrow{OA} + \frac{3}{4}\overrightarrow{AB}
$$

And $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \mathbf{b} - \mathbf{a}$, so:

$$
\overrightarrow{OD} = \mathbf{a} + \frac{3}{4}(\mathbf{b} - \mathbf{a}) = \mathbf{a} + \frac{3}{4}\mathbf{b} - \frac{3}{4}\mathbf{a} = \frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}
$$

Note that $\frac{\mathbf{a} + 3\mathbf{b}}{4} = \frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}$, both methods give the same result. ✓

(b) $C$ lies on $OA$ with $OC:CA = 2:1$, so $C$ divides $\overrightarrow{OA}$ in the ratio $2:1$ (counting from $O$). Therefore:

$$
\overrightarrow{OC} = \frac{2}{3}\overrightarrow{OA} = \frac{2}{3}\mathbf{a}
$$

Then:

$$
\overrightarrow{CD} = \overrightarrow{OD} - \overrightarrow{OC} = \left(\frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}\right) - \frac{2}{3}\mathbf{a}
$$

Compute the coefficient of $\mathbf{a}$ by finding a common denominator: $\frac{1}{4} - \frac{2}{3} = \frac{3}{12} - \frac{8}{12} = -\frac{5}{12}$.

So:

$$
\overrightarrow{CD} = -\frac{5}{12}\mathbf{a} + \frac{3}{4}\mathbf{b}
$$

(c) Substitute $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$, $\mathbf{b} = \mathbf{i} + 6\mathbf{j}$:

First find $\overrightarrow{OC}$:

$$
\overrightarrow{OC} = \frac{2}{3}(3\mathbf{i} + 2\mathbf{j}) = 2\mathbf{i} + \frac{4}{3}\mathbf{j}
$$

Then find $\overrightarrow{OD}$:

$$
\begin{aligned}
\overrightarrow{OD} &= \frac{1}{4}(3\mathbf{i} + 2\mathbf{j}) + \frac{3}{4}(\mathbf{i} + 6\mathbf{j}) \\
&= \left(\frac{3}{4} + \frac{3}{4}\right)\mathbf{i} + \left(\frac{1}{2} + \frac{9}{2}\right)\mathbf{j} \\
&= \frac{6}{4}\mathbf{i} + \frac{10}{2}\mathbf{j} \\
&= \frac{3}{2}\mathbf{i} + 5\mathbf{j}
\end{aligned}
$$

Compute the dot product:

$$
\overrightarrow{OC} \cdot \overrightarrow{OD} = \left(2\right)\left(\frac{3}{2}\right) + \left(\frac{4}{3}\right)(5) = 3 + \frac{20}{3} = \frac{9}{3} + \frac{20}{3} = \frac{29}{3} \neq 0
$$

The dot product is non-zero, so $\overrightarrow{OC}$ and $\overrightarrow{OD}$ are **not perpendicular**.

---

**Example 4** (Proving a quadrilateral is a parallelogram + finding centroid)

Four points have position vectors:
$\mathbf{a} = \mathbf{i} + \mathbf{j}$, $\mathbf{b} = 4\mathbf{i} + 2\mathbf{j}$, $\mathbf{c} = 5\mathbf{i} + 5\mathbf{j}$, $\mathbf{d} = 2\mathbf{i} + 4\mathbf{j}$.

(a) Prove that $ABCD$ is a parallelogram.
(b) Find the position vector of the centroid (intersection of diagonals).
(c) Find the position vectors of the midpoints of all four sides, and show they form a parallelogram.

**Solution approach**:
- For a parallelogram: opposite sides must be parallel and equal, i.e., $\overrightarrow{AB} = \overrightarrow{DC}$
- Centroid = midpoint of either diagonal
- Midpoint of a side = average of endpoint position vectors

**Solution**:

(a) Compute the side vectors:
$$
\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (4\mathbf{i} + 2\mathbf{j}) - (\mathbf{i} + \mathbf{j}) = 3\mathbf{i} + \mathbf{j}
$$
$$
\overrightarrow{DC} = \mathbf{c} - \mathbf{d} = (5\mathbf{i} + 5\mathbf{j}) - (2\mathbf{i} + 4\mathbf{j}) = 3\mathbf{i} + \mathbf{j}
$$

Since $\overrightarrow{AB} = \overrightarrow{DC}$, sides $AB$ and $DC$ are parallel and equal.

Also check the other pair:
$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (5\mathbf{i} + 5\mathbf{j}) - (4\mathbf{i} + 2\mathbf{j}) = \mathbf{i} + 3\mathbf{j}
$$
$$
\overrightarrow{AD} = \mathbf{d} - \mathbf{a} = (2\mathbf{i} + 4\mathbf{j}) - (\mathbf{i} + \mathbf{j}) = \mathbf{i} + 3\mathbf{j}
$$

$\overrightarrow{BC} = \overrightarrow{AD}$, so both pairs of opposite sides are parallel and equal. Therefore $ABCD$ is a parallelogram. ✓

(b) The centroid (intersection of diagonals) is the midpoint of either diagonal:
$$
\mathbf{m} = \frac{\mathbf{a} + \mathbf{c}}{2} = \frac{(\mathbf{i} + \mathbf{j}) + (5\mathbf{i} + 5\mathbf{j})}{2} = \frac{6\mathbf{i} + 6\mathbf{j}}{2} = 3\mathbf{i} + 3\mathbf{j}
$$

Verification using the other diagonal: $\frac{\mathbf{b} + \mathbf{d}}{2} = \frac{(4\mathbf{i} + 2\mathbf{j}) + (2\mathbf{i} + 4\mathbf{j})}{2} = \frac{6\mathbf{i} + 6\mathbf{j}}{2} = 3\mathbf{i} + 3\mathbf{j}$. ✓

(c) Midpoints of the four sides:
$$
M_{AB} = \frac{\mathbf{a} + \mathbf{b}}{2} = \frac{(\mathbf{i} + \mathbf{j}) + (4\mathbf{i} + 2\mathbf{j})}{2} = \frac{5}{2}\mathbf{i} + \frac{3}{2}\mathbf{j}
$$
$$
M_{BC} = \frac{\mathbf{b} + \mathbf{c}}{2} = \frac{(4\mathbf{i} + 2\mathbf{j}) + (5\mathbf{i} + 5\mathbf{j})}{2} = \frac{9}{2}\mathbf{i} + \frac{7}{2}\mathbf{j}
$$
$$
M_{CD} = \frac{\mathbf{c} + \mathbf{d}}{2} = \frac{(5\mathbf{i} + 5\mathbf{j}) + (2\mathbf{i} + 4\mathbf{j})}{2} = \frac{7}{2}\mathbf{i} + \frac{9}{2}\mathbf{j}
$$
$$
M_{DA} = \frac{\mathbf{d} + \mathbf{a}}{2} = \frac{(2\mathbf{i} + 4\mathbf{j}) + (\mathbf{i} + \mathbf{j})}{2} = \frac{3}{2}\mathbf{i} + \frac{5}{2}\mathbf{j}
$$

Now check if these four midpoints form a parallelogram:
$$
\overrightarrow{M_{AB}M_{BC}} = \left(\frac{9}{2} - \frac{5}{2}\right)\mathbf{i} + \left(\frac{7}{2} - \frac{3}{2}\right)\mathbf{j} = 2\mathbf{i} + 2\mathbf{j}
$$
$$
\overrightarrow{M_{DA}M_{CD}} = \left(\frac{7}{2} - \frac{3}{2}\right)\mathbf{i} + \left(\frac{9}{2} - \frac{5}{2}\right)\mathbf{j} = 2\mathbf{i} + 2\mathbf{j}
$$

$\overrightarrow{M_{AB}M_{BC}} = \overrightarrow{M_{DA}M_{CD}}$, so they do form a parallelogram.

> **Interesting fact**: The quadrilateral formed by joining the midpoints of any quadrilateral is always a parallelogram (Varignon's Theorem). The proof using vectors is very elegant — give it a try!

---

**Example 5** (Section formula + proving collinearity of three points with unknown parameters)

The position vectors of points $P$, $Q$, $R$ are:
$\mathbf{p} = 2\mathbf{i} + 3\mathbf{j}$, $\mathbf{q} = 8\mathbf{i} + k\mathbf{j}$, $\mathbf{r} = 14\mathbf{i} + 15\mathbf{j}$.

(a) Given that $P$, $Q$, $R$ are collinear, find the value of $k$.
(b) Hence find the ratio $PQ:QR$.

**Solution approach**:
- For collinearity, $\overrightarrow{PQ}$ must be parallel to $\overrightarrow{PR}$ (or $\overrightarrow{QR}$)
- This means there exists a scalar $\lambda$ such that $\overrightarrow{PQ} = \lambda \overrightarrow{PR}$
- Equate components to form equations, solve for $k$ and $\lambda$

**Solution**:

(a) Compute:
$$
\overrightarrow{PR} = \mathbf{r} - \mathbf{p} = (14\mathbf{i} + 15\mathbf{j}) - (2\mathbf{i} + 3\mathbf{j}) = 12\mathbf{i} + 12\mathbf{j}
$$
$$
\overrightarrow{PQ} = \mathbf{q} - \mathbf{p} = (8\mathbf{i} + k\mathbf{j}) - (2\mathbf{i} + 3\mathbf{j}) = 6\mathbf{i} + (k-3)\mathbf{j}
$$

For collinearity, there exists $\lambda$ such that $\overrightarrow{PQ} = \lambda \overrightarrow{PR}$:
$$
6\mathbf{i} + (k-3)\mathbf{j} = \lambda(12\mathbf{i} + 12\mathbf{j}) = 12\lambda\mathbf{i} + 12\lambda\mathbf{j}
$$

Equate $\mathbf{i}$ components:
$$
6 = 12\lambda \implies \lambda = \frac{1}{2}
$$

Equate $\mathbf{j}$ components:
$$
k - 3 = 12\lambda = 12 \times \frac{1}{2} = 6 \implies k = 9
$$

Therefore $k = 9$, giving $\mathbf{q} = 8\mathbf{i} + 9\mathbf{j}$.

(b) With $\lambda = \frac{1}{2}$, we have $\overrightarrow{PQ} = \frac{1}{2}\overrightarrow{PR}$.

This means $Q$ is the midpoint of $PR$. Therefore $PQ:QR = 1:1$.

**Verification**:
$\overrightarrow{QR} = \mathbf{r} - \mathbf{q} = (14\mathbf{i} + 15\mathbf{j}) - (8\mathbf{i} + 9\mathbf{j}) = 6\mathbf{i} + 6\mathbf{j}$
$\overrightarrow{PQ} = 6\mathbf{i} + 6\mathbf{j}$
So $\overrightarrow{PQ} = \overrightarrow{QR}$, confirming $Q$ is the midpoint. ✓

---

### 2.2.2 Composition and Resolution of Velocities

Velocity is a vector quantity. When an object is simultaneously involved in two or more motions, its resultant velocity is the vector sum of these velocities.

#### Relative Velocity Formula

Let the velocity of object $A$ relative to reference frame $C$ be $\mathbf{v}_{A/C}$, the velocity of object $A$ relative to object $B$ be $\mathbf{v}_{A/B}$, and the velocity of object $B$ relative to reference frame $C$ be $\mathbf{v}_{B/C}$. Then:

$$
\mathbf{v}_{A/C} = \mathbf{v}_{A/B} + \mathbf{v}_{B/C}
$$

> **Intuitive understanding**:
> - You are walking on a train at speed $\mathbf{v}_{A/B}$ (you relative to the train)
> - The train is moving relative to the ground at speed $\mathbf{v}_{B/C}$ (train relative to ground)
> - Your speed relative to the ground $\mathbf{v}_{A/C}$ is the sum of the two
>
> **Another example**: A boat travelling in a river.
> - The boat's speed in still water = $\mathbf{v}_{B/W}$ (boat relative to water)
> - The speed of the river current = $\mathbf{v}_{W/G}$ (water relative to ground)
> - The boat's actual speed relative to the ground = $\mathbf{v}_{B/W} + \mathbf{v}_{W/G}$

#### Resolution of Velocities

The opposite of composition: breaking a velocity vector into two perpendicular components (usually horizontal and vertical directions) is called **resolution of velocities**.

Let the magnitude of velocity $\mathbf{v}$ be $v$ (speed), and let the angle it makes with the horizontal be $\theta$. Then:

$$
\mathbf{v} = (v\cos\theta)\mathbf{i} + (v\sin\theta)\mathbf{j}
$$

where $v_x = v\cos\theta$ is the horizontal component and $v_y = v\sin\theta$ is the vertical component.

> **Derivation**: Project the velocity vector onto the $x$-axis and $y$-axis. In the right-angled triangle, the adjacent side $=$ hypotenuse $\times \cos\theta$, and the opposite side $=$ hypotenuse $\times \sin\theta$.

---

#### Collision Problems

The condition for two moving objects to collide is that at the **same time**, their position vectors are **equal**. That is:

$$
\mathbf{r}_1(t) = \mathbf{r}_2(t)
$$

For motion with constant velocity, the position vector satisfies:

$$
\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t
$$

where $\mathbf{r}_0$ is the initial position vector and $\mathbf{v}$ is the velocity vector. Therefore, the collision condition can be expanded to:

$$
\mathbf{r}_{01} + \mathbf{v}_1 t = \mathbf{r}_{02} + \mathbf{v}_2 t
$$

This is a vector equation in time $t$. It is equivalent to two scalar equations (one for each component) being equal, allowing us to solve for $t$ and verify consistency.

**Solution steps**:
1. Write the position vectors $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ for both objects.
2. Set $\mathbf{r}_1(t) = \mathbf{r}_2(t)$, obtaining two component equations.
3. Solve for $t$ from each equation. If the two $t$ values are equal and $t \geq 0$, they collide; otherwise, they do not.

> **Note**: "Collision" requires both objects to be at the same position at the same time. If two ships reach the same point at different times, that is called "meeting" rather than "colliding".

---

### 📌 Worked Examples 2.3: Composition of Velocities and Collision Problems

**Example 1** (Composition of velocities — boat and current)

A boat's speed in still water is $6\,\text{m/s}$ eastwards. The water current flows at $4\,\text{m/s}$ northwards. Find the magnitude and direction of the boat's velocity relative to the ground.

**Solution approach**:
- Boat's velocity relative to water $\mathbf{v}_{B/W}$ = east $6$ m/s
- Water's velocity relative to ground $\mathbf{v}_{W/G}$ = north $4$ m/s
- Boat's velocity relative to ground $\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G}$

**Solution**:

Let due east be the $+x$-axis and due north be the $+y$-axis.

Boat's velocity relative to water: $\mathbf{v}_{B/W} = 6\mathbf{i}$
Water current velocity relative to ground: $\mathbf{v}_{W/G} = 4\mathbf{j}$

By the velocity composition formula:

$$
\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G} = 6\mathbf{i} + 4\mathbf{j}
$$

Magnitude of the resultant velocity (speed):

$$
|\mathbf{v}_{B/G}| = \sqrt{6^2 + 4^2} = \sqrt{36 + 16} = \sqrt{52} = 2\sqrt{13} \approx 7.21\,\text{m/s}
$$

Direction of the resultant velocity: Let $\theta$ be the angle measured from due east (anticlockwise positive).

$$
\tan\theta = \frac{4}{6} = \frac{2}{3} \implies \theta = \arctan\left(\frac{2}{3}\right) \approx 33.69^\circ
$$

Therefore, the boat's velocity relative to the ground has magnitude $2\sqrt{13}\,\text{m/s}$, and direction $33.69^\circ$ north of east (i.e., rotated $33.69^\circ$ anticlockwise from due east).

> **Real-life example**: This is why, when a boat crosses a river, if it heads directly toward the opposite bank, it will be carried downstream by the current. To reach the point directly opposite, the boat must point its bow upstream at an angle.

---

**Example 2** (Resolution of velocity — initial velocity of a projectile)

A ball is thrown with an initial speed of $20\,\text{m/s}$ at an angle of $30^\circ$ above the horizontal.

(a) Find the horizontal and vertical components of the initial velocity.
(b) Write the initial velocity in vector form.

**Solution approach**:
- The magnitude of the velocity is $20$, and the direction is at an elevation of $30^\circ$
- Horizontal component $v_x = v\cos\theta$, vertical component $v_y = v\sin\theta$

**Solution**:

(a) Let the horizontal rightward direction be $+x$-axis and the vertical upward direction be $+y$-axis.

Horizontal component:

$$
v_x = v\cos\theta = 20 \times \cos 30^\circ = 20 \times \frac{\sqrt{3}}{2} = 10\sqrt{3} \approx 17.32\,\text{m/s}
$$

Vertical component:

$$
v_y = v\sin\theta = 20 \times \sin 30^\circ = 20 \times \frac{1}{2} = 10\,\text{m/s}
$$

(b) The initial velocity in vector form:

$$
\mathbf{v}_0 = 10\sqrt{3}\,\mathbf{i} + 10\,\mathbf{j}\,\text{m/s}
$$

> **Physical significance**:
> - In the absence of air resistance, the horizontal component $v_x$ remains constant throughout the motion (since no force acts horizontally)
> - The vertical component $v_y$ changes due to gravity at an acceleration of $-g$ ($g \approx 9.8\,\text{m/s}^2$)
> - Therefore, the velocity at any time $t$ is $\mathbf{v}(t) = 10\sqrt{3}\,\mathbf{i} + (10 - gt)\,\mathbf{j}$
> - This lays the foundation for kinematics problems in Chapter 10

---

**Example 3** (Collision problem — will two ships collide?)

Ship $P$ departs from point $(0, 0)$ travelling at velocity $\mathbf{v}_P = (3\mathbf{i} + 4\mathbf{j})\,\text{km/h}$. Ship $Q$ departs from point $(10, 5)\,\text{km}$ travelling at velocity $\mathbf{v}_Q = (-2\mathbf{i} + \mathbf{j})\,\text{km/h}$. Both ships depart at the same time. Determine whether they will collide.

**Solution approach**:
1. Write the position vectors of both ships (both in the form $\mathbf{r}_0 + \mathbf{v}t$)
2. Set $\mathbf{r}_P(t) = \mathbf{r}_Q(t)$
3. Obtain two component equations and solve for $t$ from each
4. If the $t$ values are consistent and $t \geq 0$, they collide; otherwise, they do not

**Solution**:

Let $t$ be the time (in hours) after departure.

$P$'s position vector (starting from the origin):

$$
\mathbf{r}_P(t) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 3 \\ 4 \end{pmatrix} t = \begin{pmatrix} 3t \\ 4t \end{pmatrix}
$$

$Q$'s position vector (starting from $(10,5)$):

$$
\mathbf{r}_Q(t) = \begin{pmatrix} 10 \\ 5 \end{pmatrix} + \begin{pmatrix} -2 \\ 1 \end{pmatrix} t = \begin{pmatrix} 10 - 2t \\ 5 + t \end{pmatrix}
$$

If the two ships collide, there must exist some $t \geq 0$ such that $\mathbf{r}_P(t) = \mathbf{r}_Q(t)$, i.e.:

$$
\begin{pmatrix} 3t \\ 4t \end{pmatrix} = \begin{pmatrix} 10 - 2t \\ 5 + t \end{pmatrix}
$$

This gives two component equations:

$$
\begin{cases}
x\text{-component: } & 3t = 10 - 2t \implies 5t = 10 \implies t = 2 \\[4pt]
y\text{-component: } & 4t = 5 + t \implies 3t = 5 \implies t = \dfrac{5}{3}
\end{cases}
$$

The two $t$ values are not equal ($2 \neq \frac{5}{3}$), so there is no time that satisfies both component equations simultaneously. The two ships will not collide.

> **Why don't they collide?** Even though the $x$-coordinates are equal at $t=2$, the $y$-coordinates at $t=2$ are $4\times 2 = 8$ and $5+2=7$ respectively, which are not equal. So the two ships never arrive at the same point at the same time.

---

**Example 4** (Collision with different departure times)

Ship $A$ departs from $(0, 0)$ at $t = 0$ with velocity $\mathbf{v}_A = (4\mathbf{i} + 2\mathbf{j})\,\text{km/h}$.
Ship $B$ departs from $(12, 6)\,\text{km}$ at $t = 1$ (one hour later) with velocity $\mathbf{v}_B = (-2\mathbf{i} + 4\mathbf{j})\,\text{km/h}$.

Determine whether the two ships will collide.

**Solution approach**:
- Write $\mathbf{r}_A(t)$ for $t \geq 0$
- Write $\mathbf{r}_B(t)$ — note $B$ starts at $t = 1$, so for $t \geq 1$, $\mathbf{r}_B(t) = \mathbf{r}_{B0} + \mathbf{v}_B(t - 1)$
- Set equal and solve

**Solution**:

For $t \geq 1$ (both ships are underway):

$$
\mathbf{r}_A(t) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 4 \\ 2 \end{pmatrix} t = \begin{pmatrix} 4t \\ 2t \end{pmatrix}
$$

$$
\mathbf{r}_B(t) = \begin{pmatrix} 12 \\ 6 \end{pmatrix} + \begin{pmatrix} -2 \\ 4 \end{pmatrix} (t - 1) = \begin{pmatrix} 12 - 2(t-1) \\ 6 + 4(t-1) \end{pmatrix} = \begin{pmatrix} 14 - 2t \\ 2 + 4t \end{pmatrix}
$$

Set $\mathbf{r}_A(t) = \mathbf{r}_B(t)$:
$$
\begin{cases}
4t = 14 - 2t \implies 6t = 14 \implies t = \dfrac{7}{3} \approx 2.333 \\[4pt]
2t = 2 + 4t \implies -2t = 2 \implies t = -1
\end{cases}
$$

The two $t$ values are not equal ($\frac{7}{3} \neq -1$), so the ships do not collide.

> **Note**: The $y$-component equation gives $t = -1$, which is before either ship departed — this is a meaningless solution in the physical context. The $x$-component equation gives $t = \frac{7}{3}$, but this doesn't satisfy the $y$-equation. No collision.

---

**Example 5** (Finding the course to steer — boat crossing a river)

A river flows at $3\,\text{m/s}$ from west to east. A boat has a speed of $5\,\text{m/s}$ in still water. The boat aims to travel directly north (perpendicular to the river bank).

(a) In what direction should the boat be steered (angle relative to north)?
(b) What is the boat's resultant speed relative to the ground?

**Solution approach**:
- Let the boat's velocity relative to water be $\mathbf{v}_{B/W}$ with magnitude $5$ and unknown direction $\theta$ west of north
- Water velocity: $\mathbf{v}_{W/G} = 3\mathbf{i}$ (east)
- Desired resultant: $\mathbf{v}_{B/G} = v\mathbf{j}$ (pure north)
- Use $\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G}$ to solve for $\theta$ and $v$

**Solution**:

Let due east be $+x$ and due north be $+y$.

Water velocity: $\mathbf{v}_{W/G} = 3\mathbf{i}$

Boat's velocity relative to water: steering at angle $\theta$ west of north means:
$$
\mathbf{v}_{B/W} = 5\cos(90^\circ + \theta)\mathbf{i} + 5\sin(90^\circ + \theta)\mathbf{j} = -5\sin\theta\,\mathbf{i} + 5\cos\theta\,\mathbf{j}
$$

(Alternatively: the boat points to the left of north by $\theta$, so its $x$-component is $-5\sin\theta$ and $y$-component is $5\cos\theta$.)

Desired resultant (pure north): $\mathbf{v}_{B/G} = 0\mathbf{i} + v\mathbf{j}$

Using $\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G}$:
$$
0\mathbf{i} + v\mathbf{j} = (-5\sin\theta + 3)\mathbf{i} + 5\cos\theta\,\mathbf{j}
$$

Equate $\mathbf{i}$ components:
$$
-5\sin\theta + 3 = 0 \implies \sin\theta = \frac{3}{5} = 0.6 \implies \theta = \arcsin(0.6) \approx 36.87^\circ
$$

Equate $\mathbf{j}$ components:
$$
v = 5\cos\theta = 5 \times \sqrt{1 - 0.6^2} = 5 \times \sqrt{0.64} = 5 \times 0.8 = 4
$$

(a) The boat should be steered $36.87^\circ$ west of north (or equivalently, at a bearing of $360^\circ - 36.87^\circ = 323.13^\circ$).

(b) The resultant speed relative to the ground is $4\,\text{m/s}$ due north.

> **Real-life insight**: Notice the resultant speed ($4\,\text{m/s}$) is less than the boat's still-water speed ($5\,\text{m/s}$). This is because part of the boat's effort goes into counteracting the current. This is why crossing a river with a strong current takes longer than crossing still water of the same width.

---

## 2.3 Introduction to Rates of Change (Calculus Foundation)

### 2.3.1 Why Study Rates of Change?

In the physical world, very few things remain static. A moving car — its position changes. An inflating balloon — its volume changes. A heated metal rod — its temperature changes. A **rate of change** is the mathematical tool that describes "how quickly one quantity changes with respect to another."

In sections 2.1 and 2.2, we used vectors to describe position, velocity, and acceleration. Now we ask a deeper question: **How do we precisely define "instantaneous" rate of change?**

---

### 2.3.2 From Average Rate of Change to Instantaneous Rate of Change

Let's start with a concrete kinematics example.

A particle moves along a straight line. Its displacement $s$ (in metres) as a function of time $t$ (in seconds) is:

$$
s(t) = t^2
$$

We want to find the velocity at the **instant** $t = 1$ second.

#### Step 1: Average Velocity

If we take a time interval $[1, 1 + \Delta t]$, the average velocity of the particle over this interval is:

$$
\text{Average velocity} = \frac{s(1 + \Delta t) - s(1)}{\Delta t}
$$

Substituting $s(t) = t^2$:

$$
\frac{(1 + \Delta t)^2 - 1^2}{\Delta t} = \frac{1 + 2\Delta t + (\Delta t)^2 - 1}{\Delta t} = \frac{2\Delta t + (\Delta t)^2}{\Delta t} = 2 + \Delta t
$$

#### Step 2: Let $\Delta t$ Become Smaller and Smaller

We let $\Delta t$ gradually approach 0 and observe how the average velocity changes:

| $\Delta t$ (seconds) | Average Velocity (m/s) |
|:---:|:---:|
| 0.1 | $2 + 0.1 = 2.1$ |
| 0.01 | $2 + 0.01 = 2.01$ |
| 0.001 | $2 + 0.001 = 2.001$ |
| 0.0001 | $2 + 0.0001 = 2.0001$ |
| $\to 0$ | $\to 2$ |

As $\Delta t$ gets closer and closer to 0, the average velocity gets closer and closer to **2**.

#### Step 3: The Limit

When $\Delta t$ approaches 0, the average velocity $2 + \Delta t$ approaches 2. We write:

$$
v(1) = \lim_{\Delta t \to 0} \frac{s(1 + \Delta t) - s(1)}{\Delta t} = \lim_{\Delta t \to 0} (2 + \Delta t) = 2
$$

This limiting value is the **instantaneous velocity** of the particle at $t = 1$.

> **Important understanding**: We never set $\Delta t = 0$ (that would give $0/0$, which is meaningless). We let $\Delta t$ approach 0 infinitely closely and observe what fixed value the ratio approaches. This "target of approach" is the derivative.
>
> In the language of limits: **As $\Delta t$ approaches 0, the limit of the average velocity is the instantaneous velocity.**

---

### 2.3.3 General Definition of the Derivative

In general, for a function $y = f(x)$, its **derivative** (i.e., instantaneous rate of change) at $x = a$ is defined as:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

where $h$ corresponds to $\Delta x$ or $\Delta t$ in the earlier example.

If this limit exists, we say that $f$ is **differentiable** at $x = a$.

**Notation for derivatives**:
- Leibniz notation: $\dfrac{dy}{dx}$ or $\dfrac{d}{dx}f(x)$
- Lagrange notation: $f'(x)$
- Newton notation (commonly used in physics): $\dot{y}$

> In syllabus point 14.1, only an intuitive understanding of limits is required; differentiation from first principles is not required. However, we will still present a few basic derivations here to help build your intuition.

---

### 2.3.4 Derivatives from First Principles — Basic Derivations

Let's use the limit definition to derive the derivatives of some basic functions.

#### Derivation 1: $f(x) = x^2$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} \\
&= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h} \\
&= \lim_{h \to 0} \frac{2xh + h^2}{h} \\
&= \lim_{h \to 0} (2x + h) \\
&= 2x
\end{aligned}
$$

Therefore $\dfrac{d}{dx}(x^2) = 2x$.

**Geometric meaning**: The slope of the tangent line to the function $y = x^2$ at any point $x$ is $2x$. At $x = 1$, the slope is $2$; at $x = 3$, the slope is $6$.

#### Derivation 2: $f(x) = x^3$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{(x + h)^3 - x^3}{h}
\end{aligned}
$$

Expanding $(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{x^3 + 3x^2h + 3xh^2 + h^3 - x^3}{h} \\
&= \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3}{h} \\
&= \lim_{h \to 0} (3x^2 + 3xh + h^2) \\
&= 3x^2
\end{aligned}
$$

Therefore $\dfrac{d}{dx}(x^3) = 3x^2$.

#### Derivation 3: $f(x) = \dfrac{1}{x}$ ($x \neq 0$)

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{\frac{1}{x + h} - \frac{1}{x}}{h}
\end{aligned}
$$

First, combine the fractions in the numerator:

$$
\frac{1}{x + h} - \frac{1}{x} = \frac{x - (x + h)}{x(x + h)} = \frac{-h}{x(x + h)}
$$

Therefore:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{-h}{x(x + h)} \cdot \frac{1}{h} \\
&= \lim_{h \to 0} \frac{-1}{x(x + h)} \\
&= -\frac{1}{x^2}
\end{aligned}
$$

Thus $\dfrac{d}{dx}\left(\dfrac{1}{x}\right) = -\dfrac{1}{x^2}$.

#### Derivation 4: $f(x) = \sqrt{x}$ ($x > 0$)

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h}
\end{aligned}
$$

This one requires a clever trick: multiply numerator and denominator by the conjugate $\sqrt{x + h} + \sqrt{x}$:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{(\sqrt{x + h} - \sqrt{x})(\sqrt{x + h} + \sqrt{x})}{h(\sqrt{x + h} + \sqrt{x})} \\
&= \lim_{h \to 0} \frac{(x + h) - x}{h(\sqrt{x + h} + \sqrt{x})} \\
&= \lim_{h \to 0} \frac{h}{h(\sqrt{x + h} + \sqrt{x})} \\
&= \lim_{h \to 0} \frac{1}{\sqrt{x + h} + \sqrt{x}} \\
&= \frac{1}{\sqrt{x} + \sqrt{x}} = \frac{1}{2\sqrt{x}}
\end{aligned}
$$

Therefore $\dfrac{d}{dx}(\sqrt{x}) = \dfrac{1}{2\sqrt{x}}$. Note that this is consistent with the Power Rule: $\sqrt{x} = x^{1/2}$, so $\dfrac{d}{dx}(x^{1/2}) = \dfrac{1}{2}x^{-1/2} = \dfrac{1}{2\sqrt{x}}$. ✓

> **Why the conjugate trick?** When direct substitution gives $0/0$, multiplying by the conjugate is a standard technique to rationalise the numerator and eliminate the indeterminacy.

#### Derivation 5: $f(x) = c$ (constant function)

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{c - c}{h} \\
&= \lim_{h \to 0} \frac{0}{h} \\
&= \lim_{h \to 0} 0 = 0
\end{aligned}
$$

Therefore $\dfrac{d}{dx}(c) = 0$. The rate of change of a constant is zero — a horizontal line has zero slope everywhere. This also fits the Power Rule: $c = c \cdot x^0$, and $\dfrac{d}{dx}(c \cdot x^0) = c \cdot 0 \cdot x^{-1} = 0$.

#### Derivation 6: $f(x) = ax + b$ (linear function)

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{[a(x + h) + b] - [ax + b]}{h} \\
&= \lim_{h \to 0} \frac{ax + ah + b - ax - b}{h} \\
&= \lim_{h \to 0} \frac{ah}{h} \\
&= \lim_{h \to 0} a = a
\end{aligned}
$$

Therefore $\dfrac{d}{dx}(ax + b) = a$. The derivative of a linear function is its slope — exactly what we expect.

#### Derivation 7: $f(x) = \dfrac{1}{x^2}$ ($x \neq 0$)

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{\frac{1}{(x + h)^2} - \frac{1}{x^2}}{h}
\end{aligned}
$$

Combine the fractions in the numerator:
$$
\frac{1}{(x + h)^2} - \frac{1}{x^2} = \frac{x^2 - (x + h)^2}{x^2(x + h)^2} = \frac{x^2 - (x^2 + 2xh + h^2)}{x^2(x + h)^2} = \frac{-2xh - h^2}{x^2(x + h)^2}
$$

Therefore:
$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{-2xh - h^2}{x^2(x + h)^2} \cdot \frac{1}{h} \\
&= \lim_{h \to 0} \frac{-2x - h}{x^2(x + h)^2} \\
&= \frac{-2x}{x^2 \cdot x^2} = -\frac{2x}{x^4} = -\frac{2}{x^3}
\end{aligned}
$$

Thus $\dfrac{d}{dx}\left(\dfrac{1}{x^2}\right) = -\dfrac{2}{x^3}$. Consistent with the Power Rule: $x^{-2} \to -2x^{-3}$. ✓

---

### 2.3.5 The Power Rule

From the derivations above, we can observe a pattern:

| $f(x)$ | $f'(x)$ |
|:---:|:---:|
| $x^2$ | $2x$ |
| $x^3$ | $3x^2$ |
| $x^1$ | $1$ (i.e., $1 \cdot x^0$) |
| $\dfrac{1}{x} = x^{-1}$ | $-\dfrac{1}{x^2} = -x^{-2}$ |

This pattern is the **Power Rule**: for any real number $n$,

$$
\boxed{\frac{d}{dx}(x^n) = n x^{n-1}}
$$

> **Full derivation of the Power Rule** (using the Binomial Theorem, for positive integers $n$ only):
>
> Consider $f(x) = x^n$, where $n$ is a positive integer. Expand $(x + h)^n$ using the Binomial Theorem:
> $$
> (x + h)^n = x^n + n x^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \binom{n}{3}x^{n-3}h^3 + \dots + h^n
> $$
> Therefore:
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{x^n + n x^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \dots + h^n - x^n}{h} \\
> &= \lim_{h \to 0} \left( n x^{n-1} + \binom{n}{2}x^{n-2}h + \binom{n}{3}x^{n-3}h^2 + \dots + h^{n-1} \right) \\
> &= n x^{n-1}
> \end{aligned}
> $$
> because all terms containing $h$ tend to 0 as $h \to 0$.

---

### 2.3.6 Rates of Change in the Context of Vectors: Kinematics

Now let's return to the context of vectors. If a particle's position vector $\mathbf{r}(t)$ changes with time, then its velocity vector and acceleration vector are the rates of change of the position vector with respect to time.

Let $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$. Then:

$$
\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j}
$$

$$
\mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d^2\mathbf{r}}{dt^2} = \frac{d^2x}{dt^2}\mathbf{i} + \frac{d^2y}{dt^2}\mathbf{j}
$$

That is, differentiating a vector function means differentiating each of its components separately.

---

### 2.3.7 From Acceleration to Velocity and Position (Integration Foundation)

In physics, acceleration $\mathbf{a}(t)$ is the rate of change of velocity $\mathbf{v}(t)$. If we know the acceleration and want to recover the velocity, we need to perform the inverse operation of differentiation — this is called **integration** (which will be studied in detail in Chapter 7).

The basic relationships are:

- Velocity $\mathbf{v}(t) = \int \mathbf{a}(t) \, dt + \mathbf{v}_0$ (where $\mathbf{v}_0$ is the initial velocity)
- Position $\mathbf{r}(t) = \int \mathbf{v}(t) \, dt + \mathbf{r}_0$ (where $\mathbf{r}_0$ is the initial position)

Or, using definite integrals (more suitable for problems with specific time intervals):

$$
\mathbf{v}(t) = \mathbf{v}_0 + \int_0^t \mathbf{a}(u) \, du,
\quad
\mathbf{r}(t) = \mathbf{r}_0 + \int_0^t \mathbf{v}(u) \, du
$$

The intuition to establish here is: **Differentiation** finds the rate of change (position → velocity → acceleration), while **Integration** finds the accumulated quantity (acceleration → velocity → position). They are inverse operations of each other.

---

### 📌 Worked Examples 2.4: Introduction to Rates of Change

**Example 1** (Using the limit definition to find instantaneous velocity)

A particle's displacement (in metres) as a function of time (in seconds) is $s(t) = 3t^2 - 2t + 1$.

(a) Find the average velocity from $t = 2$ to $t = 2 + h$.
(b) Use the limit to find the instantaneous velocity at $t = 2$.

**Solution approach**:
- Average velocity = $\dfrac{s(2+h) - s(2)}{h}$
- Instantaneous velocity = $\displaystyle\lim_{h \to 0}$ (average velocity)

**Solution**:

(a)
$$
\begin{aligned}
\text{Average velocity} &= \frac{s(2 + h) - s(2)}{h} \\
&= \frac{[3(2+h)^2 - 2(2+h) + 1] - [3(4) - 4 + 1]}{h} \\
&= \frac{[3(4 + 4h + h^2) - 4 - 2h + 1] - [12 - 4 + 1]}{h} \\
&= \frac{[12 + 12h + 3h^2 - 4 - 2h + 1] - 9}{h} \\
&= \frac{[9 + 10h + 3h^2] - 9}{h} \\
&= \frac{10h + 3h^2}{h} = 10 + 3h
\end{aligned}
$$

(b) The instantaneous velocity is the limit of the average velocity as $h \to 0$:

$$
v(2) = \lim_{h \to 0} (10 + 3h) = 10\,\text{m/s}
$$

Therefore, the particle's instantaneous velocity at $t = 2$ seconds is $10\,\text{m/s}$.

> **Verification**: Using the Power Rule to differentiate directly: $s'(t) = 6t - 2$, $s'(2) = 12 - 2 = 10$, consistent. ✓

---

**Example 2** (Using the limit definition to find a general derivative + verification by the Power Rule)

Use the limit definition of the derivative to find $f'(x)$ for $f(x) = 4x - x^2$.

**Solution**:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{[4(x + h) - (x + h)^2] - [4x - x^2]}{h} \\
&= \lim_{h \to 0} \frac{4x + 4h - (x^2 + 2xh + h^2) - 4x + x^2}{h} \\
&= \lim_{h \to 0} \frac{4h - 2xh - h^2}{h} \\
&= \lim_{h \to 0} (4 - 2x - h) \\
&= 4 - 2x
\end{aligned}
$$

Therefore $f'(x) = 4 - 2x$.

**Verification**: Using the Power Rule to differentiate $f(x) = 4x - x^2$ term by term:
- $\dfrac{d}{dx}(4x) = 4 \cdot 1 \cdot x^{0} = 4$
- $\dfrac{d}{dx}(-x^2) = -2x^{1} = -2x$
- Adding gives $f'(x) = 4 - 2x$, consistent with the result from the limit. ✓

---

**Example 3** (Rates of change of vectors + integration as the inverse operation)

A particle moves in a plane. Its position vector is:

$$
\mathbf{r}(t) = (t^3 - 3t)\mathbf{i} + (t^2 - 2t)\mathbf{j}
$$

where $t$ is in seconds and position is in metres.

(a) Find the velocity vector $\mathbf{v}(t)$.
(b) Find the acceleration vector $\mathbf{a}(t)$.
(c) Find the velocity and acceleration vectors at $t = 2$ seconds.
(d) Given that the particle's acceleration is $\mathbf{a}(t) = 6t\mathbf{i} + 2\mathbf{j}$, initial velocity $\mathbf{v}_0 = -3\mathbf{i} - 2\mathbf{j}$, and initial position $\mathbf{r}_0 = \mathbf{0}$, use integration to find $\mathbf{v}(t)$ and $\mathbf{r}(t)$, and verify they are consistent with parts (a) and (b).

**Solution approach**:
- Velocity = derivative of position (differentiate each component separately)
- Acceleration = derivative of velocity (differentiate each component separately)
- Integration is the inverse of differentiation: given acceleration, integrate once to get velocity (add constant), then integrate again to get position (add constant)
- Constants are determined by the initial conditions

**Solution**:

(a) Velocity is the derivative of position with respect to time; differentiate each component:

$$
\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{d}{dt}(t^3 - 3t)\,\mathbf{i} + \frac{d}{dt}(t^2 - 2t)\,\mathbf{j}
$$

Using the Power Rule:
- $\dfrac{d}{dt}(t^3) = 3t^2$
- $\dfrac{d}{dt}(-3t) = -3$
- $\dfrac{d}{dt}(t^2) = 2t$
- $\dfrac{d}{dt}(-2t) = -2$

Therefore:

$$
\mathbf{v}(t) = (3t^2 - 3)\mathbf{i} + (2t - 2)\mathbf{j}
$$

(b) Acceleration is the derivative of velocity with respect to time:

$$
\mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}(3t^2 - 3)\,\mathbf{i} + \frac{d}{dt}(2t - 2)\,\mathbf{j}
$$

$$
\mathbf{a}(t) = (6t)\mathbf{i} + 2\mathbf{j}
$$

(c) Substitute $t = 2$:

$$
\mathbf{v}(2) = (3 \times 4 - 3)\mathbf{i} + (4 - 2)\mathbf{j} = 9\mathbf{i} + 2\mathbf{j}\,\text{m/s}
$$

Magnitude of velocity: $|\mathbf{v}(2)| = \sqrt{9^2 + 2^2} = \sqrt{81 + 4} = \sqrt{85} \approx 9.22\,\text{m/s}$

$$
\mathbf{a}(2) = (6 \times 2)\mathbf{i} + 2\mathbf{j} = 12\mathbf{i} + 2\mathbf{j}\,\text{m/s}^2
$$

Magnitude of acceleration: $|\mathbf{a}(2)| = \sqrt{12^2 + 2^2} = \sqrt{144 + 4} = \sqrt{148} = 2\sqrt{37} \approx 12.17\,\text{m/s}^2$

(d) Given $\mathbf{a}(t) = (6t)\mathbf{i} + 2\mathbf{j}$, integrate the acceleration to find velocity:

$$
\mathbf{v}(t) = \int \mathbf{a}(t) \, dt = \left(\int 6t \, dt\right)\mathbf{i} + \left(\int 2 \, dt\right)\mathbf{j}
$$

$$
= (3t^2 + C_1)\mathbf{i} + (2t + C_2)\mathbf{j}
$$

From $\mathbf{v}_0 = \mathbf{v}(0) = -3\mathbf{i} - 2\mathbf{j}$, substituting $t = 0$ gives $C_1 = -3$, $C_2 = -2$. So:

$$
\mathbf{v}(t) = (3t^2 - 3)\mathbf{i} + (2t - 2)\mathbf{j}
$$

This is consistent with part (a). ✓

Now integrate the velocity to find position:

$$
\mathbf{r}(t) = \int \mathbf{v}(t) \, dt = \left(\int (3t^2 - 3) \, dt\right)\mathbf{i} + \left(\int (2t - 2) \, dt\right)\mathbf{j}
$$

$$
= (t^3 - 3t + D_1)\mathbf{i} + (t^2 - 2t + D_2)\mathbf{j}
$$

From $\mathbf{r}_0 = \mathbf{r}(0) = \mathbf{0}$, substituting $t = 0$ gives $D_1 = 0$, $D_2 = 0$. So:

$$
\mathbf{r}(t) = (t^3 - 3t)\mathbf{i} + (t^2 - 2t)\mathbf{j}
$$

This is consistent with the original position function. ✓

---

**Example 4** (First principles derivation for a cubic function)

Use the limit definition of the derivative to find $f'(x)$ for $f(x) = 2x^3 - x$.

**Solution**:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{[2(x + h)^3 - (x + h)] - [2x^3 - x]}{h}
\end{aligned}
$$

Expand $(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$:

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{2(x^3 + 3x^2h + 3xh^2 + h^3) - x - h - 2x^3 + x}{h} \\
&= \lim_{h \to 0} \frac{2x^3 + 6x^2h + 6xh^2 + 2h^3 - x - h - 2x^3 + x}{h} \\
&= \lim_{h \to 0} \frac{6x^2h + 6xh^2 + 2h^3 - h}{h} \\
&= \lim_{h \to 0} (6x^2 + 6xh + 2h^2 - 1) \\
&= 6x^2 - 1
\end{aligned}
$$

Therefore $f'(x) = 6x^2 - 1$.

**Verification** using the Power Rule term by term:
- $\dfrac{d}{dx}(2x^3) = 2 \cdot 3x^2 = 6x^2$
- $\dfrac{d}{dx}(-x) = -1$
- Sum: $6x^2 - 1$. ✓

---

**Example 5** (Kinematics: from acceleration to position via integration, with non-zero initial conditions)

A particle moves along a straight line. Its acceleration is $a(t) = 12t - 4\,\text{m/s}^2$. At $t = 0$, its velocity is $v_0 = 5\,\text{m/s}$ and its displacement is $s_0 = 10\,\text{m}$.

(a) Find the velocity $v(t)$.
(b) Find the displacement $s(t)$.
(c) Find the displacement at $t = 3$ seconds.
(d) Find the time(s) when the particle is momentarily at rest.
(e) Find the acceleration when the particle is at rest.

**Solution approach**:
- Integrate acceleration to get velocity (don't forget $+C$, use initial condition)
- Integrate velocity to get displacement (don't forget $+C$, use initial condition)
- "At rest" means $v(t) = 0$

**Solution**:

(a) Integrate $a(t) = 12t - 4$:
$$
v(t) = \int (12t - 4)\,dt = 6t^2 - 4t + C
$$

Use $v(0) = 5$:
$$
5 = 6(0)^2 - 4(0) + C \implies C = 5
$$

Therefore $v(t) = 6t^2 - 4t + 5\,\text{m/s}$.

(b) Integrate $v(t) = 6t^2 - 4t + 5$:
$$
s(t) = \int (6t^2 - 4t + 5)\,dt = 2t^3 - 2t^2 + 5t + D
$$

Use $s(0) = 10$:
$$
10 = 0 - 0 + 0 + D \implies D = 10
$$

Therefore $s(t) = 2t^3 - 2t^2 + 5t + 10\,\text{m}$.

(c) At $t = 3$:
$$
s(3) = 2(27) - 2(9) + 5(3) + 10 = 54 - 18 + 15 + 10 = 61\,\text{m}
$$

(d) At rest when $v(t) = 0$:
$$
6t^2 - 4t + 5 = 0
$$

Discriminant: $\Delta = (-4)^2 - 4(6)(5) = 16 - 120 = -104 < 0$

No real solutions — the particle never comes to rest. Its velocity is always positive (check: $v(t) = 6t^2 - 4t + 5$, discriminant $< 0$, leading coefficient positive $\implies$ always positive).

(e) Since the particle is never at rest, this part is not applicable. However, we can still verify the relationship: $a(t) = v'(t) = 12t - 4$, and $v(t) = \int a(t)\,dt + v_0$, $s(t) = \int v(t)\,dt + s_0$. ✓

> **Key insight**: The constant of integration is not arbitrary — it is determined by the initial (or boundary) conditions. This is why in physics problems, knowing the initial position and velocity is crucial. This idea is formalised in Chapter 7 (Integration).

---

## 2.4 Practice Problems

The following practice problems are written to examination difficulty, covering all the knowledge points in this chapter. The relevant syllabus reference number is indicated at the start of each problem set.

---

**Problem Set 13.1–13.3: Vector Basics and Geometry**

**1.** Given $\mathbf{a} = 2\mathbf{i} - \mathbf{j}$, $\mathbf{b} = \mathbf{i} + 3\mathbf{j}$.

(a) Find $\mathbf{a} + 2\mathbf{b}$.
(b) Find $|2\mathbf{a} - \mathbf{b}|$.
(c) Find the unit vector in the same direction as $3\mathbf{a} + \mathbf{b}$.

---

**2.** In $\triangle ABC$, $P$ is the midpoint of $BC$, and $Q$ is the midpoint of $CA$. Let $\overrightarrow{AB} = \mathbf{p}$, $\overrightarrow{AC} = \mathbf{q}$.

(a) Express $\overrightarrow{BC}$ in terms of $\mathbf{p}$ and $\mathbf{q}$.
(b) Express $\overrightarrow{PQ}$ in terms of $\mathbf{p}$ and $\mathbf{q}$.
(c) Prove that $PQ \parallel AB$ and $PQ = \frac{1}{2} AB$.

---

**3.** Three points $A$, $B$, $C$ have position vectors $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$, $\mathbf{b} = 5\mathbf{i} + 6\mathbf{j}$, $\mathbf{c} = 9\mathbf{i} + 14\mathbf{j}$ respectively.

(a) Prove that $A$, $B$, $C$ are collinear.
(b) Find the ratio $AB:BC$.

---

**Problem Set 13.3–13.4: Vector Geometry and Motion**

**4.** In $\triangle OAB$, $P$ lies on $OA$ such that $OP:PA = 1:2$, and $Q$ lies on $AB$ such that $AQ:QB = 2:3$. Let $\overrightarrow{OA} = \mathbf{a}$, $\overrightarrow{OB} = \mathbf{b}$.

(a) Express $\overrightarrow{OP}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.
(b) Express $\overrightarrow{OQ}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.
(c) Express $\overrightarrow{PQ}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.

---

**5.** Ship $A$ departs from point $(0, 5)$ at velocity $\mathbf{v}_A = (2\mathbf{i} + 3\mathbf{j})\,\text{km/h}$. Ship $B$ departs from point $(10, 0)$ at velocity $\mathbf{v}_B = (-3\mathbf{i} + 4\mathbf{j})\,\text{km/h}$. Both ships depart at the same time.

(a) Write the position vectors $\mathbf{r}_A(t)$ and $\mathbf{r}_B(t)$.
(b) Determine whether the two ships will collide.

---

**6.** A boat's speed in still water is $10\,\text{m/s}$, heading due north. The water current flows at $6\,\text{m/s}$ due east.

(a) Find the resultant velocity vector of the boat relative to the ground.
(b) Find the magnitude and direction (angle from due north) of the resultant velocity.

---

**Problem Set 14.1: Introduction to Rates of Change**

**7.** A particle's displacement $s$ (metres) as a function of time $t$ (seconds) is $s(t) = 4t^2 + 3t$.

(a) Find the average velocity from $t = 1$ to $t = 1 + h$.
(b) Use the limit to find the instantaneous velocity at $t = 1$.

---

**8.** A particle moves in a plane. Its position vector is:

$$
\mathbf{r}(t) = (2t^2 + t)\mathbf{i} + (3t - 1)\mathbf{j}
$$

(a) Find the velocity vector $\mathbf{v}(t)$.
(b) Find the acceleration vector $\mathbf{a}(t)$.
(c) Find the magnitude of the velocity at $t = 2$.

---

**Comprehensive Problem**

**9.** In parallelogram $ABCD$, the position vectors of $A$, $B$, $C$ are $\mathbf{a} = 2\mathbf{i} + \mathbf{j}$, $\mathbf{b} = 5\mathbf{i} + 3\mathbf{j}$, $\mathbf{c} = 4\mathbf{i} + 6\mathbf{j}$ respectively.

(a) Find the position vector of $D$.
(b) Determine whether $\overrightarrow{AB}$ is perpendicular to $\overrightarrow{AD}$.
(c) Find the area of parallelogram $ABCD$.

> Hint: The area of a parallelogram $= |\overrightarrow{AB}| \times |\overrightarrow{AD}| \times \sin\theta$, where $\theta$ is the angle between the two sides. Alternatively, use the determinant formula: Area $= |x_1 y_2 - x_2 y_1|$, where $\overrightarrow{AB} = (x_1, y_1)$, $\overrightarrow{AD} = (x_2, y_2)$.

---

**Problem Set — Additional Practice**

**10.** Given $\mathbf{u} = 4\mathbf{i} + k\mathbf{j}$ and $\mathbf{v} = 2\mathbf{i} - 3\mathbf{j}$.

(a) Find the value of $k$ such that $\mathbf{u}$ is perpendicular to $\mathbf{v}$.
(b) Find the value of $k$ such that $\mathbf{u}$ is parallel to $\mathbf{v}$.
(c) For $k = 1$, find the angle between $\mathbf{u}$ and $\mathbf{v}$ to the nearest $0.1^\circ$.

---

**11.** In $\triangle ABC$, $D$ lies on $AB$ such that $AD:DB = 1:2$, and $E$ lies on $AC$ such that $AE:EC = 3:1$. Let $\overrightarrow{AB} = \mathbf{p}$, $\overrightarrow{AC} = \mathbf{q}$.

(a) Express $\overrightarrow{AD}$ in terms of $\mathbf{p}$.
(b) Express $\overrightarrow{AE}$ in terms of $\mathbf{q}$.
(c) Express $\overrightarrow{DE}$ in terms of $\mathbf{p}$ and $\mathbf{q}$.
(d) Show that $DE$ is not parallel to $BC$.

---

**12.** Ship $P$ departs from $(2, 8)\,\text{km}$ at velocity $\mathbf{v}_P = (3\mathbf{i} - 2\mathbf{j})\,\text{km/h}$. Ship $Q$ departs from $(-4, 0)\,\text{km}$ at the same time with velocity $\mathbf{v}_Q = (5\mathbf{i} + 2\mathbf{j})\,\text{km/h}$.

(a) Write the position vectors $\mathbf{r}_P(t)$ and $\mathbf{r}_Q(t)$.
(b) Find the time $t$ at which the distance between the two ships is minimised.

> Hint: The distance $d(t) = |\mathbf{r}_P(t) - \mathbf{r}_Q(t)|$. Minimise $d^2(t)$ (which is equivalent to minimising $d(t)$ and avoids dealing with square roots).

---

**13.** Use the limit definition of the derivative (first principles) to find $f'(x)$ for:

(a) $f(x) = x^2 + 3x$
(b) $f(x) = \dfrac{2}{x}$

Verify each result using the Power Rule.

---

**14.** A particle moves in a plane. Its velocity vector is $\mathbf{v}(t) = (6t^2 - 4)\mathbf{i} + (2t + 1)\mathbf{j}$. At $t = 0$, its position vector is $\mathbf{r}_0 = 3\mathbf{i} - 2\mathbf{j}$.

(a) Find the acceleration vector $\mathbf{a}(t)$.
(b) Find the position vector $\mathbf{r}(t)$.
(c) Find the speed of the particle at $t = 2$.
(d) Determine whether the particle ever passes through the origin.

---

## Answers to Practice Problems

**1.**

(a) $\mathbf{a} + 2\mathbf{b} = (2\mathbf{i} - \mathbf{j}) + 2(\mathbf{i} + 3\mathbf{j}) = (2\mathbf{i} - \mathbf{j}) + (2\mathbf{i} + 6\mathbf{j}) = 4\mathbf{i} + 5\mathbf{j}$

(b) $2\mathbf{a} - \mathbf{b} = 2(2\mathbf{i} - \mathbf{j}) - (\mathbf{i} + 3\mathbf{j}) = (4\mathbf{i} - 2\mathbf{j}) - (\mathbf{i} + 3\mathbf{j}) = 3\mathbf{i} - 5\mathbf{j}$

$|2\mathbf{a} - \mathbf{b}| = \sqrt{3^2 + (-5)^2} = \sqrt{9 + 25} = \sqrt{34}$

(c) $3\mathbf{a} + \mathbf{b} = 3(2\mathbf{i} - \mathbf{j}) + (\mathbf{i} + 3\mathbf{j}) = (6\mathbf{i} - 3\mathbf{j}) + (\mathbf{i} + 3\mathbf{j}) = 7\mathbf{i}$

$|7\mathbf{i}| = 7$, so the unit vector $= \frac{7\mathbf{i}}{7} = \mathbf{i}$

---

**2.**

(a) $\overrightarrow{BC} = \overrightarrow{BA} + \overrightarrow{AC} = -\overrightarrow{AB} + \overrightarrow{AC} = -\mathbf{p} + \mathbf{q}$

(b) $P$ is the midpoint of $BC$, so $\mathbf{r}_P = \frac{\mathbf{r}_B + \mathbf{r}_C}{2}$. $Q$ is the midpoint of $CA$, so $\mathbf{r}_Q = \frac{\mathbf{r}_C + \mathbf{r}_A}{2}$.

$$
\begin{aligned}
\overrightarrow{PQ} &= \mathbf{r}_Q - \mathbf{r}_P \\
&= \frac{\mathbf{r}_C + \mathbf{r}_A}{2} - \frac{\mathbf{r}_B + \mathbf{r}_C}{2} \\
&= \frac{\mathbf{r}_A - \mathbf{r}_B}{2} \\
&= \frac{1}{2}\overrightarrow{BA} = -\frac{1}{2}\overrightarrow{AB} = -\frac{1}{2}\mathbf{p}
\end{aligned}
$$

(c) From (b), $\overrightarrow{PQ} = -\frac{1}{2}\mathbf{p} = -\frac{1}{2}\overrightarrow{AB}$, so $\overrightarrow{PQ} \parallel \overrightarrow{AB}$ and $|\overrightarrow{PQ}| = \frac{1}{2}|\overrightarrow{AB}|$, i.e., $PQ = \frac{1}{2}AB$. ✓

> This property is called the **Midpoint Theorem**: the line segment joining the midpoints of two sides of a triangle is parallel to the third side and equal to half its length.

---

**3.**

(a)
$$
\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 6\mathbf{j}) - (3\mathbf{i} + 2\mathbf{j}) = 2\mathbf{i} + 4\mathbf{j}
$$

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (9\mathbf{i} + 14\mathbf{j}) - (5\mathbf{i} + 6\mathbf{j}) = 4\mathbf{i} + 8\mathbf{j}
$$

$\overrightarrow{BC} = 2(2\mathbf{i} + 4\mathbf{j}) = 2\overrightarrow{AB}$. There exists $k = 2$ such that $\overrightarrow{BC} = k\overrightarrow{AB}$, so $A$, $B$, $C$ are collinear.

(b) $|\overrightarrow{AB}| = \sqrt{2^2 + 4^2} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$

$|\overrightarrow{BC}| = \sqrt{4^2 + 8^2} = \sqrt{16 + 64} = \sqrt{80} = 4\sqrt{5}$

So $AB:BC = 2\sqrt{5}:4\sqrt{5} = 1:2$

---

**4.**

(a) $OP:PA = 1:2$, so $OP:OA = 1:3$, i.e., $\overrightarrow{OP} = \frac{1}{3}\mathbf{a}$

(b) $AQ:QB = 2:3$, so $AQ:AB = 2:5$, $Q$ is $\frac{2}{5}$ of the way from $A$ to $B$.

$$
\begin{aligned}
\overrightarrow{OQ} &= \overrightarrow{OA} + \frac{2}{5}\overrightarrow{AB} \\
&= \mathbf{a} + \frac{2}{5}(\mathbf{b} - \mathbf{a}) \\
&= \mathbf{a} + \frac{2}{5}\mathbf{b} - \frac{2}{5}\mathbf{a} \\
&= \frac{3}{5}\mathbf{a} + \frac{2}{5}\mathbf{b}
\end{aligned}
$$

(c)
$$
\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = \left(\frac{3}{5}\mathbf{a} + \frac{2}{5}\mathbf{b}\right) - \frac{1}{3}\mathbf{a} = \left(\frac{3}{5} - \frac{1}{3}\right)\mathbf{a} + \frac{2}{5}\mathbf{b}
$$

Common denominator: $\frac{3}{5} - \frac{1}{3} = \frac{9}{15} - \frac{5}{15} = \frac{4}{15}$

So $\overrightarrow{PQ} = \frac{4}{15}\mathbf{a} + \frac{2}{5}\mathbf{b}$

---

**5.**

(a)
$$
\mathbf{r}_A(t) = \begin{pmatrix} 0 \\ 5 \end{pmatrix} + \begin{pmatrix} 2 \\ 3 \end{pmatrix} t = \begin{pmatrix} 2t \\ 5 + 3t \end{pmatrix}
$$

$$
\mathbf{r}_B(t) = \begin{pmatrix} 10 \\ 0 \end{pmatrix} + \begin{pmatrix} -3 \\ 4 \end{pmatrix} t = \begin{pmatrix} 10 - 3t \\ 4t \end{pmatrix}
$$

(b) Set $\mathbf{r}_A(t) = \mathbf{r}_B(t)$:

$$
\begin{cases}
2t = 10 - 3t \implies 5t = 10 \implies t = 2 \\[4pt]
5 + 3t = 4t \implies 5 = t \implies t = 5
\end{cases}
$$

The two $t$ values are not equal ($2 \neq 5$), so the two ships will not collide.

---

**6.**

(a) Let due north be the $+y$-axis and due east be the $+x$-axis.

Boat's velocity relative to water: $\mathbf{v}_{B/W} = 10\mathbf{j}$
Water's velocity relative to ground: $\mathbf{v}_{W/G} = 6\mathbf{i}$

Resultant velocity: $\mathbf{v}_{B/G} = 6\mathbf{i} + 10\mathbf{j}$

(b) Magnitude: $|\mathbf{v}_{B/G}| = \sqrt{6^2 + 10^2} = \sqrt{36 + 100} = \sqrt{136} = 2\sqrt{34} \approx 11.66\,\text{m/s}$

Direction: Let $\theta$ be the angle from due north.

$$
\tan\theta = \frac{6}{10} = 0.6 \implies \theta = \arctan(0.6) \approx 30.96^\circ
$$

So the direction is $30.96^\circ$ east of north (or $59.04^\circ$ north of east).

---

**7.**

(a)
$$
\begin{aligned}
\frac{s(1+h) - s(1)}{h} &= \frac{[4(1+h)^2 + 3(1+h)] - [4 + 3]}{h} \\
&= \frac{[4(1 + 2h + h^2) + 3 + 3h] - 7}{h} \\
&= \frac{4 + 8h + 4h^2 + 3 + 3h - 7}{h} \\
&= \frac{11h + 4h^2}{h} = 11 + 4h
\end{aligned}
$$

(b) $v(1) = \displaystyle\lim_{h \to 0} (11 + 4h) = 11\,\text{m/s}$

Verification: $s'(t) = 8t + 3$, $s'(1) = 8 + 3 = 11$ ✓

---

**8.**

(a) $\mathbf{v}(t) = \dfrac{d\mathbf{r}}{dt} = (4t + 1)\mathbf{i} + 3\mathbf{j}$

(b) $\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = 4\mathbf{i}$

(c) $\mathbf{v}(2) = (4 \times 2 + 1)\mathbf{i} + 3\mathbf{j} = 9\mathbf{i} + 3\mathbf{j}$

$|\mathbf{v}(2)| = \sqrt{9^2 + 3^2} = \sqrt{81 + 9} = \sqrt{90} = 3\sqrt{10} \approx 9.49\,\text{m/s}$

---

**9.**

(a) In parallelogram $ABCD$, $\overrightarrow{AD} = \overrightarrow{BC}$.

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (4\mathbf{i} + 6\mathbf{j}) - (5\mathbf{i} + 3\mathbf{j}) = -\mathbf{i} + 3\mathbf{j}
$$

So $\mathbf{d} = \mathbf{a} + \overrightarrow{BC} = (2\mathbf{i} + \mathbf{j}) + (-\mathbf{i} + 3\mathbf{j}) = \mathbf{i} + 4\mathbf{j}$

(b) $\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 3\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 3\mathbf{i} + 2\mathbf{j}$

$\overrightarrow{AD} = \mathbf{d} - \mathbf{a} = (\mathbf{i} + 4\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = -\mathbf{i} + 3\mathbf{j}$

Dot product: $\overrightarrow{AB} \cdot \overrightarrow{AD} = (3)(-1) + (2)(3) = -3 + 6 = 3 \neq 0$

So $\overrightarrow{AB}$ and $\overrightarrow{AD}$ are **not perpendicular**.

(c) Method 1 (using the determinant formula for cross product):

$$
\text{Area} = |x_1 y_2 - x_2 y_1|
$$

where $\overrightarrow{AB} = (3, 2)$, $\overrightarrow{AD} = (-1, 3)$.

$$
\text{Area} = |3 \times 3 - 2 \times (-1)| = |9 + 2| = 11
$$

Method 2 (using $|\overrightarrow{AB}| \cdot |\overrightarrow{AD}| \cdot \sin\theta$):

$$
|\overrightarrow{AB}| = \sqrt{3^2 + 2^2} = \sqrt{13}, \quad |\overrightarrow{AD}| = \sqrt{(-1)^2 + 3^2} = \sqrt{10}
$$

From the dot product $\overrightarrow{AB} \cdot \overrightarrow{AD} = |\overrightarrow{AB}||\overrightarrow{AD}|\cos\theta$:

$$
3 = \sqrt{13} \cdot \sqrt{10} \cdot \cos\theta \implies \cos\theta = \frac{3}{\sqrt{130}}
$$

$$
\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \frac{9}{130}} = \sqrt{\frac{121}{130}} = \frac{11}{\sqrt{130}}
$$

$$
\text{Area} = \sqrt{13} \cdot \sqrt{10} \cdot \frac{11}{\sqrt{130}} = \sqrt{130} \cdot \frac{11}{\sqrt{130}} = 11
$$

The area of the parallelogram is $11$ square units. ✓

---

**10.**

(a) For perpendicularity: $\mathbf{u} \cdot \mathbf{v} = 0$
$$
(4)(2) + (k)(-3) = 0 \implies 8 - 3k = 0 \implies k = \frac{8}{3}
$$

(b) For parallelism: ratio of components must be equal
$$
\frac{4}{2} = \frac{k}{-3} \implies 2 = \frac{k}{-3} \implies k = -6
$$

**Verification**: $\mathbf{u} = 4\mathbf{i} - 6\mathbf{j} = 2(2\mathbf{i} - 3\mathbf{j}) = 2\mathbf{v}$. ✓

(c) For $k = 1$, $\mathbf{u} = 4\mathbf{i} + \mathbf{j}$.
$$
\mathbf{u} \cdot \mathbf{v} = (4)(2) + (1)(-3) = 8 - 3 = 5
$$
$$
|\mathbf{u}| = \sqrt{4^2 + 1^2} = \sqrt{17}, \quad |\mathbf{v}| = \sqrt{2^2 + (-3)^2} = \sqrt{13}
$$
$$
\cos\theta = \frac{5}{\sqrt{17}\sqrt{13}} = \frac{5}{\sqrt{221}} \approx 0.3363
$$
$$
\theta = \arccos\left(\frac{5}{\sqrt{221}}\right) \approx 70.3^\circ
$$

---

**11.**

(a) $AD:DB = 1:2$, so $D$ divides $AB$ in the ratio $1:2$ (counting from $A$).

Using the section formula ($m = 1, n = 2$, from $A$ to $B$):
$$
\mathbf{r}_D = \frac{2\mathbf{r}_A + 1\mathbf{r}_B}{1+2} = \frac{2\mathbf{r}_A + \mathbf{r}_B}{3}
$$

So $\overrightarrow{AD} = \mathbf{r}_D - \mathbf{r}_A = \frac{2\mathbf{r}_A + \mathbf{r}_B}{3} - \mathbf{r}_A = \frac{\mathbf{r}_B - \mathbf{r}_A}{3} = \frac{1}{3}\overrightarrow{AB} = \frac{1}{3}\mathbf{p}$.

Alternatively, directly: $AD = \frac{1}{3}AB$, so $\overrightarrow{AD} = \frac{1}{3}\mathbf{p}$.

(b) $AE:EC = 3:1$, so $E$ divides $AC$ in the ratio $3:1$ (counting from $A$). $AE = \frac{3}{4}AC$.

$$
\overrightarrow{AE} = \frac{3}{4}\overrightarrow{AC} = \frac{3}{4}\mathbf{q}
$$

(c)
$$
\overrightarrow{DE} = \overrightarrow{AE} - \overrightarrow{AD} = \frac{3}{4}\mathbf{q} - \frac{1}{3}\mathbf{p}
$$

(d) $\overrightarrow{BC} = \overrightarrow{BA} + \overrightarrow{AC} = -\mathbf{p} + \mathbf{q}$.

For $DE \parallel BC$, there must exist a scalar $\lambda$ such that $\overrightarrow{DE} = \lambda \overrightarrow{BC}$:
$$
\frac{3}{4}\mathbf{q} - \frac{1}{3}\mathbf{p} = \lambda(-\mathbf{p} + \mathbf{q}) = -\lambda\mathbf{p} + \lambda\mathbf{q}
$$

Equate $\mathbf{p}$ coefficients: $-\frac{1}{3} = -\lambda \implies \lambda = \frac{1}{3}$
Equate $\mathbf{q}$ coefficients: $\frac{3}{4} = \lambda \implies \lambda = \frac{3}{4}$

$\frac{1}{3} \neq \frac{3}{4}$, so no such $\lambda$ exists. Therefore $DE$ is not parallel to $BC$.

---

**12.**

(a)
$$
\mathbf{r}_P(t) = \begin{pmatrix} 2 \\ 8 \end{pmatrix} + \begin{pmatrix} 3 \\ -2 \end{pmatrix} t = \begin{pmatrix} 2 + 3t \\ 8 - 2t \end{pmatrix}
$$
$$
\mathbf{r}_Q(t) = \begin{pmatrix} -4 \\ 0 \end{pmatrix} + \begin{pmatrix} 5 \\ 2 \end{pmatrix} t = \begin{pmatrix} -4 + 5t \\ 2t \end{pmatrix}
$$

(b) The relative position vector:
$$
\mathbf{r}_P(t) - \mathbf{r}_Q(t) = \begin{pmatrix} 2 + 3t - (-4 + 5t) \\ 8 - 2t - 2t \end{pmatrix} = \begin{pmatrix} 6 - 2t \\ 8 - 4t \end{pmatrix}
$$

Squared distance:
$$
d^2(t) = (6 - 2t)^2 + (8 - 4t)^2
$$
$$
= 36 - 24t + 4t^2 + 64 - 64t + 16t^2 = 20t^2 - 88t + 100
$$

This is a quadratic in $t$ (opening upwards, so it has a minimum). The minimum occurs at:
$$
t = -\frac{b}{2a} = -\frac{-88}{2 \times 20} = \frac{88}{40} = 2.2
$$

So the distance between the ships is minimised at $t = 2.2$ hours.

The minimum distance is:
$$
d(2.2) = \sqrt{20(2.2)^2 - 88(2.2) + 100} = \sqrt{96.8 - 193.6 + 100} = \sqrt{3.2} \approx 1.79\,\text{km}
$$

---

**13.**

(a) $f(x) = x^2 + 3x$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{[(x+h)^2 + 3(x+h)] - [x^2 + 3x]}{h} \\
&= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 + 3x + 3h - x^2 - 3x}{h} \\
&= \lim_{h \to 0} \frac{2xh + h^2 + 3h}{h} \\
&= \lim_{h \to 0} (2x + h + 3) \\
&= 2x + 3
\end{aligned}
$$

Verification: $\dfrac{d}{dx}(x^2) = 2x$, $\dfrac{d}{dx}(3x) = 3$, sum $= 2x + 3$. ✓

(b) $f(x) = \dfrac{2}{x} = 2x^{-1}$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{\frac{2}{x+h} - \frac{2}{x}}{h} \\
&= \lim_{h \to 0} \frac{2x - 2(x+h)}{x(x+h)} \cdot \frac{1}{h} \\
&= \lim_{h \to 0} \frac{2x - 2x - 2h}{x(x+h)} \cdot \frac{1}{h} \\
&= \lim_{h \to 0} \frac{-2h}{h \cdot x(x+h)} \\
&= \lim_{h \to 0} \frac{-2}{x(x+h)} \\
&= -\frac{2}{x^2}
\end{aligned}
$$

Verification: $\dfrac{d}{dx}(2x^{-1}) = 2 \cdot (-1)x^{-2} = -\dfrac{2}{x^2}$. ✓

---

**14.**

(a) $\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = 12t\,\mathbf{i} + 2\,\mathbf{j}$

(b) Integrate velocity to get position:
$$
\mathbf{r}(t) = \int \mathbf{v}(t)\,dt = \int (6t^2 - 4)\,dt\,\mathbf{i} + \int (2t + 1)\,dt\,\mathbf{j}
$$
$$
= (2t^3 - 4t + C_1)\mathbf{i} + (t^2 + t + C_2)\mathbf{j}
$$

Using $\mathbf{r}(0) = 3\mathbf{i} - 2\mathbf{j}$:
At $t = 0$: $C_1\mathbf{i} + C_2\mathbf{j} = 3\mathbf{i} - 2\mathbf{j} \implies C_1 = 3, C_2 = -2$

Therefore:
$$
\mathbf{r}(t) = (2t^3 - 4t + 3)\mathbf{i} + (t^2 + t - 2)\mathbf{j}
$$

(c) At $t = 2$:
$$
\mathbf{v}(2) = (6 \times 4 - 4)\mathbf{i} + (4 + 1)\mathbf{j} = 20\mathbf{i} + 5\mathbf{j}
$$

Speed $= |\mathbf{v}(2)| = \sqrt{20^2 + 5^2} = \sqrt{400 + 25} = \sqrt{425} = 5\sqrt{17} \approx 20.62\,\text{m/s}$

(d) The particle passes through the origin when $\mathbf{r}(t) = \mathbf{0}$:
$$
\begin{cases}
2t^3 - 4t + 3 = 0 \quad \text{(x-component)} \\
t^2 + t - 2 = 0 \quad \text{(y-component)}
\end{cases}
$$

From the y-component: $t^2 + t - 2 = 0 \implies (t+2)(t-1) = 0 \implies t = -2$ or $t = 1$.

$t \geq 0$ (physical time), so $t = 1$ is the only candidate.

Check the x-component at $t = 1$:
$$
2(1)^3 - 4(1) + 3 = 2 - 4 + 3 = 1 \neq 0
$$

So the particle never passes through the origin.

> **Note**: Even though the y-component is zero at $t = 1$, the x-component is 1, so the position at $t = 1$ is $(1, 0)$, not the origin.

---

## Chapter Summary

### Syllabus Coverage Checklist

| Syllabus Ref | Content | Section | Worked Examples | Practice Problems |
|:---:|------|:---:|:---:|:---:|
| 13.1 | Vector notation | 2.1.1 | 2.1(1) | 1 |
| 13.2 | Position vectors and unit vectors | 2.1.2, 2.1.4 | 2.1(1) | 1(c) |
| 13.3 | Magnitude, addition/subtraction, scalar multiplication, vector geometry | 2.1.3, 2.1.5–2.1.8, 2.2.1 | 2.1, 2.2 | 1–4, 9, 10, 11 |
| 13.4 | Composition and resolution of velocities, collision problems | 2.2.2 | 2.3 | 5, 6, 12 |
| 14.1 | Rates of change and the idea of limits | 2.3 | 2.4 | 7, 8, 13, 14 |

### Quick Reference Formula Table

**Vector Part**:

| Concept | Formula |
|:---|:---|
| Vector representation | $\mathbf{v} = x\mathbf{i} + y\mathbf{j} = \begin{pmatrix} x \\ y \end{pmatrix}$ |
| Magnitude | $|\mathbf{v}| = \sqrt{x^2 + y^2}$ |
| Unit vector | $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{|\mathbf{v}|}$ |
| Displacement | $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$ |
| Midpoint | $\mathbf{r}_M = \dfrac{\mathbf{r}_A + \mathbf{r}_B}{2}$ |
| Section formula ($AP:PB = m:n$) | $\mathbf{r}_P = \dfrac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}$ |
| Parallel condition | $\mathbf{a} = k\mathbf{b}$ (there exists scalar $k$) |
| Perpendicular condition (dot product) | $\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y = 0$ |
| Perpendicularity using slope | $k_1 \cdot k_2 = -1$ |
| Composition of velocities | $\mathbf{v}_{A/C} = \mathbf{v}_{A/B} + \mathbf{v}_{B/C}$ |
| Resolution of velocity | $\mathbf{v} = (v\cos\theta)\mathbf{i} + (v\sin\theta)\mathbf{j}$ |
| Constant velocity motion | $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$ |
| Collision condition | $\mathbf{r}_1(t) = \mathbf{r}_2(t)$ |

**Rates of Change Part**:

| Concept | Formula |
|:---|:---|
| Definition of derivative | $f'(a) = \displaystyle\lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$ |
| Power Rule | $\dfrac{d}{dx}(x^n) = n x^{n-1}$ |
| Velocity (vector) | $\mathbf{v}(t) = \dfrac{d\mathbf{r}}{dt} = \dfrac{dx}{dt}\mathbf{i} + \dfrac{dy}{dt}\mathbf{j}$ |
| Acceleration (vector) | $\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = \dfrac{d^2x}{dt^2}\mathbf{i} + \dfrac{d^2y}{dt^2}\mathbf{j}$ |
| Integration to find velocity | $\mathbf{v}(t) = \int \mathbf{a}(t) \, dt + \mathbf{v}_0$ |
| Integration to find position | $\mathbf{r}(t) = \int \mathbf{v}(t) \, dt + \mathbf{r}_0$ |

### Learning Roadmap

Starting from this chapter, subsequent chapters will deepen your understanding as follows:

- **Chapter 5 (Differentiation)**: Systematic study of differentiation rules (chain rule, product rule, quotient rule), and using derivatives to find tangents, normals, and stationary points
- **Chapter 7 (Integration)**: Learning the inverse operation of differentiation — integration — to master the complete method of finding velocity and position from acceleration
- **Chapter 10 (Comprehensive Applications)**: Combining vectors and calculus to solve complete kinematics problems

---
---

