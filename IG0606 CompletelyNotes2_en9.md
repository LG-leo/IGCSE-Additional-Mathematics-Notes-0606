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

# Chapter 9: Geometry (Straight Lines and Circles)

## Syllabus Mapping

This chapter covers the following content from the Cambridge IGCSE Additional Mathematics 0606 (2028–2030) syllabus:

| Syllabus Topic | Section |
|----------|---------|
| **7. Straight-line graphs** – Equations of straight lines, parallel/perpendicular, midpoint, length, perpendicular bisector | 9.1 |
| **7.4** – Linearisation of non-linear relationships ($y = Ax^n$, $y = Ab^x$) | 9.2 |
| **8. Coordinate geometry of the circle** – Equation of a circle, centre and radius | 9.3 |
| **8.2** – Intersection of a line and a circle (secant, tangent, no intersection) | 9.4 |
| **8.3** – Tangents to a circle (without using calculus) | 9.4 |
| **8.4** – Intersecting circles, touching circles, disjoint circles, common chord | 9.5 |

---

## Introduction

The core idea of coordinate geometry is: **to describe geometric shapes using algebraic equations**. A straight line or a circle can be fully represented by a coordinate equation; the positional relationships between two shapes — whether they intersect, are tangent, or the distance between them — can be precisely determined through algebraic operations without needing a ruler and compass.

This chapter starts from the most basic line equations and progressively builds a complete toolkit for coordinate geometry: the equation forms and geometric properties of lines, the two forms of circle equations, the positional relationships between lines and circles (especially three methods for finding tangents), and the common chord of two intersecting circles. Additionally, Section 9.2 introduces a highly practical technique for scientific experiments — **linearisation of non-linear relationships**, which transforms power functions and exponential functions into straight-line forms for analysis.

Each subsection includes complete derivations of formulas and worked examples in exam style. All examples use the **Statement | Reason** format: each step gives a conclusion first, followed by the justification.

---

## 9.1 Equations of Straight Lines

### 9.1.1 Gradient — The Direction of a Line

**Definition**: Given two points $A(x_1, y_1)$ and $B(x_2, y_2)$, the gradient $m$ of line $AB$ is the ratio of the difference in $y$-coordinates to the difference in $x$-coordinates:

$$
m = \frac{y_2 - y_1}{x_2 - x_1} \qquad (x_1 \neq x_2)
$$

**Derivation**: The gradient measures the steepness of a line relative to the horizontal axis. Let the angle between the line and the positive $x$-axis be $\theta$ ($0^\circ \leq \theta < 180^\circ$), then $m = \tan\theta$. When $\theta = 90^\circ$, the line is vertical; $\tan 90^\circ$ is undefined, so vertical lines have no gradient.

**Geometric meaning**:
- $m > 0$: The line slopes upward to the right ($\theta$ is acute)
- $m < 0$: The line slopes downward to the right ($\theta$ is obtuse)
- $m = 0$: The line is horizontal ($\theta = 0^\circ$)
- $m$ undefined: The line is vertical ($\theta = 90^\circ$)

### 9.1.2 Three Forms of the Equation of a Straight Line

**Form 1: Point-Slope Form**

Given a point $(x_1, y_1)$ on the line and the gradient $m$. Let $(x, y)$ be any point on the line. The gradient of the segment connecting this point to the known point must equal $m$:

$$
\frac{y - y_1}{x - x_1} = m
$$

Multiplying both sides by $(x - x_1)$, we obtain the point-slope form:

$$
\boxed{y - y_1 = m(x - x_1)}
$$

**Form 2: Slope-Intercept Form**

In the point-slope form, take the known point as the $y$-intercept $(0, c)$ (where $c$ is called the $y$-intercept). Substituting gives:

$$
y - c = m(x - 0) \quad \Rightarrow \quad \boxed{y = mx + c}
$$

This is the most commonly used form. $m$ is the gradient, $c$ is the $y$-intercept.

**Form 3: General Form**

Move all terms of the line equation to one side:

$$
\boxed{Ax + By + C = 0}
$$

where $A$ and $B$ are not both zero. When $B \neq 0$, the gradient can be found:

$$
y = -\frac{A}{B}x - \frac{C}{B} \quad \Rightarrow \quad m = -\frac{A}{B}
$$

The advantage of the general form is that it includes all lines uniformly, including vertical lines (where $B = 0$, the equation becomes $Ax + C = 0$, i.e., $x = -\frac{C}{A}$).

---

**Example 1**: A line passes through $(3, -2)$ with gradient $4$. Find its equation.

| Statement | Reason |
|-----------|--------|
| The point is $(3, -2)$ and the gradient is $4$. | Given. |
| Using the point-slope form $y - y_1 = m(x - x_1)$. | Appropriate formula when a point and gradient are known. |
| $y - (-2) = 4(x - 3)$. | Substituting $x_1 = 3$, $y_1 = -2$, $m = 4$. |
| $y + 2 = 4x - 12$. | Expanding the bracket. |
| $y = 4x - 14$. | Subtracting 2 from both sides. |

The equation is $y = 4x - 14$, or $4x - y - 14 = 0$ in general form.

---

**Example 2**: A line passes through $(-1, 5)$ and $(2, -1)$. Find its equation.

| Statement | Reason |
|-----------|--------|
| Let $(x_1, y_1) = (-1, 5)$ and $(x_2, y_2) = (2, -1)$. | Two points on the line are given. |
| $m = \frac{-1 - 5}{2 - (-1)} = \frac{-6}{3} = -2$. | Gradient formula $m = \frac{y_2 - y_1}{x_2 - x_1}$. |
| Using $y - y_1 = m(x - x_1)$ with $(-1, 5)$. | Point-slope form requires one point and the gradient. |
| $y - 5 = -2(x + 1)$. | Substituting $m = -2$, $x_1 = -1$, $y_1 = 5$. |
| $y - 5 = -2x - 2$. | Expanding the bracket. |
| $y = -2x + 3$. | Adding 5 to both sides. |

The equation is $y = -2x + 3$, or $2x + y - 3 = 0$.

---

**Example 3**: Convert the line $3x - 2y + 6 = 0$ to slope-intercept form, and state its gradient and $y$-intercept.

| Statement | Reason |
|-----------|--------|
| $3x - 2y + 6 = 0$. | Given general form. |
| $-2y = -3x - 6$. | Moving $3x$ and $6$ to the RHS. |
| $y = \frac{3}{2}x + 3$. | Dividing both sides by $-2$. |
| $m = \frac{3}{2}$ and $c = 3$. | In $y = mx + c$, $m$ is the gradient and $c$ is the $y$-intercept. |

The gradient is $\frac{3}{2}$ and the $y$-intercept is $3$.

### 9.1.3 Conditions for Parallel and Perpendicular Lines

**Parallel Lines**

The geometric meaning of two parallel lines is that they have the same direction. Therefore their gradients are equal:

$$
\boxed{m_1 = m_2}
$$

When both lines are vertical, their gradients are both undefined, and they are also parallel.

**Perpendicular Lines**

When two lines are perpendicular, one line rotated by $90^\circ$ coincides with the other.

**Derivation**: Let the gradients of the two lines be $m_1 = \tan\theta_1$ and $m_2 = \tan\theta_2$. If the lines are perpendicular, then $\theta_2 = \theta_1 + 90^\circ$ (or vice versa). Using the identity $\tan(\theta + 90^\circ) = -\cot\theta$:

$$
m_2 = \tan(\theta_1 + 90^\circ) = -\cot\theta_1 = -\frac{1}{\tan\theta_1} = -\frac{1}{m_1}
$$

Therefore:

$$
\boxed{m_1 \cdot m_2 = -1}
$$

Special case: A horizontal line ($m = 0$) and a vertical line (undefined gradient) are perpendicular. The product condition does not apply here, but this can be determined by geometric intuition.

---

**Example 1**: Determine whether $L_1: y = 3x + 2$ and $L_2: 6x - 2y + 5 = 0$ are parallel.

| Statement | Reason |
|-----------|--------|
| $L_1$ has gradient $m_1 = 3$. | Equation is in slope-intercept form $y = mx + c$. |
| $L_2: 6x - 2y + 5 = 0 \Rightarrow -2y = -6x - 5 \Rightarrow y = 3x + \frac{5}{2}$. | Rearranging to slope-intercept form. |
| $m_2 = 3$. | The coefficient of $x$ is the gradient. |
| $m_1 = m_2 = 3$. | Both gradients are equal. |
| Therefore $L_1 \parallel L_2$. | Parallel lines have equal gradients. |

---

**Example 2**: A line passes through $(2, -3)$ and is perpendicular to $2x + y = 5$. Find its equation.

| Statement | Reason |
|-----------|--------|
| $2x + y = 5 \Rightarrow y = -2x + 5$. | Rearranging to slope-intercept form. |
| The given line has gradient $m_1 = -2$. | In $y = mx + c$, the coefficient of $x$ is the gradient. |
| Let the required gradient be $m_2$. | The required line is perpendicular to the given line. |
| $m_1 \cdot m_2 = -1 \Rightarrow (-2)m_2 = -1 \Rightarrow m_2 = \frac{1}{2}$. | Perpendicular lines satisfy $m_1 m_2 = -1$. |
| The line passes through $(2, -3)$ with $m = \frac{1}{2}$. | Using point-slope form $y - y_1 = m(x - x_1)$. |
| $y - (-3) = \frac{1}{2}(x - 2)$. | Substituting $x_1 = 2$, $y_1 = -3$, $m = \frac{1}{2}$. |
| $y + 3 = \frac{1}{2}x - 1 \Rightarrow y = \frac{1}{2}x - 4$. | Simplifying. |

The equation is $y = \frac{1}{2}x - 4$, or $x - 2y - 8 = 0$.

---

**Example 3**: Given $A(1, 4)$, $B(3, 0)$, $C(5, 2)$. Determine whether triangle $ABC$ is right-angled.

| Statement | Reason |
|-----------|--------|
| $m_{AB} = \frac{0 - 4}{3 - 1} = \frac{-4}{2} = -2$. | Gradient formula between $A$ and $B$. |
| $m_{BC} = \frac{2 - 0}{5 - 3} = \frac{2}{2} = 1$. | Gradient formula between $B$ and $C$. |
| $m_{AC} = \frac{2 - 4}{5 - 1} = \frac{-2}{4} = -\frac{1}{2}$. | Gradient formula between $A$ and $C$. |
| $m_{AB} \cdot m_{AC} = (-2) \times \left(-\frac{1}{2}\right) = 1 \neq -1$. | Checking if $AB \perp AC$. |
| $m_{AB} \cdot m_{BC} = (-2) \times 1 = -2 \neq -1$. | Checking if $AB \perp BC$. |
| $m_{BC} \cdot m_{AC} = 1 \times \left(-\frac{1}{2}\right) = -\frac{1}{2} \neq -1$. | Checking if $BC \perp AC$. |
| No pair of gradients satisfies $m_1 m_2 = -1$. | Therefore no two sides are perpendicular. |
| Triangle $ABC$ is **not** right-angled. | A right-angled triangle requires one pair of perpendicular sides. |

### 9.1.4 Midpoint Formula

Given two points $A(x_1, y_1)$ and $B(x_2, y_2)$, the midpoint $M$ of segment $AB$ has coordinates equal to the arithmetic mean of the endpoints:

$$
\boxed{M\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)}
$$

**Derivation**: Let $M$ have coordinates $(x_M, y_M)$. The vector $\overrightarrow{AM} = \frac{1}{2}\overrightarrow{AB}$, so $(x_M - x_1, y_M - y_1) = \frac{1}{2}(x_2 - x_1, y_2 - y_1)$. Solving gives $x_M = \frac{x_1 + x_2}{2}$, $y_M = \frac{y_1 + y_2}{2}$.

---

**Example 1**: Find the midpoint of $A(-3, 7)$ and $B(5, -1)$.

| Statement | Reason |
|-----------|--------|
| $x_M = \frac{-3 + 5}{2} = \frac{2}{2} = 1$. | Midpoint formula for $x$-coordinate. |
| $y_M = \frac{7 + (-1)}{2} = \frac{6}{2} = 3$. | Midpoint formula for $y$-coordinate. |
| $M = (1, 3)$. | The midpoint of $AB$. |

---

**Example 2**: $P(2, 5)$ is the midpoint of segment $QR$, and $Q(-1, 3)$. Find $R$.

| Statement | Reason |
|-----------|--------|
| Let $R = (x, y)$. | Unknown coordinates of the endpoint. |
| $\frac{-1 + x}{2} = 2$. | Midpoint formula for $x$, equating to 2. |
| $-1 + x = 4 \Rightarrow x = 5$. | Multiplying both sides by 2. |
| $\frac{3 + y}{2} = 5$. | Midpoint formula for $y$, equating to 5. |
| $3 + y = 10 \Rightarrow y = 7$. | Multiplying both sides by 2. |
| $R = (5, 7)$. | The coordinates of the other endpoint. |

---

**Example 3**: $A(2, 3)$, $B(6, -1)$, $C(4, 5)$ are three vertices of a parallelogram. If $A$ and $C$ are opposite vertices, find the fourth vertex $D$.

| Statement | Reason |
|-----------|--------|
| In a parallelogram, diagonals bisect each other. | Property of a parallelogram. |
| The midpoint of diagonal $AC$ equals the midpoint of diagonal $BD$. | Diagonals share the same midpoint. |
| Midpoint of $AC$: $\left(\frac{2 + 4}{2}, \frac{3 + 5}{2}\right) = (3, 4)$. | Midpoint formula. |
| Let $D = (x, y)$. Then midpoint of $BD$ is $\left(\frac{6 + x}{2}, \frac{-1 + y}{2}\right)$. | Midpoint formula for $BD$. |
| $\frac{6 + x}{2} = 3 \Rightarrow 6 + x = 6 \Rightarrow x = 0$. | Equating $x$-coordinates of midpoints. |
| $\frac{-1 + y}{2} = 4 \Rightarrow -1 + y = 8 \Rightarrow y = 9$. | Equating $y$-coordinates of midpoints. |
| $D = (0, 9)$. | The fourth vertex of the parallelogram. |

### 9.1.5 Distance Between Two Points

Given two points $A(x_1, y_1)$ and $B(x_2, y_2)$, the length of segment $AB$ is given by the Pythagorean theorem:

$$
\boxed{AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}}
$$

**Derivation**: Draw horizontal and vertical lines through $A$ and $B$ to form a right-angled triangle. The horizontal leg has length $|x_2 - x_1|$, and the vertical leg has length $|y_2 - y_1|$. By the Pythagorean theorem, the hypotenuse (i.e., $AB$) is $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

