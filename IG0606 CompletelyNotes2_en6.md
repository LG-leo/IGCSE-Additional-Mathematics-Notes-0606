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

# Chapter 4: Equations and Inequalities (Graphical Methods)

## Introduction

In previous chapters, we learned algebraic methods for solving equations and inequalities — factorisation, the quadratic formula, completing the square, etc. However, many equations and inequalities are difficult to handle purely algebraically, especially those involving absolute values, cubic polynomials, and complex substitutions. **Graphical methods** provide a powerful alternative approach: using the visual representation of functions to intuitively understand the solutions of equations and the solution sets of inequalities. Graphical methods do not always give exact values, but they help us quickly grasp the overall structure of the solution and provide geometric intuition for algebraic operations.

In this chapter, we will integrate knowledge from previous chapters — particularly the **discriminant and factorisation from Chapter 3 (Quadratic Functions)**, **absolute value function graphs from Chapter 4 (Functions)**, and **differentiation tools from Chapter 5 (Differentiation)** — to systematically handle five types of problems: absolute value equations, absolute value inequalities, substitution to reduce to quadratic equations, cubic polynomial graphs and inequalities, and graphical solutions of simultaneous equations.

---

## Syllabus Mapping (Cambridge IGCSE Additional Mathematics 0606, 2028–2030)

| Syllabus Ref | Content | Corresponding Section |
|---------|------|---------|
| 4.1 | Solve equations of the form $|ax+b| = c \;(c \ge 0)$, $|ax+b| = cx+d$, $|ax+b| = |cx+d|$, $|ax^2+bx+c| = d$ (algebraic or graphical methods) | 6.1 |
| 4.2 | Solve inequalities of the form $k|ax+b| > c\;(c\ge0)$, $k|ax+b| \le c\;(c>0)$, $k|ax+b| \le |cx+d|\;(k>0)$, $|ax+b| \le cx+d$, $|ax^2+bx+c| > d$, $|ax^2+bx+c| \le d$ | 6.2 |
| 4.3 | Construct and solve quadratic equations using substitution | 6.3 |
| 4.4 | Sketch graphs of cubic polynomials (products of three linear factors) and their absolute values | 6.4 |
| 4.5 | Solve cubic inequalities of the form $f(x) \ge d$, $f(x) > d$, $f(x) \le d$, $f(x) < d$ using graphical methods | 6.4 |
| 5.1 | Solve simultaneous linear equations in two variables by elimination or substitution | 6.5 |

---

## Prerequisite Knowledge: Sets and Interval Notation

> When solving inequalities, we usually use **intervals** or **sets** to express the solution set. This section reviews basic set notation and interval representation, which form the foundation for all content in this chapter.

### Basic Concepts of Sets

A **set** is a collection of distinct, well-defined objects. The objects in a set are called **elements**.

- $a \in A$: $a$ belongs to set $A$ ($a$ is an element of $A$)
- $a \notin A$: $a$ does not belong to set $A$

**Common number sets**:

- $\mathbb{N} = \{1, 2, 3, 4, \dots\}$: Natural numbers
- $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$: Integers
- $\mathbb{Q}$: Rational numbers (numbers that can be expressed as fractions)
- $\mathbb{R}$: Real numbers (including rational and irrational numbers)
- $\mathbb{R}^+$: Positive real numbers
- $\emptyset$: Empty set (a set containing no elements)

**Representation of sets**:

**Roster form**: $A = \{1, 2, 3, 4, 5\}$

**Set-builder form**: $A = \{x \mid x \text{ is an integer greater than 0 and less than 6}\}$, or more generally $A = \{x \in \mathbb{R} \mid x^2 < 4\}$ (representing all real numbers $x$ satisfying $x^2 < 4$).

### Interval Notation

An interval is a subset of the real numbers, represented by a continuous segment on the number line.

| Type | Inequality | Interval Notation | Number Line |
|---------|-----------|---------|---------|
| Closed interval | $a \le x \le b$ | $[a, b]$ | Solid dots at both ends |
| Open interval | $a < x < b$ | $(a, b)$ | Open dots at both ends |
| Left-closed right-open | $a \le x < b$ | $[a, b)$ | Solid left, open right |
| Left-open right-closed | $a < x \le b$ | $(a, b]$ | Open left, solid right |
| Infinite interval | $x \ge a$ | $[a, \infty)$ | Extends rightward |
| Infinite interval | $x > a$ | $(a, \infty)$ | Extends rightward |
| Infinite interval | $x \le b$ | $(-\infty, b]$ | Extends leftward |
| Infinite interval | $x < b$ | $(-\infty, b)$ | Extends leftward |
| All real numbers | $x \in \mathbb{R}$ | $(-\infty, \infty)$ | Entire number line |

> ⚠️ **Note**: $\infty$ (infinity) is not a number but a concept representing "unbounded extension." Therefore the end involving $\infty$ is always written with a round bracket (open interval).

### Set Operations

**Union** $A \cup B = \{x \mid x \in A \text{ or } x \in B\}$: All elements belonging to $A$ **or** $B$.

**Intersection** $A \cap B = \{x \mid x \in A \text{ and } x \in B\}$: All elements belonging to both $A$ **and** $B$.

**Example**: Let $A = \{x \mid x < 1\}$, $B = \{x \mid x \ge -2\}$.

- $A \cap B = \{x \mid -2 \le x < 1\} = [-2, 1)$
- $A \cup B = \mathbb{R} = (-\infty, \infty)$

**Example**: Solving $x^2 - 5x + 6 > 0$ gives $x < 2$ or $x > 3$, with solution set expressed in interval notation as $(-\infty, 2) \cup (3, \infty)$. Here $\cup$ represents the "union" of the two intervals — $x$ can satisfy either one.

---

## 4.1 Absolute Value Equations

### 4.1.1 Definition and Geometric Meaning of Absolute Value

Geometrically, the absolute value $|A|$ represents the **distance** from point $A$ to the origin on the number line. Algebraically, it is defined as:

$$
|x| = \begin{cases}
x, & x \ge 0 \\
-x, & x < 0
\end{cases}
$$

Important properties of absolute value:
- $|A| \ge 0$ for all real numbers $A$
- $|A|^2 = A^2$
- $|AB| = |A| \cdot |B|$
- $\left|\dfrac{A}{B}\right| = \dfrac{|A|}{|B|}$ ($B \neq 0$)

The core idea behind solving absolute value equations is **removing the absolute value sign**, usually achieved through case analysis or squaring both sides.

### 4.1.2 Type $|ax + b| = c \quad (c \ge 0)$

This is the simplest absolute value equation. By definition, $|ax + b| = c$ is equivalent to:

$$
ax + b = c \quad \text{or} \quad ax + b = -c
$$

---

**Example 1**: Solve $|3x - 7| = 5$.

**Solution**:

$$
3x - 7 = 5 \quad \text{or} \quad 3x - 7 = -5
$$

$$
3x = 12 \quad \text{or} \quad 3x = 2
$$

$$
x = 4 \quad \text{or} \quad x = \frac{2}{3}
$$

Verification: $|3(4) - 7| = |12 - 7| = 5$ ✓, $|3(\frac{2}{3}) - 7| = |2 - 7| = 5$ ✓.

---

**Example 2**: Solve $|5 - 2x| = 9$.

**Solution**:

$$
5 - 2x = 9 \quad \text{or} \quad 5 - 2x = -9
$$

$$
-2x = 4 \quad \text{or} \quad -2x = -14
$$

$$
x = -2 \quad \text{or} \quad x = 7
$$

Verification: $|5 - 2(-2)| = |5 + 4| = 9$ ✓, $|5 - 2(7)| = |5 - 14| = 9$ ✓.

---

**Example 3**: Solve $|4x + 3| = 0$.

**Solution**:

$$
4x + 3 = 0
$$

$$
x = -\frac{3}{4}
$$

Note: When $c = 0$, there is only one solution, because $4x + 3$ equals both $0$ and $-0$ (the same). Verification: $|4(-\frac{3}{4}) + 3| = |-3 + 3| = 0$ ✓.

---

### 4.1.3 Type $|ax + b| = cx + d$

When the right-hand side also contains a variable, we cannot simply split into two equations — we must ensure the right-hand side is non-negative (absolute value is always non-negative, so the right-hand side must also be non-negative).

**Method 1: Case analysis** (based on the sign of $ax + b$).

**Method 2: Squaring both sides** to obtain a quadratic equation, then checking the solutions.

---

**Example 4**: Solve $|2x - 3| = x + 1$.

**Solution (Case analysis)**:

**Case 1**: $2x - 3 \ge 0$, i.e., $x \ge \frac{3}{2}$.
Then $|2x - 3| = 2x - 3$, and the equation becomes:

$$
2x - 3 = x + 1 \Rightarrow x = 4
$$

Check the condition: $4 \ge \frac{3}{2}$ ✓.

**Case 2**: $2x - 3 < 0$, i.e., $x < \frac{3}{2}$.
Then $|2x - 3| = -(2x - 3) = -2x + 3$, and the equation becomes:

$$
-2x + 3 = x + 1 \Rightarrow -3x = -2 \Rightarrow x = \frac{2}{3}
$$

Check the condition: $\frac{2}{3} < \frac{3}{2}$ ✓.

Therefore the solutions are $x = 4$ and $x = \frac{2}{3}$.

**Solution (Squaring and checking)**:

Square both sides: $(2x - 3)^2 = (x + 1)^2$

$$
4x^2 - 12x + 9 = x^2 + 2x + 1
$$

$$
3x^2 - 14x + 8 = 0
$$

$$
(3x - 2)(x - 4) = 0
$$

$$
x = \frac{2}{3} \quad \text{or} \quad x = 4
$$

Verification: For $x = 4$, the right-hand side $4 + 1 = 5 > 0$ ✓; for $x = \frac{2}{3}$, the right-hand side $\frac{2}{3} + 1 = \frac{5}{3} > 0$ ✓. Both solutions are valid.

