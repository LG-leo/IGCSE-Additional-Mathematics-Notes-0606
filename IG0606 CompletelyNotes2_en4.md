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

# Chapter 5: Functions (Linear, Cubic, Exponential, Logarithmic)

## Syllabus Mapping

This chapter covers all content from **Topic 1: Functions** and **Topic 6: Logarithmic and Exponential Functions** of the IGCSE 0606 Additional Mathematics (2028–2030) syllabus.

| Syllabus Ref | Corresponding Section |
|---------|---------|
| **1.1** Understand functions (including vertical line test), domain, range, one-one (horizontal line test), many-one, inverse functions, composite functions; explain whether a relation is a function | §4.1, §4.4 |
| **1.2** Find the domain and range of functions (including inverse and composite functions); understand domain restrictions for the existence of inverse/composite functions; understand $\text{Domain}(gf) \subseteq \text{Domain}(f)$, $\text{Range}(gf) \subseteq \text{Range}(g)$ | §4.1, §4.4 |
| **1.3** Recognise and use function notation: $f(x)$, $f:x \mapsto$, $f^{-1}(x)$, $fg(x)$, $f^2(x)$ ($f^2$ not used for trigonometric functions) | §4.1 |
| **1.4** Understand the relationship between $y=f(x)$ and $y=|f(x)|$, where $f(x)$ can be linear, quadratic, cubic or trigonometric (of the form $a\sin bx+c$, $a\cos bx+c$, $a\tan bx+c$) | §4.5 |
| **1.5** Explain in words why a given function does not have an inverse | §4.4 |
| **1.6** Find the inverse of a one-one function (e.g., inverse of $f(x)=e^{2x}$ is $\frac12\ln x$) | §4.4 |
| **1.7** Construct and use composite functions, understanding that $fg$ is generally not equal to $gf$ | §4.4 |
| **1.8** Sketch the relationship between a function and its inverse being symmetrical about $y=x$ | §4.4 |
| **6.1** Know and use the properties and graphs of logarithmic and exponential functions (including $\ln x$ and $e^x$, asymptotes) | §4.3 |
| **6.2** Know and use the laws of logarithms (including the change of base formula) | §4.3 |
| **6.3** Solve equations of the form $a^x = b$ | §4.3 |

> **Learning path**: §4.1 (Conceptual foundations) → §4.2 (Linear and cubic) → §4.3 (Exponential and logarithmic) → §4.4 (Inverse and composite) → §4.5 (Absolute value graphs) → Practice problems

---

## 5.1 Fundamental Concepts of Functions

### 5.1.1 What is a Function?

A function is a special type of relation: it maps **each** input value $x$ in the **domain** to **exactly one** output value $y = f(x)$. We say $y$ is the **image** of $x$.

$$
f: D \to \mathbb{R}, \quad x \mapsto f(x)
$$

where $D$ is the domain, and the **range (image set)** is the set of all possible output values $f(x)$.

**Required condition for a function**: For every $x$ in the domain, there must be one and only one corresponding $y$. This is the **vertical line test** — any vertical line intersects the graph of a function at most once.

**How to explain whether a relation is a function** (Syllabus 1.1):

For each value of $x$ in the domain, the relation gives exactly one value of $y$.

- $y = x^2$ **is** a function: each $x$ corresponds to exactly one $y$.
- $x = y^2$ **is not** a function: e.g., when $x=4$, $y$ can be $2$ or $-2$, one $x$ corresponds to two $y$'s.
- $y = \pm\sqrt{x}$ **is not** a function: each positive $x$ corresponds to two $y$ values.

### 5.1.2 One–One (Injective) and Many–One Functions

- **One–one function (injective)**: Different $x$ values in the domain correspond to different $y$ values. That is: if $x_1 \neq x_2$, then $f(x_1) \neq f(x_2)$. Test method — **horizontal line test**: any horizontal line intersects the graph at most once.

- **Many–one function**: Different $x$ values can correspond to the same $y$ value. For example $f(x) = x^2$, $f(2) = f(-2) = 4$. The horizontal line $y=4$ intersects the graph at two points.

> ⚠️ **Only one–one functions have inverses**. This is because the inverse function needs to uniquely map each output value back to an input value — if the original function is many–one, the inverse would be one–many, which violates the definition of a function.

### 5.1.3 Function Notation

Function notation used in IGCSE 0606 includes:

- **$f(x)$**: The most common notation, e.g., $f(x) = 2e^x$
- **$f: x \mapsto$**: Mapping notation, e.g., $f: x \mapsto \lg x$, meaning "$f$ maps $x$ to $\lg x$"
- **$f^{-1}(x)$**: Inverse function notation
- **$fg(x)$**: Composite function notation, $fg(x) = f(g(x))$
- **$f^2(x)$**: Denotes $f(f(x))$, i.e., $f$ composed with itself

> ⚠️ **Important**: The notation $f^2(x)$ **does not apply to trigonometric functions**. For example, $\sin^2 x$ means $(\sin x)^2$, not $\sin(\sin x)$.

### 5.1.4 Finding Domain and Range

Restrictions to consider when finding the domain:

1. **Denominator not zero**: $f(x) = \dfrac{1}{g(x)} \Rightarrow g(x) \neq 0$
2. **Even root radicand non-negative**: $f(x) = \sqrt{g(x)} \Rightarrow g(x) \geq 0$
3. **Logarithm argument positive**: $f(x) = \log_a(g(x)) \Rightarrow g(x) > 0$

**Methods for finding range**:

**Method 1 — Completing the square** (for quadratic functions):
Write $f(x) = ax^2 + bx + c$ in the form $a(x-h)^2 + k$.
- If $a > 0$, minimum is $k$, range is $[k, \infty)$
- If $a < 0$, maximum is $k$, range is $(-\infty, k]$

**Method 2 — Observation** (for monotonic functions):
If the function is strictly increasing or decreasing on its domain, the range is the interval between the function values at the endpoints.

**Method 3 — Inverse function method**:
If the function has an inverse, the range of the original function equals the domain of the inverse.

---

### Worked Examples 4.1 (Domain and Range)

**Example 1** (Basic — root and denominator): Find the domain of $f(x) = \sqrt{x-2} + \dfrac{1}{x-3}$.

**Solution**:

**Step 1** (root condition): $x-2 \geq 0 \Rightarrow x \geq 2$.

**Step 2** (denominator condition): $x-3 \neq 0 \Rightarrow x \neq 3$.

**Step 3** (intersection): Domain is $[2, 3) \cup (3, \infty)$.

---

**Example 2** (Composite — separating constant to find range): Function $f(x) = \dfrac{2x+1}{x-1}$, $x \neq 1$.

(i) Find the range;
(ii) Determine whether $f$ is one–one.

**Solution**:

(i) **Separate the constant**: Rewrite the numerator in terms of the denominator.

$$
f(x) = \frac{2x+1}{x-1} = \frac{2(x-1) + 3}{x-1}
$$

The idea: the denominator is $x-1$, we want $x-1$ in the numerator to simplify. Write $2x$ as $2(x-1) + 2$, plus the $1$ from the original numerator, giving $2(x-1) + 3$.

Continuing:

$$
f(x) = \frac{2(x-1)}{x-1} + \frac{3}{x-1} = 2 + \frac{3}{x-1}
$$

Since $\dfrac{3}{x-1} \neq 0$ for all $x \neq 1$, $f(x)$ can never equal $2$.

**Range is $\mathbb{R} \setminus \{2\}$**.

(ii) Check one–one: Suppose $f(a) = f(b)$:

$$
2 + \frac{3}{a-1} = 2 + \frac{3}{b-1}
$$

Subtract 2 from both sides:

$$
\frac{3}{a-1} = \frac{3}{b-1}
$$

Take reciprocals: $a-1 = b-1 \Rightarrow a = b$.

Therefore $f$ is one–one. Geometrically, $y = 2 + \dfrac{3}{x-1}$ is a reciprocal function after translation; each horizontal line (except $y=2$) intersects exactly once.

---

**Example 3** (Semi-circular range): Given $f(x) = \sqrt{4 - x^2}$.

(i) Find the domain and range;
(ii) Determine whether $f$ has an inverse.

**Solution**:

(i) **Domain**: $4 - x^2 \geq 0 \Rightarrow x^2 \leq 4 \Rightarrow -2 \leq x \leq 2$. Domain is $[-2, 2]$.

**Range**: Let $y = \sqrt{4 - x^2}$, then $y \geq 0$ and $y^2 = 4 - x^2$, i.e., $x^2 + y^2 = 4$ ($y \geq 0$).

This is the **upper semicircle** with centre at the origin and radius $2$. The minimum $y$ occurs at $x = \pm 2$, $y = 0$; the maximum occurs at $x = 0$, $y = 2$. Therefore the range is $[0, 2]$.

(ii) $f$ is not one–one because e.g., $f(-1) = f(1) = \sqrt{3}$. The horizontal line $y = \sqrt{3}$ intersects the upper semicircle at $(\pm 1, \sqrt{3})$, two points. Therefore $f$ has no inverse.

> However, if we restrict the domain to $x \in [0, 2]$, $f$ becomes one–one, and its inverse is $f^{-1}(x) = \sqrt{4 - x^2}$ (domain $[0, 2]$).

---

**Example 4** (Logarithm and fraction composite domain): Find the domain of $f(x) = \ln(3x - 6) + \dfrac{1}{\sqrt{8 - 2x}}$.

**Solution**:

**Condition 1** (logarithm argument > 0): $3x - 6 > 0 \Rightarrow x > 2$.

**Condition 2** (denominator radicand > 0 — since denominator cannot be zero and the root is in the denominator): $8 - 2x > 0 \Rightarrow x < 4$.

**Intersection**: $x > 2$ and $x < 4$, i.e., $(2, 4)$.

---

**Example 5** (Determining whether a relation is a function — Syllabus 1.1 requirement): Determine whether each relation is a function, and explain why.

(i) $y = \pm \sqrt{x}$, $x \geq 0$
(ii) $y = x^3 - 2x + 1$
(iii) $x^2 + y^2 = 25$

**Solution**:

(i) **Not a function**. For the same $x$ (e.g., $x=4$), the relation gives two $y$ values: $y = 2$ and $y = -2$. This violates the definition that **each input corresponds to exactly one output**. The vertical line $x=4$ intersects the graph at two points.

(ii) **Is a function**. For every real number $x$, $x^3 - 2x + 1$ computes exactly one real number $y$. The vertical line test passes at every $x$.

(iii) **Not a function**. For example, when $x=0$, $y^2 = 25 \Rightarrow y = \pm 5$, one $x$ corresponds to two $y$ values. The vertical line $x=0$ intersects the circle at $(0,5)$ and $(0,-5)$, two points.

---

## 5.2 Linear Functions and Cubic Functions

### 5.2.1 Linear Functions $f(x) = mx + c$

Linear functions are the simplest type of function. Their graph is a straight line.

**Geometric meaning of slope $m$**: For each $1$ unit increase in $x$, $y$ increases by $m$ units. If $m > 0$, the line slopes upward to the right; $m < 0$, slopes downward to the right; $m = 0$, horizontal line.

**Intercept $c$**: The $y$-coordinate of the point where the line crosses the $y$-axis, i.e., the value of $f(0)$.

**Rate of change characteristic**: The rate of change of a linear function is **constant** — at any point, the instantaneous rate of change equals $m$. This is the most important property that distinguishes linear functions from other types.

Finding slope from two points $(x_1, y_1)$ and $(x_2, y_2)$:

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

The reasoning: the vertical change between the two points is $y_2 - y_1$, the horizontal change is $x_2 - x_1$, and the slope is the "rise over run."

**Point-slope form**: The equation of a line through point $(x_0, y_0)$ with slope $m$ is:

$$
y - y_0 = m(x - x_0)
$$

### 5.2.2 Cubic Functions $f(x) = ax^3 + bx^2 + cx + d$ ($a \neq 0$)

