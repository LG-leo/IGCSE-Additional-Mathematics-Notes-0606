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

# Chapter 5: Differentiation (Derivatives)

## Syllabus Mapping

This chapter covers the following entries from **Unit 14: Calculus** of the **Cambridge IGCSE Additional Mathematics (0606) 2028–2030 syllabus**:

| Syllabus Ref | Content | Section |
|---------|------|---------|
| 14.1 | Understand the concept of a derivative (informal understanding of limits; differentiation from first principles is not required) | 5.1 |
| 14.2 | Use notation $f'(x), f''(x), \frac{dy}{dx}, \frac{d^2y}{dx^2}, \delta x, \delta x \to 0$ | 5.1 |
| 14.3 | Know and use derivatives of standard functions: $x^n$ (any rational $n$), $\sin x$, $\cos x$, $\tan x$, $e^x$, $\ln x$ (including constant multiples, sums/differences, composite functions) | 5.3, 5.4 |
| 14.4 | Product rule and quotient rule | 5.2 |
| 14.5 | Find tangents and normals | 5.5 |
| 14.6 | Find stationary points (points of inflexion not required) | 5.6 |
| 14.7 | Connected rates of change, small increments and approximations | 5.7 |
| 14.8 | Practical maxima and minima problems | 5.8 |
| 14.9 | Use first and second derivative tests to distinguish between maxima and minima | 5.6 |

**Core requirements**:
- Angles in trigonometric functions **must always be in radians**.
- Differentiation from first principles is **not required**.
- Points of inflexion are **not required**.
- The second derivative test requires a complete justification of the conclusion.

---

## Introduction

Differentiation is one of the two core operations of calculus. Its task is to quantify **change** — specifically, to quantify the **instantaneous rate of change** of a function at any given point.

Imagine you are driving along a winding road. The reading on your speedometer is the **instantaneous velocity** — it tells you how fast the car is changing at that exact moment. What differentiation does is calculate this kind of "instantaneous speed" for any function. Geometrically, the derivative gives the **slope of the tangent line** to the curve at a given point — that is, how "steep" the curve is at that point.

Why study differentiation? Because almost everything in nature is changing: the motion of objects, the growth of populations, the rise and fall of temperatures, the fluctuations of profit. Differentiation gives us a precise mathematical tool to describe these changes. Once you master differentiation, subsequent topics like integration (finding accumulated quantities), optimisation (finding the best solution), and kinematics analysis will all fall into place.

This chapter starts from the basic concept of the derivative, then covers the product rule and the quotient rule, basic differentiation formulas, the chain rule, and then applies these tools to tangents and normals, determining extreme values, connected rates of change, and practical maxima and minima problems. Each topic is accompanied by numerous worked examples and practice problems to ensure thorough understanding.

---

## 5.1 The Concept of the Derivative and Notation

### 5.1.1 From Average Rate of Change to Instantaneous Rate of Change

Rate of change is a concept we are very familiar with. For example, if a car travels 120 kilometres in 2 hours, its **average speed** is:

$$
\text{Average speed} = \frac{120}{2} = 60 \text{ km/h}
$$

But this average speed hides the details — the car may be fast at some moments and slow at others. If we want to know the speed **at a precise moment**, we need the instantaneous rate of change.

Let $y = f(x)$. Consider a small interval from $x$ to $x + \delta x$ (where $\delta x$ is read as "delta x", representing a small change in $x$). Over this interval, the average rate of change of the function is:

$$
\frac{\text{Change in function value}}{\text{Change in independent variable}} = \frac{f(x + \delta x) - f(x)}{\delta x}
$$

As $\delta x$ approaches $0$, this average rate of change approaches a limiting value — this is the **derivative** of the function at point $x$:

$$
\boxed{f'(x) = \lim_{\delta x \to 0} \frac{f(x + \delta x) - f(x)}{\delta x}}
$$

Here $\lim_{\delta x \to 0}$ means "as $\delta x$ tends to $0$". Whether this limit exists (i.e., whether the derivative exists) depends on whether the function is "smooth" at that point.

### 5.1.2 Geometric Meaning of the Derivative

Geometrically, the derivative $f'(a)$ is the **slope of the tangent line** to the curve $y = f(x)$ at the point $(a, f(a))$.

- If $f'(a) > 0$, the curve is **increasing** at that point (the tangent slopes upward to the right).
- If $f'(a) < 0$, the curve is **decreasing** at that point (the tangent slopes downward to the right).
- If $f'(a) = 0$, the curve is **horizontal** at that point (could be a maximum, a minimum, or a saddle point).

### 5.1.3 Notation

There are several notations for derivatives commonly seen in exams:

| Notation | Name | Example |
|-----|------|------|
| $f'(x)$ | Lagrange notation | $f'(x) = 2x$ |
| $\frac{dy}{dx}$ | Leibniz notation | $\frac{dy}{dx} = 2x$ |
| $\frac{d}{dx}f(x)$ | Operator notation | $\frac{d}{dx}(x^2) = 2x$ |
| $f''(x)$, $\frac{d^2y}{dx^2}$ | Second derivative | Derivative of the derivative |

> ⚠️ **Important understanding**: The notation $\frac{dy}{dx}$ is not a fraction, but a single symbol representing the result of the operation "differentiate with respect to $x$". However, in small increment approximations, we can treat it as a "ratio" ($\delta y \approx \frac{dy}{dx} \cdot \delta x$), which is very effective for linear approximations.

### 5.1.4 Intuitive Understanding of Limits

In the process of differentiation, we often encounter the indeterminate form $\frac{0}{0}$. The usual method is to **factorise and cancel** before substituting.

**Example**: Evaluate $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$.

When $x = 2$, both numerator and denominator are $0$, but we can do this:

$$
\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = 4
$$

Note: $x$ approaches $2$ but never equals $2$, so cancelling $x-2$ is valid.

---

### Worked Example 5.1A (Intuitive Understanding of the Derivative Concept)

> Given $f(x) = x^2$, use the limit definition to find $f'(2)$.

**Solution**:

$$
f'(2) = \lim_{\delta x \to 0} \frac{f(2 + \delta x) - f(2)}{\delta x}
= \lim_{\delta x \to 0} \frac{(2 + \delta x)^2 - 4}{\delta x}
$$

Expanding $(2 + \delta x)^2 = 4 + 4\delta x + (\delta x)^2$ and substituting:

$$
f'(2) = \lim_{\delta x \to 0} \frac{4 + 4\delta x + (\delta x)^2 - 4}{\delta x}
= \lim_{\delta x \to 0} \frac{4\delta x + (\delta x)^2}{\delta x}
= \lim_{\delta x \to 0} (4 + \delta x)
$$

As $\delta x \to 0$, $4 + \delta x \to 4$, so $f'(2) = 4$.

**Geometric meaning**: The slope of the tangent line to the parabola $y = x^2$ at the point $(2, 4)$ is $4$.

---

### Worked Example 5.1B (Comparing Average and Instantaneous Rates of Change)

> An object in free fall has displacement $s(t) = 5t^2$ ($s$ in metres, $t$ in seconds).
> (a) Find the average velocity from $t = 2$ to $t = 2.1$.
> (b) Find the instantaneous velocity at $t = 2$.

**Solution**:

(a) Average velocity:

$$
\text{Average velocity} = \frac{s(2.1) - s(2)}{0.1} = \frac{5(4.41) - 5(4)}{0.1}
= \frac{22.05 - 20}{0.1} = \frac{2.05}{0.1} = 20.5 \text{ m/s}
$$

(b) Instantaneous velocity. First find the derivative in general:

$$
s'(t) = \lim_{\delta t \to 0} \frac{5(t + \delta t)^2 - 5t^2}{\delta t}
= \lim_{\delta t \to 0} \frac{5(t^2 + 2t\delta t + (\delta t)^2) - 5t^2}{\delta t}
$$

$$
= \lim_{\delta t \to 0} \frac{10t\delta t + 5(\delta t)^2}{\delta t}
= \lim_{\delta t \to 0} (10t + 5\delta t) = 10t
$$

Substituting $t = 2$: $s'(2) = 10 \times 2 = 20$ m/s.

Note: The average velocity $20.5$ m/s is very close to the instantaneous velocity $20$ m/s — the smaller the interval, the closer they become.

---

### Worked Example 5.1C (Relationship Between Derivative Value and Tangent Slope)

> What is the slope of the tangent to the curve $y = \frac{1}{x}$ at the point $(2, \frac{1}{2})$? Is the curve rising or falling at that point?

**Solution**:

$$
f'(x) = \lim_{\delta x \to 0} \frac{\frac{1}{x + \delta x} - \frac{1}{x}}{\delta x}
= \lim_{\delta x \to 0} \frac{\frac{x - (x + \delta x)}{x(x + \delta x)}}{\delta x}
= \lim_{\delta x \to 0} \frac{-\delta x}{x(x + \delta x)\delta x}
$$

$$
= \lim_{\delta x \to 0} \frac{-1}{x(x + \delta x)} = -\frac{1}{x^2}
$$

Substituting $x = 2$: $f'(2) = -\frac{1}{4}$.

The slope is negative, so the curve is **falling** at $x = 2$ (as $x$ increases, $y$ decreases).

---

### Worked Example 5.1D (Limit Calculation — Cancellation Method)

> Evaluate $\lim_{x \to 3} \frac{x^2 - 2x - 3}{x - 3}$.

**Solution**:

When $x = 3$, the numerator $3^2 - 2(3) - 3 = 9 - 6 - 3 = 0$, and the denominator is also $0$. Factorise the numerator:

$$
x^2 - 2x - 3 = (x - 3)(x + 1)
$$

Therefore:

$$
\lim_{x \to 3} \frac{x^2 - 2x - 3}{x - 3} = \lim_{x \to 3} \frac{(x - 3)(x + 1)}{x - 3} = \lim_{x \to 3} (x + 1) = 4
$$

---

### Practice Problems 5.1

1. Use the limit definition to find the derivative of $f(x) = x^2 + 2x$ at $x = 1$.
2. An object's displacement is $s(t) = 2t^2 + 3t$ ($t \ge 0$). Find the instantaneous velocity at $t = 3$.
3. Evaluate $\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$.

---

## 5.2 Product Rule and Quotient Rule

When two functions are multiplied or divided, their derivatives cannot be found by simply differentiating each part separately and then multiplying or dividing. Special rules are needed.

### 5.2.1 Product Rule

Let $y = u \cdot v$, where $u$ and $v$ are both functions of $x$. Then:

$$
\boxed{\frac{dy}{dx} = u\frac{dv}{dx} + v\frac{du}{dx}}
$$

Or briefly: $(uv)' = uv' + vu'$

Memory aid: "**first times derivative of second plus second times derivative of first**" — or, more mnemonically: "differentiate the first, leave the second, plus differentiate the second, leave the first."

**Detailed derivation of the Product Rule**:

Starting from the limit definition of the derivative:

$$
(uv)' = \lim_{\delta x \to 0} \frac{u(x+\delta x)v(x+\delta x) - u(x)v(x)}{\delta x}
$$

Cleverly add and subtract $u(x+\delta x)v(x)$ in the numerator:

$$
= \lim_{\delta x \to 0} \frac{u(x+\delta x)v(x+\delta x) - u(x+\delta x)v(x) + u(x+\delta x)v(x) - u(x)v(x)}{\delta x}
$$

$$
= \lim_{\delta x \to 0} \left[ u(x+\delta x) \cdot \frac{v(x+\delta x) - v(x)}{\delta x} + v(x) \cdot \frac{u(x+\delta x) - u(x)}{\delta x} \right]
$$

As $\delta x \to 0$, $u(x+\delta x) \to u(x)$, so:

$$
(uv)' = u(x) \cdot v'(x) + v(x) \cdot u'(x) = uv' + vu'
$$

### 5.2.2 Quotient Rule

Let $y = \frac{u}{v}$, where $u$ and $v$ are both functions of $x$, and $v \neq 0$. Then:

$$
\boxed{\frac{dy}{dx} = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}}
$$

