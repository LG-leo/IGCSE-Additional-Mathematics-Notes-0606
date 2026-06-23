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

# Chapter 7: Integration (Indefinite and Definite Integrals) [Revised and Expanded Edition]

---

## Syllabus Mapping

This chapter corresponds to the following entries from **Topic 14: Calculus** of the **Cambridge IGCSE Additional Mathematics (0606) 2028–2030 syllabus**:

| Syllabus Ref | Content | Notes |
|---------|---------|---------|
| **14.10** | Understand integration as the reverse process of differentiation | Indefinite integrals must include an arbitrary constant |
| **14.11** | Integrate sums of terms in powers of $x$ | Includes $x^n$, $\dfrac{1}{x}$, $\dfrac{1}{ax+b}$ |
| **14.12** | Integrate functions of the form | $(ax+b)^n$ (any rational $n$, including $n=-1$), $\sin(ax+b)$, $\cos(ax+b)$, $\sec^2(ax+b)$, $e^{ax+b}$ |
| **14.13** | Evaluation of definite integrals and application to plane area | Between a line and a curve, between two curves, sum of two or more areas |
| **14.14** | Application of differentiation and integration to kinematics | Relationships between displacement, velocity and acceleration (see Chapter 10) |

> ⚠️ **Important**: The syllabus explicitly states that **no formulas will be given** in the List of formulas for the Calculus section. All integration formulas must be **memorised thoroughly**. Angles in trigonometric functions must always be in **radians**.

---

## Introduction

In Chapter 5, we learned **differentiation** — given a function $f(x)$, find its rate of change $f'(x)$. Differentiation answers the question "how fast is it changing?" **Integration** is the **reverse operation** of this process: given the derivative $f'(x)$, we want to recover the original function $f(x)$. Therefore, integration is also called **antidifferentiation**.

But the significance of integration goes far beyond being just a reverse operation. From a broader perspective:

- **Geometric meaning**: Definite integrals calculate the **area** under a curve. This is the core problem that took nearly two thousand years to solve — from Archimedes' "method of exhaustion" in ancient Greece to the independent development of calculus by Newton and Leibniz in the 17th century.
- **Physical meaning**: Given velocity, find displacement; given acceleration, find velocity — these are all processes of **accumulation**. In everyday life, the odometer reading is the accumulation of speed over time.
- **Analogy**: If differentiation is like taking a photograph (capturing the change at an instant), then integration is like recording a video (accumulating the change frame by frame).

**Comparison between integration and differentiation**:

| Concept | Differentiation (Chapter 5) | Integration (Chapter 7) |
|------|----------------|----------------|
| Basic question | Given $f(x)$, find $f'(x)$ | Given $f'(x)$, find $f(x)$ |
| Geometric meaning | Find slope of tangent at a point | Find area under a curve |
| Physical meaning | Given displacement, find velocity/acceleration | Given acceleration, find velocity/displacement |
| Notation | $\dfrac{d}{dx}$ | $\displaystyle \int \cdots dx$ |
| Operation properties | Linearity, product rule, quotient rule, chain rule | Linearity (no simple product/quotient rule counterpart) |

> **Core idea**: Differentiation and integration are inverse operations. Just like addition and subtraction, multiplication and division, they are a pair of "reverse operations." Understanding this inverse relationship is the cornerstone of all of calculus.

---

## 7.1 Indefinite Integrals (Antiderivatives)

### 7.1.1 From Differentiation to Integration — The Essence of the Inverse Operation

We start with the most fundamental question.

**Question**: Given that the derivative of a function $F(x)$ is $2x$, i.e., $F'(x) = 2x$, find $F(x)$.

**Thinking process**: In Chapter 5 we learned:

$$
\frac{d}{dx}(x^2) = 2x
$$

So $x^2$ is an "antiderivative" of $2x$. But the problem is — the derivative of a constant is $0$, so $x^2 + 1$, $x^2 - 5$, $x^2 + \pi$ all have derivatives equal to $2x$. This means $2x$ has **infinitely many** antiderivatives, differing only by a constant. We denote this arbitrary constant by $C$.

Using integration notation for this process:

$$
\boxed{\int 2x \, dx = x^2 + C}
$$

Where:
- $\int$ is called the **integral sign** (an elongated S, from the Latin *summa*, meaning "sum")
- $2x$ is called the **integrand**
- $dx$ indicates integration with respect to the variable $x$
- $C$ is called the **constant of integration**

> **Formal definition**: A function $F(x)$ is called an **antiderivative** of $f(x)$ if $F'(x) = f(x)$ for all $x$ in the domain. The set of all antiderivatives of $f(x)$ is called the **indefinite integral**, denoted by $\displaystyle \int f(x) \, dx = F(x) + C$.

### 7.1.2 The Inverse Relationship Between Integration and Differentiation — Verification

Since integration is the inverse of differentiation, every integration formula can be verified by differentiation. This is the most reliable way to check whether an integration result is correct.

**Verification procedure**:
1. Differentiate the result $F(x) + C$
2. Check whether the derivative equals the integrand $f(x)$
3. If they are equal, the integration is correct

**Verification example 1**: Verify $\displaystyle \int 3x^2 \, dx = x^3 + C$

$$
\frac{d}{dx}(x^3 + C) = 3x^2 \quad \checkmark
$$

**Verification example 2**: Verify $\displaystyle \int \cos x \, dx = \sin x + C$

$$
\frac{d}{dx}(\sin x + C) = \cos x \quad \checkmark
$$

**Verification example 3**: Verify $\displaystyle \int e^{2x} \, dx = \frac{1}{2}e^{2x} + C$

$$
\frac{d}{dx}\left(\frac{1}{2}e^{2x} + C\right) = \frac{1}{2} \cdot e^{2x} \cdot 2 = e^{2x} \quad \checkmark
$$

This seemingly simple method is especially important when dealing with complex integrals — if you are unsure about a result, **verifying by differentiation** is always the most reliable check.

---

**Example 1** (Understanding the concept of antiderivatives): Given $f'(x) = 6x^2$ and $f(1) = 3$, find $f(x)$.

**Solution**:

First find the indefinite integral:

$$
f(x) = \int 6x^2 \, dx = 6 \cdot \frac{x^3}{3} + C = 2x^3 + C
$$

Use the condition $f(1) = 3$ to determine $C$:

$$
f(1) = 2(1)^3 + C = 2 + C = 3 \Rightarrow C = 1
$$

Therefore $f(x) = 2x^3 + 1$.

> This is a common question type in exams — given the derivative and an initial condition, find the original function. The key is to first integrate to obtain an expression containing $C$, then substitute the condition to solve for $C$.

---

**Example 2** (Verifying integration by differentiation): Determine whether $\displaystyle \int \frac{1}{x^2} \, dx = -\frac{1}{x} + C$ is correct.

**Solution**:

Differentiate the result:

$$
\frac{d}{dx}\left(-\frac{1}{x} + C\right) = \frac{d}{dx}(-x^{-1} + C) = x^{-2} = \frac{1}{x^2}
$$

The derivative equals the integrand, so the integration is correct.

---

**Example 3** (Finding errors through differentiation): Determine whether $\displaystyle \int (2x+1)^2 \, dx = \frac{(2x+1)^3}{3} + C$ is correct.

**Solution**:

Differentiate the result:

$$
\frac{d}{dx}\left(\frac{(2x+1)^3}{3} + C\right) = \frac{1}{3} \cdot 3(2x+1)^2 \cdot 2 = 2(2x+1)^2 \neq (2x+1)^2
$$

There is an extra factor of $2$, so the integration is **incorrect**! The correct approach is:

$$
\int (2x+1)^2 \, dx = \frac{(2x+1)^3}{2 \cdot 3} + C = \frac{(2x+1)^3}{6} + C
$$

Verification: $\dfrac{d}{dx}\left(\dfrac{(2x+1)^3}{6}\right) = \dfrac{3(2x+1)^2 \cdot 2}{6} = (2x+1)^2 \quad \checkmark$

> ⚠️ **Lesson**: For integrals of the form $(ax+b)^n$, don't forget the extra factor $\dfrac{1}{a}$! This is one of the most common mistakes made by beginners.

---

### 7.1.3 Linearity of Integration

Integration satisfies **linearity**. This property derives from the linearity of differentiation and is the most fundamental rule in integration:

$$
\boxed{\int [a f(x) + b g(x)] \, dx = a \int f(x) \, dx + b \int g(x) \, dx}
$$

where $a$ and $b$ are arbitrary constants.

**Derivation**: Let $F'(x) = f(x)$, $G'(x) = g(x)$. Then by the linearity of differentiation:

$$
\frac{d}{dx}[a F(x) + b G(x)] = a F'(x) + b G'(x) = a f(x) + b g(x)
$$

Therefore $a F(x) + b G(x)$ is an antiderivative of $a f(x) + b g(x)$, proving the equality.

This property tells us two things:
1. **A constant factor can be pulled outside the integral sign**: $\displaystyle \int c f(x) \, dx = c \int f(x) \, dx$
2. **The integral of a sum equals the sum of the integrals**: $\displaystyle \int [f(x) + g(x)] \, dx = \int f(x) \, dx + \int g(x) \, dx$

> ⚠️ **Important warning**: The linearity of integration **does not mean** that "the integral of a product equals the product of the integrals"!
>
> $$
> \int f(x)g(x) \, dx \neq \int f(x) \, dx \cdot \int g(x) \, dx
> $$
>
> Nor does it mean "the integral of a quotient equals the quotient of the integrals"!
>
> $$
> \int \frac{f(x)}{g(x)} \, dx \neq \frac{\int f(x) \, dx}{\int g(x) \, dx}
> $$
>
> Integrating products and quotients requires more advanced techniques (such as integration by parts), which are not in the IGCSE syllabus. In IGCSE 0606, when encountering a product, you must **expand** first and then integrate term by term.

---

**Example 1** (Basic application of linearity): Find $\displaystyle \int (3x^2 - 5x + 2) \, dx$.

**Solution**:

$$
\begin{aligned}
\int (3x^2 - 5x + 2) \, dx &= 3 \int x^2 \, dx - 5 \int x \, dx + 2 \int 1 \, dx \\[4pt]
&= 3 \cdot \frac{x^3}{3} - 5 \cdot \frac{x^2}{2} + 2x + C \\[4pt]
&= x^3 - \frac{5}{2}x^2 + 2x + C
\end{aligned}
$$

**Verification**: $\dfrac{d}{dx}\left(x^3 - \dfrac{5}{2}x^2 + 2x + C\right) = 3x^2 - 5x + 2$. ✓

---

**Example 2** (Expand first, then integrate — handling products): Find $\displaystyle \int (x+3)(x-2) \, dx$.

**Solution**:

First expand:

$$
(x+3)(x-2) = x^2 - 2x + 3x - 6 = x^2 + x - 6
$$

Then integrate term by term:

$$
\int (x^2 + x - 6) \, dx = \frac{x^3}{3} + \frac{x^2}{2} - 6x + C
$$

> ⚠️ **Cannot** write: $\int (x+3)(x-2) \, dx = \int (x+3) \, dx \cdot \int (x-2) \, dx$

---

**Example 3** (Expanding a polynomial then integrating): Find $\displaystyle \int (2x-1)^3 \, dx$.

**Solution**:

Method 1 (Expand):

$$
(2x-1)^3 = 8x^3 - 12x^2 + 6x - 1
$$

$$
\begin{aligned}
\int (8x^3 - 12x^2 + 6x - 1) \, dx &= 8 \cdot \frac{x^4}{4} - 12 \cdot \frac{x^3}{3} + 6 \cdot \frac{x^2}{2} - x + C \\[4pt]
&= 2x^4 - 4x^3 + 3x^2 - x + C
\end{aligned}
$$

Method 2 (Using the $(ax+b)^n$ formula directly, which will be learned in §7.2.3):