The graph of a cubic function has an S-shape (or inverted S-shape). Its derivative $f'(x) = 3ax^2 + 2bx + c$ is a quadratic function, which may have two zeros (corresponding to local extreme points), or only one, or no real zeros.

**Two basic forms of cubic functions**:

1. **Product of three linear factors**: $f(x) = a(x - p)(x - q)(x - r)$, intersecting the $x$-axis at $x = p, q, r$.
2. **Product of one linear factor and one quadratic factor**: $f(x) = (x - p)(Ax^2 + Bx + C)$, which may have only one real root.

**End behaviour (leading term test)**:
- If $a > 0$: as $x \to -\infty$, $f(x) \to -\infty$; as $x \to \infty$, $f(x) \to \infty$.
- If $a < 0$: as $x \to -\infty$, $f(x) \to \infty$; as $x \to \infty$, $f(x) \to -\infty$.

---

### Worked Examples 4.2 (Linear and Cubic Functions)

**Example 1** (Linear function parameter finding): Line $L$ passes through points $A(2, 5)$ and $B(4, 11)$.

(i) Find the equation of $L$;
(ii) Find the $x$-intercept and $y$-intercept of $L$.

**Solution**:

(i) **Find the slope**:

$$
m = \frac{11 - 5}{4 - 2} = \frac{6}{2} = 3
$$

**Write the equation**: Using point-slope form with $A(2, 5)$:

$$
y - 5 = 3(x - 2)
$$

Simplifying:

$$
y - 5 = 3x - 6 \Rightarrow y = 3x - 1
$$

(ii) **$y$-intercept**: Set $x = 0$, $y = 3(0) - 1 = -1$, i.e., $(0, -1)$.

**$x$-intercept**: Set $y = 0$, $0 = 3x - 1 \Rightarrow x = \dfrac{1}{3}$, i.e., $\left(\dfrac{1}{3}, 0\right)$.

---

**Example 2** (Cubic function graph and extreme values): Given $f(x) = x^3 - 3x^2 + 2$.

(i) Find $f'(x)$ and solve $f'(x) = 0$;
(ii) Determine the type of stationary points;
(iii) Find the intercepts of $f$ with the coordinate axes.

**Solution**:

(i) **Differentiate**:

$$
f'(x) = \frac{d}{dx}(x^3) - \frac{d}{dx}(3x^2) + \frac{d}{dx}(2) = 3x^2 - 6x
$$

Factorise: $f'(x) = 3x(x - 2)$.

Set $f'(x) = 0$: $3x(x-2) = 0$, giving $x = 0$ or $x = 2$.

(ii) Use the first derivative sign test to check monotonicity around each stationary point:

**At $x = 0$**:
- Take $x = -1$ (to the left): $f'(-1) = 3(-1)(-3) = 9 > 0$, increasing
- Take $x = 1$ (to the right): $f'(1) = 3(1)(-1) = -3 < 0$, decreasing
- Left to right: increasing → decreasing → **local maximum**. $f(0) = 2$.

**At $x = 2$**:
- Take $x = 1$ (to the left): $f'(1) = -3 < 0$, decreasing
- Take $x = 3$ (to the right): $f'(3) = 3(3)(1) = 9 > 0$, increasing
- Left to right: decreasing → increasing → **local minimum**. $f(2) = 8 - 12 + 2 = -2$.

(iii) **$y$-intercept**: $f(0) = 2$, i.e., $(0, 2)$.

**$x$-intercept**: Solve $x^3 - 3x^2 + 2 = 0$.

Try rational roots. Test $x = 1$: $f(1) = 1 - 3 + 2 = 0$, so $x-1$ is a factor.

Factorise by synthetic division:

$$
\begin{array}{c|ccc}
1 & 1 & -3 & 0 & 2 \\
  &   & 1  & -2 & -2 \\
\hline
  & 1 & -2 & -2 & 0
\end{array}
$$

The quotient is $x^2 - 2x - 2$. Use the quadratic formula:

$$
x = \frac{2 \pm \sqrt{4 - 4(1)(-2)}}{2(1)} = \frac{2 \pm \sqrt{4 + 8}}{2} = \frac{2 \pm \sqrt{12}}{2} = \frac{2 \pm 2\sqrt{3}}{2} = 1 \pm \sqrt{3}
$$

Three $x$-intercepts: $x = 1$, $x = 1 + \sqrt{3}$, $x = 1 - \sqrt{3}$.

---

**Example 3** (Sign analysis and inequalities of cubic functions): Given $f(x) = (x+2)(x-1)(x-3)$.

(i) Find the solutions of $f(x) = 0$;
(ii) Solve $f(x) > 0$;
(iii) Sketch the graph of $y = f(x)$.

**Solution**:

(i) Set each linear factor to zero: $x = -2$, $x = 1$, $x = 3$.

(ii) Divide the real number line into four intervals using the three zeros. Pick a test point in each interval, determine the sign of each factor, and multiply the three signs to get the sign of $f(x)$:

| Interval | Test point | $(x+2)$ | $(x-1)$ | $(x-3)$ | Product sign |
|------|--------|---------|---------|---------|---------|
| $x < -2$ | $x = -3$ | $-1$ (negative) | $-4$ (negative) | $-6$ (negative) | neg × neg × neg = **negative** |
| $-2 < x < 1$ | $x = 0$ | $2$ (positive) | $-1$ (negative) | $-3$ (negative) | pos × neg × neg = **positive** |
| $1 < x < 3$ | $x = 2$ | $4$ (positive) | $1$ (positive) | $-1$ (negative) | pos × pos × neg = **negative** |
| $x > 3$ | $x = 4$ | $6$ (positive) | $3$ (positive) | $1$ (positive) | pos × pos × pos = **positive** |

Therefore $f(x) > 0$ for $-2 < x < 1$ or $x > 3$.

(iii) Sketch key points:
- $x$-intercepts: $(-2, 0)$, $(1, 0)$, $(3, 0)$
- $y$-intercept: $f(0) = (2)(-1)(-3) = 6$
- End behaviour: $a = 1 > 0$, so as $x \to -\infty$, $f \to -\infty$; as $x \to \infty$, $f \to \infty$
- The graph crosses the $x$-axis at each of the three zeros

---

**Example 4** (Factor theorem and cubic factorisation): Given that $f(x) = x^3 + kx^2 - 4x - 4$ is exactly divisible by $x+1$, find $k$ and fully factorise $f(x)$.

**Solution**:

**Step 1** (Apply the factor theorem): If $x+1$ is a factor, then $f(-1) = 0$.

$$
f(-1) = (-1)^3 + k(-1)^2 - 4(-1) - 4 = -1 + k + 4 - 4 = k - 1
$$

Set $f(-1) = 0$: $k - 1 = 0 \Rightarrow k = 1$.

**Step 2** (Synthetic division): $f(x) = x^3 + x^2 - 4x - 4$.

Divide by $(x+1)$:

$$
\begin{array}{c|ccc}
-1 & 1 & 1 & -4 & -4 \\
   &   & -1 & 0 & 4 \\
\hline
   & 1 & 0 & -4 & 0
\end{array}
$$

The quotient is $x^2 - 4 = (x-2)(x+2)$.

**Step 3** (Write the complete factorisation):

$$
f(x) = (x+1)(x-2)(x+2)
$$

---

## 5.3 Exponential Functions and Logarithmic Functions

> **Prerequisite Knowledge**: If you are already familiar with exponential operations (e.g., $2^3 = 8$) and logarithms (e.g., $\log_2 8 = 3$), you can skip ahead directly to §4.3.1. If this is your first encounter, the following content will help you build an intuitive understanding.

**Exponents** and **logarithms** are like a pair of "opposites" — one asks "what is the result?", the other asks "how many times was it used?"

---

**🔢 Exponents — Repeated Multiplication**

The exponential operation $a^n$ means "multiply $a$ by itself $n$ times":

$$
2^3 = 2 \times 2 \times 2 = 8
$$

Here $a$ is called the **base**, $n$ is called the **exponent**, and the result $8$ is called the **power**.

A classic example of **exponential growth**: fold a sheet of paper once and it becomes 2 layers, fold twice and it becomes 4 layers. After $x$ folds, the number of layers is $2^x$. This is why exponential growth is so astonishing — after 10 folds, it exceeds 1000 layers.

---

**🔄 Logarithms — The "Reverse Operation" of Exponents**

A logarithm answers: **"How many times must the base $a$ be multiplied to obtain $x$?"**

$$
\log_2 8 = 3 \quad\Longleftrightarrow\quad 2^3 = 8
$$

Read as: "the logarithm of $8$ to the base $2$ is $3$", meaning "$2$ needs to be multiplied $3$ times to get $8$".

| Exponential form | Logarithmic form | How to read it |
|:---|:---|:---|
| $2^3 = 8$ | $\log_2 8 = 3$ | The logarithm of 8 to the base 2 is 3 |
| $10^2 = 100$ | $\log_{10} 100 = 2$ | The logarithm of 100 to the base 10 is 2 |
| $e^1 = e$ | $\ln e = 1$ | The natural logarithm of $e$ is 1 |

**Key insight**: Exponents and logarithms are **inverse operations** — just like addition and subtraction, multiplication and division.

$$
\underbrace{2^3 = 8}_{\text{Exponential: given base and exponent, find the power}} \quad \Longleftrightarrow \quad \underbrace{\log_2 8 = 3}_{\text{Logarithm: given base and power, find the exponent}}
$$

---

**📊 Why Are They So Important?**

Exponential functions describe processes that "grow faster and faster":
- Bacterial reproduction (doubles every 20 minutes)
- Compound interest (interest earning interest)
- Radioactive decay (substance decreasing over time)

Logarithmic functions "compress" this explosive growth into a readable scale:
- The Richter scale for earthquakes ($\log$ scale)
- Decibels for sound ($\log$ scale)
- pH values ($\log$ scale)

---

**🗺️ Learning Path for This Section**

```
Exponential function $a^x$         Logarithmic function $\log_a x$
       ↓                                  ↑
       ├── Basic properties ────────────┤ Mutually inverse
       ├── Natural base $e$              └── Laws (product, quotient, power, change of base)
       └── Graphs and asymptotes              └── Solving exponential equations $a^x = b$
```

---

### 5.3.1 Exponential Functions $f(x) = a^x$ ($a > 0$, $a \neq 1$)

The core characteristic of an exponential function is that the rate of growth (or decay) is proportional to the function value itself.

**Graph properties** (taking $a > 1$ as an example):
- Domain: $\mathbb{R}$ (all real numbers)
- Range: $(0, \infty)$ (always positive)
- Always passes through $(0, 1)$, because $a^0 = 1$
- When $a > 1$, the function is strictly increasing; when $0 < a < 1$, strictly decreasing
- **Horizontal asymptote**: $y = 0$ (the $x$-axis). When $a > 1$, approaches $y=0$ as $x \to -\infty$; when $0 < a < 1$, approaches $y=0$ as $x \to \infty$

**More general form**: $y = k e^{nx} + a$
- Horizontal asymptote is $y = a$
- $k$ controls vertical stretch and direction ($k > 0$ means the graph is above the asymptote, $k < 0$ means below)

**Why is $e$ so important?**

$$
\frac{d}{dx}e^x = e^x
$$

$e^x$ is the **only function whose derivative equals itself**. For a general base $a$:

$$
\frac{d}{dx}a^x = a^x \ln a
$$

When $a = e$, $\ln e = 1$, and the derivative simplifies to $e^x$ itself.

### 5.3.2 Detailed Derivation of the Natural Exponential Function $e^x$

**Question**: Does there exist a number $e$ such that the derivative of $e^x$ equals $e^x$?

Start from the general exponential function $f(x) = a^x$. By the definition of the derivative:

$$
f'(x) = \lim_{h \to 0} \frac{a^{x+h} - a^x}{h}
$$

**Step 1**: Factor out $a^x$:

$$
f'(x) = \lim_{h \to 0} \frac{a^x(a^h - 1)}{h} = a^x \cdot \lim_{h \to 0} \frac{a^h - 1}{h}
$$