Or briefly: $\left(\frac{u}{v}\right)' = \frac{vu' - uv'}{v^2}$

Memory aid: "**bottom times derivative of top minus top times derivative of bottom, all over bottom squared**" — remember that the derivative of the top comes first, and subtract.

**Derivation of the Quotient Rule** (derived from the Product Rule):

Write $\frac{u}{v}$ as $u \cdot v^{-1}$, then use the Product Rule and Chain Rule:

$$
\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{d}{dx}(u \cdot v^{-1}) = u \cdot \frac{d}{dx}(v^{-1}) + v^{-1} \cdot \frac{du}{dx}
$$

$$
= u \cdot (-1)v^{-2} \cdot \frac{dv}{dx} + \frac{1}{v} \cdot \frac{du}{dx}
= -\frac{u}{v^2}\frac{dv}{dx} + \frac{1}{v}\frac{du}{dx}
$$

Putting over a common denominator:

$$
= \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}
$$

---

### Worked Example 5.2A (Product Rule Basics)

> Find the derivatives of the following functions:
> (a) $y = (x^2 + 1)(x^3 - 2x)$
> (b) $y = x\sin x$
> (c) $y = e^x \cos x$
> (d) $y = x^2\ln x$

**Solution**:

(a) Let $u = x^2 + 1$, $v = x^3 - 2x$.
Then $u' = 2x$, $v' = 3x^2 - 2$.

$$
y' = uv' + vu' = (x^2 + 1)(3x^2 - 2) + (x^3 - 2x)(2x)
$$

Expanding:

$$
= 3x^4 - 2x^2 + 3x^2 - 2 + 2x^4 - 4x^2 = 5x^4 - 3x^2 - 2
$$

(Can also verify by expanding the original expression first and then differentiating.)

(b) Let $u = x$, $v = \sin x$, then $u' = 1$, $v' = \cos x$.

$$
y' = x\cos x + \sin x \cdot 1 = x\cos x + \sin x
$$

(c) Let $u = e^x$, $v = \cos x$, then $u' = e^x$, $v' = -\sin x$.

$$
y' = e^x \cdot (-\sin x) + \cos x \cdot e^x = e^x(\cos x - \sin x)
$$

(d) Let $u = x^2$, $v = \ln x$, then $u' = 2x$, $v' = \frac{1}{x}$.

$$
y' = x^2 \cdot \frac{1}{x} + \ln x \cdot 2x = x + 2x\ln x
$$

---

### Worked Example 5.2B (Quotient Rule Basics)

> Find the derivatives of the following functions:
> (a) $y = \frac{x}{x+1}$
> (b) $y = \frac{x^2}{\sin x}$
> (c) $y = \frac{e^x}{x^2 + 1}$
> (d) $y = \frac{\ln x}{x}$

**Solution**:

(a) Let $u = x$, $v = x+1$, then $u' = 1$, $v' = 1$.

$$
y' = \frac{vu' - uv'}{v^2} = \frac{(x+1)(1) - x(1)}{(x+1)^2} = \frac{x+1-x}{(x+1)^2} = \frac{1}{(x+1)^2}
$$

(b) Let $u = x^2$, $v = \sin x$, then $u' = 2x$, $v' = \cos x$.

$$
y' = \frac{(\sin x)(2x) - (x^2)(\cos x)}{\sin^2 x} = \frac{2x\sin x - x^2\cos x}{\sin^2 x}
$$

(c) Let $u = e^x$, $v = x^2 + 1$, then $u' = e^x$, $v' = 2x$.

$$
y' = \frac{(x^2+1)e^x - e^x(2x)}{(x^2+1)^2} = \frac{e^x(x^2 + 1 - 2x)}{(x^2+1)^2} = \frac{e^x(x-1)^2}{(x^2+1)^2}
$$

(d) Let $u = \ln x$, $v = x$, then $u' = \frac{1}{x}$, $v' = 1$.

$$
y' = \frac{x \cdot \frac{1}{x} - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}
$$

---

### Worked Example 5.2C (Integrated Product and Quotient Rule)

> (a) Given $y = (x^2 + 1)\ln x$, find $\frac{dy}{dx}$.
> (b) Given $y = \frac{\sin x}{e^x}$, find $\frac{dy}{dx}$.
> (c) Given $y = \tan x$, use $\tan x = \frac{\sin x}{\cos x}$ and the quotient rule to verify $\frac{d}{dx}(\tan x) = \sec^2 x$.
> (d) Find the derivative of $y = \frac{2x-1}{x^2+3}$.

**Solution**:

(a) Product Rule. Let $u = x^2 + 1$, $v = \ln x$, then $u' = 2x$, $v' = \frac{1}{x}$.

$$
\frac{dy}{dx} = (x^2+1)\cdot\frac{1}{x} + \ln x \cdot 2x = \frac{x^2+1}{x} + 2x\ln x = x + \frac{1}{x} + 2x\ln x
$$

(b) Quotient Rule. Let $u = \sin x$, $v = e^x$, then $u' = \cos x$, $v' = e^x$.

$$
\frac{dy}{dx} = \frac{e^x\cos x - \sin x \cdot e^x}{(e^x)^2} = \frac{e^x(\cos x - \sin x)}{e^{2x}} = \frac{\cos x - \sin x}{e^x}
$$

(c) Let $u = \sin x$, $v = \cos x$, then $u' = \cos x$, $v' = -\sin x$.

$$
\frac{d}{dx}\left(\frac{\sin x}{\cos x}\right) = \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x}
= \frac{\cos^2 x + \sin^2 x}{\cos^2 x}
$$

By the trigonometric identity $\sin^2 x + \cos^2 x = 1$:

$$
\frac{d}{dx}(\tan x) = \frac{1}{\cos^2 x} = \sec^2 x
$$

Verification complete.

(d) Let $u = 2x-1$, $v = x^2+3$, then $u' = 2$, $v' = 2x$.

$$
y' = \frac{(x^2+3)(2) - (2x-1)(2x)}{(x^2+3)^2}
= \frac{2x^2+6 - 4x^2 + 2x}{(x^2+3)^2}
= \frac{-2x^2 + 2x + 6}{(x^2+3)^2}
= \frac{-2(x^2 - x - 3)}{(x^2+3)^2}
$$

---

### Practice Problems 5.2

1. Find the derivative of $y = x^2 e^x$.
2. Find the derivative of $y = \frac{3x}{x-2}$.
3. Find the derivative of $y = x\cos x$.
4. Find the derivative of $y = \frac{x+1}{x^2+1}$.
5. Find the derivative of $y = e^x \sin x$.

---

## 5.3 Basic Differentiation Formulas

Now that we have the concept of the derivative, we need an efficient set of tools for differentiation, rather than using the limit definition every time. Below are the most basic differentiation formulas, which must be mastered thoroughly.

### 5.3.1 Derivation of the Power Rule

For $f(x) = x^n$, where $n$ is a positive integer, we first derive using the Binomial Theorem.

From the definition of the derivative:

$$
f'(x) = \lim_{\delta x \to 0} \frac{(x + \delta x)^n - x^n}{\delta x}
$$

By the Binomial Theorem:

$$
(x + \delta x)^n = x^n + nx^{n-1}\delta x + \frac{n(n-1)}{2}x^{n-2}(\delta x)^2 + \cdots + (\delta x)^n
$$

Substituting:

$$
f'(x) = \lim_{\delta x \to 0} \frac{nx^{n-1}\delta x + \frac{n(n-1)}{2}x^{n-2}(\delta x)^2 + \cdots + (\delta x)^n}{\delta x}
$$

$$
= \lim_{\delta x \to 0} \left[ nx^{n-1} + \frac{n(n-1)}{2}x^{n-2}\delta x + \cdots + (\delta x)^{n-1} \right]
$$

As $\delta x \to 0$, all terms except the first tend to $0$, so:

$$
\boxed{\frac{d}{dx}(x^n) = n x^{n-1}}
$$

This formula holds not only for positive integers but for **any rational number** $n$, as explicitly required by the syllabus.

The following table shows common cases:

| $f(x)$ | Rewritten as $x^n$ | $f'(x)$ | Explanation |
|--------|-----------------|---------|------|
| $x^2$ | $x^2$ | $2x$ | $n=2$ |
| $x^3$ | $x^3$ | $3x^2$ | $n=3$ |
| $x$ | $x^1$ | $1$ | $n=1$ |
| $1$ | $x^0$ | $0$ | $n=0$ |
| $\sqrt{x}$ | $x^{1/2}$ | $\frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$ | $n = \frac{1}{2}$ |
| $\frac{1}{x}$ | $x^{-1}$ | $-x^{-2} = -\frac{1}{x^2}$ | $n = -1$ |
| $\frac{1}{x^2}$ | $x^{-2}$ | $-2x^{-3} = -\frac{2}{x^3}$ | $n = -2$ |
| $\sqrt[3]{x}$ | $x^{1/3}$ | $\frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$ | $n = \frac{1}{3}$ |

### 5.3.2 Constant Multiple and Sum/Difference Rules

Differentiating linear combinations of functions is very straightforward:

- **Constant multiple rule**: $\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)$
  - Derivation: $\lim_{\delta x \to 0} \frac{c f(x+\delta x) - c f(x)}{\delta x} = c \cdot \lim_{\delta x \to 0} \frac{f(x+\delta x) - f(x)}{\delta x} = c f'(x)$

- **Sum rule**: $\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$
  - Derivation: $\lim_{\delta x \to 0} \frac{[f(x+\delta x)+g(x+\delta x)] - [f(x)+g(x)]}{\delta x} = \lim_{\delta x \to 0} \frac{f(x+\delta x)-f(x)}{\delta x} + \lim_{\delta x \to 0} \frac{g(x+\delta x)-g(x)}{\delta x} = f'(x) + g'(x)$

- **Difference rule**: $\frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)$

**Example**: $f(x) = 3x^2 - 4x + 5$

$$
f'(x) = 3 \cdot (2x) - 4 \cdot (1) + 0 = 6x - 4
$$

### 5.3.3 Derivatives of Trigonometric Functions

**Core condition**: All angles in trigonometric functions **must be in radians**.

Why must we use radians? Because in radians, $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$. This limit is the foundation for differentiating trigonometric functions. If degrees were used, this limit would include an extra factor of $\frac{\pi}{180}$, and the derivative formulas would no longer be simple.

**Derivation of the derivative of $\sin x$**:

$$
\frac{d}{dx}(\sin x) = \lim_{\delta x \to 0} \frac{\sin(x+\delta x) - \sin x}{\delta x}
$$

Using the trigonometric identity $\sin(A+B) = \sin A\cos B + \cos A\sin B$:

$$
= \lim_{\delta x \to 0} \frac{\sin x\cos(\delta x) + \cos x\sin(\delta x) - \sin x}{\delta x}
$$

$$
= \lim_{\delta x \to 0} \left[ \sin x \cdot \frac{\cos(\delta x) - 1}{\delta x} + \cos x \cdot \frac{\sin(\delta x)}{\delta x} \right]
$$

Using the two important limits: $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$ and $\lim_{\theta \to 0} \frac{\cos\theta - 1}{\theta} = 0$, we get:

$$
\frac{d}{dx}(\sin x) = \sin x \cdot 0 + \cos x \cdot 1 = \cos x
$$

Similarly, $\frac{d}{dx}(\cos x) = -\sin x$ can be derived.

For $\tan x$, we use $\tan x = \frac{\sin x}{\cos x}$ and the quotient rule (see Section 5.2).

Summary of standard formulas:

$$
\boxed{\frac{d}{dx}(\sin x) = \cos x}
$$

$$
\boxed{\frac{d}{dx}(\cos x) = -\sin x}
$$

$$
\boxed{\frac{d}{dx}(\tan x) = \sec^2 x}
$$

### 5.3.4 Derivatives of Exponential and Logarithmic Functions

$$
\boxed{\frac{d}{dx}(e^x) = e^x}
$$

This is one of the most beautiful formulas in calculus — the derivative of $e^x$ is itself. Geometrically, this means that at any point on the curve $y = e^x$, the slope of the tangent is equal to the function value at that point.

For a general exponential function $a^x$ ($a > 0, a \neq 1$):

$$
\frac{d}{dx}(a^x) = a^x \ln a
$$

**Concise derivation**: Write $a^x$ as $e^{\ln(a^x)} = e^{x\ln a}$, then use the chain rule:

$$
\frac{d}{dx}(a^x) = \frac{d}{dx}(e^{x\ln a}) = e^{x\ln a} \cdot \ln a = a^x \ln a
$$

**Detailed step-by-step derivation**:

### Step 1: Rewrite the base using an identity
Any positive number $a$ can be written as an exponential of $e$ using the natural logarithm:
$$
a = e^{\ln a}
$$

### Step 2: Substitute into the original function
Raise both sides to the power of $x$:
$$
a^x = (e^{\ln a})^x
$$

### Step 3: Simplify the exponent (power rule)
Using $(e^{m})^n = e^{m \cdot n}$, multiply the exponents:
$$
(e^{\ln a})^x = e^{x \cdot \ln a}
$$
Now the original function becomes:
$$
y = e^{x \ln a}
$$

### Step 4: Set up the intermediate variable (prepare for the chain rule)
Let:
$$
u = x \cdot \ln a
$$
Note: since $a$ is a constant, $\ln a$ is also a constant.

Then the original function becomes:
$$
y = e^{u}
$$

### Step 5: Differentiate separately

**(1) Differentiate $u$ with respect to $x$** ($\ln a$ is a constant coefficient):
$$
\frac{du}{dx} = \ln a
$$

**(2) Differentiate $y$ with respect to $u$** (the derivative of the exponential function is itself):
$$
\frac{dy}{du} = e^{u}
$$

### Step 6: Apply the chain rule
The chain rule states:
$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$
Substituting the results from Step 5:
$$
\frac{dy}{dx} = e^{u} \cdot (\ln a)
$$

### Step 7: Substitute back and simplify
Replace $u$ with $x \ln a$:
$$
\frac{dy}{dx} = e^{x \ln a} \cdot \ln a
$$
From Step 3 we know $e^{x \ln a} = a^x$, so this simplifies to:
$$
\boxed{\frac{d}{dx}(a^x) = a^x \ln a}
$$

---

For the natural logarithm:

$$
\boxed{\frac{d}{dx}(\ln x) = \frac{1}{x}}
$$

For a logarithm with a general base:

$$
\frac{d}{dx}(\log_a x) = \frac{1}{x \ln a}
$$

**Derivation of the derivative of $\ln x$**:

Let $y = \ln x$, then $e^y = x$. Differentiate both sides with respect to $x$ (implicit differentiation):

$$
e^y \cdot \frac{dy}{dx} = 1 \quad \Rightarrow \quad \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}
$$

---

### Worked Example 5.3A (Differentiating Polynomials)

> Find the derivatives of the following functions:
> (a) $f(x) = 2x^5 - 3x^3 + 7x - 10$
> (b) $g(x) = \frac{1}{3}x^6 + \frac{4}{x^2} - \sqrt{x}$
> (c) $h(x) = (x+1)(x-2)$ (expand first, then differentiate)
> (d) $p(x) = 5x^4 + 2x^{-3} - 3x^{1/2} + 8$

**Solution**:

(a) Differentiate term by term:

$$
f'(x) = 2 \cdot 5x^4 - 3 \cdot 3x^2 + 7 - 0 = 10x^4 - 9x^2 + 7
$$

(b) First rewrite in power form: $\frac{4}{x^2} = 4x^{-2}$, $\sqrt{x} = x^{1/2}$.

$$
g(x) = \frac{1}{3}x^6 + 4x^{-2} - x^{1/2}
$$

$$
g'(x) = \frac{1}{3} \cdot 6x^5 + 4 \cdot (-2)x^{-3} - \frac{1}{2}x^{-1/2}
= 2x^5 - 8x^{-3} - \frac{1}{2}x^{-1/2}
$$

Writing in fraction form:

$$
g'(x) = 2x^5 - \frac{8}{x^3} - \frac{1}{2\sqrt{x}}
$$

(c) First expand: $(x+1)(x-2) = x^2 - x - 2$, then differentiate:

$$
h'(x) = 2x - 1
$$

(d)

$$
p'(x) = 5 \cdot 4x^3 + 2 \cdot (-3)x^{-4} - 3 \cdot \frac{1}{2}x^{-1/2} + 0
= 20x^3 - 6x^{-4} - \frac{3}{2}x^{-1/2}
$$

---

### Worked Example 5.3B (Differentiating Trigonometric Functions)

> Find the derivatives of the following functions:
> (a) $f(x) = 3\sin x - 2\cos x$
> (b) $g(x) = \tan x + 5$
> (c) Find $f'(0)$, where $f(x) = \sin x - \cos x$
> (d) $h(x) = 4\sin x + \frac{1}{2}\cos x$

**Solution**:

(a)

$$
f'(x) = 3\cos x - 2(-\sin x) = 3\cos x + 2\sin x
$$

(b)

$$
g'(x) = \sec^2 x + 0 = \sec^2 x
$$

(c) First differentiate: $f'(x) = \cos x + \sin x$

Substituting $x = 0$: $f'(0) = \cos 0 + \sin 0 = 1 + 0 = 1$

(d)

$$
h'(x) = 4\cos x + \frac{1}{2}(-\sin x) = 4\cos x - \frac{1}{2}\sin x
$$

---

### Worked Example 5.3C (Differentiating Exponential and Logarithmic Functions)

> Find the derivatives of the following functions:
> (a) $f(x) = 4e^x - \frac{1}{2}\ln x$
> (b) $g(x) = 3^x + \log_2 x$
> (c) Given $h(x) = e^x + \ln x$, find $h'(1)$
> (d) $p(x) = 5^x - 2e^x + 3\ln x$

**Solution**:

(a)

$$
f'(x) = 4e^x - \frac{1}{2} \cdot \frac{1}{x} = 4e^x - \frac{1}{2x}
$$

(b) Use formulas: $\frac{d}{dx}(3^x) = 3^x \ln 3$, $\frac{d}{dx}(\log_2 x) = \frac{1}{x\ln 2}$

$$
g'(x) = 3^x \ln 3 + \frac{1}{x\ln 2}
$$

(c) First differentiate: $h'(x) = e^x + \frac{1}{x}$

Substituting $x = 1$: $h'(1) = e^1 + \frac{1}{1} = e + 1$

(d)

$$
p'(x) = 5^x \ln 5 - 2e^x + 3 \cdot \frac{1}{x} = 5^x \ln 5 - 2e^x + \frac{3}{x}
$$

---

### Worked Example 5.3D (Comprehensive Differentiation — Rewriting First)

> Find the derivatives of the following functions:
> (a) $f(x) = \frac{2}{\sqrt[3]{x}}$
> (b) $g(x) = (2x)^3$ (note the difference from $2x^3$)

**Solution**:

(a) First rewrite: $\frac{2}{\sqrt[3]{x}} = 2x^{-1/3}$

$$
f'(x) = 2 \cdot \left(-\frac{1}{3}\right)x^{-4/3} = -\frac{2}{3}x^{-4/3} = -\frac{2}{3\sqrt[3]{x^4}}
$$

(b) $(2x)^3 = 8x^3$, so $g'(x) = 8 \cdot 3x^2 = 24x^2$

Note: If it were $2x^3$, the derivative would be $6x^2$ — they are different.

---

### Practice Problems 5.3

1. Find the derivative of $f(x) = 4x^3 - 2x^2 + 5x - 7$.
2. Find the derivative of $g(x) = \frac{3}{x^2} - \frac{1}{2\sqrt{x}} + 6x^{1/3}$.
3. Find the derivative of $h(x) = 5\sin x - 3\cos x + 2\tan x$.
4. Find the derivative of $p(x) = 2e^x + 4^x - \frac{1}{3}\ln x$.

