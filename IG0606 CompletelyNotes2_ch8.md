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

# Chapter 8: Trigonometry (Including Radians)

---

## Introduction and Syllabus Mapping

Trigonometry is one of the most instrumental and widely applicable chapters in Additional Mathematics. From angle measurement in geometry, to differentiation and integration of trigonometric functions in calculus, to motion analysis in physics — trigonometry is everywhere. This chapter will systematically build your complete understanding of trigonometric functions.

### Syllabus Mapping (Cambridge IGCSE Additional Mathematics 0606, 2028–2030)

| Syllabus Ref | Content | Corresponding Section |
|---------|------|---------|
| 9.1 | Arc length and sector area (radians) | **8.1** |
| 10.1 | The six trigonometric functions for any angle | **8.2** |
| 10.2 | Amplitude and period of trigonometric functions | **8.3** |
| 10.3 | Sketch graphs of $y = a\sin(bx) + c$ etc. | **8.3** |
| 10.4 | Use identities such as $\sin^2 A + \cos^2 A = 1$ | **8.4** |
| 10.5 | Solve trigonometric equations (including all six functions) | **8.5** |
| 10.6 | Prove trigonometric identities | **8.6** |

> **Exam information**: Both Paper 1 (non-calculator) and Paper 2 (calculator) may test trigonometry. Radians are **mandatory** in the calculus sections. The formula sheet provided only lists the three identities $\sin^2 A + \cos^2 A = 1$, $\sec^2 A = 1 + \tan^2 A$, $\csc^2 A = 1 + \cot^2 A$. **Arc length and sector area formulas are not provided** and must be memorised.

---

## 8.1 Radians (Arc Length, Sector Area, Composite Figures)

### 8.1.1 Why Use Radians?

In elementary geometry, we are used to measuring angles in **degrees**. However, in higher mathematics, **radians** are the natural unit. There are two reasons:

**Reason 1**: Radians directly relate angles to arc length. When angles are expressed in radians, the arc length formula $s = r\theta$ is extremely concise. If degrees were used, the formula would become $s = \frac{\pi r\theta}{180}$, introducing an unnecessary coefficient.

**Reason 2** (more important): In calculus, the derivative formulas for trigonometric functions are only simple and elegant when using radians. For example:

$$
\frac{d}{dx}\sin x = \cos x \quad (\text{radians})
$$

If degrees were used, the formula would become $\frac{d}{dx}\sin x^\circ = \frac{\pi}{180}\cos x^\circ$, introducing the extra constant factor $\pi/180$. Therefore, in the IGCSE Additional Mathematics calculus section, **all angles must be in radians**.

### 8.1.2 Definition of a Radian

**Definition**: One radian is the angle subtended at the centre of a circle when the arc length equals the radius.

Let the radius of a circle be $r$, the length of an arc be $s$, and the angle subtended by that arc be $\theta$ (in radians). Then:

$$
\theta = \frac{s}{r} \quad \text{or equivalently} \quad s = r\theta
$$

When $s = r$, $\theta = 1$ radian.

**Derivation of conversion to degrees**: A full circle corresponds to $360^\circ$, and the full circumference is $2\pi r$. Using $s = r\theta$, a full circle gives:

$$
2\pi r = r \times (\text{number of radians in a full circle})
$$

Thus the number of radians in a full circle is $2\pi$, i.e.:

$$
360^\circ = 2\pi \text{ radians}
$$

Dividing both sides by 2:

$$
180^\circ = \pi \text{ radians}
$$

From this all conversion relationships can be derived:

$$
1^\circ = \frac{\pi}{180} \text{ radians}, \qquad
1 \text{ radian} = \frac{180^\circ}{\pi} \approx 57.3^\circ
$$

**Common angles in radians**:

| Degrees | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|------|-----------|------------|------------|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Radians | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

**Memory tip**: Remember $\pi = 180^\circ$, then work out the proportion. For example, $30^\circ = \frac{180^\circ}{6} = \frac{\pi}{6}$.

### 8.1.3 Derivation of the Arc Length Formula

In a circle of radius $r$, the full circumference is $2\pi r$, corresponding to a central angle of $2\pi$ radians.

Let the central angle be $\theta$ radians, and the arc length subtended by it be $s$. Since arc length is proportional to the central angle:

$$
\frac{s}{2\pi r} = \frac{\theta}{2\pi}
$$

Cross-multiplying:

$$
s = \frac{\theta}{2\pi} \times 2\pi r = r\theta
$$

Therefore:

$$
\boxed{s = r\theta}
$$

where $\theta$ **must be in radians**.

### 8.1.4 Derivation of the Sector Area Formula

**Method 1 (Proportion method)**: The area of a full circle is $\pi r^2$, corresponding to $2\pi$ radians. The ratio of the sector area $A$ to the full circle area equals the ratio of $\theta$ to $2\pi$:

$$
\frac{A}{\pi r^2} = \frac{\theta}{2\pi}
$$

$$
A = \frac{\theta}{2\pi} \times \pi r^2 = \frac{1}{2}r^2\theta
$$

**Method 2 (Integration, calculus perspective)**: Consider the sector as composed of infinitely many tiny triangles. The area of each small triangle is approximately $\frac{1}{2}r \cdot r\,d\theta = \frac{1}{2}r^2\,d\theta$. Integrating from $0$ to $\theta$:

$$
A = \int_0^\theta \frac{1}{2}r^2\,d\theta = \frac{1}{2}r^2\theta
$$

Both methods give the same result:

$$
\boxed{A = \frac{1}{2}r^2\theta}
$$

### 8.1.5 Area of a Segment

In a sector, the line segment joining the two endpoints of the arc is called the **chord**. The region between the chord and the arc is called a **segment**.

**Derivation of the segment area**:

Segment area $=$ Sector area $-$ Triangle area

We already know the sector area is $\frac{1}{2}r^2\theta$. The triangle is an isosceles triangle formed by two radii and the chord. Its area can be found using the "two sides and included angle" formula:

$$
A_{\triangle} = \frac{1}{2} \cdot r \cdot r \cdot \sin\theta = \frac{1}{2}r^2\sin\theta
$$

Therefore:

$$
\boxed{A_{\text{segment}} = \frac{1}{2}r^2\theta - \frac{1}{2}r^2\sin\theta = \frac{1}{2}r^2(\theta - \sin\theta)}
$$

> ⚠️ **Note**: $\theta$ in this formula must be in radians, and it is the central angle of the sector.

### 8.1.6 Problem-Solving Strategy for Composite Figures

When encountering composite figures containing arcs, sectors, and triangles, the general approach is:

1. **Decompose the figure**: Break the complex shape into basic shapes such as sectors, triangles, rectangles, etc.
2. **Identify known quantities**: Mark all known radii, angles (note whether they are in degrees or radians), and side lengths
3. **Unify units**: Convert all angles to radians (if they are not already)
4. **Calculate separately**: Use the arc length, sector area, and triangle area formulas to compute each part
5. **Combine results**: Add or subtract according to the geometric relationships

### 8.1.7 Worked Examples

---

**Example 1 (Converting between degrees and radians)**:
(a) Convert $150^\circ$ to radians.
(b) Convert $\frac{5\pi}{6}$ radians to degrees.

**Solution**:

(a) Using $1^\circ = \frac{\pi}{180}$ radians:

$$
150^\circ = 150 \times \frac{\pi}{180} = \frac{150\pi}{180} = \frac{5\pi}{6} \text{ radians}
$$

(b) Using $1$ radian $= \frac{180^\circ}{\pi}$:

$$
\frac{5\pi}{6} \text{ radians} = \frac{5\pi}{6} \times \frac{180^\circ}{\pi} = \frac{5 \times 180^\circ}{6} = 150^\circ
$$

**Answer**: (a) $\dfrac{5\pi}{6}$ radians (b) $150^\circ$

---

**Example 2 (Given radius and angle, find arc length and sector area)**: A sector has radius $12$ cm and central angle $\frac{2\pi}{3}$ radians. Find:
(a) the arc length
(b) the sector area

**Solution**:

(a) Using $s = r\theta$:

$$
s = 12 \times \frac{2\pi}{3} = 8\pi \text{ cm}
$$

(b) Using $A = \frac{1}{2}r^2\theta$:

$$
A = \frac{1}{2} \times 12^2 \times \frac{2\pi}{3} = \frac{1}{2} \times 144 \times \frac{2\pi}{3} = 72 \times \frac{2\pi}{3} = 48\pi \text{ cm}^2
$$

**Answer**: (a) $8\pi$ cm (b) $48\pi$ cm²

---

**Example 3 (Given arc length, find angle and sector area)**: A sector has radius $10$ cm and arc length $25$ cm. Find:
(a) the central angle (radians)
(b) the sector area

**Solution**:

(a) From $s = r\theta$, solving for $\theta$:

$$
\theta = \frac{s}{r} = \frac{25}{10} = 2.5 \text{ radians}
$$

(b) Using $A = \frac{1}{2}r^2\theta$:

$$
A = \frac{1}{2} \times 10^2 \times 2.5 = \frac{1}{2} \times 100 \times 2.5 = 125 \text{ cm}^2
$$

**Answer**: (a) $2.5$ radians (b) $125$ cm²

---

**Example 4 (Given sector area, find angle and arc length)**: A sector of radius $6$ cm has area $15\pi$ cm². Find:
(a) the central angle (radians)
(b) the arc length

**Solution**:

(a) From $A = \frac{1}{2}r^2\theta$, solving for $\theta$:

$$
15\pi = \frac{1}{2} \times 6^2 \times \theta = \frac{1}{2} \times 36 \times \theta = 18\theta
$$

$$
\theta = \frac{15\pi}{18} = \frac{5\pi}{6} \text{ radians}
$$

(b) Using $s = r\theta$:

$$
s = 6 \times \frac{5\pi}{6} = 5\pi \text{ cm}
$$

**Answer**: (a) $\dfrac{5\pi}{6}$ radians (b) $5\pi$ cm

---

**Example 5 (Segment area)**: In a circle of radius $8$ cm, a sector with central angle $\frac{\pi}{4}$ has its triangular portion removed. Find the area of the remaining segment.

**Solution**:

**Step 1**: Compute the sector area.

$$
A_{\text{sector}} = \frac{1}{2}r^2\theta = \frac{1}{2} \times 8^2 \times \frac{\pi}{4} = \frac{1}{2} \times 64 \times \frac{\pi}{4} = 8\pi \text{ cm}^2
$$

**Step 2**: Compute the triangle area (two sides are the radii $8$ cm, included angle $\frac{\pi}{4}$).

$$
A_{\triangle} = \frac{1}{2}r^2\sin\theta = \frac{1}{2} \times 8^2 \times \sin\frac{\pi}{4} = \frac{1}{2} \times 64 \times \frac{\sqrt{2}}{2} = 16\sqrt{2} \text{ cm}^2
$$

**Step 3**: Segment area $=$ Sector area $-$ Triangle area.

$$
A_{\text{segment}} = 8\pi - 16\sqrt{2} \text{ cm}^2
$$

**Answer**: $8\pi - 16\sqrt{2}$ cm²

---

**Example 6 (Composite figure — two sectors)**: The figure consists of a large sector of radius $5$ cm (central angle $\frac{\pi}{3}$) and a small sector of radius $3$ cm (same central angle), forming an "annular sector." Find the area of the shaded region (the region between the two sectors).

**Solution**:

**Idea**: Shaded area $=$ Large sector area $-$ Small sector area.

**Step 1**: Large sector area.

$$
A_{\text{large}} = \frac{1}{2} \times 5^2 \times \frac{\pi}{3} = \frac{1}{2} \times 25 \times \frac{\pi}{3} = \frac{25\pi}{6} \text{ cm}^2
$$