---

**Example 5**: Solve $|x + 2| = 2x - 1$.

**Solution**:

**Case 1**: $x + 2 \ge 0$, i.e., $x \ge -2$.

$$
x + 2 = 2x - 1 \Rightarrow 3 = x \Rightarrow x = 3
$$

Check: $3 \ge -2$ ✓. Verify the right-hand side: $2(3) - 1 = 5 > 0$ ✓.

**Case 2**: $x + 2 < 0$, i.e., $x < -2$.

$$
-(x + 2) = 2x - 1 \Rightarrow -x - 2 = 2x - 1 \Rightarrow -1 = 3x \Rightarrow x = -\frac{1}{3}
$$

Check the condition: $-\frac{1}{3} < -2$? No! $-\frac{1}{3} > -2$, so this solution is invalid.

Therefore the only solution is $x = 3$.

---

**Example 6**: Solve $|3x + 1| = 2 - x$.

**Solution**:

**Case 1**: $3x + 1 \ge 0$, i.e., $x \ge -\frac{1}{3}$.

$$
3x + 1 = 2 - x \Rightarrow 4x = 1 \Rightarrow x = \frac{1}{4}
$$

Check: $\frac{1}{4} \ge -\frac{1}{3}$ ✓. Right-hand side: $2 - \frac{1}{4} = \frac{7}{4} > 0$ ✓.

**Case 2**: $3x + 1 < 0$, i.e., $x < -\frac{1}{3}$.

$$
-(3x + 1) = 2 - x \Rightarrow -3x - 1 = 2 - x \Rightarrow -2x = 3 \Rightarrow x = -\frac{3}{2}
$$

Check: $-\frac{3}{2} < -\frac{1}{3}$ ✓. Right-hand side: $2 - (-\frac{3}{2}) = \frac{7}{2} > 0$ ✓.

Therefore the solutions are $x = \frac{1}{4}$ and $x = -\frac{3}{2}$.

---

### 4.1.4 Type $|ax + b| = |cx + d|$

When two absolute values are equal, it means the two expressions are either equal or opposites. No case analysis conditions are needed.

$$
|ax + b| = |cx + d| \quad \Longleftrightarrow \quad ax + b = cx + d \quad \text{or} \quad ax + b = -(cx + d)
$$

---

**Example 7**: Solve $|2x + 5| = |x - 3|$.

**Solution**:

$$
2x + 5 = x - 3 \quad \text{or} \quad 2x + 5 = -(x - 3)
$$

**Equation 1**: $2x + 5 = x - 3 \Rightarrow x = -8$

**Equation 2**: $2x + 5 = -x + 3 \Rightarrow 3x = -2 \Rightarrow x = -\frac{2}{3}$

Therefore the solutions are $x = -8$ and $x = -\frac{2}{3}$.

Verification: $|2(-8) + 5| = |-11| = 11$, $|(-8) - 3| = |-11| = 11$ ✓.
$|2(-\frac{2}{3}) + 5| = |-\frac{4}{3} + 5| = |\frac{11}{3}| = \frac{11}{3}$, $|-\frac{2}{3} - 3| = |-\frac{11}{3}| = \frac{11}{3}$ ✓.

---

**Example 8**: Solve $|5x - 2| = |3x + 4|$.

**Solution**:

$$
5x - 2 = 3x + 4 \quad \text{or} \quad 5x - 2 = -(3x + 4)
$$

**Equation 1**: $5x - 2 = 3x + 4 \Rightarrow 2x = 6 \Rightarrow x = 3$

**Equation 2**: $5x - 2 = -3x - 4 \Rightarrow 8x = -2 \Rightarrow x = -\frac{1}{4}$

Therefore the solutions are $x = 3$ and $x = -\frac{1}{4}$.

---

**Example 9**: Solve $|x + 1| = |2x - 5|$.

**Solution**:

$$
x + 1 = 2x - 5 \quad \text{or} \quad x + 1 = -(2x - 5)
$$

**Equation 1**: $x + 1 = 2x - 5 \Rightarrow 6 = x \Rightarrow x = 6$

**Equation 2**: $x + 1 = -2x + 5 \Rightarrow 3x = 4 \Rightarrow x = \frac{4}{3}$

Therefore the solutions are $x = 6$ and $x = \frac{4}{3}$.

---

### 4.1.5 Type $|ax^2 + bx + c| = d$

When the expression inside the absolute value is a quadratic function, the approach is the same: removing the absolute value gives two quadratic equations.

---

**Example 10**: Solve $|x^2 - 4x + 3| = 3$.

**Solution**:

$$
x^2 - 4x + 3 = 3 \quad \text{or} \quad x^2 - 4x + 3 = -3
$$

**Equation 1**: $x^2 - 4x = 0 \Rightarrow x(x - 4) = 0 \Rightarrow x = 0$ or $x = 4$

**Equation 2**: $x^2 - 4x + 6 = 0$

Discriminant $\Delta = (-4)^2 - 4(1)(6) = 16 - 24 = -8 < 0$, no real solutions.

Therefore the solutions are $x = 0$ and $x = 4$.

---

**Example 11**: Solve $|2x^2 - 5x - 3| = 2$.

**Solution**:

$$
2x^2 - 5x - 3 = 2 \quad \text{or} \quad 2x^2 - 5x - 3 = -2
$$

**Equation 1**: $2x^2 - 5x - 5 = 0$

$$
x = \frac{5 \pm \sqrt{25 - 4(2)(-5)}}{2(2)} = \frac{5 \pm \sqrt{25 + 40}}{4} = \frac{5 \pm \sqrt{65}}{4}
$$

**Equation 2**: $2x^2 - 5x - 1 = 0$

$$
x = \frac{5 \pm \sqrt{25 - 4(2)(-1)}}{4} = \frac{5 \pm \sqrt{25 + 8}}{4} = \frac{5 \pm \sqrt{33}}{4}
$$

Therefore there are four solutions: $x = \frac{5 \pm \sqrt{65}}{4}$ and $x = \frac{5 \pm \sqrt{33}}{4}$.

---

**Example 12**: Solve $|x^2 - 9| = 7$.

**Solution**:

$$
x^2 - 9 = 7 \quad \text{or} \quad x^2 - 9 = -7
$$

**Equation 1**: $x^2 = 16 \Rightarrow x = \pm 4$

**Equation 2**: $x^2 = 2 \Rightarrow x = \pm \sqrt{2}$

Therefore the solutions are $x = 4, -4, \sqrt{2}, -\sqrt{2}$.

---

## 4.2 Absolute Value Inequalities

The core idea of absolute value inequalities: **transform the absolute value inequality into a system of inequalities without absolute value**, then solve using the number line or graphs.

### 4.2.1 Basic Types $|ax + b| > c$ and $|ax + b| \le c$

**Core rules** ($c > 0$):

$$
|ax + b| > c \quad \Longleftrightarrow \quad ax + b < -c \quad \text{or} \quad ax + b > c
$$

$$
|ax + b| \le c \quad \Longleftrightarrow \quad -c \le ax + b \le c
$$

> Memory aid: "**Greater than → outside, less than → middle**."

For $k|ax + b| > c$ ($k > 0$, $c \ge 0$), first divide both sides by $k$ to get the standard form: $|ax + b| > \frac{c}{k}$.

---

**Example 1**: Solve $|2x - 5| > 3$.

**Solution**:

"Greater than → outside":

$$
2x - 5 < -3 \quad \text{or} \quad 2x - 5 > 3
$$

$$
2x < 2 \quad \text{or} \quad 2x > 8
$$

$$
x < 1 \quad \text{or} \quad x > 4
$$

Solution set: $x \in (-\infty, 1) \cup (4, \infty)$.

---

**Example 2**: Solve $3|2x + 1| \le 15$.

**Solution**:

First divide by $3$: $|2x + 1| \le 5$

"Less than → middle":

$$
-5 \le 2x + 1 \le 5
$$

Left: $-5 \le 2x + 1 \Rightarrow -6 \le 2x \Rightarrow x \ge -3$
Right: $2x + 1 \le 5 \Rightarrow 2x \le 4 \Rightarrow x \le 2$

Therefore the solution set is $-3 \le x \le 2$, i.e., $x \in [-3, 2]$.

---

**Example 3**: Solve $2|4 - x| > 10$.

**Solution**:

Divide by $2$: $|4 - x| > 5$

"Greater than → outside":

$$
4 - x < -5 \quad \text{or} \quad 4 - x > 5
$$

$$
-x < -9 \quad \text{or} \quad -x > 1
$$

$$
x > 9 \quad \text{or} \quad x < -1
$$

Solution set: $x \in (-\infty, -1) \cup (9, \infty)$.

---

### 4.2.2 Type $k|ax + b| \le |cx + d| \quad (k > 0)$

When both sides have absolute values, the most reliable method is **squaring both sides**, using the property $|A|^2 = A^2$ to obtain an inequality without absolute values.

---

**Example 4**: Solve $|2x - 1| \le |x + 3|$.

**Solution**:

Square both sides (the inequality sign remains unchanged since both sides are non-negative):

$$
(2x - 1)^2 \le (x + 3)^2
$$

$$
4x^2 - 4x + 1 \le x^2 + 6x + 9
$$

$$
3x^2 - 10x - 8 \le 0
$$

Solve $3x^2 - 10x - 8 = 0$:

$$
x = \frac{10 \pm \sqrt{100 + 96}}{6} = \frac{10 \pm \sqrt{196}}{6} = \frac{10 \pm 14}{6}
$$

$$
x = \frac{24}{6} = 4 \quad \text{or} \quad x = \frac{-4}{6} = -\frac{2}{3}
$$

The coefficient of $x^2$ is $3 > 0$, so the parabola opens upward, and $3x^2 - 10x - 8 \le 0$ is satisfied between the roots:

$$
-\frac{2}{3} \le x \le 4
$$

i.e., $x \in \left[-\frac{2}{3}, 4\right]$.