---

## 5.4 Chain Rule

### 5.4.1 Principle of the Chain Rule

When we want to differentiate a composite function — for example, $y = (2x+1)^3$ or $y = \sin(3x)$ — we need the **chain rule**.

The core idea of the chain rule is "differentiate layer by layer, multiply as you go." Let $y$ be a function of $u$, and $u$ be a function of $x$, i.e., $y = f(u)$ and $u = g(x)$. Then:

$$
\boxed{\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}}
$$

Written another way: if $y = f(g(x))$, then:

$$
\frac{dy}{dx} = f'(g(x)) \cdot g'(x)
$$

That is: **the derivative of the outer function with respect to the intermediate variable, multiplied by the derivative of the intermediate variable with respect to the independent variable**.

### 5.4.2 Intuitive Understanding of the Chain Rule

Why does the chain rule work? Consider small changes:

- When $x$ changes by $\delta x$, $u = g(x)$ changes by $\delta u \approx g'(x)\delta x$
- When $u$ changes by $\delta u$, $y = f(u)$ changes by $\delta y \approx f'(u)\delta u$

Therefore:

$$
\frac{\delta y}{\delta x} \approx \frac{f'(u)\delta u}{\delta x} \approx f'(u) \cdot \frac{\delta u}{\delta x} \approx f'(u) \cdot g'(x)
$$

As $\delta x \to 0$, the approximation becomes an exact equality.

### 5.4.3 Common Application Patterns of the Chain Rule

The following six patterns cover the most common applications of the chain rule in IGCSE Additional Mathematics. Each pattern is accompanied by a complete step-by-step derivation and a typical example.

---

#### Pattern 1: $y = (ax+b)^n$

**Formula**: $\displaystyle \frac{dy}{dx} = a n (ax+b)^{n-1}$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then the original function can be written as $y = u^n$.

- Outer function: $y = u^n$ (power function)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

Compute the derivative of $y$ with respect to $u$ and the derivative of $u$ with respect to $x$:

$$
\frac{dy}{du} = \frac{d}{du}(u^n) = n u^{n-1}
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

The chain rule states $\displaystyle \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$. Substituting the results from Step 2:

$$
\frac{dy}{dx} = (n u^{n-1}) \cdot a = a n u^{n-1}
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = a n (ax+b)^{n-1}}
$$

**📌 Example**: Find the derivative of $y = (3x - 2)^5$.

Using the formula, $a = 3$, $n = 5$, so:

$$
\frac{dy}{dx} = 3 \times 5 \times (3x - 2)^{4} = 15(3x-2)^4
$$

---

#### Pattern 2: $y = \sin(ax+b)$

**Formula**: $\displaystyle \frac{dy}{dx} = a\cos(ax+b)$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then $y = \sin u$.

- Outer function: $y = \sin u$ (sine function)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

$$
\frac{dy}{du} = \frac{d}{du}(\sin u) = \cos u
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (\cos u) \cdot a = a \cos u
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = a\cos(ax+b)}
$$

**📌 Example**: Find the derivative of $y = \sin\left(2x + \frac{\pi}{3}\right)$.

Using the formula, $a = 2$, so:

$$
\frac{dy}{dx} = 2\cos\left(2x + \frac{\pi}{3}\right)
$$

---

#### Pattern 3: $y = \cos(ax+b)$

**Formula**: $\displaystyle \frac{dy}{dx} = -a\sin(ax+b)$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then $y = \cos u$.

- Outer function: $y = \cos u$ (cosine function)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

$$
\frac{dy}{du} = \frac{d}{du}(\cos u) = -\sin u
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (-\sin u) \cdot a = -a \sin u
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = -a\sin(ax+b)}
$$

**📌 Example**: Find the derivative of $y = \cos\left(\frac{x}{2}\right)$.

Using the formula, $a = \frac{1}{2}$, so:

$$
\frac{dy}{dx} = -\frac{1}{2}\sin\left(\frac{x}{2}\right)
$$

---

#### Pattern 4: $y = e^{ax+b}$

**Formula**: $\displaystyle \frac{dy}{dx} = a e^{ax+b}$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then $y = e^u$.

- Outer function: $y = e^u$ (exponential function, base $e$)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

$$
\frac{dy}{du} = \frac{d}{du}(e^u) = e^u
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (e^u) \cdot a = a e^u
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = a e^{ax+b}}
$$

**📌 Example**: Find the derivative of $y = e^{-3x+1}$.

Using the formula, $a = -3$, so:

$$
\frac{dy}{dx} = -3 e^{-3x+1}
$$

---

#### Pattern 5: $y = \ln(ax+b)$

**Formula**: $\displaystyle \frac{dy}{dx} = \frac{a}{ax+b}$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then $y = \ln u$.

- Outer function: $y = \ln u$ (natural logarithm function)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

$$
\frac{dy}{du} = \frac{d}{du}(\ln u) = \frac{1}{u}
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \frac{1}{u} \cdot a = \frac{a}{u}
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = \frac{a}{ax+b}}
$$

**📌 Example**: Find the derivative of $y = \ln(3x^2 + 1)$.

Note: Here the inner function is $3x^2 + 1$, not a simple linear $ax+b$ form. We use the general chain rule:

Let $u = 3x^2 + 1$, then $y = \ln u$.

$$
\frac{dy}{dx} = \frac{1}{u} \cdot \frac{du}{dx} = \frac{1}{3x^2 + 1} \cdot 6x = \frac{6x}{3x^2 + 1}
$$

---

#### Pattern 6: $y = \tan(ax+b)$

**Formula**: $\displaystyle \frac{dy}{dx} = a\sec^2(ax+b)$

**Step-by-step derivation**:

**Step 1: Set up the intermediate variable**

Let $u = ax + b$, then $y = \tan u$.

- Outer function: $y = \tan u$ (tangent function)
- Inner function: $u = ax + b$ (linear function)

**Step 2: Differentiate separately**

The derivative of $\tan u$ is $\displaystyle \frac{d}{du}(\tan u) = \sec^2 u$ (derived using $\tan u = \frac{\sin u}{\cos u}$ and the quotient rule).

$$
\frac{dy}{du} = \frac{d}{du}(\tan u) = \sec^2 u
$$

$$
\frac{du}{dx} = \frac{d}{dx}(ax + b) = a
$$

**Step 3: Apply the chain rule**

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (\sec^2 u) \cdot a = a \sec^2 u
$$

**Step 4: Substitute back the original variable**

Replace $u$ with $ax + b$:

$$
\boxed{\frac{dy}{dx} = a\sec^2(ax+b)}
$$

**📌 Example**: Find the derivative of $y = \tan(5x)$.

Using the formula, $a = 5$, so:

$$
\frac{dy}{dx} = 5\sec^2(5x)
$$

### 5.4.4 Multi-layer Chain Rule

When a function has three or more layers of composition, the chain rule can be applied multiple times in succession. For example, $y = f(g(h(x)))$:

$$
\frac{dy}{dx} = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)
$$

Start from the outermost layer and work inward, multiplying at each step.

---

### Worked Example 5.4A (Polynomial Composite Functions)

> Find the derivatives of the following functions:
> (a) $y = (3x - 2)^5$
> (b) $y = \frac{1}{(2x+1)^3}$
> (c) $y = \sqrt{4x - 1}$
> (d) $y = (5 - 2x)^{-4}$

**Solution**:

(a) Let $u = 3x - 2$, then $y = u^5$.

$$
\frac{dy}{dx} = 5u^4 \cdot 3 = 5(3x-2)^4 \cdot 3 = 15(3x-2)^4
$$

(b) Write as $y = (2x+1)^{-3}$, let $u = 2x+1$.

$$
\frac{dy}{dx} = (-3)u^{-4} \cdot 2 = -6(2x+1)^{-4} = -\frac{6}{(2x+1)^4}
$$

(c) Write as $y = (4x-1)^{1/2}$, let $u = 4x-1$.

$$
\frac{dy}{dx} = \frac{1}{2}u^{-1/2} \cdot 4 = \frac{1}{2}(4x-1)^{-1/2} \cdot 4 = \frac{2}{\sqrt{4x-1}}
$$

(d) Let $u = 5 - 2x$, then $y = u^{-4}$.

$$
\frac{dy}{dx} = (-4)u^{-5} \cdot (-2) = 8(5-2x)^{-5} = \frac{8}{(5-2x)^5}
$$

---

### Worked Example 5.4B (Trigonometric and Exponential Composite Functions)

> Find the derivatives of the following functions:
> (a) $y = \sin\left(2x + \frac{\pi}{3}\right)$
> (b) $y = e^{-3x + 1}$
> (c) $y = \tan(5x)$
> (d) $y = \cos\left(\frac{x}{2}\right)$

**Solution**:

(a) Let $u = 2x + \frac{\pi}{3}$, then $y = \sin u$.

$$
\frac{dy}{dx} = \cos u \cdot 2 = 2\cos\left(2x + \frac{\pi}{3}\right)
$$

(b) Let $u = -3x + 1$, then $y = e^u$.

$$
\frac{dy}{dx} = e^u \cdot (-3) = -3e^{-3x+1}
$$

(c) Let $u = 5x$, then $y = \tan u$.

$$
\frac{dy}{dx} = \sec^2 u \cdot 5 = 5\sec^2(5x)
$$

(d) Let $u = \frac{x}{2}$, then $y = \cos u$.

$$
\frac{dy}{dx} = -\sin u \cdot \frac{1}{2} = -\frac{1}{2}\sin\left(\frac{x}{2}\right)
$$

---

### Worked Example 5.4C (Logarithmic Composite and Multi-layer Chain Rule)

> Find the derivatives of the following functions:
> (a) $y = \ln(3x^2 + 1)$
> (b) $y = e^{\sin x}$
> (c) $y = \sin^3 x$ (i.e., $(\sin x)^3$)
> (d) $y = \sqrt{\cos x}$

**Solution**:

(a) Let $u = 3x^2 + 1$, then $y = \ln u$.

$$
\frac{dy}{dx} = \frac{1}{u} \cdot 6x = \frac{6x}{3x^2 + 1}
$$

(b) Let $u = \sin x$, then $y = e^u$.

$$
\frac{dy}{dx} = e^u \cdot \cos x = e^{\sin x} \cdot \cos x
$$

(c) There are two layers: let $u = \sin x$, $y = u^3$, then:

$$
\frac{dy}{dx} = 3u^2 \cdot \cos x = 3\sin^2 x \cdot \cos x
$$