**Step 2**: Denote $L(a) = \displaystyle\lim_{h \to 0} \frac{a^h - 1}{h}$. This limit depends on $a$. So:

$$
f'(x) = a^x \cdot L(a) = f(x) \cdot L(a)
$$

**Step 3**: We want $L(a) = 1$, so that $f'(x) = f(x)$. Solving $L(a) = 1$ numerically:

| $a$ | $L(a) \approx \dfrac{a^{0.001} - 1}{0.001}$ |
|-----|-------------------------------------------|
| $2$ | $\approx 0.693$ |
| $2.7$ | $\approx 0.993$ |
| $2.71$ | $\approx 0.996$ |
| $2.718$ | $\approx 0.999$ |
| $2.71828$ | $\approx 1.000$ |

This special number is $e \approx 2.71828$, which can also be defined as a limit:

$$
e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
$$

**Numerical verification**:
- $n = 1$: $(1+1)^1 = 2$
- $n = 10$: $(1.1)^{10} \approx 2.594$
- $n = 100$: $(1.01)^{100} \approx 2.705$
- $n = 10000$: $(1.0001)^{10000} \approx 2.718$

### 5.3.3 Logarithmic Functions $f(x) = \log_a x$ ($a > 0$, $a \neq 1$)

The logarithmic function is the **inverse** of the exponential function:

$$
y = \log_a x \iff a^y = x \quad (x > 0)
$$

**Graph properties** (taking $a > 1$ as an example):
- Domain: $(0, \infty)$ (the argument must be positive)
- Range: $\mathbb{R}$
- Always passes through $(1, 0)$, because $\log_a 1 = 0$
- When $a > 1$, the function is strictly increasing; when $0 < a < 1$, strictly decreasing
- **Vertical asymptote**: $x = 0$ (the $y$-axis). When $a > 1$, as $x \to 0^+$, $\log_a x \to -\infty$

**More general form**: $y = k \ln(ax + b)$
- Vertical asymptote at $ax + b = 0$, i.e., $x = -\dfrac{b}{a}$
- Domain is $x > -\dfrac{b}{a}$

**Two important special bases**:
- **Common logarithm** (base $10$): $\log_{10} x$, sometimes written as $\lg x$
- **Natural logarithm** (base $e$): $\log_e x$, written as $\ln x$

**Exponential and logarithmic functions are inverses of each other**:

$$
y = a^x \quad \stackrel{\text{inverse}}{\longleftrightarrow} \quad y = \log_a x
$$

**Derivation of symmetry**:
Suppose point $(p, q)$ lies on $y = a^x$, then $q = a^p$.
By the definition of the logarithm, $p = \log_a q$, so point $(q, p)$ lies on $y = \log_a x$.
Point $(p, q)$ reflected across the line $y = x$ is exactly $(q, p)$ (because the coordinates are swapped).
Therefore the graphs of the two functions are symmetrical about $y = x$.

### 5.3.4 Detailed Derivation of Logarithmic Laws

The essence of logarithm laws is **downgrading** the operation — multiplication becomes addition, division becomes subtraction, and exponents become coefficients.

**Law 1 — Logarithm of a product**: $\log_a (MN) = \log_a M + \log_a N$

*Derivation*:
Let $\log_a M = x$, $\log_a N = y$.
By definition of the logarithm: $a^x = M$, $a^y = N$.
Then $MN = a^x \cdot a^y = a^{x+y}$.
By the definition of the logarithm again: $\log_a (MN) = x + y = \log_a M + \log_a N$. $\square$

**Law 2 — Logarithm of a quotient**: $\log_a \left(\dfrac{M}{N}\right) = \log_a M - \log_a N$

*Derivation*:
Let $\log_a M = x$, $\log_a N = y$.
Then $\dfrac{M}{N} = \dfrac{a^x}{a^y} = a^{x-y}$.
Therefore $\log_a \left(\dfrac{M}{N}\right) = x - y = \log_a M - \log_a N$. $\square$

**Law 3 — Logarithm of a power**: $\log_a (M^k) = k \log_a M$

*Derivation*:
Let $\log_a M = x$, then $a^x = M$.
Then $M^k = (a^x)^k = a^{kx}$.
By definition: $\log_a (M^k) = kx = k \log_a M$. $\square$

**Law 4 — Change of base formula**: $\log_a M = \dfrac{\log_b M}{\log_b a}$

*Derivation*:
Let $y = \log_a M$, then $a^y = M$.
Take the logarithm to base $b$ of both sides:
$\log_b (a^y) = \log_b M$
$y \log_b a = \log_b M$
$y = \dfrac{\log_b M}{\log_b a}$
Therefore $\log_a M = \dfrac{\log_b M}{\log_b a}$. $\square$

The two most common applications of the change of base formula:

$$
\log_a M = \frac{\log M}{\log a} \quad \text{(change to common logarithm)},
\qquad
\log_a M = \frac{\ln M}{\ln a} \quad \text{(change to natural logarithm)}
$$

**Inverse identities** (directly from the definition of inverse functions):

$$
a^{\log_a x} = x \quad (x > 0), \qquad \log_a (a^x) = x \quad (x \in \mathbb{R})
$$

### 5.3.5 Solving Exponential Equations $a^x = b$

**Basic method**: Take logarithms of both sides, then use the power law to bring the exponent down as a coefficient.

$$
a^x = b \quad \Rightarrow \quad \ln(a^x) = \ln b \quad \Rightarrow \quad x \ln a = \ln b \quad \Rightarrow \quad x = \frac{\ln b}{\ln a}
$$

Common logarithms can also be used: $x = \dfrac{\log b}{\log a}$.

> ⚠️ **Note**: The equation has a real solution only when $b > 0$. If $b \leq 0$, the equation $a^x = b$ has no real solution (since the range of the exponential function is $(0, \infty)$).

---

### Worked Examples 4.3 (Exponential and Logarithmic Functions)

**Example 1** (Logarithm simplification and evaluation): Simplify $\log_2 24 - \log_2 3 + \log_2 \dfrac{1}{2}$.

**Solution**:

**Step 1** (Use the quotient law to combine the first two terms):

$$
\log_2 24 - \log_2 3 = \log_2 \frac{24}{3} = \log_2 8
$$

**Step 2** (Use the product law to continue):

$$
\log_2 8 + \log_2 \frac{1}{2} = \log_2 \left(8 \times \frac{1}{2}\right) = \log_2 4
$$

**Step 3** (Evaluate): $\log_2 4 = 2$, because $2^2 = 4$.

Therefore the value of the expression is $2$.

---

**Example 2** (Change of base and logarithmic equations):

(i) Express $\log_5 20$ in terms of natural logarithms and simplify;
(ii) Solve $\log_2 (x+1) + \log_2 (x-1) = 3$.

**Solution**:

(i) Using the change of base formula:

$$
\log_5 20 = \frac{\ln 20}{\ln 5}
$$

Factor $20 = 4 \times 5$, so $\ln 20 = \ln(4 \times 5) = \ln 4 + \ln 5 = \ln(2^2) + \ln 5 = 2\ln 2 + \ln 5$.

Therefore:

$$
\log_5 20 = \frac{2\ln 2 + \ln 5}{\ln 5} = \frac{2\ln 2}{\ln 5} + 1
$$

(ii) **Step 1** (Combine the logarithms):

$$
\log_2[(x+1)(x-1)] = 3 \Rightarrow \log_2(x^2 - 1) = 3
$$

**Step 2** (Remove the logarithm — exponentiate both sides base $2$):

$$
x^2 - 1 = 2^3 = 8
$$

**Step 3** (Solve the quadratic):

$$
x^2 = 9 \Rightarrow x = \pm 3
$$

**Step 4** (Check the domain): The arguments of logarithms must be positive.

$x+1 > 0 \Rightarrow x > -1$, $x-1 > 0 \Rightarrow x > 1$. Intersection gives $x > 1$.

$x = 3 > 1$, valid. $x = -3$ does not satisfy $x > 1$, rejected.

Therefore $x = 3$.

---

**Example 3** (Solving exponential equations and exponential–logarithmic composites):

(i) Solve $3^{2x-1} = 7$, giving the result in terms of natural logarithms;
(ii) Given $f(x) = \ln(e^{2x} + 1)$, find $f(0)$.

**Solution**:

(i) Take natural logarithms of both sides:

$$
\ln(3^{2x-1}) = \ln 7
$$

Use the power law to bring the exponent down:

$$
(2x - 1)\ln 3 = \ln 7
$$

Solve for $x$:

$$
2x - 1 = \frac{\ln 7}{\ln 3} \Rightarrow 2x = 1 + \frac{\ln 7}{\ln 3} \Rightarrow x = \frac{1}{2}\left(1 + \frac{\ln 7}{\ln 3}\right)
$$

(ii) Substitute $x = 0$:

$$
f(0) = \ln(e^{0} + 1) = \ln(1 + 1) = \ln 2
$$

---

**Example 4** (Exponential equation — substitution method): Solve $4^x - 5 \cdot 2^x + 4 = 0$.

**Solution**:

**Step 1** (Identify the structure): Note that $4^x = (2^2)^x = 2^{2x} = (2^x)^2$.

**Step 2** (Substitute): Let $u = 2^x$, noting $u > 0$ (since the exponential function is always positive).

The equation becomes:

$$
u^2 - 5u + 4 = 0
$$

**Step 3** (Solve the quadratic):

$$
(u-1)(u-4) = 0 \Rightarrow u = 1 \text{ or } u = 4
$$

**Step 4** (Back-substitute):

- $2^x = 1 \Rightarrow x = \log_2 1 = 0$
- $2^x = 4 \Rightarrow x = \log_2 4 = 2$

Both solutions satisfy the domain, so $x = 0$ or $x = 2$.

---

**Example 5** (Logarithmic equation — change of base leading to a quadratic): Solve $\log_3 x + \log_x 3 = 2$.

**Solution**:

**Step 1** (Change of base): Use the change of base formula to express $\log_x 3$ in base $3$:

$$
\log_x 3 = \frac{\log_3 3}{\log_3 x} = \frac{1}{\log_3 x}
$$

**Step 2** (Substitute): Let $u = \log_3 x$ (note $x > 0$ and $x \neq 1$, otherwise $\log_x 3$ is undefined).

The equation becomes:

$$
u + \frac{1}{u} = 2
$$

**Step 3** (Clear denominators): Multiply both sides by $u$ ($u \neq 0$):

$$
u^2 + 1 = 2u \Rightarrow u^2 - 2u + 1 = 0 \Rightarrow (u-1)^2 = 0
$$

**Step 4** (Back-substitute): $u = 1 \Rightarrow \log_3 x = 1 \Rightarrow x = 3^1 = 3$.

**Verification**: $\log_3 3 = 1$, $\log_3 3 = 1$, $1 + 1 = 2$. $\checkmark$

---

**Example 6** (Exponential inequality — taking logarithms of both sides): Solve $2^x < 5$.

**Solution**:

Take natural logarithms of both sides. Since $\ln$ is an increasing function, the direction of the inequality **does not change**:

$$
\ln(2^x) < \ln 5
$$

Use the power law:

$$
x \ln 2 < \ln 5
$$

Since $\ln 2 > 0$, dividing both sides by $\ln 2$ does not change the inequality direction:

$$
x < \frac{\ln 5}{\ln 2}
$$

So the solution is $x < \dfrac{\ln 5}{\ln 2}$ (approximately $x < 2.322$).

> ⚠️ **Note**: If the base $a$ satisfies $0 < a < 1$, the inequality direction reverses when taking logarithms (because $\ln a < 0$). For example, solving $\left(\dfrac12\right)^x < 3$:
>
> $x\ln\frac12 < \ln 3$, since $\ln\frac12 < 0$, dividing both sides gives $x > \dfrac{\ln 3}{\ln(1/2)}$.

---

**Example 7** (Expressing unknown logarithms in terms of known ones): Given $\log_a 2 = p$, $\log_a 5 = q$. Express in terms of $p$ and $q$:

(i) $\log_a 20$;
(ii) $\log_a 0.4$.

**Solution**:

(i) $20 = 2^2 \times 5$, so:

$$
\log_a 20 = \log_a (2^2 \times 5) = \log_a 2^2 + \log_a 5 = 2\log_a 2 + \log_a 5 = 2p + q
$$

(ii) $0.4 = \dfrac{2}{5}$, so:

$$
\log_a 0.4 = \log_a \frac{2}{5} = \log_a 2 - \log_a 5 = p - q
$$

---

**Example 8** (Asymptotes and transformations of exponential function graphs — Syllabus 6.1): Function $f(x) = 3e^{2x} - 4$.

(i) Find the horizontal asymptote of $f(x)$;
(ii) Find the intercepts of $f(x)$ with the coordinate axes;
(iii) Describe the domain and range of $f$.

**Solution**:

(i) As $x \to -\infty$, $e^{2x} \to 0$, so $3e^{2x} - 4 \to -4$.

Thus the horizontal asymptote is $y = -4$.

(ii) **$y$-intercept**: Set $x = 0$, $f(0) = 3e^{0} - 4 = 3 - 4 = -1$, i.e., $(0, -1)$.

**$x$-intercept**: Set $f(x) = 0$:

$$
3e^{2x} - 4 = 0 \Rightarrow e^{2x} = \frac{4}{3}
$$

Take natural logarithms of both sides: $2x = \ln\frac{4}{3} \Rightarrow x = \dfrac12\ln\frac{4}{3}$.

The $x$-intercept is $\left(\dfrac12\ln\frac{4}{3}, 0\right)$.

(iii) **Domain**: $\mathbb{R}$ (all real numbers).

**Range**: Since $e^{2x} > 0$ for all real $x$, $3e^{2x} > 0$, $3e^{2x} - 4 > -4$. Range is $(-4, \infty)$.

---

**Example 9** (Asymptotes of logarithmic function graphs — Syllabus 6.1): Function $g(x) = 2\ln(x-1) + 3$.

(i) Find the domain and vertical asymptote of $g(x)$;
(ii) Find the intercepts of $g(x)$ with the coordinate axes.

**Solution**:

(i) **Domain**: The argument must be positive: $x-1 > 0 \Rightarrow x > 1$. Domain is $(1, \infty)$.

**Vertical asymptote**: Occurs where the argument is zero: $x-1 = 0 \Rightarrow x = 1$. As $x \to 1^+$, $\ln(x-1) \to -\infty$, $g(x) \to -\infty$.

Therefore the vertical asymptote is $x = 1$.

(ii) **$y$-intercept**: $x = 0$ is not in the domain, so there is no $y$-intercept.

**$x$-intercept**: Set $g(x) = 0$:

$$
2\ln(x-1) + 3 = 0 \Rightarrow \ln(x-1) = -\frac{3}{2}
$$

Exponentiate both sides: $x - 1 = e^{-3/2} \Rightarrow x = 1 + e^{-3/2}$.

The $x$-intercept is $(1 + e^{-3/2}, 0)$ (approximately $(1.223, 0)$).

---

## 5.4 Inverse Functions and Composite Functions

### 5.4.1 Inverse Functions

**Definition**: If a function $f$ is one–one (injective), then it has an inverse $f^{-1}$, satisfying:

$$
f^{-1}(y) = x \iff f(x) = y
$$

**Core properties**:

$$
f^{-1}(f(x)) = x, \qquad f(f^{-1}(x)) = x
$$

**Geometric meaning**: The graphs of $y = f(x)$ and $y = f^{-1}(x)$ are symmetrical about the line $y = x$.

**Detailed derivation of symmetry**:

Let point $(a, b)$ lie on $y = f(x)$, i.e., $b = f(a)$.
By the definition of the inverse, $a = f^{-1}(b)$, so point $(b, a)$ lies on $y = f^{-1}(x)$.
Point $(a, b)$ reflected across the line $y = x$ is exactly $(b, a)$ (because the coordinates are swapped).
Therefore the graphs of $f$ and $f^{-1}$ are mirror images of each other across $y = x$.

**Example**: For $f(x) = 2^x$ and $f^{-1}(x) = \log_2 x$:
- $f$ passes through $(0, 1)$, $(1, 2)$, $(2, 4)$
- $f^{-1}$ passes through $(1, 0)$, $(2, 1)$, $(4, 2)$
- Each pair of points is symmetrical about $y = x$

**Why do only one–one functions have inverses?**

If $f$ is not one–one (i.e., there exist $x_1 \neq x_2$ such that $f(x_1) = f(x_2) = y_0$), then the inverse $f^{-1}$ would need to return two different values — $x_1$ and $x_2$ — at $x = y_0$, which violates the definition of a function. Therefore non–one–one functions have no inverses.

**How to explain in words why a function has no inverse** (Syllabus 1.5 standard wording):

"The function $f$ is not one–one because different $x$ values correspond to the same $y$ value. For example, $f(a) = f(b)$ but $a \neq b$. The horizontal line $y = f(a)$ intersects the graph of $y = f(x)$ at more than one point. Therefore $f$ has no inverse."

**Steps for finding the inverse**:
1. Write $y = f(x)$ as an equation.
2. Solve for $x$ in terms of $y$.
3. Swap the roles of $x$ and $y$ to obtain the expression $y = f^{-1}(x)$.
4. State the domain of the inverse function (which is the range of the original function).

**Relationship between the domain and range of a function and its inverse**:
- Domain of $f$ = Range of $f^{-1}$
- Range of $f$ = Domain of $f^{-1}$

> ⚠️ **Key point**: Sometimes the domain of the original function must be **restricted** to make $f$ one–one, so that an inverse exists. For example, $f(x) = x^2$ is not one–one on all of $\mathbb{R}$, but restricting to $x \geq 0$ makes it one–one, and the inverse becomes $\sqrt{x}$.

### 5.4.2 Composite Functions

**Definition**: $(f \circ g)(x) = f(g(x))$, read as "$f$ composed with $g$", also written as $fg(x)$.

**Order of composition**: Apply $g$ first, then apply $f$ to the result. The order is usually not commutative — generally $f(g(x)) \neq g(f(x))$.

**Domain of a composite function**: Two conditions must be satisfied:
1. $x$ must be in the domain of $g$
2. $g(x)$ must be in the domain of $f$

**Important relationships** (Syllabus 1.2):

$$
\text{Domain}(gf) \subseteq \text{Domain}(f), \qquad \text{Range}(gf) \subseteq \text{Range}(g)
$$

> Explanation: To compute $gf(x) = g(f(x))$, $x$ must first be in the domain of $f$, and $f(x)$ must be in the domain of $g$. Therefore the domain of $gf$ is a subset of the domain of $f$. The output of $gf$ comes from $g$, so its range is a subset of the range of $g$.

**Further explanation of domain restrictions for the existence of composite functions**:

Sometimes the domain of $f$ needs to be restricted for $gf$ to exist. This is because $f(x)$ must lie within the domain of $g$.

*Example*: Given $f(x) = x^2$ (domain $\mathbb{R}$), $g(x) = \sqrt{1 - x^2}$ (domain $|x| \leq 1$).

$gf(x) = g(f(x)) = \sqrt{1 - (x^2)^2} = \sqrt{1 - x^4}$.

The domain of $gf$ requires $1 - x^4 \geq 0 \Rightarrow |x| \leq 1$.

So $\text{Domain}(gf) = [-1, 1] \subset \mathbb{R} = \text{Domain}(f)$.

---

### Worked Examples 4.4 (Inverse Functions and Composite Functions)

**Example 1** (Finding the inverse — linear function): Find the inverse of $f(x) = \dfrac{2x - 3}{5}$.

**Solution**:

**Step 1** (Write the equation): $y = \dfrac{2x - 3}{5}$

**Step 2** (Solve for $x$):

$$
5y = 2x - 3 \Rightarrow 2x = 5y + 3 \Rightarrow x = \frac{5y + 3}{2}
$$

**Step 3** (Swap $x$ and $y$):

$$
f^{-1}(x) = \frac{5x + 3}{2}
$$

**Step 4** (Domain): The domain of the inverse is $\mathbb{R}$ (the range of the original function is $\mathbb{R}$).

**Verification**:

$$
f(f^{-1}(x)) = f\left(\frac{5x+3}{2}\right) = \frac{2\cdot\frac{5x+3}{2} - 3}{5} = \frac{5x+3-3}{5} = x
$$

---

**Example 2** (Finding the inverse — with domain restriction): Given $f(x) = x^2 - 4x + 3$, $x \geq 2$. Find $f^{-1}(x)$ and its domain.

**Solution**:

**Step 1** (Complete the square to find the vertex and range):

$$
f(x) = x^2 - 4x + 3 = (x^2 - 4x + 4) - 4 + 3 = (x-2)^2 - 1
$$

The vertex is at $(2, -1)$. Since $a = 1 > 0$ and the domain is $x \geq 2$ (to the right of the vertex), the function is strictly increasing. The range is $[-1, \infty)$.

**Step 2** (Solve for $x$): Let $y = (x-2)^2 - 1$.

$$
y + 1 = (x-2)^2 \Rightarrow x - 2 = \pm \sqrt{y+1}
$$

Since $x \geq 2$, take the positive root: $x = 2 + \sqrt{y+1}$.

**Step 3** (Swap $x$ and $y$):

$$
f^{-1}(x) = 2 + \sqrt{x+1}
$$

**Step 4** (Domain): The domain of the inverse is the range of the original function, i.e., $[-1, \infty)$.

**Verification**:

$$
f(f^{-1}(x)) = f(2 + \sqrt{x+1}) = (2+\sqrt{x+1} - 2)^2 - 1 = (x+1) - 1 = x
$$

---

**Example 3** (Composite function and its domain — detailed derivation): Given $f(x) = \sqrt{x-1}$, $g(x) = \dfrac{1}{x-2}$.

(i) Find $fg(x)$ and its domain;
(ii) Find $gf(x)$ and its domain.

**Solution**:

(i) $fg(x) = f(g(x)) = \sqrt{\dfrac{1}{x-2} - 1}$

**Domain analysis**:

**Condition 1**: $g(x)$ must be defined. Denominator non-zero: $x \neq 2$.

**Condition 2**: $g(x)$ must lie in the domain of $f$. $f$'s domain requires the radicand $\geq 0$, i.e.:

$$
\frac{1}{x-2} - 1 \geq 0
$$

Solve this inequality. This is the key step — consider cases:

*Case A*: $x > 2$. Multiply both sides by the positive number $(x-2)$, the inequality sign stays the same:

$$
1 \geq x - 2 \Rightarrow x \leq 3
$$

Combining with $x > 2$, we get $2 < x \leq 3$.

*Case B*: $x < 2$. Multiply both sides by the negative number $(x-2)$, the inequality sign reverses:

$$
1 \leq x - 2 \Rightarrow x \geq 3
$$

Combining with $x < 2$, there is no solution.

Therefore condition 2 gives $2 < x \leq 3$.

**Intersection**: $x \neq 2$ and $2 < x \leq 3$, the domain is $(2, 3]$.

**Simplify the expression**:

$$
\frac{1}{x-2} - 1 = \frac{1 - (x-2)}{x-2} = \frac{3 - x}{x-2}
$$

Therefore:

$$
fg(x) = \sqrt{\frac{3 - x}{x - 2}}, \quad x \in (2, 3]
$$

(ii) $gf(x) = g(f(x)) = \dfrac{1}{\sqrt{x-1} - 2}$

**Domain analysis**:

**Condition 1**: $f(x)$ must be defined. Radicand non-negative: $x - 1 \geq 0 \Rightarrow x \geq 1$.

**Condition 2**: $f(x)$ must lie in $g$'s domain. $g$'s denominator cannot be zero: $\sqrt{x-1} - 2 \neq 0$.

$$
\sqrt{x-1} \neq 2 \Rightarrow x-1 \neq 4 \Rightarrow x \neq 5
$$