---

**Example 5**: Solve $2|x + 2| > |3x - 1|$.

**Solution**:

Square both sides:

$$
4(x + 2)^2 > (3x - 1)^2
$$

$$
4(x^2 + 4x + 4) > 9x^2 - 6x + 1
$$

$$
4x^2 + 16x + 16 > 9x^2 - 6x + 1
$$

$$
0 > 5x^2 - 22x - 15
$$

$$
5x^2 - 22x - 15 < 0
$$

Solve $5x^2 - 22x - 15 = 0$:

$$
x = \frac{22 \pm \sqrt{484 + 300}}{10} = \frac{22 \pm \sqrt{784}}{10} = \frac{22 \pm 28}{10}
$$

$$
x = \frac{50}{10} = 5 \quad \text{or} \quad x = \frac{-6}{10} = -\frac{3}{5}
$$

The coefficient of $x^2$ is $5 > 0$, so the solution of $5x^2 - 22x - 15 < 0$ is:

$$
-\frac{3}{5} < x < 5
$$

i.e., $x \in \left(-\frac{3}{5}, 5\right)$.

---

**Example 6**: Solve $3|x - 1| \le 2|x + 2|$.

**Solution**:

Square both sides:

$$
9(x - 1)^2 \le 4(x + 2)^2
$$

$$
9(x^2 - 2x + 1) \le 4(x^2 + 4x + 4)
$$

$$
9x^2 - 18x + 9 \le 4x^2 + 16x + 16
$$

$$
5x^2 - 34x - 7 \le 0
$$

Solve $5x^2 - 34x - 7 = 0$:

$$
x = \frac{34 \pm \sqrt{1156 + 140}}{10} = \frac{34 \pm \sqrt{1296}}{10} = \frac{34 \pm 36}{10}
$$

$$
x = \frac{70}{10} = 7 \quad \text{or} \quad x = \frac{-2}{10} = -\frac{1}{5}
$$

The coefficient of $x^2$ is $5 > 0$, so the solution of $5x^2 - 34x - 7 \le 0$ is:

$$
-\frac{1}{5} \le x \le 7
$$

i.e., $x \in \left[-\frac{1}{5}, 7\right]$.

---

### 4.2.3 Type $|ax + b| \le cx + d$

The right-hand side of this type of inequality is a linear expression. There are two methods: algebraic case analysis and graphical method.

**Algebraic case analysis**: Discuss based on the sign of $ax + b$, solve and check whether it satisfies the condition.

**Graphical method**: Draw the graphs of $y = |ax + b|$ and $y = cx + d$, and find the intervals where the former lies below (or above) the latter.

---

**Example 7**: Solve $|x - 3| \le 2x + 1$.

**Solution (Algebraic case analysis)**:

**Case 1**: $x - 3 \ge 0$, i.e., $x \ge 3$.

$$
x - 3 \le 2x + 1 \Rightarrow -4 \le x
$$

Combining with $x \ge 3$ gives $x \ge 3$.

**Case 2**: $x - 3 < 0$, i.e., $x < 3$.

$$
-(x - 3) \le 2x + 1 \Rightarrow -x + 3 \le 2x + 1 \Rightarrow 2 \le 3x \Rightarrow x \ge \frac{2}{3}
$$

Combining with $x < 3$ gives $\frac{2}{3} \le x < 3$.

Taking the union of both cases: $x \ge \frac{2}{3}$, i.e., $x \in \left[\frac{2}{3}, \infty\right)$.

---

**Example 8**: Solve $|2x + 5| > x + 4$.

**Solution**:

**Case 1**: $2x + 5 \ge 0$, i.e., $x \ge -\frac{5}{2}$.

$$
2x + 5 > x + 4 \Rightarrow x > -1
$$

Combining with $x \ge -\frac{5}{2}$ gives $x > -1$.

**Case 2**: $2x + 5 < 0$, i.e., $x < -\frac{5}{2}$.

$$
-(2x + 5) > x + 4 \Rightarrow -2x - 5 > x + 4 \Rightarrow -3x > 9 \Rightarrow x < -3
$$

Combining with $x < -\frac{5}{2}$ gives $x < -3$.

Solution set: $x \in (-\infty, -3) \cup (-1, \infty)$.

---

**Example 9**: Solve $|x + 2| \le 3x - 1$.

**Solution**:

**Case 1**: $x + 2 \ge 0$, i.e., $x \ge -2$.

$$
x + 2 \le 3x - 1 \Rightarrow 3 \le 2x \Rightarrow x \ge \frac{3}{2}
$$

Combining with $x \ge -2$ gives $x \ge \frac{3}{2}$.

**Case 2**: $x + 2 < 0$, i.e., $x < -2$.

$$
-(x + 2) \le 3x - 1 \Rightarrow -x - 2 \le 3x - 1 \Rightarrow -1 \le 4x \Rightarrow x \ge -\frac{1}{4}
$$

But the condition is $x < -2$, and $-\frac{1}{4} > -2$, so there is no valid solution.

Therefore the solution set is $x \ge \frac{3}{2}$, i.e., $x \in \left[\frac{3}{2}, \infty\right)$.

---

### 4.2.4 Type $|ax^2 + bx + c| > d$ and $|ax^2 + bx + c| \le d$

Approach: Remove the absolute value to obtain two quadratic inequalities, solve each separately, then take the union or intersection.

---

**Example 10**: Solve $|x^2 - 3x| \le 4$.

**Solution**:

From $|f(x)| \le 4$ we get $-4 \le x^2 - 3x \le 4$.

**Left inequality**: $x^2 - 3x \ge -4$

$$
x^2 - 3x + 4 \ge 0
$$

Discriminant $\Delta = 9 - 16 = -7 < 0$, and the coefficient of $x^2$ is $1 > 0$, so $x^2 - 3x + 4 > 0$ holds for all $x$. The left inequality is automatically satisfied.

**Right inequality**: $x^2 - 3x \le 4$

$$
x^2 - 3x - 4 \le 0
$$

$$
(x - 4)(x + 1) \le 0
$$

Solution: $-1 \le x \le 4$.

Therefore the solution set of the original inequality is $x \in [-1, 4]$.

---

**Example 11**: Solve $|x^2 - 2x - 3| > 3$.

**Solution**:

From $|f(x)| > 3$ we get $x^2 - 2x - 3 < -3$ or $x^2 - 2x - 3 > 3$.

**Inequality 1**: $x^2 - 2x - 3 < -3$

$$
x^2 - 2x < 0 \Rightarrow x(x - 2) < 0 \Rightarrow 0 < x < 2
$$

**Inequality 2**: $x^2 - 2x - 3 > 3$

$$
x^2 - 2x - 6 > 0
$$

Solve $x^2 - 2x - 6 = 0$:

$$
x = \frac{2 \pm \sqrt{4 + 24}}{2} = \frac{2 \pm \sqrt{28}}{2} = \frac{2 \pm 2\sqrt{7}}{2} = 1 \pm \sqrt{7}
$$

The coefficient of $x^2$ is $1 > 0$, so $x^2 - 2x - 6 > 0$ holds for:

$$
x < 1 - \sqrt{7} \quad \text{or} \quad x > 1 + \sqrt{7}
$$

where $1 - \sqrt{7} \approx 1 - 2.646 = -1.646$, $1 + \sqrt{7} \approx 3.646$.

The solution set of the original inequality is the union of the two inequality solution sets:

$$
x \in (-\infty, 1 - \sqrt{7}) \cup (0, 2) \cup (1 + \sqrt{7}, \infty)
$$

---

**Example 12**: Solve $|2x^2 + x - 1| \le 5$.

**Solution**:

From $-5 \le 2x^2 + x - 1 \le 5$.

**Left inequality**: $2x^2 + x - 1 \ge -5$

$$
2x^2 + x + 4 \ge 0
$$

Discriminant $\Delta = 1 - 32 = -31 < 0$, coefficient of $x^2$ is $2 > 0$, always true.

**Right inequality**: $2x^2 + x - 1 \le 5$

$$
2x^2 + x - 6 \le 0
$$

Solve $2x^2 + x - 6 = 0$:

$$
x = \frac{-1 \pm \sqrt{1 + 48}}{4} = \frac{-1 \pm \sqrt{49}}{4} = \frac{-1 \pm 7}{4}
$$

$$
x = \frac{6}{4} = \frac{3}{2} \quad \text{or} \quad x = \frac{-8}{4} = -2
$$

The coefficient of $x^2$ is $2 > 0$, so $2x^2 + x - 6 \le 0$ holds for:

$$
-2 \le x \le \frac{3}{2}
$$

Therefore the solution set is $x \in \left[-2, \frac{3}{2}\right]$.

---

## 4.3 Substitution to Reduce to a Quadratic Equation

Some equations do not initially look like quadratic equations, but through clever **substitution** they can be transformed into familiar quadratic equations. The core of the substitution method is identifying a repeated structure in the expression, letting $u$ represent it, thereby simplifying the original equation.

### 4.3.1 Exponential Substitution

Equations of the form $a^{2x} + b \cdot a^x + c = 0$ can be solved by letting $u = a^x$ ($u > 0$), then $a^{2x} = (a^x)^2 = u^2$.

For equations like $3e^x = 12 - 5e^{-x}$, multiply both sides by $e^x$ and then let $u = e^x$.

---

**Example 1**: Solve $4^x - 5 \cdot 2^x + 4 = 0$.

**Solution**:

Note that $4^x = (2^2)^x = (2^x)^2$. Let $u = 2^x > 0$, then:

$$
u^2 - 5u + 4 = 0
$$

$$
(u - 1)(u - 4) = 0
$$

$$
u = 1 \quad \text{or} \quad u = 4
$$

Back-substitute $u = 2^x$:

- $2^x = 1 \Rightarrow x = 0$ (since $2^0 = 1$)
- $2^x = 4 \Rightarrow x = 2$ (since $2^2 = 4$)

