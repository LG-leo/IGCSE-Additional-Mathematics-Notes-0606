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

# Chapter 3: Quadratic Functions (Including Polynomial Factors)

## Chapter Introduction

Quadratic functions are a core tool that runs throughout IGCSE Additional Mathematics (0606). From solving equations to finding extreme values, from inequalities to curve analysis, knowledge of quadratic functions is ubiquitous. This chapter organically integrates the conceptual system of quadratic functions with polynomial factorisation, forming a complete logical chain from "factors" to "functions" to "graphs."

**Syllabus Mapping**:

| Syllabus Ref | Content | Corresponding Section |
|:---:|:---|:---:|
| **3.1** | Remainder Theorem and Factor Theorem | §3.1.1, §3.1.2 |
| **3.2** | Factorising polynomials (cubic → linear × quadratic) | §3.1.3 |
| **3.3** | Solving cubic equations | §3.1.4 |
| **2.1** | Completing the square or differentiation to find stationary values of quadratic functions | §3.4, §3.7 |
| **2.2** | Using stationary values to sketch graphs or find ranges | §3.4 |
| **2.3** | Discriminant and conditions for roots, relative position of a line and a curve | §3.2 |
| **2.4** | Solving quadratic equations (factorisation, formula, completing the square) | §3.3 |
| **2.5** | Quadratic inequalities (algebraic or graphical methods) | §3.5 |
| **4.4** | Graphs of products of three linear factors and absolute value graphs | §3.6.1, §3.6.2 |
| **4.5** | Graphical solution of cubic inequalities | §3.6.3 |

---

## 3.1 Factorisation of Polynomials

### 3.1.1 The Remainder Theorem

**Statement of the Theorem**: When a polynomial $f(x)$ is divided by a linear factor $(x - a)$, the remainder is equal to $f(a)$.

**Complete Derivation**:

Let $f(x)$ be divided by $(x - a)$, yielding a quotient $q(x)$ and a remainder $R$. Since the divisor $(x - a)$ is of degree 1, the degree of the remainder $R$ must be lower than the degree of the divisor, so $R$ can only be a constant. Therefore, we have the identity:

$$
f(x) = (x - a) \cdot q(x) + R
$$

This identity holds for **all** values of $x$ — this is a fundamental property of polynomial identities.

Now, we cleverly choose to substitute $x = a$. We choose $x = a$ because it makes the factor $(x - a)$ equal to zero, thereby eliminating the term containing $q(x)$:

$$
f(a) = (a - a) \cdot q(a) + R = 0 \cdot q(a) + R = R
$$

Therefore $R = f(a)$. This is the entirety of the Remainder Theorem.

**Why is this theorem so useful?**

To find the remainder, we do not need to perform long division — we simply substitute $x = a$ into the original polynomial and evaluate. This greatly simplifies the calculation, especially when the polynomial is of a higher degree.

**Generalised Form**:

If the divisor is $(ax + b)$, then set $ax + b = 0$ to obtain $x = -\frac{b}{a}$, and the remainder is:

$$
R = f\!\left(-\frac{b}{a}\right)
$$

The reasoning is exactly the same — find the value of $x$ that makes the divisor zero, then substitute.

---

**Example 1**: Find the remainder when $f(x) = 2x^3 - 3x^2 + 4x - 5$ is divided by $x - 2$.

**Detailed solution**:

The divisor is $x - 2$; set $x - 2 = 0$ to get $x = 2$. By the Remainder Theorem, the remainder $R = f(2)$.

Substitute and calculate term by term:

$$
\begin{aligned}
f(2) &= 2(2)^3 - 3(2)^2 + 4(2) - 5 \\
&\text{(first compute powers: $2^3 = 8$, $2^2 = 4$)} \\
&= 2 \times 8 - 3 \times 4 + 8 - 5 \\
&\text{(then multiply: $2 \times 8 = 16$, $3 \times 4 = 12$)} \\
&= 16 - 12 + 8 - 5 \\
&= 7
\end{aligned}
$$

So the remainder is $7$.

---

**Example 2**: When $f(x) = x^3 + kx^2 - 2x + 3$ is divided by $x + 1$, the remainder is $5$. Find the value of the constant $k$.

**Detailed solution**:

The divisor is $x + 1$; set $x + 1 = 0$ to get $x = -1$. Note the sign: the solution of $x + 1 = 0$ is $x = -1$, not $x = 1$. This is a common mistake.

By the Remainder Theorem, the remainder equals $f(-1)$. The problem states the remainder is $5$, so $f(-1) = 5$.

Substitute and calculate:

$$
\begin{aligned}
f(-1) &= (-1)^3 + k(-1)^2 - 2(-1) + 3 = 5 \\
&\text{(compute term by term: $(-1)^3 = -1$, $(-1)^2 = 1$, $-2(-1) = 2$)} \\
-1 + k + 2 + 3 &= 5 \\
k + 4 &= 5 \\
k &= 1
\end{aligned}
$$

So $k = 1$.

---

**Example 3**: Find the remainder when $f(x) = 6x^3 + x^2 - 8x + 2$ is divided by $2x - 1$.

**Detailed solution**:

The divisor is $2x - 1$, not of the simple form $(x - a)$. Set $2x - 1 = 0$, giving $x = \frac{1}{2}$.

When substituting $x = \frac{1}{2}$, pay careful attention to the fraction arithmetic:

$$
\begin{aligned}
f\!\left(\frac{1}{2}\right) &= 6\left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^2 - 8\left(\frac{1}{2}\right) + 2 \\
&= 6 \times \frac{1}{8} + \frac{1}{4} - 4 + 2 \\
&= \frac{6}{8} + \frac{1}{4} - 2 \\
&= \frac{3}{4} + \frac{1}{4} - 2 \\
&= 1 - 2 = -1
\end{aligned}
$$

So the remainder is $-1$.

---

**Example 4**: Find the remainder when $f(x) = 4x^4 - 3x^3 + 2x^2 - x + 5$ is divided by $x - 1$.

**Detailed solution**:

Set $x - 1 = 0$ to get $x = 1$. The remainder $R = f(1)$.

$$
\begin{aligned}
f(1) &= 4(1)^4 - 3(1)^3 + 2(1)^2 - 1 + 5 \\
&= 4 - 3 + 2 - 1 + 5 \\
&= 7
\end{aligned}
$$

The remainder is $7$. Even with a higher-degree polynomial, the Remainder Theorem still applies.

---

**Example 5**: Find the remainder when $f(x) = x^4 - 2x^3 + 3x^2 - 4x + 2$ is divided by $x + 2$.

**Detailed solution**:

Set $x + 2 = 0$ to get $x = -2$.

$$
\begin{aligned}
f(-2) &= (-2)^4 - 2(-2)^3 + 3(-2)^2 - 4(-2) + 2 \\
&= 16 - 2(-8) + 3(4) + 8 + 2 \\
&= 16 + 16 + 12 + 8 + 2 \\
&= 54
\end{aligned}
$$

The remainder is $54$.

---

**Example 6**: Find the remainder when $f(x) = 8x^3 - 4x^2 + 2x - 1$ is divided by $2x + 3$.

**Detailed solution**:

Set $2x + 3 = 0$ to get $x = -\frac{3}{2}$. The remainder $R = f\!\left(-\frac{3}{2}\right)$.

$$
\begin{aligned}
f\!\left(-\frac{3}{2}\right) &= 8\left(-\frac{3}{2}\right)^3 - 4\left(-\frac{3}{2}\right)^2 + 2\left(-\frac{3}{2}\right) - 1 \\
&= 8\left(-\frac{27}{8}\right) - 4\left(\frac{9}{4}\right) - 3 - 1 \\
&= -27 - 9 - 3 - 1 = -40
\end{aligned}
$$

The remainder is $-40$.

---

### 3.1.2 The Factor Theorem

**Statement of the Theorem**: If $f(a) = 0$, then $(x - a)$ is a factor of $f(x)$. Conversely, if $(x - a)$ is a factor of $f(x)$, then $f(a) = 0$.

**Derivation**:

The Factor Theorem is a direct corollary of the Remainder Theorem. By the Remainder Theorem, the remainder when $f(x)$ is divided by $(x - a)$ equals $f(a)$. If $f(a) = 0$, this means the remainder is zero — that is, $(x - a)$ **exactly divides** $f(x)$ with no remainder, so $(x - a)$ is a factor of $f(x)$.

Conversely, if $(x - a)$ is a factor of $f(x)$, then $f(x) = (x - a) \cdot q(x)$. Substituting $x = a$ gives $f(a) = 0$.

**Practical significance**:

To determine whether $(x - a)$ is a factor of $f(x)$, we only need to check whether $f(a) = 0$. This is much faster than performing long division. Moreover, the Factor Theorem is the **starting point for factorising cubic polynomials** — by testing roots to find a zero, we have found a linear factor.

**Root-testing strategy**:

For polynomials with integer coefficients, possible rational roots are $\pm \frac{\text{factors of the constant term}}{\text{factors of the leading coefficient}}$. For cubic polynomials, we usually start by testing the simplest values: $\pm 1, \pm 2, \pm 3$.

---

**Example 1**: Show that $(x - 2)$ is a factor of $f(x) = x^3 - 3x^2 - 4x + 12$.

**Detailed solution**:

To prove that $(x - 2)$ is a factor, by the Factor Theorem, we only need to show that $f(2) = 0$.

$$
\begin{aligned}
f(2) &= 2^3 - 3(2)^2 - 4(2) + 12 \\
&= 8 - 12 - 8 + 12 = 0
\end{aligned}
$$

Since $f(2) = 0$, $(x - 2)$ is a factor of $f(x)$. ✓

---

**Example 2**: The polynomial $f(x) = 2x^3 + ax^2 + bx - 6$ has factors $(x - 1)$ and $(x + 2)$. Find the values of $a$ and $b$.

**Detailed solution**:

By the Factor Theorem:
- $(x - 1)$ is a factor $\Rightarrow$ $f(1) = 0$
- $(x + 2)$ is a factor $\Rightarrow$ $f(-2) = 0$

From $f(1) = 0$:

$$
2 + a + b - 6 = 0 \;\Rightarrow\; a + b = 4 \tag{1}
$$

From $f(-2) = 0$:

$$
-16 + 4a - 2b - 6 = 0 \;\Rightarrow\; 4a - 2b = 22 \tag{2}
$$

Solve (1) and (2) simultaneously. From (1), $b = 4 - a$. Substitute into (2):

$$
4a - 2(4 - a) = 22 \;\Rightarrow\; 4a - 8 + 2a = 22 \;\Rightarrow\; 6a = 30 \;\Rightarrow\; a = 5
$$

Therefore $b = 4 - 5 = -1$.

---

**Example 3**: Given that $x - 2$ is a factor of $f(x) = x^3 - px^2 + 5x - 2$, find the value of $p$ and fully factorise $f(x)$.

**Detailed solution**:

By the Factor Theorem, $f(2) = 0$:

$$
8 - 4p + 10 - 2 = 16 - 4p = 0 \;\Rightarrow\; p = 4
$$

So $f(x) = x^3 - 4x^2 + 5x - 2$.

Use synthetic division by $(x - 2)$:

$$
\begin{array}{r|rrrr}
2 & 1 & -4 & 5 & -2 \\
  &   & 2  & -4 & 2 \\
\hline
  & 1 & -2 & 1 & 0
\end{array}
$$

The quotient is $x^2 - 2x + 1 = (x - 1)^2$.

Therefore:

$$
\boxed{f(x) = (x - 2)(x - 1)^2}
$$

---

**Example 4**: Given that $x - 3$ is a factor of $f(x) = 2x^3 - 7x^2 + 2x + 3$, factorise $f(x)$.

**Detailed solution**:

Synthetic division:

$$
\begin{array}{r|rrrr}
3 & 2 & -7 & 2 & 3 \\
  &   & 6  & -3 & -3 \\
\hline
  & 2 & -1 & -1 & 0
\end{array}
$$

The quotient is $2x^2 - x - 1$.

Factorise the quadratic: $2x^2 - x - 1 = 2x^2 - 2x + x - 1 = 2x(x - 1) + 1(x - 1) = (2x + 1)(x - 1)$.

Therefore:

$$
\boxed{f(x) = (x - 3)(2x + 1)(x - 1)}
$$

---

**Example 5**: The polynomial $f(x) = 3x^3 + kx^2 - 4x + 4$ has a factor $(x + 1)$. Find the value of $k$.

**Detailed solution**:

$(x + 1)$ is a factor $\Rightarrow$ $f(-1) = 0$.

$$
f(-1) = -3 + k + 4 + 4 = k + 5 = 0 \;\Rightarrow\; k = -5
$$

---

**Example 6**: Given that $x - 1$ and $x - 2$ are both factors of $f(x) = x^3 + ax^2 + bx + c$, and that when $f(x)$ is divided by $x + 1$, the remainder is $-12$, find the values of $a, b, c$ and write $f(x)$ in fully factorised form.

**Detailed solution**:

From the given conditions:

$$
f(1) = 1 + a + b + c = 0 \quad\Rightarrow\quad a + b + c = -1 \tag{1}
$$

$$
f(2) = 8 + 4a + 2b + c = 0 \quad\Rightarrow\quad 4a + 2b + c = -8 \tag{2}
$$

$$
f(-1) = -1 + a - b + c = -12 \quad\Rightarrow\quad a - b + c = -11 \tag{3}
$$

Then：

$$
(2)-(1):\; 3a + b = -7 \tag{4}
$$

$$
(1)-(3):\; 2b = 10 \Rightarrow b = 5
$$

Substitute into (4): $3a + 5 = -7 \Rightarrow 3a = -12 \Rightarrow a = -4$

Substitute into (1): $-4 + 5 + c = -1 \Rightarrow c = -2$

So $f(x) = x^3 - 4x^2 + 5x - 2$.

Verification:
- $f(1) = 1 - 4 + 5 - 2 = 0$ ✓
- $f(2) = 8 - 16 + 10 - 2 = 0$ ✓
- $f(-1) = -1 - 4 - 5 - 2 = -12$ ✓

Divide by $(x - 1)$ using synthetic division:

$$
\begin{array}{r|rrrr}
1 & 1 & -4 & 5 & -2 \\
  &   & 1  & -3 & 2 \\
\hline
  & 1 & -3 & 2 & 0
\end{array}
$$

The quotient is $x^2 - 3x + 2 = (x - 1)(x - 2)$.

So $f(x) = (x - 1)^2(x - 2)$.

---

### 3.1.3 Factorising Cubic Polynomials

Factorising a cubic polynomial $f(x) = ax^3 + bx^2 + cx + d$ is like unlocking a "three-layer lock": first find a key (a linear factor), open the first lock to reveal a quadratic lock, then use familiar quadratic factorisation methods to open it.

**Standard Procedure**:

**Step 1: Test roots — Use the Factor Theorem to find a linear factor**

Test $x = \pm 1, \pm 2, \pm 3, \dots$ and fractions $\pm \frac{\text{factors of the constant term}}{\text{factors of the leading coefficient}}$. Find $p$ such that $f(p) = 0$; then $(x - p)$ is a factor.

**Step 2: Synthetic division — Find the quadratic quotient**

Divide $f(x)$ by $(x - p)$ to obtain a quadratic $Ax^2 + Bx + C$.

**Step 3: Factorise the quadratic**

Use factorisation, the quadratic formula, or completing the square to factor $Ax^2 + Bx + C$.

**Step 4: Complete factorisation**

Write $f(x) = (x - p) \times (\text{factorisation of the quadratic})$.

---

#### Detailed Explanation of Synthetic Division

Synthetic division is a concise format for polynomial division that only uses coefficients, without writing variables.

**Steps** (using $f(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0$ divided by $(x - p)$ as an example):

```
p |  a₃   a₂   a₁   a₀
  |      p·b₂ p·b₁ p·b₀
  ------------------------
     b₂   b₁   b₀   R
```

where:
- $b_2 = a_3$ (bring down the leading coefficient)
- $b_1 = a_2 + p \cdot b_2$
- $b_0 = a_1 + p \cdot b_1$
- $R = a_0 + p \cdot b_0$ (remainder)

The quotient is $b_2 x^2 + b_1 x + b_0$, and the remainder is $R$.

---

**Example 1**: Factorise $f(x) = x^3 - 6x^2 + 11x - 6$.

**Detailed solution**:

**Step 1: Test roots**. Start with the simplest value $x = 1$:

$$
f(1) = 1 - 6 + 11 - 6 = 0
$$

So $(x - 1)$ is a factor.

**Step 2: Synthetic division**.

```
    1 |  1   -6   11   -6
      |      1   -5    6
      -------------------
         1   -5    6    0
```

**Detailed process explanation**:
- Place the coefficients $1, -6, 11, -6$ in order.
- The number $1$ on the far left comes from the root $x = 1$ of $(x - 1)$.
- **Bring down**: Write the leading coefficient $1$ directly below.
- **Step 1**: $1 \times 1 = 1$, write it in the second position of the second row. $-6 + 1 = -5$, write it below.
- **Step 2**: $(-5) \times 1 = -5$, write it in the third position of the second row. $11 + (-5) = 6$, write it below.
- **Step 3**: $6 \times 1 = 6$, write it in the fourth position of the second row. $-6 + 6 = 0$, write it below.

The numbers in the third row — $1, -5, 6, 0$ — mean:
- $1, -5, 6$ are the coefficients of the quotient: $1x^2 - 5x + 6$
- The final $0$ is the remainder — a remainder of $0$ confirms exact divisibility, verifying that $(x - 1)$ is indeed a factor.

**Step 3: Factorise the quadratic**.

$$
x^2 - 5x + 6 = (x - 2)(x - 3)
$$

Find two numbers whose product is $6$ and sum is $-5$: they are $-2$ and $-3$.

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = (x - 1)(x - 2)(x - 3)}
$$

---

**Example 2**: Factorise $f(x) = 2x^3 - 3x^2 - 11x + 6$.

**Detailed solution**:

**Step 1: Test roots**.

The leading coefficient is $2$ and the constant term is $6$. Possible rational roots are $\pm 1, \pm 2, \pm 3, \pm 6, \pm \frac{1}{2}, \pm \frac{3}{2}$.

Test $x = 2$: $f(2) = 16 - 12 - 22 + 6 = -12 \neq 0$.
Test $x = -2$:

$$
f(-2) = -16 - 12 + 22 + 6 = 0
$$

So $(x + 2)$ is a factor (note $x = -2$ corresponds to $x + 2 = 0$).

**Step 2: Synthetic division**.

```
    -2 |  2   -3   -11    6
       |     -4    14    -6
       --------------------
          2   -7     3    0
```

**Process explanation**:
- The number on the far left is $-2$ (the value of the root).
- Bring down $2$.
- $2 \times (-2) = -4$, $-3 + (-4) = -7$.
- $(-7) \times (-2) = 14$, $-11 + 14 = 3$.
- $3 \times (-2) = -6$, $6 + (-6) = 0$.

The quotient is $2x^2 - 7x + 3$.

**Step 3: Factorise $2x^2 - 7x + 3$**.

$a \times c = 2 \times 3 = 6$. Find two numbers whose product is $6$ and sum is $-7$: $(-1) \times (-6) = 6$, $(-1) + (-6) = -7$.

Split and group:

$$
\begin{aligned}
2x^2 - 7x + 3 &= 2x^2 - x - 6x + 3 \\
&= x(2x - 1) - 3(2x - 1) \\
&= (2x - 1)(x - 3)
\end{aligned}
$$

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = (x + 2)(2x - 1)(x - 3)}
$$

---

**Example 3**: Factorise $f(x) = 3x^3 + 6x^2 - 3x - 6$.

**Detailed solution**:

**Step 0: Observation**. All coefficients are divisible by $3$, so first take out the common factor $3$:

$$
f(x) = 3(x^3 + 2x^2 - x - 2)
$$

Let $g(x) = x^3 + 2x^2 - x - 2$.

**Step 1: Test roots**. Test $x = 1$: $g(1) = 1 + 2 - 1 - 2 = 0$. So $(x - 1)$ is a factor of $g(x)$.

**Step 2: Synthetic division**.

```
    1 |  1    2   -1   -2
      |       1    3    2
      --------------------
         1    3    2    0
```

The quotient is $x^2 + 3x + 2$.

**Step 3: Factorise the quadratic**.

$$
x^2 + 3x + 2 = (x + 1)(x + 2)
$$

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = 3(x - 1)(x + 1)(x + 2)}
$$

---

**Example 4**: Factorise $f(x) = 2x^3 - 9x^2 + 7x + 6$.

**Detailed solution**:

**Step 1: Test roots**.

Test $x = 1$: $f(1) = 2 - 9 + 7 + 6 = 6 \neq 0$.
Test $x = -1$: $f(-1) = -2 - 9 - 7 + 6 = -12 \neq 0$.
Test $x = 2$: $f(2) = 16 - 36 + 14 + 6 = 0$. ✓

So $(x - 2)$ is a factor.

**Step 2: Synthetic division**.

```
    2 |  2   -9    7    6
      |       4  -10   -6
      --------------------
         2   -5   -3    0
```

The quotient is $2x^2 - 5x - 3$.

**Step 3: Factorise $2x^2 - 5x - 3$**.

$a \times c = 2 \times (-3) = -6$. Find two numbers whose product is $-6$ and sum is $-5$: $(-6) \times 1 = -6$, $(-6) + 1 = -5$.

$$
2x^2 - 6x + x - 3 = 2x(x - 3) + 1(x - 3) = (2x + 1)(x - 3)
$$

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = (x - 2)(2x + 1)(x - 3)}
$$

---

**Example 5**: Factorise $f(x) = 6x^3 - 7x^2 - 7x + 6$.

**Detailed solution**:

**Step 1: Test roots**.

Test $x = 1$: $f(1) = 6 - 7 - 7 + 6 = -2 \neq 0$.
Test $x = -1$: $f(-1) = -6 - 7 + 7 + 6 = 0$. ✓

So $(x + 1)$ is a factor.

**Step 2: Synthetic division**.

```
    -1 |  6   -7   -7    6
       |     -6   13   -6
       --------------------
          6  -13    6    0
```