---

**Example 1**: Find the distance between $A(-2, 5)$ and $B(4, -3)$.

| Statement | Reason |
|-----------|--------|
| $AB = \sqrt{(4 - (-2))^2 + (-3 - 5)^2}$. | Distance formula. |
| $= \sqrt{6^2 + (-8)^2}$. | Simplifying inside the brackets. |
| $= \sqrt{36 + 64} = \sqrt{100} = 10$. | Evaluating squares and summing. |

---

**Example 2**: Point $P$ is on the $x$-axis and its distance from $A(1, 4)$ is $5$. Find $P$.

| Statement | Reason |
|-----------|--------|
| Let $P = (p, 0)$. | Any point on the $x$-axis has $y = 0$. |
| $PA = \sqrt{(p - 1)^2 + (0 - 4)^2} = 5$. | Distance from $P$ to $A$ is given as $5$. |
| $(p - 1)^2 + 16 = 25$. | Squaring both sides. |
| $(p - 1)^2 = 9$. | Subtracting 16 from both sides. |
| $p - 1 = 3$ or $p - 1 = -3$. | Taking square root (two possibilities). |
| $p = 4$ or $p = -2$. | Solving for $p$. |
| $P = (4, 0)$ or $P = (-2, 0)$. | Two points satisfy the condition. |

---

**Example 3**: Prove that $A(1, 2)$, $B(4, 6)$, $C(7, 2)$ form an isosceles triangle.

| Statement | Reason |
|-----------|--------|
| $AB = \sqrt{(4 - 1)^2 + (6 - 2)^2} = \sqrt{9 + 16} = 5$. | Distance formula for $AB$. |
| $BC = \sqrt{(7 - 4)^2 + (2 - 6)^2} = \sqrt{9 + 16} = 5$. | Distance formula for $BC$. |
| $AC = \sqrt{(7 - 1)^2 + (2 - 2)^2} = \sqrt{36 + 0} = 6$. | Distance formula for $AC$. |
| $AB = BC = 5$, but $AB \neq AC$ and $BC \neq AC$. | Two sides are equal, the third is different. |
| Triangle $ABC$ is isosceles with $AB = BC$. | An isosceles triangle has at least two equal sides. |

### 9.1.6 Perpendicular Distance from a Point to a Line

The perpendicular distance from point $P(x_0, y_0)$ to line $Ax + By + C = 0$ is:

$$
\boxed{d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}}
$$

**Derivation**: The normal vector of line $L: Ax + By + C = 0$ is $(A, B)$. Draw a perpendicular from $P$ to $L$, with foot $H$. $H$ can be expressed as $H = (x_0 + tA, y_0 + tB)$, where $t$ is a real number. Since $H$ lies on $L$:

$$
A(x_0 + tA) + B(y_0 + tB) + C = 0
$$

$$
Ax_0 + By_0 + C + t(A^2 + B^2) = 0
$$

$$
t = -\frac{Ax_0 + By_0 + C}{A^2 + B^2}
$$

The distance $d = PH = \sqrt{(tA)^2 + (tB)^2} = |t|\sqrt{A^2 + B^2} = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$.

---

**Example 1**: Find the distance from $(2, -3)$ to $3x - 4y + 5 = 0$.

| Statement | Reason |
|-----------|--------|
| $A = 3$, $B = -4$, $C = 5$, $x_0 = 2$, $y_0 = -3$. | Identifying coefficients and point coordinates. |
| $d = \frac{|3(2) + (-4)(-3) + 5|}{\sqrt{3^2 + (-4)^2}}$. | Substituting into the distance formula. |
| $= \frac{|6 + 12 + 5|}{\sqrt{9 + 16}} = \frac{23}{5}$. | Evaluating numerator and denominator. |
| $d = \frac{23}{5} = 4.6$. | The perpendicular distance from the point to the line. |

---

**Example 2**: Find the distance between the parallel lines $2x + 3y - 6 = 0$ and $2x + 3y + 12 = 0$.

| Statement | Reason |
|-----------|--------|
| On $L_1: 2x + 3y - 6 = 0$, take $x = 0 \Rightarrow 3y = 6 \Rightarrow y = 2$. | Choosing a convenient point on the first line. |
| Point $P(0, 2)$ lies on $L_1$. | Substituting gives $0 + 6 - 6 = 0$, which is true. |
| Distance from $P$ to $L_2: 2x + 3y + 12 = 0$ is required. | Parallel lines have constant separation. |
| $d = \frac{|2(0) + 3(2) + 12|}{\sqrt{2^2 + 3^2}}$. | Distance formula with $P$ and $L_2$. |
| $= \frac{|0 + 6 + 12|}{\sqrt{4 + 9}} = \frac{18}{\sqrt{13}}$. | Simplifying. |
| The distance between the two parallel lines is $\frac{18}{\sqrt{13}}$. | This is the perpendicular distance between them. |

---

**Example 3**: The distance from point $(k, 4)$ to line $5x - 12y + 3 = 0$ is $2$. Find all possible values of $k$.

| Statement | Reason |
|-----------|--------|
| $d = \frac{|5k - 12(4) + 3|}{\sqrt{5^2 + (-12)^2}} = 2$. | Distance formula, equated to 2. |
| $\frac{|5k - 48 + 3|}{13} = 2 \Rightarrow \frac{|5k - 45|}{13} = 2$. | Simplifying numerator and denominator. |
| $|5k - 45| = 26$. | Multiplying both sides by 13. |
| $5k - 45 = 26$ or $5k - 45 = -26$. | Definition of absolute value. |
| $5k = 71$ or $5k = 19$. | Adding 45 to both sides. |
| $k = \frac{71}{5}$ or $k = \frac{19}{5}$. | Dividing by 5. |

### 9.1.7 Perpendicular Bisector

The perpendicular bisector of a line segment is a line that simultaneously satisfies two conditions:
1. It is **perpendicular** to the segment
2. It **passes through** the midpoint of the segment

**Steps to find it**:
1. Find the midpoint $M$ of segment $AB$
2. Find the gradient $m_{AB}$ of $AB$; the gradient of the perpendicular bisector is $-\frac{1}{m_{AB}}$ (if $m_{AB} \neq 0$)
3. Use the point-slope form to write the equation of the line through $M$ with gradient $-\frac{1}{m_{AB}}$

---

**Example 1**: Find the equation of the perpendicular bisector of the segment joining $A(1, 3)$ and $B(5, -1)$.

| Statement | Reason |
|-----------|--------|
| $M = \left(\frac{1 + 5}{2}, \frac{3 + (-1)}{2}\right) = (3, 1)$. | Midpoint formula. |
| $m_{AB} = \frac{-1 - 3}{5 - 1} = \frac{-4}{4} = -1$. | Gradient of $AB$. |
| Perpendicular gradient $= -\frac{1}{-1} = 1$. | Perpendicular gradient is the negative reciprocal. |
| Line through $(3, 1)$ with gradient $1$: $y - 1 = 1(x - 3)$. | Point-slope form. |
| $y = x - 2$. | Simplifying. |
| The perpendicular bisector is $y = x - 2$. | In general form: $x - y - 2 = 0$. |

---

**Example 2**: Points $P(2, 5)$ and $Q(8, 3)$. Find the intercepts of the perpendicular bisector of $PQ$ with the coordinate axes.