Therefore the solutions are $x = 0$ and $x = 2$.

---

**Example 2**: Solve $2e^x = 7 - 3e^{-x}$.

**Solution**:

Multiply both sides by $e^x$ ($e^x > 0$, so no extraneous roots are introduced):

$$
2e^{2x} = 7e^x - 3
$$

$$
2e^{2x} - 7e^x + 3 = 0
$$

Let $u = e^x > 0$, then:

$$
2u^2 - 7u + 3 = 0
$$

$$
(2u - 1)(u - 3) = 0
$$

$$
u = \frac{1}{2} \quad \text{or} \quad u = 3
$$

Back-substitute $u = e^x$:

- $e^x = \frac{1}{2} \Rightarrow x = \ln \frac{1}{2} = -\ln 2$
- $e^x = 3 \Rightarrow x = \ln 3$

Therefore the solutions are $x = -\ln 2$ and $x = \ln 3$.

---

**Example 3**: Solve $3^{2x+1} - 10 \cdot 3^x + 3 = 0$.

**Solution**:

Note that $3^{2x+1} = 3 \cdot 3^{2x} = 3(3^x)^2$. Let $u = 3^x > 0$, then:

$$
3u^2 - 10u + 3 = 0
$$

$$
(3u - 1)(u - 3) = 0
$$

$$
u = \frac{1}{3} \quad \text{or} \quad u = 3
$$

Back-substitute $u = 3^x$:

- $3^x = \frac{1}{3} = 3^{-1} \Rightarrow x = -1$
- $3^x = 3 \Rightarrow x = 1$

Therefore the solutions are $x = -1$ and $x = 1$.

---

### 4.3.2 Logarithmic Substitution

Equations of the form $(\ln x)^2 + a \ln x + b = 0$ or $2(\ln 5x)^2 + \ln 5x - 6 = 0$ can be solved by letting $u = \ln(g(x))$.

---

**Example 4**: Solve $(\ln x)^2 - 3\ln x + 2 = 0$.

**Solution**:

Let $u = \ln x$, then:

$$
u^2 - 3u + 2 = 0
$$

$$
(u - 1)(u - 2) = 0
$$

$$
u = 1 \quad \text{or} \quad u = 2
$$

Back-substitute $u = \ln x$:

- $\ln x = 1 \Rightarrow x = e^1 = e$
- $\ln x = 2 \Rightarrow x = e^2$

Therefore the solutions are $x = e$ and $x = e^2$.

---

**Example 5**: Solve $2(\ln 5x)^2 + \ln 5x - 6 = 0$.

**Solution**:

Let $u = \ln 5x$, then:

$$
2u^2 + u - 6 = 0
$$

Factorise:

$$
2u^2 + 4u - 3u - 6 = 0
$$

$$
2u(u + 2) - 3(u + 2) = 0
$$

$$
(u + 2)(2u - 3) = 0
$$

$$
u = -2 \quad \text{or} \quad u = \frac{3}{2}
$$

Back-substitute $u = \ln 5x$:

- $\ln 5x = -2 \Rightarrow 5x = e^{-2} \Rightarrow x = \frac{1}{5}e^{-2}$
- $\ln 5x = \frac{3}{2} \Rightarrow 5x = e^{3/2} \Rightarrow x = \frac{1}{5}e^{3/2}$

Therefore the solutions are $x = \frac{1}{5}e^{-2}$ and $x = \frac{1}{5}e^{3/2}$.

---

**Example 6**: Solve $\log_3 x + \log_x 3 = 2$.

**Solution**:

Use the change of base formula: $\log_x 3 = \frac{\log_3 3}{\log_3 x} = \frac{1}{\log_3 x}$.

Let $u = \log_3 x$ (note $x > 0$ and $x \neq 1$, so $u \neq 0$), then:

$$
u + \frac{1}{u} = 2
$$

$$
u^2 + 1 = 2u
$$

$$
u^2 - 2u + 1 = 0
$$

$$
(u - 1)^2 = 0
$$

$$
u = 1
$$

Back-substitute: $\log_3 x = 1 \Rightarrow x = 3^1 = 3$.

Verification: $\log_3 3 + \log_3 3 = 1 + 1 = 2$ ✓.

---

### 4.3.3 Radical Substitution

For equations of the form $x - 6\sqrt{x} + 8 = 0$, let $u = \sqrt{x}$ ($u \ge 0$), then $x = u^2$.

More generally, for equations like $x^{\frac{2}{3}} - 4x^{\frac{1}{3}} + 2 = 0$, let $u = x^{\frac{1}{3}}$, then $x^{\frac{2}{3}} = u^2$.

---

**Example 7**: Solve $x - 7\sqrt{x} + 12 = 0$.

**Solution**:

Let $u = \sqrt{x} \ge 0$, then $x = u^2$.

$$
u^2 - 7u + 12 = 0
$$

$$
(u - 3)(u - 4) = 0
$$

$$
u = 3 \quad \text{or} \quad u = 4
$$

Back-substitute $u = \sqrt{x}$:

- $\sqrt{x} = 3 \Rightarrow x = 9$
- $\sqrt{x} = 4 \Rightarrow x = 16$

Verification: $9 - 7\sqrt{9} + 12 = 9 - 21 + 12 = 0$ ✓, $16 - 7\sqrt{16} + 12 = 16 - 28 + 12 = 0$ ✓.

---

**Example 8**: Solve $x^{\frac{2}{3}} - 4x^{\frac{1}{3}} + 3 = 0$.

**Solution**:

Let $u = x^{\frac{1}{3}}$, then $x^{\frac{2}{3}} = u^2$.

$$
u^2 - 4u + 3 = 0
$$

$$
(u - 1)(u - 3) = 0
$$

$$
u = 1 \quad \text{or} \quad u = 3
$$

Back-substitute $u = x^{\frac{1}{3}}$:

- $x^{\frac{1}{3}} = 1 \Rightarrow x = 1^3 = 1$
- $x^{\frac{1}{3}} = 3 \Rightarrow x = 3^3 = 27$

Verification: $1^{\frac{2}{3}} - 4(1)^{\frac{1}{3}} + 3 = 1 - 4 + 3 = 0$ ✓, $27^{\frac{2}{3}} - 4(27)^{\frac{1}{3}} + 3 = 9 - 12 + 3 = 0$ ✓.

---

**Example 9**: Solve $2x + 3\sqrt{x} - 2 = 0$.

**Solution**:

Let $u = \sqrt{x} \ge 0$, then $x = u^2$.

$$
2u^2 + 3u - 2 = 0
$$

$$
(2u - 1)(u + 2) = 0
$$

$$
u = \frac{1}{2} \quad \text{or} \quad u = -2
$$

$u = \sqrt{x} \ge 0$, so $u = -2$ is invalid.

Back-substitute: $\sqrt{x} = \frac{1}{2} \Rightarrow x = \frac{1}{4}$.

Verification: $2(\frac{1}{4}) + 3\sqrt{\frac{1}{4}} - 2 = \frac{1}{2} + \frac{3}{2} - 2 = 0$ ✓.

---

### 4.3.4 Fraction Substitution

For equations of the form $x^2 + \frac{1}{x^2} + a\left(x + \frac{1}{x}\right) + b = 0$, use the relationship $(x + \frac{1}{x})^2 = x^2 + 2 + \frac{1}{x^2}$ and let $u = x + \frac{1}{x}$.

---

**Example 10**: Solve $x^2 + \frac{1}{x^2} - 5\left(x + \frac{1}{x}\right) + 6 = 0$.

**Solution**:

Let $u = x + \frac{1}{x}$, then $u^2 = x^2 + 2 + \frac{1}{x^2}$, so $x^2 + \frac{1}{x^2} = u^2 - 2$.

The original equation becomes:

$$
(u^2 - 2) - 5u + 6 = 0
$$

$$
u^2 - 5u + 4 = 0
$$

$$
(u - 1)(u - 4) = 0
$$

$$
u = 1 \quad \text{or} \quad u = 4
$$

**Back-substitute $u = 1$**: $x + \frac{1}{x} = 1$

Multiply both sides by $x$ ($x \neq 0$): $x^2 + 1 = x \Rightarrow x^2 - x + 1 = 0$.

Discriminant $\Delta = 1 - 4 = -3 < 0$, no real solutions.

**Back-substitute $u = 4$**: $x + \frac{1}{x} = 4$

$$
x^2 + 1 = 4x \Rightarrow x^2 - 4x + 1 = 0
$$

$$
x = \frac{4 \pm \sqrt{16 - 4}}{2} = \frac{4 \pm \sqrt{12}}{2} = \frac{4 \pm 2\sqrt{3}}{2} = 2 \pm \sqrt{3}
$$

Therefore the solutions are $x = 2 + \sqrt{3}$ and $x = 2 - \sqrt{3}$.

---

### 4.3.5 Trigonometric Substitution (Using Identities)

For equations of the form $\sin^2 x + \sin x - 2 = 0$, let $u = \sin x$, but note the domain restriction $u \in [-1, 1]$.

---

**Example 11**: Solve $2\cos^2 x + 3\sin x - 3 = 0$, $x \in [0, 2\pi)$.

**Solution**:

Use the identity $\cos^2 x = 1 - \sin^2 x$:

$$
2(1 - \sin^2 x) + 3\sin x - 3 = 0
$$

$$
2 - 2\sin^2 x + 3\sin x - 3 = 0
$$

$$
-2\sin^2 x + 3\sin x - 1 = 0
$$

Multiply by $-1$:

$$
2\sin^2 x - 3\sin x + 1 = 0
$$

Let $u = \sin x$, $u \in [-1, 1]$:

$$
2u^2 - 3u + 1 = 0
$$

$$
(2u - 1)(u - 1) = 0
$$

$$
u = \frac{1}{2} \quad \text{or} \quad u = 1
$$

Back-substitute:

- $\sin x = \frac{1}{2}$: on $[0, 2\pi)$, $x = \frac{\pi}{6}$ or $x = \frac{5\pi}{6}$
- $\sin x = 1$: on $[0, 2\pi)$, $x = \frac{\pi}{2}$

Therefore the solutions are $x = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}$.

---

## 4.4 Cubic Polynomial Graphs and Inequalities

### 4.4.1 Graph Features of Products of Three Linear Factors

A cubic polynomial $f(x) = (x - a)(x - b)(x - c)$ (where $a < b < c$) has the following graph features:

- **$x$-intercepts**: $x = a, x = b, x = c$ (three real roots)
- **End behaviour**: If the leading coefficient is positive, as $x \to \infty$, $f(x) \to \infty$; as $x \to -\infty$, $f(x) \to -\infty$
- **Graph shape**: Enters from the third quadrant, crosses through $x = a, x = b, x = c$ in sequence, and enters the first quadrant
- **Sign in each interval**:

| Interval | $(-\infty, a)$ | $(a, b)$ | $(b, c)$ | $(c, \infty)$ |
|------|--------|--------|--------|--------|
| $(x-a)$ | − | + | + | + |
| $(x-b)$ | − | − | + | + |
| $(x-c)$ | − | − | − | + |
| $f(x)$ sign | − | + | − | + |

---

**Example 1**: Sketch the graph of $f(x) = (x + 2)(x - 1)(x - 3)$.

**Solution**:

**$x$-intercepts**: $f(x) = 0 \Rightarrow x = -2, 1, 3$

**$y$-intercept**: $f(0) = (0 + 2)(0 - 1)(0 - 3) = 2 \times (-1) \times (-3) = 6$, point $(0, 6)$

**End behaviour**: Expanding, the leading term is $x^3$, coefficient positive. As $x \to -\infty$, $f(x) \to -\infty$; as $x \to \infty$, $f(x) \to \infty$.

**Sign table**:

| Interval | $(-\infty, -2)$ | $(-2, 1)$ | $(1, 3)$ | $(3, \infty)$ |
|------|-------|-------|-------|-------|
| $f(x)$ | − | + | − | + |

The graph enters from the third quadrant, crosses the $x$-axis at $x = -2$ going upward, passes through $(0, 6)$, crosses the $x$-axis at $x = 1$ going downward, reaches a local minimum, then rises to cross the $x$-axis for the third time at $x = 3$, and finally extends to the top-right.

---

**Example 2**: Sketch the graph of $f(x) = (2x - 1)(x + 1)(x - 2)$.

**Solution**:

**$x$-intercepts**: $(2x - 1)(x + 1)(x - 2) = 0 \Rightarrow x = \frac{1}{2}, -1, 2$

In order: $x = -1, \frac{1}{2}, 2$

**$y$-intercept**: $f(0) = (0 - 1)(0 + 1)(0 - 2) = (-1) \times 1 \times (-2) = 2$, point $(0, 2)$

**End behaviour**: Leading term is $2x \cdot x \cdot x = 2x^3$, coefficient positive ($2 > 0$).

**Sign table**:

| Interval | $(-\infty, -1)$ | $(-1, \frac{1}{2})$ | $(\frac{1}{2}, 2)$ | $(2, \infty)$ |
|------|---------|-------------|------------|--------|
| $(2x-1)$ | − | − | + | + |
| $(x+1)$ | − | + | + | + |
| $(x-2)$ | − | − | − | + |
| $f(x)$ | − | + | − | + |

---

**Example 3**: Sketch the graph of $f(x) = -(x + 3)(x - 1)(x - 4)$.

**Solution**:

Note the leading coefficient is negative: $-(x)(x)(x) = -x^3$. $x$-intercepts are $-3, 1, 4$.

**End behaviour**: As $x \to -\infty$, $f(x) \to \infty$ (because a negative cubic term means it enters from the second quadrant); as $x \to \infty$, $f(x) \to -\infty$.

**$y$-intercept**: $f(0) = -(3)(-1)(-4) = -(3)(-1)(-4) = -(12) = -12$, point $(0, -12)$

**Sign table**:

| Interval | $(-\infty, -3)$ | $(-3, 1)$ | $(1, 4)$ | $(4, \infty)$ |
|------|---------|--------|--------|--------|
| $-(x+3)$ | + (neg × neg) | − (neg × pos) | − | − |
| $(x-1)$ | − | − | + | + |
| $(x-4)$ | − | − | − | + |
| $f(x)$ | + | − | + | − |

---

### 4.4.2 Graphs of Absolute Value Cubic Functions $y = |f(x)|$

The graph of $y = |f(x)|$ is obtained by reflecting the parts of $y = f(x)$ that lie below the $x$-axis upward about the $x$-axis:

$$
|f(x)| = \begin{cases}
f(x), & f(x) \ge 0 \\
-f(x), & f(x) < 0
\end{cases}
$$

---

**Example 4**: Sketch the graph of $y = |(x + 2)(x - 1)(x - 3)|$.

**Solution**:

First sketch the graph of $f(x) = (x + 2)(x - 1)(x - 3)$.

$f(x)$ is negative on the intervals $(-\infty, -2)$ and $(1, 3)$.

Reflect these parts upward about the $x$-axis.

Final graph features:
- $x$-intercepts remain the same: $x = -2, 1, 3$ (at these points the graph "touches" the $x$-axis but does not cross)
- The entire graph lies above or on the $x$-axis
- The troughs on $(-\infty, -2)$ and $(1, 3)$ become peaks
- The peak on $(-2, 1)$ remains above

---

**Example 5**: Sketch the graph of $y = |(x - 1)(x - 2)(x - 4)|$ and label the axis intercepts.

**Solution**:

$f(x) = (x - 1)(x - 2)(x - 4)$ has $x$-intercepts at $1, 2, 4$.

Sign of $f(x)$:

| Interval | $(-\infty, 1)$ | $(1, 2)$ | $(2, 4)$ | $(4, \infty)$ |
|------|-------|-------|-------|-------|
| $f(x)$ | − | + | − | + |

$f(x)$ is negative on $(-\infty, 1)$ and $(2, 4)$. Reflect these parts upward.

$y$-intercept: $|f(0)| = |(-1)(-2)(-4)| = |-8| = 8$, point $(0, 8)$.

---

**Example 6**: Discuss how the number of solutions of $|(x + 1)(x - 2)(x - 5)| = k$ ($k > 0$) varies with $k$.

**Solution**:

Sketch the graph of $y = |(x + 1)(x - 2)(x - 5)|$. $x$-intercepts are $-1, 2, 5$.

Sign of $f(x) = (x + 1)(x - 2)(x - 5)$:

| Interval | $(-\infty, -1)$ | $(-1, 2)$ | $(2, 5)$ | $(5, \infty)$ |
|------|--------|--------|--------|--------|
| $f(x)$ | − | + | − | + |

Negative intervals (reflected upward): $(-\infty, -1)$ and $(2, 5)$.

Let $M_1$ be the maximum value of $f(x)$ on $(-1, 2)$, and $M_2$ be the maximum value of $|f(x)|$ on $(2, 5)$ (i.e., the absolute value of the minimum of $f(x)$ on $(2,5)$).

- If $0 < k < \min(M_1, M_2)$: 6 solutions (6 intersections of the horizontal line with the graph)
- If $k = M_1$ or $k = M_2$: some intersections coincide, the number of solutions decreases
- If $k > \max(M_1, M_2)$: 2 solutions

> **Note**: This type of problem usually appears in more difficult questions and requires combining derivatives to find local extreme values.

---

### 4.4.3 Graphical Solution of Cubic Inequalities

For $f(x) \ge d$ (or $>, \le, <$), where $f(x)$ is the product of three linear factors:

**Graphical solution steps**:

1. Sketch the graph of $y = f(x)$ (label the three $x$-intercepts and the $y$-intercept)
2. Draw the horizontal line $y = d$
3. Find the intervals where $f(x)$ is above the line (for $f(x) > d$) or below the line (for $f(x) < d$)
4. Find the intersection points if necessary

---

**Example 7**: Solve $(x + 1)(x - 2)(x - 4) \ge 0$.

**Solution**:

$f(x) = (x + 1)(x - 2)(x - 4)$, $d = 0$ (i.e., comparing with the $x$-axis).

The three roots are $-1, 2, 4$, and the leading coefficient is positive.

Sign table:

| Interval | $(-\infty, -1)$ | $(-1, 2)$ | $(2, 4)$ | $(4, \infty)$ |
|------|---------|--------|--------|--------|
| $f(x)$ | − | + | − | + |

$f(x) \ge 0$ holds for $x \in [-1, 2] \cup [4, \infty)$.

---

**Example 8**: Solve $(x - 1)(x - 3)(x - 5) < 0$.

**Solution**:

The three roots are $1, 3, 5$, and the leading coefficient is positive.

Sign table:

| Interval | $(-\infty, 1)$ | $(1, 3)$ | $(3, 5)$ | $(5, \infty)$ |
|------|------|------|------|------|
| $f(x)$ | − | + | − | + |

$f(x) < 0$ holds for $x \in (-\infty, 1) \cup (3, 5)$.

---

**Example 9**: Given $f(x) = (2x + 1)(x - 2)(x - 3)$, solve $f(x) \le 0$.

**Solution**:

Zeros: $2x + 1 = 0 \Rightarrow x = -\frac{1}{2}$, and $x = 2, x = 3$.

In order: $-\frac{1}{2}, 2, 3$.

Leading coefficient: $2x \cdot x \cdot x = 2x^3$, coefficient positive.

Sign table:

| Interval | $(-\infty, -\frac{1}{2})$ | $(-\frac{1}{2}, 2)$ | $(2, 3)$ | $(3, \infty)$ |
|------|-------------|-----------|--------|--------|
| $(2x+1)$ | − | + | + | + |
| $(x-2)$ | − | − | + | + |
| $(x-3)$ | − | − | − | + |
| $f(x)$ | − | + | − | + |