**Intersection**: $x \geq 1$ and $x \neq 5$, the domain is $[1, 5) \cup (5, \infty)$.

---

**Example 4** (Range of composite functions and $fg \neq gf$): $f(x) = 2^x$, $g(x) = x^2$. Find expressions for $fg(x)$ and $gf(x)$, and find the range of $fg(x)$.

**Solution**:

**$fg(x)$**: $fg(x) = f(g(x)) = 2^{x^2}$

**$gf(x)$**: $gf(x) = g(f(x)) = (2^x)^2 = 2^{2x} = 4^x$

Note that $fg(x) = 2^{x^2} \neq 4^x = gf(x)$, showing that the order of composition matters.

**Find the range of $fg(x)$**:
- $g(x) = x^2$ has range $[0, \infty)$
- $f(u) = 2^u$ is strictly increasing on $[0, \infty)$
- Minimum: when $u = 0$, $2^0 = 1$
- Upper bound: as $u \to \infty$, $2^u \to \infty$

Therefore the range of $fg(x)$ is $[1, \infty)$.

---

**Example 5** (Explaining in words why a function has no inverse — Syllabus 1.5):

(i) $f(x) = x^2$, domain $\mathbb{R}$.
(ii) $f(x) = \cos x$, domain $[0, 2\pi]$.

**Solution**:

(i) $f(x) = x^2$ **is not one–one** because different $x$ values correspond to the same $y$ value. For example, $f(2) = 4$ and $f(-2) = 4$, i.e., $2 \neq -2$ but $f(2) = f(-2)$. The horizontal line $y = 4$ intersects the graph of $y = x^2$ at $(2, 4)$ and $(-2, 4)$, two points. Therefore $f$ has no inverse.

> However, if we restrict the domain to $x \geq 0$, then $f$ becomes one–one, and the inverse is $f^{-1}(x) = \sqrt{x}$.

(ii) $f(x) = \cos x$ **is not one–one** on $[0, 2\pi]$. For example, $\cos(\frac{\pi}{3}) = \frac12$ and $\cos(\frac{5\pi}{3}) = \frac12$, but $\frac{\pi}{3} \neq \frac{5\pi}{3}$. The horizontal line $y = \frac12$ intersects the graph at two points. Therefore $f$ has no inverse.

> However, if we restrict the domain to $[0, \pi]$, $\cos x$ is strictly decreasing, and the inverse is $\arccos x$.

---

**Example 6** (Sketching the symmetrical relationship between a function and its inverse about $y=x$ — Syllabus 1.8): Given $f(x) = e^x$.

(i) Find $f^{-1}(x)$;
(ii) Describe the relationship between $y = f(x)$, $y = f^{-1}(x)$ and $y = x$ on the same coordinate axes.

**Solution**:

(i) $y = e^x \Rightarrow x = \ln y \Rightarrow f^{-1}(x) = \ln x$ (domain $x > 0$).

(ii) **Symmetry**: The graphs of $y = e^x$ and $y = \ln x$ are symmetrical about the line $y = x$.

Corresponding points:
- $e^x$ passes through $(0, 1)$ → $\ln x$ passes through $(1, 0)$
- $e^x$ passes through $(1, e)$ → $\ln x$ passes through $(e, 1)$
- $e^x$ passes through $(-1, e^{-1})$ → $\ln x$ passes through $(e^{-1}, -1)$

Each curve is the mirror image of the other in $y = x$.

**Asymptote relationship**:
- $y = e^x$ has a horizontal asymptote $y = 0$ (the $x$-axis)
- $y = \ln x$ has a vertical asymptote $x = 0$ (the $y$-axis)
- This pair of asymptotes is also symmetrical about $y = x$

---

**Example 7** (The importance of order in composite functions $fg \neq gf$ — Syllabus 1.7): $f(x) = 3x + 1$, $g(x) = x^2$. Find $fg(x)$ and $gf(x)$ and compare.

**Solution**:

$fg(x) = f(g(x)) = f(x^2) = 3x^2 + 1$

$gf(x) = g(f(x)) = g(3x+1) = (3x+1)^2 = 9x^2 + 6x + 1$

Clearly $fg(x) \neq gf(x)$, so the order of composition is crucial.

---

**Example 8** (Integrated application of inverse and composite functions): Given $f(x) = 2x + 3$, $g(x) = \dfrac{1}{x-1}$, $x \neq 1$.

(i) Find $f^{-1}(x)$;
(ii) Find $gf^{-1}(x)$ and its domain.

**Solution**:

(i) $y = 2x + 3 \Rightarrow 2x = y - 3 \Rightarrow x = \dfrac{y-3}{2}$
Swap: $f^{-1}(x) = \dfrac{x-3}{2}$, domain $\mathbb{R}$.

(ii) $gf^{-1}(x) = g\left(\dfrac{x-3}{2}\right) = \dfrac{1}{\dfrac{x-3}{2} - 1}$

Simplify the denominator: $\dfrac{x-3}{2} - 1 = \dfrac{x-3 - 2}{2} = \dfrac{x-5}{2}$

Therefore:

$$
gf^{-1}(x) = \frac{1}{\frac{x-5}{2}} = \frac{2}{x-5}
$$

**Domain**:
- $f^{-1}(x)$ has domain $\mathbb{R}$ (no restriction)
- $g$'s domain requires the denominator non-zero: $\dfrac{x-3}{2} - 1 \neq 0 \Rightarrow \dfrac{x-5}{2} \neq 0 \Rightarrow x \neq 5$

Therefore the domain is $\mathbb{R} \setminus \{5\}$.

---

**Example 9** (Syllabus 1.6 specified example — inverse of an exponential function): Given $f(x) = e^{2x}$, find $f^{-1}(x)$.

**Solution**:

Let $y = e^{2x}$. Take natural logarithms of both sides:

$$
\ln y = \ln(e^{2x}) = 2x \cdot \ln e = 2x
$$

Since $\ln e = 1$, we have $2x = \ln y \Rightarrow x = \frac12\ln y$.

Swap $x$ and $y$:

$$
f^{-1}(x) = \frac12\ln x
$$

**Domain**: The range of the original function $f(x) = e^{2x}$ is $(0, \infty)$, so the domain of $f^{-1}$ is $(0, \infty)$.

**Verification**:

$$
f(f^{-1}(x)) = e^{2 \cdot \frac12\ln x} = e^{\ln x} = x \quad (x > 0)
$$

---

**Example 10** (Verifying $\text{Domain}(gf) \subseteq \text{Domain}(f)$ — Syllabus 1.2): $f(x) = \sqrt{x}$, $g(x) = \dfrac{1}{x-3}$. Find the domain of $gf(x)$ and verify $\text{Domain}(gf) \subseteq \text{Domain}(f)$.

**Solution**:

$gf(x) = g(f(x)) = \dfrac{1}{\sqrt{x} - 3}$

**Condition 1**: $f$'s domain: $x \geq 0$.
**Condition 2**: $f(x)$ must be in $g$'s domain: $\sqrt{x} - 3 \neq 0 \Rightarrow \sqrt{x} \neq 3 \Rightarrow x \neq 9$.

Intersection: $x \geq 0$ and $x \neq 9$, i.e., $[0, 9) \cup (9, \infty)$.

Verifying $\text{Domain}(gf) \subseteq \text{Domain}(f)$:
$\text{Domain}(f) = [0, \infty)$, $\text{Domain}(gf) = [0, 9) \cup (9, \infty) \subset [0, \infty)$. $\checkmark$

---

## 5.5 Graphs of Absolute Value Functions $y = |f(x)|$

### 5.5.1 Basic Principles

$y = |f(x)|$ is defined as:

$$
|f(x)| = \begin{cases}
f(x), & f(x) \geq 0 \\
-f(x), & f(x) < 0
\end{cases}
$$

**Graph transformation rule**: Take the graph of $y = f(x)$, **reflect** the parts below the $x$-axis **upwards** across the $x$-axis (i.e., take the absolute value of the $y$-coordinate), while the parts above and on the $x$-axis remain unchanged.

**Key observations**:
- After reflection, all $y$ values are non-negative ($|f(x)| \geq 0$).
- At points where $f(x) = 0$ (i.e., $x$-intercepts), the absolute value graph forms **cusps** — because the slope suddenly changes sign on either side.
- The range of $|f(x)|$ is $[0, \infty)$ (if the original function can take arbitrarily large positive values) or $[0, \text{finite maximum}]$.

### 5.5.2 Characteristics of Absolute Value Graphs for Different Function Types

| Original function type | Features of $|f(x)|$ |
|-----------|----------------|
| **Linear** $|mx + c|$ | V-shape, cusp at $x = -c/m$ |
| **Quadratic** $|ax^2+bx+c|$ | Cusps at $x$-intercepts, portions of parabola below $x$-axis reflected upward |
| **Cubic** $|(x-p)(x-q)(x-r)|$ | Cusps at all three $x$-intercepts |
| **Trigonometric** $|a\sin bx + c|$ | Period halved (for $\sin$, from $2\pi$ to $\pi$), troughs become peaks |
| **Trigonometric** $|a\cos bx + c|$ | Period halved (for $\cos$, from $2\pi$ to $\pi$), troughs become peaks |
| **Trigonometric** $|a\tan bx + c|$ | Vertical asymptotes unchanged, graph reflected to make $y \geq 0$ |
| **Exponential** $|a^x|$ | Same as $a^x$ (since $a^x > 0$) |
| **Logarithmic** $|\log_a x|$ | Cusp at $x$-intercept, part where $x < 1$ reflected upward |

### 5.5.3 Solving Absolute Value Equations and Inequalities

**Equation $|f(x)| = k$ ($k > 0$)**: Equivalent to $f(x) = k$ or $f(x) = -k$.

**Inequality $|f(x)| < k$ ($k > 0$)**: Equivalent to $-k < f(x) < k$.

**Inequality $|f(x)| > k$ ($k > 0$)**: Equivalent to $f(x) > k$ or $f(x) < -k$.

---

### Worked Examples 4.5 (Absolute Value Functions)

**Example 1** (Absolute value of a linear function — V-shape): Sketch the graph of $y = |2x - 3|$ and find the values of $x$ for which $y = 5$.

**Solution**:

**Sketch**:

$f(x) = 2x - 3$, $f(x) = 0$ when $x = 1.5$.

When $x \geq 1.5$, $2x - 3 \geq 0$, so $|2x-3| = 2x-3$ (straight line, slope $2$).
When $x < 1.5$, $2x - 3 < 0$, so $|2x-3| = -(2x-3) = -2x+3$ (straight line, slope $-2$).

The graph is V-shaped, with the cusp at $(1.5, 0)$.

**Solve $|2x-3| = 5$**:

Case 1: $2x-3 = 5 \Rightarrow 2x = 8 \Rightarrow x = 4$
Case 2: $2x-3 = -5 \Rightarrow 2x = -2 \Rightarrow x = -1$

Solutions are $x = 4$ or $x = -1$.

---

**Example 2** (Absolute value of a quadratic function): Sketch the graph of $y = |x^2 - 4x + 3|$.

**Solution**:

**Step 1** (Sketch the original function): $y = x^2 - 4x + 3 = (x-1)(x-3)$.

- $x$-intercepts: $x = 1$ and $x = 3$
- Vertex: $x = 2$, $y = 4 - 8 + 3 = -1$, i.e., $(2, -1)$
- Opens upward ($a = 1 > 0$)

**Step 2** (Take absolute value): On the interval $[1, 3]$, the original function $f(x) \leq 0$; this part is reflected upward. For $x < 1$ and $x > 3$, $f(x) > 0$, so these parts remain unchanged.

**Step 3** (Mark key points): Cusps at $x = 1$ and $x = 3$. After reflection, the original vertex $(2, -1)$ becomes $(2, 1)$.

Range is $[0, \infty)$.

---

**Example 3** (Absolute value graph and sign analysis of a cubic function): Given $f(x) = (x+1)(x-1)(x-2)$.