The quotient is $6x^2 - 13x + 6$.

**Step 3: Factorise $6x^2 - 13x + 6$**.

$a \times c = 6 \times 6 = 36$. Find two numbers whose product is $36$ and sum is $-13$: $(-9) \times (-4) = 36$, $(-9) + (-4) = -13$.

$$
6x^2 - 9x - 4x + 6 = 3x(2x - 3) - 2(2x - 3) = (3x - 2)(2x - 3)
$$

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = (x + 1)(3x - 2)(2x - 3)}
$$

---

**Example 6**: Factorise $f(x) = x^3 + 2x^2 - 5x - 6$.

**Detailed solution**:

**Step 1: Test roots**.

Test $x = 1$: $f(1) = 1 + 2 - 5 - 6 = -8 \neq 0$.
Test $x = -1$: $f(-1) = -1 + 2 + 5 - 6 = 0$. ✓

So $(x + 1)$ is a factor.

**Step 2: Synthetic division**.

```
    -1 |  1    2   -5   -6
       |     -1   -1    6
       --------------------
          1    1   -6    0
```

The quotient is $x^2 + x - 6$.

**Step 3: Factorise the quadratic**.

$$
x^2 + x - 6 = (x + 3)(x - 2)
$$

**Step 4: Complete factorisation**.

$$
\boxed{f(x) = (x + 1)(x + 3)(x - 2)}
$$

---

### 3.1.4 Solving Cubic Equations

The process for solving a cubic equation $ax^3 + bx^2 + cx + d = 0$ is **to factorise the cubic polynomial, then set each factor equal to zero**. This is because if the product of several factors is zero, at least one of the factors must be zero.

---

**Example 1**: Solve $x^3 - 4x^2 + x + 6 = 0$.

**Detailed solution**:

Test roots: $f(2) = 8 - 16 + 2 + 6 = 0$, so $(x - 2)$ is a factor.

Synthetic division:

```
    2 |  1   -4    1    6
      |       2   -4   -6
      --------------------
         1   -2   -3    0
```

Quotient: $x^2 - 2x - 3 = (x - 3)(x + 1)$.

So $(x - 2)(x - 3)(x + 1) = 0$.

Therefore:

$$
\boxed{x = 2,\quad x = 3,\quad x = -1}
$$

---

**Example 2**: Solve $x^3 - 5x^2 + 8x - 4 = 0$.

**Detailed solution**:

Test $x = 1$: $f(1) = 1 - 5 + 8 - 4 = 0$.

Synthetic division:

```
    1 |  1   -5    8   -4
      |       1   -4    4
      --------------------
         1   -4    4    0
```

Quotient: $x^2 - 4x + 4 = (x - 2)^2$.

So $(x - 1)(x - 2)^2 = 0$.

Therefore:

$$
\boxed{x = 1 \quad\text{or}\quad x = 2\ (\text{double root})}
$$

---

**Example 3**: Given that $x = 2$ is a root of $2x^3 - 3x^2 - 18x + k = 0$, find $k$ and solve the equation.

**Detailed solution**:

Substitute $x = 2$: $16 - 12 - 36 + k = -32 + k = 0 \Rightarrow k = 32$.

The equation is $2x^3 - 3x^2 - 18x + 32 = 0$. We know $(x - 2)$ is a factor.

Synthetic division:

```
    2 |  2   -3   -18   32
      |       4     2   -32
      ----------------------
         2    1   -16    0
```

Quotient: $2x^2 + x - 16$. Use the quadratic formula:

$$
x = \frac{-1 \pm \sqrt{1 + 128}}{4} = \frac{-1 \pm \sqrt{129}}{4}
$$

Therefore the solutions are:

$$
\boxed{x = 2,\quad x = \frac{-1 + \sqrt{129}}{4},\quad x = \frac{-1 - \sqrt{129}}{4}}
$$

---

**Example 4**: Solve $x^3 - 2x^2 - 5x + 6 = 0$.

**Detailed solution**:

Test $x = 1$: $f(1) = 1 - 2 - 5 + 6 = 0$. ✓

Synthetic division:

```
    1 |  1   -2   -5    6
      |       1   -1   -6
      --------------------
         1   -1   -6    0
```

Quotient: $x^2 - x - 6 = (x - 3)(x + 2)$.

So $(x - 1)(x - 3)(x + 2) = 0$.

Therefore:

$$
\boxed{x = 1,\quad x = 3,\quad x = -2}
$$

---

**Example 5**: Solve $2x^3 - x^2 - 13x - 6 = 0$.

**Detailed solution**:

Test $x = -1$: $f(-1) = -2 - 1 + 13 - 6 = 4 \neq 0$.
Test $x = -2$: $f(-2) = -16 - 4 + 26 - 6 = 0$. ✓

Synthetic division:

```
    -2 |  2   -1   -13   -6
       |     -4    10    6
       ---------------------
          2   -5    -3    0
```

Quotient: $2x^2 - 5x - 3 = (2x + 1)(x - 3)$.

So $(x + 2)(2x + 1)(x - 3) = 0$.

Therefore:

$$
\boxed{x = -2,\quad x = -\frac{1}{2},\quad x = 3}
$$

---

**Example 6**: Given that $x = 3$ is a root of $x^3 + 4x^2 - 11x + k = 0$, find $k$ and solve the equation.

**Detailed solution**:

Substitute $x = 3$: $27 + 36 - 33 + k = 30 + k = 0 \Rightarrow k = -30$.

The equation is $x^3 + 4x^2 - 11x - 30 = 0$. We know $(x - 3)$ is a factor.

Synthetic division:

```
    3 |  1    4   -11   -30
      |       3    21    30
      ---------------------
         1    7    10     0
```

Quotient: $x^2 + 7x + 10 = (x + 2)(x + 5)$.

So $(x - 3)(x + 2)(x + 5) = 0$.

Therefore:

$$
\boxed{x = 3,\quad x = -2,\quad x = -5}
$$

---

## 3.2 The Discriminant $\Delta$

### 3.2.1 Definition and Three Cases

For a quadratic equation $ax^2 + bx + c = 0$ ($a \neq 0$), the quadratic formula is:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

The expression under the square root, $b^2 - 4ac$, determines the nature of the roots. We define the **discriminant**:

$$
\boxed{\Delta = b^2 - 4ac}
$$

**Why does $\Delta$ determine the nature of the roots?**

| Value of $\Delta$ | $\sqrt{\Delta}$ | Nature of Roots |
|:---:|:---|:---|
| $\Delta > 0$ | $\sqrt{\Delta}$ is a positive real number | $\frac{-b \pm \text{positive}}{2a}$, two distinct real roots |
| $\Delta = 0$ | $\sqrt{\Delta} = 0$ | $\frac{-b \pm 0}{2a} = -\frac{b}{2a}$, one repeated root |
| $\Delta < 0$ | $\sqrt{\Delta}$ is not a real number | No real roots |

---

**Example 1**: Determine the nature of the roots of the following equations:
(a) $2x^2 - 3x + 1 = 0$
(b) $4x^2 - 4x + 1 = 0$
(c) $3x^2 + 2x + 5 = 0$

**Detailed solution**:

(a) $\Delta = (-3)^2 - 4(2)(1) = 9 - 8 = 1 > 0$, two distinct real roots.

(b) $\Delta = (-4)^2 - 4(4)(1) = 16 - 16 = 0$, one repeated root.

(c) $\Delta = 2^2 - 4(3)(5) = 4 - 60 = -56 < 0$, no real roots.

---

**Example 2**: The equation $x^2 + kx + 4 = 0$ has a repeated root. Find $k$.

**Detailed solution**:

$\Delta = k^2 - 16 = 0 \Rightarrow k = \pm 4$.

---

**Example 3**: The equation $2x^2 - 3x + k = 0$ has two distinct real roots. Find the range of $k$.

**Detailed solution**:

$\Delta = 9 - 8k > 0 \Rightarrow k < \frac{9}{8}$.

---

**Example 4**: The equation $x^2 - 2x + (k - 3) = 0$ has no real roots. Find the range of $k$.

**Detailed solution**:

$\Delta = (-2)^2 - 4(1)(k - 3) = 4 - 4k + 12 = 16 - 4k < 0 \Rightarrow 4k > 16 \Rightarrow k > 4$.

---

**Example 5**: The equation $kx^2 + 3x + 2 = 0$ has a repeated root. Find the value of $k$.

**Detailed solution**:

Note that $k$ is the coefficient of $x^2$, so $k \neq 0$.

$\Delta = 9 - 8k = 0 \Rightarrow k = \frac{9}{8}$.

---

**Example 6**: The equation $3x^2 - 4x + k = 0$ has two distinct real roots. Find the range of $k$.

**Detailed solution**:

$\Delta = 16 - 12k > 0 \Rightarrow k < \frac{4}{3}$.

---

### 3.2.2 Relative Position of a Line and a Curve

Substitute the line $y = mx + c$ into the curve to eliminate $y$, obtaining a quadratic equation in $x$:

| Value of $\Delta$ | Number of Intersection Points | Relative Position |
|:---:|:---:|:---|
| $\Delta > 0$ | 2 points | Intersect at two points |
| $\Delta = 0$ | 1 point | Tangent (touch) |
| $\Delta < 0$ | 0 points | No intersection |

---

**Example 1**: Determine the relative position of $y = 2x + 1$ and $y = x^2 - 3x + 4$.

After substitution: $x^2 - 5x + 3 = 0$, $\Delta = 25 - 12 = 13 > 0$, intersect at two points.

---

**Example 2**: Find $k$ such that $y = 3x + k$ is tangent to $y = x^2 - x + 2$.

After substitution: $x^2 - 4x + (2 - k) = 0$, $\Delta = 16 - 4(2 - k) = 8 + 4k = 0 \Rightarrow k = -2$.

---

**Example 3**: Find $c$ such that $y = x + c$ does not intersect $y = 2x^2 - 3x + 1$.

After substitution: $2x^2 - 4x + (1 - c) = 0$, $\Delta = 16 - 8(1 - c) = 8 + 8c < 0 \Rightarrow c < -1$.

---

**Example 4**: Find $k$ such that the line $y = 2x + k$ intersects the curve $y = x^2 - 2x + 3$ at two points.

After substitution: $x^2 - 4x + (3 - k) = 0$, $\Delta = 16 - 4(3 - k) = 4 + 4k > 0 \Rightarrow k > -1$.

---

**Example 5**: The line $y = mx + 1$ is tangent to the curve $y = x^2 - 3x + 5$. Find $m$.

After substitution: $x^2 - (m + 3)x + 4 = 0$.

$\Delta = (m + 3)^2 - 16 = 0 \Rightarrow (m + 3)^2 = 16 \Rightarrow m + 3 = \pm 4 \Rightarrow m = 1$ or $m = -7$.

---

**Example 6**: Find $c$ such that the line $y = 5x + c$ is tangent to the curve $y = x^2 + x + 2$.

After substitution: $x^2 + x + 2 = 5x + c \Rightarrow x^2 - 4x + (2 - c) = 0$.

$\Delta = 16 - 4(2 - c) = 8 + 4c = 0 \Rightarrow c = -2$.