$f(x) \le 0$ holds for $x \in (-\infty, -\frac{1}{2}] \cup [2, 3]$.

---

## 4.5 Simultaneous Equations

### 4.5.1 Graphical Meaning of Simultaneous Equations

The solution to two simultaneous equations $\begin{cases} y = f(x) \\ y = g(x) \end{cases}$ is the coordinates of the **intersection points** of the two function graphs.

### 4.5.2 Line with Line

The most common methods for solving systems of two linear equations are **elimination** and **substitution**.

---

**Example 1**: Solve $\begin{cases} 3x + 2y = 7 \\ 5x - 3y = 37 \end{cases}$.

**Solution (Elimination method)**:

Multiply the first equation by $3$ and the second by $2$:

$$
\begin{cases}
9x + 6y = 21 \\
10x - 6y = 74
\end{cases}
$$

Adding: $19x = 95 \Rightarrow x = 5$

Substitute into the first equation: $3(5) + 2y = 7 \Rightarrow 15 + 2y = 7 \Rightarrow 2y = -8 \Rightarrow y = -4$

Therefore the solution is $(x, y) = (5, -4)$.

---

**Example 2**: Solve $\begin{cases} 2x - 5y = 3 \\ 4x + y = 17 \end{cases}$.

**Solution (Substitution method)**:

From the second equation: $y = 17 - 4x$.

Substitute into the first equation:

$$
2x - 5(17 - 4x) = 3
$$

$$
2x - 85 + 20x = 3
$$

$$
22x = 88
$$

$$
x = 4
$$

Substitute back: $y = 17 - 4(4) = 1$

Therefore the solution is $(x, y) = (4, 1)$.

---

**Example 3**: Solve $\begin{cases} \dfrac{x}{2} + \dfrac{y}{3} = 4 \\ \dfrac{x}{4} - \dfrac{y}{2} = 0 \end{cases}$.

**Solution**:

First clear denominators. Multiply the first equation by $6$ and the second by $4$:

$$
\begin{cases}
3x + 2y = 24 \\
x - 2y = 0
\end{cases}
$$

Adding the two equations: $4x = 24 \Rightarrow x = 6$

Substitute into $x - 2y = 0 \Rightarrow 6 - 2y = 0 \Rightarrow y = 3$

Therefore the solution is $(x, y) = (6, 3)$.

---

### 4.5.3 Line with Curve

The general method is **substitution**: solve for one variable from the linear equation and substitute into the quadratic equation, obtaining a quadratic equation in one variable. The discriminant $\Delta$ determines the number of intersection points:

- $\Delta > 0$: Two distinct intersection points (intersect at two points)
- $\Delta = 0$: One intersection point (tangent)
- $\Delta < 0$: No intersection points (do not meet)

---

**Example 4**: Find the intersection points of the line $y = 2x - 1$ and the curve $y = x^2 - 2x + 2$.

**Solution**:

Set $2x - 1 = x^2 - 2x + 2$:

$$
0 = x^2 - 4x + 3
$$

$$
(x - 1)(x - 3) = 0
$$

$$
x = 1 \quad \text{or} \quad x = 3
$$

Substitute into $y = 2x - 1$:

- $x = 1$: $y = 1$, intersection point $(1, 1)$
- $x = 3$: $y = 5$, intersection point $(3, 5)$

---

**Example 5**: Find the value of $k$ such that the line $y = 3x + k$ is tangent to the curve $y = x^2 - 4x + 7$.

**Solution**:

Set $3x + k = x^2 - 4x + 7$:

$$
0 = x^2 - 7x + 7 - k
$$

Tangency condition: $\Delta = 0$

$$
\Delta = (-7)^2 - 4(1)(7 - k) = 49 - 28 + 4k = 21 + 4k = 0
$$

$$
k = -\frac{21}{4}
$$

When $k = -\frac{21}{4}$, the line is tangent to the curve.

Point of tangency: $x^2 - 7x + 7 - (-\frac{21}{4}) = x^2 - 7x + 7 + \frac{21}{4} = x^2 - 7x + \frac{49}{4} = (x - \frac{7}{2})^2 = 0$

So $x = \frac{7}{2}$, $y = 3(\frac{7}{2}) - \frac{21}{4} = \frac{42}{4} - \frac{21}{4} = \frac{21}{4}$.

The point of tangency is $(\frac{7}{2}, \frac{21}{4})$.

---

**Example 6**: Determine the relative position of the line $y = 2x + 5$ and the circle $x^2 + (y - 1)^2 = 5$.

**Solution**:

Substitute $y = 2x + 5$:

$$
x^2 + (2x + 5 - 1)^2 = 5
$$

$$
x^2 + (2x + 4)^2 = 5
$$

$$
x^2 + 4x^2 + 16x + 16 = 5
$$

$$
5x^2 + 16x + 11 = 0
$$

Discriminant $\Delta = 16^2 - 4(5)(11) = 256 - 220 = 36 > 0$

Therefore the line intersects the circle at two distinct points.

Solve $5x^2 + 16x + 11 = 0$:

$$
x = \frac{-16 \pm \sqrt{36}}{10} = \frac{-16 \pm 6}{10}
$$

$$
x = -1 \quad \text{or} \quad x = -\frac{11}{5}
$$

Corresponding $y = 2(-1) + 5 = 3$ and $y = 2(-\frac{11}{5}) + 5 = -\frac{22}{5} + 5 = \frac{3}{5}$.

The intersection points are $(-1, 3)$ and $(-\frac{11}{5}, \frac{3}{5})$.

---

### 4.5.4 Curve with Curve

When both equations are quadratic (or of higher degree), substituting may yield a higher-degree equation, but it can usually be simplified through factorisation or clever substitution.

---

**Example 7**: Solve $\begin{cases} x^2 + y^2 = 10 \\ y = 3x \end{cases}$.

**Solution**:

Substitute $y = 3x$ into the circle equation:

$$
x^2 + (3x)^2 = 10
$$

$$
x^2 + 9x^2 = 10
$$

$$
10x^2 = 10
$$

$$
x^2 = 1
$$

$$
x = \pm 1
$$

Corresponding $y = 3(\pm 1) = \pm 3$.

Solutions: $(1, 3)$ and $(-1, -3)$.

---

**Example 8**: Solve $\begin{cases} x^2 + y^2 = 41 \\ xy = 20 \end{cases}$.

**Solution**:

From $xy = 20$, $y = \frac{20}{x}$ ($x \neq 0$). Substitute into the first equation:

$$
x^2 + \left(\frac{20}{x}\right)^2 = 41
$$

$$
x^2 + \frac{400}{x^2} = 41
$$

Multiply both sides by $x^2$:

$$
x^4 + 400 = 41x^2
$$

$$
x^4 - 41x^2 + 400 = 0
$$

Let $u = x^2 \ge 0$:

$$
u^2 - 41u + 400 = 0
$$

$$
(u - 16)(u - 25) = 0
$$

$$
u = 16 \quad \text{or} \quad u = 25
$$

$x^2 = 16 \Rightarrow x = \pm 4$, corresponding $y = \frac{20}{\pm 4} = \pm 5$

$x^2 = 25 \Rightarrow x = \pm 5$, corresponding $y = \frac{20}{\pm 5} = \pm 4$

Therefore the solutions are $(4, 5)$, $(-4, -5)$, $(5, 4)$, $(-5, -4)$.

---

**Example 9**: Solve $\begin{cases} y - x + 3 = 0 \\ x^2 - 3xy + y^2 + 19 = 0 \end{cases}$.

**Solution**:

From the first equation: $y = x - 3$.

Substitute into the second equation:

$$
x^2 - 3x(x - 3) + (x - 3)^2 + 19 = 0
$$

$$
x^2 - 3x^2 + 9x + x^2 - 6x + 9 + 19 = 0
$$

$$
-x^2 + 3x + 28 = 0
$$

Multiply by $-1$:

$$
x^2 - 3x - 28 = 0
$$

$$
(x - 7)(x + 4) = 0
$$

$$
x = 7 \quad \text{or} \quad x = -4
$$

Corresponding $y = 7 - 3 = 4$ and $y = -4 - 3 = -7$.

Solutions: $(7, 4)$ and $(-4, -7)$.

---

## Practice Problems

### Group A: Absolute Value Equations

**A1**: Solve $|4x - 3| = 9$.
**A2**: Solve $|5 - 3x| = 7$.
**A3**: Solve $|2x + 1| = x + 5$.
**A4**: Solve $|x - 4| = 2x - 5$.
**A5**: Solve $|3x + 2| = |x - 6|$.
**A6**: Solve $|2x - 5| = |4x + 3|$.
**A7**: Solve $|x^2 - 5x + 6| = 2$.
**A8**: Solve $|x^2 - 2x - 3| = 3$.

---

### Group B: Absolute Value Inequalities

**B1**: Solve $|3x + 1| > 7$.
**B2**: Solve $2|5 - x| \le 8$.
**B3**: Solve $|2x - 3| \le |x + 2|$.
**B4**: Solve $2|x + 1| > |3x - 2|$.
**B5**: Solve $|x + 1| \le 2x + 3$.
**B6**: Solve $|2x - 3| > x + 1$.
**B7**: Solve $|x^2 - 4| \le 5$.
**B8**: Solve $|x^2 - 3x| > 2$.

---

### Group C: Substitution Method

**C1**: Solve $2^{2x} - 6 \cdot 2^x + 8 = 0$.
**C2**: Solve $e^{2x} - 5e^x + 6 = 0$.
**C3**: Solve $5e^x = 8 - 3e^{-x}$.
**C4**: Solve $(\ln x)^2 + \ln x - 6 = 0$.
**C5**: Solve $2(\log_3 x)^2 - 5\log_3 x + 2 = 0$.
**C6**: Solve $x - 6\sqrt{x} + 5 = 0$.
**C7**: Solve $x^{\frac{2}{3}} - 2x^{\frac{1}{3}} - 3 = 0$.
**C8**: Solve $x^2 + \frac{1}{x^2} - 3\left(x + \frac{1}{x}\right) + 2 = 0$.