$$
\int (2x-1)^3 \, dx = \frac{(2x-1)^4}{2 \cdot 4} + C = \frac{(2x-1)^4}{8} + C
$$

The two methods give answers that look different in form but are actually equivalent (expanding both gives the same result). ✓

---

**Example 4** (Simplify a fraction before integrating): Find $\displaystyle \int \frac{x^3 + 3x^2 - 2}{x^2} \, dx$.

**Solution**:

First simplify: $\dfrac{x^3 + 3x^2 - 2}{x^2} = x + 3 - \dfrac{2}{x^2} = x + 3 - 2x^{-2}$

Then integrate term by term:

$$
\begin{aligned}
\int (x + 3 - 2x^{-2}) \, dx &= \frac{x^2}{2} + 3x - 2 \cdot \frac{x^{-1}}{-1} + C \\[4pt]
&= \frac{x^2}{2} + 3x + \frac{2}{x} + C
\end{aligned}
$$

> ⚠️ **Common mistake**: Do not try to integrate the fraction as a whole! You must first separate the fraction into a sum of individual terms before integrating term by term.

---

## 7.2 Basic Integration Formulas (Complete Derivations with Many Examples)

This section is **the most core content of this chapter**. All formulas must be memorised thoroughly, as the examination **does not provide a formula sheet**. For each formula, I will provide:
1. The formula itself
2. Derivation starting from differentiation
3. At least 3 worked examples (from basic to comprehensive)

---

### 7.2.1 Power Rule for Integration: $\displaystyle \int x^n \, dx \quad (n \neq -1)$

**Formula**:

$$
\boxed{\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)}
$$

**Derivation**: Differentiate the right-hand side:

$$
\frac{d}{dx}\left(\frac{x^{n+1}}{n+1} + C\right) = \frac{n+1}{n+1} x^{n} = x^n
$$

The derivative equals the integrand $x^n$, proving the formula.

**Key points to understand**:
- **Add 1 to the exponent**: $n \to n+1$
- **Divide by the new exponent**: divide by $(n+1)$
- This formula holds for **all rational numbers** $n \neq -1$, including negative numbers and fractions

**Quick reference table for common exponent forms**:

| Integrand | Rewritten as power | Integration result |
|---------|-------------|---------|
| $x^5$ | $x^5$ | $\dfrac{x^6}{6}$ |
| $\dfrac{1}{x^3}$ | $x^{-3}$ | $\dfrac{x^{-2}}{-2} = -\dfrac{1}{2x^2}$ |
| $\sqrt{x}$ | $x^{1/2}$ | $\dfrac{x^{3/2}}{3/2} = \dfrac{2}{3}x^{3/2}$ |
| $\dfrac{1}{\sqrt{x}}$ | $x^{-1/2}$ | $\dfrac{x^{1/2}}{1/2} = 2\sqrt{x}$ |
| $\sqrt[3]{x^2}$ | $x^{2/3}$ | $\dfrac{x^{5/3}}{5/3} = \dfrac{3}{5}x^{5/3}$ |

---

**Example 1** (Positive integer exponent): Find $\displaystyle \int x^8 \, dx$.

**Solution**:

$$
\int x^8 \, dx = \frac{x^{8+1}}{8+1} + C = \frac{x^9}{9} + C
$$

**Verification**: $\dfrac{d}{dx}\left(\dfrac{x^9}{9}\right) = \dfrac{9x^8}{9} = x^8$. ✓

---

**Example 2** (Negative exponent): Find $\displaystyle \int \frac{1}{x^4} \, dx$.

**Solution**:

First rewrite: $\dfrac{1}{x^4} = x^{-4}$

$$
\int x^{-4} \, dx = \frac{x^{-4+1}}{-4+1} + C = \frac{x^{-3}}{-3} + C = -\frac{1}{3x^3} + C
$$

**Verification**: $\dfrac{d}{dx}\left(-\dfrac{1}{3}x^{-3}\right) = -\dfrac{1}{3} \cdot (-3)x^{-4} = x^{-4}$. ✓

> ⚠️ **Common mistake**: When $n = -4$, $n+1 = -3$ (not $-5$!). Many students mistakenly think that adding 1 makes the exponent more negative, but in fact $-4+1 = -3$. Always writing out the intermediate steps can help avoid this type of error.

---

**Example 3** (Fractional exponent — square root): Find $\displaystyle \int \sqrt{x} \, dx$.

**Solution**:

$\sqrt{x} = x^{1/2}$

$$
\int x^{1/2} \, dx = \frac{x^{1/2+1}}{1/2+1} + C = \frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C
$$

This can also be written as $\dfrac{2}{3}\sqrt{x^3} + C$ or $\dfrac{2}{3}x\sqrt{x} + C$.

**Verification**: $\dfrac{d}{dx}\left(\dfrac{2}{3}x^{3/2}\right) = \dfrac{2}{3} \cdot \dfrac{3}{2}x^{1/2} = x^{1/2} = \sqrt{x}$. ✓

---

**Example 4** (Fractional exponent — cube root): Find $\displaystyle \int \sqrt[3]{x} \, dx$.

**Solution**:

$\sqrt[3]{x} = x^{1/3}$

$$
\int x^{1/3} \, dx = \frac{x^{1/3+1}}{1/3+1} + C = \frac{x^{4/3}}{4/3} + C = \frac{3}{4}x^{4/3} + C
$$

---

**Example 5** (Negative fractional exponent): Find $\displaystyle \int \frac{1}{\sqrt[3]{x^2}} \, dx$.

**Solution**:

$\dfrac{1}{\sqrt[3]{x^2}} = \dfrac{1}{x^{2/3}} = x^{-2/3}$

$$
\int x^{-2/3} \, dx = \frac{x^{-2/3+1}}{-2/3+1} + C = \frac{x^{1/3}}{1/3} + C = 3x^{1/3} + C = 3\sqrt[3]{x} + C
$$

**Verification**: $\dfrac{d}{dx}(3x^{1/3}) = 3 \cdot \dfrac{1}{3}x^{-2/3} = x^{-2/3} = \dfrac{1}{\sqrt[3]{x^2}}$. ✓

---

**Example 6** (Comprehensive — mixed terms): Find $\displaystyle \int \left( 4x^3 + \frac{2}{x^5} - 3\sqrt{x} + \frac{1}{\sqrt{x}} \right) dx$.

**Solution**:

First rewrite each term in power form:

$$
4x^3 + 2x^{-5} - 3x^{1/2} + x^{-1/2}
$$

Integrate term by term:

$$
\begin{aligned}
\int 4x^3 \, dx &= 4 \cdot \frac{x^4}{4} = x^4 \\[4pt]
\int 2x^{-5} \, dx &= 2 \cdot \frac{x^{-4}}{-4} = -\frac{1}{2}x^{-4} = -\frac{1}{2x^4} \\[4pt]
\int -3x^{1/2} \, dx &= -3 \cdot \frac{x^{3/2}}{3/2} = -3 \cdot \frac{2}{3}x^{3/2} = -2x^{3/2} \\[4pt]
\int x^{-1/2} \, dx &= \frac{x^{1/2}}{1/2} = 2x^{1/2} = 2\sqrt{x}
\end{aligned}
$$

Combine the results:

$$
\int \left( 4x^3 + \frac{2}{x^5} - 3\sqrt{x} + \frac{1}{\sqrt{x}} \right) dx = x^4 - \frac{1}{2x^4} - 2x^{3/2} + 2\sqrt{x} + C
$$

---

### 7.2.2 Special Case: $\displaystyle \int \frac{1}{x} \, dx$

**Formula**:

$$
\boxed{\int \frac{1}{x} \, dx = \ln |x| + C}
$$

**Why is $n=-1$ a special case?**

Recall the power rule: $\displaystyle \int x^n \, dx = \frac{x^{n+1}}{n+1} + C$. If $n = -1$, then $n+1 = 0$, making the denominator zero — the formula breaks down! Therefore the integral of $\dfrac{1}{x}$ needs to be handled separately.

**Derivation**: Recall the derivative of $\ln x$.

When $x > 0$:

$$
\frac{d}{dx}(\ln x) = \frac{1}{x}
$$

When $x < 0$, $|x| = -x > 0$, by the chain rule:

$$
\frac{d}{dx}[\ln (-x)] = \frac{1}{-x} \cdot (-1) = \frac{1}{x}
$$

Both cases can be uniformly written as $\dfrac{d}{dx}(\ln |x|) = \dfrac{1}{x}$, therefore $\displaystyle \int \frac{1}{x} \, dx = \ln |x| + C$.

> ⚠️ **The absolute value sign cannot be omitted!** It ensures the formula still holds when $x$ is negative.

**Comparison with the Power Rule**:

$$
\int x^2 \, dx = \frac{x^3}{3} + C, \quad \int x^1 \, dx = \frac{x^2}{2} + C, \quad \int x^0 \, dx = x + C, \quad \int x^{-1} \, dx = \ln|x| + C
$$

Note that $x^0 = 1$, whose integral is $x$, not $\ln|x|$ — only $x^{-1}$ gives $\ln|x|$.

---

**Example 1** (Basic form): Find $\displaystyle \int \frac{5}{x} \, dx$.

**Solution**:

$$
\int \frac{5}{x} \, dx = 5 \int \frac{1}{x} \, dx = 5\ln |x| + C
$$

---

**Example 2** (Mixed with power functions): Find $\displaystyle \int \left( x^3 - \frac{2}{x} \right) dx$.

**Solution**:

$$
\int \left( x^3 - \frac{2}{x} \right) dx = \frac{x^4}{4} - 2\ln|x| + C
$$

---

**Example 3** (Simplify before integrating — common exam type): Find $\displaystyle \int \frac{x^2 + 3x - 1}{x} \, dx$.

**Solution**:

First simplify:

$$
\frac{x^2 + 3x - 1}{x} = x + 3 - \frac{1}{x}
$$

Then integrate:

$$
\int \left( x + 3 - \frac{1}{x} \right) dx = \frac{x^2}{2} + 3x - \ln|x| + C
$$

> ⚠️ **Common mistake**: Some students try to apply the power rule directly to $\dfrac{x^2+3x-1}{x}$ as a whole — this is not allowed! You must first simplify it into a sum of individual terms.

---

**Example 4** (Carefully distinguish $\dfrac{1}{x}$ from $x^{-2}$): Find $\displaystyle \int \frac{x^3 - 2x^2 + 1}{x^2} \, dx$.

**Solution**:

Simplify:

$$
\frac{x^3 - 2x^2 + 1}{x^2} = x - 2 + \frac{1}{x^2} = x - 2 + x^{-2}
$$

Integrate:

$$
\int (x - 2 + x^{-2}) \, dx = \frac{x^2}{2} - 2x + \frac{x^{-1}}{-1} + C = \frac{x^2}{2} - 2x - \frac{1}{x} + C
$$

Notice that here $x^{-2}$ uses the power rule ($n=-2 \neq -1$), and only $\dfrac{1}{x} = x^{-1}$ uses $\ln|x|$. Do not confuse the two!

---

### 7.2.3 Integrating Linear Composite Forms: $\displaystyle \int (ax+b)^n \, dx$

**Formula** ($n \neq -1$):

$$
\boxed{\int (ax+b)^n \, dx = \frac{(ax+b)^{n+1}}{a(n+1)} + C \quad (n \neq -1)}
$$

When $n = -1$:

$$
\boxed{\int \frac{1}{ax+b} \, dx = \frac{1}{a} \ln |ax+b| + C}
$$

**Derivation** (using substitution thinking):

Let $u = ax+b$, then $du = a \, dx$, i.e., $dx = \dfrac{du}{a}$.

$$
\int (ax+b)^n \, dx = \int u^n \cdot \frac{du}{a} = \frac{1}{a} \int u^n \, du = \frac{1}{a} \cdot \frac{u^{n+1}}{n+1} + C = \frac{(ax+b)^{n+1}}{a(n+1)} + C
$$