**Step 2**: Small sector area.

$$
A_{\text{small}} = \frac{1}{2} \times 3^2 \times \frac{\pi}{3} = \frac{1}{2} \times 9 \times \frac{\pi}{3} = \frac{3\pi}{2} \text{ cm}^2
$$

**Step 3**: Shaded area.

$$
A = A_{\text{large}} - A_{\text{small}} = \frac{25\pi}{6} - \frac{3\pi}{2} = \frac{25\pi}{6} - \frac{9\pi}{6} = \frac{16\pi}{6} = \frac{8\pi}{3} \text{ cm}^2
$$

**Answer**: $\dfrac{8\pi}{3}$ cm²

---

**Example 7 (Composite figure — sector and triangle)**: A sector has radius $10$ cm and central angle $60^\circ$. Inside the sector, the largest possible isosceles triangle is drawn, with two sides being the radii and the base being the chord. Find the area remaining after removing the triangle from the sector.

**Solution**:

**Step 1**: Convert $60^\circ$ to radians.

$$
\theta = 60^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{3}
$$

**Step 2**: Sector area.

$$
A_{\text{sector}} = \frac{1}{2} \times 10^2 \times \frac{\pi}{3} = 50 \times \frac{\pi}{3} = \frac{50\pi}{3} \text{ cm}^2
$$

**Step 3**: Triangle area. The isosceles triangle has vertex angle $\frac{\pi}{3}$ and equal sides $10$ cm.

$$
A_{\triangle} = \frac{1}{2} \times 10 \times 10 \times \sin\frac{\pi}{3} = 50 \times \frac{\sqrt{3}}{2} = 25\sqrt{3} \text{ cm}^2
$$

**Step 4**: Remaining area.

$$
A = \frac{50\pi}{3} - 25\sqrt{3} \text{ cm}^2
$$

**Answer**: $\dfrac{50\pi}{3} - 25\sqrt{3}$ cm²

---

> ⚠️ **Common errors**:
> 1. $\theta$ in the arc length and sector area formulas **must be in radians**, not degrees
> 2. In the segment area formula $\theta - \sin\theta$, both occurrences of $\theta$ are in radians
> 3. When encountering mixed units of degrees and radians, unify the units first before calculating

---

## 8.2 The Six Trigonometric Functions (Any Angle)

### 8.2.1 From Acute-Angle Ratios to Trigonometric Functions of Any Angle

In a right-angled triangle, for an acute angle $\theta$, our initial definitions are:

$$
\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}, \quad
\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}, \quad
\tan\theta = \frac{\text{opposite}}{\text{adjacent}}
$$

But this definition has a serious limitation — it only applies to angles $0^\circ < \theta < 90^\circ$. If the angle is greater than $90^\circ$ or negative, a right-angled triangle cannot be directly used.

**The breakthrough**: We place angles in a **coordinate system** and use the **unit circle** to redefine trigonometric functions, thereby extending the domain to all real numbers.

### 8.2.2 The Unit Circle Definition

A **unit circle** is a circle with centre at the origin and radius $1$, with equation:

$$
x^2 + y^2 = 1
$$

For any angle $\theta$, we position it as follows:
- The vertex of the angle is at the origin
- The initial side is along the positive $x$-axis
- The terminal side is obtained by rotating the initial side anticlockwise by $\theta$ (clockwise if $\theta$ is negative)

Let the terminal side intersect the unit circle at point $P(x, y)$. Then we define:

$$
\boxed{\sin\theta = y}, \qquad \boxed{\cos\theta = x}, \qquad \boxed{\tan\theta = \frac{y}{x} \;(x \neq 0)}
$$

**Why is this definition reasonable?**

When $\theta$ is an acute angle, the point $P$ on the unit circle forms a right-angled triangle — dropping a perpendicular from $P$ to the $x$-axis gives a triangle with opposite side $y$, adjacent side $x$, and hypotenuse $1$. Therefore $\sin\theta = y/1 = y$, $\cos\theta = x/1 = x$, which is entirely consistent with the right-angled triangle definition.

And when $\theta$ is any angle, the coordinates $x$ and $y$ can be positive, zero, or negative — the signs of the trigonometric functions change accordingly. This is exactly what we want!

### 8.2.3 Complete Definition of the Six Trigonometric Functions

Starting from $\sin\theta$ and $\cos\theta$, we can define four more functions:

**Tangent**:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{y}{x}, \quad \cos\theta \neq 0
$$

**Cosecant** (reciprocal of $\sin$):

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{y}, \quad \sin\theta \neq 0
$$

**Secant** (reciprocal of $\cos$):

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{x}, \quad \cos\theta \neq 0
$$

**Cotangent** (reciprocal of $\tan$):

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta} = \frac{x}{y}, \quad \sin\theta \neq 0
$$

**Summary table of the six functions**:

| Function | Notation | Unit Circle Definition | Domain Restriction |
|------|------|-----------|-----------|
| Sine | $\sin\theta$ | $y$ | All real numbers |
| Cosine | $\cos\theta$ | $x$ | All real numbers |
| Tangent | $\tan\theta$ | $y/x$ | $x \neq 0$, i.e., $\theta \neq \frac{\pi}{2} + n\pi$ |
| Cosecant | $\csc\theta$ | $1/y$ | $y \neq 0$, i.e., $\theta \neq n\pi$ |
| Secant | $\sec\theta$ | $1/x$ | $x \neq 0$, i.e., $\theta \neq \frac{\pi}{2} + n\pi$ |
| Cotangent | $\cot\theta$ | $x/y$ | $y \neq 0$, i.e., $\theta \neq n\pi$ |

### 8.2.4 Derivation of Exact Values for Special Angles

**Special triangle method**:

**(a) Derivation for $45^\circ$ ($\frac{\pi}{4}$)**

Consider an isosceles right-angled triangle with both legs equal to $1$. The hypotenuse is $\sqrt{2}$.

$$
\sin\frac{\pi}{4} = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

$$
\cos\frac{\pi}{4} = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

$$
\tan\frac{\pi}{4} = \frac{\text{opposite}}{\text{adjacent}} = \frac{1}{1} = 1
$$

**(b) Derivation for $30^\circ$ ($\frac{\pi}{6}$) and $60^\circ$ ($\frac{\pi}{3}$)**

Consider a $30^\circ$-$60^\circ$-$90^\circ$ triangle with side ratio $1 : \sqrt{3} : 2$ (the side opposite $30^\circ$ is $1$, opposite $60^\circ$ is $\sqrt{3}$, hypotenuse is $2$).

For $30^\circ$:

$$
\sin\frac{\pi}{6} = \frac{1}{2}, \quad
\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}, \quad
\tan\frac{\pi}{6} = \frac{1}{\sqrt{3}}
$$

For $60^\circ$:

$$
\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}, \quad
\cos\frac{\pi}{3} = \frac{1}{2}, \quad
\tan\frac{\pi}{3} = \sqrt{3}
$$

**(c) Derivation for $0^\circ$ and $90^\circ$**

On the unit circle, when $\theta = 0$, the terminal side coincides with the positive $x$-axis, intersecting at $(1, 0)$. So $\sin 0 = 0$, $\cos 0 = 1$, $\tan 0 = 0/1 = 0$.

When $\theta = \frac{\pi}{2}$, the terminal side coincides with the positive $y$-axis, intersecting at $(0, 1)$. So $\sin\frac{\pi}{2} = 1$, $\cos\frac{\pi}{2} = 0$, $\tan\frac{\pi}{2}$ is undefined (denominator zero).

**Complete special angle values table**:

| $\theta$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ |
|----------|-----|-----------------|-----------------|-----------------|-----------------|-------|-------------------|
| $\sin\theta$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ |
| $\cos\theta$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | undefined | $0$ | undefined |

### 8.2.5 Sign Rules — ASTC

The signs of trigonometric functions in the four quadrants are determined by the signs of the $x$ and $y$ coordinates on the unit circle.

| Quadrant | Angle range | $x = \cos\theta$ | $y = \sin\theta$ | $\tan\theta = y/x$ | Positive functions |
|------|---------|-----------------|-----------------|-------------------|---------|
| I | $0 < \theta < \dfrac{\pi}{2}$ | $+$ | $+$ | $+$ | **A**ll (all six) |
| II | $\dfrac{\pi}{2} < \theta < \pi$ | $-$ | $+$ | $-$ | **S**in (and csc) |
| III | $\pi < \theta < \dfrac{3\pi}{2}$ | $-$ | $-$ | $+$ | **T**an (and cot) |
| IV | $\dfrac{3\pi}{2} < \theta < 2\pi$ | $+$ | $-$ | $-$ | **C**os (and sec) |

**Memory aid**: Going anticlockwise from Quadrant I — ASTC, "All Students Take Calculus."

Complete sign table for all six functions:

| Quadrant | $\sin$ | $\cos$ | $\tan$ | $\sec$ | $\csc$ | $\cot$ |
|------|--------|--------|--------|--------|--------|--------|
| I | $+$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| II | $+$ | $-$ | $-$ | $-$ | $+$ | $-$ |
| III | $-$ | $-$ | $+$ | $-$ | $-$ | $+$ |
| IV | $-$ | $+$ | $-$ | $+$ | $-$ | $-$ |

### 8.2.6 Reference Angle Method

A **reference angle** is the smallest acute angle between the terminal side of a given angle and the $x$-axis, usually denoted by $\alpha$, with $0 \leq \alpha \leq \frac{\pi}{2}$.

For any angle $\theta$ (taken in $[0, 2\pi)$), the reference angle $\alpha$ is:

| $\theta$ quadrant | Reference angle $\alpha$ |
|-----------------|---------------|
| I | $\alpha = \theta$ |
| II | $\alpha = \pi - \theta$ |
| III | $\alpha = \theta - \pi$ |
| IV | $\alpha = 2\pi - \theta$ |

> **Core property**: The trigonometric function value of any angle equals the absolute value of the function at its reference angle, with the sign determined by the quadrant. i.e.:
> $$
> \sin\theta = \pm\sin\alpha,\quad \cos\theta = \pm\cos\alpha,\quad \tan\theta = \pm\tan\alpha
> $$
> The sign is determined by the quadrant in which $\theta$ lies.

### 8.2.7 Worked Examples

---

**Example 1 (Given $\sin$, find other functions — acute angle case)**: Given $\sin\theta = \frac{4}{5}$ and $0 < \theta < \frac{\pi}{2}$, find $\cos\theta$, $\tan\theta$, $\sec\theta$, $\csc\theta$, $\cot\theta$.

**Solution**:

**Step 1**: Use $\sin^2\theta + \cos^2\theta = 1$ to find $\cos^2\theta$.

$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{4}{5}\right)^2 = 1 - \frac{16}{25} = \frac{9}{25}
$$

**Step 2**: Determine the sign of $\cos\theta$. $\theta$ is in Quadrant I, $\cos\theta > 0$, so:

$$
\cos\theta = \sqrt{\frac{9}{25}} = \frac{3}{5}
$$

**Step 3**: Find the other functions in order.

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{4/5}{3/5} = \frac{4}{3}
$$

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{3/5} = \frac{5}{3}
$$

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{4/5} = \frac{5}{4}
$$

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{1}{4/3} = \frac{3}{4}
$$

**Answer**: $\cos\theta = \frac{3}{5}$, $\tan\theta = \frac{4}{3}$, $\sec\theta = \frac{5}{3}$, $\csc\theta = \frac{5}{4}$, $\cot\theta = \frac{3}{4}$

---