---

## 3.3 Solving Quadratic Equations

There are three core methods for solving $ax^2 + bx + c = 0$:

| Method | When to Use | Advantages | Disadvantages |
|:---|:---|:---|:---|
| **Factorisation** | When the expression is easily factorisable | Fastest, exact answer | Not all quadratics are factorisable |
| **Quadratic Formula** | Any situation | Universal, methodical | Slightly more calculation, may involve radicals |
| **Completing the Square** | When vertex form is needed | Gives extreme value information at the same time | Slightly more steps |

---

### 3.3.1 Factorisation Method

**Core principle**: If $A \times B = 0$, then $A = 0$ or $B = 0$.

**For $x^2 + bx + c = 0$ (leading coefficient = 1)**:

Find $p, q$ such that $p + q = b$ and $pq = c$. Then $x^2 + bx + c = (x + p)(x + q)$.

Since $(x + p)(x + q) = x^2 + (p + q)x + pq$.

**For $ax^2 + bx + c = 0$ (leading coefficient ≠ 1)**:

Find $p, q$ such that $pq = ac$ and $p + q = b$. Split the middle term and factor by grouping.

---

**Example 1**: Solve $x^2 - 5x + 6 = 0$.

Find $p+q=-5$, $pq=6$: $(-2)+(-3)=-5$, $(-2)\times(-3)=6$.

$(x-2)(x-3)=0 \Rightarrow x=2$ or $x=3$.

---

**Example 2**: Solve $2x^2 - 5x - 3 = 0$.

$ac = 2\times(-3)=-6$, find $p+q=-5$, $pq=-6$: $(-6)+1=-5$, $(-6)\times1=-6$.

Split: $2x^2-6x+x-3 = 2x(x-3)+1(x-3) = (2x+1)(x-3)$.

$x=-\frac{1}{2}$ or $x=3$.

---

**Example 3**: Solve $3x^2 + 2 = 7x$.

Rearrange: $3x^2 - 7x + 2 = 0$. $ac=6$, $(-6)+(-1)=-7$, $(-6)\times(-1)=6$.

$3x^2-6x-x+2 = 3x(x-2)-1(x-2) = (3x-1)(x-2)$.

$x=\frac{1}{3}$ or $x=2$.

---

**Example 4**: Solve $x^2 + x - 12 = 0$.

Find $p+q=1$, $pq=-12$: $4+(-3)=1$, $4\times(-3)=-12$.

$(x+4)(x-3)=0 \Rightarrow x=-4$ or $x=3$.

---

**Example 5**: Solve $6x^2 - 5x - 6 = 0$.

$ac = 6\times(-6)=-36$, find $p+q=-5$, $pq=-36$: $(-9)+4=-5$, $(-9)\times4=-36$.

$6x^2-9x+4x-6 = 3x(2x-3)+2(2x-3) = (3x+2)(2x-3)$.

$x=-\frac{2}{3}$ or $x=\frac{3}{2}$.

---

**Example 6**: Solve $4x^2 + 4x = 3$.

Rearrange: $4x^2 + 4x - 3 = 0$. $ac = 4\times(-3)=-12$, find $p+q=4$, $pq=-12$: $6+(-2)=4$, $6\times(-2)=-12$.

$4x^2+6x-2x-3 = 2x(2x+3)-1(2x+3) = (2x-1)(2x+3)$.

$x=\frac{1}{2}$ or $x=-\frac{3}{2}$.

---

### 3.3.2 Quadratic Formula

**The Quadratic Formula**:

$$
\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}
$$

**Complete derivation** (by completing the square):

$$
\begin{aligned}
ax^2 + bx + c &= 0 \\
x^2 + \frac{b}{a}x + \frac{c}{a} &= 0 \quad (\text{divide both sides by } a) \\
x^2 + \frac{b}{a}x &= -\frac{c}{a} \quad (\text{rearrange}) \\
x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 &= \left(\frac{b}{2a}\right)^2 - \frac{c}{a} \quad (\text{complete the square}) \\
\left(x + \frac{b}{2a}\right)^2 &= \frac{b^2 - 4ac}{4a^2} \\
x + \frac{b}{2a} &= \pm \frac{\sqrt{b^2 - 4ac}}{2a} \\
x &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{aligned}
$$

---

**Example 1**: Solve $2x^2 - 3x - 4 = 0$.

$a=2, b=-3, c=-4$.

$$
x = \frac{3 \pm \sqrt{9 + 32}}{4} = \frac{3 \pm \sqrt{41}}{4}
$$

---

**Example 2**: Solve $x^2 - 2x - 3 = 0$.

$$
x = \frac{2 \pm \sqrt{4 + 12}}{2} = \frac{2 \pm 4}{2}
$$

$x=3$ or $x=-1$.

---

**Example 3**: Solve $4x^2 - 12x + 9 = 0$.

$$
x = \frac{12 \pm \sqrt{144 - 144}}{8} = \frac{12}{8} = \frac{3}{2}\ (\text{repeated root})
$$

---

**Example 4**: Solve $x^2 - 3x - 5 = 0$.

$$
x = \frac{3 \pm \sqrt{9 + 20}}{2} = \frac{3 \pm \sqrt{29}}{2}
$$

---

**Example 5**: Solve $3x^2 + 2x - 4 = 0$.

$$
x = \frac{-2 \pm \sqrt{4 + 48}}{6} = \frac{-2 \pm \sqrt{52}}{6} = \frac{-2 \pm 2\sqrt{13}}{6} = \frac{-1 \pm \sqrt{13}}{3}
$$

---

**Example 6**: Solve $5x^2 + 2x - 1 = 0$.

$$
x = \frac{-2 \pm \sqrt{4 + 20}}{10} = \frac{-2 \pm \sqrt{24}}{10} = \frac{-2 \pm 2\sqrt{6}}{10} = \frac{-1 \pm \sqrt{6}}{5}
$$

---

### 3.3.3 Completing the Square

Completing the square rewrites $ax^2 + bx + c$ in the form $a(x + p)^2 + q$.

**Complete derivation**:

$$
\begin{aligned}
ax^2 + bx + c &= a\left(x^2 + \frac{b}{a}x\right) + c \\
&= a\left[x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 - \left(\frac{b}{2a}\right)^2\right] + c \\
&= a\left[\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2}\right] + c \\
&= a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)
\end{aligned}
$$

**Final form**:

$$
\boxed{ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + \frac{4ac - b^2}{4a}}
$$

---

**Example 1**: Solve $x^2 - 6x + 5 = 0$ by completing the square.

$$
\begin{aligned}
x^2 - 6x + 5 &= 0 \\
x^2 - 6x &= -5 \\
x^2 - 6x + 9 &= -5 + 9 \quad (\text{add } (\frac{6}{2})^2=9) \\
(x - 3)^2 &= 4 \\
x - 3 &= \pm 2 \\
x &= 5 \text{ or } x = 1
\end{aligned}
$$

---

**Example 2**: Solve $2x^2 - 8x + 3 = 0$ by completing the square.

$$
\begin{aligned}
2x^2 - 8x + 3 &= 0 \\
2(x^2 - 4x) &= -3 \\
2[(x^2 - 4x + 4) - 4] &= -3 \\
2(x - 2)^2 - 8 &= -3 \\
2(x - 2)^2 &= 5 \\
(x - 2)^2 &= \frac{5}{2} \\
x &= 2 \pm \frac{\sqrt{10}}{2}
\end{aligned}
$$

---

**Example 3**: Write $f(x) = 3x^2 + 12x + 5$ in the form $a(x + p)^2 + q$.

$$
\begin{aligned}
f(x) &= 3x^2 + 12x + 5 \\
&= 3(x^2 + 4x) + 5 \\
&= 3[(x + 2)^2 - 4] + 5 \\
&= 3(x + 2)^2 - 12 + 5 \\
&= 3(x + 2)^2 - 7
\end{aligned}
$$

The vertex is $(-2, -7)$, and since $a=3>0$, the parabola opens upwards.

---

**Example 4**: Solve $x^2 - 8x + 13 = 0$ by completing the square.

$$
\begin{aligned}
x^2 - 8x + 13 &= 0 \\
x^2 - 8x &= -13 \\
x^2 - 8x + 16 &= -13 + 16 \quad (\text{add } (\frac{8}{2})^2=16) \\
(x - 4)^2 &= 3 \\
x - 4 &= \pm \sqrt{3} \\
x &= 4 \pm \sqrt{3}
\end{aligned}
$$

---

**Example 5**: Solve $2x^2 - 8x + 5 = 0$ by completing the square.

$$
\begin{aligned}
2x^2 - 8x + 5 &= 0 \\
2(x^2 - 4x) &= -5 \\
2[(x - 2)^2 - 4] &= -5 \\
2(x - 2)^2 - 8 &= -5 \\
2(x - 2)^2 &= 3 \\
(x - 2)^2 &= \frac{3}{2} \\
x &= 2 \pm \frac{\sqrt{6}}{2}
\end{aligned}
$$

---

**Example 6**: Write $f(x) = -2x^2 + 8x - 5$ in the form $a(x + p)^2 + q$.

$$
\begin{aligned}
f(x) &= -2x^2 + 8x - 5 \\
&= -2(x^2 - 4x) - 5 \\
&= -2[(x - 2)^2 - 4] - 5 \\
&= -2(x - 2)^2 + 8 - 5 \\
&= -2(x - 2)^2 + 3
\end{aligned}
$$

The vertex is $(2, 3)$, and since $a=-2<0$, the parabola opens downwards.

---

### Comparison of Three Methods — Solving the Same Equation with All Three

Solve $x^2 - 4x - 5 = 0$:

**Factorisation** (fastest):
$(x - 5)(x + 1) = 0$, $x = 5$ or $x = -1$.

**Quadratic Formula**:
$x = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm 6}{2}$, $x = 5$ or $x = -1$.

**Completing the Square**:
$(x - 2)^2 = 9$, $x - 2 = \pm 3$, $x = 5$ or $x = -1$.

All three methods give the same result, but factorisation is the quickest — **use factorisation whenever possible**.

---

## 3.4 Completing the Square and Extreme Values

### 3.4.1 Finding Extreme Values by Completing the Square

In $f(x) = a(x + p)^2 + q$, since $(x + p)^2 \geq 0$:
- $a > 0$: $f(x) \geq q$, minimum value $q$ at $x = -p$.
- $a < 0$: $f(x) \leq q$, maximum value $q$ at $x = -p$.

**Why?** Because the minimum value of $(x + p)^2$ is $0$ (when $x = -p$), at which point $f(x) = q$.

---

**Example 1**: Find the minimum value of $f(x) = x^2 - 4x + 7$.

$f(x) = (x - 2)^2 + 3$. $a=1>0$, minimum value $3$ at $x=2$.

---

**Example 2**: Find the maximum value of $f(x) = -2x^2 + 12x - 10$.

$f(x) = -2(x - 3)^2 + 8$. $a=-2<0$, maximum value $8$ at $x=3$.

---

**Example 3**: Find the extreme values of $f(x) = x^2 - 2x - 3$ on $[0, 4]$.

