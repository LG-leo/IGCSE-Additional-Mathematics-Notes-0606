# U1 – Function / Mapping

Input $\rightarrow$ output is called **mapping**.

- Algebraically (linear): $x \mapsto x + 1$  
  Read as: *x is mapped to x + 1*.
- **One-one** (one input, one output): **injective**, e.g. $f(x)=2x+1$.
- **Many-one** (more inputs, one output): e.g. $f(x)=x^2$.
- **One-many** (one input, more outputs): e.g. $f(x)=\pm\sqrt{x}$.

## Definition of a function

- A function maps each $x$ value to **exactly one** $y$ value for a defined set of input values.
- One-one and many-one mappings are called functions.

It can be written as:

$$
f: x \mapsto x + 1,\quad x \in \mathbb{R}
$$

or

$$
f(x) = x + 1,\quad x \in \mathbb{R}
$$

Read as: *the function $f$ such that $x$ is mapped to $x+1$*.  
$f(x)$ represents the output values for the function $f$.

## Composite functions

A composite function is formed by applying one function to the result of another.

If you have two functions $f$ and $g$, the composite function $f \circ g$ (read as “$f$ composed with $g$”) is defined as

$$
(f \circ g)(x) = f(g(x))
$$

This means you first apply $g$ to $x$, then apply $f$ to the result.

- $f$ is the outer function; $g$ is the inner function.
- In IG 0606 ADD, we often write $fg(x)$ instead of $f \circ g$.
- Domain of $gf$: $\{x \in \text{dom } f \mid f(x) \in \text{dom } g\}$.

## Modulus functions

- *Modulus* means *absolute value*.
- $f(x)=|x|$ is a modulus function.

---

1. Trigonometric Modulus Graphs y = |a sin(bx) + c|

Syllabus reference: 1.4 (modulus function can be applied to trigonometric functions)

Common issue with textbooks: they only cover linear/quadratic modulus; trigonometric modulus is either omitted or explained too briefly.

Drawing steps (using y = |2 sin x - 1| as an example):

1. First draw the original function y = 2 sin x - 1
   - Amplitude = 2, equilibrium line y = -1, period = 2π
   - Draw half a period of the wave, mark the intersections with the x-axis (solve 2 sin x - 1 = 0 → sin x = 0.5 → x = π/6, 5π/6, etc.)

2. Identify the parts of the original function that lie below the x-axis
   - The original function is negative when sin x < 0.5, i.e. intervals like (-π, π/6), etc.

3. Reflection
   - Reflect the parts below the x-axis upward across the x-axis, creating "sharp points" or "rounded tips"

4. Final graph
   - The result is a series of "peaks" or "W" shapes; the original x-intercepts become cusp points (non‑differentiable)

Key points:
- The modulus of a trigonometric function turns troughs into peaks
- The period stays the same, but the peaks may become wider because negative parts are flipped up
- The points where the original graph crossed the x-axis become cusps (sharp corners)

## Graphs of $y=|f(x)|$ where $f(x)$ is linear

Steps:
1. Draw the graph of the linear function.
2. Reflect the part of the line that lies below the $x$-axis in the $x$-axis.

## Inverse function

- The inverse function $f^{-1}(x)$ swaps the domain and range.
- A symmetric even function does **not** have an inverse (unless the domain is restricted).
- Only one‑one functions have inverses.

---

# U2 – Simultaneous Equations

## One linear and one non‑linear