---

### Group D: Cubic Polynomial Graphs and Inequalities

**D1**: Sketch the graph of $f(x) = (x + 3)(x - 2)(x - 5)$, labelling the axis intercepts.
**D2**: Sketch the graph of $f(x) = (2x + 3)(x - 1)(x - 4)$.
**D3**: Sketch the graph of $y = |(x + 3)(x - 2)(x - 5)|$.
**D4**: Solve $(x + 2)(x - 1)(x - 4) \ge 0$.
**D5**: Solve $(x - 1)(x - 3)(x - 6) < 0$.
**D6**: Given $f(x) = (x + 1)(x - 2)(x - 5)$, solve $f(x) \le 0$.

---

### Group E: Simultaneous Equations

**E1**: Solve $\begin{cases} 2x + 3y = 8 \\ 5x - 2y = 1 \end{cases}$.
**E2**: Solve $\begin{cases} 4x - 3y = 11 \\ 3x + 2y = 21 \end{cases}$.
**E3**: Find the intersection points of the line $y = 3x - 2$ and the parabola $y = x^2$.
**E4**: Find the intersection points of the line $y = 2x + 1$ and the curve $y = x^2 - 3x + 5$.
**E5**: Find the value of $k$ such that the line $y = x + k$ is tangent to the curve $y = x^2 - 5x + 7$.
**E6**: Solve $\begin{cases} x^2 + y^2 = 13 \\ y = 2x - 1 \end{cases}$.
**E7**: Solve $\begin{cases} x^2 + y^2 = 25 \\ xy = 12 \end{cases}$.
**E8**: Solve $\begin{cases} x^2 - 2xy + y^2 = 1 \\ x + y = 3 \end{cases}$.

---

## Answers to Practice Problems

### Group A Answers

**A1**: $|4x - 3| = 9$
$4x - 3 = 9$ or $4x - 3 = -9$
$4x = 12$ or $4x = -6$
$x = 3$ or $x = -\frac{3}{2}$

**A2**: $|5 - 3x| = 7$
$5 - 3x = 7$ or $5 - 3x = -7$
$-3x = 2$ or $-3x = -12$
$x = -\frac{2}{3}$ or $x = 4$

**A3**: $|2x + 1| = x + 5$
Case 1 ($x \ge -\frac{1}{2}$): $2x + 1 = x + 5 \Rightarrow x = 4$ ✓
Case 2 ($x < -\frac{1}{2}$): $-(2x + 1) = x + 5 \Rightarrow -2x - 1 = x + 5 \Rightarrow -3x = 6 \Rightarrow x = -2$ ✓
Solutions: $x = 4$ and $x = -2$

**A4**: $|x - 4| = 2x - 5$
Case 1 ($x \ge 4$): $x - 4 = 2x - 5 \Rightarrow -x = -1 \Rightarrow x = 1$, but $1 \ge 4$ is false ✗
Case 2 ($x < 4$): $-(x - 4) = 2x - 5 \Rightarrow -x + 4 = 2x - 5 \Rightarrow 9 = 3x \Rightarrow x = 3$, $3 < 4$ ✓
Solution: $x = 3$

**A5**: $|3x + 2| = |x - 6|$
$3x + 2 = x - 6$ or $3x + 2 = -(x - 6)$
$2x = -8$ or $3x + 2 = -x + 6$
$x = -4$ or $4x = 4$
$x = -4$ or $x = 1$

**A6**: $|2x - 5| = |4x + 3|$
$2x - 5 = 4x + 3$ or $2x - 5 = -(4x + 3)$
$-2x = 8$ or $2x - 5 = -4x - 3$
$x = -4$ or $6x = 2$
$x = -4$ or $x = \frac{1}{3}$

**A7**: $|x^2 - 5x + 6| = 2$
$x^2 - 5x + 6 = 2$ or $x^2 - 5x + 6 = -2$
$x^2 - 5x + 4 = 0$ or $x^2 - 5x + 8 = 0$
$(x - 1)(x - 4) = 0$, $\Delta = 25 - 32 = -7 < 0$, no solution
$x = 1$ or $x = 4$

**A8**: $|x^2 - 2x - 3| = 3$
$x^2 - 2x - 3 = 3$ or $x^2 - 2x - 3 = -3$
$x^2 - 2x - 6 = 0$ or $x^2 - 2x = 0$
$x = \frac{2 \pm \sqrt{4 + 24}}{2} = 1 \pm \sqrt{7}$ or $x(x - 2) = 0 \Rightarrow x = 0$ or $x = 2$
Solutions: $x = 1 \pm \sqrt{7}, 0, 2$

---

### Group B Answers

**B1**: $|3x + 1| > 7$
$3x + 1 < -7$ or $3x + 1 > 7$
$3x < -8$ or $3x > 6$
$x < -\frac{8}{3}$ or $x > 2$
$x \in (-\infty, -\frac{8}{3}) \cup (2, \infty)$

**B2**: $2|5 - x| \le 8$
$|5 - x| \le 4$
$-4 \le 5 - x \le 4$
Left: $-4 \le 5 - x \Rightarrow x \le 9$
Right: $5 - x \le 4 \Rightarrow -x \le -1 \Rightarrow x \ge 1$
$x \in [1, 9]$

**B3**: $|2x - 3| \le |x + 2|$
$(2x - 3)^2 \le (x + 2)^2$
$4x^2 - 12x + 9 \le x^2 + 4x + 4$
$3x^2 - 16x + 5 \le 0$
$(3x - 1)(x - 5) \le 0$
$x \in [\frac{1}{3}, 5]$

**B4**: $2|x + 1| > |3x - 2|$
$4(x + 1)^2 > (3x - 2)^2$
$4(x^2 + 2x + 1) > 9x^2 - 12x + 4$
$4x^2 + 8x + 4 > 9x^2 - 12x + 4$
$0 > 5x^2 - 20x$
$5x^2 - 20x < 0$
$5x(x - 4) < 0$
$0 < x < 4$
$x \in (0, 4)$

**B5**: $|x + 1| \le 2x + 3$
Case 1 ($x \ge -1$): $x + 1 \le 2x + 3 \Rightarrow -2 \le x$, combined with $x \ge -1$ gives $x \ge -1$
Case 2 ($x < -1$): $-(x + 1) \le 2x + 3 \Rightarrow -x - 1 \le 2x + 3 \Rightarrow -4 \le 3x \Rightarrow x \ge -\frac{4}{3}$
Combined with $x < -1$ gives $-\frac{4}{3} \le x < -1$
Union: $x \ge -\frac{4}{3}$, i.e., $x \in [-\frac{4}{3}, \infty)$

**B6**: $|2x - 3| > x + 1$
Case 1 ($x \ge \frac{3}{2}$): $2x - 3 > x + 1 \Rightarrow x > 4$, combined gives $x > 4$
Case 2 ($x < \frac{3}{2}$): $-(2x - 3) > x + 1 \Rightarrow -2x + 3 > x + 1 \Rightarrow 2 > 3x \Rightarrow x < \frac{2}{3}$, combined gives $x < \frac{2}{3}$
$x \in (-\infty, \frac{2}{3}) \cup (4, \infty)$

**B7**: $|x^2 - 4| \le 5$
$-5 \le x^2 - 4 \le 5$
Left: $x^2 - 4 \ge -5 \Rightarrow x^2 \ge -1$, always true
Right: $x^2 - 4 \le 5 \Rightarrow x^2 \le 9 \Rightarrow -3 \le x \le 3$
$x \in [-3, 3]$

**B8**: $|x^2 - 3x| > 2$
$x^2 - 3x < -2$ or $x^2 - 3x > 2$
Inequality 1: $x^2 - 3x + 2 < 0 \Rightarrow (x - 1)(x - 2) < 0 \Rightarrow 1 < x < 2$
Inequality 2: $x^2 - 3x - 2 > 0$
$x = \frac{3 \pm \sqrt{9 + 8}}{2} = \frac{3 \pm \sqrt{17}}{2}$
$x < \frac{3 - \sqrt{17}}{2}$ or $x > \frac{3 + \sqrt{17}}{2}$
where $\frac{3 - \sqrt{17}}{2} \approx -0.562$, $\frac{3 + \sqrt{17}}{2} \approx 3.562$
Solution set: $x \in (-\infty, \frac{3 - \sqrt{17}}{2}) \cup (1, 2) \cup (\frac{3 + \sqrt{17}}{2}, \infty)$

---

### Group C Answers

**C1**: $2^{2x} - 6 \cdot 2^x + 8 = 0$
Let $u = 2^x > 0$: $u^2 - 6u + 8 = 0 \Rightarrow (u - 2)(u - 4) = 0$
$u = 2$ or $u = 4$
$2^x = 2 \Rightarrow x = 1$; $2^x = 4 \Rightarrow x = 2$

**C2**: $e^{2x} - 5e^x + 6 = 0$
Let $u = e^x > 0$: $u^2 - 5u + 6 = 0 \Rightarrow (u - 2)(u - 3) = 0$
$u = 2$ or $u = 3$
$e^x = 2 \Rightarrow x = \ln 2$; $e^x = 3 \Rightarrow x = \ln 3$

**C3**: $5e^x = 8 - 3e^{-x}$
Multiply by $e^x$: $5e^{2x} = 8e^x - 3$
$5e^{2x} - 8e^x + 3 = 0$
Let $u = e^x > 0$: $5u^2 - 8u + 3 = 0 \Rightarrow (5u - 3)(u - 1) = 0$
$u = \frac{3}{5}$ or $u = 1$
$e^x = \frac{3}{5} \Rightarrow x = \ln \frac{3}{5}$; $e^x = 1 \Rightarrow x = 0$