$f(x) = (x - 1)^2 - 4$. The vertex $(1, -4)$ lies within the interval, so minimum is $-4$.
$f(0) = -3$, $f(4) = 5$. Maximum is $5$.

---

**Example 4**: Find the minimum value of $f(x) = x^2 + 6x + 11$.

$f(x) = (x + 3)^2 + 2$. Minimum value $2$ at $x = -3$.

---

**Example 5**: Find the maximum value of $f(x) = -x^2 + 4x + 1$.

$f(x) = -(x - 2)^2 + 5$. Maximum value $5$ at $x = 2$.

---

**Example 6**: Find the range of $f(x) = x^2 - 4x + 5$ on $[1, 5]$.

$f(x) = (x - 2)^2 + 1$, vertex $(2, 1)$ lies within the interval. $f(1)=2$, $f(5)=10$. Range: $[1, 10]$.

---

### 3.4.2 Sketching Graphs

Four key elements: direction of opening, vertex, $x$-intercepts, $y$-intercept.

---

**Example 1**: $f(x) = x^2 - 2x - 3$.
Opens upwards, vertex $(1, -4)$, $x$-intercepts $(-1,0)$ and $(3,0)$, $y$-intercept $(0,-3)$.

**Example 2**: $f(x) = -x^2 + 4x$.
Opens downwards, vertex $(2, 4)$, $x$-intercepts $(0,0)$ and $(4,0)$.

**Example 3**: $f(x) = x^2 + 2x + 3$.
Opens upwards, vertex $(-1, 2)$, $\Delta < 0$ so no $x$-intercepts, $y$-intercept $(0,3)$. Entirely above the $x$-axis.

**Example 4**: $f(x) = -2x^2 + 4x + 6$.
Opens downwards, vertex $(1, 8)$, $x$-intercepts $(-1,0)$ and $(3,0)$, $y$-intercept $(0,6)$.

---

### 3.4.3 Finding the Range

Steps: Complete the square → determine whether the vertex is within the domain → evaluate endpoints → compare.

**Example 1**: $f(x) = 2x^2 - 8x + 3$ on $\mathbb{R}$.
$f(x)=2(x-2)^2-5$, range $[-5,\infty)$.

**Example 2**: $f(x) = x^2 - 2x + 3$ on $[-1,3]$.
$f(x)=(x-1)^2+2$, vertex lies within the interval. $f(1)=2$, $f(-1)=6$, $f(3)=6$, range $[2,6]$.

**Example 3**: $f(x) = x^2 - 4x + 5$ on $[3,5]$.
$f(x)=(x-2)^2+1$, vertex $x=2$ not in the interval, function is increasing. $f(3)=2$, $f(5)=10$, range $[2,10]$.

**Example 4**: $f(x) = -x^2 + 2x + 3$ on $[-1,4]$.
$f(x)=-(x-1)^2+4$, vertex $(1,4)$ lies within the interval. $f(-1)=0$, $f(4)=-5$. Range $[-5,4]$.

---

## 3.5 Quadratic Inequalities

### 3.5.1 Algebraic Method (Sign Table Method)

**Complete steps**:

**Step 1**: Rearrange to $ax^2 + bx + c \;(>/</\geq/\leq)\;0$. If $a < 0$, multiply both sides by $-1$ and reverse the inequality sign.

**Step 2**: Solve the corresponding equation $ax^2 + bx + c = 0$ to obtain roots $x_1 \leq x_2$.

**Step 3**: Write the solution set.

**Sign Rule** (when $a > 0$):

```
Sign:    +      -      +
       ———|—————|—————>
          x₁    x₂
```

- **Greater than → outside**: $ax^2 + bx + c > 0 \Rightarrow x < x_1$ or $x > x_2$
- **Less than → inside**: $ax^2 + bx + c < 0 \Rightarrow x_1 < x < x_2$

**Why does this sign rule hold?**

Because when $a > 0$, the parabola opens upwards. Between the two roots, the parabola lies below the $x$-axis (negative values); outside the two roots, the parabola lies above the $x$-axis (positive values).

**Special cases**:

| $\Delta$ case | $>0$ | $<0$ |
|:---|:---|:---|
| $\Delta = 0$ ($a>0$) | $x \neq x_1$ | No solution |
| $\Delta < 0$ ($a>0$) | $\mathbb{R}$ (all real numbers) | No solution |

---

**Example 1**: Solve $x^2 - 5x + 6 > 0$.

$(x - 2)(x - 3) > 0$. Roots are $x = 2$ and $x = 3$. $a = 1 > 0$.

"Greater than → outside": $x < 2$ or $x > 3$.

Verification: Take $x=0$: $0-0+6=6 > 0$ ✓; take $x=2.5$: $6.25-12.5+6=-0.25 < 0$ ✓.

---

**Example 2**: Solve $2x^2 - 5x - 3 \leq 0$.

$(2x + 1)(x - 3) \leq 0$. Roots are $x = -\frac{1}{2}$ and $x = 3$. $a = 2 > 0$.

"Less than → inside" (including endpoints): $-\frac{1}{2} \leq x \leq 3$.

---

**Example 3**: Solve $x^2 + 2x + 3 > 0$.

$\Delta = 4 - 12 = -8 < 0$, $a = 1 > 0$. Always positive. Solution set: $\mathbb{R}$.

---

**Example 4**: Solve $-x^2 + 3x + 4 > 0$.

$a = -1 < 0$, multiply both sides by $-1$: $x^2 - 3x - 4 < 0$.

$(x - 4)(x + 1) < 0$. Roots are $x = -1$ and $x = 4$.

"Less than → inside": $-1 < x < 4$.

---

**Example 5**: Solve $x^2 - 4x + 4 \geq 0$.

$(x - 2)^2 \geq 0$. A square is always $\geq 0$, so the solution set is $\mathbb{R}$.

---

**Example 6**: Solve $x^2 - 4x + 4 < 0$.

$(x - 2)^2 < 0$. A square can never be less than zero, so **no solution**.

---

### 3.5.2 Graphical Method

Sketch the graph of $y = ax^2 + bx + c$, then look at the parts where the parabola is above the $x$-axis ($> 0$) or below the $x$-axis ($< 0$).

---

**Example 1**: Solve $x^2 - x - 2 < 0$ using the graphical method.

$y = x^2 - x - 2$, $a=1>0$, opens upwards. $x$-intercepts $(-1,0)$ and $(2,0)$.

The graph lies below the $x$-axis for $-1 < x < 2$. Solution set: $-1 < x < 2$.

---

**Example 2**: Given that $x^2 - 2kx + 4 > 0$ holds for all real $x$, find $k$.

$a=1>0$, so we need $\Delta < 0$: $4k^2 - 16 < 0 \Rightarrow k^2 < 4 \Rightarrow -2 < k < 2$.

---

**Example 3**: Solve $x^2 - 4 \geq 3x$.

Rearrange: $x^2 - 3x - 4 \geq 0$. $(x - 4)(x + 1) \geq 0$.

"Greater than → outside" (including endpoints): $x \leq -1$ or $x \geq 4$.

---

**Example 4**: Solve $x^2 - 3x - 10 > 0$.

$(x - 5)(x + 2) > 0$. $x < -2$ or $x > 5$.

---

**Example 5**: Solve $2x^2 + 5x - 3 \leq 0$.

$(2x - 1)(x + 3) \leq 0$. $-3 \leq x \leq \frac{1}{2}$.

---

**Example 6**: Solve $x^2 - 6x + 9 \geq 0$.

$(x - 3)^2 \geq 0$, solution set $\mathbb{R}$.

---

### 3.5.3 Inequalities with Parameters

**Example 1**: Find $k$ such that $x^2 + kx + 9 \geq 0$ holds for all $x$.

$a=1>0$, so we need $\Delta \leq 0$: $k^2 - 36 \leq 0 \Rightarrow -6 \leq k \leq 6$.

---

**Example 2**: Find $k$ such that $kx^2 + 2x + 3 > 0$ holds for all $x$.

If $k = 0$: $2x+3>0$ does not hold for all $x$, so eliminate.
If $k \neq 0$: we need $k > 0$ and $\Delta = 4 - 12k < 0 \Rightarrow k > \frac{1}{3}$.

Therefore $k > \frac{1}{3}$.

---

**Example 3**: Find $k$ such that $x^2 - 2kx + 4 > 0$ holds for all real $x$.

$\Delta = 4k^2 - 16 < 0 \Rightarrow k^2 < 4 \Rightarrow -2 < k < 2$.

---

**Example 4**: Find $k$ such that $(k-1)x^2 + 2x + 1 > 0$ holds for all $x$.

If $k-1 = 0$, i.e., $k=1$: $2x+1 > 0$, does not hold for all $x$.
If $k-1 \neq 0$: need $k-1 > 0$ and $\Delta = 4 - 4(k-1) = 8 - 4k < 0 \Rightarrow k > 2$.

Therefore $k > 2$.

---

## 3.6 Graphs of Cubic Polynomials and Inequalities

### 3.6.1 Graphs of Products of Three Linear Factors

Characteristics of the graph of $f(x) = a(x - p)(x - q)(x - r)$:

**(1) $x$-intercepts**: $x = p, q, r$ (three zeros).

**(2) $y$-intercept**: $f(0) = a(-p)(-q)(-r) = -a \cdot pqr$.

**(3) End behaviour** — determined by the leading term $ax^3$:

When $|x|$ is large, the leading term $ax^3$ dominates:

| Sign of $a$ | $x \to -\infty$ | $x \to +\infty$ |
|:---:|:---:|:---:|
| $a > 0$ | $f(x) \to -\infty$ (bottom-left) | $f(x) \to +\infty$ (top-right) |
| $a < 0$ | $f(x) \to +\infty$ (top-left) | $f(x) \to -\infty$ (bottom-right) |

**(4) Behaviour at zeros**:
- **Simple root** (factor has degree 1): The graph **crosses** the $x$-axis.
- **Double root** (factor has degree 2): The graph **touches and bounces back** (tangent to the $x$-axis).

**Sketching steps**:
1. Mark the $x$-intercepts $p, q, r$.
2. Mark the $y$-intercept.
3. Determine the end behaviour based on the sign of $a$.
4. Connect the points with a smooth S-shaped curve, crossing at simple roots and bouncing at double roots.

---

**Example 1**: Sketch the graph of $f(x) = (x + 1)(x - 1)(x - 3)$.

$x$-intercepts: $x = -1,\;1,\;3$ (three simple roots, all crossed).
$y$-intercept: $f(0) = (1)(-1)(-3) = 3$, passing through $(0, 3)$.
$a = 1 > 0$: left end goes down, right end goes up.

Behaviour: From the third quadrant → crosses $x = -1$ from bottom to top → local maximum → crosses $x = 1$ from top to bottom → local minimum → crosses $x = 3$ from bottom to top → extends to the top-right.

---

**Example 2**: Sketch the graph of $f(x) = -(x + 2)(x - 1)(x - 4)$.

$x$-intercepts: $x = -2,\;1,\;4$.
$y$-intercept: $f(0) = -(2)(-1)(-4) = -8$, passing through $(0, -8)$.
$a = -1 < 0$: left end goes up, right end goes down.