**Example 2 (Given $\sin$, find other functions — general angle case)**: Given $\sin\theta = \frac{3}{5}$ and $\theta$ is in Quadrant II, find $\cos\theta$, $\tan\theta$, $\sec\theta$, $\csc\theta$, $\cot\theta$.

**Solution**:

**Step 1**: Use $\sin^2\theta + \cos^2\theta = 1$ to find $\cos^2\theta$.

$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}
$$

**Step 2**: Determine the sign of $\cos\theta$. $\theta$ is in Quadrant II, $\cos\theta < 0$, so:

$$
\cos\theta = -\sqrt{\frac{16}{25}} = -\frac{4}{5}
$$

**Step 3**: Find the other functions in order.

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{3/5}{-4/5} = -\frac{3}{4}
$$

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{-4/5} = -\frac{5}{4}
$$

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{3/5} = \frac{5}{3}
$$

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{1}{-3/4} = -\frac{4}{3}
$$

**Answer**: $\cos\theta = -\frac{4}{5}$, $\tan\theta = -\frac{3}{4}$, $\sec\theta = -\frac{5}{4}$, $\csc\theta = \frac{5}{3}$, $\cot\theta = -\frac{4}{3}$

> **Comparison**: Compared to Example 1, when $\theta$ changed from Quadrant I to Quadrant II, the signs of $\cos$ and $\tan$ changed (from positive to negative), but the absolute values are the same. This demonstrates the reference angle method.

---

**Example 3 (Using reference angle to find trig values of any angle)**: Find the exact values of $\sin\frac{5\pi}{6}$, $\cos\frac{5\pi}{6}$, $\tan\frac{5\pi}{6}$.

**Solution**:

**Step 1**: Determine the quadrant of $\theta = \frac{5\pi}{6}$.

$\frac{5\pi}{6}$ corresponds to $150^\circ$, in Quadrant II (between $\frac{\pi}{2}$ and $\pi$).

**Step 2**: Find the reference angle.

For Quadrant II, $\alpha = \pi - \theta = \pi - \frac{5\pi}{6} = \frac{\pi}{6}$.

**Step 3**: Determine the sign of each function.

In Quadrant II, $\sin$ is positive, $\cos$ is negative, $\tan$ is negative.

**Step 4**: Write the answers.

$$
\sin\frac{5\pi}{6} = +\sin\frac{\pi}{6} = \frac{1}{2}
$$

$$
\cos\frac{5\pi}{6} = -\cos\frac{\pi}{6} = -\frac{\sqrt{3}}{2}
$$

$$
\tan\frac{5\pi}{6} = -\tan\frac{\pi}{6} = -\frac{1}{\sqrt{3}}
$$

---

**Example 4 (Reference angle method — Quadrant IV)**: Find the exact values of $\sin\frac{7\pi}{4}$, $\cos\frac{7\pi}{4}$, $\tan\frac{7\pi}{4}$.

**Solution**:

**Step 1**: Determine the quadrant. $\frac{7\pi}{4}$ corresponds to $315^\circ$, in Quadrant IV.

**Step 2**: Find the reference angle. For Quadrant IV, $\alpha = 2\pi - \theta = 2\pi - \frac{7\pi}{4} = \frac{\pi}{4}$.

**Step 3**: Determine the signs. In Quadrant IV, $\sin$ is negative, $\cos$ is positive, $\tan$ is negative.

**Step 4**: Write the answers.

$$
\sin\frac{7\pi}{4} = -\sin\frac{\pi}{4} = -\frac{\sqrt{2}}{2}
$$

$$
\cos\frac{7\pi}{4} = +\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$

$$
\tan\frac{7\pi}{4} = -\tan\frac{\pi}{4} = -1
$$

---

**Example 5 (Given $\tan$, find other functions)**: Given $\tan\theta = 2$ and $\pi < \theta < \frac{3\pi}{2}$, find $\sin\theta$ and $\cos\theta$.

**Solution**:

**Step 1**: Determine that $\theta$ is in Quadrant III ($\pi$ to $\frac{3\pi}{2}$). In Quadrant III, both $\sin$ and $\cos$ are negative.

**Step 2**: From $\tan\theta = \frac{\sin\theta}{\cos\theta} = 2$, we have $\sin\theta = 2\cos\theta$.

**Step 3**: Substitute into $\sin^2\theta + \cos^2\theta = 1$.

$$
(2\cos\theta)^2 + \cos^2\theta = 1
$$

$$
4\cos^2\theta + \cos^2\theta = 1
$$

$$
5\cos^2\theta = 1
$$

$$
\cos^2\theta = \frac{1}{5}
$$

**Step 4**: Determine the sign. $\theta$ is in Quadrant III, $\cos\theta < 0$, so:

$$
\cos\theta = -\sqrt{\frac{1}{5}} = -\frac{1}{\sqrt{5}}
$$

**Step 5**: Find $\sin\theta$.

$$
\sin\theta = 2\cos\theta = 2 \times \left(-\frac{1}{\sqrt{5}}\right) = -\frac{2}{\sqrt{5}}
$$

**Answer**: $\sin\theta = -\dfrac{2}{\sqrt{5}}$, $\cos\theta = -\dfrac{1}{\sqrt{5}}$

---

**Example 6 (Given $\sec$, find other functions)**: Given $\sec\theta = 3$ and $\frac{3\pi}{2} < \theta < 2\pi$, find $\sin\theta$, $\cos\theta$, $\tan\theta$.

**Solution**:

**Step 1**: From $\sec\theta = \frac{1}{\cos\theta} = 3$, we get $\cos\theta = \frac{1}{3}$. $\theta$ is in Quadrant IV, $\cos\theta > 0$, consistent.

**Step 2**: From $\sin^2\theta + \cos^2\theta = 1$:

$$
\sin^2\theta = 1 - \cos^2\theta = 1 - \frac{1}{9} = \frac{8}{9}
$$

**Step 3**: Determine the sign. $\theta$ is in Quadrant IV, $\sin\theta < 0$, so:

$$
\sin\theta = -\sqrt{\frac{8}{9}} = -\frac{2\sqrt{2}}{3}
$$

**Step 4**: Find $\tan\theta$.

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-2\sqrt{2}/3}{1/3} = -2\sqrt{2}
$$

**Answer**: $\sin\theta = -\dfrac{2\sqrt{2}}{3}$, $\cos\theta = \dfrac{1}{3}$, $\tan\theta = -2\sqrt{2}$

---

## 8.3 Graphs of Trigonometric Functions (Amplitude, Period, Asymptotes)

### 8.3.1 Graphs of Basic Trigonometric Functions

#### $y = \sin x$

Key points on $[0, 2\pi]$:

| $x$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-------|-------------------|--------|
| $\sin x$ | $0$ | $1$ | $0$ | $-1$ | $0$ |

**Properties summary**:

- **Domain**: $\mathbb{R}$ (all real numbers)
- **Range**: $[-1, 1]$
- **Periodicity**: period $2\pi$, i.e., $\sin(x + 2\pi) = \sin x$
- **Parity**: odd function, $\sin(-x) = -\sin x$, symmetric about the origin
- **Zeros**: $x = n\pi$ ($n \in \mathbb{Z}$)
- **Maximum**: $1$ at $x = \frac{\pi}{2} + 2n\pi$
- **Minimum**: $-1$ at $x = \frac{3\pi}{2} + 2n\pi$

Graph shape: Starts at $0$, rises to $1$, falls through $0$ to $-1$, returns to $0$, oscillating like a wave.

#### $y = \cos x$

Key points:

| $x$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-------|-------------------|--------|
| $\cos x$ | $1$ | $0$ | $-1$ | $0$ | $1$ |

**Properties summary**:

- **Domain**: $\mathbb{R}$
- **Range**: $[-1, 1]$
- **Periodicity**: period $2\pi$
- **Parity**: even function, $\cos(-x) = \cos x$, symmetric about the $y$-axis
- **Zeros**: $x = \frac{\pi}{2} + n\pi$
- **Maximum**: $1$ at $x = 2n\pi$
- **Minimum**: $-1$ at $x = \pi + 2n\pi$

**Relationship between sine and cosine**:

$$
\cos x = \sin\left(x + \frac{\pi}{2}\right), \qquad
\sin x = \cos\left(x - \frac{\pi}{2}\right)
$$

That is, the cosine curve is the sine curve shifted left by $\frac{\pi}{2}$.

#### $y = \tan x$

Key points and asymptotes:

| $x$ | $-\dfrac{\pi}{2}$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ |
|-----|-------------------|-----|-----------------|-------|-------------------|
| $\tan x$ | undefined | $0$ | undefined | $0$ | undefined |

**Properties summary**:

- **Domain**: $x \neq \frac{\pi}{2} + n\pi$ (at these points $\cos x = 0$, tangent is undefined)
- **Range**: $\mathbb{R}$ (all real numbers)
- **Periodicity**: period $\pi$, i.e., $\tan(x + \pi) = \tan x$
- **Parity**: odd function, $\tan(-x) = -\tan x$, symmetric about the origin
- **Zeros**: $x = n\pi$
- **Asymptotes**: $x = \frac{\pi}{2} + n\pi$ (vertical asymptotes)

Graph shape: In each period $(-\frac{\pi}{2}, \frac{\pi}{2})$, the function rises from $-\infty$, passes through $0$, to $+\infty$.

#### $y = \sec x$, $y = \csc x$, $y = \cot x$ — Summary

- $y = \sec x = \frac{1}{\cos x}$: vertical asymptotes where $\cos x = 0$ ($x = \frac{\pi}{2} + n\pi$), range $(-\infty, -1] \cup [1, \infty)$, period $2\pi$, even function
- $y = \csc x = \frac{1}{\sin x}$: vertical asymptotes where $\sin x = 0$ ($x = n\pi$), range $(-\infty, -1] \cup [1, \infty)$, period $2\pi$, odd function
- $y = \cot x = \frac{\cos x}{\sin x}$: vertical asymptotes where $\sin x = 0$ ($x = n\pi$), range $\mathbb{R}$, period $\pi$, odd function

### 8.3.2 Transformations of Trigonometric Functions

Consider the general form $y = a\sin(bx + c) + d$ (also applicable to $\cos$ and $\tan$, though $\tan$ has no concept of amplitude).

#### Amplitude

The parameter $a$ controls vertical stretching or compression. For sine and cosine, $|a|$ is the maximum distance the wave deviates from the centre line.

**Derivation**: $\sin x$ has range $[-1, 1]$. Multiplying by $a$ changes the range to $[-|a|, |a|]$ (if $a > 0$) or $[|a|, -|a|]$ (if $a < 0$). Therefore the amplitude is $|a|$.

**Example**: $y = 3\sin x$ has amplitude $3$, maximum $3$, minimum $-3$.

#### Period

The parameter $b$ controls horizontal stretching or compression.

**Derivation**: $\sin x$ has period $2\pi$, i.e., $\sin(x + 2\pi) = \sin x$. For $y = \sin(bx)$, we want the smallest positive $T$ such that $\sin(b(x + T)) = \sin(bx)$. Since $\sin$ has period $2\pi$, we need $bT = 2\pi$, giving:

$$
T = \frac{2\pi}{|b|}
$$

For $\tan(bx)$, since $\tan x$ has period $\pi$:

$$
T = \frac{\pi}{|b|}
$$

**Example**: $y = \sin(2x)$ has period $T = \frac{2\pi}{2} = \pi$. $y = \tan\left(\frac{x}{2}\right)$ has period $T = \frac{\pi}{1/2} = 2\pi$.

#### Phase Shift

The parameter $c$ causes horizontal translation.

**Derivation**:

$$
y = \sin(bx + c) = \sin\left[b\left(x + \frac{c}{b}\right)\right]
$$

This is equivalent to shifting the graph of $y = \sin(bx)$ left by $\frac{c}{b}$ units. If $\frac{c}{b} > 0$, shift left; if $\frac{c}{b} < 0$, shift right. The **phase shift** is usually defined as $-\frac{c}{b}$ (a positive value means a rightward shift).

#### Vertical Shift

The parameter $d$ shifts the entire graph up ($d > 0$) or down ($d < 0$) by $|d|$ units. $d$ is also the $y$-coordinate of the new centre line (midline).

**Summary formulas** for $y = a\sin(bx + c) + d$:

| Parameter | Name | Formula |
|------|------|---------|
| $|a|$ | Amplitude | Max $= d + |a|$, Min $= d - |a|$ |
| $T = \dfrac{2\pi}{|b|}$ | Period | For $\tan$: $\dfrac{\pi}{|b|}$ |
| $-\dfrac{c}{b}$ | Phase shift | $>0$ shift right, $<0$ shift left |
| $d$ | Vertical shift | New midline is $y = d$ |

### 8.3.3 Method for Sketching Graphs

**Steps for sketching $y = a\sin(bx + c) + d$**:

1. Determine the amplitude $|a|$, period $T = \frac{2\pi}{|b|}$, phase shift $-\frac{c}{b}$, and vertical shift $d$
2. Find the key points in one complete period (usually 5 points: start, peak, midpoint, trough, end)
3. Mark the midline $y = d$, and the maximum $d + |a|$ and minimum $d - |a|$
4. Starting from the shifted start point, mark a key point every $T/4$
5. Connect the points with a smooth wave

### 8.3.4 Worked Examples

---

**Example 1 (Determining transformation parameters)**: For the function $y = 4\cos\left(3x + \frac{\pi}{2}\right) - 2$, find the amplitude, period, phase shift, and vertical shift, and state its maximum and minimum values.

**Solution**:

Comparing with the standard form $y = a\cos(bx + c) + d$:

$$
a = 4,\quad b = 3,\quad c = \frac{\pi}{2},\quad d = -2
$$

**Amplitude**: $|a| = |4| = 4$

**Period**: $T = \frac{2\pi}{|b|} = \frac{2\pi}{3}$

**Phase shift**: $-\frac{c}{b} = -\frac{\pi/2}{3} = -\frac{\pi}{6}$ (negative means shift left by $\frac{\pi}{6}$)

**Vertical shift**: $d = -2$ (shift down $2$ units)

**Maximum**: $d + |a| = -2 + 4 = 2$

**Minimum**: $d - |a| = -2 - 4 = -6$

---

**Example 2 (Finding function expression from graph features — revised version)**: A sine-type function satisfies: amplitude $2$, period $\pi$, at $x = 0$ the function value is $1$ (on the midline) and is rising. The vertical shift makes the midline $y = 1$. Write one possible expression for the function.

**Solution**:

**Step 1**: Let the function be $y = a\sin(bx + c) + d$.

**Step 2**: From amplitude $2$, $|a| = 2$, take $a = 2$.

**Step 3**: From period $T = \pi$: $T = \frac{2\pi}{|b|} = \pi$, so $|b| = 2$, take $b = 2$.

**Step 4**: From midline $y = 1$, $d = 1$.

**Step 5**: At $x = 0$, $y = 1$ (on the midline) and rising — this means the sine's argument is $0$ (since $\sin 0 = 0$ and near $0$ it rises):

$$
2\sin(2 \times 0 + c) + 1 = 1 \Rightarrow 2\sin c + 1 = 1 \Rightarrow \sin c = 0
$$

$\sin c = 0$ gives $c = n\pi$. When $c = 0$, $y = 2\sin(2x) + 1$. At $x = 0$:
- $y = 1$ (midline) ✓
- Derivative $y' = 4\cos(2x)$, at $x = 0$, $y' = 4 > 0$, rising ✓

**Answer**: $y = 2\sin(2x) + 1$

---

**Example 3 (Asymptotes of tangent functions)**: Find the period and the equations of the asymptotes within one period of $y = 3\tan\left(2x - \frac{\pi}{3}\right) + 1$.

**Solution**:

**Step 1**: Find the period. For $\tan$, $T = \frac{\pi}{|b|} = \frac{\pi}{2}$.

**Step 2**: Find the asymptotes. $\tan(u)$ has asymptotes at $u = \frac{\pi}{2} + n\pi$.

Set $2x - \frac{\pi}{3} = \frac{\pi}{2} + n\pi$:

$$
2x = \frac{\pi}{2} + \frac{\pi}{3} + n\pi = \frac{3\pi}{6} + \frac{2\pi}{6} + n\pi = \frac{5\pi}{6} + n\pi
$$

$$
x = \frac{5\pi}{12} + \frac{n\pi}{2}
$$

**Step 3**: Taking $n = 0$ and $n = 1$ (covering two asymptotes in one period $\frac{\pi}{2}$):

$$
x = \frac{5\pi}{12},\quad x = \frac{5\pi}{12} + \frac{\pi}{2} = \frac{5\pi}{12} + \frac{6\pi}{12} = \frac{11\pi}{12}
$$

**Answer**: Period is $\dfrac{\pi}{2}$, asymptotes are $x = \dfrac{5\pi}{12} + \dfrac{n\pi}{2}$ ($n \in \mathbb{Z}$)

---

**Example 4 (Graph transformation — from $y = \sin x$ to $y = 2\sin(3x) + 1$)**: Describe how to obtain the graph of $y = 2\sin(3x) + 1$ from $y = \sin x$.

**Solution**:

**Step 1**: Horizontal compression. $y = \sin x \to y = \sin(3x)$: the period is compressed from $2\pi$ to $\frac{2\pi}{3}$, the frequency becomes $3$ times the original.

**Step 2**: Vertical stretch. $y = \sin(3x) \to y = 2\sin(3x)$: amplitude changes from $1$ to $2$, maximum from $1$ to $2$, minimum from $-1$ to $-2$.

**Step 3**: Vertical shift. $y = 2\sin(3x) \to y = 2\sin(3x) + 1$: the entire graph shifts up by $1$ unit, new midline is $y = 1$.

**Order of transformations**: First horizontal (period), then vertical (amplitude), finally vertical shift.

---

**Example 5 (Finding function from graph — given points)**: A cosine-type function $y = a\cos(bx) + d$ passes through $(0, 5)$ and $(\pi, -1)$, and has period $2\pi$. Find $a$, $b$, $d$.

**Solution**:

**Step 1**: From period $T = 2\pi$: $T = \frac{2\pi}{|b|} = 2\pi$, so $|b| = 1$, take $b = 1$.

**Step 2**: Substitute $(0, 5)$: $y = a\cos(0) + d = a + d = 5$

**Step 3**: Substitute $(\pi, -1)$: $y = a\cos(\pi) + d = -a + d = -1$

**Step 4**: Solve the system:

$$
\begin{cases}
a + d = 5 \\
-a + d = -1
\end{cases}
$$

Adding: $2d = 4 \Rightarrow d = 2$
Substituting into the first equation: $a + 2 = 5 \Rightarrow a = 3$

**Answer**: $a = 3$, $b = 1$, $d = 2$, function is $y = 3\cos x + 2$

---

## 8.4 Trigonometric Identities

### 8.4.1 Three Basic Pythagorean Identities

**Identity 1: $\sin^2\theta + \cos^2\theta = 1$**

**Derivation**: On the unit circle, the point $(\cos\theta, \sin\theta)$ lies on the circle $x^2 + y^2 = 1$. Substituting gives:

$$
(\cos\theta)^2 + (\sin\theta)^2 = 1
$$

i.e., $\sin^2\theta + \cos^2\theta = 1$.

**Identity 2: $\sec^2\theta = 1 + \tan^2\theta$**

**Derivation**: Divide both sides of $\sin^2\theta + \cos^2\theta = 1$ by $\cos^2\theta$ (assuming $\cos\theta \neq 0$):

$$
\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}
$$

$$
\tan^2\theta + 1 = \sec^2\theta
$$

i.e., $\sec^2\theta = 1 + \tan^2\theta$.

**Identity 3: $\csc^2\theta = 1 + \cot^2\theta$**

**Derivation**: Divide both sides of $\sin^2\theta + \cos^2\theta = 1$ by $\sin^2\theta$ (assuming $\sin\theta \neq 0$):

$$
\frac{\sin^2\theta}{\sin^2\theta} + \frac{\cos^2\theta}{\sin^2\theta} = \frac{1}{\sin^2\theta}
$$

$$
1 + \cot^2\theta = \csc^2\theta
$$

i.e., $\csc^2\theta = 1 + \cot^2\theta$.

> ✅ **Exam tip**: These three identities are provided on the syllabus **formula sheet** and can be directly quoted in the exam.

### 8.4.2 Double Angle Formulas

Although the syllabus does not explicitly list the double angle formulas, these can be derived from the basic identities and are very commonly used in solving equations and proving identities.

**Derivation of $\sin(2\theta)$**:

Starting from the sum formula $\sin(A + B) = \sin A\cos B + \cos A\sin B$, let $A = B = \theta$:

$$
\sin(2\theta) = \sin\theta\cos\theta + \cos\theta\sin\theta = 2\sin\theta\cos\theta
$$

Therefore:

$$
\boxed{\sin(2\theta) = 2\sin\theta\cos\theta}
$$

**Derivation of $\cos(2\theta)$**:

Starting from the sum formula $\cos(A + B) = \cos A\cos B - \sin A\sin B$, let $A = B = \theta$:

$$
\cos(2\theta) = \cos\theta\cos\theta - \sin\theta\sin\theta = \cos^2\theta - \sin^2\theta
$$

Using $\sin^2\theta + \cos^2\theta = 1$, we can obtain two other forms:

Substituting $\sin^2\theta = 1 - \cos^2\theta$:

$$
\cos(2\theta) = \cos^2\theta - (1 - \cos^2\theta) = 2\cos^2\theta - 1
$$

Substituting $\cos^2\theta = 1 - \sin^2\theta$:

$$
\cos(2\theta) = (1 - \sin^2\theta) - \sin^2\theta = 1 - 2\sin^2\theta
$$

Therefore $\cos(2\theta)$ has three equivalent forms:

$$
\boxed{\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta}
$$

**Derivation of $\tan(2\theta)$**:

Starting from the sum formula $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A\tan B}$, let $A = B = \theta$:

$$
\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}
$$

i.e.:

$$
\boxed{\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}}
$$

### 8.4.3 Half-Angle Formulas (Derived from Double Angle Formulas)

From $\cos(2\theta) = 2\cos^2\theta - 1$, solving for $\cos^2\theta$:

$$
2\cos^2\theta = 1 + \cos(2\theta) \;\Rightarrow\; \boxed{\cos^2\theta = \frac{1 + \cos(2\theta)}{2}}
$$

From $\cos(2\theta) = 1 - 2\sin^2\theta$, solving for $\sin^2\theta$:

$$
2\sin^2\theta = 1 - \cos(2\theta) \;\Rightarrow\; \boxed{\sin^2\theta = \frac{1 - \cos(2\theta)}{2}}
$$

These two formulas are very important in **integration** — they are used to reduce the power of trigonometric functions.

### 8.4.4 Worked Examples

---

**Example 1 (Using identities to find values)**: Given $\cos\theta = \frac{3}{5}$ and $\theta$ is in Quadrant IV, find $\sin\theta$, $\tan\theta$, $\sin(2\theta)$, $\cos(2\theta)$.

**Solution**:

**Step 1**: Use $\sin^2\theta + \cos^2\theta = 1$ to find $\sin^2\theta$.