(d) Write as $y = (\cos x)^{1/2}$, let $u = \cos x$, $y = u^{1/2}$.

$$
\frac{dy}{dx} = \frac{1}{2}u^{-1/2} \cdot (-\sin x) = \frac{1}{2}(\cos x)^{-1/2} \cdot (-\sin x) = -\frac{\sin x}{2\sqrt{\cos x}}
$$

---

### Worked Example 5.4D (Three-layer Chain Rule)

> Find the derivative of $y = \sin^2(3x)$.

**Solution**:

There are three layers: $y = (\sin(3x))^2$

Let $v = 3x$, $u = \sin v$, $y = u^2$.

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx} = (2u) \cdot (\cos v) \cdot (3)
$$

$$
= 2\sin(3x) \cdot \cos(3x) \cdot 3 = 6\sin(3x)\cos(3x) = 3\sin(6x)
$$

(The last step uses the double angle formula $\sin 2\theta = 2\sin\theta\cos\theta$.)

---

### Practice Problems 5.4

1. Find the derivative of $y = (5x + 2)^4$.
2. Find the derivative of $y = \frac{1}{\sqrt{3x - 1}}$.
3. Find the derivative of $y = e^{2x-3}$.
4. Find the derivative of $y = \ln(x^2 + 4)$.
5. Find the derivative of $y = \cos^3(2x)$.

---

## 5.5 Tangents and Normals

### 5.5.1 Basic Knowledge

Given a smooth curve $y = f(x)$ and a point $P(a, f(a))$ on it:

- **Tangent**: The line that passes through $P$ with slope $f'(a)$. The tangent is the **best linear approximation** to the curve at that point.
- **Normal**: The line that passes through $P$ and is perpendicular to the tangent.

### 5.5.2 Standard Three-Step Method (When the Point of Tangency is Known)

When the problem says "the tangent at point $P$", $P$ is the point of tangency. The solution steps are:

1. **Find the coordinates of the point of tangency**: Determine $a$, compute $f(a)$, get $(a, f(a))$.
2. **Find the slope of the tangent**: $m = f'(a)$.
3. **Write the tangent equation**: Use point-slope form $y - y_0 = m(x - x_0)$:

$$
y - f(a) = f'(a)(x - a)
$$