Behaviour: From the second quadrant → crosses $x = -2$ from top to bottom → local minimum → crosses $x = 1$ from bottom to top → local maximum → crosses $x = 4$ from top to bottom → extends to the bottom-right.

---

**Example 3**: Sketch the graph of $f(x) = (x - 1)^2(x + 2)$.

$x$-intercepts: $x = -2$ (simple root, crosses), $x = 1$ (double root, touches and bounces).
$y$-intercept: $f(0) = (1)^2(2) = 2$, passing through $(0, 2)$.
$a = 1 > 0$: left end goes down, right end goes up.

Behaviour: From the third quadrant → crosses $x = -2$ from bottom to top → local maximum → descends to touch the $x$-axis at $x = 1$ and bounces back → extends to the top-right.

---

**Example 4**: Sketch the graph of $f(x) = -(x + 1)(x - 2)^2$.

$x$-intercepts: $x = -1$ (simple root, crosses), $x = 2$ (double root, touches and bounces).
$y$-intercept: $f(0) = -(1)(4) = -4$, passing through $(0, -4)$.
$a = -1 < 0$: left end goes up, right end goes down.

Behaviour: From the second quadrant → crosses $x = -1$ from top to bottom → local minimum → rises to touch the $x$-axis at $x = 2$ and bounces back → extends to the bottom-right.

---

**Example 5**: Sketch the graph of $f(x) = (x + 3)(x + 1)(x - 2)$.

$x$-intercepts: $x = -3,\;-1,\;2$ (three simple roots).
$y$-intercept: $f(0) = (3)(1)(-2) = -6$, passing through $(0, -6)$.
$a = 1 > 0$: left end goes down, right end goes up.

---

**Example 6**: Sketch the graph of $f(x) = -2(x + 1)(x - 1)(x - 3)$.

$x$-intercepts: $x = -1,\;1,\;3$.
$y$-intercept: $f(0) = -2(1)(-1)(-3) = -6$, passing through $(0, -6)$.
$a = -2 < 0$: left end goes up, right end goes down.

---

### 3.6.2 Absolute Value Graphs

**Core rule** (must memorise):

$$
y = |f(x)|
$$

- **Keep** the parts where $f(x) \geq 0$ (parts **above** the $x$-axis remain **unchanged**)
- **Reflect** the parts where $f(x) < 0$ (reflect the parts **below** the $x$-axis **upwards across the $x$-axis**)

In other words: **Negative parts are folded up to the positive side**.

Therefore, in the graph of $y = |f(x)|$:
1. The graph is always **above** (or on) the $x$-axis; there can never be negative values.
2. At the zeros where $f(x) = 0$, the absolute value graph will have **sharp corners (cusps)** (because when the sign changes from positive to negative or vice versa, the slope suddenly reverses direction).
3. The parts of the original function above the $x$-axis remain unchanged; the parts below are "folded" upwards.

---

**Example 1**: Sketch the graph of $y = |(x + 1)(x - 1)(x - 3)|$.

First analyse the sign of $f(x) = (x + 1)(x - 1)(x - 3)$:

| Interval | $x<-1$ | $-1<x<1$ | $1<x<3$ | $x>3$ |
|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $-$ | $+$ | $-$ | $+$ |

Reflect the negative parts ($x < -1$ and $1 < x < 3$) upwards across the $x$-axis.

The final graph touches the $x$-axis at $x = -1, 1, 3$ (cusps), and all other parts are above the $x$-axis.

---

**Example 2**: Sketch the graph of $y = |(x - 1)(x - 2)(x - 4)|$.

Analyse the sign of $f(x) = (x - 1)(x - 2)(x - 4)$:

$f(0) = (-1)(-2)(-4) = -8$, so at $x=0$, $f(x) < 0$.

| Interval | $x<1$ | $1<x<2$ | $2<x<4$ | $x>4$ |
|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $-$ | $+$ | $-$ | $+$ |

Reflect the negative regions ($x<1$ and $2<x<4$) upwards. Cusps at $x=1,2,4$.

---

**Example 3**: Find the number of real roots of $|(x + 1)(x - 1)(x - 2)| = 2$.

Sign analysis: $x<-1$ ($-$), $-1<x<1$ ($+$), $1<x<2$ ($-$), $x>2$ ($+$).

After the absolute value transformation, $|f(0)| = |(1)(-1)(-2)| = 2$, so $(0,2)$ is an intersection point.

The horizontal line $y=2$ intersects the graph:
- $x<-1$: 1 intersection
- $-1<x<1$: 2 intersections
- $1<x<2$: 2 intersections
- $x>2$: 1 intersection

Total **5 intersections**, meaning the equation has 5 real roots.

---

**Example 4**: Sketch the graph of $y = |(x + 2)(x - 1)^2|$.

$f(x) = (x + 2)(x - 1)^2$.

Sign: $x<-2$ ($-$), $-2<x<1$ ($+$), $x>1$ ($+$).

Reflect the part where $x<-2$ upwards. There is a cusp at $x=-2$; at $x=1$, the graph touches smoothly (double root — the original function does not change sign here, so no reflection is needed).

---

**Example 5**: Sketch the graph of $y = |(x+1)(x-2)(x-5)|$.

Sign: $x<-1$ ($-$), $-1<x<2$ ($+$), $2<x<5$ ($-$), $x>5$ ($+$).

Reflect the $x<-1$ and $2<x<5$ parts. Cusps at $x=-1,2,5$.

---

**Example 6**: Estimate the number of real roots of $|(x+2)(x-1)(x-4)|=3$.

The parts of the graph for $x<-2$ and $1<x<4$ are reflected upwards. The horizontal line $y=3$ intersects the graph at approximately 5 points, giving approximately 5 real roots.

---

### 3.6.3 Graphical Solution of Cubic Inequalities (Syllabus 4.5)

For $f(x) \geq d$ (similarly for $>$, $\leq$, $<$), where $f(x) = a(x-p)(x-q)(x-r)$:

1. Sketch the graph of $y = f(x)$.
2. Draw the horizontal line $y = d$.
3. Find the $x$-coordinates of the intersection points (solve $f(x) = d$).
4. Read off the intervals of $x$ that satisfy the inequality.

**When $d = 0$**, the horizontal line is the $x$-axis, and the problem reduces to analysing the sign of $f(x)$.

---

**Example 1**: $f(x) = (x+1)(x-1)(x-3)$, solve $f(x) \leq 0$.

Sign table:

| Interval | $x<-1$ | $-1<x<1$ | $1<x<3$ | $x>3$ |
|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $-$ | $+$ | $-$ | $+$ |

$f(x) \leq 0$ corresponds to intervals where the function is negative or zero (including endpoints):

$$
\boxed{x \leq -1 \quad \text{or} \quad 1 \leq x \leq 3}
$$

---

**Example 2**: $f(x) = -(x+1)(x-2)(x-5)$, solve $f(x) > 0$.

First consider $g(x) = (x+1)(x-2)(x-5)$, $a_g = 1 > 0$.

Sign of $g(x)$: $x<-1$ ($-$), $-1<x<2$ ($+$), $2<x<5$ ($-$), $x>5$ ($+$).

$f(x) = -g(x)$, so the sign of $f(x)$ is the opposite of $g(x)$:

| Interval | $x<-1$ | $-1<x<2$ | $2<x<5$ | $x>5$ |
|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $+$ | $-$ | $+$ | $-$ |

$f(x) > 0$ corresponds to positive intervals (excluding endpoints):

$$
\boxed{x < -1 \quad \text{or} \quad 2 < x < 5}
$$

---

**Example 3**: $f(x) = (x+2)(x-1)(x-4)$, solve $f(x) \geq 8$.

Expand: $f(x) = x^3 - 3x^2 - 6x + 8$.

Solve $f(x) = 8$:

$$
x^3 - 3x^2 - 6x + 8 = 8 \Rightarrow x^3 - 3x^2 - 6x = 0 \Rightarrow x(x^2 - 3x - 6) = 0
$$

$x = 0$ or $x = \frac{3 \pm \sqrt{33}}{2}$. $\frac{3 - \sqrt{33}}{2} \approx -1.372$, $\frac{3 + \sqrt{33}}{2} \approx 4.372$.

$a = 1 > 0$, left end goes down, right end goes up. The solution set for $f(x) \geq 8$ is:

$$
\boxed{\frac{3 - \sqrt{33}}{2} \leq x \leq 0 \quad \text{or} \quad x \geq \frac{3 + \sqrt{33}}{2}}
$$

---

**Example 4**: $f(x) = (x+1)(x-2)(x-4)$, solve $f(x) \leq 0$.

Sign: $x<-1$ ($-$), $-1<x<2$ ($+$), $2<x<4$ ($-$), $x>4$ ($+$).

$\leq 0$: $x \leq -1$ or $2 \leq x \leq 4$.

---

**Example 5**: $f(x) = -(x+2)(x-1)(x-5)$, solve $f(x) \geq 0$.

$f(x) \geq 0 \iff -(x+2)(x-1)(x-5) \geq 0 \iff (x+2)(x-1)(x-5) \leq 0$.

Sign: $x<-2$ ($-$), $-2<x<1$ ($+$), $1<x<5$ ($-$), $x>5$ ($+$).

$(x+2)(x-1)(x-5) \leq 0$: $x \leq -2$ or $1 \leq x \leq 5$.

---

**Example 6**: Solve $(x+1)(x-1)(x-3) \geq 4$.

$f(x) = (x+1)(x-1)(x-3) = x^3 - 3x^2 - x + 3$.

$f(x) = 4 \Rightarrow x^3 - 3x^2 - x - 1 = 0$. This cubic is not easy to factorise. In an actual exam, the intersection coordinates would typically be given or solvable with a calculator.

---

## 3.7 Using Differentiation to Find Extreme Values of Quadratic Functions

### 3.7.1 Introduction to the Differentiation Method

Before learning differentiation, we used completing the square to find extreme values. Now, with the tool of differentiation, we can use derivatives to find extreme values, laying the foundation for solving extreme value problems of more complex functions (cubic, exponential, trigonometric, etc.) in the future.

**Core idea**: At an extreme point, the tangent line to the function is horizontal, meaning the slope is zero, i.e., **the derivative is zero**.

For a quadratic function $f(x) = ax^2 + bx + c$:

**Step 1: Differentiate**.

By the Power Rule $(x^n)' = nx^{n-1}$:

$$
f'(x) = \frac{d}{dx}(ax^2 + bx + c) = 2ax + b
$$

**Derivation process**:
- $\frac{d}{dx}(ax^2) = a \cdot 2x = 2ax$
- $\frac{d}{dx}(bx) = b \cdot 1 = b$
- $\frac{d}{dx}(c) = 0$ (the derivative of a constant is zero)

**Step 2: Set the derivative to zero to find the stationary point**.

$$
2ax + b = 0 \;\Rightarrow\; x = -\frac{b}{2a}
$$

This is exactly the $x$-coordinate of the vertex we obtained by completing the square!

**Step 3: Substitute into the original function to find the extreme value**.

$$
\begin{aligned}
f\!\left(-\frac{b}{2a}\right) &= a\left(-\frac{b}{2a}\right)^2 + b\left(-\frac{b}{2a}\right) + c \\
&= a \cdot \frac{b^2}{4a^2} - \frac{b^2}{2a} + c \\
&= -\frac{b^2}{4a} + c = \frac{4ac - b^2}{4a}
\end{aligned}
$$