$$
\sin^2\theta = 1 - \cos^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}
$$

**Step 2**: Determine the sign of $\sin\theta$. $\theta$ is in Quadrant IV, $\sin\theta < 0$.

$$
\sin\theta = -\sqrt{\frac{16}{25}} = -\frac{4}{5}
$$

**Step 3**: Find $\tan\theta$.

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-4/5}{3/5} = -\frac{4}{3}
$$

**Step 4**: Find $\sin(2\theta)$.

$$
\sin(2\theta) = 2\sin\theta\cos\theta = 2 \times \left(-\frac{4}{5}\right) \times \frac{3}{5} = -\frac{24}{25}
$$

**Step 5**: Find $\cos(2\theta)$ (using $\cos^2\theta - \sin^2\theta$ form).

$$
\cos(2\theta) = \cos^2\theta - \sin^2\theta = \left(\frac{3}{5}\right)^2 - \left(-\frac{4}{5}\right)^2 = \frac{9}{25} - \frac{16}{25} = -\frac{7}{25}
$$

**Answer**: $\sin\theta = -\dfrac{4}{5}$, $\tan\theta = -\dfrac{4}{3}$, $\sin(2\theta) = -\dfrac{24}{25}$, $\cos(2\theta) = -\dfrac{7}{25}$

---

**Example 2 (Simplifying an expression and evaluating using identities)**: Simplify $\frac{\sin(2\theta)}{1 - \cos(2\theta)}$, and use this to find its value when $\theta = \frac{\pi}{6}$.

**Solution**:

**Step 1**: Substitute the double angle formulas.

$$
\frac{\sin(2\theta)}{1 - \cos(2\theta)} = \frac{2\sin\theta\cos\theta}{1 - (1 - 2\sin^2\theta)}
$$

**Step 2**: Simplify the denominator.

$$
1 - \cos(2\theta) = 1 - (1 - 2\sin^2\theta) = 2\sin^2\theta
$$

**Step 3**: Simplify the entire expression.

$$
\frac{2\sin\theta\cos\theta}{2\sin^2\theta} = \frac{\cos\theta}{\sin\theta} = \cot\theta
$$

**Step 4**: Substitute $\theta = \frac{\pi}{6}$.

$$
\cot\frac{\pi}{6} = \frac{\cos\frac{\pi}{6}}{\sin\frac{\pi}{6}} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3}
$$

**Answer**: Simplified result is $\cot\theta$, equal to $\sqrt{3}$ when $\theta = \frac{\pi}{6}$

---

**Example 5 (Proving an identity and evaluating)**: Prove that $\sin^4\theta - \cos^4\theta = \sin^2\theta - \cos^2\theta$, and hence find its value when $\theta = \frac{\pi}{3}$.

**Solution**:

**Proof**:

LHS $= \sin^4\theta - \cos^4\theta = (\sin^2\theta)^2 - (\cos^2\theta)^2$

Using the difference of squares:

$$
= (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta)
$$

Since $\sin^2\theta + \cos^2\theta = 1$:

$$
= (\sin^2\theta - \cos^2\theta) \times 1 = \sin^2\theta - \cos^2\theta = \text{RHS}
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

**Evaluation**: Substitute $\theta = \frac{\pi}{3}$.

$$
\sin^2\frac{\pi}{3} - \cos^2\frac{\pi}{3} = \left(\frac{\sqrt{3}}{2}\right)^2 - \left(\frac{1}{2}\right)^2 = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}
$$

**Answer**: Identity proved; at $\theta = \frac{\pi}{3}$ the value is $\frac{1}{2}$

---
---

## 8.5 Solving Trigonometric Equations

### 8.5.1 Overall Solution Strategy (Review)

The core process for solving trigonometric equations is as follows:

```
Original equation
   │
   ▼
Does it contain functions of different names? ──Yes──→ Use identities to convert to the same name
   │                                                    │
   │No                                                  ▼
   ▼                                              Simplified equation
Convert to basic form: sin x = k,                    │
cos x = k, tan x = k                                 │
   │                                                  │
   ▼                                                  ▼
Find reference angle α
   │
   ▼
Determine the quadrants of the solutions based on the sign of k (for tan, directly add the period)
   │
   ▼
Write all solutions within the given interval
   │
   ▼
Check the domain, exclude invalid solutions
```

> **Core idea**: No matter how complex a trigonometric equation is, the ultimate goal is to use identities and algebraic manipulation to simplify it to one or more basic forms ($\sin x = k$, $\cos x = k$, $\tan x = k$), and then systematically find all solutions using the reference angle method.

---

### 8.5.2 Basic Form $\sin x = k$ ($-1 \leq k \leq 1$)

#### Geometric Derivation — Understanding from the Unit Circle

On the unit circle, $\sin\theta = y$ is the $y$-coordinate of the intersection point of the terminal side with the unit circle. Therefore, the equation $\sin x = k$ is equivalent to: **on the unit circle, find all angles $x$ whose terminal side intersects the horizontal line $y = k$**.

**Case 1**: When $0 < k < 1$.

The horizontal line $y = k$ intersects the unit circle at two points (symmetric about the $y$-axis):
- One in Quadrant I, corresponding to angle $\alpha$ (acute angle)
- The other in Quadrant II, corresponding to angle $\pi - \alpha$

Why is the solution in Quadrant II equal to $\pi - \alpha$?

We can understand this using the sine of supplementary angles. On the unit circle, the terminal side of angle $\pi - \alpha$ is symmetric to the terminal side of $\alpha$ about the $y$-axis. Therefore their $y$-coordinates are the same:

$$
\sin(\pi - \alpha) = \sin\alpha
$$

When $\sin\alpha = |k|$, $\sin(\pi - \alpha) = |k|$. Since $k > 0$, $\sin(\pi - \alpha) = k$.

**Case 2**: When $-1 < k < 0$.

The horizontal line $y = k$ is below the $x$-axis. It also intersects the unit circle at two points:
- One in Quadrant III, corresponding to angle $\pi + \alpha$
- The other in Quadrant IV, corresponding to angle $2\pi - \alpha$

**Derivation of $\pi + \alpha$**: The terminal side of $\pi + \alpha$ is symmetric to that of $\alpha$ about the origin. Therefore:

$$
\sin(\pi + \alpha) = -\sin\alpha = -|k|
$$

Since $k < 0$, $-|k| = k$, so $\sin(\pi + \alpha) = k$.

**Derivation of $2\pi - \alpha$**: The terminal side of $2\pi - \alpha$ is symmetric to that of $\alpha$ about the $x$-axis:

$$
\sin(2\pi - \alpha) = -\sin\alpha = -|k| = k
$$

#### Complete Solution Steps

**Step 1**: Check feasibility. Verify $|k| \leq 1$. If $|k| > 1$, the equation has no solution (since the range of $\sin$ is $[-1, 1]$).

**Step 2**: Find the reference angle.

$$
\alpha = \arcsin(|k|), \quad \alpha \in \left[0, \frac{\pi}{2}\right]
$$

The reference angle $\alpha$ is an acute (or boundary) angle between $0$ and $\frac{\pi}{2}$, representing the smallest angle between the terminal side and the $x$-axis.

**Step 3**: Determine the quadrants of the solutions based on the sign of $k$.

| Sign of $k$ | Quadrants of solutions | Corresponding angles |
|-----------|---------------------|---------|
| $k > 0$ | Quadrants I, II | $x = \alpha$, $x = \pi - \alpha$ |
| $k = 0$ | Positive and negative $x$-axis | $x = 0$, $x = \pi$ (within $[0, 2\pi)$) |
| $k < 0$ | Quadrants III, IV | $x = \pi + \alpha$, $x = 2\pi - \alpha$ |

**Step 4**: Write the general solution. Since the period of $\sin$ is $2\pi$, all solutions can be expressed as:

$$
x = x_0 + 2n\pi, \quad n \in \mathbb{Z}
$$

where $x_0$ are the basic solutions found in Step 3.

#### Special Cases

**(a) $k = 0$**: Solutions of $\sin x = 0$.

Within $[0, 2\pi)$, $\sin x = 0$ occurs at $x = 0$ and $x = \pi$. General solution:

$$
x = n\pi, \quad n \in \mathbb{Z}
$$

**(b) $k = 1$**: Solutions of $\sin x = 1$.

Within $[0, 2\pi)$, $\sin x = 1$ only at $x = \frac{\pi}{2}$. General solution:

$$
x = \frac{\pi}{2} + 2n\pi, \quad n \in \mathbb{Z}
$$

**(c) $k = -1$**: Solutions of $\sin x = -1$.

Within $[0, 2\pi)$, $\sin x = -1$ only at $x = \frac{3\pi}{2}$. General solution:

$$
x = \frac{3\pi}{2} + 2n\pi, \quad n \in \mathbb{Z}
$$

#### Worked Examples

---

**Example 1 ($\sin x = k$, $k > 0$ standard case)**: Solve $\sin x = \frac{\sqrt{3}}{2}$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: Check feasibility. $\frac{\sqrt{3}}{2} \approx 0.866 \leq 1$, solvable.

**Step 2**: Find the reference angle. $\alpha = \arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$.

**Step 3**: $k = \frac{\sqrt{3}}{2} > 0$, solutions are in Quadrants I and II.

Quadrant I: $x = \alpha = \dfrac{\pi}{3}$
Quadrant II: $x = \pi - \alpha = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

**Step 4**: Verification. $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ ✓, $\sin\frac{2\pi}{3} = \sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ ✓

**Answer**: $x = \dfrac{\pi}{3}$ and $x = \dfrac{2\pi}{3}$

---

**Example 2 ($\sin x = k$, $k < 0$ standard case)**: Solve $\sin x = -\frac{1}{2}$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: Check feasibility. $\left|-\frac{1}{2}\right| = \frac{1}{2} \leq 1$, solvable.

**Step 2**: Find the reference angle. $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$.

**Step 3**: $k = -\frac{1}{2} < 0$, solutions are in Quadrants III and IV.

Quadrant III: $x = \pi + \alpha = \pi + \dfrac{\pi}{6} = \dfrac{7\pi}{6}$
Quadrant IV: $x = 2\pi - \alpha = 2\pi - \dfrac{\pi}{6} = \dfrac{11\pi}{6}$

**Step 4**: Verification. $\sin\frac{7\pi}{6} = -\sin\frac{\pi}{6} = -\frac{1}{2}$ ✓, $\sin\frac{11\pi}{6} = -\sin\frac{\pi}{6} = -\frac{1}{2}$ ✓

**Answer**: $x = \dfrac{7\pi}{6}$ and $x = \dfrac{11\pi}{6}$

---

**Example 3 ($\sin x = k$, general solution)**: Find the general solution of $\sin x = \frac{\sqrt{2}}{2}$.

**Solution**:

**Step 1**: Reference angle $\alpha = \arcsin\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4}$.

**Step 2**: $k > 0$, basic solutions:

$$
x_1 = \frac{\pi}{4}, \quad x_2 = \pi - \frac{\pi}{4} = \frac{3\pi}{4}
$$

**Step 3**: General solution by adding integer multiples of $2\pi$:

$$
x = \frac{\pi}{4} + 2n\pi \quad \text{or} \quad x = \frac{3\pi}{4} + 2n\pi, \quad n \in \mathbb{Z}
$$

**Answer**: $x = \dfrac{\pi}{4} + 2n\pi$ or $x = \dfrac{3\pi}{4} + 2n\pi$ ($n \in \mathbb{Z}$)

---

### 8.5.3 Basic Form $\cos x = k$ ($-1 \leq k \leq 1$)