(i) Sketch the graph of $y = |f(x)|$;
(ii) Discuss the number of intersection points between $|f(x)|$ and $y = 2$.

**Solution**:

(i) **Sign analysis**:

| Interval | Test point | $(x+1)$ | $(x-1)$ | $(x-2)$ | Sign of $f(x)$ | $|f(x)|$ |
|------|--------|---------|---------|---------|------------|----------|
| $x < -1$ | $x=-2$ | neg | neg | neg | **neg** | reflected to positive |
| $-1 < x < 1$ | $x=0$ | pos | neg | neg | **pos** | unchanged |
| $1 < x < 2$ | $x=1.5$ | pos | pos | neg | **neg** | reflected to positive |
| $x > 2$ | $x=3$ | pos | pos | pos | **pos** | unchanged |

$x$-intercepts: $x = -1, 1, 2$ (all cusps).
$y$-intercept: $f(0) = (1)(-1)(-2) = 2$.

(ii) Intersections of $y = 2$ with $|f(x)|$:
- On $(-1, 1)$: $f(0) = 2$, one intersection.
- In the reflected region $x < -1$: $|f(x)| = -f(x)$. $f(-2) = (-1)(-3)(-4) = -12$, $|f(-2)| = 12$, $f(-1) = 0$. By continuity, $y = 2$ intersects once in this region.
- In the reflected region $(1, 2)$: similarly intersects once.

Therefore there are **3 intersection points** in total.

---

**Example 4** (Form $|a\sin bx + c|$ — Syllabus 1.4 specified): Sketch the graph of $y = |\sin x|$ on $[0, 2\pi]$.

**Solution**:

First sketch $y = \sin x$:
- On $[0, \pi]$, $\sin x \geq 0$ (on or above the $x$-axis)
- On $[\pi, 2\pi]$, $\sin x \leq 0$ (below the $x$-axis)

Take absolute value:
- $[0, \pi]$: unchanged
- $[\pi, 2\pi]$: reflected upward ($|\sin x| = -\sin x$)

Graph features:
- Two identical "arches": $(0,0)\to(\frac{\pi}{2},1)\to(\pi,0)$ and $(\pi,0)\to(\frac{3\pi}{2},1)\to(2\pi,0)$
- **Period**: $\pi$ (the original $\sin x$ has period $2\pi$; after reflection, it repeats every $\pi$)
- **Range**: $[0, 1]$
- **Cusps**: at $x = 0, \pi, 2\pi$, etc.

---

**Example 5** (Form $|a\cos bx + c|$ — Syllabus 1.4 specified): Sketch the graph of $y = |3\cos 2x - 1|$ on $[0, \pi]$.

**Solution**:

**Step 1** (Sketch the original function $y = 3\cos 2x - 1$):
- Amplitude $3$, period $\dfrac{2\pi}{2} = \pi$, shifted down by $1$ unit
- Maximum: $3(1) - 1 = 2$, minimum: $3(-1) - 1 = -4$
- Zeros: $3\cos 2x - 1 = 0 \Rightarrow \cos 2x = \dfrac13$
  $2x = \arccos\dfrac13$ or $2x = 2\pi - \arccos\dfrac13$
  i.e., $x = \dfrac12\arccos\dfrac13$ or $x = \pi - \dfrac12\arccos\dfrac13$
  Let $\alpha = \dfrac12\arccos\dfrac13 \approx 0.615$ radians

**Step 2** (Take absolute value):
- On the interval between the two zeros ($\alpha < x < \pi - \alpha$), $3\cos 2x - 1 \leq 0$, this part is reflected upward
- The remaining parts are unchanged

**Step 3** (Mark key points):
- Cusps: at $x = \alpha$ and $x = \pi - \alpha$
- Reflected "peak": the original minimum at $x = \dfrac{\pi}{2}$, where $3\cos\pi - 1 = -4$, becomes $4$
- Original maxima at $x = 0$ (value $2$) and $x = \pi$ (value $2$) remain unchanged

**Final graph features**:
- Range: $[0, 4]$
- Number of cusps (in one period): 2
- Asymptotes: none

---

**Example 6** (Form $|a\tan bx + c|$ — Syllabus 1.4 specified): Sketch the graph of $y = |\tan x - 1|$ on $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.

**Solution**:

**Step 1** (Sketch the original function $y = \tan x - 1$):
- $\tan x$ has period $\pi$, shifted down by $1$ unit
- Vertical asymptotes: $x = -\dfrac{\pi}{2}$ and $x = \dfrac{\pi}{2}$
- Zero: $\tan x - 1 = 0 \Rightarrow \tan x = 1 \Rightarrow x = \dfrac{\pi}{4}$ (within $(-\frac{\pi}{2}, \frac{\pi}{2})$)
- As $x \to \dfrac{\pi}{2}^-$, $\tan x \to \infty$, $\tan x - 1 \to \infty$
- As $x \to -\dfrac{\pi}{2}^+$, $\tan x \to -\infty$, $\tan x - 1 \to -\infty$

**Step 2** (Take absolute value):
- When $x < \dfrac{\pi}{4}$, $\tan x - 1 < 0$, reflect upward
- When $x > \dfrac{\pi}{4}$, $\tan x - 1 > 0$, unchanged
- When $x = \dfrac{\pi}{4}$, $\tan\dfrac{\pi}{4} - 1 = 0$, cusp

**Step 3** (Analyse behaviour after reflection):
- In the region $x < \dfrac{\pi}{4}$, $|\tan x - 1| = -(\tan x - 1) = 1 - \tan x$
  As $x \to -\dfrac{\pi}{2}^+$, $\tan x \to -\infty$, $1 - \tan x \to \infty$
- In the region $x > \dfrac{\pi}{4}$, $|\tan x - 1| = \tan x - 1$
  As $x \to \dfrac{\pi}{2}^-$, $\tan x \to \infty$, $\tan x - 1 \to \infty$

**Final graph features**:
- Vertical asymptotes still at $x = -\dfrac{\pi}{2}$ and $x = \dfrac{\pi}{2}$ (absolute value does not change the position of asymptotes)
- Cusp at $x = \dfrac{\pi}{4}$
- The graph tends to infinity on both sides of the cusp
- Range: $[0, \infty)$ (minimum value $0$ at $x = \dfrac{\pi}{4}$)

---

**Example 7** (Absolute value equation — quadratic type): Solve $|x^2 - 3x + 2| = 2$.

**Solution**:

Original quadratic: $x^2 - 3x + 2 = (x-1)(x-2)$, roots at $x = 1, 2$.

**Case 1**: $x^2 - 3x + 2 = 2$

$$
x^2 - 3x = 0 \Rightarrow x(x-3) = 0 \Rightarrow x = 0 \text{ or } x = 3
$$

Check: $x = 0$ gives $0 - 0 + 2 = 2 > 0$ (in the non-negative region), valid. $x = 3$ gives $9 - 9 + 2 = 2 > 0$, valid.

**Case 2**: $x^2 - 3x + 2 = -2$

$$
x^2 - 3x + 4 = 0
$$

Discriminant $\Delta = 9 - 16 = -7 < 0$, no real solutions.

Therefore the solutions are $x = 0$ or $x = 3$.

---

**Example 8** (Absolute value inequality — squaring technique): Solve $|x-1| > |2x+3|$.

**Solution**:

Both sides are non-negative, so we can square both sides without changing the inequality direction:

$$
(x-1)^2 > (2x+3)^2
$$

Expand:

$$
x^2 - 2x + 1 > 4x^2 + 12x + 9
$$

Rearrange:

$$
0 > 3x^2 + 14x + 8 \Rightarrow 3x^2 + 14x + 8 < 0
$$

Find roots:

$$
x = \frac{-14 \pm \sqrt{196 - 96}}{6} = \frac{-14 \pm 10}{6}
$$

$x = \dfrac{-14 + 10}{6} = -\dfrac{4}{6} = -\dfrac{2}{3}$, $x = \dfrac{-14 - 10}{6} = -\dfrac{24}{6} = -4$.

Since the coefficient of $x^2$ is $3 > 0$, the parabola opens upward, and the inequality holds between the roots:

$$
-4 < x < -\frac{2}{3}
$$

---

**Example 9** (Extreme values of absolute value functions — geometric interpretation): Function $f(x) = |x-1| + |x-3|$, find the minimum value of $f(x)$.

**Solution**:

**Geometric interpretation**: $|x-1|$ is the distance from $x$ to $1$ on the number line, $|x-3|$ is the distance from $x$ to $3$. $f(x)$ is the sum of these two distances.

When $x$ lies between $[1, 3]$, the sum of the two distances is always equal to the segment length $2$.
When $x < 1$ or $x > 3$, the sum is greater than $2$.

Therefore the minimum value of $f(x)$ is $2$, attained for $x \in [1, 3]$.

**Algebraic verification** — piecewise analysis:

$$
f(x) = \begin{cases}
-(x-1) - (x-3) = -2x + 4, & x < 1 \\
(x-1) - (x-3) = 2, & 1 \leq x \leq 3 \\
(x-1) + (x-3) = 2x - 4, & x > 3
\end{cases}
$$

When $x < 1$, $f(x) = -2x + 4 > 2$ (since $-2x > -2$).
When $1 \leq x \leq 3$, $f(x) = 2$.
When $x > 3$, $f(x) = 2x - 4 > 2$.

The minimum value is $2$.

---

## Chapter Practice Problems

### I. Domain and Range (6 questions)

1. Find the domain of $f(x) = \dfrac{\sqrt{x+3}}{x-5}$.

2. Given $f(x) = x^2 - 6x + 10$, $x \in \mathbb{R}$. Find the minimum value of $f(x)$ and its range.

3. Find the domain and range of $f(x) = \ln(4 - x^2)$.

4. Find the domain of $f(x) = \dfrac{1}{\sqrt{2x-1}} + \ln(5-x)$.

5. Determine whether $y = \pm \sqrt{9 - x^2}$ ($|x| \leq 3$) is a function, and explain why.

6. Given $f(x) = \dfrac{3x-1}{x+2}$, find the range of $f$ and determine whether $f$ is one–one.

### II. Linear and Cubic Functions (5 questions)

7. Line $L$ passes through $(2, -1)$ and is parallel to $y = 3x + 2$. Find the equation of $L$.

8. Given $f(x) = x^3 - 2x^2 - 5x + 6$.
   (i) Verify that $x = 1$ is a root of $f(x)$ and fully factorise $f(x)$;
   (ii) Find all solutions of $f(x) = 0$.

9. Given the cubic function $f(x) = x^3 - 3x^2 - 9x + 11$, find $f'(x)$ and solve $f'(x) = 0$, determining the type of stationary points.

10. Solve the cubic inequality $(x+1)(x-2)(x-4) > 0$.

11. Given that $f(x) = x^3 + kx^2 - 5x - 6$ is exactly divisible by $x+2$, find $k$ and fully factorise $f(x)$.

### III. Exponentials and Logarithms (9 questions)

12. Simplify: $\log_3 54 - \log_3 2 + \log_3 \dfrac13$.

13. Solve $2^{x+1} = 5$, giving the result in terms of natural logarithms.

14. Solve $\log_3 (x+2) + \log_3 (x-4) = 2$.

15. Solve $3^{2x} - 10 \cdot 3^x + 9 = 0$.

16. Compute: $\log_2 3 \cdot \log_3 4 \cdot \log_4 5 \cdot \log_5 2$.

17. Function $f(x) = 2e^{x} - 3$. Find the horizontal asymptote, $y$-intercept and $x$-intercept of $f(x)$.

18. Solve $3^x < 7$.

19. Given $\log_a 3 = p$, $\log_a 7 = q$. Express $\log_a 21$ and $\log_a \dfrac73$ in terms of $p$ and $q$.

20. Solve $\log_2 x + \log_4 x = 3$. (Hint: Use the change of base formula to convert $\log_4 x$ to base $2$.)

### IV. Inverse Functions and Composite Functions (8 questions)

