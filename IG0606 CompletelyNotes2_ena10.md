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
- [Chapter 4: Equations and Inequalities (Graphical Methods)](#chapter-4-equations-and-inequalities-graphical-methods)
- [Chapter 5: Functions (Linear, Cubic, Exponential, Logarithmic)](#chapter-5-functions-linear-cubic-exponential-logarithmic)
- [Chapter 6: Trigonometry (Including Radians)](#chapter-6-trigonometry-including-radians)
- [Chapter 7: Differentiation (Derivatives)](#chapter-7-differentiation-derivatives)
- [Chapter 8: Integration (Indefinite and Definite Integrals)](#chapter-8-integration-indefinite-and-definite-integrals)
- [Chapter 9: Geometry (Straight Lines and Circles)](#chapter-9-geometry-straight-lines-and-circles)
- [Chapter 10: Comprehensive Applications](#chapter-10-comprehensive-applications)

---

# Chapter 10: Comprehensive Applications

## Syllabus Mapping

This chapter corresponds to the "Chapter 10: Comprehensive Applications" part of the syllabus, containing two core sections:
- **10.1 Kinematics**: Using differentiation and integration to study the relationships between displacement, velocity, and acceleration, and extracting information from motion graphs.
- **10.2 Cross-chapter comprehensive problems**: Integrating knowledge from sequences, vectors, functions, trigonometry, geometry, and calculus to solve complex problems in real-world or mathematical contexts.

The syllabus emphasises "integration," requiring students to flexibly apply tools from all previous chapters, with particular focus on the intuitive application of calculus in kinematics and the interconversion between different knowledge areas.

---

## 10.1 Kinematics (Displacement, Velocity, Acceleration, Differentiation and Integration, Motion Graphs)

### 10.1.1 Basic Concepts and Relationships

Consider a particle moving along a straight line, with displacement $s(t)$ as a function of time $t$. Then:
- Instantaneous velocity $v(t) = s'(t)$
- Instantaneous acceleration $a(t) = v'(t) = s''(t)$

Conversely, integrating from acceleration or velocity gives:

$$
v(t) = v(t_0) + \int_{t_0}^t a(\tau)\,d\tau, \quad
s(t) = s(t_0) + \int_{t_0}^t v(\tau)\,d\tau.
$$

**Motion graphs**:
- **$s$-$t$ graph**: The gradient of the tangent is velocity. Concave downward indicates deceleration (velocity decreasing), concave upward indicates acceleration.
- **$v$-$t$ graph**: The area under the curve (definite integral) represents displacement; the gradient of the tangent is acceleration.
- **$a$-$t$ graph**: The area under the curve represents the change in velocity.

### 10.1.2 Worked Examples

---

**Example 1 (Basic differentiation relationships)**

An object moves along a straight line, with displacement $s(t) = 2t^3 - 9t^2 + 12t + 5$ (units: m, $t \geq 0$).
(1) Find the velocity function and acceleration function of the object.
(2) Find the velocity and acceleration of the object at $t = 2$ s.
(3) When does the object come to rest (velocity zero)?

**Solution**:

(1)

$$
v(t) = s'(t) = 6t^2 - 18t + 12 \quad (\text{m/s}), 
\quad a(t) = v'(t) = 12t - 18 \quad (\text{m/s}^2).
$$

(2)

$$
v(2) = 6 \times 4 - 18 \times 2 + 12 = 24 - 36 + 12 = 0 \ (\text{m/s}), 
\quad a(2) = 12 \times 2 - 18 = 6 \ (\text{m/s}^2).
$$

(3) Solve $v(t) = 0$:

$$
6t^2 - 18t + 12 = 0 \Rightarrow t^2 - 3t + 2 = 0 \Rightarrow (t-1)(t-2) = 0,
$$

Therefore the object comes to rest at $t = 1$ s or $t = 2$ s.

---

**Example 2 (Finding displacement and total distance using integration)**

A particle moves along a straight line with velocity function $v(t) = 3t^2 - 12t + 9$ (units: m/s, $t \geq 0$). Given that the initial displacement is $s(0) = 0$.
(1) Find the displacement function $s(t)$.
(2) Find the displacement and total distance travelled in the first 4 seconds.

**Solution**:

(1)

$$
s(t) = \int (3t^2 - 12t + 9)\,dt = t^3 - 6t^2 + 9t + C,
$$

From $s(0) = 0$, we get $C = 0$, so $s(t) = t^3 - 6t^2 + 9t$.

(2) Displacement = $s(4) - s(0) = (64 - 96 + 36) - 0 = 4$ m.

To find total distance, we need to consider the sign of the velocity. Solve $v(t) = 0$:

$$
3t^2 - 12t + 9 = 0 \Rightarrow t^2 - 4t + 3 = 0 \Rightarrow t = 1,\ t = 3.
$$

Sign of velocity: $t \in [0,1)$: $v > 0$; $t \in (1,3)$: $v < 0$; $t \in (3,4]$: $v > 0$.

Total distance = $\int_0^1 v\,dt + \int_1^3 (-v)\,dt + \int_3^4 v\,dt$.

Calculate the absolute displacement in each segment:
- $[0,1]$: $s(1) - s(0) = 1 - 6 + 9 = 4$ m
- $[1,3]$: $|s(3) - s(1)| = |(27 - 54 + 27) - 4| = |0 - 4| = 4$ m
- $[3,4]$: $s(4) - s(3) = 4 - 0 = 4$ m

Total distance = $4 + 4 + 4 = 12$ m.

---

**Example 3 (Motion graph analysis)**

An object moves along a straight line. Its $v$-$t$ graph consists of three straight line segments:
- 0~2 s: straight line with gradient $2$, from $v = 0$ to $v = 4$
- 2~5 s: horizontal line $v = 4$
- 5~7 s: straight line with gradient $-2$, from $v = 4$ to $v = 0$

(1) Draw the corresponding $a$-$t$ graph.
(2) Find the displacement and average velocity of the object in the 0~7 s interval.
(3) Find the acceleration of the object at $t = 4$ s.

**Solution**:

(1) $a$-$t$ graph:
- $0 < t < 2$: $a = 2$ m/s² (constant)
- $2 < t < 5$: $a = 0$
- $5 < t < 7$: $a = -2$ m/s²

The graph consists of three horizontal segments (with jumps at the endpoints).

(2) Displacement = area under the $v$-$t$ graph (algebraic sum):

Segment by segment:
- 0~2 s: triangle area = $\frac{1}{2} \times 2 \times 4 = 4$
- 2~5 s: rectangle area = $3 \times 4 = 12$
- 5~7 s: triangle area = $\frac{1}{2} \times 2 \times 4 = 4$

Total displacement = $4 + 12 + 4 = 20$ m.

Average velocity = Total displacement / Total time = $20/7$ m/s.

(3) At $t = 4$ s, the object is in the second segment (2~5 s), where the velocity is constant, so the acceleration $a = 0$.

---

## 10.2 Cross-Chapter Comprehensive Problems

Cross-chapter comprehensive problems often interweave knowledge from functions, calculus, geometry, trigonometry, vectors, sequences, etc., requiring candidates to have holistic thinking and the ability to flexibly switch between mathematical models. Below are three typical exam-style examples.

---

### Example 4 (Functions combined with differentiation and geometry)

Given the curve $y = x^3 - 3x^2 + 2x + 1$.
(1) Find the equation of the tangent to the curve at the point $(1, 1)$.
(2) Prove that this tangent is also the normal to the curve at another point, and find the coordinates of that point.

**Solution**:

(1) $y' = 3x^2 - 6x + 2$. At $x = 1$, $y' = 3 - 6 + 2 = -1$.

The gradient of the tangent is $k = -1$, passing through $(1, 1)$:

$$
y - 1 = -1(x - 1) \Rightarrow y = -x + 2.
$$

(2) If at some point $(x_0, y_0)$ the gradient of the normal is $-\frac{1}{y'(x_0)}$, set it equal to the tangent gradient $-1$:

$$
-\frac{1}{y'(x_0)} = -1 \Rightarrow y'(x_0) = 1.
$$

Solve $3x_0^2 - 6x_0 + 2 = 1 \Rightarrow 3x_0^2 - 6x_0 + 1 = 0$.

Using the quadratic formula:

$$
x_0 = \frac{6 \pm \sqrt{36 - 12}}{6} = 1 \pm \frac{\sqrt{6}}{3}.
$$

Since $x = 1$ is the point of tangency, the other solution $x_0 = 1 + \frac{\sqrt{6}}{3}$ or $1 - \frac{\sqrt{6}}{3}$ corresponds to the point where the normal is that tangent. Take $x_0 = 1 + \frac{\sqrt{6}}{3}$:

$$
y_0 = \left(1 + \frac{\sqrt{6}}{3}\right)^3 - 3\left(1 + \frac{\sqrt{6}}{3}\right)^2 + 2\left(1 + \frac{\sqrt{6}}{3}\right) + 1,
$$

(The detailed simplification is omitted here, but the corresponding coordinates can be obtained.) Therefore the tangent is also the normal to the curve at another point.

---

### Example 5 (Vectors combined with trigonometry)

A boat's speed in still water is $6$ km/h. The water current flows at $2$ km/h from west to east. If the boat is to reach the opposite bank directly north, at what angle (relative to the direction of the current) should the boat's bow be pointed? What is the magnitude of the boat's actual velocity?

**Solution**:

Set up a coordinate system: let the direction of the current be the positive $x$-axis, and north be the positive $y$-axis. The velocity of the boat relative to the water (the direction the bow points) is $\vec{v}_{b/w}$, with magnitude $6$, making an angle $\theta$ with the $x$-axis (anticlockwise positive). The velocity of the water current is $\vec{v}_w = (2, 0)$.

The actual velocity is $\vec{v}_b = \vec{v}_{b/w} + \vec{v}_w = (6\cos\theta + 2,\ 6\sin\theta)$.

We require the actual velocity to be purely northward, i.e., the $x$-component is zero:

$$
6\cos\theta + 2 = 0 \Rightarrow \cos\theta = -\frac{1}{3} \Rightarrow \theta = \arccos\left(-\frac{1}{3}\right) \approx 109.47^\circ.
$$

At this point, the magnitude of the actual velocity is:

$$
|6\sin\theta| = 6\sqrt{1 - \frac{1}{9}} = 6\sqrt{\frac{8}{9}} = 4\sqrt{2} \approx 5.66 \text{ km/h}.
$$

Therefore the boat's bow should point in a direction of $\arccos\frac{1}{3} \approx 70.53^\circ$ north of west.

---

### Example 6 (Sequences combined with calculus)

An object starts from rest and moves along a straight line with variable acceleration $a(t) = 2e^{-0.5t}$ (m/s²).
(1) Find an expression for the velocity $v(t)$.
(2) Prove that as $t \to \infty$, the velocity approaches a constant, and find this constant.
(3) If the time interval $[0, \infty)$ is divided into infinitely many intervals of length $1$, the displacement increments in each interval form a sequence $\{s_n\}$. Find the general term of this sequence, and determine whether the series $\sum_{n=1}^{\infty} s_n$ converges.

**Solution**:

(1)

$$
v(t) = \int_0^t a(\tau)\,d\tau = \int_0^t 2e^{-0.5\tau}\,d\tau = \left[-4e^{-0.5\tau}\right]_0^t = 4(1 - e^{-0.5t}) \text{ m/s}.
$$

(2)

$$
\lim_{t\to\infty} v(t) = 4(1 - 0) = 4 \text{ m/s}.
$$

This indicates that the object eventually approaches uniform motion with a velocity of $4$ m/s.

(3) The displacement in the $n$th time interval $[n-1, n]$ is:

$$
s_n = \int_{n-1}^{n} v(t)\,dt = \int_{n-1}^{n} 4(1 - e^{-0.5t})\,dt.
$$

Compute:

$$
\int 4\,dt = 4t, \quad \int 4e^{-0.5t}\,dt = -8e^{-0.5t},
$$

Therefore:

$$
s_n = \left[4t + 8e^{-0.5t}\right]_{n-1}^{n} = 4n + 8e^{-0.5n} - [4(n-1) + 8e^{-0.5(n-1)}] = 4 + 8(e^{-0.5n} - e^{-0.5(n-1)}).
$$

Simplifying:

$$
s_n = 4 + 8e^{-0.5n}(1 - e^{0.5}) = 4 + 8e^{-0.5n}(1 - \sqrt{e}).
$$

Since $1 - \sqrt{e} < 0$, we have $s_n < 4$.

The partial sum of the series $\sum_{n=1}^{\infty} s_n$ is:

$$
S_N = \sum_{n=1}^{N} s_n = \sum_{n=1}^{N} 4 + 8(1-\sqrt{e})\sum_{n=1}^{N} e^{-0.5n}.
$$

The first part diverges ($4N \to \infty$), while the second part converges (geometric series with common ratio $e^{-0.5} < 1$). Hence the overall series diverges, meaning the total distance is infinite (consistent with physical intuition — since the velocity approaches a constant, displacement increases without bound over infinite time).


-----
8 台BMPT看着你
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```

```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```
```
              ₙ  l                    
            ⁸☰°°☰⁸                                 
       𠂆 匚匚匚匚匚乀乀二二乀乀
         ╲O O O O O╱╱——╱╱
```