#### Geometric Derivation — Understanding from the Unit Circle

On the unit circle, $\cos\theta = x$ is the $x$-coordinate of the intersection point of the terminal side with the unit circle. The equation $\cos x = k$ is equivalent to: **on the unit circle, find all angles $x$ whose terminal side intersects the vertical line $x = k$**.

**Case 1**: When $0 < k < 1$.

The vertical line $x = k$ intersects the unit circle at two points (symmetric about the $x$-axis):
- One in Quadrant I, corresponding to angle $\alpha$
- The other in Quadrant IV, corresponding to angle $2\pi - \alpha$ (or $-\alpha$)

**Derivation of $2\pi - \alpha$**: The terminal side of $2\pi - \alpha$ is symmetric to that of $\alpha$ about the $x$-axis:

$$
\cos(2\pi - \alpha) = \cos\alpha = |k|
$$

Since $\cos$ is positive in Quadrant IV, $\cos(2\pi - \alpha) = |k| = k$.

**Case 2**: When $-1 < k < 0$.

The vertical line $x = k$ (to the left of the $y$-axis) intersects the unit circle at two points:
- One in Quadrant II, corresponding to angle $\pi - \alpha$
- The other in Quadrant III, corresponding to angle $\pi + \alpha$

**Derivation of $\pi - \alpha$**: The terminal side of $\pi - \alpha$ is symmetric to that of $\alpha$ about the $y$-axis:

$$
\cos(\pi - \alpha) = -\cos\alpha = -|k|
$$

Since $k < 0$, $-|k| = k$, so $\cos(\pi - \alpha) = k$.

**Derivation of $\pi + \alpha$**: The terminal side of $\pi + \alpha$ is symmetric to that of $\alpha$ about the origin:

$$
\cos(\pi + \alpha) = -\cos\alpha = -|k| = k
$$

#### Complete Solution Steps

**Step 1**: Check feasibility. Confirm $|k| \leq 1$.

**Step 2**: Find the reference angle.

$$
\alpha = \arccos(|k|), \quad \alpha \in [0, \pi]
$$

Note: The range of $\arccos$ is $[0, \pi]$, different from $\arcsin$. So $\alpha$ is directly obtained from $\arccos(|k|)$, always within $[0, \pi]$.

**Step 3**: Determine the quadrants based on the sign of $k$.

| Sign of $k$ | Quadrants of solutions | Corresponding angles |
|-----------|---------------------|---------|
| $k > 0$ | Quadrants I, IV | $x = \alpha$, $x = 2\pi - \alpha$ |
| $k = 0$ | $y$-axis positive and negative | $x = \frac{\pi}{2}$, $x = \frac{3\pi}{2}$ (within $[0, 2\pi)$) |
| $k < 0$ | Quadrants II, III | $x = \pi - \alpha$, $x = \pi + \alpha$ |

**Step 4**: Write the general solution. Since the period of $\cos$ is $2\pi$, a concise general solution is:

$$
x = \pm\alpha + 2n\pi, \quad n \in \mathbb{Z}
$$

#### Special Cases

**(a) $k = 0$**: Solutions of $\cos x = 0$.

Within $[0, 2\pi)$, $\cos x = 0$ at $x = \frac{\pi}{2}$ and $x = \frac{3\pi}{2}$. General solution:

$$
x = \frac{\pi}{2} + n\pi, \quad n \in \mathbb{Z}
$$

**(b) $k = 1$**: Solutions of $\cos x = 1$.

Within $[0, 2\pi)$, $\cos x = 1$ only at $x = 0$. General solution:

$$
x = 2n\pi, \quad n \in \mathbb{Z}
$$

**(c) $k = -1$**: Solutions of $\cos x = -1$.

Within $[0, 2\pi)$, $\cos x = -1$ only at $x = \pi$. General solution:

$$
x = \pi + 2n\pi = (2n + 1)\pi, \quad n \in \mathbb{Z}
$$

#### Comparison of Solution Distributions for $\sin$ and $\cos$

| | $\sin x = k$ | $\cos x = k$ |
|--|-------------|-------------|
| $k > 0$ | Quadrants I, II: $\alpha$, $\pi - \alpha$ | Quadrants I, IV: $\alpha$, $2\pi - \alpha$ |
| $k < 0$ | Quadrants III, IV: $\pi + \alpha$, $2\pi - \alpha$ | Quadrants II, III: $\pi - \alpha$, $\pi + \alpha$ |
| Period | $2\pi$ | $2\pi$ |
| Concise general solution | $x = n\pi + (-1)^n\alpha$ | $x = \pm\alpha + 2n\pi$ |

> **Memory tip**: Positive solutions of $\sin$ are "up" (Quadrants I, II), positive solutions of $\cos$ are "right" (Quadrants I, IV). This "up" and "right" corresponds to the regions on the unit circle where $y$ and $x$ coordinates are positive, respectively.

---

**Example 1 ($\cos x = k$, $k > 0$ standard case)**: Solve $\cos x = \frac{\sqrt{2}}{2}$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: Check feasibility. $\frac{\sqrt{2}}{2} \leq 1$, solvable.

**Step 2**: Find reference angle. $\alpha = \arccos\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4}$.

**Step 3**: $k = \frac{\sqrt{2}}{2} > 0$, solutions are in Quadrants I and IV.

Quadrant I: $x = \alpha = \dfrac{\pi}{4}$
Quadrant IV: $x = 2\pi - \alpha = 2\pi - \dfrac{\pi}{4} = \dfrac{8\pi}{4} - \dfrac{\pi}{4} = \dfrac{7\pi}{4}$

**Step 4**: Verification. $\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ ✓, $\cos\frac{7\pi}{4} = \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ ✓

**Answer**: $x = \dfrac{\pi}{4}$ and $x = \dfrac{7\pi}{4}$

---

**Example 2 ($\cos x = k$, $k < 0$ standard case)**: Solve $\cos x = -\frac{1}{2}$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: $\left|-\frac{1}{2}\right| = \frac{1}{2} \leq 1$, solvable.

**Step 2**: Find reference angle. $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$.

**Step 3**: $k = -\frac{1}{2} < 0$, solutions are in Quadrants II and III.

Quadrant II: $x = \pi - \alpha = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$
Quadrant III: $x = \pi + \alpha = \pi + \dfrac{\pi}{3} = \dfrac{4\pi}{3}$

**Step 4**: Verification. $\cos\frac{2\pi}{3} = -\cos\frac{\pi}{3} = -\frac{1}{2}$ ✓, $\cos\frac{4\pi}{3} = -\cos\frac{\pi}{3} = -\frac{1}{2}$ ✓

**Answer**: $x = \dfrac{2\pi}{3}$ and $x = \dfrac{4\pi}{3}$

---

**Example 7 (Comparison of $\sin$ and $\cos$)**: Compare the solutions of $\sin x = \frac{\sqrt{3}}{2}$ and $\cos x = \frac{\sqrt{3}}{2}$ on $[0, 2\pi)$.

**Solution**:

$\frac{\sqrt{3}}{2} \approx 0.866$. For $\sin x = \frac{\sqrt{3}}{2}$: $\alpha = \frac{\pi}{3}$ (since $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$).
For $\cos x = \frac{\sqrt{3}}{2}$: $\alpha = \frac{\pi}{6}$ (since $\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$).

| Equation | Reference angle $\alpha$ | Solutions on $[0, 2\pi)$ |
|---------|-----------------------|--------------------------|
| $\sin x = \frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{3}$, $\frac{2\pi}{3}$ |
| $\cos x = \frac{\sqrt{3}}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{6}$, $\frac{11\pi}{6}$ |

**Insight**: The solution distribution patterns of $\sin$ and $\cos$ differ, so careful distinction is needed.

---

### 8.5.4 Basic Form $\tan x = k$ ($k \in \mathbb{R}$)

#### Fundamental Differences from $\sin$ and $\cos$

The tangent function $\tan x = \frac{\sin x}{\cos x}$ has three important features that make solving $\tan x = k$ different from $\sin$ and $\cos$:

1. **Range is all real numbers**: $k$ can be any real number, no restriction to $[-1, 1]$
2. **Period is $\pi$ (not $2\pi$)**: $\tan(x + \pi) = \tan x$, so the pattern repeats every $\pi$
3. **Has vertical asymptotes**: $\tan x$ is undefined at $x = \frac{\pi}{2} + n\pi$

#### Geometric Derivation — Understanding from the Unit Circle

On the unit circle, $\tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}$. Geometrically, $\tan\theta$ can also be thought of as the $y$-coordinate of the intersection of the **vertical line through $(1, 0)$** with the extension of the terminal side.

The equation $\tan x = k$ means finding terminal sides for which $\frac{y}{x} = k$, i.e., $y = kx$. This is equivalent to finding all angles whose terminal side coincides (or coincides in the opposite direction) with the line $y = kx$.

**Key observation**: If $\tan\alpha = k$ ($\alpha$ is an acute angle), then:
- In Quadrant I, $x = \alpha$ satisfies the condition
- In Quadrant III, $x = \pi + \alpha$ also satisfies the condition, because the ratio $\frac{y}{x}$ is the same
- More generally, $x = \alpha + n\pi$ all satisfy the condition

This is the geometric representation of the fact that the period of $\tan$ is $\pi$.

#### Complete Solution Steps

**Step 1**: Find the reference angle.

$$
\alpha = \arctan(|k|), \quad \alpha \in \left(0, \frac{\pi}{2}\right)
$$

**Step 2**: Determine the principal value.

If you don't need to discuss quadrants separately, you can directly use the calculator to find the principal value of $\arctan(k)$ (which lies between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$), then add integer multiples of $\pi$.

**Step 3**: Write the general solution.

$$
x = \arctan(k) + n\pi, \quad n \in \mathbb{Z}
$$

Or, using the reference angle $\alpha$ and quadrant method:
- $k > 0$: Quadrant I $x = \alpha$, Quadrant III $x = \pi + \alpha$, general solution $x = \alpha + n\pi$
- $k < 0$: Quadrant II $x = \pi - \alpha$, Quadrant IV $x = 2\pi - \alpha$, general solution $x = -\alpha + n\pi$ (or $x = \pi - \alpha + n\pi$)

**Simplification tip**: Using $x = \arctan(k) + n\pi$ directly is the most concise method, no need for quadrant-by-quadrant analysis.

#### Domain Check

$\tan x$ is undefined at $x = \frac{\pi}{2} + n\pi$. If a solution coincides exactly with these values (theoretically impossible since $\tan$ tends to infinity at these points), it must be excluded.

#### Worked Examples

---

**Example 1 ($\tan x = k$, $k > 0$ standard case)**: Solve $\tan x = \sqrt{3}$ for $0 \leq x < 2\pi$.

**Solution**:

**Method 1 (Reference angle method)**:

**Step 1**: $\alpha = \arctan(\sqrt{3}) = \frac{\pi}{3}$.

**Step 2**: $k = \sqrt{3} > 0$, general solution $x = \frac{\pi}{3} + n\pi$.

**Step 3**: Within $[0, 2\pi)$, take $n = 0, 1$:

$$
x = \frac{\pi}{3}, \quad x = \frac{\pi}{3} + \pi = \frac{4\pi}{3}
$$

**Method 2 (Direct principal value method)**:

$\arctan(\sqrt{3}) = \frac{\pi}{3}$, general solution $x = \frac{\pi}{3} + n\pi$, within $[0, 2\pi)$ take $n = 0, 1$.

**Step 4**: Verification. $\tan\frac{\pi}{3} = \sqrt{3}$ ✓, $\tan\frac{4\pi}{3} = \tan\frac{\pi}{3} = \sqrt{3}$ ✓