| Statement | Reason |
|-----------|--------|
| $M = \left(\frac{2 + 8}{2}, \frac{5 + 3}{2}\right) = (5, 4)$. | Midpoint of $PQ$. |
| $m_{PQ} = \frac{3 - 5}{8 - 2} = \frac{-2}{6} = -\frac{1}{3}$. | Gradient of $PQ$. |
| Perpendicular gradient $= 3$. | Negative reciprocal of $-\frac{1}{3}$. |
| Equation: $y - 4 = 3(x - 5)$. | Point-slope form with $(5, 4)$ and $m = 3$. |
| $y = 3x - 11$. | Simplifying to slope-intercept form. |
| $x$-intercept: set $y = 0 \Rightarrow 0 = 3x - 11 \Rightarrow x = \frac{11}{3}$. | The line crosses the $x$-axis where $y = 0$. |
| $y$-intercept: set $x = 0 \Rightarrow y = -11$. | The line crosses the $y$-axis where $x = 0$. |
| The perpendicular bisector meets the axes at $\left(\frac{11}{3}, 0\right)$ and $(0, -11)$. | These are the required intersection points. |

---

**Example 3**: $A(0, 0)$, $B(6, 2)$, $C(4, 8)$ are vertices of a triangle. Find the equation of the perpendicular bisector of $AB$, and prove that it passes through the midpoint of $AC$.

| Statement | Reason |
|-----------|--------|
| $M_{AB} = \left(\frac{0 + 6}{2}, \frac{0 + 2}{2}\right) = (3, 1)$. | Midpoint of $AB$. |
| $m_{AB} = \frac{2 - 0}{6 - 0} = \frac{1}{3}$. | Gradient of $AB$. |
| Perpendicular gradient $= -3$. | Negative reciprocal of $\frac{1}{3}$. |
| Equation: $y - 1 = -3(x - 3)$. | Point-slope form. |
| $y = -3x + 10$. | Simplifying. |
| Midpoint of $AC$: $\left(\frac{0 + 4}{2}, \frac{0 + 8}{2}\right) = (2, 4)$. | Midpoint formula for $AC$. |
| Does $(2, 4)$ satisfy $y = -3x + 10$? LHS: $4$, RHS: $-3(2) + 10 = 4$. | Substituting the point. |
| $4 = 4$, so the point lies on the line. | Therefore the perpendicular bisector of $AB$ passes through the midpoint of $AC$. |

---

## 9.2 Linearisation of Non-Linear Relationships

In scientific experiments, the relationship between two variables is often not linear but instead follows a **power function** $y = Ax^n$ or an **exponential function** $y = Ab^x$. Through suitable variable substitution, we can **transform** these non-linear relationships **into straight-line form**, and then use linear regression (calculating gradient and intercept) to determine the unknown parameters.

### 9.2.1 Power Function $y = Ax^n$

Taking natural logarithms of both sides of $y = Ax^n$:

$$
\ln y = \ln(Ax^n) = \ln A + \ln(x^n) = \ln A + n \ln x
$$

Let $Y = \ln y$, $X = \ln x$, then:

$$
\boxed{Y = nX + \ln A}
$$

This is a straight-line equation in $X$ and $Y$, with gradient $m = n$ and $Y$-intercept $c = \ln A$.

**Procedure**: For each experimental data pair $(x, y)$, compute $(\ln x, \ln y)$; plot $\ln x$ on the horizontal axis and $\ln y$ on the vertical axis; read the gradient (which equals $n$) and the $Y$-intercept (which equals $\ln A$), then exponentiate to obtain $A$.

### 9.2.2 Exponential Function $y = Ab^x$

Taking natural logarithms of both sides of $y = Ab^x$:

$$
\ln y = \ln(Ab^x) = \ln A + \ln(b^x) = \ln A + x \ln b
$$

Let $Y = \ln y$, $X = x$ (note that $X$ is the original $x$, no transformation needed), then:

$$
\boxed{Y = (\ln b)X + \ln A}
$$

This is a straight-line equation in $X$ and $Y$, with gradient $m = \ln b$ and $Y$-intercept $c = \ln A$.

**Procedure**: For each $(x, y)$, compute $(x, \ln y)$; plot $x$ on the horizontal axis and $\ln y$ on the vertical axis; read the gradient (which equals $\ln b$, then exponentiate to get $b$) and the $Y$-intercept (which equals $\ln A$, then exponentiate to get $A$).

---

**Example 1**: Variables $x$ and $y$ satisfy $y = Ax^n$. After transforming to $(\ln x, \ln y)$, the resulting straight line has gradient $2.5$ and $\ln y$-intercept $1.2$. Find $A$ and $n$.

| Statement | Reason |
|-----------|--------|
| $Y = nX + \ln A$, where $Y = \ln y$ and $X = \ln x$. | Linearised form of $y = Ax^n$. |
| The graph of $Y$ against $X$ has slope $2.5$ and $Y$-intercept $1.2$. | Given experimental results. |
| $n = 2.5$. | The slope equals $n$ in the linearised equation. |
| $\ln A = 1.2 \Rightarrow A = e^{1.2}$. | The $Y$-intercept equals $\ln A$. |
| The relationship is $y = e^{1.2} x^{2.5}$. | Substituting the values of $A$ and $n$. |

---

**Example 2**: Variables $x$ and $y$ satisfy $y = Ab^x$. After transforming to $(x, \ln y)$, the resulting straight line has slope $0.75$ and $\ln y$-intercept $2.3$. Find $A$ and $b$.

| Statement | Reason |
|-----------|--------|
| $Y = (\ln b)X + \ln A$, where $Y = \ln y$ and $X = x$. | Linearised form of $y = Ab^x$. |
| $\ln b = 0.75 \Rightarrow b = e^{0.75}$. | The slope equals $\ln b$. |
| $\ln A = 2.3 \Rightarrow A = e^{2.3}$. | The $Y$-intercept equals $\ln A$. |
| $y = e^{2.3} \cdot (e^{0.75})^x = e^{2.3 + 0.75x}$. | The exponential relationship. |

---

**Example 3**: Given $y = 5x^3$. Linearise it, and state the gradient and $Y$-intercept if $\ln x$ is plotted against $\ln y$.

| Statement | Reason |
|-----------|--------|
| $\ln y = \ln(5x^3) = \ln 5 + 3\ln x$. | Taking natural log of both sides. |
| $Y = 3X + \ln 5$, where $Y = \ln y$, $X = \ln x$. | The linearised equation. |
| The gradient is $3$. | This equals the exponent $n$. |
| The $Y$-intercept is $\ln 5 \approx 1.609$. | This equals $\ln A$. |

---



## 9.3 Equation of a Circle

A circle is the set of all points in a plane whose distance from a fixed point (the centre) is a constant (the radius). This definition directly gives the standard equation of a circle.

### 9.3.1 Standard Form

Let the centre be $C(a, b)$ and the radius be $r$. For any point $P(x, y)$ on the circle, $PC = r$ by the distance formula:

$$
\sqrt{(x - a)^2 + (y - b)^2} = r
$$

Squaring both sides gives the standard form:

$$
\boxed{(x - a)^2 + (y - b)^2 = r^2}
$$

When the centre is at the origin, $a = b = 0$, the equation simplifies to $x^2 + y^2 = r^2$.