**Step 4: Use the second derivative to determine the type of extreme value**.

The second derivative is the derivative of the first derivative:

$$
f''(x) = \frac{d}{dx}(2ax + b) = 2a
$$

- $f''(x) = 2a > 0$ (i.e., $a > 0$): **Minimum**. Because $f'' > 0$ means $f'$ is increasing, so $f'$ goes from negative to positive through zero, meaning the function decreases then increases.
- $f''(x) = 2a < 0$ (i.e., $a < 0$): **Maximum**.

---

**Comparison with Completing the Square**:

The differentiation method gives $x = -\frac{b}{2a}$, and completing the square gives $f(x) = a\left(x + \frac{b}{2a}\right)^2 + \frac{4ac-b^2}{4a}$, with the vertex's $x$-coordinate being $-\frac{b}{2a}$ in both cases. The two methods are completely equivalent.

---

**Example 1**: Use differentiation to find the extreme value of $f(x) = 2x^2 - 8x + 5$.

$f'(x) = 4x - 8$. Set $f'(x) = 0$: $4x = 8 \Rightarrow x = 2$.

$f''(x) = 4 > 0$, so it is a minimum.

$f(2) = 8 - 16 + 5 = -3$.

**Verification** (by completing the square): $f(x) = 2(x - 2)^2 - 3$, minimum $-3$. ✓

---

**Example 2**: Use differentiation to find the extreme value of $f(x) = -3x^2 + 12x - 7$.

$f'(x) = -6x + 12$. Set $f'(x) = 0$: $x = 2$.

$f''(x) = -6 < 0$, so it is a maximum.

$f(2) = -12 + 24 - 7 = 5$.

**Verification** (by completing the square): $f(x) = -3(x - 2)^2 + 5$, maximum $5$. ✓

---

**Example 3**: Given that $f(x) = x^2 + kx + 4$ has an extreme value at $x = 3$, find $k$ and determine its type.

$f'(x) = 2x + k$. $f'(3) = 6 + k = 0 \Rightarrow k = -6$.

$f''(x) = 2 > 0$, so it is a minimum.

$f(3) = 9 - 18 + 4 = -5$.

---

**Example 4**: Use differentiation to find the extreme value of $f(x) = 5x^2 - 20x + 3$, and compare with completing the square.

**Differentiation method**: $f'(x) = 10x - 20 = 0 \Rightarrow x = 2$. $f''(x) = 10 > 0$, minimum $f(2) = 20 - 40 + 3 = -17$.

**Completing the square**: $f(x) = 5(x-2)^2 - 17$, minimum $-17$. Both methods agree. ✓

**Comparison**: The differentiation method is more direct and does not require completing the square.

---

**Example 5**: Use differentiation to find the extreme value of $f(x) = -4x^2 + 24x - 31$.

$f'(x) = -8x + 24 = 0 \Rightarrow x = 3$. $f''(x) = -8 < 0$, maximum $f(3) = -36 + 72 - 31 = 5$.

---

**Example 6**: Given that $f(x) = 3x^2 + 2mx + 5$ has an extreme value at $x = -2$, find $m$ and the extreme value.

$f'(x) = 6x + 2m$. $f'(-2) = -12 + 2m = 0 \Rightarrow m = 6$.

$f''(x) = 6 > 0$, minimum. $f(-2) = 12 - 24 + 5 = -7$.

---

**Example 7**: Use differentiation to prove that the minimum value of $f(x) = x^2 + 4x + 7$ is $3$.

$f'(x) = 2x + 4 = 0 \Rightarrow x = -2$. $f''(x) = 2 > 0$, minimum $f(-2) = 4 - 8 + 7 = 3$. QED. ✓

---

**Example 8**: A rectangular garden has a perimeter of $40$ metres. Find the maximum area.

Let the length be $x$ metres, then the width is $20 - x$ metres.

Area $A(x) = x(20 - x) = 20x - x^2 = -x^2 + 20x$.

$A'(x) = -2x + 20 = 0 \Rightarrow x = 10$. $A''(x) = -2 < 0$, maximum.

Maximum area $A(10) = 100$ square metres.

---

**Example 9**: Find the extreme value of $f(x) = 2x^2 - 12x + 5$ and verify by completing the square.

**Differentiation method**: $f'(x) = 4x - 12 = 0 \Rightarrow x = 3$. $f''(x) = 4 > 0$, minimum $f(3) = 18 - 36 + 5 = -13$.

**Verification by completing the square**: $f(x) = 2(x-3)^2 - 13$, minimum $-13$. ✓

---

**Example 10**: Given that $f(x) = ax^2 + 6x + 2$ has an extreme value at $x = -1$, find $a$ and the extreme value.

$f'(x) = 2ax + 6$. $f'(-1) = -2a + 6 = 0 \Rightarrow a = 3$.

$f''(x) = 2a = 6 > 0$, minimum. $f(-1) = 3 - 6 + 2 = -1$.

---

**Example 11**: Use differentiation to find the extreme value of $f(x) = 4x^2 - 16x + 7$.

$f'(x) = 8x - 16 = 0 \Rightarrow x = 2$. $f''(x) = 8 > 0$, minimum $f(2) = 16 - 32 + 7 = -9$.

---

**Example 12**: Use differentiation to find the extreme value of $f(x) = -5x^2 + 30x - 41$.

$f'(x) = -10x + 30 = 0 \Rightarrow x = 3$. $f''(x) = -10 < 0$, maximum $f(3) = -45 + 90 - 41 = 4$.

---

**Example 13**: Given that $f(x) = 2x^2 + kx + 3$ has an extreme value at $x = -2$, find $k$ and the extreme value.

$f'(x) = 4x + k$. $f'(-2) = -8 + k = 0 \Rightarrow k = 8$.

$f''(x) = 4 > 0$, minimum. $f(-2) = 8 - 16 + 3 = -5$.

---

**Example 14**: Given that $f(x) = -3x^2 + mx + 1$ has an extreme value at $x = 1$, find $m$ and the extreme value.

$f'(x) = -6x + m$. $f'(1) = -6 + m = 0 \Rightarrow m = 6$.

$f''(x) = -6 < 0$, maximum. $f(1) = -3 + 6 + 1 = 4$.

---

**Example 15**: Use both differentiation and completing the square to find the extreme value of $f(x) = 3x^2 - 18x + 25$, and compare the two methods.

**Differentiation method**: $f'(x) = 6x - 18 = 0 \Rightarrow x = 3$. $f''(x) = 6 > 0$, minimum $f(3) = 27 - 54 + 25 = -2$.

**Completing the square**: $f(x) = 3(x^2 - 6x) + 25 = 3[(x-3)^2 - 9] + 25 = 3(x-3)^2 - 27 + 25 = 3(x-3)^2 - 2$. Minimum $-2$ at $x=3$. ✓

**Comparison**: Differentiation requires only three steps (differentiate → set to zero → second derivative), while completing the square requires algebraic manipulation. For quadratic functions, both are equally manageable, but for more complex functions, differentiation is more advantageous.

---

## Chapter Summary

| Topic | Core Content |
|:---|:---|
| **Remainder Theorem** | Remainder when $f(x) \div (x-a)$ is $f(a)$; $f(x) \div (ax+b)$ has remainder $f(-b/a)$ |
| **Factor Theorem** | $f(a)=0 \iff (x-a)$ is a factor |
| **Cubic factorisation procedure** | Test roots → Synthetic division → Factorise quadratic |
| **Synthetic division** | Division format using only coefficients, more concise than long division |
| **Discriminant $\Delta$** | $\Delta = b^2-4ac$; $\Delta>0$ two distinct roots, $\Delta=0$ repeated root, $\Delta<0$ no real roots |
| **Line and curve** | Substitute to eliminate $y$ → quadratic → $\Delta$ determines intersect/tangent/no intersection |
| **Three methods for solving quadratics** | Factorisation (fastest), Quadratic formula (universal), Completing the square (vertex form) |
| **Extreme values** | $a(x+p)^2+q$, $a>0$ minimum $q$, $a<0$ maximum $q$ |
| **Quadratic inequalities** | When $a>0$: "greater than → outside, less than → inside" |
| **Cubic graphs** | $a>0$ bottom-left to top-right, $a<0$ top-left to bottom-right; simple root crosses, double root bounces |
| **Absolute value graphs** | Negative parts reflected upwards across the $x$-axis, cusps at zeros |
| **Cubic inequalities** | Sketch graph → draw horizontal line $y=d$ → read intervals |
| **Differentiation for extreme values** | $f'(x)=0$ gives stationary point, $f''(x)$ determines max/min |

---

## Practice Problems

**1. Remainder Theorem**:
(a) Find the remainder when $f(x) = 5x^3 - 4x^2 + 3x - 2$ is divided by $x - 2$.
(b) The polynomial $f(x) = 2x^3 + kx^2 - 3x + 1$ has remainder $15$ when divided by $x + 2$. Find $k$.
(c) Find the remainder when $f(x) = 8x^3 - 6x^2 + 4x - 1$ is divided by $2x - 3$.

**2. Factor Theorem**:
(a) Show that $(x + 2)$ is a factor of $f(x) = x^3 + 3x^2 - 4x - 12$.
(b) The polynomial $f(x) = 3x^3 + ax^2 + bx - 10$ has factors $(x - 2)$ and $(x + 1)$. Find $a$ and $b$.
(c) Given that $x - 3$ is a factor of $f(x) = 2x^3 - 5x^2 + kx - 6$, find $k$.

**3. Factorising Cubic Polynomials**:
(a) $x^3 - 3x^2 - 10x + 24$
(b) $3x^3 + 2x^2 - 7x + 2$
(c) $4x^3 - 12x^2 - x + 3$

**4. Solving Cubic Equations**:
(a) $x^3 - 2x^2 - 5x + 6 = 0$
(b) $2x^3 - 3x^2 - 3x + 2 = 0$
(c) Given that $x = -3$ is a root of $x^3 + 3x^2 - 4x + k = 0$, find $k$ and solve the equation.

**5. Discriminant**:
(a) Determine the nature of the roots of $2x^2 - 5x + 4 = 0$.
(b) The equation $x^2 - 6x + k = 0$ has a repeated root. Find $k$.
(c) The equation $3x^2 + kx + 3 = 0$ has no real roots. Find the range of $k$.

**6. Line and Curve**:
(a) Determine the relative position of $y = 4x - 3$ and $y = x^2 - x + 2$.
(b) Find $k$ such that $y = 2x + k$ is tangent to $y = x^2 - 4x + 7$.
(c) Find $m$ such that $y = mx - 1$ intersects $y = x^2 - 2x + 4$ at two points.

**7. Solving Quadratic Equations**:
(a) $x^2 - 7x + 12 = 0$ (by factorisation)
(b) $3x^2 + 5x - 2 = 0$ (by factorisation)
(c) $2x^2 - 4x - 3 = 0$ (by quadratic formula)
(d) $x^2 - 8x + 13 = 0$ (by completing the square)
(e) $5x^2 + 2x - 1 = 0$ (by quadratic formula)
(f) $2x^2 - 8x + 5 = 0$ (by completing the square)