**Answer**: $x = \dfrac{\pi}{3}$ and $x = \dfrac{4\pi}{3}$

---

**Example 2 ($\tan x = k$, $k < 0$ standard case)**: Solve $\tan x = -1$ for $0 \leq x < 2\pi$.

**Solution**:

**Method 1 (Reference angle method)**:

**Step 1**: $\alpha = \arctan(1) = \frac{\pi}{4}$.

**Step 2**: $k = -1 < 0$, solutions are in Quadrants II and IV.

Quadrant II: $x = \pi - \alpha = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$
Quadrant IV: $x = 2\pi - \alpha = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}$

General solution: $x = \frac{3\pi}{4} + n\pi$ or $x = -\frac{\pi}{4} + n\pi$.

**Method 2 (Direct principal value method)**:

$\arctan(-1) = -\frac{\pi}{4}$, general solution $x = -\frac{\pi}{4} + n\pi$.

Within $[0, 2\pi)$, take $n = 1, 2$:

$$
x = -\frac{\pi}{4} + \pi = \frac{3\pi}{4}, \quad x = -\frac{\pi}{4} + 2\pi = \frac{7\pi}{4}
$$

**Step 3**: Verification. $\tan\frac{3\pi}{4} = -1$ ✓, $\tan\frac{7\pi}{4} = -1$ ✓

**Answer**: $x = \dfrac{3\pi}{4}$ and $x = \dfrac{7\pi}{4}$

---

**Example 6 (Comparison of all three basic forms)**: Solve the following three equations on $[0, 2\pi)$ and compare the number and distribution of solutions:
(a) $\sin x = \frac{1}{2}$
(b) $\cos x = \frac{1}{2}$
(c) $\tan x = \frac{1}{2}$

**Solution**:

**(a) $\sin x = \frac{1}{2}$**

Reference angle $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$.

$k > 0$, Quadrants I and II: $x = \frac{\pi}{6}$, $x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$

**2 solutions**.

**(b) $\cos x = \frac{1}{2}$**

Reference angle $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$.

$k > 0$, Quadrants I and IV: $x = \frac{\pi}{3}$, $x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$

**2 solutions**.

**(c) $\tan x = \frac{1}{2}$**

$\arctan\left(\frac{1}{2}\right) \approx 0.4636$, general solution $x = 0.4636 + n\pi$.

Within $[0, 2\pi)$: $n = 0$ gives $0.4636$, $n = 1$ gives $0.4636 + \pi \approx 3.6052$.

**2 solutions**.

**Comparison summary**:

| Equation | Reference angle | Solutions (radians) | Number of solutions |
|---------|---------------|-------------------|-------------------|
| $\sin x = \frac{1}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{6}$, $\frac{5\pi}{6}$ | 2 |
| $\cos x = \frac{1}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{3}$, $\frac{5\pi}{3}$ | 2 |
| $\tan x = \frac{1}{2}$ | $0.4636$ | $0.4636$, $3.6052$ | 2 |

On $[0, 2\pi)$, all three basic forms have 2 solutions (except special cases like $k = \pm 1$ or $k = 0$).

---

### 8.5.5 Equations Involving $\sec$, $\csc$, $\cot$

$\sec x$, $\csc x$, $\cot x$ are the reciprocals of $\cos x$, $\sin x$, $\tan x$ respectively. To solve such equations, we usually first take the reciprocal to convert to a basic form, but extra attention must be paid to the **domain**.

#### Conversion Method

| Equation form | Conversion step | Note |
|-------------|----------------|------|
| $\sec x = k$ | $\cos x = \frac{1}{k}$ | $k \neq 0$; $\cos x \neq 0$ |
| $\csc x = k$ | $\sin x = \frac{1}{k}$ | $k \neq 0$; $\sin x \neq 0$ |
| $\cot x = k$ | $\tan x = \frac{1}{k}$ | $k \neq 0$; $\sin x \neq 0$ |

---

**Example 1 ($\sec x = k$)**: Solve $\sec x = 2$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: Convert to $\cos x$. $\sec x = \frac{1}{\cos x} = 2$, so $\cos x = \frac{1}{2}$.

**Step 2**: Solve $\cos x = \frac{1}{2}$.

Reference angle $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$.

$k > 0$, Quadrants I and IV:

$$
x = \frac{\pi}{3}, \quad x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}
$$

**Step 3**: Check the domain. $\sec x$ is undefined where $\cos x = 0$. Both solutions give $\cos x = \frac{1}{2} \neq 0$, so they are valid.

**Answer**: $x = \dfrac{\pi}{3}$ and $x = \dfrac{5\pi}{3}$

---

**Example 2 ($\csc x = k$)**: Solve $\csc x = -2$ for $0 \leq x < 2\pi$.

**Solution**:

**Step 1**: $\csc x = \frac{1}{\sin x} = -2$, so $\sin x = -\frac{1}{2}$.

**Step 2**: Solve $\sin x = -\frac{1}{2}$.

Reference angle $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$.

$k < 0$, Quadrants III and IV:

$$
x = \pi + \frac{\pi}{6} = \frac{7\pi}{6}, \quad x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}
$$

**Step 3**: Check domain. $\csc x$ is undefined where $\sin x = 0$. Both solutions give $\sin x = -\frac{1}{2} \neq 0$, valid.

**Answer**: $x = \dfrac{7\pi}{6}$ and $x = \dfrac{11\pi}{6}$

---

### 8.5.6 Equations Using Identities (Syllabus Focus)

When the equation contains trigonometric functions of different names or higher powers, we need to use identities to unify the function name or reduce the power. This is a key focus area explicitly required by the syllabus.

#### Common Conversion Strategies

| Equation feature | Conversion method | Example |
|----------------|-----------------|---------|
| Contains $\tan$ and $\sec$ | Use $\sec^2 = 1 + \tan^2$ to unify variables | $2\sec^2 x + \tan x - 3 = 0$ |
| Contains $\cot$ and $\csc$ | Use $\csc^2 = 1 + \cot^2$ to unify variables | $3\csc^2 x - 2\cot^2 x = 4$ |
| Contains $\cot$ and $\tan$ | Use $\cot = \frac{1}{\tan}$ to interconvert | $4\cot\theta = \tan\theta$ |
| $a\sin(k\theta) + b\cos(k\theta) = 0$ | Divide by $\cos(k\theta)$ to get $\tan(k\theta) = -\frac{b}{a}$ | $5\sin 3\theta + 2\cos 3\theta = 0$ |
| Contains $\sin^2$ and $\cos^2$ | Use $\sin^2 + \cos^2 = 1$ to eliminate one variable | $\sin^2 x + \cos x = 1$ |
| Contains $\sin(2\theta)$ or $\cos(2\theta)$ | Expand or reduce power using double angle formulas | $\cos 2\theta + \sin\theta = 0$ |
| Contains $\csc^2(\frac{\theta}{2})$ etc. with compound angles | Substitute $u = \frac{\theta}{2}$ | $3\csc^2(\frac{\theta}{2}) = 4$ |

---

**Type 1: Converting $\cot$ and $\tan$**

**Example 1** (Syllabus example): Solve $4\cot\theta = \tan\theta$ for $0 \leq \theta < 2\pi$.

**Analysis**: The equation contains both $\cot$ and $\tan$, which are reciprocal. We can substitute $\cot\theta = \frac{1}{\tan\theta}$ to unify them into $\tan$.

**Solution**:

**Step 1**: Substitute $\cot\theta = \frac{1}{\tan\theta}$.

$$
4 \times \frac{1}{\tan\theta} = \tan\theta
$$

**Step 2**: Multiply both sides by $\tan\theta$ (note: $\tan\theta \neq 0$, otherwise the left side is undefined).

$$
4 = \tan^2\theta
$$

**Step 3**: Take the square root of both sides.

$$
\tan\theta = \pm 2
$$

**Step 4**: Solve each equation separately.

**Sub-case 1**: $\tan\theta = 2$.

$\alpha_1 = \arctan(2) \approx 1.1071$.

General solution $\theta = 1.1071 + n\pi$.

Within $[0, 2\pi)$: $n = 0$ gives $1.1071$, $n = 1$ gives $1.1071 + \pi \approx 4.2487$.

**Sub-case 2**: $\tan\theta = -2$.

$\alpha_2 = \arctan(-2) \approx -1.1071$.

General solution $\theta = -1.1071 + n\pi$.

Within $[0, 2\pi)$: $n = 1$ gives $-1.1071 + \pi \approx 2.0344$, $n = 2$ gives $-1.1071 + 2\pi \approx 5.1760$.

**Step 5**: Check the domain. The original equation requires $\sin\theta \neq 0$ (for $\cot\theta$) and $\cos\theta \neq 0$ (for $\tan\theta$). None of the four solutions violate this.

**Answer**: $\theta \in \{1.1071,\; 2.0344,\; 4.2487,\; 5.1760\}$

---

**Type 2: Using $\sec^2 = 1 + \tan^2$**

**Example 2** (Syllabus example): Solve $2\sec^2 x + \tan x - 3 = 0$ for $0 \leq x < 2\pi$.

**Analysis**: The equation contains both $\sec^2$ and $\tan$. Using the identity $\sec^2 x = 1 + \tan^2 x$, we can transform it into a quadratic in $\tan x$.

**Solution**:

**Step 1**: Substitute $\sec^2 x = 1 + \tan^2 x$.

$$
2(1 + \tan^2 x) + \tan x - 3 = 0
$$

**Step 2**: Expand and simplify.

$$
2 + 2\tan^2 x + \tan x - 3 = 0
$$

$$
2\tan^2 x + \tan x - 1 = 0
$$

**Step 3**: Let $u = \tan x$, solve $2u^2 + u - 1 = 0$.

Factorising: $(2u - 1)(u + 1) = 0$

$$
u = \frac{1}{2} \quad\text{or}\quad u = -1
$$

i.e., $\tan x = \frac{1}{2}$ or $\tan x = -1$.

**Step 4**: Solve $\tan x = \frac{1}{2}$.

$\alpha_1 = \arctan\left(\frac{1}{2}\right) \approx 0.4636$.

General solution $x = 0.4636 + n\pi$.

Within $[0, 2\pi)$: $n = 0$ gives $0.4636$, $n = 1$ gives $0.4636 + \pi \approx 3.6052$.

**Step 5**: Solve $\tan x = -1$.

$\arctan(-1) = -\frac{\pi}{4}$.

General solution $x = -\frac{\pi}{4} + n\pi$.

Within $[0, 2\pi)$: $n = 1$ gives $-\frac{\pi}{4} + \pi = \frac{3\pi}{4}$, $n = 2$ gives $-\frac{\pi}{4} + 2\pi = \frac{7\pi}{4}$.

**Step 6**: Check the domain. $\sec x$ is undefined where $\cos x = 0$ ($x = \frac{\pi}{2} + n\pi$). None of the four solutions satisfy this.

**Answer**: $x \in \{0.4636,\; 3.6052,\; \dfrac{3\pi}{4},\; \dfrac{7\pi}{4}\}$

---

**Type 3: $a\sin(k\theta) + b\cos(k\theta) = 0$**

**Example 3** (Syllabus example): Solve $5\sin 3\theta + 2\cos 3\theta = 0$ for $0 \leq \theta < 2\pi$.

**Analysis**: The equation contains both $\sin 3\theta$ and $\cos 3\theta$, and both terms have the same degree. Dividing both sides by $\cos 3\theta$ converts it to a $\tan$ form. However, we must separately check the case $\cos 3\theta = 0$.

**Solution**:

**Step 1**: Rearrange.

$$
5\sin 3\theta = -2\cos 3\theta
$$