### 9.3.2 General Form

Expanding the standard form:

$$
x^2 - 2ax + a^2 + y^2 - 2by + b^2 = r^2
$$

Rearranging and collecting constant terms:

$$
x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - r^2) = 0
$$

Let $g = -a$, $f = -b$, $c = a^2 + b^2 - r^2$. Then we obtain the general form:

$$
\boxed{x^2 + y^2 + 2gx + 2fy + c = 0}
$$

Working backwards from the general form to find the centre and radius:

- Centre: $(-g, -f)$
- Radius: $r = \sqrt{g^2 + f^2 - c}$

**Existence condition**: $g^2 + f^2 - c > 0$ represents a real circle; $= 0$ represents a point circle; $< 0$ represents an imaginary circle (no real graph).

---

**Example 1**: Write the equation of the circle with centre $(-3, 4)$ and radius $6$.

| Statement | Reason |
|-----------|--------|
| $(x - (-3))^2 + (y - 4)^2 = 6^2$. | Standard form $(x - a)^2 + (y - b)^2 = r^2$. |
| $(x + 3)^2 + (y - 4)^2 = 36$. | Simplifying. |
| $x^2 + 6x + 9 + y^2 - 8y + 16 = 36$. | Expanding the brackets. |
| $x^2 + y^2 + 6x - 8y - 11 = 0$. | Collecting terms and subtracting 36. |

---

**Example 2**: The equation of a circle is $x^2 + y^2 - 10x + 4y + 13 = 0$. Find its centre and radius.

| Statement | Reason |
|-----------|--------|
| $2g = -10 \Rightarrow g = -5$. | Comparing with $x^2 + y^2 + 2gx + 2fy + c = 0$. |
| $2f = 4 \Rightarrow f = 2$. | Coefficient of $y$. |
| $c = 13$. | Constant term. |
| Centre $= (-g, -f) = (5, -2)$. | Centre formula. |
| $r = \sqrt{g^2 + f^2 - c} = \sqrt{(-5)^2 + 2^2 - 13}$. | Radius formula. |
| $= \sqrt{25 + 4 - 13} = \sqrt{16} = 4$. | Evaluating. |
| Centre is $(5, -2)$ and radius is $4$. | Final answer. |

---

**Example 3**: Use completing the square to convert $x^2 + y^2 + 6x - 2y - 6 = 0$ to standard form, and find its centre and radius.

| Statement | Reason |
|-----------|--------|
| $(x^2 + 6x) + (y^2 - 2y) = 6$. | Grouping $x$ and $y$ terms, moving constant to RHS. |
| $(x^2 + 6x + 9) + (y^2 - 2y + 1) = 6 + 9 + 1$. | Completing the square: add $(\frac{6}{2})^2 = 9$ and $(\frac{-2}{2})^2 = 1$ to both sides. |
| $(x + 3)^2 + (y - 1)^2 = 16$. | Factorising the perfect squares. |
| Centre $= (-3, 1)$ and radius $= \sqrt{16} = 4$. | Reading from standard form $(x - a)^2 + (y - b)^2 = r^2$. |

---

## 9.4 Lines and Circles

### 9.4.1 Determining the Positional Relationship

Substitute the line equation into the circle equation to obtain a quadratic in $x$ (or $y$). The discriminant $\Delta$ of this quadratic determines the number of intersection points:

- $\Delta > 0$: Two distinct real roots $\Rightarrow$ Two intersection points (the line is a **secant**)
- $\Delta = 0$: One repeated root $\Rightarrow$ One intersection point (the line is a **tangent**)
- $\Delta < 0$: No real roots $\Rightarrow$ No intersection (the line and circle are **disjoint**)

### 9.4.2 Three Methods for Finding Tangents

**Case 1: Point of tangency $(x_1, y_1)$ is known to be on the circle**

For the circle $(x - a)^2 + (y - b)^2 = r^2$, the tangent at point $(x_1, y_1)$ is:

$$
\boxed{(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2}
$$

**Derivation**: The vector from centre $C(a, b)$ to the point of tangency $P(x_1, y_1)$ is $(x_1 - a, y_1 - b)$. The tangent is perpendicular to the radius $CP$. Let $Q(x, y)$ be any point on the tangent. Then the dot product of vector $\overrightarrow{PQ} = (x - x_1, y - y_1)$ and $\overrightarrow{CP}$ is zero:

$$
(x_1 - a)(x - x_1) + (y_1 - b)(y - y_1) = 0
$$

Rearranging gives $(x_1 - a)(x - a) + (y_1 - b)(y - b) = (x_1 - a)^2 + (y_1 - b)^2 = r^2$.

For a circle centred at the origin, $x^2 + y^2 = r^2$, the tangent simplifies to:

$$
\boxed{x_1 x + y_1 y = r^2}
$$

---

**Example 1 (Known point of tangency)**: Circle $x^2 + y^2 = 25$, find the tangent at $(3, -4)$.

| Statement | Reason |
|-----------|--------|
| Centre is $(0, 0)$, $r^2 = 25$, point is $(3, -4)$. | Identifying from $x^2 + y^2 = r^2$ form. |
| Tangent formula: $x_1 x + y_1 y = r^2$. | Formula for a circle centred at the origin. |
| $3x + (-4)y = 25 \Rightarrow 3x - 4y = 25$. | Substituting $x_1 = 3$, $y_1 = -4$, $r^2 = 25$. |
| $3x - 4y - 25 = 0$. | The equation of the tangent in general form. |

---

**Example 2 (Known point of tangency)**: Circle $(x - 2)^2 + (y + 1)^2 = 16$, find the tangent at $(6, -1)$.

| Statement | Reason |
|-----------|--------|
| Centre $(a, b) = (2, -1)$, $r^2 = 16$, point $(x_1, y_1) = (6, -1)$. | Given in standard form. |
| Formula: $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$. | Tangent at a point on the circle. |
| $(6 - 2)(x - 2) + (-1 + 1)(y + 1) = 16$. | Substituting values. |
| $4(x - 2) + 0 \cdot (y + 1) = 16$. | Simplifying. |
| $4x - 8 = 16 \Rightarrow 4x = 24 \Rightarrow x = 6$. | Solving. |
| The tangent is the vertical line $x = 6$. | This is consistent: $(6, -1)$ is the rightmost point of the circle. |

---

**Case 2: The gradient $m$ of the tangent is known**

For a circle with centre $(a, b)$ and radius $r$, the equation of the tangent with gradient $m$ is:

$$
\boxed{y - b = m(x - a) \pm r\sqrt{1 + m^2}}
$$

**Derivation**: Let the tangent be $y = mx + k$. The distance from the centre to the line equals the radius:

$$
\frac{|ma - b + k|}{\sqrt{m^2 + 1}} = r
$$

Solving gives $k = b - ma \pm r\sqrt{m^2 + 1}$. Substituting into $y = mx + k$ gives the result.

When the centre is at the origin, this simplifies to $y = mx \pm r\sqrt{1 + m^2}$.

---

**Example 3 (Known gradient)**: Find the equations of the tangents to the circle $x^2 + y^2 = 9$ with gradient $2$.

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, $r = 3$, $m = 2$. | Given. |
| $y = mx \pm r\sqrt{1 + m^2} = 2x \pm 3\sqrt{1 + 4}$. | Formula for tangent with given slope, centre at origin. |
| $y = 2x \pm 3\sqrt{5}$. | Simplifying. |
| The two tangents are $y = 2x + 3\sqrt{5}$ and $y = 2x - 3\sqrt{5}$. | The $\pm$ gives two parallel tangents, one above and one below. |

---

**Case 3: Tangent drawn from an external point $(x_0, y_0)$**

Procedure:
1. Let the gradient of the tangent be $m$, equation $y - y_0 = m(x - x_0)$
2. Convert to general form $mx - y + (y_0 - mx_0) = 0$
3. Set the distance from the centre to this line equal to the radius, solving for $m$
4. Check whether the vertical line $x = x_0$ is also a tangent

---

**Example 4 (External point)**: Circle $x^2 + y^2 = 5$ and external point $P(4, 3)$. Find the equations of the tangents from $P$ to the circle.

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, radius $r = \sqrt{5}$. | Given circle. |
| Let the tangent be $y - 3 = m(x - 4)$. | Point-slope form through $P(4, 3)$. |
| $mx - y + (3 - 4m) = 0$. | Rearranging to general form. |
| $\frac{|m(0) - 0 + (3 - 4m)|}{\sqrt{m^2 + 1}} = \sqrt{5}$. | Distance from centre $(0,0)$ to line equals radius. |
| $|3 - 4m| = \sqrt{5}\sqrt{m^2 + 1}$. | Multiplying both sides by $\sqrt{m^2 + 1}$. |
| $(3 - 4m)^2 = 5(m^2 + 1)$. | Squaring both sides. |
| $9 - 24m + 16m^2 = 5m^2 + 5$. | Expanding. |
| $11m^2 - 24m + 4 = 0$. | Collecting like terms. |
| $(11m - 2)(m - 2) = 0 \Rightarrow m = \frac{2}{11}$ or $m = 2$. | Factorising. |
| For $m = 2$: $y - 3 = 2(x - 4) \Rightarrow y = 2x - 5$. | First tangent. |
| For $m = \frac{2}{11}$: $y - 3 = \frac{2}{11}(x - 4) \Rightarrow 11y - 33 = 2x - 8 \Rightarrow 2x - 11y + 25 = 0$. | Second tangent. |
| Check $x = 4$: distance from $(0,0)$ to $x = 4$ is $4 \neq \sqrt{5}$. | Vertical line is not a tangent. |
| The two tangents are $y = 2x - 5$ and $2x - 11y + 25 = 0$. | Final answer. |

### 9.4.3 Comprehensive Judgement and Evaluation

**Example 5**: The line $y = x + k$ is tangent to the circle $x^2 + y^2 = 8$. Find $k$.

| Statement | Reason |
|-----------|--------|
| Substitute $y = x + k$ into $x^2 + y^2 = 8$. | Finding intersection points. |
| $x^2 + (x + k)^2 = 8$. | Substituting. |
| $x^2 + x^2 + 2kx + k^2 = 8$. | Expanding. |
| $2x^2 + 2kx + (k^2 - 8) = 0$. | Collecting terms. |
| For tangency, $\Delta = 0$. | A tangent touches at exactly one point. |
| $\Delta = (2k)^2 - 4(2)(k^2 - 8) = 4k^2 - 8k^2 + 64$. | Discriminant of the quadratic. |
| $\Delta = -4k^2 + 64 = 0$. | Setting discriminant to zero. |
| $k^2 = 16 \Rightarrow k = \pm 4$. | Solving for $k$. |
| The line $y = x + 4$ or $y = x - 4$ is tangent to the circle. | Two parallel tangents with slope $1$. |

---

**Example 6**: Determine the position of the line $y = 2x - 1$ relative to the circle $(x - 1)^2 + (y + 2)^2 = 5$.

| Statement | Reason |
|-----------|--------|
| Centre $(1, -2)$, radius $r = \sqrt{5}$. | From standard form. |
| Substitute $y = 2x - 1$: $(x - 1)^2 + (2x - 1 + 2)^2 = 5$. | Substituting into circle equation. |
| $(x - 1)^2 + (2x + 1)^2 = 5$. | Simplifying inside brackets. |
| $x^2 - 2x + 1 + 4x^2 + 4x + 1 = 5$. | Expanding. |
| $5x^2 + 2x + 2 = 5 \Rightarrow 5x^2 + 2x - 3 = 0$. | Collecting terms. |
| $\Delta = 2^2 - 4(5)(-3) = 4 + 60 = 64 > 0$. | Discriminant is positive. |
| Since $\Delta > 0$, the line intersects the circle at two distinct points. | The line is a secant. |

---

## 9.5 Positional Relationships Between Two Circles

### 9.5.1 Five Types of Relationships

Let circle $C_1$ have centre $O_1$ and radius $r_1$; circle $C_2$ have centre $O_2$ and radius $r_2$; and let the distance between centres be $d = O_1O_2$.

| Relationship | Condition | Description |
|------|------|-----------|
| **Separate (externally disjoint)** | $d > r_1 + r_2$ | No common points, circles do not overlap |
| **Externally tangent** | $d = r_1 + r_2$ | Exactly one common point, touching externally |
| **Intersecting** | $|r_1 - r_2| < d < r_1 + r_2$ | Two common points |
| **Internally tangent** | $d = |r_1 - r_2|$ | Exactly one common point, one circle inside the other |
| **One contains the other** | $d < |r_1 - r_2|$ | One circle completely inside the other, no common points |
| **Concentric circles** | $d = 0$ (and $r_1 \neq r_2$) | Centres coincide (a special case of one containing the other) |

### 9.5.2 Common Chord

When two circles intersect at two points, the line joining these two points is called the **common chord**.

Let the equations of the two circles be:

$$
C_1: x^2 + y^2 + 2g_1x + 2f_1y + c_1 = 0
$$

$$
C_2: x^2 + y^2 + 2g_2x + 2f_2y + c_2 = 0
$$

The intersection points satisfy both equations. Subtracting the equations eliminates the $x^2 + y^2$ terms, leaving a straight line:

$$
\boxed{2(g_1 - g_2)x + 2(f_1 - f_2)y + (c_1 - c_2) = 0}
$$

Since both intersection points satisfy both circle equations, they must also satisfy the subtracted equation. Therefore this line passes through both intersection points — it is the **common chord**. When the circles are tangent, this line becomes the **common tangent**.

---

**Example 1 (Determining positional relationship)**: Determine the positional relationship between $C_1: x^2 + y^2 = 4$ and $C_2: (x - 4)^2 + y^2 = 1$.

| Statement | Reason |
|-----------|--------|
| $C_1$: centre $O_1(0, 0)$, radius $r_1 = 2$. | From standard form. |
| $C_2$: centre $O_2(4, 0)$, radius $r_2 = 1$. | From standard form. |
| $d = \sqrt{(4 - 0)^2 + (0 - 0)^2} = 4$. | Distance between centres. |
| $r_1 + r_2 = 2 + 1 = 3$. | Sum of radii. |
| $d = 4 > 3 = r_1 + r_2$. | Since the centre distance exceeds the sum of radii. |
| The circles are **separate** (externally disjoint). | They have no common points. |

---

**Example 2 (Tangency condition)**: Circle $C_1: x^2 + y^2 = 9$ is externally tangent to $C_2: (x - 5)^2 + y^2 = r^2$. Find $r$.

| Statement | Reason |
|-----------|--------|
| $C_1$: $(0, 0)$, $r_1 = 3$. $C_2$: $(5, 0)$, $r_2 = r$. | Identifying centres and radii. |
| $d = \sqrt{(5 - 0)^2 + 0^2} = 5$. | Distance between centres. |
| For external tangency: $d = r_1 + r_2$. | Definition of externally tangent circles. |
| $5 = 3 + r \Rightarrow r = 2$. | Solving for $r$. |
| The radius of $C_2$ must be $2$. | So the circles touch at exactly one point. |

---

**Example 3 (Finding the common chord)**: Two circles $C_1: x^2 + y^2 - 6x + 4y - 3 = 0$ and $C_2: x^2 + y^2 + 2x - 8y + 5 = 0$ intersect. Find the equation of the common chord.

| Statement | Reason |
|-----------|--------|
| $C_1 - C_2$: $(x^2 + y^2 - 6x + 4y - 3) - (x^2 + y^2 + 2x - 8y + 5) = 0$. | Subtracting the equations eliminates $x^2 + y^2$. |
| $-6x + 4y - 3 - 2x + 8y - 5 = 0$. | Removing brackets and simplifying signs. |
| $-8x + 12y - 8 = 0$. | Collecting like terms. |
| Divide by $-4$: $2x - 3y + 2 = 0$. | Simplifying. |
| The common chord is $2x - 3y + 2 = 0$. | This line passes through both intersection points. |

---

## 9.6 Comprehensive Examples (Answers at the End of Chapter)

The following examples integrate multiple knowledge points from this chapter. It is recommended to attempt them independently before checking the detailed solutions.

---

**Example 1**: Circle $C$ has its centre on the line $y = 2x + 1$, and it passes through points $A(1, 4)$ and $B(3, 0)$. Find the equation of circle $C$.

---

**Example 2**: The line $y = 2x + k$ intersects the circle $x^2 + y^2 - 2x + 4y - 4 = 0$ at two distinct points. Find the range of $k$.

---

**Example 3**: Circle $C_1: (x - 1)^2 + (y - 3)^2 = 25$ and circle $C_2: (x + 2)^2 + (y - 7)^2 = 4$.
(a) Determine the positional relationship between the two circles.
(b) If they intersect, find the equation of the common chord.

---

**Example 4**: Circle $x^2 + y^2 = 10$ and external point $P(5, 5)$. Find the equations of the two tangents from $P$ to the circle.

---

**Example 5**: Points $A(2, 5)$, $B(6, 1)$, $C(8, 5)$.
(a) Find the equation of the perpendicular bisector of $AB$.
(b) Find the equation of the perpendicular bisector of $BC$.
(c) Prove that the intersection of these two perpendicular bisectors is the centre of the circle passing through $A$, $B$, and $C$.

---

## 9.7 Solutions to Comprehensive Examples

### Solution to Example 1

| Statement | Reason |
|-----------|--------|
| Let the centre be $(h, 2h + 1)$. | The centre lies on $y = 2x + 1$. |
| $A(1, 4)$ and $B(3, 0)$ are on the circle. | Given. |
| $CA = CB$ (both equal the radius). | All points on a circle are equidistant from the centre. |
| $(h - 1)^2 + (2h + 1 - 4)^2 = (h - 3)^2 + (2h + 1 - 0)^2$. | Using distance formula: $CA^2 = CB^2$. |
| $(h - 1)^2 + (2h - 3)^2 = (h - 3)^2 + (2h + 1)^2$. | Simplifying $y$-differences. |
| $h^2 - 2h + 1 + 4h^2 - 12h + 9 = h^2 - 6h + 9 + 4h^2 + 4h + 1$. | Expanding all squares. |
| $5h^2 - 14h + 10 = 5h^2 - 2h + 10$. | Collecting like terms on both sides. |
| $-14h + 10 = -2h + 10 \Rightarrow -12h = 0 \Rightarrow h = 0$. | Subtracting $5h^2$ and $10$ from both sides. |
| Centre $= (0, 1)$. | Substituting $h = 0$ into $(h, 2h + 1)$. |
| $r^2 = (0 - 1)^2 + (1 - 4)^2 = 1 + 9 = 10$. | Distance from centre to $A(1, 4)$. |
| The circle equation is $(x - 0)^2 + (y - 1)^2 = 10$, i.e., $x^2 + (y - 1)^2 = 10$. | Final answer. |

---

### Solution to Example 2

| Statement | Reason |
|-----------|--------|
| $x^2 + y^2 - 2x + 4y - 4 = 0 \Rightarrow (x - 1)^2 + (y + 2)^2 = 9$. | Completing the square to find centre and radius. |
| Centre $(1, -2)$, radius $r = 3$. | From standard form. |
| Substitute $y = 2x + k$: $(x - 1)^2 + (2x + k + 2)^2 = 9$. | Substituting into circle equation. |
| $x^2 - 2x + 1 + 4x^2 + 4(k + 2)x + (k + 2)^2 = 9$. | Expanding. |
| $5x^2 + [4(k + 2) - 2]x + [1 + (k + 2)^2 - 9] = 0$. | Grouping $x^2$, $x$ and constant terms. |
| $5x^2 + (4k + 6)x + (k^2 + 4k + 4 - 8) = 0$. | Simplifying coefficients. |
| $5x^2 + (4k + 6)x + (k^2 + 4k - 4) = 0$. | Final quadratic in $x$. |
| For two distinct intersections, $\Delta > 0$. | A quadratic with $\Delta > 0$ has two distinct real roots. |
| $\Delta = (4k + 6)^2 - 4(5)(k^2 + 4k - 4) > 0$. | Discriminant condition. |
| $16k^2 + 48k + 36 - 20k^2 - 80k + 80 > 0$. | Expanding. |
| $-4k^2 - 32k + 116 > 0$. | Collecting terms. |
| Divide by $-4$ (reverse inequality): $k^2 + 8k - 29 < 0$. | Note: dividing by a negative flips the inequality. |
| Roots of $k^2 + 8k - 29 = 0$: $k = \frac{-8 \pm \sqrt{64 + 116}}{2} = \frac{-8 \pm \sqrt{180}}{2} = -4 \pm 3\sqrt{5}$. | Quadratic formula. |
| Since the quadratic in $k$ opens upward, $k^2 + 8k - 29 < 0$ between the roots. | The inequality is satisfied for values between the roots. |
| $-4 - 3\sqrt{5} < k < -4 + 3\sqrt{5}$. | The range of $k$ for which the line intersects the circle at two points. |

---

### Solution to Example 3

**Part (a)**

| Statement | Reason |
|-----------|--------|
| $C_1$: centre $O_1(1, 3)$, $r_1 = 5$. | From $(x - 1)^2 + (y - 3)^2 = 25$. |
| $C_2$: centre $O_2(-2, 7)$, $r_2 = 2$. | From $(x + 2)^2 + (y - 7)^2 = 4$. |
| $d = \sqrt{(1 - (-2))^2 + (3 - 7)^2} = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = 5$. | Distance between centres. |
| $r_1 + r_2 = 5 + 2 = 7$, $|r_1 - r_2| = 3$. | Sum and difference of radii. |
| $3 < 5 < 7$, i.e., $|r_1 - r_2| < d < r_1 + r_2$. | $d$ lies between the difference and the sum. |
| Therefore the circles **intersect at two points**. | Condition for two intersections. |

**Part (b)**

| Statement | Reason |
|-----------|--------|
| $C_1$ in general form: $x^2 + y^2 - 2x - 6y - 15 = 0$. | Expanding $(x - 1)^2 + (y - 3)^2 = 25$. |
| $C_2$ in general form: $(x+2)^2 + (y-7)^2 = 4 \Rightarrow x^2 + 4x + 4 + y^2 - 14y + 49 = 4 \Rightarrow x^2 + y^2 + 4x - 14y + 49 = 0$. | Expanding $(x + 2)^2 + (y - 7)^2 = 4$. |
| Subtract $C_2$ from $C_1$: $(x^2 + y^2 - 2x - 6y - 15) - (x^2 + y^2 + 4x - 14y + 49) = 0$. | $x^2 + y^2$ terms cancel. |
| $-2x - 6y - 15 - 4x + 14y - 49 = 0 \Rightarrow -6x + 8y - 64 = 0$. | Simplifying. |
| Divide by $-2$: $3x - 4y + 32 = 0$. | The common chord equation. |

---

### Solution to Example 4

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, radius $r = \sqrt{10}$. | Circle $x^2 + y^2 = 10$. |
| Let tangent have slope $m$, equation $y - 5 = m(x - 5)$. | Point-slope form through $P(5, 5)$. |
| $mx - y + (5 - 5m) = 0$. | General form. |
| Distance from $(0,0)$ to line $= \frac{|5 - 5m|}{\sqrt{m^2 + 1}} = \sqrt{10}$. | Distance equals radius. |
| $|5 - 5m| = \sqrt{10}\sqrt{m^2 + 1}$. | Multiplying both sides. |
| $(5 - 5m)^2 = 10(m^2 + 1)$. | Squaring both sides. |
| $25 - 50m + 25m^2 = 10m^2 + 10$. | Expanding. |
| $15m^2 - 50m + 15 = 0$. | Collecting terms. |
| Divide by $5$: $3m^2 - 10m + 3 = 0$. | Simplifying. |
| $(3m - 1)(m - 3) = 0 \Rightarrow m = 3$ or $m = \frac{1}{3}$. | Factorising. |
| For $m = 3$: $y - 5 = 3(x - 5) \Rightarrow y = 3x - 10$. | First tangent. |
| For $m = \frac{1}{3}$: $y - 5 = \frac{1}{3}(x - 5) \Rightarrow 3y - 15 = x - 5 \Rightarrow x - 3y + 10 = 0$. | Second tangent. |
| Check $x = 5$: distance from $(0,0)$ to $x = 5$ is $5 \neq \sqrt{10}$. | Not a tangent. |
| The two tangents are $y = 3x - 10$ and $x - 3y + 10 = 0$. | Final answer. |

---

### Solution to Example 5

**Part (a)**

| Statement | Reason |
|-----------|--------|
| $A(2, 5)$, $B(6, 1)$. | Given. |
| Midpoint $M_{AB} = \left(\frac{2 + 6}{2}, \frac{5 + 1}{2}\right) = (4, 3)$. | Midpoint formula. |
| $m_{AB} = \frac{1 - 5}{6 - 2} = \frac{-4}{4} = -1$. | Gradient of $AB$. |
| Perpendicular gradient $= 1$. | Negative reciprocal of $-1$. |
| Equation: $y - 3 = 1(x - 4) \Rightarrow y = x - 1$. | Perpendicular bisector of $AB$. |

**Part (b)**

| Statement | Reason |
|-----------|--------|
| $B(6, 1)$, $C(8, 5)$. | Given. |
| Midpoint $M_{BC} = \left(\frac{6 + 8}{2}, \frac{1 + 5}{2}\right) = (7, 3)$. | Midpoint formula. |
| $m_{BC} = \frac{5 - 1}{8 - 6} = \frac{4}{2} = 2$. | Gradient of $BC$. |
| Perpendicular gradient $= -\frac{1}{2}$. | Negative reciprocal of $2$. |
| Equation: $y - 3 = -\frac{1}{2}(x - 7)$. | Perpendicular bisector of $BC$. |
| $y - 3 = -\frac{1}{2}x + \frac{7}{2} \Rightarrow y = -\frac{1}{2}x + \frac{13}{2}$. | Simplifying. |

**Part (c)**

| Statement | Reason |
|-----------|--------|
| Intersection of the two bisectors: $x - 1 = -\frac{1}{2}x + \frac{13}{2}$. | Equating $y$ from both equations. |
| $x + \frac{1}{2}x = \frac{13}{2} + 1 \Rightarrow \frac{3}{2}x = \frac{15}{2} \Rightarrow x = 5$. | Solving for $x$. |
| $y = 5 - 1 = 4$. | Substituting $x = 5$ into $y = x - 1$. |
| Intersection $O = (5, 4)$. | The common point of the two perpendicular bisectors. |
| $OA = \sqrt{(5 - 2)^2 + (4 - 5)^2} = \sqrt{9 + 1} = \sqrt{10}$. | Distance from $O$ to $A$. |
| $OB = \sqrt{(5 - 6)^2 + (4 - 1)^2} = \sqrt{1 + 9} = \sqrt{10}$. | Distance from $O$ to $B$. |
| $OC = \sqrt{(5 - 8)^2 + (4 - 5)^2} = \sqrt{9 + 1} = \sqrt{10}$. | Distance from $O$ to $C$. |
| $OA = OB = OC = \sqrt{10}$. | $O$ is equidistant from all three vertices. |
| Therefore $O(5, 4)$ is the centre of the circle passing through $A$, $B$ and $C$, with radius $\sqrt{10}$. | The perpendicular bisectors of any two chords of a circle intersect at the centre. |

---

## 9.8 Chapter Summary

| Topic | Core Formula / Method |
|------|----------------|
| **Equation of a line** | Slope-intercept $y = mx + c$, point-slope $y - y_1 = m(x - x_1)$, general $Ax + By + C = 0$ |
| **Parallel condition** | $m_1 = m_2$ |
| **Perpendicular condition** | $m_1 \cdot m_2 = -1$ |
| **Midpoint formula** | $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ |
| **Distance between two points** | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| **Distance from point to line** | $d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$ |
| **Perpendicular bisector** | Gradient $= -\frac{1}{m_{AB}}$, passes through midpoint of $AB$ |
| **Linearisation — Power function** | $y = Ax^n \Rightarrow \ln y = n\ln x + \ln A$ |
| **Linearisation — Exponential function** | $y = Ab^x \Rightarrow \ln y = (\ln b)x + \ln A$ |
| **Standard form of a circle** | $(x - a)^2 + (y - b)^2 = r^2$, centre $(a, b)$, radius $r$ |
| **General form of a circle** | $x^2 + y^2 + 2gx + 2fy + c = 0$, centre $(-g, -f)$, radius $\sqrt{g^2 + f^2 - c}$ |
| **Line and circle** | Substitute $\to$ quadratic $\to$ $\Delta > 0$ intersect, $\Delta = 0$ tangent, $\Delta < 0$ disjoint |
| **Tangent (known point of tangency)** | $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$ |
| **Tangent (known gradient)** | $y - b = m(x - a) \pm r\sqrt{1 + m^2}$ |
| **Two circles** | Compare $d$ with $r_1 + r_2$ and $|r_1 - r_2|$ |
| **Common chord** | Subtract one circle equation from the other |

---
---