The slope of the **normal** $m_{\perp}$ satisfies $m \cdot m_{\perp} = -1$ (when $m \neq 0$), i.e., $m_{\perp} = -\frac{1}{f'(a)}$. The equation of the normal is:

$$
y - f(a) = -\frac{1}{f'(a)}(x - a)
$$

Special cases:
- If $f'(a) = 0$ (tangent is horizontal), the normal is the vertical line $x = a$.
- If $f'(a)$ does not exist (e.g., a cusp), the tangent is vertical and the normal is horizontal.

### 5.5.3 Why is the Tangent Slope Equal to the Derivative?

Geometrically, the line connecting two points $(a, f(a))$ and $(a+\delta x, f(a+\delta x))$ on the curve has slope $\frac{f(a+\delta x) - f(a)}{\delta x}$. As $\delta x$ approaches $0$, this line approaches the tangent line, and its slope approaches the derivative $f'(a)$.

Algebraically, the tangent equation $y = f(a) + f'(a)(x-a)$ has the same function value and the same first derivative as the curve at $x=a$, making it the "best linear approximation."

### 5.5.4 Important Pitfall: When the Point of Tangency is Unknown

If the problem says "the tangent passing through point $P$" (rather than "at point $P$"), then $P$ **may not be the point of tangency**. In this case:

1. Let the point of tangency be $(a, f(a))$, where $a$ is unknown.
2. Write the tangent equation: $y - f(a) = f'(a)(x - a)$.
3. Substitute the coordinates of $P$ into the equation to obtain an equation in $a$, then solve for all possible $a$.
4. Each $a$ corresponds to one tangent.

---

### Worked Example 5.5A (Tangent and Normal When the Point of Tangency is Known)

> What are the equations of the tangent and normal to the curve $y = x^2 - 3x + 2$ at the point $(2, 0)$?

**Solution**:

Point of tangency: $(2, 0)$, i.e., $a = 2$, $f(2) = 0$.

Differentiate: $f'(x) = 2x - 3$, $f'(2) = 2(2) - 3 = 1$.

Tangent equation:

$$
y - 0 = 1(x - 2) \quad \Rightarrow \quad y = x - 2
$$

Slope of normal $m_{\perp} = -\frac{1}{1} = -1$, normal equation:

$$
y - 0 = -1(x - 2) \quad \Rightarrow \quad y = -x + 2
$$

---

### Worked Example 5.5B (Tangent and Normal with Trigonometric Functions)

> Find the equations of the tangent and normal to the curve $y = \sin x$ at the point $\left(\frac{\pi}{6}, \frac{1}{2}\right)$.

**Solution**:

Point of tangency: $\left(\frac{\pi}{6}, \frac{1}{2}\right)$.

Differentiate: $f'(x) = \cos x$, $f'\left(\frac{\pi}{6}\right) = \cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$.

Tangent equation:

$$
y - \frac{1}{2} = \frac{\sqrt{3}}{2}\left(x - \frac{\pi}{6}\right)
$$

Simplifying:

$$
y = \frac{\sqrt{3}}{2}x - \frac{\sqrt{3}\pi}{12} + \frac{1}{2}
$$

Slope of normal $m_{\perp} = -\frac{1}{\sqrt{3}/2} = -\frac{2}{\sqrt{3}}$, normal equation:

$$
y - \frac{1}{2} = -\frac{2}{\sqrt{3}}\left(x - \frac{\pi}{6}\right)
$$

---

### Worked Example 5.5C ("Passing Through" a Point — Point of Tangency Unknown)

> Find the equations of the tangents to the curve $y = x^2$ that pass through the point $P(2, 3)$.

**Solution**:

Note that $P(2, 3)$ is not on the curve $y = x^2$ (since $2^2 = 4 \neq 3$), so $P$ is not the point of tangency. Let the point of tangency be $(a, a^2)$.

$f(x) = x^2$, $f'(x) = 2x$, so $f'(a) = 2a$.

Tangent equation:

$$
y - a^2 = 2a(x - a)
$$

Substitute $P(2, 3)$:

$$
3 - a^2 = 2a(2 - a)
$$

Expanding:

$$
3 - a^2 = 4a - 2a^2
$$

Rearranging:

$$
a^2 - 4a + 3 = 0
$$

Factorising:

$$
(a - 1)(a - 3) = 0
$$

So $a = 1$ or $a = 3$.

- When $a = 1$, the point of tangency is $(1, 1)$, slope $m = 2$, tangent equation: $y - 1 = 2(x - 1)$, i.e., $y = 2x - 1$.
- When $a = 3$, the point of tangency is $(3, 9)$, slope $m = 6$, tangent equation: $y - 9 = 6(x - 3)$, i.e., $y = 6x - 9$.

Point $P(2, 3)$ has two distinct tangents to the curve.

---

### Worked Example 5.5D (Tangent and Coordinate Axes Intersections)

> Find the intersections of the tangent to the curve $y = \ln x$ at the point $(1, 0)$ with the $x$-axis and $y$-axis.

**Solution**:

$f(x) = \ln x$, $f'(x) = \frac{1}{x}$, $f'(1) = 1$.

Tangent equation: $y - 0 = 1(x - 1)$, i.e., $y = x - 1$.

Intersection with $x$-axis: set $y = 0$, $0 = x - 1$, $x = 1$, i.e., $(1, 0)$ (which is the point of tangency itself).

Intersection with $y$-axis: set $x = 0$, $y = 0 - 1 = -1$, i.e., $(0, -1)$.

---

### Practice Problems 5.5

1. Find the equations of the tangent and normal to the curve $y = x^3$ at the point $(2, 8)$.
2. Find the equation of the tangent to the curve $y = e^x$ at the point $(0, 1)$.
3. Find the equations of the tangent and normal to the curve $y = \sqrt{x}$ at the point $(4, 2)$.
4. Find the equations of the tangents to the curve $y = x^2 - 2x$ that pass through the point $(1, -4)$.

---

## 5.6 Stationary Points (Maxima and Minima)

### 5.6.1 What is a Stationary Point?

A **stationary point** is a point on the graph where the tangent is horizontal (slope zero). At a stationary point, the function value may be a local maximum, a local minimum, or neither (the latter case is not examined in IGCSE).

**Steps for finding stationary points**:
1. Find $f'(x)$.
2. Solve $f'(x) = 0$.
3. Each solution $x = a$ corresponds to a stationary point $(a, f(a))$.

### 5.6.2 Distinguishing Between Maxima and Minima

There are two methods to distinguish between maxima and minima.

**Method 1: First Derivative Test (Sign Change Method)**

Observe the sign of $f'(x)$ on either side of the stationary point $x = a$:

| $x$ slightly less than $a$ (left) | $x = a$ | $x$ slightly greater than $a$ (right) | Conclusion |
|:---:|:---:|:---:|:---:|
| $f' > 0$ (increasing) | $f' = 0$ | $f' < 0$ (decreasing) | **Local maximum** |
| $f' < 0$ (decreasing) | $f' = 0$ | $f' > 0$ (increasing) | **Local minimum** |
| $f' > 0$ (increasing) | $f' = 0$ | $f' > 0$ (increasing) | Not an extremum (not examined) |
| $f' < 0$ (decreasing) | $f' = 0$ | $f' < 0$ (decreasing) | Not an extremum (not examined) |

Why does the sign change determine the type of extremum? Imagine climbing a mountain:
- If you first go uphill ($f'>0$), reach the summit ($f'=0$), then go downhill ($f'<0$), the summit is a local maximum.
- If you first go downhill ($f'<0$), reach the valley floor ($f'=0$), then go uphill ($f'>0$), the valley floor is a local minimum.

**Method 2: Second Derivative Test**

The second derivative $f''(x)$ is the derivative of the first derivative. It tells us the rate of change of $f'(x)$.

- If $f'(a) = 0$ and $f''(a) > 0$ → **Local minimum** (the curve is "concave up" at that point, like the bottom of a bowl).
- If $f'(a) = 0$ and $f''(a) < 0$ → **Local maximum** (the curve is "concave down" at that point, like an upside-down bowl).
- If $f''(a) = 0$, the test is inconclusive, and the first derivative test must be used.

**Why can the second derivative determine the type?**
- $f''(a) > 0$ means $f'(x)$ is increasing at $x=a$. Since $f'(a)=0$, $f'$ changes from negative to positive → minimum.
- $f''(a) < 0$ means $f'(x)$ is decreasing at $x=a$. Since $f'(a)=0$, $f'$ changes from positive to negative → maximum.

### 5.6.3 Finding the Second Derivative

The second derivative is the derivative of the first derivative. In notation:

$$
f''(x) = \frac{d}{dx}(f'(x)) \quad \text{or} \quad \frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right)
$$

**Example**: $f(x) = x^3 - 3x^2 + 2$
- First derivative: $f'(x) = 3x^2 - 6x$
- Second derivative: $f''(x) = 6x - 6$

---

### Worked Example 5.6A (Stationary Points of a Polynomial Function)

> Find the stationary points of $f(x) = 2x^3 - 9x^2 + 12x - 3$ and determine whether they are maxima or minima.

**Solution**:

Step 1: Find $f'(x)$ and set it to zero.

$$
f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x-1)(x-2)
$$

Set $f'(x) = 0$: $x = 1$ or $x = 2$.

$$
f(1) = 2 - 9 + 12 - 3 = 2, \quad \text{stationary point } (1, 2)
$$
$$
f(2) = 16 - 36 + 24 - 3 = 1, \quad \text{stationary point } (2, 1)
$$

Step 2: Use the second derivative test.

$$
f''(x) = 12x - 18
$$

- $f''(1) = 12(1) - 18 = -6 < 0$ → $(1, 2)$ is a **local maximum**.
- $f''(2) = 12(2) - 18 = 6 > 0$ → $(2, 1)$ is a **local minimum**.

First derivative test verification: to the left of $x=1$, take $x=0$, $f'(0) = 12 > 0$; to the right of $x=1$, take $x=1.5$, $f'(1.5) = 6(0.5)(-0.5) = -1.5 < 0$. Sign changes from positive to negative, confirming a maximum.

---

### Worked Example 5.6B (Stationary Points with Trigonometric Functions)

> Find the stationary points of $f(x) = \sin x + \cos x$ on the interval $[0, 2\pi]$ and determine their types.

**Solution**:

$$
f'(x) = \cos x - \sin x
$$

Set $f'(x) = 0$:

$$
\cos x - \sin x = 0 \quad \Rightarrow \quad \cos x = \sin x \quad \Rightarrow \quad \tan x = 1
$$

On $[0, 2\pi]$, the solutions to $\tan x = 1$ are $x = \frac{\pi}{4}$ and $x = \frac{5\pi}{4}$.

$$
f\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2}, \quad
f\left(\frac{5\pi}{4}\right) = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2}
$$

Find the second derivative: $f''(x) = -\sin x - \cos x$.

- $f''\left(\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} < 0$ → $\left(\frac{\pi}{4}, \sqrt{2}\right)$ is a **local maximum**.
- $f''\left(\frac{5\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} > 0$ → $\left(\frac{5\pi}{4}, -\sqrt{2}\right)$ is a **local minimum**.

---

### Worked Example 5.6C (Stationary Points with Exponential Functions)

> Find the stationary point of $f(x) = xe^{-x}$ and determine its type. Find the maximum value of the function.

**Solution**:

Use the Product Rule: let $u = x$, $v = e^{-x}$, then $u' = 1$, $v' = -e^{-x}$.

$$
f'(x) = x \cdot (-e^{-x}) + e^{-x} \cdot 1 = e^{-x}(1 - x)
$$

Set $f'(x) = 0$. Since $e^{-x} > 0$ for all $x$, we have $1 - x = 0$, i.e., $x = 1$.

$$
f(1) = 1 \cdot e^{-1} = \frac{1}{e}
$$

The stationary point is $\left(1, \frac{1}{e}\right)$.

Using the first derivative test: to the left of $x=1$, take $x=0$, $f'(0) = e^0(1-0) = 1 > 0$; to the right of $x=1$, take $x=2$, $f'(2) = e^{-2}(1-2) = -e^{-2} < 0$. The sign changes from positive to negative, so $\left(1, \frac{1}{e}\right)$ is a **local maximum**.

Since $xe^{-x} \to 0$ as $x \to \infty$ and $xe^{-x} \to -\infty$ as $x \to -\infty$, this local maximum is also the global maximum, with value $\frac{1}{e}$.

---

### Worked Example 5.6D (Finding Parameters from Stationary Points)

> Given that $f(x) = x^3 + ax^2 + b$ has a stationary point at $x = 2$, and the function value at this stationary point is $5$, find the constants $a$ and $b$.

**Solution**:

$f'(x) = 3x^2 + 2ax$

There is a stationary point at $x=2$, so $f'(2) = 0$:

$$
3(2)^2 + 2a(2) = 0 \quad \Rightarrow \quad 12 + 4a = 0 \quad \Rightarrow \quad a = -3
$$

The function value at the stationary point is $f(2) = 5$:

$$
f(2) = 2^3 + (-3)(2)^2 + b = 8 - 12 + b = b - 4 = 5 \quad \Rightarrow \quad b = 9
$$

Thus $a = -3$, $b = 9$. $f(x) = x^3 - 3x^2 + 9$.

---

### Practice Problems 5.6

1. Find the stationary points of $f(x) = x^3 - 6x^2 + 9x + 1$ and determine their types.
2. Find the stationary points of $f(x) = x^2 e^x$ and determine their types.
3. Given that $f(x) = x^3 + ax + b$ has a stationary point at $x = 1$ with $f(1) = 4$, find $a$ and $b$.
4. Find the extreme values of $f(x) = 2x^3 - 3x^2 - 12x + 5$.

---

## 5.7 Connected Rates of Change and Small Increments Approximation

### 5.7.1 Connected Rates of Change

Connected rates of change problems deal with the **rates of change of multiple interrelated quantities**. The core idea is: if $y$ depends on $u$ through some relationship, and $u$ in turn depends on $x$, then we can link $\frac{dy}{dx}$ to $\frac{dy}{du}$ and $\frac{du}{dx}$ through the chain rule.

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

More generally, when the problem involves time $t$, we often use:

$$
\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}
$$

**Problem-solving steps**:
1. Identify all relevant variables, determine the known rate of change and the required rate of change.
2. Establish the functional relationship between the variables (geometric formula, physical relationship, etc.).
3. Differentiate both sides of the relationship with respect to time $t$ (implicit differentiation).
4. Substitute the known values and solve for the unknown rate of change.

### 5.7.2 Small Increments and Approximations

Another important application of the derivative is using the tangent line to approximate the change in a function near a given point.

Recall the definition of the derivative:

$$
f'(a) \approx \frac{f(a + \delta x) - f(a)}{\delta x} \quad \text{(when $\delta x$ is small)}
$$

Rearranging gives:

$$
\boxed{f(a + \delta x) \approx f(a) + f'(a) \cdot \delta x}
$$

This is the **linear approximation** formula. It tells us: for a small change $\delta x$, the change in the function value is approximately equal to the derivative multiplied by the change in the independent variable.

In Leibniz notation:

$$
\delta y \approx \frac{dy}{dx} \cdot \delta x
$$

where $\delta y = f(x + \delta x) - f(x)$ is the actual change in the function value, and $\frac{dy}{dx} \cdot \delta x$ is the change along the tangent line (the approximate value).

**Why does this work?** Geometrically, the tangent line is the best approximation to the curve near the point of tangency. When $\delta x$ is small, the point $(a+\delta x, f(a+\delta x))$ on the curve is very close to the point $(a+\delta x, f(a) + f'(a)\delta x)$ on the tangent line, so we can use the change on the tangent line to approximate the change on the curve.

---

### Worked Example 5.7A (Connected Rates of Change — Area of a Circle)

> The radius of a circle is increasing at a rate of $2$ cm/s. Find the rate at which the area is increasing when the radius is $5$ cm.

**Solution**:

Let the radius be $r$ and the area be $A$. We know $\frac{dr}{dt} = 2$, and we need to find $\frac{dA}{dt}$ when $r = 5$.

Area of a circle: $A = \pi r^2$

Differentiate with respect to time $t$ (using the chain rule):

$$
\frac{dA}{dt} = \frac{dA}{dr} \cdot \frac{dr}{dt} = 2\pi r \cdot \frac{dr}{dt}
$$

Substitute the known values: $r = 5$, $\frac{dr}{dt} = 2$.

$$
\frac{dA}{dt} = 2\pi \cdot 5 \cdot 2 = 20\pi \text{ cm}^2/\text{s}
$$

So when the radius is $5$ cm, the area is increasing at a rate of $20\pi$ cm²/s.

---

### Worked Example 5.7B (Connected Rates of Change — Kinematics)

> An inverted conical container has a top radius of $4$ m and a height of $8$ m. Water is being poured in at a rate of $2$ m³/min. Find the rate at which the water level is rising when the water depth is $3$ m.

**Solution**:

Let the water depth be $h$, the radius of the water surface be $r$, and the volume of water be $V$. We know $\frac{dV}{dt} = 2$, and we need to find $\frac{dh}{dt}$ when $h = 3$.

By similar triangles: $\frac{r}{h} = \frac{4}{8} = \frac{1}{2}$, so $r = \frac{h}{2}$.

Volume of a cone:

$$
V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{h}{2}\right)^2 h = \frac{1}{3}\pi \cdot \frac{h^2}{4} \cdot h = \frac{\pi}{12}h^3
$$

Differentiate with respect to time:

$$
\frac{dV}{dt} = \frac{dV}{dh} \cdot \frac{dh}{dt} = \frac{\pi}{12} \cdot 3h^2 \cdot \frac{dh}{dt} = \frac{\pi}{4}h^2 \cdot \frac{dh}{dt}
$$

Substitute $\frac{dV}{dt} = 2$ and $h = 3$:

$$
2 = \frac{\pi}{4} \cdot 3^2 \cdot \frac{dh}{dt} = \frac{9\pi}{4} \cdot \frac{dh}{dt}
$$

Solving:

$$
\frac{dh}{dt} = \frac{2 \cdot 4}{9\pi} = \frac{8}{9\pi} \text{ m/min}
$$

So when the water depth is $3$ m, the water level is rising at a rate of $\frac{8}{9\pi}$ m/min.

---

### Worked Example 5.7C (Small Increments Approximation)

> Use differential approximation to estimate the value of $\sqrt{4.02}$.

**Solution**:

Let $f(x) = \sqrt{x}$, choose $a = 4$ (a number whose square root is easy to compute), and $\delta x = 0.02$.

$$
f(x) = x^{1/2}, \quad f'(x) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}
$$

$$
f(4) = \sqrt{4} = 2, \quad f'(4) = \frac{1}{2\sqrt{4}} = \frac{1}{4}
$$

Linear approximation formula:

$$
f(4 + 0.02) \approx f(4) + f'(4) \cdot 0.02
$$

$$
\sqrt{4.02} \approx 2 + \frac{1}{4} \times 0.02 = 2 + 0.005 = 2.005
$$

Compared to the exact value $2.004993\ldots$, the approximation $2.005$ has a very small error (about $7 \times 10^{-6}$).

---

### Worked Example 5.7D (Small Increments Approximation — Finding Maximum Error from Known Error)

> The volume of a sphere is given by $V = \frac{4}{3}\pi r^3$. If the maximum error in measuring the radius is $0.1$ cm, find the maximum approximate error in calculating the volume when the measured radius is $5$ cm.

**Solution**:

We know $r = 5$ and $|\delta r| \leq 0.1$.

$$
\frac{dV}{dr} = 4\pi r^2
$$

$$
\delta V \approx \frac{dV}{dr} \cdot \delta r = 4\pi r^2 \cdot \delta r
$$

Maximum error (taking absolute values):

$$
|\delta V|_{\max} \approx 4\pi \cdot 5^2 \cdot 0.1 = 4\pi \cdot 25 \cdot 0.1 = 10\pi \text{ cm}^3
$$

So the maximum approximate error in the volume is about $10\pi \approx 31.4$ cm³.

---

### Practice Problems 5.7

1. The side length of a square is increasing at a rate of $3$ cm/s. Find the rate at which the area is increasing when the side length is $10$ cm.
2. Use differential approximation to estimate $\sqrt[3]{8.03}$. (Hint: let $f(x) = \sqrt[3]{x}$)
3. Gas is expanding in a spherical container. When the radius is $2$ m, the volume is increasing at a rate of $16\pi$ m³/s. Find the rate at which the radius is increasing at that moment.

---

## 5.8 Practical Maxima and Minima Problems

### 5.8.1 Problem-solving Approach

Practical maxima and minima problems apply calculus to real-world optimisation problems — for example, how to use the least material to make a container, how to maximise profit given a certain cost, how to determine the fastest route, etc.

**Standard problem-solving steps**:

1. **Understand the problem**: Identify the quantity to be maximised or minimised (the objective function).
2. **Introduce variables**: Introduce variables to represent all relevant quantities.
3. **Establish relationships**: Use the information given in the problem (geometric relations, physical constraints, etc.) to express the objective function in terms of **a single variable**.
4. **Differentiate and find stationary points**: Differentiate the objective function, set the derivative to zero, and solve for the stationary point.
5. **Determine the type**: Use the first or second derivative test to confirm whether it is a maximum or minimum.
6. **Check reasonableness**: Verify that the stationary point lies within the domain, and answer the original question.

> ⚠️ **Key point**: Practical problems usually have constraint conditions (e.g., fixed total length, fixed area). Use the constraint to eliminate extra variables and reduce the objective function to a single-variable function.

---

### Worked Example 5.8A (Maximising Area)

> A $100$ m length of fencing is used to enclose a rectangular garden with one side against a wall (the wall is long enough). Find the maximum area of the garden and the dimensions at which it occurs.

**Solution**:

Let the two sides perpendicular to the wall have length $x$ m, and the side parallel to the wall have length $y$ m.

Total fencing length is $100$ m, constraint: $2x + y = 100$, i.e., $y = 100 - 2x$.

Garden area $A = x \cdot y = x(100 - 2x) = 100x - 2x^2$.

Note the domain: $x > 0$ and $y > 0$, i.e., $100 - 2x > 0$, $x < 50$, so $0 < x < 50$.

Differentiate:

$$
A'(x) = 100 - 4x
$$

Set $A'(x) = 0$: $100 - 4x = 0$, giving $x = 25$.

Second derivative: $A''(x) = -4 < 0$, confirming $x = 25$ is a **maximum**.

At this point, $y = 100 - 2(25) = 50$.

Maximum area: $A = 25 \times 50 = 1250$ m².

**Answer**: When the sides perpendicular to the wall are $25$ m and the side parallel to the wall is $50$ m, the maximum area is $1250$ m².

---

### Worked Example 5.8B (Maximising Volume — Open Box)

> From a rectangular sheet of cardboard measuring $30$ cm $\times$ $20$ cm, four squares of side length $x$ cm are cut from the corners, and the sides are folded up to make an open box. Find the value of $x$ that maximises the volume of the box, and find the maximum volume.

**Solution**:

After cutting squares of side $x$, the base dimensions of the box are $(30 - 2x) \times (20 - 2x)$, and the height is $x$.

Volume of the box:

$$
V(x) = x(30 - 2x)(20 - 2x) = x(600 - 60x - 40x + 4x^2) = x(600 - 100x + 4x^2)
$$

$$
V(x) = 4x^3 - 100x^2 + 600x
$$

Domain: $x > 0$, $30 - 2x > 0 \Rightarrow x < 15$, $20 - 2x > 0 \Rightarrow x < 10$, so $0 < x < 10$.

Differentiate:

$$
V'(x) = 12x^2 - 200x + 600
$$

Set $V'(x) = 0$:

$$
12x^2 - 200x + 600 = 0
$$

Divide both sides by $4$: $3x^2 - 50x + 150 = 0$

Using the quadratic formula:

$$
x = \frac{50 \pm \sqrt{2500 - 1800}}{6} = \frac{50 \pm \sqrt{700}}{6} = \frac{50 \pm 10\sqrt{7}}{6}
$$

The two solutions: $x_1 = \frac{50 + 10\sqrt{7}}{6} \approx \frac{50 + 26.46}{6} \approx 12.74$ (outside the domain $x < 10$, discard)

$$
x_2 = \frac{50 - 10\sqrt{7}}{6} \approx \frac{50 - 26.46}{6} \approx 3.92
$$

So $x = \frac{50 - 10\sqrt{7}}{6} \approx 3.92$ cm.

Verify with the second derivative: $V''(x) = 24x - 200$

$$
V''(3.92) = 24(3.92) - 200 \approx 94.08 - 200 = -105.92 < 0
$$

Confirmed as a maximum.

Maximum volume:

$$
V = 3.92 \times (30 - 7.84) \times (20 - 7.84) = 3.92 \times 22.16 \times 12.16 \approx 1056.3 \text{ cm}^3
$$

**Answer**: When the side length of the cut squares is approximately $3.92$ cm, the box volume is maximised at approximately $1056$ cm³.

---

### Worked Example 5.8C (Minimising Cost)

> A company needs to manufacture an open cylindrical bucket with a fixed volume of $V = 1000\pi$ cm³. The material for the base costs $2$ yuan/cm², and the material for the sides costs $1$ yuan/cm². Find the base radius $r$ and height $h$ that minimise the total cost, and find the minimum cost.

**Solution**:

Let the base radius be $r$ cm and the height be $h$ cm.

Volume constraint: $V = \pi r^2 h = 1000\pi$, so $h = \frac{1000}{r^2}$.

Cost: base area $\pi r^2$, price $2$ yuan/cm²; lateral surface area $2\pi r h$, price $1$ yuan/cm².

$$
C = 2 \cdot \pi r^2 + 1 \cdot 2\pi r h = 2\pi r^2 + 2\pi r \cdot \frac{1000}{r^2} = 2\pi r^2 + \frac{2000\pi}{r}
$$

Domain: $r > 0$.

Differentiate:

$$
C'(r) = 4\pi r - \frac{2000\pi}{r^2}
$$

Set $C'(r) = 0$:

$$
4\pi r - \frac{2000\pi}{r^2} = 0 \quad \Rightarrow \quad 4\pi r = \frac{2000\pi}{r^2}
$$

Divide both sides by $\pi$ ($\pi > 0$):

$$
4r = \frac{2000}{r^2} \quad \Rightarrow \quad 4r^3 = 2000 \quad \Rightarrow \quad r^3 = 500
$$

So: $r = \sqrt[3]{500} = \sqrt[3]{5 \times 100} = 5\sqrt[3]{4}$ cm.

At this point, $h = \frac{1000}{r^2} = \frac{1000}{500^{2/3}} = 2 \cdot 500^{1/3} = 2r$.

Thus $h = 2r$, i.e., the height equals the diameter when the cost is minimised.

Verify with the second derivative:

$$
C''(r) = 4\pi + \frac{4000\pi}{r^3}
$$

Substituting $r^3 = 500$: $C''(r) = 4\pi + \frac{4000\pi}{500} = 4\pi + 8\pi = 12\pi > 0$, confirmed as a minimum.

Minimum cost:

$$
C_{\min} = 6\pi \cdot 500^{2/3} \text{ yuan}
$$

Approximate calculation: $500^{2/3} = (500^{1/3})^2 \approx (7.937)^2 \approx 63$, so $C_{\min} \approx 6\pi \times 63 \approx 1188$ yuan.

**Answer**: When the base radius $r = \sqrt[3]{500}$ cm (about $7.94$ cm) and the height $h = 2r$ (about $15.88$ cm), the minimum cost is approximately $1188$ yuan.

---

### Worked Example 5.8D (Maximising Profit)

> A factory produces a product. The cost of producing $x$ units per day is $C(x) = 200 + 10x + 0.01x^2$ yuan, and the selling price is $30$ yuan per unit. Find the number of units that should be produced per day to maximise profit, and find the maximum profit.

**Solution**:

Revenue: $R(x) = 30x$

Profit: $P(x) = R(x) - C(x) = 30x - (200 + 10x + 0.01x^2) = -0.01x^2 + 20x - 200$

Domain: $x \ge 0$ and integer (in practice, positive integers, but we can use the continuous function to approximate the maximum and then round).

Differentiate:

$$
P'(x) = -0.02x + 20
$$

Set $P'(x) = 0$: $-0.02x + 20 = 0$, giving $x = 1000$.

Second derivative: $P''(x) = -0.02 < 0$, confirmed as a maximum.

Maximum profit:

$$
P(1000) = -0.01(1000)^2 + 20(1000) - 200 = -10000 + 20000 - 200 = 9800 \text{ yuan}
$$

**Answer**: Maximum profit occurs when $1000$ units are produced per day, with a maximum profit of $9800$ yuan.

---

### Practice Problems 5.8

1. A $120$ m length of fencing is used to enclose a rectangular garden (not against a wall). Find the maximum area and the dimensions at which it occurs.
2. Find the shortest distance from the curve $y = x^2 - 4x + 5$ to the origin $(0,0)$.
   (Hint: distance squared $d^2 = x^2 + y^2$, substitute $y$ and minimise)
3. An open cylindrical can has a fixed volume $V$ (constant). Find the ratio of the base radius $r$ to the height $h$ that minimises the surface area.

---

## Chapter Summary (Quick Reference Table)

| Topic | Formula/Method | Section |
|--------|-----------|:----:|
| Limit definition of derivative | $\displaystyle f'(x) = \lim_{\delta x \to 0} \frac{f(x+\delta x) - f(x)}{\delta x}$ | 5.1 |
| Power Rule | $\frac{d}{dx}(x^n) = nx^{n-1}$ ($n$ any rational number) | 5.2 |
| Trigonometric derivatives | $\frac{d}{dx}(\sin x) = \cos x$, $\frac{d}{dx}(\cos x) = -\sin x$, $\frac{d}{dx}(\tan x) = \sec^2 x$ | 5.2 |
| Exponential & logarithmic derivatives | $\frac{d}{dx}(e^x) = e^x$, $\frac{d}{dx}(\ln x) = \frac{1}{x}$, $\frac{d}{dx}(a^x) = a^x\ln a$ | 5.2 |
| Chain Rule | $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ | 5.3 |
| Product Rule | $(uv)' = uv' + vu'$ | 5.4 |
| Quotient Rule | $\left(\frac{u}{v}\right)' = \frac{vu' - uv'}{v^2}$ | 5.4 |
| Tangent equation | $y - f(a) = f'(a)(x - a)$ | 5.5 |
| Normal equation | $y - f(a) = -\frac{1}{f'(a)}(x - a)$ ($f'(a) \neq 0$) | 5.5 |
| Stationary points | Solve $f'(x) = 0$ | 5.6 |
| Second derivative test | $f''(a) > 0$ is minimum, $f''(a) < 0$ is maximum | 5.6 |
| Connected rates of change | $\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}$ | 5.7 |
| Small increments approximation | $f(a + \delta x) \approx f(a) + f'(a)\delta x$, $\delta y \approx \frac{dy}{dx}\delta x$ | 5.7 |
| Practical maxima/minima | Build single-variable function $\to$ differentiate and find stationary point $\to$ determine type $\to$ answer original question | 5.8 |

---

## Answers to Practice Problems

### 5.1 Concept of Derivative and Notation

1. $f'(1) = 4$
   - $f(1+\delta x) = (1+\delta x)^2 + 2(1+\delta x) = 1 + 2\delta x + (\delta x)^2 + 2 + 2\delta x = 3 + 4\delta x + (\delta x)^2$
   - $f(1) = 1^2 + 2(1) = 3$
   - $\frac{f(1+\delta x) - f(1)}{\delta x} = \frac{4\delta x + (\delta x)^2}{\delta x} = 4 + \delta x \to 4$

2. $s'(3) = 15$ m/s
   - $s'(t) = 4t + 3$, $s'(3) = 4(3) + 3 = 15$

3. $8$
   - $\lim_{x \to 4} \frac{x^2 - 16}{x - 4} = \lim_{x \to 4} \frac{(x-4)(x+4)}{x-4} = \lim_{x \to 4} (x+4) = 8$


### 5.2 Product Rule and Quotient Rule

1. $y' = 2xe^x + x^2e^x = xe^x(2 + x)$
2. $y' = \frac{3(x-2) - 3x(1)}{(x-2)^2} = \frac{3x-6-3x}{(x-2)^2} = -\frac{6}{(x-2)^2}$
3. $y' = \cos x - x\sin x$
4. $y' = \frac{(1)(x^2+1) - (x+1)(2x)}{(x^2+1)^2} = \frac{x^2+1 - 2x^2 - 2x}{(x^2+1)^2} = \frac{-x^2 - 2x + 1}{(x^2+1)^2}$
5. $y' = e^x\sin x + e^x\cos x = e^x(\sin x + \cos x)$


### 5.3 Basic Differentiation Formulas

1. $f'(x) = 12x^2 - 4x + 5$

2. $g'(x) = -\frac{6}{x^3} + \frac{1}{4x\sqrt{x}} + 2x^{-2/3}$
   - Specifically: $\frac{3}{x^2} = 3x^{-2} \to -6x^{-3}$; $-\frac{1}{2}x^{-1/2} \to \frac{1}{4}x^{-3/2}$; $6x^{1/3} \to 2x^{-2/3}$

3. $h'(x) = 5\cos x + 3\sin x + 2\sec^2 x$

4. $p'(x) = 2e^x + 4^x\ln 4 - \frac{1}{3x}$


### 5.4 Chain Rule

1. $y' = 20(5x+2)^3$
2. $y = (3x-1)^{-1/2}$, $y' = -\frac{3}{2}(3x-1)^{-3/2} = -\frac{3}{2\sqrt{(3x-1)^3}}$
3. $y' = 2e^{2x-3}$
4. $y' = \frac{2x}{x^2+4}$
5. $y' = 3\cos^2(2x) \cdot (-\sin(2x)) \cdot 2 = -6\cos^2(2x)\sin(2x) = -3\cos(2x)\sin(4x)$


### 5.5 Tangents and Normals

1. $f(x) = x^3$, $f'(x) = 3x^2$, $f'(2) = 12$
   - Tangent: $y - 8 = 12(x - 2)$, i.e., $y = 12x - 16$
   - Normal: $y - 8 = -\frac{1}{12}(x - 2)$, i.e., $y = -\frac{1}{12}x + \frac{49}{6}$

2. $f(x) = e^x$, $f'(x) = e^x$, $f'(0) = 1$
   - Tangent: $y - 1 = 1(x - 0)$, i.e., $y = x + 1$

3. $f(x) = \sqrt{x}$, $f'(x) = \frac{1}{2\sqrt{x}}$, $f'(4) = \frac{1}{4}$
   - Tangent: $y - 2 = \frac{1}{4}(x - 4)$, i.e., $y = \frac{1}{4}x + 1$
   - Normal: $y - 2 = -4(x - 4)$, i.e., $y = -4x + 18$

4. Let the point of tangency be $(a, a^2 - 2a)$, $f'(a) = 2a - 2$.
   Tangent equation: $y - (a^2 - 2a) = (2a - 2)(x - a)$
   Substitute $(1, -4)$: $-4 - (a^2 - 2a) = (2a - 2)(1 - a)$
   Simplify: $-4 - a^2 + 2a = (2a-2)(1-a) = 2a-2 - 2a^2 + 2a = -2a^2 + 4a - 2$
   Rearranging: $-4 - a^2 + 2a = -2a^2 + 4a - 2$, bring terms: $a^2 - 2a - 2 = 0$
   So $a = 1 \pm \sqrt{3}$
   - $a = 1 + \sqrt{3}$: slope $m = 2\sqrt{3}$, tangent $y = 2\sqrt{3}x - 2\sqrt{3} - 4$
   - $a = 1 - \sqrt{3}$: slope $m = -2\sqrt{3}$, tangent $y = -2\sqrt{3}x + 2\sqrt{3} - 4$


### 5.6 Stationary Points

1. $f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$
   $x = 1$: $f(1) = 5$, $f''(1) = 6-12 = -6 < 0$ → maximum
   $x = 3$: $f(3) = 1$, $f''(3) = 18-12 = 6 > 0$ → minimum

2. $f'(x) = 2xe^x + x^2e^x = xe^x(2 + x)$
   $x = 0$: $f(0) = 0$, $f''(0) = 2 > 0$ → minimum
   $x = -2$: $f(-2) = 4e^{-2}$, $f''(-2) = -2e^{-2} < 0$ → maximum

3. $f'(x) = 3x^2 + a$, $f'(1) = 3 + a = 0$ → $a = -3$
   $f(1) = 1 + (-3)(1) + b = 4$ → $b = 6$

4. $f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x-2)(x+1)$
   $x = -1$: $f(-1) = -2 - 3 + 12 + 5 = 12$, $f''(-1) = -12 - 6 = -18 < 0$ → maximum $12$
   $x = 2$: $f(2) = 16 - 12 - 24 + 5 = -15$, $f''(2) = 24 - 6 = 18 > 0$ → minimum $-15$


### 5.7 Connected Rates of Change and Small Increments Approximation

1. $A = s^2$, $\frac{dA}{dt} = 2s\frac{ds}{dt} = 2(10)(3) = 60$ cm²/s

2. $f(x) = x^{1/3}$, $f'(x) = \frac{1}{3}x^{-2/3}$, take $a = 8$, $\delta x = 0.03$
   $f(8) = 2$, $f'(8) = \frac{1}{3}(8)^{-2/3} = \frac{1}{3}\cdot\frac{1}{4} = \frac{1}{12}$
   $\sqrt[3]{8.03} \approx 2 + \frac{1}{12} \times 0.03 = 2 + 0.0025 = 2.0025$

3. $V = \frac{4}{3}\pi r^3$, $\frac{dV}{dt} = 4\pi r^2\frac{dr}{dt}$
   $16\pi = 4\pi(2)^2\frac{dr}{dt} = 16\pi\frac{dr}{dt}$ → $\frac{dr}{dt} = 1$ m/s


### 5.8 Practical Maxima and Minima Problems

1. Let length be $x$, width be $y$, $2x + 2y = 120$, $y = 60 - x$
   $A = xy = x(60-x) = 60x - x^2$
   $A'(x) = 60 - 2x = 0$ → $x = 30$, $y = 30$
   $A''(x) = -2 < 0$ → maximum
   Maximum area $= 30 \times 30 = 900$ m²

2. $d^2 = x^2 + (x^2 - 4x + 5)^2$
   Let $g(x) = d^2$, differentiate and find the minimum.
   
   Simpler approach: let $h(x) = x^2 + (x^2-4x+5)^2$
   $h'(x) = 2x + 2(x^2-4x+5)(2x-4)$
   $= 2x + 2(x^2-4x+5)(2)(x-2)$
   $= 2x + 4(x^2-4x+5)(x-2)$
   
   Set $h'(x) = 0$, we can find $x = 2$.
   $d^2 = 2^2 + (4-8+5)^2 = 4 + 1 = 5$, $d = \sqrt{5}$

3. Surface area $S = \pi r^2 + 2\pi rh$, volume $V = \pi r^2 h$ (constant), $h = \frac{V}{\pi r^2}$
   $S = \pi r^2 + 2\pi r\left(\frac{V}{\pi r^2}\right) = \pi r^2 + \frac{2V}{r}$
   $S'(r) = 2\pi r - \frac{2V}{r^2} = 0$ → $2\pi r = \frac{2V}{r^2}$ → $\pi r^3 = V$ → $r^3 = \frac{V}{\pi}$
   And $V = \pi r^2 h$, so $\pi r^3 = \pi r^2 h$ → $r = h$
   **Answer**: $r : h = 1 : 1$, i.e., the base radius equals the height for minimum surface area.

---
---