**Intuitive understanding**: Compare with $\int x^n \, dx = \dfrac{x^{n+1}}{n+1}$. Here $x$ is replaced by $(ax+b)$, but an extra factor of $\dfrac{1}{a}$ appears. This $\dfrac{1}{a}$ comes from the reverse of the chain rule — because the derivative of $(ax+b)$ is $a$, so in the reverse operation we must divide by $a$.

**Memory aid**: "Add 1 to the exponent, divide by the new exponent, then divide by $a$."

---

**Example 1** (Positive integer $n$): Find $\displaystyle \int (5x+2)^3 \, dx$.

**Solution**:

Here $a=5$, $n=3$.

$$
\int (5x+2)^3 \, dx = \frac{(5x+2)^{4}}{5 \cdot 4} + C = \frac{(5x+2)^4}{20} + C
$$

**Verification**: $\dfrac{d}{dx}\left[\dfrac{(5x+2)^4}{20}\right] = \dfrac{4(5x+2)^3 \cdot 5}{20} = \dfrac{20(5x+2)^3}{20} = (5x+2)^3$. ✓

---

**Example 2** (Negative integer $n$): Find $\displaystyle \int \frac{1}{(3x-1)^4} \, dx$.

**Solution**:

Rewrite as $(3x-1)^{-4}$, $a=3$, $n=-4$.

$$
\int (3x-1)^{-4} \, dx = \frac{(3x-1)^{-3}}{3 \cdot (-3)} + C = -\frac{1}{9}(3x-1)^{-3} + C = -\frac{1}{9(3x-1)^3} + C
$$

---

**Example 3** (Fractional $n$ — radical form): Find $\displaystyle \int \sqrt{4x+3} \, dx$.

**Solution**:

$\sqrt{4x+3} = (4x+3)^{1/2}$, $a=4$, $n=\dfrac{1}{2}$.

$$
\int (4x+3)^{1/2} \, dx = \frac{(4x+3)^{3/2}}{4 \cdot (3/2)} + C = \frac{(4x+3)^{3/2}}{6} + C
$$

i.e., $\dfrac{1}{6}(4x+3)^{3/2} + C$.

---

**Example 4** ($n=-1$ case — logarithmic form): Find $\displaystyle \int \frac{1}{2x+5} \, dx$.

**Solution**:

$a=2$, use $\displaystyle \int \frac{1}{ax+b} \, dx = \frac{1}{a}\ln|ax+b| + C$.

$$
\int \frac{1}{2x+5} \, dx = \frac{1}{2} \ln|2x+5| + C
$$

**Verification**: $\dfrac{d}{dx}\left(\dfrac{1}{2}\ln|2x+5|\right) = \dfrac{1}{2} \cdot \dfrac{1}{2x+5} \cdot 2 = \dfrac{1}{2x+5}$. ✓

---

**Example 5** (Comprehensive — two terms mixed): Find $\displaystyle \int \left( \frac{1}{(3x-2)^2} + \frac{4}{x+1} \right) dx$.

**Solution**:

First term: $\displaystyle \int (3x-2)^{-2} \, dx = \frac{(3x-2)^{-1}}{3 \cdot (-1)} + C_1 = -\frac{1}{3(3x-2)} + C_1$

Second term: $\displaystyle \int \frac{4}{x+1} \, dx = 4\ln|x+1| + C_2$

Combine:

$$
\int \left( \frac{1}{(3x-2)^2} + \frac{4}{x+1} \right) dx = -\frac{1}{3(3x-2)} + 4\ln|x+1| + C
$$

---

**Example 6** (Requires simplifying before using formula): Find $\displaystyle \int \frac{2x+3}{(x+1)^2} \, dx$.

**Solution**:

This type of problem requires first decomposing the fraction into partial fractions:

$$
\frac{2x+3}{(x+1)^2} = \frac{2(x+1)+1}{(x+1)^2} = \frac{2}{x+1} + \frac{1}{(x+1)^2}
$$

Then integrate term by term:

$$
\int \frac{2}{x+1} \, dx = 2\ln|x+1|, \quad \int (x+1)^{-2} \, dx = \frac{(x+1)^{-1}}{-1} = -\frac{1}{x+1}
$$

Result:

$$
\int \frac{2x+3}{(x+1)^2} \, dx = 2\ln|x+1| - \frac{1}{x+1} + C
$$

---

### 7.2.4 Integrating Exponential Functions: $\displaystyle \int e^{ax+b} \, dx$

**Formula**:

$$
\boxed{\int e^{ax+b} \, dx = \frac{1}{a} e^{ax+b} + C \quad (a \neq 0)}
$$

**Derivation**: Differentiate the right-hand side:

$$
\frac{d}{dx}\left(\frac{1}{a} e^{ax+b} + C\right) = \frac{1}{a} \cdot e^{ax+b} \cdot a = e^{ax+b}
$$

**Understanding**: Similar to the $(ax+b)^n$ case, dividing by $a$ is because the chain rule gives $(ax+b)' = a$, and the reverse operation produces the factor $\frac{1}{a}$.

In fact, these two formulas can be understood uniformly: when integrating a linear composite function $f(ax+b)$, the result always contains an extra factor $\frac{1}{a}$.

> **Additional knowledge** (for awareness only, not in IGCSE): For a general base $a^x$ ($a>0, a\neq1$), $\displaystyle \int a^x \, dx = \frac{a^x}{\ln a} + C$. This is because $\dfrac{d}{dx}(a^x) = a^x \ln a$.

---

**Example 1** (Basic): Find $\displaystyle \int e^{4x} \, dx$.

**Solution**:

$$
\int e^{4x} \, dx = \frac{1}{4} e^{4x} + C
$$

---

**Example 2** (Negative coefficient): Find $\displaystyle \int e^{-2x} \, dx$.

**Solution**:

$a = -2$, so $\dfrac{1}{a} = -\dfrac{1}{2}$.

$$
\int e^{-2x} \, dx = -\frac{1}{2} e^{-2x} + C
$$

---

**Example 3** (With constant term): Find $\displaystyle \int e^{3x-2} \, dx$.

**Solution**:

$a=3$, $b=-2$.

$$
\int e^{3x-2} \, dx = \frac{1}{3} e^{3x-2} + C
$$

---

**Example 4** (Fractional coefficient): Find $\displaystyle \int e^{\frac{x}{3} + \pi} \, dx$.

**Solution**:

$a = \dfrac{1}{3}$, $\dfrac{1}{a} = 3$.

$$
\int e^{\frac{x}{3} + \pi} \, dx = 3 e^{\frac{x}{3} + \pi} + C
$$

---

**Example 5** (Exponential and polynomial mixed): Find $\displaystyle \int (2x^4 - 3e^{2x} + e) \, dx$.

**Solution**:

Note that $e$ is a constant (Euler's number, $e \approx 2.718$), so $\int e \, dx = ex$.

$$
\begin{aligned}
\int 2x^4 \, dx &= 2 \cdot \frac{x^5}{5} = \frac{2}{5}x^5 \\[4pt]
\int -3e^{2x} \, dx &= -3 \cdot \frac{1}{2} e^{2x} = -\frac{3}{2}e^{2x} \\[4pt]
\int e \, dx &= ex
\end{aligned}
$$

Result:

$$
\int (2x^4 - 3e^{2x} + e) \, dx = \frac{2}{5}x^5 - \frac{3}{2}e^{2x} + ex + C
$$

---

**Example 6** (Exponential mixed — positive and negative exponents): Find $\displaystyle \int (e^{3x} + e^{-3x}) \, dx$.

**Solution**:

$$
\int e^{3x} \, dx = \frac{1}{3}e^{3x}, \quad \int e^{-3x} \, dx = -\frac{1}{3}e^{-3x}
$$

Result:

$$
\int (e^{3x} + e^{-3x}) \, dx = \frac{1}{3}e^{3x} - \frac{1}{3}e^{-3x} + C = \frac{1}{3}(e^{3x} - e^{-3x}) + C
$$

---

### 7.2.5 Integrating Trigonometric Functions

The three basic trigonometric integration formulas are all derived by reversing the derivative formulas learned in Chapter 5.

**Quick reference table**:

| Derivative formula | Corresponding integral formula |
|---------|------------|
| $\dfrac{d}{dx}(\sin x) = \cos x$ | $\displaystyle \int \cos x \, dx = \sin x + C$ |
| $\dfrac{d}{dx}(\cos x) = -\sin x$ | $\displaystyle \int \sin x \, dx = -\cos x + C$ |
| $\dfrac{d}{dx}(\tan x) = \sec^2 x$ | $\displaystyle \int \sec^2 x \, dx = \tan x + C$ |

For the more general $ax+b$ form, all three formulas follow the "divide by $a$" pattern.

---

#### (1) $\displaystyle \int \sin(ax+b) \, dx$

**Formula**:

$$
\boxed{\int \sin(ax+b) \, dx = -\frac{1}{a} \cos(ax+b) + C}
$$

**Derivation**: Assume the antiderivative is $k \cos(ax+b)$. Differentiating gives:

$$
\frac{d}{dx}[k \cos(ax+b)] = k \cdot [-\sin(ax+b)] \cdot a = -ak \sin(ax+b)
$$

We want $-ak = 1$, i.e., $k = -\dfrac{1}{a}$. Therefore the antiderivative is $-\dfrac{1}{a}\cos(ax+b)$.

**Verification**:

$$
\frac{d}{dx}\left(-\frac{1}{a}\cos(ax+b) + C\right) = -\frac{1}{a} \cdot [-\sin(ax+b)] \cdot a = \sin(ax+b) \quad \checkmark
$$

**Key points to remember**:
- $\sin$ integrates to $-\cos$ (note the negative sign)
- Then divide by $a$

---

**Example 1** (Basic): Find $\displaystyle \int \sin(2x) \, dx$.

**Solution**:

$$
\int \sin(2x) \, dx = -\frac{1}{2} \cos(2x) + C
$$

---

**Example 2** (With phase shift): Find $\displaystyle \int \sin(3x + \pi) \, dx$.

**Solution**:

$a=3$, $b=\pi$.

$$
\int \sin(3x + \pi) \, dx = -\frac{1}{3} \cos(3x + \pi) + C
$$

Using $\cos(\theta+\pi) = -\cos\theta$, this simplifies to $\dfrac{1}{3}\cos(3x) + C$, though this is not necessary.

---

**Example 3** (With coefficient): Find $\displaystyle \int -5\sin\left(\frac{x}{2}\right) dx$.

**Solution**:

$a = \dfrac{1}{2}$, $\dfrac{1}{a} = 2$.

$$
\int -5\sin\left(\frac{x}{2}\right) dx = -5 \cdot \left(-2\cos\left(\frac{x}{2}\right)\right) + C = 10\cos\left(\frac{x}{2}\right) + C
$$

---

#### (2) $\displaystyle \int \cos(ax+b) \, dx$

**Formula**:

$$
\boxed{\int \cos(ax+b) \, dx = \frac{1}{a} \sin(ax+b) + C}
$$

**Derivation**: Assume the antiderivative is $k \sin(ax+b)$. Differentiating gives:

$$
\frac{d}{dx}[k \sin(ax+b)] = k \cdot \cos(ax+b) \cdot a = ak \cos(ax+b)
$$

Set $ak = 1$, giving $k = \dfrac{1}{a}$.

**Verification**:

$$
\frac{d}{dx}\left(\frac{1}{a}\sin(ax+b) + C\right) = \frac{1}{a} \cdot \cos(ax+b) \cdot a = \cos(ax+b) \quad \checkmark
$$

**Key points to remember**:
- $\cos$ integrates to $\sin$ (no negative sign)
- Then divide by $a$

---

**Example 1** (Basic): Find $\displaystyle \int \cos(5x) \, dx$.

**Solution**:

$$
\int \cos(5x) \, dx = \frac{1}{5} \sin(5x) + C
$$

---

**Example 2** (With phase shift and coefficient): Find $\displaystyle \int 3\cos(2x-1) \, dx$.

**Solution**:

$$
\int 3\cos(2x-1) \, dx = 3 \cdot \frac{1}{2} \sin(2x-1) + C = \frac{3}{2} \sin(2x-1) + C
$$

---

**Example 3** (Using even function property): Find $\displaystyle \int \cos(-3x) \, dx$.

**Solution**:

Using $\cos(-\theta) = \cos\theta$ (cosine is an even function):

$$
\int \cos(-3x) \, dx = \int \cos(3x) \, dx = \frac{1}{3} \sin(3x) + C
$$

Or directly using the formula with $a=-3$:

$$
\int \cos(-3x) \, dx = \frac{1}{-3} \sin(-3x) + C = -\frac{1}{3}[-\sin(3x)] + C = \frac{1}{3}\sin(3x) + C
$$

Both methods give the same result.

---

#### (3) $\displaystyle \int \sec^2(ax+b) \, dx$

**Formula**:

$$
\boxed{\int \sec^2(ax+b) \, dx = \frac{1}{a} \tan(ax+b) + C}
$$

**Derivation**: $\dfrac{d}{dx}(\tan x) = \sec^2 x$, therefore:

$$
\frac{d}{dx}\left(\frac{1}{a} \tan(ax+b)\right) = \frac{1}{a} \cdot \sec^2(ax+b) \cdot a = \sec^2(ax+b)
$$

**Key points to remember**:
- $\sec^2$ integrates to $\tan$ (no negative sign)
- Then divide by $a$

---

**Example 1** (Basic): Find $\displaystyle \int \sec^2(3x) \, dx$.

**Solution**:

$$
\int \sec^2(3x) \, dx = \frac{1}{3} \tan(3x) + C
$$

---

**Example 2** (With phase shift): Find $\displaystyle \int \sec^2\left(2x - \frac{\pi}{4}\right) dx$.

**Solution**:

$$
\int \sec^2\left(2x - \frac{\pi}{4}\right) dx = \frac{1}{2} \tan\left(2x - \frac{\pi}{4}\right) + C
$$

---

**Example 3** (Comprehensive): Find $\displaystyle \int (2\sec^2 x - 3\sec^2(4x)) \, dx$.

**Solution**:

$$
\int 2\sec^2 x \, dx = 2\tan x, \quad \int -3\sec^2(4x) \, dx = -3 \cdot \frac{1}{4} \tan(4x) = -\frac{3}{4}\tan(4x)
$$

Result:

$$
\int (2\sec^2 x - 3\sec^2(4x)) \, dx = 2\tan x - \frac{3}{4}\tan(4x) + C
$$

---

### 7.2.6 Super Comprehensive Examples (Complete Skills Check)

The following examples cover all types of integration techniques in this chapter. It is recommended to try them yourself first before checking the solutions.

---

**Example 1** (Six-term mix — all types): Find $\displaystyle \int \left( 8x^7 - \frac{3}{x^4} + 5e^{2x} + 2\sin 3x - 4\cos\left(\frac{x}{2}\right) + 6\sec^2(5x) \right) dx$.

**Solution**:

Process each term:

| Term | Integration process | Result |
|---|---------|------|
| $8x^7$ | $8 \cdot \dfrac{x^8}{8}$ | $x^8$ |
| $-\dfrac{3}{x^4} = -3x^{-4}$ | $-3 \cdot \dfrac{x^{-3}}{-3}$ | $\dfrac{1}{x^3}$ |
| $5e^{2x}$ | $5 \cdot \dfrac{1}{2}e^{2x}$ | $\dfrac{5}{2}e^{2x}$ |
| $2\sin 3x$ | $2 \cdot \left(-\dfrac{1}{3}\cos 3x\right)$ | $-\dfrac{2}{3}\cos 3x$ |
| $-4\cos\left(\dfrac{x}{2}\right)$ | $-4 \cdot \dfrac{1}{1/2}\sin\left(\dfrac{x}{2}\right) = -4 \cdot 2\sin\left(\dfrac{x}{2}\right)$ | $-8\sin\left(\dfrac{x}{2}\right)$ |
| $6\sec^2(5x)$ | $6 \cdot \dfrac{1}{5}\tan(5x)$ | $\dfrac{6}{5}\tan(5x)$ |

Combine:

$$
\boxed{x^8 + \frac{1}{x^3} + \frac{5}{2}e^{2x} - \frac{2}{3}\cos 3x - 8\sin\left(\frac{x}{2}\right) + \frac{6}{5}\tan(5x) + C}
$$

---

**Example 2** (Expand first, then integrate — polynomial product): Find $\displaystyle \int (x^2 - 1)(x^2 + 2) \, dx$.

**Solution**:

Expand: $(x^2 - 1)(x^2 + 2) = x^4 + 2x^2 - x^2 - 2 = x^4 + x^2 - 2$

Integrate:

$$
\int (x^4 + x^2 - 2) \, dx = \frac{x^5}{5} + \frac{x^3}{3} - 2x + C
$$

---

**Example 3** (Simplify fraction first, then integrate): Find $\displaystyle \int \frac{2x^4 - 3x^2 + 5x - 1}{x^2} \, dx$.

**Solution**:

Simplify:

$$
\frac{2x^4 - 3x^2 + 5x - 1}{x^2} = 2x^2 - 3 + \frac{5}{x} - \frac{1}{x^2} = 2x^2 - 3 + 5x^{-1} - x^{-2}
$$

Integrate:

$$
\begin{aligned}
\int (2x^2 - 3 + 5x^{-1} - x^{-2}) \, dx &= 2 \cdot \frac{x^3}{3} - 3x + 5\ln|x| - \frac{x^{-1}}{-1} + C \\[4pt]
&= \frac{2}{3}x^3 - 3x + 5\ln|x| + \frac{1}{x} + C
\end{aligned}
$$

---

**Example 4** ($(ax+b)^n$ mixed with trigonometric and exponential): Find $\displaystyle \int \left( (3x+1)^4 + \frac{2}{5x-3} - \sin\left(4x-\frac{\pi}{6}\right) \right) dx$.

**Solution**:

First term: $\displaystyle \int (3x+1)^4 \, dx = \frac{(3x+1)^5}{3 \cdot 5} + C_1 = \frac{(3x+1)^5}{15} + C_1$

Second term: $\displaystyle \int \frac{2}{5x-3} \, dx = 2 \cdot \frac{1}{5} \ln|5x-3| + C_2 = \frac{2}{5}\ln|5x-3| + C_2$

Third term: $\displaystyle \int -\sin\left(4x-\frac{\pi}{6}\right) dx = -\left(-\frac{1}{4}\right)\cos\left(4x-\frac{\pi}{6}\right) + C_3 = \frac{1}{4}\cos\left(4x-\frac{\pi}{6}\right) + C_3$

Combine:

$$
\int \left( (3x+1)^4 + \frac{2}{5x-3} - \sin\left(4x-\frac{\pi}{6}\right) \right) dx = \frac{(3x+1)^5}{15} + \frac{2}{5}\ln|5x-3| + \frac{1}{4}\cos\left(4x-\frac{\pi}{6}\right) + C
$$

---

## 7.3 Definite Integrals

### 7.3.1 From Indefinite to Definite Integrals — The Fundamental Theorem of Calculus

An **indefinite integral** $\displaystyle \int f(x) \, dx$ gives a **family of functions** (containing an arbitrary constant $C$), while a **definite integral** $\displaystyle \int_a^b f(x) \, dx$ gives a **numerical value** — it represents the "accumulated effect" of the function $f(x)$ over the interval $[a, b]$.

The bridge connecting them is the **Fundamental Theorem of Calculus (FTC)**, also known as the **Newton-Leibniz formula**:

$$
\boxed{\int_a^b f(x) \, dx = F(b) - F(a)}
$$

where $F'(x) = f(x)$, i.e., $F(x)$ is any antiderivative of $f(x)$.

**Intuitive derivation**:

Consider the function $A(x) = \int_a^x f(t) \, dt$, which represents the accumulated area from $a$ to $x$. When $x$ increases by a small amount $h$:

$$
A(x+h) - A(x) \approx f(x) \cdot h
$$

Therefore:

$$
\lim_{h \to 0} \frac{A(x+h) - A(x)}{h} = f(x)
$$

i.e., $A'(x) = f(x)$. So $A(x)$ is an antiderivative of $f(x)$. Let $F(x)$ be any antiderivative of $f(x)$, then $F(x) = A(x) + C$. Hence:

$$
F(b) - F(a) = [A(b) + C] - [A(a) + C] = A(b) - A(a) = A(b) - 0 = \int_a^b f(x) \, dx
$$

**Common notation**:

$$
\int_a^b f(x) \, dx = \big[ F(x) \big]_{a}^{b} = \big[ F(x) \big]_{x=a}^{x=b} = F(b) - F(a)
$$

> ⚠️ **Key distinction**: In definite integrals, **do not add the constant of integration $C$**, because it cancels out when computing $F(b)-F(a)$.

---

### 7.3.2 Properties of Definite Integrals

**Property 1 (Linearity)**:

$$
\int_a^b [c f(x) + d g(x)] \, dx = c \int_a^b f(x) \, dx + d \int_a^b g(x) \, dx
$$

**Property 2 (Interval additivity)** — one of the most important properties:

$$
\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx
$$

This theorem is crucial for handling cases where the function changes sign. When $f(x)$ changes sign on $[a,b]$, we need to split the interval at the zeros — this is precisely the application of Property 2.

**Property 3 (Reverse interval)**:

$$
\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx
$$

**Derivation**: $\int_a^b f(x) \, dx = F(b)-F(a) = -[F(a)-F(b)] = -\int_b^a f(x) \, dx$.

**Property 4 (Zero interval)**:

$$
\int_a^a f(x) \, dx = 0
$$

**Property 5 (Comparison property)**: If $f(x) \geq g(x)$ on $[a,b]$, then:

$$
\int_a^b f(x) \, dx \geq \int_a^b g(x) \, dx
$$

---

### 7.3.3 Procedure for Computing Definite Integrals

General steps for computing definite integrals:

1. **Find the antiderivative**: Find an antiderivative $F(x)$ of the integrand $f(x)$ (without adding $C$)
2. **Substitute the limits**: Compute $F(b) - F(a)$
3. **Simplify the result**: Give the final numerical value or simplified expression

---

**Example 1** (Simple power function — geometric verification): Evaluate $\displaystyle \int_1^4 (2x+1) \, dx$.

**Solution**:

First find the antiderivative: $\displaystyle \int (2x+1) \, dx = x^2 + x + C$

So:

$$
\int_1^4 (2x+1) \, dx = \big[ x^2 + x \big]_{1}^{4} = (16 + 4) - (1 + 1) = 20 - 2 = 18
$$

**Geometric verification**: $y=2x+1$ is a straight line. At $x=1$, $y=3$; at $x=4$, $y=9$; interval length $3$. Trapezoid area $= \dfrac{3+9}{2} \times 3 = 18$, consistent with the integration result. ✓

---

**Example 2** (Quadratic function): Evaluate $\displaystyle \int_{-1}^{2} (x^2 - 2x + 3) \, dx$.

**Solution**:

$$
\begin{aligned}
\int_{-1}^{2} (x^2 - 2x + 3) \, dx &= \left[ \frac{x^3}{3} - x^2 + 3x \right]_{-1}^{2} \\[4pt]
&= \left( \frac{8}{3} - 4 + 6 \right) - \left( -\frac{1}{3} - 1 - 3 \right) \\[4pt]
&= \left( \frac{8}{3} + 2 \right) - \left( -\frac{1}{3} - 4 \right) \\[4pt]
&= \frac{14}{3} - \left( -\frac{13}{3} \right) = \frac{27}{3} = 9
\end{aligned}
$$

---

**Example 3** (Trigonometric function): Evaluate $\displaystyle \int_0^{\pi} \cos x \, dx$.

**Solution**:

$$
\int_0^{\pi} \cos x \, dx = \big[ \sin x \big]_{0}^{\pi} = \sin \pi - \sin 0 = 0 - 0 = 0
$$

**Geometric meaning**: The cosine function on $[0,\pi]$ is positive on $[0,\pi/2]$ and negative on $[\pi/2,\pi]$. The positive and negative areas exactly cancel out, so the signed area is zero.

---

**Example 4** (Exponential and $1/x$ mixed): Evaluate $\displaystyle \int_1^2 \left( e^{3x} + \frac{2}{x} \right) dx$.

**Solution**:

$$
\begin{aligned}
\int_1^2 \left( e^{3x} + \frac{2}{x} \right) dx &= \left[ \frac{1}{3} e^{3x} + 2\ln|x| \right]_1^2 \\[4pt]
&= \left( \frac{1}{3} e^{6} + 2\ln 2 \right) - \left( \frac{1}{3} e^{3} + 2\ln 1 \right) \\[4pt]
&= \frac{1}{3}(e^6 - e^3) + 2\ln 2
\end{aligned}
$$

(Note that $\ln 1 = 0$)

---

**Example 5** ($(ax+b)^n$ form — comparison of two methods): Evaluate $\displaystyle \int_0^1 (3x+2)^4 \, dx$.

**Solution**:

Method 1 (Using the formula directly): $a=3$, $n=4$.

$$
\int (3x+2)^4 \, dx = \frac{(3x+2)^5}{3 \cdot 5} = \frac{(3x+2)^5}{15}
$$

$$
\int_0^1 (3x+2)^4 \, dx = \left[ \frac{(3x+2)^5}{15} \right]_0^1 = \frac{5^5}{15} - \frac{2^5}{15} = \frac{3125}{15} - \frac{32}{15} = \frac{3093}{15} = \frac{1031}{5}
$$

Method 2 (Expand): $(3x+2)^4 = 81x^4 + 216x^3 + 216x^2 + 96x + 16$

$$
\int_0^1 (81x^4 + 216x^3 + 216x^2 + 96x + 16) \, dx = \left[ \frac{81x^5}{5} + 54x^4 + 72x^3 + 48x^2 + 16x \right]_0^1
$$

$$
= \frac{81}{5} + 54 + 72 + 48 + 16 = \frac{81}{5} + 190 = \frac{81}{5} + \frac{950}{5} = \frac{1031}{5}
$$

Both methods give the same result. ✓

---

**Example 6** (Definite integral with $\ln$): Evaluate $\displaystyle \int_2^4 \frac{1}{x-1} \, dx$.

**Solution**:

$$
\int_2^4 \frac{1}{x-1} \, dx = \big[ \ln|x-1| \big]_2^4 = \ln 3 - \ln 1 = \ln 3
$$

---

### 7.3.4 Definite Integrals and Signed Area

The definite integral $\int_a^b f(x) \, dx$ gives the **signed area**:

- When $f(x) \geq 0$, the integral value is positive, equal to the actual area between the curve and the $x$-axis
- When $f(x) \leq 0$, the integral value is negative, and its absolute value equals the actual area
- When $f(x)$ changes sign, the positive and negative parts cancel each other out

**Example**: Evaluate $\displaystyle \int_{-2}^{3} (x-1) \, dx$ and explain its geometric meaning.

**Solution**:

$$
\int_{-2}^{3} (x-1) \, dx = \left[ \frac{x^2}{2} - x \right]_{-2}^3 = \left( \frac{9}{2} - 3 \right) - \left( 2 + 2 \right) = \frac{3}{2} - 4 = -\frac{5}{2}
$$

The result is $-\dfrac{5}{2}$, indicating that on the interval $[-2,3]$, the area below the $x$-axis is $\dfrac{5}{2}$ square units more than the area above. The function $y=x-1$ crosses the $x$-axis at $x=1$; on $[-2,1]$ the curve is below the axis, and on $[1,3]$ the curve is above.

---

**Example 2** (Using symmetry to simplify computation): Evaluate $\displaystyle \int_{-a}^{a} x^3 \, dx$.

**Solution**:

Since $x^3$ is an odd function ($(-x)^3 = -x^3$), its integral over the symmetric interval $[-a,a]$ is zero:

$$
\int_{-a}^{a} x^3 \, dx = \left[ \frac{x^4}{4} \right]_{-a}^{a} = \frac{a^4}{4} - \frac{a^4}{4} = 0
$$

> **General rules**: The definite integral of an odd function over a symmetric interval is zero; the definite integral of an even function over a symmetric interval equals twice the integral over the half-interval.
> - $f$ is odd: $\int_{-a}^{a} f(x) \, dx = 0$
> - $f$ is even: $\int_{-a}^{a} f(x) \, dx = 2\int_{0}^{a} f(x) \, dx$

---

## 7.4 Plane Area

This section is one of the most important geometric applications of definite integrals. We will systematically learn how to use integration to compute the area of various plane figures.

### 7.4.1 Area Between a Curve and the $x$-axis

**Case 1**: $f(x) \geq 0$ on $[a,b]$

$$
A = \int_a^b f(x) \, dx
$$

**Case 2**: $f(x) \leq 0$ on $[a,b]$

$$
A = -\int_a^b f(x) \, dx = \int_a^b |f(x)| \, dx
$$

**Case 3**: $f(x)$ changes sign on $[a,b]$ (general case)

$$
A = \int_a^b |f(x)| \, dx
$$

**Standard solution procedure**:
1. **Solve $f(x) = 0$**: Find all intersection points of the curve with the $x$-axis
2. **Split the interval**: Use the zeros to divide the integration interval into several subintervals
3. **Determine the sign**: On each subinterval, take a test point to determine whether $f(x)$ is positive or negative
4. **Integrate by segments**: Integrate directly on positive intervals; take the absolute value (add a negative sign) on negative intervals
5. **Sum**: Add the areas of all subintervals

---

**Example 1** (Entirely above the $x$-axis): Find the area bounded by the curve $y = x^2 + 1$ and the $x$-axis from $x=0$ to $x=2$.

**Solution**:

On $[0,2]$, $x^2 + 1 \geq 1 > 0$, so integrate directly:

$$
A = \int_0^2 (x^2 + 1) \, dx = \left[ \frac{x^3}{3} + x \right]_0^2 = \left( \frac{8}{3} + 2 \right) - 0 = \frac{14}{3}
$$

---

**Example 2** (Entirely below the $x$-axis): Find the area bounded by the curve $y = -e^x$ and the $x$-axis from $x=-1$ to $x=1$.

**Solution**:

On $[-1,1]$, $-e^x < 0$, so the area is:

$$
A = -\int_{-1}^{1} (-e^x) \, dx = \int_{-1}^{1} e^x \, dx = \big[ e^x \big]_{-1}^{1} = e - e^{-1}
$$

---

**Example 3** (Sign change — piecewise approach): Find the total area bounded by the curve $y = x^2 - 1$ and the $x$-axis on $[-2, 2]$.

**Solution**:

**Step 1**: Find zeros. $x^2 - 1 = 0 \Rightarrow x = \pm 1$.

**Step 2**: The interval $[-2,2]$ is split by the three points $-2,-1,1,2$ into three subintervals: $[-2,-1]$, $[-1,1]$, $[1,2]$.

**Step 3**: Determine the sign.
- On $[-2,-1]$, take $x=-1.5$: $f(-1.5) = 2.25-1 = 1.25 > 0$, above the axis
- On $[-1,1]$, take $x=0$: $f(0) = -1 < 0$, below the axis
- On $[1,2]$, take $x=1.5$: $f(1.5) = 2.25-1 = 1.25 > 0$, above the axis

**Step 4**:

$$
\begin{aligned}
A &= \int_{-2}^{-1} (x^2-1) \, dx + \int_{-1}^{1} -(x^2-1) \, dx + \int_{1}^{2} (x^2-1) \, dx \\[4pt]
&= \left[ \frac{x^3}{3} - x \right]_{-2}^{-1} + \left[ -\frac{x^3}{3} + x \right]_{-1}^{1} + \left[ \frac{x^3}{3} - x \right]_{1}^{2}
\end{aligned}
$$

First part: $\left( -\frac{1}{3} + 1 \right) - \left( -\frac{8}{3} + 2 \right) = \frac{2}{3} - \left( -\frac{2}{3} \right) = \frac{4}{3}$

Second part: $\left( -\frac{1}{3} + 1 \right) - \left( \frac{1}{3} - 1 \right) = \frac{2}{3} - \left( -\frac{2}{3} \right) = \frac{4}{3}$

Third part: $\left( \frac{8}{3} - 2 \right) - \left( \frac{1}{3} - 1 \right) = \frac{2}{3} - \left( -\frac{2}{3} \right) = \frac{4}{3}$

Total area:

$$
A = \frac{4}{3} + \frac{4}{3} + \frac{4}{3} = 4
$$

---

**Example 4** (Typical exam question — downward-opening parabola): Find the area bounded by the curve $y = 9 - x^2$ and the $x$-axis.

**Solution**:

Intersections with the $x$-axis: $9 - x^2 = 0 \Rightarrow x = \pm 3$.

On $[-3,3]$, $9 - x^2 \geq 0$, so:

$$
\begin{aligned}
A &= \int_{-3}^{3} (9 - x^2) \, dx = \left[ 9x - \frac{x^3}{3} \right]_{-3}^{3} \\[4pt]
&= \left( 27 - 9 \right) - \left( -27 + 9 \right) \\[4pt]
&= 18 - (-18) = 36
\end{aligned}
$$

The area is $36$ square units.

---

**Example 5** (Cubic function — three zeros, two intervals): Find the total area bounded by the curve $y = x^3 - 4x$ and the $x$-axis on $[-2,2]$.

**Solution**:

**Step 1**: $x^3 - 4x = x(x^2-4) = x(x-2)(x+2) = 0$, zeros at $x = -2, 0, 2$.

**Step 2**: The interval is split into $[-2,0]$ and $[0,2]$.

**Step 3**:
- On $[-2,0]$, take $x=-1$: $f(-1) = -1 + 4 = 3 > 0$
- On $[0,2]$, take $x=1$: $f(1) = 1 - 4 = -3 < 0$

**Step 4**:

$$
\begin{aligned}
A &= \int_{-2}^{0} (x^3 - 4x) \, dx + \int_{0}^{2} -(x^3 - 4x) \, dx \\[4pt]
&= \left[ \frac{x^4}{4} - 2x^2 \right]_{-2}^{0} + \left[ -\frac{x^4}{4} + 2x^2 \right]_{0}^{2}
\end{aligned}
$$

First part: $(0) - \left( \frac{16}{4} - 8 \right) = -(4-8) = 4$

Second part: $\left( -\frac{16}{4} + 8 \right) - 0 = (-4+8) = 4$

Total area: $A = 4 + 4 = 8$

---

### 7.4.2 Area Between a Line and a Curve

**Core method**: If on the interval $[a,b]$, the curve $y = f(x)$ lies above the line $y = g(x)$ (i.e., $f(x) \geq g(x)$), then the area between them is:

$$
\boxed{A = \int_a^b [f(x) - g(x)] \, dx}
$$

**Solution procedure**:
1. Find intersection points: solve $f(x) = g(x)$
2. Determine the integration interval
3. Determine which function is above and which is below (take a test point in the interval)
4. Integrate the difference (upper minus lower)

---

**Example 1** (Curve above): Find the area bounded by the curve $y = x^2 + 1$ and the line $y = x + 3$.

**Solution**:

**Step 1**: Intersection points: $x^2 + 1 = x + 3 \Rightarrow x^2 - x - 2 = 0 \Rightarrow (x-2)(x+1) = 0$, giving $x = -1$ or $x = 2$.

**Step 2**: The interval is $[-1,2]$.

**Step 3**: Test with $x=0$: $f(0) = 1$, $g(0) = 3$, so $g(x) = x+3$ is above.

**Step 4**:

$$
\begin{aligned}
A &= \int_{-1}^{2} [(x+3) - (x^2+1)] \, dx \\[4pt]
&= \int_{-1}^{2} (2 + x - x^2) \, dx \\[4pt]
&= \left[ 2x + \frac{x^2}{2} - \frac{x^3}{3} \right]_{-1}^{2} \\[4pt]
&= \left( 4 + 2 - \frac{8}{3} \right) - \left( -2 + \frac{1}{2} + \frac{1}{3} \right) \\[4pt]
&= \frac{10}{3} - \left( -\frac{7}{6} \right) = \frac{10}{3} + \frac{7}{6} = \frac{27}{6} = \frac{9}{2}
\end{aligned}
$$

---

**Example 2** (Line above — classic problem): Find the area bounded by the line $y = 2x$ and the curve $y = x^2$.

**Solution**:

Intersection points: $x^2 = 2x \Rightarrow x^2 - 2x = 0 \Rightarrow x(x-2) = 0$, giving $x=0$ and $x=2$.

On $[0,2]$, test with $x=1$: $f(1)=1$, $g(1)=2$, so $y=2x$ is above.

$$
A = \int_0^2 (2x - x^2) \, dx = \left[ x^2 - \frac{x^3}{3} \right]_0^2 = \left( 4 - \frac{8}{3} \right) - 0 = \frac{4}{3}
$$

---

**Example 3** (Root function and line): Find the area bounded by the curve $y = \sqrt{x}$ and the line $y = \dfrac{x}{2}$.

**Solution**:

Intersection points: $\sqrt{x} = \dfrac{x}{2} \Rightarrow 2\sqrt{x} = x \Rightarrow x = 2\sqrt{x} \Rightarrow x - 2\sqrt{x} = 0 \Rightarrow \sqrt{x}(\sqrt{x} - 2) = 0$, giving $x=0$ or $x=4$.

On $[0,4]$, test with $x=1$: $\sqrt{1}=1$, $\dfrac{1}{2}=0.5$, so $y=\sqrt{x}$ is above.

$$
\begin{aligned}
A &= \int_0^4 \left( \sqrt{x} - \frac{x}{2} \right) dx = \int_0^4 \left( x^{1/2} - \frac{x}{2} \right) dx \\[4pt]
&= \left[ \frac{2}{3}x^{3/2} - \frac{x^2}{4} \right]_0^4 = \left( \frac{2}{3} \cdot 8 - \frac{16}{4} \right) - 0 = \frac{16}{3} - 4 = \frac{4}{3}
\end{aligned}
$$

---

### 7.4.3 Area Between Two Curves

When two curves $y = f(x)$ and $y = g(x)$ have multiple intersection points over an interval, piecewise handling is required — on each subinterval, determine which curve is above and which is below.

---

**Example 1** (Symmetric curves): Find the area bounded by $y = x^2$ and $y = 4 - x^2$.

**Solution**:

Intersection points: $x^2 = 4 - x^2 \Rightarrow 2x^2 = 4 \Rightarrow x^2 = 2 \Rightarrow x = \pm\sqrt{2}$.

On $[-\sqrt{2}, \sqrt{2}]$, test with $x=0$: $f(0)=0$, $g(0)=4$, so $y=4-x^2$ is above.

$$
\begin{aligned}
A &= \int_{-\sqrt{2}}^{\sqrt{2}} [(4 - x^2) - x^2] \, dx = \int_{-\sqrt{2}}^{\sqrt{2}} (4 - 2x^2) \, dx \\[4pt]
&= \left[ 4x - \frac{2x^3}{3} \right]_{-\sqrt{2}}^{\sqrt{2}} \\[4pt]
&= \left( 4\sqrt{2} - \frac{4\sqrt{2}}{3} \right) - \left( -4\sqrt{2} + \frac{4\sqrt{2}}{3} \right) \\[4pt]
&= \frac{8\sqrt{2}}{3} - \left( -\frac{8\sqrt{2}}{3} \right) = \frac{16\sqrt{2}}{3}
\end{aligned}
$$

---

**Example 2** (Upper/lower relationship changes — needs piecewise splitting): Find the total area bounded by $y = x^3$ and $y = x$.

**Solution**:

Intersection points: $x^3 = x \Rightarrow x^3 - x = 0 \Rightarrow x(x-1)(x+1) = 0$, giving $x = -1, 0, 1$.

The interval is split into $[-1,0]$ and $[0,1]$.

- On $[-1,0]$, test with $x=-0.5$: $f(-0.5) = -0.125$, $g(-0.5) = -0.5$, $y=x^3$ is above (since $-0.125 > -0.5$)
- On $[0,1]$, test with $x=0.5$: $f(0.5)=0.125$, $g(0.5)=0.5$, $y=x$ is above

$$
\begin{aligned}
A &= \int_{-1}^{0} (x^3 - x) \, dx + \int_{0}^{1} (x - x^3) \, dx \\[4pt]
&= \left[ \frac{x^4}{4} - \frac{x^2}{2} \right]_{-1}^{0} + \left[ \frac{x^2}{2} - \frac{x^4}{4} \right]_{0}^{1} \\[4pt]
&= \left(0 - \left(\frac{1}{4} - \frac{1}{2}\right)\right) + \left(\left(\frac{1}{2} - \frac{1}{4}\right) - 0\right) \\[4pt]
&= \frac{1}{4} + \frac{1}{4} = \frac{1}{2}
\end{aligned}
$$

---

### 7.4.4 Sum of Multiple Areas (Syllabus Focus)

The syllabus explicitly requires "a sum of two areas." The key step in such problems is **correctly splitting the interval**.

---

**Example 1** (Cubic function with $x$-axis — three segments): Find the total area bounded by the curve $y = x^3 - x^2 - 2x$ and the $x$-axis.

**Solution**:

Factorise: $x^3 - x^2 - 2x = x(x^2 - x - 2) = x(x-2)(x+1)$, zeros at $x = -1, 0, 2$.

- On $[-1,0]$, $f(-0.5) = 0.625 > 0$
- On $[0,2]$, $f(1) = -2 < 0$

$$
\begin{aligned}
A &= \int_{-1}^{0} (x^3 - x^2 - 2x) \, dx + \int_{0}^{2} -(x^3 - x^2 - 2x) \, dx \\[4pt]
&= \left[ \frac{x^4}{4} - \frac{x^3}{3} - x^2 \right]_{-1}^{0} + \left[ -\frac{x^4}{4} + \frac{x^3}{3} + x^2 \right]_{0}^{2}
\end{aligned}
$$

First part: $(0) - \left( \frac{1}{4} + \frac{1}{3} - 1 \right) = -\left( -\frac{5}{12} \right) = \frac{5}{12}$

Second part: $\left( -\frac{16}{4} + \frac{8}{3} + 4 \right) - 0 = \left( -4 + 4 \right) + \frac{8}{3} = \frac{8}{3}$

Total area: $A = \dfrac{5}{12} + \dfrac{8}{3} = \dfrac{5}{12} + \dfrac{32}{12} = \dfrac{37}{12}$

---

**Example 2** (Quadratic function — three segments): Find the total area bounded by the curve $y = x^2 - 4x + 3$ and the $x$-axis on $[0,4]$.

**Solution**:

Zeros: $x^2 - 4x + 3 = (x-1)(x-3) = 0$, giving $x=1, 3$.

The interval $[0,4]$ is split into $[0,1]$, $[1,3]$, $[3,4]$.

- $[0,1]$: $f(0.5) = 1.25 > 0$
- $[1,3]$: $f(2) = -1 < 0$
- $[3,4]$: $f(3.5) = 1.25 > 0$

$$
\begin{aligned}
A &= \int_0^1 (x^2 - 4x + 3) dx + \int_1^3 -(x^2 - 4x + 3) dx + \int_3^4 (x^2 - 4x + 3) dx \\[4pt]
&= \left[ \frac{x^3}{3} - 2x^2 + 3x \right]_0^1 + \left[ -\frac{x^3}{3} + 2x^2 - 3x \right]_1^3 + \left[ \frac{x^3}{3} - 2x^2 + 3x \right]_3^4 \\[4pt]
&= \frac{4}{3} + \frac{4}{3} + \frac{4}{3} = 4
\end{aligned}
$$

---

### 7.4.5 Summary of Strategies for Plane Area Problems

| Scenario | Identifying Feature | Method |
|------|---------|------|
| Curve above $x$-axis | $f(x) \geq 0$ | $A = \int_a^b f(x) \, dx$ |
| Curve below $x$-axis | $f(x) \leq 0$ | $A = -\int_a^b f(x) \, dx$ |
| Curve crosses $x$-axis | $f(x)$ changes sign | Split at zeros, take absolute values separately |
| Line and curve | Two functions given | $A = \int_a^b [f(x)-g(x)] \, dx$ (upper minus lower) |
| Two curves, multiple intersections | Multiple intersection points | Piecewise handling, upper minus lower on each segment |
| Sum of multiple areas | Three or more subintervals | Integrate each separately, then add |

---

### 7.5 Application of Definite Integrals to Kinematics

> **Syllabus reference 14.14**: Use differentiation and integration to solve kinematics problems (displacement, velocity, acceleration).

In Chapter 5, we learned to use **differentiation** to find velocity and acceleration from displacement. **Integration** provides the reverse path: given acceleration, find velocity; given velocity, find displacement.

**Core relationships** (to be discussed in detail in Chapter 10):

$$
a(t) = \frac{dv}{dt}, \quad v(t) = \frac{ds}{dt}
$$

Reverse:

$$
v(t) = \int a(t) \, dt, \quad s(t) = \int v(t) \, dt
$$

---

**Example 1** (Given acceleration, find velocity and displacement): A particle moves along a straight line with acceleration $a(t) = 12t^2 - 6$. At $t=0$, the velocity is $v=2$ and the displacement is $s=1$. Find $v(t)$ and $s(t)$.

**Solution**:

$$
v(t) = \int (12t^2 - 6) \, dt = 4t^3 - 6t + C
$$

From $v(0) = 2$, we get $C = 2$, so $v(t) = 4t^3 - 6t + 2$.

$$
s(t) = \int (4t^3 - 6t + 2) \, dt = t^4 - 3t^2 + 2t + D
$$

From $s(0) = 1$, we get $D = 1$, so $s(t) = t^4 - 3t^2 + 2t + 1$.

---

**Example 2** (Finding displacement from $v(t)$): A particle's velocity is $v(t) = t^2 - 5t + 6$. Find the net displacement from $t=1$ to $t=4$.

**Solution**:

Net displacement $= \displaystyle \int_1^4 (t^2 - 5t + 6) \, dt = \left[ \frac{t^3}{3} - \frac{5t^2}{2} + 6t \right]_1^4$

$$
= \left( \frac{64}{3} - \frac{80}{2} + 24 \right) - \left( \frac{1}{3} - \frac{5}{2} + 6 \right) = \left( \frac{64}{3} - 40 + 24 \right) - \left( \frac{1}{3} + \frac{1}{2} \right)
$$

$$
= \left( \frac{64}{3} - 16 \right) - \frac{5}{6} = \frac{16}{3} - \frac{5}{6} = \frac{32}{6} - \frac{5}{6} = \frac{27}{6} = \frac{9}{2}
$$

The net displacement is $\dfrac{9}{2}$ units in the positive direction.

---

(More content on kinematics will be discussed in depth in Chapter 10.)

---

## Chapter Core Formula Quick Reference Table

| Integrand | Indefinite Integral | Conditions/Notes |
|---------|---------|---------|
| $x^n$ | $\displaystyle \frac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\dfrac{1}{x}$ | $\displaystyle \ln|x| + C$ | Memorise separately; power rule fails |
| $e^{ax+b}$ | $\displaystyle \frac{1}{a}e^{ax+b} + C$ | $a \neq 0$ |
| $\sin(ax+b)$ | $\displaystyle -\frac{1}{a}\cos(ax+b) + C$ | $a \neq 0$ |
| $\cos(ax+b)$ | $\displaystyle \frac{1}{a}\sin(ax+b) + C$ | $a \neq 0$ |
| $\sec^2(ax+b)$ | $\displaystyle \frac{1}{a}\tan(ax+b) + C$ | $a \neq 0$ |
| $(ax+b)^n$ | $\displaystyle \frac{(ax+b)^{n+1}}{a(n+1)} + C$ | $n \neq -1$ |
| $\dfrac{1}{ax+b}$ | $\displaystyle \frac{1}{a}\ln|ax+b| + C$ | $a \neq 0$ |
| Definite integral $\int_a^b f(x) \, dx$ | $F(b) - F(a)$ | $F'(x) = f(x)$, no $C$ |
| Plane area (upper $-$ lower) | $\displaystyle \int_a^b [f(x)-g(x)] \, dx$ | First confirm $f(x) \geq g(x)$ |
| Area for sign-changing curve with $x$-axis | Split at zeros, take absolute values | First find zeros |

---

## Practice Problems

The following practice problems are graded by difficulty, covering all knowledge points in this chapter. **Answers are at the end.**

---

### Group A: Basic Indefinite Integrals

1. $\displaystyle \int x^9 \, dx$
2. $\displaystyle \int \frac{1}{x^5} \, dx$
3. $\displaystyle \int \sqrt[5]{x} \, dx$
4. $\displaystyle \int \frac{1}{\sqrt[3]{x}} \, dx$
5. $\displaystyle \int (4x^3 - 3x^2 + 2x - 1) \, dx$
6. $\displaystyle \int \frac{6}{x} \, dx$
7. $\displaystyle \int e^{7x} \, dx$
8. $\displaystyle \int e^{-\frac{x}{3}} \, dx$
9. $\displaystyle \int \sin(4x) \, dx$
10. $\displaystyle \int \cos\left(\frac{x}{3}\right) dx$
11. $\displaystyle \int \sec^2(6x) \, dx$
12. $\displaystyle \int (5x-2)^3 \, dx$

---

### Group B: Advanced Indefinite Integrals

13. $\displaystyle \int \left( 2x^6 - 5x^{-4} + \frac{3}{x^2} \right) dx$
14. $\displaystyle \int \left( \frac{1}{3x} + e^{4x} \right) dx$
15. $\displaystyle \int \left( \sin\frac{x}{2} + \cos 2x \right) dx$
16. $\displaystyle \int \frac{1}{(2x+3)^3} \, dx$
17. $\displaystyle \int \left( 2e^{3x-1} - 5\sin\left(2x+\frac{\pi}{4}\right) + 3\sec^2(1-2x) \right) dx$
18. $\displaystyle \int \frac{x^4 + 2x^2 - 3}{x^2} \, dx$
19. $\displaystyle \int (e^x - 1)^2 \, dx$
20. $\displaystyle \int \frac{5}{\sqrt{3x+2}} \, dx$
21. $\displaystyle \int \left( \frac{3}{2x-1} + \frac{1}{(x+2)^4} \right) dx$
22. $\displaystyle \int \frac{2x^2+3x+1}{x} \, dx$

---

### Group C: Definite Integrals

23. $\displaystyle \int_0^4 3x \, dx$
24. $\displaystyle \int_1^3 (2x-1) \, dx$
25. $\displaystyle \int_{-1}^2 (x^2 + 2) \, dx$
26. $\displaystyle \int_0^{\pi/2} \cos x \, dx$
27. $\displaystyle \int_0^2 e^{3x} \, dx$
28. $\displaystyle \int_1^4 \frac{3}{\sqrt{x}} \, dx$
29. $\displaystyle \int_0^{\pi/3} \sec^2 x \, dx$
30. $\displaystyle \int_{-1}^1 (x^5 - x^3) \, dx$ (use symmetry)
31. $\displaystyle \int_0^1 (4x-1)^3 \, dx$
32. $\displaystyle \int_0^{\pi/4} \sin\left(2x+\frac{\pi}{4}\right) dx$
33. $\displaystyle \int_2^5 \frac{2}{x-1} \, dx$
34. $\displaystyle \int_0^1 (e^{2x} + e^{-x}) \, dx$

---

### Group D: Plane Area

35. Find the area bounded by the curve $y = x^2 + 2$ and the $x$-axis from $x=0$ to $x=2$.
36. Find the area bounded by the curve $y = 4 - x^2$ and the $x$-axis.
37. Find the total area bounded by the curve $y = x^2 - 2x - 3$ and the $x$-axis.
38. Find the total area bounded by the curve $y = x^2 - 2x$ and the $x$-axis on $[-1, 3]$.
39. Find the area bounded by the line $y = 2x + 3$ and the curve $y = x^2$.
40. Find the area bounded by the curve $y = x^2 - 4x + 5$ and the line $y = x + 1$.
41. Find the area bounded by the curves $y = x^2$ and $y = 2x - x^2$.
42. Find the total area bounded by $y = x^3 - 4x$ and the $x$-axis.
43. Find the area bounded by $y = 4x - x^2$ and the line $y = x$.
44. Find the area bounded by $y = x^2$ and the line $y = 4$.

---

## Answers to Practice Problems

### Group A Answers

1. $\displaystyle \frac{x^{10}}{10} + C$
2. $\displaystyle -\frac{1}{4x^4} + C$
   **Detailed**: $\int x^{-5} dx = \dfrac{x^{-4}}{-4} = -\dfrac{1}{4x^4}$
3. $\displaystyle \frac{5}{6}x^{6/5} + C$
   **Detailed**: $\sqrt[5]{x} = x^{1/5}$, $\int x^{1/5} dx = \dfrac{x^{6/5}}{6/5} = \dfrac{5}{6}x^{6/5}$
4. $\displaystyle \frac{3}{2}x^{2/3} + C$
   **Detailed**: $\dfrac{1}{\sqrt[3]{x}} = x^{-1/3}$, $\int x^{-1/3} dx = \dfrac{x^{2/3}}{2/3} = \dfrac{3}{2}x^{2/3}$
5. $\displaystyle x^4 - x^3 + x^2 - x + C$
6. $6\ln|x| + C$
7. $\displaystyle \frac{1}{7}e^{7x} + C$
8. $\displaystyle -3e^{-\frac{x}{3}} + C$
   **Detailed**: $\int e^{-\frac{x}{3}} dx = \dfrac{1}{-1/3} e^{-\frac{x}{3}} = -3e^{-\frac{x}{3}}$
9. $\displaystyle -\frac{1}{4}\cos(4x) + C$
10. $\displaystyle 3\sin\left(\frac{x}{3}\right) + C$
    **Detailed**: $\int \cos\left(\frac{x}{3}\right) dx = \dfrac{1}{1/3}\sin\left(\frac{x}{3}\right) = 3\sin\left(\frac{x}{3}\right)$
11. $\displaystyle \frac{1}{6}\tan(6x) + C$
12. $\displaystyle \frac{(5x-2)^4}{20} + C$
    **Detailed**: $\int (5x-2)^3 dx = \dfrac{(5x-2)^4}{5 \cdot 4} = \dfrac{(5x-2)^4}{20}$

---

### Group B Answers

13. $\displaystyle \frac{2}{7}x^7 + \frac{5}{3x^3} - \frac{3}{x} + C$
    **Detailed**: $\int 2x^6 dx = \frac{2}{7}x^7$, $\int -5x^{-4} dx = -5 \cdot \frac{x^{-3}}{-3} = \frac{5}{3}x^{-3} = \frac{5}{3x^3}$, $\int 3x^{-2} dx = 3 \cdot \frac{x^{-1}}{-1} = -\frac{3}{x}$
14. $\displaystyle \frac{1}{3}\ln|x| + \frac{1}{4}e^{4x} + C$
15. $\displaystyle -2\cos\frac{x}{2} + \frac{1}{2}\sin 2x + C$
    **Detailed**: $\int \sin\frac{x}{2} dx = -\dfrac{1}{1/2}\cos\frac{x}{2} = -2\cos\frac{x}{2}$, $\int \cos 2x dx = \frac{1}{2}\sin 2x$
16. $\displaystyle -\frac{1}{4(2x+3)^2} + C$
    **Detailed**: $\int (2x+3)^{-3} dx = \dfrac{(2x+3)^{-2}}{2 \cdot (-2)} = -\dfrac{1}{4}(2x+3)^{-2} = -\dfrac{1}{4(2x+3)^2}$
17. $\displaystyle \frac{2}{3}e^{3x-1} + \frac{5}{2}\cos\left(2x+\frac{\pi}{4}\right) - \frac{3}{2}\tan(1-2x) + C$
    **Detailed**: $\int 2e^{3x-1} dx = 2 \cdot \frac{1}{3}e^{3x-1} = \frac{2}{3}e^{3x-1}$
    $\int -5\sin(2x+\frac{\pi}{4}) dx = -5 \cdot (-\frac{1}{2})\cos(2x+\frac{\pi}{4}) = \frac{5}{2}\cos(2x+\frac{\pi}{4})$
    $\int 3\sec^2(1-2x) dx = 3 \cdot \frac{1}{-2}\tan(1-2x) = -\frac{3}{2}\tan(1-2x)$
18. $\displaystyle \frac{x^3}{3} + 2x + \frac{3}{x} + C$
    **Detailed**: $\dfrac{x^4+2x^2-3}{x^2} = x^2 + 2 - 3x^{-2}$, integrating gives $\frac{x^3}{3} + 2x + \frac{3}{x} + C$
19. $\displaystyle \frac{1}{2}e^{2x} - 2e^x + x + C$
    **Detailed**: $(e^x-1)^2 = e^{2x} - 2e^x + 1$, $\int e^{2x} dx = \frac{1}{2}e^{2x}$, $\int -2e^x dx = -2e^x$, $\int 1 dx = x$
20. $\displaystyle \frac{10}{3}\sqrt{3x+2} + C$
    **Detailed**: $\int 5(3x+2)^{-1/2} dx = 5 \cdot \dfrac{(3x+2)^{1/2}}{3 \cdot (1/2)} = 5 \cdot \dfrac{2}{3}\sqrt{3x+2} = \frac{10}{3}\sqrt{3x+2}$
21. $\displaystyle \frac{3}{2}\ln|2x-1| - \frac{1}{3(x+2)^3} + C$
    **Detailed**: $\int \frac{3}{2x-1} dx = 3 \cdot \frac{1}{2}\ln|2x-1| = \frac{3}{2}\ln|2x-1|$
    $\int (x+2)^{-4} dx = \dfrac{(x+2)^{-3}}{-3} = -\dfrac{1}{3(x+2)^3}$
22. $\displaystyle x^2 + 3x + \ln|x| + C$
    **Detailed**: $\dfrac{2x^2+3x+1}{x} = 2x + 3 + \frac{1}{x}$, integrating gives $x^2 + 3x + \ln|x| + C$

---

### Group C Answers

23. $24$
    **Detailed**: $\int_0^4 3x \, dx = \left[\frac{3x^2}{2}\right]_0^4 = \frac{48}{2} = 24$
24. $6$
    **Detailed**: $\int_1^3 (2x-1) dx = [x^2 - x]_1^3 = (9-3) - (1-1) = 6$
25. $9$
    **Detailed**: $\int_{-1}^2 (x^2+2) dx = \left[\frac{x^3}{3}+2x\right]_{-1}^2 = \left(\frac{8}{3}+4\right) - \left(-\frac{1}{3}-2\right) = \frac{20}{3} + \frac{7}{3} = \frac{27}{3} = 9$
26. $1$
    **Detailed**: $\int_0^{\pi/2} \cos x \, dx = [\sin x]_0^{\pi/2} = 1 - 0 = 1$
27. $\displaystyle \frac{1}{3}(e^6 - 1)$
    **Detailed**: $\int_0^2 e^{3x} dx = \left[\frac{1}{3}e^{3x}\right]_0^2 = \frac{1}{3}e^6 - \frac{1}{3}e^0 = \frac{1}{3}(e^6-1)$
28. $6$
    **Detailed**: $\int_1^4 3x^{-1/2} dx = [6\sqrt{x}]_1^4 = 6 \cdot 2 - 6 \cdot 1 = 12 - 6 = 6$
29. $\sqrt{3}$
    **Detailed**: $\int_0^{\pi/3} \sec^2 x \, dx = [\tan x]_0^{\pi/3} = \sqrt{3} - 0 = \sqrt{3}$
30. $0$
    **Detailed**: $x^5 - x^3$ is odd, integral over symmetric interval $[-1,1]$ is zero.
31. $5$
    **Detailed**: $\int_0^1 (4x-1)^3 dx = \left[\frac{(4x-1)^4}{4 \cdot 4}\right]_0^1 = \left[\frac{(4x-1)^4}{16}\right]_0^1 = \frac{3^4}{16} - \frac{(-1)^4}{16} = \frac{81}{16} - \frac{1}{16} = \frac{80}{16} = 5$
32. $\displaystyle \frac{\sqrt{2}}{2}$
    **Detailed**: $\int_0^{\pi/4} \sin(2x+\frac{\pi}{4}) dx = \left[-\frac{1}{2}\cos(2x+\frac{\pi}{4})\right]_0^{\pi/4}$
    $= -\frac{1}{2}\left[\cos(\frac{\pi}{2}+\frac{\pi}{4}) - \cos\frac{\pi}{4}\right] = -\frac{1}{2}\left[-\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\right] = -\frac{1}{2}(-\sqrt{2}) = \frac{\sqrt{2}}{2}$
33. $2\ln 4 = 4\ln 2$
    **Detailed**: $\int_2^5 \frac{2}{x-1} dx = [2\ln|x-1|]_2^5 = 2\ln 4 - 2\ln 1 = 2\ln 4 = 4\ln 2$
34. $\displaystyle \frac{1}{2}(e^2 + 1) - \frac{1}{e}$
    **Detailed**: $\int_0^1 (e^{2x} + e^{-x}) dx = \left[\frac{1}{2}e^{2x} - e^{-x}\right]_0^1 = \left(\frac{1}{2}e^2 - e^{-1}\right) - \left(\frac{1}{2} - 1\right) = \frac{1}{2}e^2 - \frac{1}{e} + \frac{1}{2} = \frac{1}{2}(e^2+1) - \frac{1}{e}$

---

### Group D Answers

35. $\displaystyle \frac{20}{3}$
    **Detailed**: $A = \int_0^2 (x^2+2) dx = \left[\frac{x^3}{3}+2x\right]_0^2 = \frac{8}{3} + 4 = \frac{20}{3}$
36. $\displaystyle \frac{32}{3}$
    **Detailed**: Intersects $x$-axis at $x=\pm2$. $A = \int_{-2}^2 (4-x^2) dx = \left[4x-\frac{x^3}{3}\right]_{-2}^2 = (8-\frac{8}{3}) - (-8+\frac{8}{3}) = \frac{16}{3} + \frac{16}{3} = \frac{32}{3}$
37. $\displaystyle \frac{32}{3}$
    **Detailed**: $x^2-2x-3 = (x-3)(x+1)=0$, zeros $x=-1,3$. On $[-1,3]$, $f(x)\leq0$.
    $A = -\int_{-1}^3 (x^2-2x-3) dx = \int_{-1}^3 (-x^2+2x+3) dx = \left[-\frac{x^3}{3}+x^2+3x\right]_{-1}^3$
    $= (-9+9+9) - (\frac{1}{3}+1-3) = 9 - (-\frac{5}{3}) = \frac{32}{3}$
38. $\displaystyle 4$
    **Detailed**: $x^2-2x = x(x-2)=0$, zeros $x=0,2$.
    On $[-1,0]$ $f(x)\geq0$, on $[0,2]$ $f(x)\leq0$, on $[2,3]$ $f(x)\geq0$.
    $A = \int_{-1}^0 (x^2-2x) dx + \int_0^2 -(x^2-2x) dx + \int_2^3 (x^2-2x) dx$
    $= \left[\frac{x^3}{3}-x^2\right]_{-1}^0 + \left[-\frac{x^3}{3}+x^2\right]_0^2 + \left[\frac{x^3}{3}-x^2\right]_2^3$
    $= \frac{4}{3} + \frac{4}{3} + \frac{4}{3} = 4$
39. $\displaystyle \frac{32}{3}$
    **Detailed**: Intersection: $x^2 = 2x+3 \Rightarrow x^2-2x-3=0 \Rightarrow (x-3)(x+1)=0$, $x=-1,3$.
    On $[-1,3]$, $y=2x+3$ is above.
    $A = \int_{-1}^3 [(2x+3)-x^2] dx = \left[x^2+3x-\frac{x^3}{3}\right]_{-1}^3$
    $= (9+9-9) - (1-3+\frac{1}{3}) = 9 - (-\frac{5}{3}) = \frac{32}{3}$
40. $\displaystyle \frac{9}{2}$
    **Detailed**: Intersection: $x^2-4x+5 = x+1 \Rightarrow x^2-5x+4=0 \Rightarrow (x-1)(x-4)=0$, $x=1,4$.
    On $[1,4]$, $y=x+1$ is above (test $x=2$: $f(2)=1$, $g(2)=3$).
    $A = \int_1^4 [(x+1)-(x^2-4x+5)] dx = \int_1^4 (-x^2+5x-4) dx$
    $= \left[-\frac{x^3}{3}+\frac{5x^2}{2}-4x\right]_1^4$
    $= \left(-\frac{64}{3}+40-16\right) - \left(-\frac{1}{3}+\frac{5}{2}-4\right)$
    $= \frac{8}{3} - \left(-\frac{11}{6}\right) = \frac{8}{3} + \frac{11}{6} = \frac{27}{6} = \frac{9}{2}$
41. $\displaystyle \frac{1}{3}$
    **Detailed**: Intersection: $x^2 = 2x-x^2 \Rightarrow 2x^2-2x=0 \Rightarrow 2x(x-1)=0$, $x=0,1$.
    On $[0,1]$, $y=2x-x^2$ is above (test $x=0.5$: $0.25$ vs $0.75$).
    $A = \int_0^1 [(2x-x^2)-x^2] dx = \int_0^1 (2x-2x^2) dx = \left[x^2-\frac{2x^3}{3}\right]_0^1 = 1 - \frac{2}{3} = \frac{1}{3}$
42. $\displaystyle 8$
    **Detailed**: $x^3-4x = x(x-2)(x+2)=0$, zeros $x=-2,0,2$.
    On $[-2,0]$ $f(x)\geq0$, on $[0,2]$ $f(x)\leq0$.
    $A = \int_{-2}^0 (x^3-4x)dx + \int_0^2 -(x^3-4x)dx$
    $= \left[\frac{x^4}{4}-2x^2\right]_{-2}^0 + \left[-\frac{x^4}{4}+2x^2\right]_0^2$
    $= (0-(4-8)) + ((-4+8)-0) = 4 + 4 = 8$
43. $\displaystyle \frac{9}{2}$
    **Detailed**: Intersection: $4x-x^2 = x \Rightarrow 3x-x^2=0 \Rightarrow x(3-x)=0$, $x=0,3$.
    On $[0,3]$, $y=4x-x^2$ is above.
    $A = \int_0^3 [(4x-x^2)-x] dx = \int_0^3 (3x-x^2) dx = \left[\frac{3x^2}{2}-\frac{x^3}{3}\right]_0^3 = \frac{27}{2} - 9 = \frac{9}{2}$
44. $\displaystyle \frac{32}{3}$
    **Detailed**: Intersection: $x^2 = 4 \Rightarrow x = \pm 2$.
    On $[-2,2]$, $y=4$ is above.
    $A = \int_{-2}^2 (4 - x^2) dx = \left[4x - \frac{x^3}{3}\right]_{-2}^2 = (8-\frac{8}{3}) - (-8+\frac{8}{3}) = \frac{16}{3} + \frac{16}{3} = \frac{32}{3}$

---

## Appendix: Common Mistakes and Pitfall Guide

| # | Type of Mistake | ❌ Incorrect | ✅ Correct | Reason |
|---|---------|-----------|-----------|------|
| 1 | Forgetting $+C$ | $\int 2x \, dx = x^2$ | $\int 2x \, dx = x^2 + C$ | Indefinite integral is a family of functions, not a single function |
| 2 | Misapplying power rule to $1/x$ | $\int x^{-1} dx = \frac{x^0}{0}$ | $\int \frac{1}{x} dx = \ln\|x\| + C$ | When $n=-1$, denominator is zero, formula fails |
| 3 | Omitting $1/a$ in $(ax+b)^n$ | $\int (2x+1)^3 = \frac{(2x+1)^4}{4}$ | $\int (2x+1)^3 = \frac{(2x+1)^4}{8}$ | Reverse chain rule produces factor $1/a$ |
| 4 | Wrong sign for $\sin$ integral | $\int \sin(2x) = \frac{1}{2}\cos(2x)$ | $\int \sin(2x) = -\frac{1}{2}\cos(2x)$ | Antiderivative of $\sin$ is $-\cos$, not $\cos$ |
| 5 | Adding $C$ in definite integrals | $\int_1^2 2x = [x^2+C]_1^2$ | $\int_1^2 2x = [x^2]_1^2 = 4-1=3$ | $C$ cancels out in subtraction, no need to write |
| 6 | Not splitting area for sign changes | Directly compute $\int_{-2}^2 (x^2-1) dx$ | Split at $x=\pm1$ and take absolute values | Definite integral gives signed area, not actual area |
| 7 | Wrong identification of upper/lower function | Assume $f$ is above | Use a test point to confirm | Area must be positive; upper minus lower must not be reversed |
| 8 | Integrating a product separately | $\int (x+1)(x-1)dx = \int(x+1)dx \cdot \int(x-1)dx$ | Expand first, then integrate | No product rule for integration |
| 9 | Omitting absolute value in $\ln$ | $\int\frac{1}{x}dx = \ln x + C$ | $\int\frac{1}{x}dx = \ln\|x\| + C$ | $\ln x$ is undefined when $x<0$ |
| 10 | Angle mode for trig functions | Calculator in degree mode | Must use radian mode | Integration formulas are derived using radians |

---

### 🔧 Quick Self-Check List

Ask yourself these questions before solving a problem:

- [ ] Did I add the constant of integration $C$? (indefinite integrals)
- [ ] Did I omit $C$ for definite integrals?
- [ ] Did I check for the special case $n=-1$?
- [ ] Did I divide by $a$ for $(ax+b)^n$?
- [ ] Did I add a negative sign for $\sin$ integrals?
- [ ] For area problems, did I check whether the curve is above or below the $x$-axis?
- [ ] For area between two curves, did I confirm which one is above?
- [ ] Do I need to split the interval for piecewise handling?

> **Final advice**: After completing every integration, develop the habit of **verifying by differentiation**. This not only helps you find errors but also deepens your understanding of the core idea that "integration is the reverse operation of differentiation."

---
---

---