**8. Extreme Values and Range**:
(a) Find the minimum value of $f(x) = x^2 + 8x + 19$.
(b) Find the maximum value of $f(x) = -2x^2 + 8x - 3$.
(c) Find the range of $f(x) = x^2 - 6x + 10$ on $[1, 5]$.
(d) Find the range of $f(x) = -x^2 + 2x + 3$ on $[-1, 4]$.

**9. Quadratic Inequalities**:
(a) $x^2 - 3x - 10 > 0$
(b) $2x^2 - 7x + 3 \leq 0$
(c) $-x^2 + 5x - 6 \geq 0$
(d) Find $k$ such that $x^2 + kx + 16 > 0$ holds for all real $x$.

**10. Cubic Graphs**:
(a) Sketch the graph of $f(x) = (x - 1)(x - 3)(x - 5)$, labelling the intercepts.
(b) Sketch the graph of $f(x) = -(x + 2)(x - 1)(x - 3)$, labelling the intercepts.
(c) Sketch the graph of $f(x) = (x + 1)^2(x - 4)$, labelling the intercepts and bounce point.
(d) Sketch the graph of $y = |(x + 1)(x - 1)(x - 5)|$.
(e) Estimate the number of real roots of $|(x + 2)(x - 1)(x - 4)| = 3$.

**11. Cubic Inequalities**:
(a) Solve $(x + 1)(x - 2)(x - 4) \leq 0$.
(b) Solve $-(x + 2)(x - 1)(x - 5) > 0$.
(c) Solve $(x + 1)(x - 1)(x - 3) \geq 4$.

**12. Differentiation for Extreme Values**:
(a) Use differentiation to find the extreme value of $f(x) = 4x^2 - 16x + 7$.
(b) Use differentiation to find the extreme value of $f(x) = -5x^2 + 30x - 41$.
(c) Given that $f(x) = 2x^2 + kx + 3$ has an extreme value at $x = -2$, find $k$ and the extreme value.
(d) Given that $f(x) = -3x^2 + mx + 1$ has an extreme value at $x = 1$, find $m$ and the extreme value.
(e) Use differentiation to prove that the minimum value of $f(x) = x^2 - 10x + 28$ is $3$.
(f) Use both differentiation and completing the square to find the extreme value of $f(x) = 3x^2 - 18x + 25$, and compare the two methods.

---

<details>
<summary><strong>Click to view all answers</strong></summary>

**1. Remainder Theorem**:
(a) $f(2) = 5(8) - 4(4) + 3(2) - 2 = 40 - 16 + 6 - 2 = 28$.
(b) $f(-2) = 2(-8) + k(4) - 3(-2) + 1 = -16 + 4k + 6 + 1 = 4k - 9 = 15 \Rightarrow k = 6$.
(c) $x = \frac{3}{2}$: $f(\frac{3}{2}) = 8(\frac{27}{8}) - 6(\frac{9}{4}) + 4(\frac{3}{2}) - 1 = 27 - \frac{27}{2} + 6 - 1 = \frac{54 - 27 + 12 - 2}{2} = \frac{37}{2}$.

**2. Factor Theorem**:
(a) $f(-2) = -8 + 12 + 8 - 12 = 0$, therefore $(x+2)$ is a factor of $f(x)$. ✓
(b) $f(2) = 24 + 4a + 2b - 10 = 14 + 4a + 2b = 0 \Rightarrow 2a + b = -7$; $f(-1) = -3 + a - b - 10 = -13 + a - b = 0 \Rightarrow a - b = 13$. Solving gives $a = 2$, $b = -11$.
(c) $f(3) = 54 - 45 + 3k - 6 = 3 + 3k = 0 \Rightarrow k = -1$.

**3. Factorising Cubic Polynomials**:
(a) $f(2) = 8 - 12 - 20 + 24 = 0$. Synthetic division gives $x^2 - x - 12 = (x - 4)(x + 3)$. $f(x) = (x - 2)(x - 4)(x + 3)$.
(b) $f(1) = 3 + 2 - 7 + 2 = 0$. Synthetic division gives $3x^2 + 5x - 2 = (3x - 1)(x + 2)$. $f(x) = (x - 1)(3x - 1)(x + 2)$.
(c) $f(3) = 108 - 108 - 3 + 3 = 0$. Synthetic division gives $4x^2 - 1 = (2x + 1)(2x - 1)$. $f(x) = (x - 3)(2x + 1)(2x - 1)$.

**4. Solving Cubic Equations**:
(a) $f(1) = 0$, factorising gives $(x - 1)(x + 2)(x - 3) = 0$, solutions: $x = 1, -2, 3$.
(b) $f(-1) = 0$, factorising gives $(x + 1)(2x - 1)(x - 2) = 0$, solutions: $x = -1, \frac{1}{2}, 2$.
(c) $f(-3) = -27 + 27 + 12 + k = 12 + k = 0 \Rightarrow k = -12$. Equation: $x^3 + 3x^2 - 4x - 12 = 0$, factorising gives $(x + 3)(x + 2)(x - 2) = 0$, solutions: $x = -3, -2, 2$.

**5. Discriminant**:
(a) $\Delta = 25 - 32 = -7 < 0$, no real roots.
(b) $\Delta = 36 - 4k = 0 \Rightarrow k = 9$.
(c) $\Delta = k^2 - 36 < 0 \Rightarrow -6 < k < 6$.

**6. Line and Curve**:
(a) Substituting gives $x^2 - 5x + 5 = 0$, $\Delta = 25 - 20 = 5 > 0$, intersect at two points.
(b) Substituting gives $x^2 - 6x + (7 - k) = 0$, $\Delta = 36 - 4(7 - k) = 8 + 4k = 0 \Rightarrow k = -2$.
(c) Substituting gives $x^2 - (m + 2)x + 5 = 0$, $\Delta = (m+2)^2 - 20 > 0 \Rightarrow m < -2 - 2\sqrt{5}$ or $m > -2 + 2\sqrt{5}$.

**7. Solving Quadratic Equations**:
(a) $(x - 3)(x - 4) = 0$, $x = 3$ or $x = 4$.
(b) $(3x - 1)(x + 2) = 0$, $x = \frac{1}{3}$ or $x = -2$.
(c) $x = \frac{4 \pm \sqrt{16 + 24}}{4} = \frac{4 \pm \sqrt{40}}{4} = \frac{4 \pm 2\sqrt{10}}{4} = \frac{2 \pm \sqrt{10}}{2}$.
(d) $(x - 4)^2 = 3$, $x = 4 \pm \sqrt{3}$.
(e) $x = \frac{-2 \pm \sqrt{4 + 20}}{10} = \frac{-2 \pm \sqrt{24}}{10} = \frac{-2 \pm 2\sqrt{6}}{10} = \frac{-1 \pm \sqrt{6}}{5}$.
(f) $2(x - 2)^2 = 3$, $(x - 2)^2 = \frac{3}{2}$, $x = 2 \pm \frac{\sqrt{6}}{2}$.

**8. Extreme Values and Range**:
(a) $f(x) = (x + 4)^2 + 3$, minimum $3$.
(b) $f(x) = -2(x - 2)^2 + 5$, maximum $5$.
(c) $f(x) = (x - 3)^2 + 1$, vertex $x=3$ lies within $[1,5]$, $f(3)=1$, $f(1)=5$, $f(5)=5$, range $[1,5]$.
(d) $f(x) = -(x - 1)^2 + 4$, vertex $x=1$ lies within $[-1,4]$, $f(1)=4$, $f(-1)=0$, $f(4)=-5$, range $[-5,4]$.

**9. Quadratic Inequalities**:
(a) $(x - 5)(x + 2) > 0$, $x < -2$ or $x > 5$.
(b) $(2x - 1)(x - 3) \leq 0$, $\frac{1}{2} \leq x \leq 3$.
(c) Multiply by $-1$: $x^2 - 5x + 6 \leq 0$, $(x - 2)(x - 3) \leq 0$, $2 \leq x \leq 3$.
(d) $\Delta = k^2 - 64 < 0 \Rightarrow -8 < k < 8$.

**10. Cubic Graphs**:
(a) $x$-intercepts $1,3,5$, $y$-intercept $(-1)(-3)(-5) = -15$, $a>0$ bottom-left to top-right.
(b) $x$-intercepts $-2,1,3$, $y$-intercept $-(2)(-1)(-3) = 6$, $a<0$ top-left to bottom-right.
(c) $x$-intercepts: $-1$ (double root, bounce), $4$ (simple root, cross), $y$-intercept $(1)^2(-4) = -4$, $a>0$ bottom-left to top-right.
(d) $f(x)$ negative for $x<-1$, positive for $-1<x<1$, negative for $1<x<5$, positive for $x>5$. Reflect $x<-1$ and $1<x<5$ parts upwards.
(e) Approximately 5 real roots.

**11. Cubic Inequalities**:
(a) Sign: $x<-1$ ($-$), $-1<x<2$ ($+$), $2<x<4$ ($-$), $x>4$ ($+$). $\leq 0$: $x \leq -1$ or $2 \leq x \leq 4$.
(b) $f(x) > 0$: $x<-2$ or $1<x<5$.
(c) Need to solve $x^3 - 3x^2 - x - 1 = 0$. Non-integer roots — in an exam the intersection points would be given or solved with a calculator.

**12. Differentiation for Extreme Values**:
(a) $f'(x) = 8x - 16 = 0 \Rightarrow x = 2$, $f''(x) = 8 > 0$, minimum $f(2) = 16 - 32 + 7 = -9$.
(b) $f'(x) = -10x + 30 = 0 \Rightarrow x = 3$, $f''(x) = -10 < 0$, maximum $f(3) = -45 + 90 - 41 = 4$.
(c) $f'(x) = 4x + k$, $f'(-2) = -8 + k = 0 \Rightarrow k = 8$. $f''(x) = 4 > 0$, minimum $f(-2) = 8 - 16 + 3 = -5$.
(d) $f'(x) = -6x + m$, $f'(1) = -6 + m = 0 \Rightarrow m = 6$. $f''(x) = -6 < 0$, maximum $f(1) = -3 + 6 + 1 = 4$.
(e) $f'(x) = 2x - 10 = 0 \Rightarrow x = 5$, $f''(x) = 2 > 0$, minimum $f(5) = 25 - 50 + 28 = 3$. QED. ✓
(f) **Differentiation method**: $f'(x) = 6x - 18 = 0 \Rightarrow x = 3$, $f''(x) = 6 > 0$, minimum $f(3) = 27 - 54 + 25 = -2$.
**Completing the square**: $f(x) = 3(x^2 - 6x) + 25 = 3[(x - 3)^2 - 9] + 25 = 3(x - 3)^2 - 27 + 25 = 3(x - 3)^2 - 2$. Minimum $-2$ at $x=3$. ✓
**Comparison**: Differentiation requires only three steps (differentiate → set to zero → second derivative), while completing the square requires algebraic manipulation. For quadratic functions, both are equally manageable, but for more complex functions, differentiation is more advantageous.

</details>

---
---