21. Find the inverse $f^{-1}(x)$ of $f(x) = \dfrac{3x - 2}{4}$.

22. Given $f(x) = x^2 + 2x$, $x \geq -1$. Find $f^{-1}(x)$ and its domain.

23. Given $f(x) = 2x + 1$, $g(x) = \dfrac1x$. Find $fg(x)$ and $gf(x)$, and find the domain of $gf(x)$.

24. Given $f(x) = e^{3x}$, find $f^{-1}(x)$.

25. Given $f(x) = \ln(x+2)$, $x > -2$. Find $f^{-1}(x)$.

26. Explain in words why $f(x) = x^4$ (domain $\mathbb{R}$) has no inverse.

27. $f(x) = \sqrt{x+1}$, $g(x) = x^2 - 4$. Find $fg(x)$ and its domain.

28. Given $f(x) = x^2$, $x \geq 0$, $g(x) = 2x + 1$. Verify $\text{Domain}(gf) \subseteq \text{Domain}(f)$.

### V. Absolute Value Functions (6 questions)

29. Sketch the graph of $y = |x-2|$ and solve $|x-2| = 3$.

30. Solve $|2x+1| < 5$.

31. Sketch the graph of $y = |\cos x|$ on $[0, 2\pi]$ and state its period.

32. Solve $|x^2 - 5x + 6| = 2$.

33. Solve $|x+2| \geq 3$.

34. Function $f(x) = |x-2| + |x+1|$, find the minimum value of $f(x)$.

### VI. Trigonometric Absolute Values (3 new questions — Syllabus 1.4 specified)

35. Sketch the key features of $y = |2\cos x + 1|$ on $[0, 2\pi]$, labelling key points and the positions of cusps.

36. Sketch the graph of $y = |\tan x|$ on $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$, indicating the positions of asymptotes.

37. Given $f(x) = |3\sin 2x - 2|$, find the maximum and minimum values of $f(x)$ on $[0, \pi]$.

### VII. Domain Restrictions and Existence of Composite Functions (1 new question — Syllabus 1.2)

38. Given $f(x) = \sqrt{x-2}$, $g(x) = \dfrac{1}{\sqrt{5-x}}$. Find $gf(x)$ and its domain, and verify $\text{Domain}(gf) \subseteq \text{Domain}(f)$.

---

## Answers to Practice Problems

### I. Domain and Range

**1.**
Condition 1 (root): $x+3 \geq 0 \Rightarrow x \geq -3$.
Condition 2 (denominator non-zero): $x-5 \neq 0 \Rightarrow x \neq 5$.
Intersection: $[-3, 5) \cup (5, \infty)$.

---

**2.**
Complete the square:

$$
f(x) = (x^2 - 6x + 9) + 1 = (x-3)^2 + 1
$$

Since $(x-3)^2 \geq 0$, $f(x) \geq 1$.
Minimum at $x = 3$, $f(3) = 1$.
Range is $[1, \infty)$.

---

**3.**
Domain: $4 - x^2 > 0 \Rightarrow x^2 < 4 \Rightarrow -2 < x < 2$, i.e., $(-2, 2)$.

Range: Let $u = 4 - x^2$, $x \in (-2, 2)$, then $u \in (0, 4]$.
$f(x) = \ln u$, $u \in (0, 4]$.
$\ln u$ is increasing on $(0, 4]$, minimum approaches $-\infty$ (as $u \to 0^+$), maximum is $\ln 4$ (at $u = 4$).
Range is $(-\infty, \ln 4]$.

---

**4.**
Condition 1 (denominator radicand): $2x-1 > 0$ (strictly greater, as it is in the denominator) $\Rightarrow x > \dfrac12$.
Condition 2 (logarithm argument): $5 - x > 0 \Rightarrow x < 5$.
Intersection: $\left(\dfrac12, 5\right)$.

---

**5.**
**Not a function**. For example, when $x = 0$, $y = \pm \sqrt{9 - 0} = \pm 3$, one $x$ corresponds to two $y$ values. The vertical line $x = 0$ intersects the graph at $(0, 3)$ and $(0, -3)$, two points.

---

**6.**
Separate the constant:

$$
f(x) = \frac{3x-1}{x+2} = \frac{3(x+2) - 7}{x+2} = 3 - \frac{7}{x+2}
$$

Since $\dfrac{7}{x+2} \neq 0$, $f(x) \neq 3$. Range is $\mathbb{R} \setminus \{3\}$.

One–one test: Suppose $f(a) = f(b)$:

$$
3 - \frac{7}{a+2} = 3 - \frac{7}{b+2} \Rightarrow \frac{7}{a+2} = \frac{7}{b+2} \Rightarrow a+2 = b+2 \Rightarrow a = b
$$

Therefore $f$ is one–one.

---

### II. Linear and Cubic Functions

**7.**
Parallel lines have the same slope, $m = 3$.
Point-slope form: $y - (-1) = 3(x - 2) \Rightarrow y + 1 = 3x - 6 \Rightarrow y = 3x - 7$.

---

**8.**
(i) $f(1) = 1 - 2 - 5 + 6 = 0$, so $x-1$ is a factor.

Synthetic division:

$$
\begin{array}{c|ccc}
1 & 1 & -2 & -5 & 6 \\
  &   & 1  & -1 & -6 \\
\hline
  & 1 & -1 & -6 & 0
\end{array}
$$

Quotient: $x^2 - x - 6 = (x-3)(x+2)$.

Therefore $f(x) = (x-1)(x-3)(x+2)$.

(ii) Solutions of $f(x) = 0$: $x = 1, 3, -2$.

---

**9.**
$f'(x) = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)$.

Set $f'(x) = 0$: $x = -1$ or $x = 3$.

Sign test:
- $x < -1$ (take $x = -2$): $f'(-2) = 3(-5)(-1) = 15 > 0$, increasing
- $-1 < x < 3$ (take $x = 0$): $f'(0) = 3(-3)(1) = -9 < 0$, decreasing
- $x > 3$ (take $x = 4$): $f'(4) = 3(1)(5) = 15 > 0$, increasing

$x = -1$: increasing → decreasing → **local maximum**, $f(-1) = -1 - 3 + 9 + 11 = 16$.
$x = 3$: decreasing → increasing → **local minimum**, $f(3) = 27 - 27 - 27 + 11 = -16$.

---

**10.**
Three roots: $x = -1, 2, 4$. Leading coefficient $a = 1 > 0$.

Sign analysis:

| Interval | $x+1$ | $x-2$ | $x-4$ | Product |
|------|-------|-------|-------|------|
| $x < -1$ | neg | neg | neg | **neg** |
| $-1 < x < 2$ | pos | neg | neg | **pos** |
| $2 < x < 4$ | pos | pos | neg | **neg** |
| $x > 4$ | pos | pos | pos | **pos** |

$f(x) > 0$ for $-1 < x < 2$ or $x > 4$.

---

**11.**
By the factor theorem, $f(-2) = 0$:

$$
f(-2) = (-2)^3 + k(4) - 5(-2) - 6 = -8 + 4k + 10 - 6 = 4k - 4 = 0
$$

$k = 1$.

Synthetic division by $(x+2)$:

$$
\begin{array}{c|ccc}
-2 & 1 & 1 & -5 & -6 \\
   &   & -2 & 2 & 6 \\
\hline
   & 1 & -1 & -3 & 0
\end{array}
$$

Quotient: $x^2 - x - 3$.

Therefore $f(x) = (x+2)(x^2 - x - 3)$. The quadratic cannot be further factorised over the rationals.

---

### III. Exponentials and Logarithms

**12.**

$$
\log_3 54 - \log_3 2 = \log_3 \frac{54}{2} = \log_3 27 = 3
$$

$$
3 + \log_3 \frac13 = \log_3 \left(27 \times \frac13\right) = \log_3 9 = 2
$$

The value is $2$.

---

**13.**

$$
2^{x+1} = 5 \Rightarrow \ln(2^{x+1}) = \ln 5 \Rightarrow (x+1)\ln 2 = \ln 5
$$

$$
x+1 = \frac{\ln 5}{\ln 2} \Rightarrow x = \frac{\ln 5}{\ln 2} - 1
$$

---

**14.**

$$
\log_3[(x+2)(x-4)] = 2 \Rightarrow (x+2)(x-4) = 3^2 = 9
$$

$$
x^2 - 2x - 8 = 9 \Rightarrow x^2 - 2x - 17 = 0
$$

$$
x = \frac{2 \pm \sqrt{4 + 68}}{2} = \frac{2 \pm \sqrt{72}}{2} = \frac{2 \pm 6\sqrt{2}}{2} = 1 \pm 3\sqrt{2}
$$

Check domain: $x+2 > 0$ and $x-4 > 0 \Rightarrow x > 4$.

$1 + 3\sqrt{2} \approx 5.24 > 4$, valid.
$1 - 3\sqrt{2} \approx -3.24 < 4$, rejected.

Therefore $x = 1 + 3\sqrt{2}$.

---

**15.**
Let $u = 3^x > 0$, then $3^{2x} = (3^x)^2 = u^2$.

$$
u^2 - 10u + 9 = 0 \Rightarrow (u-1)(u-9) = 0 \Rightarrow u = 1 \text{ or } u = 9
$$

$3^x = 1 \Rightarrow x = 0$.
$3^x = 9 \Rightarrow x = 2$.

Solutions are $x = 0$ or $x = 2$.

---

**16.**
Use the change of base formula, converting everything to natural logarithms:

$$
\log_2 3 = \frac{\ln 3}{\ln 2}, \quad \log_3 4 = \frac{\ln 4}{\ln 3}, \quad \log_4 5 = \frac{\ln 5}{\ln 4}, \quad \log_5 2 = \frac{\ln 2}{\ln 5}
$$

The product is:

$$
\frac{\ln 3}{\ln 2} \cdot \frac{\ln 4}{\ln 3} \cdot \frac{\ln 5}{\ln 4} \cdot \frac{\ln 2}{\ln 5} = 1
$$

The value is $1$ (all terms cancel out).

---

**17.**
Horizontal asymptote: as $x \to -\infty$, $e^x \to 0$, $2e^x - 3 \to -3$, asymptote is $y = -3$.

$y$-intercept: $f(0) = 2e^0 - 3 = 2 - 3 = -1$, i.e., $(0, -1)$.

$x$-intercept: $2e^x - 3 = 0 \Rightarrow e^x = \dfrac32 \Rightarrow x = \ln\dfrac32$, i.e., $\left(\ln\dfrac32, 0\right)$.

---

**18.**
$3^x < 7 \Rightarrow \ln(3^x) < \ln 7 \Rightarrow x\ln 3 < \ln 7 \Rightarrow x < \dfrac{\ln 7}{\ln 3}$.

---

**19.**
$\log_a 21 = \log_a (3 \times 7) = \log_a 3 + \log_a 7 = p + q$.

$\log_a \dfrac73 = \log_a 7 - \log_a 3 = q - p$.

---

**20.**
Use the change of base formula to convert $\log_4 x$ to base $2$:

$$
\log_4 x = \frac{\log_2 x}{\log_2 4} = \frac{\log_2 x}{2}
$$

Let $u = \log_2 x$, then the equation becomes:

$$
u + \frac{u}{2} = 3 \Rightarrow \frac{3u}{2} = 3 \Rightarrow u = 2
$$

$\log_2 x = 2 \Rightarrow x = 2^2 = 4$.

---

### IV. Inverse Functions and Composite Functions

**21.**
$y = \dfrac{3x-2}{4} \Rightarrow 4y = 3x - 2 \Rightarrow 3x = 4y + 2 \Rightarrow x = \dfrac{4y+2}{3}$.

Swap: $f^{-1}(x) = \dfrac{4x+2}{3}$.

---

**22.**
Complete the square: $f(x) = (x+1)^2 - 1$, $x \geq -1$. Range is $[-1, \infty)$.

Let $y = (x+1)^2 - 1 \Rightarrow y+1 = (x+1)^2 \Rightarrow x+1 = \sqrt{y+1}$ (since $x \geq -1$, take the positive root).