**C4**: $(\ln x)^2 + \ln x - 6 = 0$
Let $u = \ln x$: $u^2 + u - 6 = 0 \Rightarrow (u + 3)(u - 2) = 0$
$u = -3$ or $u = 2$
$\ln x = -3 \Rightarrow x = e^{-3}$; $\ln x = 2 \Rightarrow x = e^2$

**C5**: $2(\log_3 x)^2 - 5\log_3 x + 2 = 0$
Let $u = \log_3 x$: $2u^2 - 5u + 2 = 0 \Rightarrow (2u - 1)(u - 2) = 0$
$u = \frac{1}{2}$ or $u = 2$
$\log_3 x = \frac{1}{2} \Rightarrow x = 3^{1/2} = \sqrt{3}$; $\log_3 x = 2 \Rightarrow x = 3^2 = 9$

**C6**: $x - 6\sqrt{x} + 5 = 0$
Let $u = \sqrt{x} \ge 0$: $u^2 - 6u + 5 = 0 \Rightarrow (u - 1)(u - 5) = 0$
$u = 1$ or $u = 5$
$\sqrt{x} = 1 \Rightarrow x = 1$; $\sqrt{x} = 5 \Rightarrow x = 25$

**C7**: $x^{\frac{2}{3}} - 2x^{\frac{1}{3}} - 3 = 0$
Let $u = x^{\frac{1}{3}}$: $u^2 - 2u - 3 = 0 \Rightarrow (u - 3)(u + 1) = 0$
$u = 3$ or $u = -1$
$x^{\frac{1}{3}} = 3 \Rightarrow x = 27$; $x^{\frac{1}{3}} = -1 \Rightarrow x = -1$

**C8**: $x^2 + \frac{1}{x^2} - 3\left(x + \frac{1}{x}\right) + 2 = 0$
Let $u = x + \frac{1}{x}$, then $u^2 = x^2 + 2 + \frac{1}{x^2} \Rightarrow x^2 + \frac{1}{x^2} = u^2 - 2$
$(u^2 - 2) - 3u + 2 = 0 \Rightarrow u^2 - 3u = 0 \Rightarrow u(u - 3) = 0$
$u = 0$ or $u = 3$
$u = 0$: $x + \frac{1}{x} = 0 \Rightarrow x^2 + 1 = 0$, no real solution
$u = 3$: $x + \frac{1}{x} = 3 \Rightarrow x^2 - 3x + 1 = 0 \Rightarrow x = \frac{3 \pm \sqrt{5}}{2}$

---

### Group D Answers

**D1**: $f(x) = (x + 3)(x - 2)(x - 5)$
$x$-intercepts: $-3, 2, 5$
$y$-intercept: $f(0) = 3 \times (-2) \times (-5) = 30$, point $(0, 30)$
Leading coefficient positive. As $x \to -\infty$, $f(x) \to -\infty$; as $x \to \infty$, $f(x) \to \infty$
Sign: $(-\infty, -3)$: −; $(-3, 2)$: +; $(2, 5)$: −; $(5, \infty)$: +

**D2**: $f(x) = (2x + 3)(x - 1)(x - 4)$
$x$-intercepts: $-\frac{3}{2}, 1, 4$
$y$-intercept: $f(0) = 3 \times (-1) \times (-4) = 12$, point $(0, 12)$
Leading coefficient $2 > 0$, end behaviour same as D1.
Sign: $(-\infty, -\frac{3}{2})$: −; $(-\frac{3}{2}, 1)$: +; $(1, 4)$: −; $(4, \infty)$: +

**D3**: $y = |(x + 3)(x - 2)(x - 5)|$
Reflect the negative parts of $f(x)$ on $(-\infty, -3)$ and $(2, 5)$ upward. $x$-intercepts remain at $-3, 2, 5$. $y$-intercept is $|30| = 30$. The entire graph lies above (or on) the $x$-axis.

**D4**: $(x + 2)(x - 1)(x - 4) \ge 0$
Roots: $-2, 1, 4$, leading coefficient positive.
Sign: $(-\infty, -2)$: −; $(-2, 1)$: +; $(1, 4)$: −; $(4, \infty)$: +
Solution: $x \in [-2, 1] \cup [4, \infty)$

**D5**: $(x - 1)(x - 3)(x - 6) < 0$
Roots: $1, 3, 6$, leading coefficient positive.
Sign: $(-\infty, 1)$: −; $(1, 3)$: +; $(3, 6)$: −; $(6, \infty)$: +
Solution: $x \in (-\infty, 1) \cup (3, 6)$

**D6**: $f(x) = (x + 1)(x - 2)(x - 5) \le 0$
Roots: $-1, 2, 5$, leading coefficient positive.
Sign: $(-\infty, -1)$: −; $(-1, 2)$: +; $(2, 5)$: −; $(5, \infty)$: +
Solution: $x \in (-\infty, -1] \cup [2, 5]$

---

### Group E Answers

**E1**: $\begin{cases} 2x + 3y = 8 \\ 5x - 2y = 1 \end{cases}$
Multiply the first by $2$, the second by $3$: $\begin{cases} 4x + 6y = 16 \\ 15x - 6y = 3 \end{cases}$
Adding: $19x = 19 \Rightarrow x = 1$
Substitute: $2(1) + 3y = 8 \Rightarrow 3y = 6 \Rightarrow y = 2$
Solution: $(1, 2)$

**E2**: $\begin{cases} 4x - 3y = 11 \\ 3x + 2y = 21 \end{cases}$
Multiply the first by $2$, the second by $3$: $\begin{cases} 8x - 6y = 22 \\ 9x + 6y = 63 \end{cases}$
Adding: $17x = 85 \Rightarrow x = 5$
Substitute: $4(5) - 3y = 11 \Rightarrow 20 - 3y = 11 \Rightarrow 3y = 9 \Rightarrow y = 3$
Solution: $(5, 3)$

**E3**: $y = 3x - 2$ and $y = x^2$
$x^2 = 3x - 2 \Rightarrow x^2 - 3x + 2 = 0 \Rightarrow (x - 1)(x - 2) = 0$
$x = 1$ or $x = 2$
Intersection points: $(1, 1)$ and $(2, 4)$

**E4**: $y = 2x + 1$ and $y = x^2 - 3x + 5$
$2x + 1 = x^2 - 3x + 5 \Rightarrow 0 = x^2 - 5x + 4 \Rightarrow (x - 1)(x - 4) = 0$
$x = 1$ or $x = 4$
Intersection points: $(1, 3)$ and $(4, 9)$

**E5**: $y = x + k$ tangent to $y = x^2 - 5x + 7$
$x + k = x^2 - 5x + 7 \Rightarrow 0 = x^2 - 6x + 7 - k$
$\Delta = (-6)^2 - 4(1)(7 - k) = 36 - 28 + 4k = 8 + 4k = 0$
$k = -2$

**E6**: $\begin{cases} x^2 + y^2 = 13 \\ y = 2x - 1 \end{cases}$
Substitute: $x^2 + (2x - 1)^2 = 13 \Rightarrow x^2 + 4x^2 - 4x + 1 = 13 \Rightarrow 5x^2 - 4x - 12 = 0$
$(5x + 6)(x - 2) = 0 \Rightarrow x = -\frac{6}{5}$ or $x = 2$
$y = 2(-\frac{6}{5}) - 1 = -\frac{12}{5} - 1 = -\frac{17}{5}$; $y = 2(2) - 1 = 3$
Solutions: $(-\frac{6}{5}, -\frac{17}{5})$ and $(2, 3)$

**E7**: $\begin{cases} x^2 + y^2 = 25 \\ xy = 12 \end{cases}$
From $xy = 12$, $y = \frac{12}{x}$ ($x \neq 0$)
Substitute: $x^2 + \frac{144}{x^2} = 25 \Rightarrow x^4 - 25x^2 + 144 = 0$
Let $u = x^2 \ge 0$: $u^2 - 25u + 144 = 0 \Rightarrow (u - 9)(u - 16) = 0$
$u = 9 \Rightarrow x = \pm 3$, $y = \frac{12}{\pm 3} = \pm 4$
$u = 16 \Rightarrow x = \pm 4$, $y = \frac{12}{\pm 4} = \pm 3$
Solutions: $(3, 4)$, $(-3, -4)$, $(4, 3)$, $(-4, -3)$

**E8**: $\begin{cases} x^2 - 2xy + y^2 = 1 \\ x + y = 3 \end{cases}$
Note $x^2 - 2xy + y^2 = (x - y)^2 = 1$, so $x - y = \pm 1$
Together with $x + y = 3$:
When $x - y = 1$: $\begin{cases} x + y = 3 \\ x - y = 1 \end{cases} \Rightarrow x = 2, y = 1$
When $x - y = -1$: $\begin{cases} x + y = 3 \\ x - y = -1 \end{cases} \Rightarrow x = 1, y = 2$
Solutions: $(2, 1)$ and $(1, 2)$

---

## Chapter Summary

| Topic | Core Method | Key Points |
|--------|---------|---------|
| **Sets and intervals** | Set-builder notation, interval notation | Open intervals use round brackets, closed use square brackets; $\cup$ denotes union |
| **6.1 Absolute value equations** | Case analysis or squaring both sides | $|A| = B$ requires $B \ge 0$; $|A| = |B| \iff A = \pm B$ |
| **6.2 Absolute value inequalities** | Transform into inequality systems or square | $|A| > c \iff A < -c$ or $A > c$; $|A| \le c \iff -c \le A \le c$ |
| **6.3 Substitution method** | Identify repeated structure, let $u = g(x)$ | Check existence and domain after back-substitution (e.g., $u \ge 0$, $u \neq 0$) |
| **6.4 Cubic polynomial graphs and inequalities** | Find three $x$-intercepts, sign analysis | Leading coefficient determines end behaviour; absolute value graphs reflect negative parts upward |
| **6.5 Simultaneous equations** | Substitution + discriminant | $\Delta > 0$ two intersections, $\Delta = 0$ tangent, $\Delta < 0$ no intersection |

---
---