Key words:
- **Parabola**: a curve such as the path of something thrown up then down.
- **Turning point** / **stationary point**: a point where the derivative is zero ($f'(x)=0$). In a quadratic function, turning point = stationary point.
- **Discriminant**: $\Delta = b^2-4ac$.

Solve a linear and a non‑linear system:
$$
\begin{cases}
y = x^2 - 5 \\
y = x + 1
\end{cases}
$$
Set $x+1 = x^2-5$ → $x^2 - x - 6 = 0$ → $(x+2)(x-3)=0$ → $x=-2$ or $x=3$.

## Maximum & minimum values of a quadratic function

Quadratic function: $y = ax^2+bx+c$ ($a\neq 0$).  
Its graph is a parabola (cubic functions are **not** parabolas).

- If $a<0$ (concave down), the curve has a **maximum** point.
- If $a>0$ (concave up), the curve has a **minimum** point.
- The maximum or minimum point is called a **turning point** or **stationary point**.

### Forms of a quadratic

| Form | Formula | Information | When to use |
|------|---------|-------------|-------------|
| Simple form | $y = ax^2+bx+c$ | $y$-intercept $(0,c)$, concavity from $a$ | Given three points |
| Vertex form | $y = a(x-h)^2+k$ | Vertex $(h,k)$, symmetry $x=h$, extreme value $k$ | Given vertex and another point; find max/min |
| Factorized form | $y = a(x-p)(x-q)$ | $x$-intercepts $(p,0)$ and $(q,0)$ | Given $x$-intercepts |

### Completing the square (example)

For $y = 2x^2-8x+5$:

1. Factor leading coefficient from first two terms:  
   $y = 2(x^2-4x)+5$.
2. Complete the square inside:  
   $x^2-4x = (x-2)^2 - 4$.
3. Substitute back:  
   $y = 2[(x-2)^2-4] + 5$.
4. Simplify:  
   $y = 2(x-2)^2 - 8 + 5 = 2(x-2)^2 - 3$.

Vertex form: $y = 2(x-2)^2 - 3$ → vertex $(2,-3)$, symmetry $x=2$, minimum value $-3$.

### Example 1: $y = 2x^2+8x+5$

1. $y = 2(x^2+4x)+5$.
2. For $x^2+4x$: half of 4 is 2, square → 4.  
   $x^2+4x = (x^2+4x+4)-4 = (x+2)^2-4$.
3. $y = 2[(x+2)^2-4]+5 = 2(x+2)^2-8+5 = 2(x+2)^2-3$.

Vertex: $(-2,-3)$, minimum value $-3$.

### From simple form to radical roots

1. Write the function.
2. Use discriminant to check roots.
3. Use $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ to find roots and simplify.
4. Write factorized form (if roots are real).

### From vertex form to radical roots

1. Set $y=0$.
2. Take square roots.
3. Write factorized form.

Example:
$$
2(x-2)^2 - 2 = 0 \;\Rightarrow\; (x-2)^2 = 1 \;\Rightarrow\; x-2 = \pm 1
$$
$$
y = 2(x-3)(x-1)
$$

## Graphs of $y=|f(x)|$ where $f(x)$ is quadratic

- Form: $y = |ax^2+bx+c|$.
- Step: reflect the part below the $x$-axis upwards across the $x$-axis (through the zero points).

## Quadratic inequalities

Solve as equalities, then consider direction.

Example: $2x-5 < 9$ → $2x < 14$ → $x < 7$.

## Roots of a quadratic & intersection of a line and a curve

For $ax^2+bx+c=0$:
$$
x = \frac{-b \pm \sqrt{\Delta}}{2a}, \quad \Delta = b^2-4ac
$$

| $\Delta$ | Roots | Line and curve intersection |
|----------|-------|-----------------------------|
| $>0$ | Two distinct real roots | Two distinct points – the line cuts the curve |
| $=0$ | Two equal real roots | One point – the line touches the curve (tangent) |
| $<0$ | No real roots | No intersection – the line does not meet the curve |

Condition for real root(s): $\Delta \ge 0$.

### Factoring with discriminant (example)

Factor $5(x^2-14x-3)$:

$\Delta = (-14)^2 - 4\cdot1\cdot(-3) = 196+12=208$, $\sqrt{208}=4\sqrt{13}$.

$$
x = \frac{14 \pm 4\sqrt{13}}{2} = 7 \pm 2\sqrt{13}
$$
So
$$
x^2-14x-3 = (x - (7+2\sqrt{13}))(x - (7-2\sqrt{13}))
$$
Thus
$$
5(x^2-14x-3) = 5(x-7-2\sqrt{13})(x-7+2\sqrt{13})
$$

Use this method when integer factors are hard to find.

---

# U3 – Factors and Polynomials

## Introduction

A polynomial is of the form:
$$
a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0
$$

## Division of polynomials, factor theorem, remainder theorem

When dividing $P(x)$ by $(x-k)$, we have:
$$
P(x) = (x-k) \cdot Q(x) + R
$$
where $Q(x)$ is the quotient (degree $n-1$) and $R$ is a constant remainder.

### Long division (example: $2x^3-5x^2+3x-4$ divided by $x-2$)

```
        2x^2 - x + 1
x-2 ) 2x^3 - 5x^2 + 3x - 4
      2x^3 - 4x^2
      ----------
            -x^2 + 3x
            -x^2 + 2x
            ----------
                   x - 4
                   x - 2
                   -----
                      -2
```

**Rule (in Chinese and English):**
- Arrange dividend and divisor in descending powers; fill missing terms with 0.
- Divide first term of dividend by first term of divisor → first term of quotient.
- Multiply quotient term by divisor, write below, subtract.
- Bring down next term, repeat until remainder degree < divisor degree.

### Remainder theorem

When $P(x)$ is divided by $(x-r)$, the remainder is $R = P(r)$.

That is:
$$
P(x) = (x-r) \cdot Q(x) + P(r)
$$

**Remainder Theorem Techniques**

| Technique | 中文 | English |
|-----------|------|---------|
| 1 | 若除式为 $ax+b$ ($a\neq1$)，先化为 $x+\frac{b}{a}$ 形式，余数为 $P(-\frac{b}{a})$。 | If the divisor is $ax+b$ ($a\neq1$), rewrite as $x+\frac{b}{a}$; the remainder is $P(-\frac{b}{a})$. |
| 2 | 利用余数定理求未知系数：根据已知余数列方程求解。 | Use the Remainder Theorem to find unknown coefficients: set up an equation from the given remainder. |
| 3 | 余数定理与因式定理结合：若 $P(k)=0$，则 $x-k$ 是因式。 | Combine with the Factor Theorem: if $P(k)=0$, then $x-k$ is a factor. |
| 4 | 若只需求余数，不必做整步除法，直接代入即可。 | If only the remainder is needed, avoid full division; just evaluate $P(k)$. |

### Factor theorem

If $P(r)=0$, then $x-r$ is a factor of $P(x)$, i.e. $P(x) = (x-r) \cdot Q(x)$ and the remainder is $0$.

### Synthetic division

A faster alternative when the divisor is of the form $x-k$.

**Example:** Divide $P(x)=2x^3-5x^2+3x-4$ by $x-2$.

1. Write coefficients: $2, -5, 3, -4$.
2. Write $k=2$ on the left.
3. Bring down first coefficient $2$.
4. Multiply by $k$: $2\times2=4$, add to next: $-5+4=-1$.
5. Multiply: $-1\times2=-2$, add to next: $3+(-2)=1$.
6. Multiply: $1\times2=2$, add to last: $-4+2=-2$ (remainder).

Result: quotient $Q(x)=2x^2-x+1$, remainder $R=-2$.

### Advanced factoring techniques

**Using the Factor Theorem to find roots, then reduce the degree**

For a cubic polynomial $P(x)$:
- Try possible rational roots: $\pm \frac{\text{factor of constant}}{\text{factor of leading coefficient}}$ (e.g., $\pm1,\pm2,\pm\frac12,\dots$).
- Find $r$ such that $P(r)=0$ → $x-r$ is a factor.
- Divide $P(x)$ by $x-r$ (long or synthetic) to obtain a quadratic quotient.
- Factor the quadratic (by inspection, cross-multiplication, or quadratic formula).

**Example:** $P(x)=x^3-6x^2+11x-6$
- Try $x=1$: $P(1)=0$ → factor $x-1$.
- Synthetic division yields $x^2-5x+6$.
- Factor: $(x-2)(x-3)$.
- Final: $P(x)=(x-1)(x-2)(x-3)$.

| Step | Action |
|------|--------|
| 1. Rational Root Test | List possible rational roots; try them until $P(r)=0$. |
| 2. Factor Theorem | If $P(r)=0$, then $x-r$ is a factor. |
| 3. Polynomial Division | Divide $P(x)$ by $x-r$ to get quotient $Q(x)$ (degree one less). |
| 4. Continue Factoring | If $Q(x)$ is quadratic, factor it; if degree ≥3, repeat steps 1–3. |
| 5. Final Form | Write $P(x)=(x-r_1)(x-r_2)\cdots$ (include leading coefficient if needed). |

## Cubic expressions and equations

General form: $f(x)=ax^3+bx^2+cx+d$.

Can use division, factor theorem, remainder theorem.

**Remainder Theorem example:**  
Find remainder when $P(x)=2x^3-5x^2+3x-4$ is divided by $x-2$:
$$
P(2)=2(8)-5(4)+3(2)-4 = 16-20+6-4 = -2
$$

---

# U4 – Equations, Inequalities and Graphs

## Solving equations of the type $|ax+b| = |cx+d|$

$|p| = |q| \iff p^2 = q^2$, so:
$$
ax+b = cx+d \quad \text{OR} \quad ax+b = -(cx+d)
$$
Solve both linear equations, then combine solutions.

- Each absolute value graph is a “V”.
- The number of intersection points of two “V” shapes can be $0$, $1$, $2$, or infinitely many (if the lines coincide).

## Solving modulus inequalities

### With a constant: $|2x+3| > 4$

Algebraic method:
$$
2x+3 < -4 \quad \text{or} \quad 2x+3 > 4
$$

### With two moduli: $|a| > |b|$

Square both sides: $a^2 > b^2$, factorise, solve.

### With a variable inside the modulus

For $|x+1|$:
$$
|x+1| = \begin{cases}
x+1, & x \ge -1 \\
-(x+1), & x < -1
\end{cases}
$$

## Sketching graphs of cubic polynomials and their moduli

A cubic function: $f(x)=ax^3+bx^2+cx+d$ ($a\neq0$).

- If $a>0$: as $x\to -\infty$, $f(x)\to -\infty$; as $x\to +\infty$, $f(x)\to +\infty$.
- If $a<0$: as $x\to -\infty$, $f(x)\to +\infty$; as $x\to +\infty$, $f(x)\to -\infty$.
- Roots and factors: can have one real root or three real roots (including repeated).
- Use Factor Theorem to find a linear factor, then factor the quadratic.
- Derivative: $f'(x)=3ax^2+2bx+c$ – used to find stationary points.
- Sketch: plot $x$-intercepts, $y$-intercept, use sign of $a$ for end behavior.
- Modulus: $y=|f(x)|$ reflects the part below the $x$-axis upward.

For $f(x)=a(x-b)(x-c)(x-d)$:
- If $a>0$, the function increases overall; if $a<0$, it decreases overall.

### Maxima and minima – global (absolute) vs local (relative)

**Example:** $f(x)=x^3-3x$, domain $\mathbb{R}$.
- Local maximum at $x=-1$: $f(-1)=2$ (neighbouring values are less).
- Local minimum at $x=1$: $f(1)=-2$ (neighbouring values are greater).
- Global maximum: none (goes to $+\infty$).
- Global minimum: none (goes to $-\infty$).

If domain is restricted to $[-2,2]$:
- Global maximum: at $x=2$ ($f(2)=2$) and also at $x=-1$ ($2$).
- Global minimum: at $x=1$ ($-2$).

**Finding local extrema:**
1. Find $f'(x)$, solve $f'(x)=0$ to get stationary points.
2. Use $f''(x)$:
   - $f''(x)<0$ → local maximum
   - $f''(x)>0$ → local minimum
3. If $f''(x)=0$, use sign change of $f'$ to decide.

**Finding global extrema on a closed interval $[a,b]$:**
1. Find all stationary points inside the interval.
2. Evaluate $f$ at endpoints $a$ and $b$.
3. Compare values: largest is global max, smallest is global min.

**Common mistakes:**
- Confusing local with global: cubic on $\mathbb{R}$ has no global extrema.
- Forgetting endpoints: on a closed interval, extrema may occur at endpoints.
- Terminology: “local” / “relative” vs “absolute” / “global”.

### Sketching the graph of a cubic function

Convert to factorized form $f(x)=a(x-p)(x-q)(x-r)$ if possible.

1. **General direction:** Use sign of $a$ to determine end behavior.
2. **Intercepts:**
   - $y$-intercept: $f(0)=d$ (simple form) or $a(-p)(-q)(-r)$ (factorized).
   - $x$-intercepts: from factorized form directly; from simple form use Factor Theorem to find one root, then long division, then solve quadratic.
   - At a double root, the graph is tangent to the $x$-axis (touches but does not cross).
3. **Stationary points:** Solve $f'(x)=3ax^2+2bx+c=0$ to find $x$-coordinates of turning points. Use $f''(x)$ to classify (optional). Substitute back to find $y$-coordinates.
4. **Additional points:** Choose a few $x$ values to refine the shape.
5. **Draw:** Connect smoothly from left to right, passing through all intercepts and turning points. The curve is differentiable everywhere (no sharp corners).