**Step 2**: Divide both sides by $\cos 3\theta$ (first assume $\cos 3\theta \neq 0$).

$$
5\tan 3\theta = -2
$$

$$
\tan 3\theta = -\frac{2}{5}
$$

**Step 3**: Solve $\tan 3\theta = -\frac{2}{5}$.

$\alpha = \arctan\left(-\frac{2}{5}\right) \approx -0.3805$.

General solution: $3\theta = -0.3805 + n\pi$, i.e., $\theta = -\frac{0.3805}{3} + \frac{n\pi}{3} \approx -0.1268 + \frac{n\pi}{3}$.

**Step 4**: Find values of $n$ within $[0, 2\pi)$.

| $n$ | $\theta = -0.1268 + \frac{n\pi}{3}$ | Within $[0, 2\pi)$? |
|-----|--------------------------------------|---------------------|
| $1$ | $-0.1268 + \frac{\pi}{3} \approx 0.9204$ | ✓ |
| $2$ | $-0.1268 + \frac{2\pi}{3} \approx 1.9676$ | ✓ |
| $3$ | $-0.1268 + \pi \approx 3.0148$ | ✓ |
| $4$ | $-0.1268 + \frac{4\pi}{3} \approx 4.0620$ | ✓ |
| $5$ | $-0.1268 + \frac{5\pi}{3} \approx 5.1092$ | ✓ |
| $6$ | $-0.1268 + 2\pi \approx 6.1564$ | ✓ |
| $0$ | $-0.1268$ | ✗ (negative) |
| $7$ | $-0.1268 + \frac{7\pi}{3} \approx 7.2036$ | ✗ ($\geq 2\pi$) |

A total of 6 solutions.

**Step 5**: Check the case $\cos 3\theta = 0$.

When $\cos 3\theta = 0$, $3\theta = \frac{\pi}{2} + n\pi$, i.e., $\theta = \frac{\pi}{6} + \frac{n\pi}{3}$.

Substituting into the original equation: $5\sin 3\theta + 2\cos 3\theta = 5\sin(\frac{\pi}{2} + n\pi) + 2 \times 0 = 5(\pm 1) = \pm 5 \neq 0$.

Therefore the solutions of $\cos 3\theta = 0$ are not solutions of the original equation, so no extra solutions need to be added.

**Answer**: $\theta \in \{0.9204,\; 1.9676,\; 3.0148,\; 4.0620,\; 5.1092,\; 6.1564\}$

---

## 8.6 Proving Trigonometric Identities

### 8.6.1 Overview of Proof Strategies

Proving trigonometric identities does not have a fixed algorithm, but the following strategies are generally effective:

| Strategy | When to Use | Operation |
|---------|------------|----------|
| **Strategy 1: Start from the more complex side** | The two sides are asymmetric | Choose the side with more terms or more complex structure to simplify |
| **Strategy 2: Convert everything to $\sin$ and $\cos$** | Contains $\tan$, $\sec$, $\csc$, $\cot$ | Use basic relationships: $\tan = \frac{\sin}{\cos}$, $\sec = \frac{1}{\cos}$, etc. |
| **Strategy 3: Combine fractions by finding a common denominator** | Fraction addition/subtraction | Find a common denominator, combine numerators |
| **Strategy 4: Use $\sin^2 + \cos^2 = 1$** | Appears with $1$ or squared terms | Replace or combine using the identity |
| **Strategy 5: Factorisation** | Numerator/denominator can be factorised | Extract common factors, difference of squares |
| **Strategy 6: Multiply numerator and denominator by the conjugate** | Denominator contains $1 \pm \sin\theta$ or $1 \pm \cos\theta$ | Multiply by $1 \mp \sin\theta$ or $1 \mp \cos\theta$ |
| **Strategy 7: Use double angle formulas** | Angles are inconsistent | Expand $2\theta$ or reduce powers |

### 8.6.2 Writing Standards for Proofs

When writing a proof, follow these conventions:

1. Clearly state which side you start from ("LHS $=$" or "RHS $=$")
2. Each step must be based on a known identity or algebraic operation
3. End with a form identical to the other side
4. Conclude with "$\blacksquare$" or "QED"

### 8.6.3 Detailed Proof Examples

---

**Example 1 (Strategy: Convert to $\sin$ and $\cos$)**: Prove $\tan x + \cot x = \sec x \csc x$.

**Proof**:

Starting from the LHS:

$$
\tan x + \cot x = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}
$$

Finding a common denominator $\sin x \cos x$:

$$
= \frac{\sin^2 x + \cos^2 x}{\sin x \cos x}
$$

Using $\sin^2 x + \cos^2 x = 1$:

$$
= \frac{1}{\sin x \cos x}
$$

Now the RHS:

$$
\sec x \csc x = \frac{1}{\cos x} \cdot \frac{1}{\sin x} = \frac{1}{\sin x \cos x}
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 2 (Strategy: Combine fractions)**: Prove $\dfrac{\sin\theta}{1 + \cos\theta} + \dfrac{1 + \cos\theta}{\sin\theta} = 2\csc\theta$.

**Proof**:

Starting from the LHS, find a common denominator:

$$
\frac{\sin\theta}{1 + \cos\theta} + \frac{1 + \cos\theta}{\sin\theta}
= \frac{\sin^2\theta + (1 + \cos\theta)^2}{\sin\theta(1 + \cos\theta)}
$$

Expand the numerator:

$$
\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta
$$

Using $\sin^2\theta + \cos^2\theta = 1$:

$$
= (\sin^2\theta + \cos^2\theta) + 1 + 2\cos\theta = 1 + 1 + 2\cos\theta = 2 + 2\cos\theta
$$

Factor out $2(1 + \cos\theta)$:

$$
= \frac{2(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)}
$$

Cancel $1 + \cos\theta$ (note $1 + \cos\theta \neq 0$):

$$
= \frac{2}{\sin\theta} = 2\csc\theta
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 3 (Strategy: Multiply numerator and denominator by conjugate)**: Prove $\dfrac{1 - \sin\theta}{\cos\theta} = \dfrac{\cos\theta}{1 + \sin\theta}$.

**Proof**:

Starting from the LHS, multiply numerator and denominator by $1 + \sin\theta$:

$$
\frac{1 - \sin\theta}{\cos\theta} = \frac{(1 - \sin\theta)(1 + \sin\theta)}{\cos\theta(1 + \sin\theta)}
$$

The numerator expands to $1 - \sin^2\theta = \cos^2\theta$:

$$
= \frac{\cos^2\theta}{\cos\theta(1 + \sin\theta)}
$$

Cancel $\cos\theta$ (assuming $\cos\theta \neq 0$):

$$
= \frac{\cos\theta}{1 + \sin\theta}
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

**Alternative proof** (starting from the RHS):

$$
\frac{\cos\theta}{1 + \sin\theta} = \frac{\cos\theta(1 - \sin\theta)}{(1 + \sin\theta)(1 - \sin\theta)} = \frac{\cos\theta(1 - \sin\theta)}{1 - \sin^2\theta}
$$

$$
= \frac{\cos\theta(1 - \sin\theta)}{\cos^2\theta} = \frac{1 - \sin\theta}{\cos\theta}
$$

The same result is obtained. $\blacksquare$

---

**Example 4 (Strategy: Using $\sec^2 = 1 + \tan^2$)**: Prove $\sec^2\theta + \csc^2\theta = \sec^2\theta\csc^2\theta$.

**Proof**:

Starting from the LHS, convert $\sec$ and $\csc$ to $\sin$ and $\cos$:

$$
\sec^2\theta + \csc^2\theta = \frac{1}{\cos^2\theta} + \frac{1}{\sin^2\theta}
$$

Find a common denominator $\sin^2\theta\cos^2\theta$:

$$
= \frac{\sin^2\theta + \cos^2\theta}{\sin^2\theta\cos^2\theta}
$$

Using $\sin^2\theta + \cos^2\theta = 1$:

$$
= \frac{1}{\sin^2\theta\cos^2\theta}
$$

Now the RHS:

$$
\sec^2\theta\csc^2\theta = \frac{1}{\cos^2\theta} \cdot \frac{1}{\sin^2\theta} = \frac{1}{\sin^2\theta\cos^2\theta}
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 5 (Strategy: Factorisation + identity)**: Prove $\cos^4\theta - \sin^4\theta = \cos(2\theta)$.

**Proof**:

Starting from the LHS, use the difference of squares:

$$
\cos^4\theta - \sin^4\theta = (\cos^2\theta)^2 - (\sin^2\theta)^2
$$

$$
= (\cos^2\theta - \sin^2\theta)(\cos^2\theta + \sin^2\theta)
$$

Using $\cos^2\theta + \sin^2\theta = 1$:

$$
= (\cos^2\theta - \sin^2\theta) \times 1 = \cos^2\theta - \sin^2\theta
$$

Using the double angle formula $\cos(2\theta) = \cos^2\theta - \sin^2\theta$:

$$
= \cos(2\theta)
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 6 (Strategy: Using $\csc^2 = 1 + \cot^2$)**: Prove $\dfrac{1 + \tan^2\theta}{1 + \cot^2\theta} = \tan^2\theta$.

**Proof**:

Starting from the LHS. The numerator is $\sec^2\theta = 1 + \tan^2\theta$, the denominator is $\csc^2\theta = 1 + \cot^2\theta$:

$$
\frac{1 + \tan^2\theta}{1 + \cot^2\theta} = \frac{\sec^2\theta}{\csc^2\theta}
$$

Convert $\sec$ and $\csc$ to $\sin$ and $\cos$:

$$
= \frac{1/\cos^2\theta}{1/\sin^2\theta} = \frac{\sin^2\theta}{\cos^2\theta} = \tan^2\theta
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 7 (Strategy: Using double angle formulas)**: Prove $\dfrac{\sin(2\theta)}{1 - \cos(2\theta)} = \cot\theta$.

**Proof**:

Starting from the LHS, substitute $\sin(2\theta) = 2\sin\theta\cos\theta$ and $\cos(2\theta) = 1 - 2\sin^2\theta$:

$$
\frac{\sin(2\theta)}{1 - \cos(2\theta)} = \frac{2\sin\theta\cos\theta}{1 - (1 - 2\sin^2\theta)}
$$

Simplify the denominator:

$$
= \frac{2\sin\theta\cos\theta}{2\sin^2\theta}
$$

Cancel $2\sin\theta$ (assuming $\sin\theta \neq 0$):

$$
= \frac{\cos\theta}{\sin\theta} = \cot\theta
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

**Example 8 (Comprehensive strategy)**: Prove $\sin x \tan x + \cos x = \sec x$.

> This is a type of example explicitly listed in the syllabus.

**Proof**:

Starting from the LHS, convert $\tan x$ to $\frac{\sin x}{\cos x}$:

$$
\sin x \tan x + \cos x = \sin x \cdot \frac{\sin x}{\cos x} + \cos x
$$

$$
= \frac{\sin^2 x}{\cos x} + \cos x
$$

Write $\cos x$ as $\frac{\cos^2 x}{\cos x}$ and combine:

$$
= \frac{\sin^2 x + \cos^2 x}{\cos x}
$$

Using $\sin^2 x + \cos^2 x = 1$:

$$
= \frac{1}{\cos x} = \sec x
$$

LHS $=$ RHS, the identity is proved. $\blacksquare$

---

> **Proof summary**: Proving trigonometric identities is essentially a process of "simplification and transformation." The most important thing is to be familiar with the three basic identities and algebraic manipulation techniques. Start from the more complex side and gradually move towards the other side. If one approach doesn't work, try starting from the other side or changing the transformation strategy.

---
---