$x = \sqrt{y+1} - 1$.

Swap: $f^{-1}(x) = \sqrt{x+1} - 1$, domain $[-1, \infty)$.

---

**23.**
$fg(x) = f(g(x)) = f\left(\dfrac1x\right) = 2\left(\dfrac1x\right) + 1 = \dfrac{2}{x} + 1$, $x \neq 0$.

$gf(x) = g(f(x)) = g(2x+1) = \dfrac{1}{2x+1}$.

Domain of $gf(x)$: $2x+1 \neq 0 \Rightarrow x \neq -\dfrac12$, i.e., $\mathbb{R} \setminus \left\{-\dfrac12\right\}$.

---

**24.**
$y = e^{3x} \Rightarrow \ln y = 3x \Rightarrow x = \dfrac13\ln y$.

Swap: $f^{-1}(x) = \dfrac13\ln x$, domain $x > 0$.

---

**25.**
$y = \ln(x+2) \Rightarrow e^y = x+2 \Rightarrow x = e^y - 2$.

Swap: $f^{-1}(x) = e^x - 2$.

The range of the original function is $\mathbb{R}$, so the domain of $f^{-1}$ is $\mathbb{R}$.

Verification: $f(f^{-1}(x)) = \ln(e^x - 2 + 2) = \ln(e^x) = x$. $\checkmark$

---

**26.**
$f(x) = x^4$ **is not one–one** because different $x$ values correspond to the same $y$ value. For example, $f(2) = 16$ and $f(-2) = 16$, i.e., $2 \neq -2$ but $f(2) = f(-2)$. The horizontal line $y = 16$ intersects the graph of $y = x^4$ at $(2, 16)$ and $(-2, 16)$, two points. Therefore $f$ has no inverse.

> If we restrict the domain to $x \geq 0$, then the inverse is $f^{-1}(x) = \sqrt[4]{x}$.

---

**27.**
$fg(x) = f(g(x)) = \sqrt{(x^2 - 4) + 1} = \sqrt{x^2 - 3}$.

Domain: $f(x) = \sqrt{x+1}$ has domain $x+1 \geq 0 \Rightarrow x \geq -1$.

So $g(x) \geq -1 \Rightarrow x^2 - 4 \geq -1 \Rightarrow x^2 \geq 3 \Rightarrow |x| \geq \sqrt{3}$.

Domain is $(-\infty, -\sqrt{3}] \cup [\sqrt{3}, \infty)$.

---

**28.**
$f(x) = x^2$, $x \geq 0$, domain $[0, \infty)$.
$g(x) = 2x + 1$, domain $\mathbb{R}$.

$gf(x) = g(f(x)) = 2x^2 + 1$.

Domain of $gf$: $x$ must be in $f$'s domain ($x \geq 0$), and $f(x)$ must be in $g$'s domain ($\mathbb{R}$, no restriction).

Therefore $\text{Domain}(gf) = [0, \infty)$.

$\text{Domain}(f) = [0, \infty)$, so $\text{Domain}(gf) \subseteq \text{Domain}(f)$ holds (in fact they are equal). $\checkmark$

---

### V. Absolute Value Functions

**29.**
V-shape, cusp at $(2, 0)$.
$x \geq 2$: $y = x-2$; $x < 2$: $y = 2-x$.

Solve $|x-2| = 3$:
Case 1: $x-2 = 3 \Rightarrow x = 5$
Case 2: $x-2 = -3 \Rightarrow x = -1$

Solutions: $x = 5$ or $x = -1$.

---

**30.**
$|2x+1| < 5 \Rightarrow -5 < 2x+1 < 5$.

Left: $-5 < 2x+1 \Rightarrow -6 < 2x \Rightarrow -3 < x$.
Right: $2x+1 < 5 \Rightarrow 2x < 4 \Rightarrow x < 2$.

Intersection: $-3 < x < 2$.

---

**31.**
$y = |\cos x|$ on $[0, 2\pi]$:
- $[0, \frac{\pi}{2}]$: $\cos x \geq 0$, decreasing from $(0,1)$ to $(\frac{\pi}{2}, 0)$
- $[\frac{\pi}{2}, \frac{3\pi}{2}]$: $\cos x \leq 0$, reflected upward: from $(\frac{\pi}{2}, 0)$ up to $(\pi, 1)$ then down to $(\frac{3\pi}{2}, 0)$
- $[\frac{3\pi}{2}, 2\pi]$: $\cos x \geq 0$, increasing from $(\frac{3\pi}{2}, 0)$ to $(2\pi, 1)$

Period is $\pi$. Cusps at $x = \dfrac{\pi}{2}, \dfrac{3\pi}{2}$, etc.

---

**32.**
$x^2 - 5x + 6 = (x-2)(x-3)$.

Case 1: $x^2 - 5x + 6 = 2 \Rightarrow x^2 - 5x + 4 = 0 \Rightarrow (x-1)(x-4) = 0 \Rightarrow x = 1$ or $x = 4$.
Check: $x=1$ gives $1-5+6=2>0$, valid. $x=4$ gives $16-20+6=2>0$, valid.

Case 2: $x^2 - 5x + 6 = -2 \Rightarrow x^2 - 5x + 8 = 0$.
$\Delta = 25 - 32 = -7 < 0$, no real solutions.

Solutions: $x = 1$ or $x = 4$.

---

**33.**
$|x+2| \geq 3 \Rightarrow x+2 \leq -3$ or $x+2 \geq 3$.

$x+2 \leq -3 \Rightarrow x \leq -5$.
$x+2 \geq 3 \Rightarrow x \geq 1$.

Solution: $x \leq -5$ or $x \geq 1$.

---

**34.**
Geometric interpretation: $|x-2|$ is the distance from $x$ to $2$, $|x+1| = |x-(-1)|$ is the distance from $x$ to $-1$. $f(x)$ is the sum of these two distances.

The distance on the number line from $-1$ to $2$ is $3$. When $x$ lies between $[-1, 2]$, the sum of the two distances is always $3$. When $x < -1$ or $x > 2$, the sum is greater than $3$.

Therefore the minimum value is $3$, attained for $x \in [-1, 2]$.

Algebraic verification:

$$
f(x) = \begin{cases}
-(x-2) - (x+1) = -2x + 1, & x < -1 \\
-(x-2) + (x+1) = 3, & -1 \leq x \leq 2 \\
(x-2) + (x+1) = 2x - 1, & x > 2
\end{cases}
$$

When $x < -1$, $f(x) = -2x + 1 > 3$.
When $-1 \leq x \leq 2$, $f(x) = 3$.
When $x > 2$, $f(x) = 2x - 1 > 3$.

The minimum value is $3$.

---

### VI. Trigonometric Absolute Values

**35.**
$y = 2\cos x + 1$ on $[0, 2\pi]$:
- Maximum: $2(1) + 1 = 3$ ($x = 0, 2\pi$)
- Minimum: $2(-1) + 1 = -1$ ($x = \pi$)
- Zeros: $2\cos x + 1 = 0 \Rightarrow \cos x = -\dfrac12 \Rightarrow x = \dfrac{2\pi}{3}, \dfrac{4\pi}{3}$

After taking absolute value:
- On $[\frac{2\pi}{3}, \frac{4\pi}{3}]$, $2\cos x + 1 \leq 0$, reflected upward
- Remaining parts unchanged
- Cusps: $x = \dfrac{2\pi}{3}$ and $x = \dfrac{4\pi}{3}$
- After reflection, the maximum occurs at $x = \pi$: $|2\cos\pi + 1| = |-2+1| = 1$
- Original maxima at $x = 0$ (value $3$) and $x = 2\pi$ (value $3$) remain unchanged

Range: $[0, 3]$.

---

**36.**
$y = |\tan x|$ on $(-\frac{\pi}{2}, \frac{\pi}{2})$:

- $(-\frac{\pi}{2}, 0)$: $\tan x < 0$, reflected upward, $|\tan x| = -\tan x$
- $(0, \frac{\pi}{2})$: $\tan x > 0$, unchanged, $|\tan x| = \tan x$
- $x = 0$: $\tan 0 = 0$, cusp

**Asymptotes**: $x = -\dfrac{\pi}{2}$ and $x = \dfrac{\pi}{2}$ are still vertical asymptotes (absolute value does not change the position of asymptotes).

Graph features:
- Cusp at $x = 0$
- As $x \to \pm\frac{\pi}{2}$, $|\tan x| \to \infty$
- Range: $[0, \infty)$
- Graph is symmetric about $x = 0$ (even function), because $|\tan(-x)| = |-\tan x| = |\tan x|$

---

**37.**
$f(x) = |3\sin 2x - 2|$, $x \in [0, \pi]$.

First analyse $y = 3\sin 2x - 2$:
- Amplitude $3$, period $\pi$, shifted down by $2$
- Maximum: $3(1) - 2 = 1$, minimum: $3(-1) - 2 = -5$
- Zeros: $3\sin 2x - 2 = 0 \Rightarrow \sin 2x = \dfrac23$
  $2x = \arcsin\dfrac23$ or $2x = \pi - \arcsin\dfrac23$
  Let $\alpha = \dfrac12\arcsin\dfrac23 \approx 0.364$ radians
  Then $x = \alpha$ or $x = \dfrac{\pi}{2} - \alpha$

On $[0, \pi]$, $3\sin 2x - 2$ is negative on $[\alpha, \frac{\pi}{2} - \alpha]$, so this part is reflected upward.

Maximum: after reflection, the original minimum $-5$ (at $x = \dfrac{3\pi}{4}$) becomes $5$. So the maximum of $f(x)$ is $5$.
Minimum: $0$ (at the zeros $x = \alpha$ and $x = \dfrac{\pi}{2} - \alpha$).

Therefore $f(x)$ on $[0, \pi]$ has maximum $5$ and minimum $0$.

---

### VII. Domain Restrictions and Existence of Composite Functions

**38.**
$f(x) = \sqrt{x-2}$, domain $[2, \infty)$.
$g(x) = \dfrac{1}{\sqrt{5-x}}$, domain $x < 5$.

$gf(x) = g(f(x)) = \dfrac{1}{\sqrt{5 - \sqrt{x-2}}}$.

Domain conditions:
1. $f$'s domain: $x \geq 2$
2. $f(x)$ must be in $g$'s domain:
   - $5 - \sqrt{x-2} > 0$ (denominator radicand must be positive)
   - $\sqrt{x-2} < 5 \Rightarrow x-2 < 25 \Rightarrow x < 27$
   - $5 - \sqrt{x-2} \neq 0$ is already guaranteed by $>0$

Intersection: $2 \leq x < 27$.

Verification $\text{Domain}(gf) \subseteq \text{Domain}(f)$:
$\text{Domain}(f) = [2, \infty)$, $\text{Domain}(gf) = [2, 27) \subset [2, \infty)$. $\checkmark$

---

> **Study tips**: Functions are the cornerstone of IGCSE 0606 Additional Mathematics — differentiation, integration, curve sketching, and kinematics are all built upon the concept of functions. The key points of this chapter are:
>
> 1. Master the calculation of domain and range (especially when roots, denominators, and logarithms appear together)
> 2. Deeply understand the inverse relationship between exponentials and logarithms ($a^{\log_a x} = x$, $\log_a(a^x) = x$)
> 3. Master the flexible use of logarithm laws (especially the change of base formula $\log_a M = \dfrac{\log_b M}{\log_b a}$)
> 4. Be proficient in finding inverse functions and composite functions, paying attention to changes in domain
> 5. Be able to sketch transformed graphs of $|f(x)|$ (linear, quadratic, cubic, trigonometric of the forms $a\sin bx + c$, $a\cos bx + c$, $a\tan bx + c$)
> 6. Be able to explain in words why a function has no inverse (Syllabus 1.5)
> 7. Understand $\text{Domain}(gf) \subseteq \text{Domain}(f)$ and $\text{Range}(gf) \subseteq \text{Range}(g)$ (Syllabus 1.2)

---
---

