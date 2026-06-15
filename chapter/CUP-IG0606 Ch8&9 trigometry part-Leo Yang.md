>not classified by course book.
- 这份笔记由 LG-leo 整理和维护。如果你觉得这份笔记对你有帮助，欢迎在 GitHub 上关注我或给我一个 ⭐，这能帮助我持续产出更多免费的学习资源。
- 我的其他课程笔记：https://github.com/LG-leo?tab=repositories
- This note is maintained by LG-leo. If you find it helpful, feel free to follow me or leave a ⭐ on GitHub. It helps me keep producing more free study resources. Check out my other notes: https://github.com/LG-leo?tab=repositories
# U8 Circular Measure (弧度制)

## 8.1 Radian Measure

### 8.1.1 Basic Formulas

$$
s = r\theta, \quad A = \frac{1}{2}r^2\theta
$$

where $\theta$ must be in radians, $s$ is arc length, $A$ is sector area.

**Conversion between degrees and radians**:

$$
180^\circ = \pi\ \text{rad} \quad\Rightarrow\quad 1^\circ = \frac{\pi}{180}\ \text{rad},\quad 1\ \text{rad} = \frac{180}{\pi}^\circ
$$

---

### 8.1.2 Basic Problems: Given radius and angle, find arc length or sector area

**Steps**:
1. If the angle is given in degrees, convert to radians: $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$.
2. Substitute into $s = r\theta$ or $A = \frac{1}{2}r^2\theta$.

**Example**: Radius 5 cm, central angle $60^\circ$. Find arc length and sector area.
- Convert: $60 \times \frac{\pi}{180} = \frac{\pi}{3}$ rad.
- Arc length: $s = 5 \times \frac{\pi}{3} = \frac{5\pi}{3}$ cm.
- Sector area: $A = \frac12 \times 25 \times \frac{\pi}{3} = \frac{25\pi}{6}$ cm².

**Pitfall**: Do not use degrees in the formulas; they require radians.

---

### 8.1.3 Composite Shapes (Sectors with Triangles or Polygons)

**Type**: Find the perimeter or area of a shape made of a sector and other polygons.

**Steps**:
1. Break the shape into basic parts (sector, triangle, rectangle, etc.).
2. Compute each part’s arc length, side lengths, area. Watch for overlapping edges.
3. Add or subtract as required.

**Example**: A shape consists of a sector of radius $r$ and central angle $\theta$ together with the triangle formed by the two radii. Find total area and perimeter.
- Sector area: $A_{\text{sector}} = \frac12 r^2\theta$.
- Triangle area: $A_{\triangle} = \frac12 r^2\sin\theta$ (if the included angle is $\theta$).
- Total area: $A_{\text{total}} = \frac12 r^2\theta + \frac12 r^2\sin\theta$.
- Perimeter: two radii $2r$ + arc length $r\theta$ + chord length $= 2r\sin\frac{\theta}{2}$ (if the third side is the chord).

> **Note**: If the shape is a segment (sector minus triangle), subtract the triangle area.

---

# U9 Trigonometry (三角函数)

## 9.1 Trigonometric Functions – Basics

### 9.1.1 The Unit Circle

The **unit circle** is a circle of radius $1$ centred at the origin $O(0,0)$.  
For any angle $\theta$ measured anti‑clockwise from the positive $x$-axis, let $P(x,y)$ be the point where the terminal side of $\theta$ meets the unit circle.

#### Coordinates on the unit circle

$$
\boxed{P = (\cos\theta,\ \sin\theta)}
$$

That is:
- $x = \cos\theta$ — the horizontal coordinate
- $y = \sin\theta$ — the vertical coordinate

From this we immediately get the **range** of sine and cosine:

$$
-1 \le \sin\theta \le 1,\qquad -1 \le \cos\theta \le 1
$$

#### Tangent from the unit circle

$$
\tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}\quad (x \neq 0)
$$

Geometrically, $\tan\theta$ is the **slope** of the radius $OP$, or the $y$-coordinate of the intersection of the line $OP$ with the vertical line $x=1$ (the tangent line to the circle at $(1,0)$).

#### Reciprocal functions

Each basic function has a reciprocal:

| Function | Reciprocal | Notation | Domain restriction |
|----------|------------|----------|-------------------|
| $\sin\theta$ | $\displaystyle\frac{1}{\sin\theta}$ | $\csc\theta$ (cosecant, also written $\operatorname{cosec}\theta$ in CIE 0606) | $\sin\theta \neq 0$ |
| $\cos\theta$ | $\displaystyle\frac{1}{\cos\theta}$ | $\sec\theta$ (secant) | $\cos\theta \neq 0$ |
| $\tan\theta$ | $\displaystyle\frac{1}{\tan\theta}$ | $\cot\theta$ (cotangent) | $\tan\theta \neq 0$ |

In terms of the unit circle point $P(x,y)$:

$$
\csc\theta = \frac{1}{y}\ (y\neq 0),\qquad
\sec\theta = \frac{1}{x}\ (x\neq 0),\qquad
\cot\theta = \frac{x}{y}\ (y\neq 0)
$$

> **Remember**: reciprocal functions are **not** the same as inverse functions ($\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$).  
> $\csc\theta = \frac{1}{\sin\theta}$ (reciprocal), but $\sin^{-1}x$ (inverse) means "the angle whose sine is $x$".

#### Sign of trig functions in each quadrant (ASTC)

The unit circle is divided into **four quadrants**. The sign of each trig function depends on which quadrant $\theta$ lies in:

```
        y
        |
   II   |   I
  (-,+) |   (+,+)
        |
--------+-------- x
        |
  III   |   IV
 (-,-)  |   (+,-)
        |
```

| Quadrant | Range | $\sin$ | $\cos$ | $\tan$ | Mnemonic |
|:--------:|-------|:------:|:------:|:------:|:--------:|
| **I** | $0 < \theta < \frac{\pi}{2}$ | $+$ | $+$ | $+$ | **A**ll positive |
| **II** | $\frac{\pi}{2} < \theta < \pi$ | $+$ | $-$ | $-$ | **S**ine positive |
| **III** | $\pi < \theta < \frac{3\pi}{2}$ | $-$ | $-$ | $+$ | **T**angent positive |
| **IV** | $\frac{3\pi}{2} < \theta < 2\pi$ | $-$ | $+$ | $-$ | **C**osine positive |

**ASTC rule**: **A**ll – **S**ine – **T**angent – **C**osine (read anti‑clockwise from QI).

The reciprocal functions share the same sign as their base function:
- $\csc\theta$ has the same sign as $\sin\theta$
- $\sec\theta$ has the same sign as $\cos\theta$
- $\cot\theta$ has the same sign as $\tan\theta$

---

### 9.1.2 Special Angle Values (Must Memorise)

| Degrees | 0° | 30° | 45° | 60° | 90° | 180° | 270° | 360° |
|---------|----|----|----|----|----|----|----|----|
| Radians | 0 | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ | $\pi$ | $3\pi/2$ | $2\pi$ |
| $\sin$ | 0 | $1/2$ | $\sqrt{2}/2$ | $\sqrt{3}/2$ | 1 | 0 | -1 | 0 |
| $\cos$ | 1 | $\sqrt{3}/2$ | $\sqrt{2}/2$ | $1/2$ | 0 | -1 | 0 | 1 |
| $\tan$ | 0 | $1/\sqrt{3}$ | 1 | $\sqrt{3}$ | undefined | 0 | undefined | 0 |

---

### 9.1.3 Given One Trig Value, Find Others

**Steps**:
1. Use $\sin^2\theta + \cos^2\theta = 1$ to find the other sine/cosine.
2. Use $\tan\theta = \frac{\sin\theta}{\cos\theta}$ to find tangent.
3. Reciprocal functions: $\sec\theta = 1/\cos\theta$, etc.
4. **Determine sign using the quadrant**.

**Example**: $\sin\theta = \frac{3}{5}$ and $\theta$ is in quadrant II. Find $\cos\theta$ and $\tan\theta$.
- $\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$ → $\cos\theta = \pm\frac{4}{5}$.
- In quadrant II, cosine is negative → $\cos\theta = -\frac{4}{5}$.
- $\tan\theta = \frac{3/5}{-4/5} = -\frac{3}{4}$.

**Pitfall**: Forgetting the quadrant leads to wrong sign.

---

## 9.2 Graphs and Properties

### 9.2.1 Basic Graphs

| Function | Period | Parity | Zeros | Asymptotes | Range |
|----------|--------|--------|-------|------------|-------|
| $\sin x$ | $2\pi$ | odd | $k\pi$ | none | $[-1,1]$ |
| $\cos x$ | $2\pi$ | even | $\frac{\pi}{2}+k\pi$ | none | $[-1,1]$ |
| $\tan x$ | $\pi$ | odd | $k\pi$ | $x=\frac{\pi}{2}+k\pi$ | $\mathbb{R}$ |

---

## General Form
For a sine or cosine function:
$$
y = a\sin(bx + c) + d
$$
or
$$
y = a\cos(bx + c) + d
$$

- Amplitude: $|a|$ – the maximum vertical distance from the equilibrium line $y = d$.
- Period: $2\pi / |b|$ (for sine/cosine); for tangent: $\pi / |b|$.
- Phase shift: $-c / b$ (right if positive, left if negative).
- Vertical shift: $d$.

---

## Example: $y = 3\sin(2x + 6) + 4$

### 1. Amplitude
$$
Amplitude = |a| = |3| = 3
$$
The graph oscillates 3 units above and below the line $y = 4$.

### 2. y‑intercept
Set $x = 0$:
$$
y(0) = 3\sin(6) + 4
$$
Here $6$ is in radians.  
$\sin 6 \approx -0.2794$ (because $6$ rad is about $343.8$ degrees).  
$$
y(0) \approx 3 \times (-0.2794) + 4 = -0.8382 + 4 = 3.1618 \approx 3
$$
So the graph crosses the y‑axis near $y = 3$.

### 3. Maximum and Minimum Values
The sine function ranges from $-1$ to $1$. Thus:
$$
3\sin(2x + 6) \in [-3, 3]
$$
Adding the vertical shift $d = 4$:
$$
y \in [1, 7]
$$
- Maximum: when $\sin(2x + 6) = 1$,  
  $y_{\max} = 3 \times 1 + 4 = 7$.
- Minimum: when $\sin(2x + 6) = -1$,  
  $y_{\min} = 3 \times (-1) + 4 = 1$.

The extreme values depend only on the amplitude and vertical shift, not on the phase shift.

### 4. Phase Shift
Rewrite the argument:
$$
2x + 6 = 2(x + 3)
$$
Then $y = 3\sin(2(x+3)) + 4$.  
The graph of $y = 3\sin(2x) + 4$ is shifted left by 3 units (because $x$ is replaced by $x+3$).  
Check using the formula:
$$
-c/b = -6/2 = -3 \quad\text{(negative means left shift)}
$$

---

## Key Points
- Amplitude = $|a|$
- Period = $2\pi / |b|$ (sine/cosine)
- Phase shift = $-c / b$ (positive → right, negative → left)
- Vertical shift = $d$
- Maximum value = $|a| + d$
- Minimum value = $-|a| + d$

These formulas work for cosine as well. For tangent, the period is $\pi / |b|$ and there is no amplitude (the range is all real numbers).
---

### 9.2.3 Determine Equation from Graph

**Example**: Graph has maximum $(0,3)$ and minimum $(\pi, -1)$. Find the equation.

**Steps**:
- Amplitude $a = \frac{3-(-1)}{2} = 2$.
- Vertical shift $d = \frac{3+(-1)}{2} = 1$.
- From max to min is half period: $\frac{T}{2} = \pi$ → $T=2\pi$ → $b=1$.
- Assume $y = 2\sin(x+c)+1$. Plug $(0,3)$: $3=2\sin c+1$ → $\sin c=1$ → $c=\frac{\pi}{2}$.
- Equation: $y = 2\sin(x+\frac{\pi}{2})+1 = 2\cos x+1$.

**Pitfall**: Decide whether to use sine or cosine; both work with different phase shifts.

---

## 9.3 Trigonometric Identities

### 9.3.1 Core Identities (given in formula sheet)

$$
\sin^2\theta + \cos^2\theta = 1
$$
$$
\sec^2\theta = 1 + \tan^2\theta,\qquad \csc^2\theta = 1 + \cot^2\theta
$$
$$
\tan\theta = \frac{\sin\theta}{\cos\theta},\quad \cot\theta = \frac{\cos\theta}{\sin\theta}
$$

---

### 9.3.2 Simplifying Trigonometric Expressions

**General strategy**:
1. Convert everything to $\sin x$ and $\cos x$ (using $\tan x = \frac{\sin x}{\cos x}$, $\sec x = \frac{1}{\cos x}$, etc.).
2. Use $\sin^2 x + \cos^2 x = 1$ (or its siblings $1+\tan^2 x = \sec^2 x$, $1+\cot^2 x = \csc^2 x$).
3. Combine fractions over a common denominator.
4. Factorise and cancel where possible.

---

#### Example 1: Basic — combine fractions

Simplify $\displaystyle\frac{\sin x}{1+\cos x} + \frac{1+\cos x}{\sin x}$.

**Solution**:

Common denominator $\sin x(1+\cos x)$:

$$
\frac{\sin^2 x + (1+\cos x)^2}{\sin x(1+\cos x)}
$$

Expand numerator:

$$
\sin^2 x + 1 + 2\cos x + \cos^2 x
= (\sin^2 x+\cos^2 x) + 1 + 2\cos x
= 2 + 2\cos x
$$

Factor $2(1+\cos x)$ and cancel $(1+\cos x)$:

$$
\frac{2(1+\cos x)}{\sin x(1+\cos x)} = \frac{2}{\sin x} = 2\csc x
$$

---

#### Example 2: Use identity $1+\tan^2 x = \sec^2 x$

Simplify $\displaystyle\frac{\sec^2 x - 1}{\sec^2 x}$.

**Solution**:

Method 1 — use $1+\tan^2 x = \sec^2 x$ directly:

$$
\frac{\sec^2 x - 1}{\sec^2 x} = \frac{\tan^2 x}{\sec^2 x}
= \frac{\frac{\sin^2 x}{\cos^2 x}}{\frac{1}{\cos^2 x}}
= \frac{\sin^2 x}{\cos^2 x} \cdot \frac{\cos^2 x}{1}
= \sin^2 x
$$

Method 2 — split the fraction:

$$
\frac{\sec^2 x}{\sec^2 x} - \frac{1}{\sec^2 x}
= 1 - \cos^2 x = \sin^2 x
$$

---

#### Example 3: Factor and cancel

Simplify $\displaystyle\frac{\sin^2 x - 1}{\tan x \sin x - \tan x}$.

**Solution**:

Numerator: $\sin^2 x - 1 = -(1 - \sin^2 x) = -\cos^2 x$.

Denominator: $\tan x(\sin x - 1) = \frac{\sin x}{\cos x}(\sin x - 1)$.

So:

$$
\frac{-\cos^2 x}{\frac{\sin x}{\cos x}(\sin x - 1)}
= -\cos^2 x \cdot \frac{\cos x}{\sin x(\sin x - 1)}
= -\frac{\cos^3 x}{\sin x(\sin x - 1)}
$$

This doesn't simplify further — but if the original was $\frac{\sin^2 x - 1}{\tan x \sin x - \tan x}$, we can also note $\sin^2 x - 1 = -(\sin x - 1)(\sin x + 1)$, giving:

$$
\frac{-(\sin x - 1)(\sin x + 1)}{\tan x(\sin x - 1)}
= -\frac{\sin x + 1}{\tan x}
= -\frac{\sin x + 1}{\frac{\sin x}{\cos x}}
= -(\sin x + 1) \cdot \frac{\cos x}{\sin x}
= -\frac{\cos x(\sin x + 1)}{\sin x}
$$

Both forms are equivalent.

---

#### Example 4: Using $\csc^2 x = 1 + \cot^2 x$

Simplify $\displaystyle\frac{\csc^2 x - \cot^2 x}{\cos x}$.

**Solution**:

Since $\csc^2 x - \cot^2 x = 1$ (from $1+\cot^2 x = \csc^2 x$), we get:

$$
\frac{1}{\cos x} = \sec x
$$

---

### 9.3.3 Proving Trigonometric Identities

**What is a "proof"?**  
You start from one side of the equation and, using only algebraic manipulation and known identities, transform it into exactly the other side. You **cannot** move terms across the $=$ sign (that would assume the statement is already true).

---

#### General strategy (step‑by‑step)

| Step | What to do |
|:----:|------------|
| 1 | **Pick the harder side** — start from the side that looks more complicated. |
| 2 | **Convert to $\sin$ and $\cos$** — replace $\tan$, $\cot$, $\sec$, $\csc$ with their $\sin$/$\cos$ forms. |
| 3 | **Apply Pythagorean identities** — look for $\sin^2 + \cos^2 = 1$, $1+\tan^2 = \sec^2$, $1+\cot^2 = \csc^2$. |
| 4 | **Algebraic manipulation** — factor, expand, combine fractions, find common denominators. |
| 5 | **Simplify** — cancel common factors, rewrite as a single trig function. |
| 6 | **Reach the other side** — once you arrive at the RHS (or LHS), you are done. |

---

#### Worked Examples (increasing difficulty)

---

##### Example 1: Basic — convert to $\sin$ and $\cos$

Prove $\displaystyle\tan x + \cot x = \sec x \csc x$.

**Proof**:

$$
\text{LHS} = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}
= \frac{\sin^2 x + \cos^2 x}{\sin x \cos x}
= \frac{1}{\sin x \cos x}
= \frac{1}{\cos x} \cdot \frac{1}{\sin x}
= \sec x \csc x = \text{RHS}
$$

---

##### Example 2: Factor a difference of squares

Prove $\displaystyle\frac{1 - \sin^2 x}{1 - \sin x} = 1 + \sin x$.

**Proof**:

$$
\text{LHS} = \frac{\cos^2 x}{1 - \sin x}
= \frac{(1 - \sin x)(1 + \sin x)}{1 - \sin x}
= 1 + \sin x = \text{RHS}
$$

(Using $1 - \sin^2 x = \cos^2 x$, then factorising as difference of squares.)

---

##### Example 3: Combine two fractions

Prove $\displaystyle\frac{1}{1 - \sin x} + \frac{1}{1 + \sin x} = 2\sec^2 x$.

**Proof**:

$$
\begin{aligned}
\text{LHS}
&= \frac{(1 + \sin x) + (1 - \sin x)}{(1 - \sin x)(1 + \sin x)}
= \frac{2}{1 - \sin^2 x} \\[4pt]
&= \frac{2}{\cos^2 x}
= 2 \cdot \frac{1}{\cos^2 x}
= 2\sec^2 x = \text{RHS}
\end{aligned}
$$

---

##### Example 4: Use $\sec^2 x = 1 + \tan^2 x$

Prove $\displaystyle\frac{\sec^2 x}{\tan x} = \frac{1}{\sin x \cos x}$.

**Proof**:

$$
\begin{aligned}
\text{LHS}
&= \frac{1 + \tan^2 x}{\tan x}
= \frac{1}{\tan x} + \frac{\tan^2 x}{\tan x}
= \cot x + \tan x \\[4pt]
&= \frac{\cos x}{\sin x} + \frac{\sin x}{\cos x}
= \frac{\cos^2 x + \sin^2 x}{\sin x \cos x}
= \frac{1}{\sin x \cos x} = \text{RHS}
\end{aligned}
$$

---

##### Example 5: Multiply by the conjugate

Prove $\displaystyle\frac{\sin x}{1 + \cos x} + \frac{1 + \cos x}{\sin x} = 2\csc x$.

**Proof**:

$$
\begin{aligned}
\text{LHS}
&= \frac{\sin^2 x + (1 + \cos x)^2}{\sin x(1 + \cos x)} \\[4pt]
&= \frac{\sin^2 x + 1 + 2\cos x + \cos^2 x}{\sin x(1 + \cos x)} \\[4pt]
&= \frac{(\sin^2 x + \cos^2 x) + 1 + 2\cos x}{\sin x(1 + \cos x)} \\[4pt]
&= \frac{2 + 2\cos x}{\sin x(1 + \cos x)}
= \frac{2(1 + \cos x)}{\sin x(1 + \cos x)} \\[4pt]
&= \frac{2}{\sin x} = 2\csc x = \text{RHS}
\end{aligned}
$$

---

##### Example 6: Combine with Pythagorean substitution

Prove $\displaystyle\frac{\cos x}{1 - \tan x} + \frac{\sin x}{1 - \cot x} = \sin x + \cos x$.

**Proof**:

Rewrite each denominator:

$$
1 - \tan x = 1 - \frac{\sin x}{\cos x} = \frac{\cos x - \sin x}{\cos x}
$$

$$
1 - \cot x = 1 - \frac{\cos x}{\sin x} = \frac{\sin x - \cos x}{\sin x}
$$

So:

$$
\begin{aligned}
\text{LHS}
&= \cos x \cdot \frac{\cos x}{\cos x - \sin x}
\;+\; \sin x \cdot \frac{\sin x}{\sin x - \cos x} \\[4pt]
&= \frac{\cos^2 x}{\cos x - \sin x} + \frac{\sin^2 x}{\sin x - \cos x} \\[4pt]
&= \frac{\cos^2 x}{\cos x - \sin x} - \frac{\sin^2 x}{\cos x - \sin x} \\[4pt]
&= \frac{\cos^2 x - \sin^2 x}{\cos x - \sin x}
= \frac{(\cos x - \sin x)(\cos x + \sin x)}{\cos x - \sin x} \\[4pt]
&= \cos x + \sin x = \text{RHS}
\end{aligned}
$$

---

##### Example 7: Using $1 + \tan^2 x = \sec^2 x$ cleverly

Prove $\displaystyle\sqrt{\frac{1 - \sin x}{1 + \sin x}} = \sec x - \tan x$ (for $0 < x < \frac{\pi}{2}$).

**Proof**:

Multiply numerator and denominator inside the square root by $1 - \sin x$:

$$
\frac{1 - \sin x}{1 + \sin x} \cdot \frac{1 - \sin x}{1 - \sin x}
= \frac{(1 - \sin x)^2}{1 - \sin^2 x}
= \frac{(1 - \sin x)^2}{\cos^2 x}
$$

Take the square root (positive since $0 < x < \frac{\pi}{2}$):

$$
\sqrt{\frac{(1 - \sin x)^2}{\cos^2 x}}
= \frac{1 - \sin x}{\cos x}
= \frac{1}{\cos x} - \frac{\sin x}{\cos x}
= \sec x - \tan x = \text{RHS}
$$

---

### 9.3.4 Practice Questions (with answers)

Try these yourself before looking at the answers.

**Q1.** Simplify $\displaystyle\frac{\sin^2 x}{1 + \cos x}$.

<details>
<summary>Answer</summary>

$$
\frac{\sin^2 x}{1 + \cos x}
= \frac{1 - \cos^2 x}{1 + \cos x}
= \frac{(1 - \cos x)(1 + \cos x)}{1 + \cos x}
= 1 - \cos x
$$
</details>

---

**Q2.** Prove $\displaystyle\frac{1}{\sin x \cos x} - \frac{\cos x}{\sin x} = \tan x$.

<details>
<summary>Answer</summary>

$$
\begin{aligned}
\text{LHS}
&= \frac{1}{\sin x \cos x} - \frac{\cos x}{\sin x}
= \frac{1}{\sin x \cos x} - \frac{\cos^2 x}{\sin x \cos x} \\[4pt]
&= \frac{1 - \cos^2 x}{\sin x \cos x}
= \frac{\sin^2 x}{\sin x \cos x}
= \frac{\sin x}{\cos x} = \tan x = \text{RHS}
\end{aligned}
$$
</details>

---

**Q3.** Prove $\displaystyle\frac{1 + \sin x}{\cos x} + \frac{\cos x}{1 + \sin x} = 2\sec x$.

<details>
<summary>Answer</summary>

$$
\begin{aligned}
\text{LHS}
&= \frac{(1 + \sin x)^2 + \cos^2 x}{\cos x(1 + \sin x)} \\[4pt]
&= \frac{1 + 2\sin x + \sin^2 x + \cos^2 x}{\cos x(1 + \sin x)} \\[4pt]
&= \frac{2 + 2\sin x}{\cos x(1 + \sin x)}
= \frac{2(1 + \sin x)}{\cos x(1 + \sin x)}
= \frac{2}{\cos x} = 2\sec x = \text{RHS}
\end{aligned}
$$
</details>

---

**Q4.** Prove $\displaystyle\tan^2 x - \sin^2 x = \tan^2 x \sin^2 x$.

<details>
<summary>Answer</summary>

$$
\begin{aligned}
\text{LHS}
&= \frac{\sin^2 x}{\cos^2 x} - \sin^2 x
= \sin^2 x\left(\frac{1}{\cos^2 x} - 1\right) \\[4pt]
&= \sin^2 x (\sec^2 x - 1)
= \sin^2 x \cdot \tan^2 x = \text{RHS}
\end{aligned}
$$
</details>

---

**Q5.** Prove $\displaystyle\sec^4 x - \sec^2 x = \tan^4 x + \tan^2 x$.

<details>
<summary>Answer</summary>

$$
\begin{aligned}
\text{LHS}
&= \sec^2 x (\sec^2 x - 1)
= (1 + \tan^2 x)(\tan^2 x) \\[4pt]
&= \tan^2 x + \tan^4 x = \text{RHS}
\end{aligned}
$$
</details>

---

**Q6.** Prove $\displaystyle\frac{\sin x}{1 + \cos x} = \frac{1 - \cos x}{\sin x}$.

<details>
<summary>Answer</summary>

Method — cross-multiply or combine:

$$
\frac{\sin x}{1 + \cos x} \cdot \frac{1 - \cos x}{1 - \cos x}
= \frac{\sin x(1 - \cos x)}{1 - \cos^2 x}
= \frac{\sin x(1 - \cos x)}{\sin^2 x}
= \frac{1 - \cos x}{\sin x} = \text{RHS}
$$
</details>

---

**Q7.** (Challenge) Prove $\displaystyle\frac{\sec x + \csc x}{1 + \tan x} = \csc x$.

<details>
<summary>Answer</summary>

$$
\begin{aligned}
\text{LHS}
&= \frac{\frac{1}{\cos x} + \frac{1}{\sin x}}{1 + \frac{\sin x}{\cos x}}
= \frac{\frac{\sin x + \cos x}{\sin x \cos x}}{\frac{\cos x + \sin x}{\cos x}} \\[4pt]
&= \frac{\sin x + \cos x}{\sin x \cos x} \cdot \frac{\cos x}{\sin x + \cos x}
= \frac{1}{\sin x} = \csc x = \text{RHS}
\end{aligned}
$$
</details>

---

#### Quick tips summary

| Technique | When to use | Example |
|-----------|-------------|---------|
| Convert to $\sin$, $\cos$ | Almost always the first step | Ex. 1, 2, 3 |
| Pythagorean identities | Replace $\sin^2 + \cos^2$, $1+\tan^2$, $1+\cot^2$ | Ex. 3, 4 |
| Factor / expand | Look for common factors or difference of squares | Ex. 2, 4 |
| Combine fractions | When you have a sum/difference of fractions | Ex. 3, 5 |
| Multiply by conjugate | Useful when $1 \pm \sin x$ or $1 \pm \cos x$ appears | Ex. 7, Q6 |
| Split a fraction | Write $\frac{a+b}{c} = \frac{a}{c} + \frac{b}{c}$ | Ex. 2 (method 2) |

---

## 9.4 Solving Trigonometric Equations

### 9.4.1 Basic Forms

#### (i) $\sin x = a$

**Steps**:
- Find principal value $x_0 = \arcsin a$ (usually acute, $-\frac{\pi}{2} \le x_0 \le \frac{\pi}{2}$).
- In $[0,2\pi)$: solutions are $x_0$ and $\pi - x_0$.
- General solution: $x = x_0 + 2k\pi$ or $x = \pi - x_0 + 2k\pi$, $k \in \mathbb{Z}$.
- If $a<0$, $x_0$ is negative; add $2\pi$ to get a solution in $[0,2\pi)$.

**Example 1**: $\sin x = \frac12$, $0\le x<2\pi$.
- $x_0 = \frac{\pi}{6}$, so $x = \frac{\pi}{6}$ or $x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$.
- **Answer**: $x = \frac{\pi}{6},\ \frac{5\pi}{6}$.

**Example 2**: $\sin x = -\frac{\sqrt{3}}{2}$, $0\le x<2\pi$.
- $\arcsin\frac{\sqrt{3}}{2} = \frac{\pi}{3}$, so $x_0 = -\frac{\pi}{3}$ (negative because $\sin$ is negative in QIII/IV).
- In $[0,2\pi)$: $x = \pi - (-\frac{\pi}{3}) = \frac{4\pi}{3}$ or $x = 2\pi + (-\frac{\pi}{3}) = \frac{5\pi}{3}$.
- **Answer**: $x = \frac{4\pi}{3},\ \frac{5\pi}{3}$.

**Example 3**: $\sin x = 0.4$, $0\le x<2\pi$ (use calculator).
- $x_0 = \arcsin 0.4 \approx 0.4115$ rad.
- Second solution: $\pi - 0.4115 \approx 2.7301$ rad.
- **Answer**: $x \approx 0.4115,\ 2.7301$.

---

#### (ii) $\cos x = a$

**Steps**:
- Principal value $x_0 = \arccos a$ (in $[0,\pi]$).
- In $[0,2\pi)$: solutions are $x_0$ and $2\pi - x_0$.
- General: $x = \pm x_0 + 2k\pi$, $k \in \mathbb{Z}$.

**Example 1**: $\cos x = -\frac12$, $0\le x<2\pi$.
- $x_0 = \arccos(-\frac12) = \frac{2\pi}{3}$.
- $2\pi - \frac{2\pi}{3} = \frac{4\pi}{3}$.
- **Answer**: $x = \frac{2\pi}{3},\ \frac{4\pi}{3}$.

**Example 2**: $\cos x = \frac{1}{\sqrt{2}}$, $0\le x<2\pi$.
- $x_0 = \arccos\frac{1}{\sqrt{2}} = \frac{\pi}{4}$.
- $2\pi - \frac{\pi}{4} = \frac{7\pi}{4}$.
- **Answer**: $x = \frac{\pi}{4},\ \frac{7\pi}{4}$.

---

#### (iii) $\tan x = a$

**Steps**:
- Principal value $x_0 = \arctan a$ (in $(-\frac{\pi}{2},\frac{\pi}{2})$).
- Period $\pi$: general solution $x = x_0 + k\pi$, $k \in \mathbb{Z}$.
- In $[0,2\pi)$: add $k\pi$ until you have all solutions in range.

**Example 1**: $\tan x = \sqrt{3}$, $0\le x<2\pi$.
- $x_0 = \frac{\pi}{3}$.
- $x = \frac{\pi}{3} + 0\pi = \frac{\pi}{3}$; $x = \frac{\pi}{3} + \pi = \frac{4\pi}{3}$.
- **Answer**: $x = \frac{\pi}{3},\ \frac{4\pi}{3}$.

**Example 2**: $\tan x = -1$, $0\le x<2\pi$.
- $x_0 = \arctan(-1) = -\frac{\pi}{4}$.
- Add $\pi$: $-\frac{\pi}{4}+\pi = \frac{3\pi}{4}$; $-\frac{\pi}{4}+2\pi = \frac{7\pi}{4}$.
- **Answer**: $x = \frac{3\pi}{4},\ \frac{7\pi}{4}$.

---

### 9.4.2 Equations Involving Multiple Angles ($\sin 2x$, $\cos 3x$, etc.)

When the angle is $ax + b$ instead of $x$, the key is to **adjust the range** first.

**Steps**:
1. Let $u = ax + b$.
2. Rewrite the range of $x$ as a range for $u$.
3. Solve $\sin u = a$ (or $\cos u = a$, $\tan u = a$) in the $u$ range.
4. Convert each $u$ solution back to $x = \frac{u - b}{a}$.

#### Example 1: $\sin 2x = \frac12$, $0 \le x < 2\pi$.

Let $u = 2x$. Since $0 \le x < 2\pi$, we have $0 \le u < 4\pi$.

$\sin u = \frac12$ in $[0,4\pi)$:
- $u = \frac{\pi}{6},\ \frac{5\pi}{6}$ (first cycle)
- Add $2\pi$: $u = \frac{\pi}{6}+2\pi = \frac{13\pi}{6},\ \frac{5\pi}{6}+2\pi = \frac{17\pi}{6}$.

Now $x = \frac{u}{2}$:
$$
x = \frac{\pi}{12},\ \frac{5\pi}{12},\ \frac{13\pi}{12},\ \frac{17\pi}{12}.
$$

#### Example 2: $\cos(3x - \frac{\pi}{4}) = -\frac{\sqrt{2}}{2}$, $0 \le x < 2\pi$.

Let $u = 3x - \frac{\pi}{4}$. Range: $0 \le x < 2\pi \Rightarrow -\frac{\pi}{4} \le u < 6\pi - \frac{\pi}{4}$.

$\cos u = -\frac{\sqrt{2}}{2}$:
- $u_0 = \arccos(-\frac{\sqrt{2}}{2}) = \frac{3\pi}{4}$.
- Solutions in $[0,2\pi)$: $u = \frac{3\pi}{4},\ 2\pi - \frac{3\pi}{4} = \frac{5\pi}{4}$.
- Extend to the full $u$ range by adding $2\pi$ multiples:
  - $\frac{3\pi}{4},\ \frac{3\pi}{4}+2\pi = \frac{11\pi}{4},\ \frac{3\pi}{4}+4\pi = \frac{19\pi}{4}$
  - $\frac{5\pi}{4},\ \frac{5\pi}{4}+2\pi = \frac{13\pi}{4},\ \frac{5\pi}{4}+4\pi = \frac{21\pi}{4}$
- (Check which lie in $[-\frac{\pi}{4}, 6\pi-\frac{\pi}{4})$.)

Now $x = \frac{u + \frac{\pi}{4}}{3}$:
$$
x = \frac{\pi}{3},\ \frac{\pi}{2},\ \pi,\ \frac{7\pi}{6},\ \frac{5\pi}{3},\ \frac{11\pi}{6}.
$$

#### Example 3: $\tan 2x = 1$, $0 \le x < \pi$.

Let $u = 2x$, so $0 \le u < 2\pi$.

$\tan u = 1$: $u_0 = \frac{\pi}{4}$, period $\pi$.
- $u = \frac{\pi}{4},\ \frac{\pi}{4}+\pi = \frac{5\pi}{4}$.

$x = \frac{u}{2}$:
$$
x = \frac{\pi}{8},\ \frac{5\pi}{8}.
$$

---

### 9.4.3 Reducible to Quadratic Form

**Steps**:
1. Let $t = \sin x$ (or $\cos x$, $\tan x$).
2. Solve the quadratic $at^2 + bt + c = 0$.
3. For each solution $t$, solve $\sin x = t$ (or $\cos x = t$, $\tan x = t$).
4. **Check**: for $\sin$ and $\cos$, discard $t$ outside $[-1,1]$.
5. Find all solutions in the given interval.

#### Example 1: Basic quadratic

$2\sin^2 x + \sin x - 1 = 0$, $0\le x<2\pi$.

- Let $t = \sin x$: $2t^2 + t - 1 = 0 \Rightarrow (2t-1)(t+1)=0 \Rightarrow t = \frac12$ or $t = -1$.
- $\sin x = \frac12 \Rightarrow x = \frac{\pi}{6},\ \frac{5\pi}{6}$.
- $\sin x = -1 \Rightarrow x = \frac{3\pi}{2}$.
- **Answer**: $x = \frac{\pi}{6},\ \frac{5\pi}{6},\ \frac{3\pi}{2}$.

#### Example 2: Using $\cos^2 x = 1 - \sin^2 x$

$3\cos^2 x - \sin x - 1 = 0$, $0\le x<2\pi$.

- Replace $\cos^2 x$: $3(1 - \sin^2 x) - \sin x - 1 = 0 \Rightarrow 3 - 3\sin^2 x - \sin x - 1 = 0$.
- Simplify: $-3\sin^2 x - \sin x + 2 = 0 \Rightarrow 3\sin^2 x + \sin x - 2 = 0$.
- Let $t = \sin x$: $3t^2 + t - 2 = 0 \Rightarrow (3t-2)(t+1)=0 \Rightarrow t = \frac23$ or $t = -1$.
- $\sin x = \frac23 \Rightarrow x = \arcsin\frac23 \approx 0.7297$, and $x = \pi - 0.7297 \approx 2.4119$.
- $\sin x = -1 \Rightarrow x = \frac{3\pi}{2}$.
- **Answer**: $x \approx 0.7297,\ 2.4119,\ \frac{3\pi}{2}$.

#### Example 3: Discarding invalid solutions

$2\cos^2 x + 3\cos x - 2 = 0$, $0\le x<2\pi$.

- Let $t = \cos x$: $2t^2 + 3t - 2 = 0 \Rightarrow (2t-1)(t+2)=0 \Rightarrow t = \frac12$ or $t = -2$.
- $t = -2$ is outside $[-1,1]$ → **discard**.
- $\cos x = \frac12 \Rightarrow x = \frac{\pi}{3},\ \frac{5\pi}{3}$.
- **Answer**: $x = \frac{\pi}{3},\ \frac{5\pi}{3}$.

---

### 9.4.4 Using Identities to Convert to One Function

#### Example 1: Using $\sec^2 x = 1 + \tan^2 x$

$2\sec^2 x + \tan x - 3 = 0$, $0 \le x < 2\pi$.

- $\sec^2 x = 1 + \tan^2 x$: $2(1+\tan^2 x) + \tan x - 3 = 0 \Rightarrow 2\tan^2 x + \tan x - 1 = 0$.
- Let $t = \tan x$: $2t^2 + t - 1 = 0 \Rightarrow (2t-1)(t+1)=0 \Rightarrow t = \frac12$ or $t = -1$.
- $\tan x = \frac12 \Rightarrow x = \arctan\frac12 \approx 0.4636,\ 0.4636+\pi \approx 3.6052$ (add $\pi$).
- $\tan x = -1 \Rightarrow x = \frac{3\pi}{4},\ \frac{7\pi}{4}$.
- **Answer**: $x \approx 0.4636,\ 3.6052,\ \frac{3\pi}{4},\ \frac{7\pi}{4}$.

#### Example 2: Using $\sin^2 x + \cos^2 x = 1$

$3\sin x = 2\cos^2 x$, $0 \le x < 2\pi$.

- Replace $\cos^2 x = 1 - \sin^2 x$: $3\sin x = 2(1 - \sin^2 x) \Rightarrow 2\sin^2 x + 3\sin x - 2 = 0$.
- Let $t = \sin x$: $2t^2 + 3t - 2 = 0 \Rightarrow (2t-1)(t+2)=0 \Rightarrow t = \frac12$ (discard $t=-2$).
- $\sin x = \frac12 \Rightarrow x = \frac{\pi}{6},\ \frac{5\pi}{6}$.
- **Answer**: $x = \frac{\pi}{6},\ \frac{5\pi}{6}$.

#### Example 3: Using $\csc^2 x = 1 + \cot^2 x$

$\cot^2 x + \csc x = 1$, $0 \le x < 2\pi$, $x \neq 0,\pi$.

- $\csc^2 x = 1 + \cot^2 x \Rightarrow \cot^2 x = \csc^2 x - 1$.
- Substitute: $(\csc^2 x - 1) + \csc x = 1 \Rightarrow \csc^2 x + \csc x - 2 = 0$.
- Let $t = \csc x$: $t^2 + t - 2 = 0 \Rightarrow (t+2)(t-1)=0 \Rightarrow t = -2$ or $t = 1$.
- $\csc x = -2 \Rightarrow \sin x = -\frac12 \Rightarrow x = \frac{7\pi}{6},\ \frac{11\pi}{6}$.
- $\csc x = 1 \Rightarrow \sin x = 1 \Rightarrow x = \frac{\pi}{2}$.
- **Answer**: $x = \frac{\pi}{2},\ \frac{7\pi}{6},\ \frac{11\pi}{6}$.

---

### 9.4.5 Equations Involving $a\sin x + b\cos x$ (Harmonic Form / R‑Form)

An expression of the form $a\sin x + b\cos x$ can be rewritten as a **single** sine or cosine function:

$$
\boxed{a\sin x + b\cos x \equiv R\sin(x + \alpha)}
\quad\text{or}\quad
\boxed{a\sin x + b\cos x \equiv R\cos(x - \alpha)}
$$

where

$$
R = \sqrt{a^2 + b^2},\qquad
\alpha = \arctan\frac{b}{a}\ (\text{for }R\sin(x+\alpha))
$$

> **Which form to use?**  
> - $R\sin(x+\alpha)$: useful when solving $\sin$ equations  
> - $R\cos(x-\alpha)$: useful when finding maximum/minimum  

**Steps to solve $a\sin x + b\cos x = c$**:
1. Find $R = \sqrt{a^2 + b^2}$.
2. Find $\alpha$ such that $\cos\alpha = \frac{a}{R}$, $\sin\alpha = \frac{b}{R}$.
3. Rewrite as $R\sin(x+\alpha) = c$ (or $R\cos(x-\alpha) = c$).
4. Solve $\sin(x+\alpha) = \frac{c}{R}$ (must have $|c| \le R$ for solutions).
5. Use the standard method for $\sin u = k$.

#### Example 1: Solve $3\sin x + 4\cos x = 2$, $0 \le x < 2\pi$.

- $R = \sqrt{3^2 + 4^2} = 5$.
- $\alpha = \arctan\frac{4}{3} \approx 0.9273$ rad.
- Equation: $5\sin(x + 0.9273) = 2 \Rightarrow \sin(x + 0.9273) = 0.4$.
- Let $u = x + 0.9273$: $\sin u = 0.4$, $0.9273 \le u < 2\pi + 0.9273$.
- $u_0 = \arcsin 0.4 \approx 0.4115$. Solutions: $u = 0.4115$ and $u = \pi - 0.4115 \approx 2.7301$.
- $x = u - 0.9273$: $x \approx -0.5158$ (outside range, add $2\pi$ → $5.7675$), $x \approx 1.8028$.
- **Answer**: $x \approx 1.8028,\ 5.7675$.

#### Example 2: Find max/min of $y = 5\sin x - 12\cos x + 7$.

- Rewrite $5\sin x - 12\cos x = R\sin(x - \alpha)$ (note the minus).
- $R = \sqrt{5^2 + (-12)^2} = 13$.
- $\alpha = \arctan\frac{12}{5} \approx 1.176$ rad (since $\cos\alpha = \frac{5}{13}$, $\sin\alpha = \frac{12}{13}$).
- So $y = 13\sin(x - 1.176) + 7$.
- $\sin$ ranges from $-1$ to $1$, so $13\sin(x - 1.176)$ ranges from $-13$ to $13$.
- **Maximum**: $y_{\max} = 13 + 7 = 20$; **minimum**: $y_{\min} = -13 + 7 = -6$.

#### Example 3: Prove $5\cos x - 12\sin x \le 13$.

- Write $5\cos x - 12\sin x = R\cos(x + \alpha)$.
- $R = \sqrt{5^2 + 12^2} = 13$, $\alpha = \arctan\frac{12}{5} \approx 1.176$.
- Thus $5\cos x - 12\sin x = 13\cos(x + 1.176)$.
- Since $-1 \le \cos \le 1$, we have $-13 \le 13\cos(x+1.176) \le 13$.
- Therefore $5\cos x - 12\sin x \le 13$ (and its minimum is $-13$).

#### Example 4: Solve $\sin x - \sqrt{3}\cos x = 1$, $0 \le x < 2\pi$.

- $R = \sqrt{1^2 + (\sqrt{3})^2} = 2$.
- $\alpha = \arctan\frac{\sqrt{3}}{1} = \frac{\pi}{3}$ (since $\cos\alpha = \frac12$, $\sin\alpha = \frac{\sqrt{3}}{2}$).
- Equation: $2\sin\!\left(x - \frac{\pi}{3}\right) = 1 \Rightarrow \sin\!\left(x - \frac{\pi}{3}\right) = \frac12$.
- Let $u = x - \frac{\pi}{3}$: $\sin u = \frac12$, $-\frac{\pi}{3} \le u < 2\pi - \frac{\pi}{3}$.
- $u = \frac{\pi}{6},\ \frac{5\pi}{6}$.
- $x = u + \frac{\pi}{3}$: $x = \frac{\pi}{2},\ \frac{7\pi}{6}$.
- **Answer**: $x = \frac{\pi}{2},\ \frac{7\pi}{6}$.

---

### 9.4.6 Graphical Method

**When to use**: Equations like $\sin x = \frac{x}{2}$ or when asked to "use a graphical method".

**Steps**:
1. Rewrite as $f(x) = g(x)$.
2. Sketch $y = f(x)$ and $y = g(x)$ on the same axes.
3. Intersection points give solutions (approximate or count).
4. If exact values are not required, read approximate values from the graph.

**Example**: $\sin x = \frac{x}{2}$ on $[-\pi, \pi]$. How many solutions?
- Sketch $y = \sin x$ and the line $y = x/2$.
- Intersection at $x = 0$ (since both 0).
- On the positive side, the line is below the sine curve for small $x$, then crosses again near $x \approx 1.9$.
- Negative side symmetric due to oddness. Total **3 solutions**.

**Pitfall**: Graphs must be accurate; mark key points (zeros, peaks, intercepts).

---

### 9.4.7 Using a Calculator (Paper 2) / Proving $\sin x = \frac{x}{2}$ Has Exactly Three Solutions on $[-\pi,\pi]$ Using Calculus

---

### Proving $\sin x = \frac{x}{2}$ Has Exactly Three Solutions on $[-\pi,\pi]$ Using Calculus

#### Step 1: Define the function and use parity

Let  
$$
f(x) = \sin x - \frac{x}{2}.
$$

Since $\sin(-x) = -\sin x$, we have  
$$
f(-x) = -\sin x + \frac{x}{2} = -\left(\sin x - \frac{x}{2}\right) = -f(x).
$$

Thus $f$ is odd: if $x_0 \neq 0$ is a root, then $-x_0$ is also a root. We only need to study roots on $[0,\pi]$ and then mirror to the negative side. Clearly $f(0)=0$, so $x=0$ is one solution.

#### Step 2: Derivative and monotonicity intervals

$$
f'(x) = \cos x - \frac12.
$$

On $[0,\pi]$, $\cos x$ decreases from $1$ to $-1$. Solving $f'(x)=0$ gives $\cos x = \frac12$, whose unique solution is $x = \frac{\pi}{3}$ (since $\cos\frac{\pi}{3}=\frac12$). Hence:

- For $0 \le x < \frac{\pi}{3}$: $\cos x > \frac12$ so $f'(x) > 0$; $f$ is strictly increasing.
- For $\frac{\pi}{3} < x \le \pi$: $\cos x < \frac12$ so $f'(x) < 0$; $f$ is strictly decreasing.

#### Step 3: Evaluate $f$ at key points

$$
f(0) = \sin 0 - 0 = 0.
$$

$$
f\!\left(\frac{\pi}{3}\right) = \sin\frac{\pi}{3} - \frac{\pi/3}{2}
= \frac{\sqrt{3}}{2} - \frac{\pi}{6}
\approx 0.866025 - 0.523599 = 0.342426 > 0.
$$

$$
f(\pi) = \sin\pi - \frac{\pi}{2}
= 0 - \frac{\pi}{2}
\approx -1.5708 < 0.
$$

#### Step 4: Count the roots

- On $[0,\frac{\pi}{3}]$, $f$ increases strictly from $0$ to $f(\frac{\pi}{3})>0$. Since $f(0)=0$ and $f$ is strictly increasing, there is **no** other root in $(0,\frac{\pi}{3}]$.
- On $[\frac{\pi}{3},\pi]$, $f$ decreases strictly from $f(\frac{\pi}{3})>0$ to $f(\pi)<0$. By the Intermediate Value Theorem, there exists a **unique** $c \in (\frac{\pi}{3},\pi)$ such that $f(c)=0$. Strict monotonicity guarantees uniqueness.

Thus there is exactly one positive root $c \in (0,\pi]$ ($c \approx 1.8955$).

#### Step 5: Obtain the negative root by oddness

Because $f$ is odd and $c>0$ is a root, $f(-c) = -f(c) = 0$, so $-c$ is also a root. By symmetry of monotonicity, there is no other root in $(-\pi,0)$.

#### Step 6: Conclusion

On $[-\pi,\pi]$, the solutions are  

$$
x = -c,\qquad x = 0,\qquad x = c,
$$

giving **3 solutions** in total.

---

## Table of Derivatives of Trigonometric Functions

| Function f(x) | Derivative f'(x) |
| :--- | :--- |
| sin x | cos x |
| cos x | - sin x |
| tan x | sec² x (or 1 + tan² x) |
| cot x | - csc² x |
| sec x | sec x tan x |
| csc x (written cosec x in CIE 0606) | - csc x cot x |

> **Note**: In CIE IGCSE 0606, cosecant is written as cosec x, derivative remains - cosec x cot x.
---

## 9.5 Common Problem Types & Solutions

| Type | Key Method |
|------|------------|
| **Angle–radian conversion** | Multiply/divide by $\pi/180$ |
| **Arc length / sector area** | Use $s=r\theta,\ A=\frac12 r^2\theta$ with radians |
| **Composite shapes** | Break into parts, compute separately |
| **Find trig values from one given** | Use $\sin^2+\cos^2=1$ and quadrant signs |
| **Sketch trig graphs** | Determine amplitude, period, phase shift, vertical shift |
| **Solve $\sin x = a$, $\cos x = a$, $\tan x = a$** | Reference angle + symmetry/period |
| **Solve with multiple angles** | Let $u = ax+b$, adjust range, solve for $u$, back-substitute |
| **Quadratic trig equations** | Substitute $t = \sin x$ (etc.), solve quadratic, check $|t|\le1$ |
| **Using identities** | Replace using $\sin^2+\cos^2=1$, $\sec^2=1+\tan^2$, $\csc^2=1+\cot^2$ |
| **$a\sin x + b\cos x = c$ (R‑form)** | $R = \sqrt{a^2+b^2}$, write $R\sin(x+\alpha)=c$, solve |
| **Max/min of $a\sin x + b\cos x + d$** | Rewrite as $R\sin(x+\alpha)+d$; max $= R+d$, min $= -R+d$ |
| **Prove identities** | Start from complex side, convert to sine/cosine, use $\sin^2+\cos^2=1$ |
| **Graphical solutions** | Sketch both sides, count intersections |

---

## 9.6 Common Pitfalls

| Pitfall | Correct Practice |
|---------|------------------|
| Using degrees in radian formulas | Convert to radians first |
| Solving $\sin x = a$ with only one solution | Two solutions in $[0,2\pi)$ unless $a=\pm1$ |
| Forgetting $\tan x$ period is $\pi$ | Add $k\pi$, not $2k\pi$ |
| Substitution quadratic: ignoring range of $\sin x$ | Discard $t$ outside $[-1,1]$ |
| Proving identities by moving terms prematurely | Keep side‑by‑side manipulation |
| Phase shift sign confusion | Solve $bx+c=0$ to find shift direction |
| Calculator mode mismatch | Use radian mode unless problem explicitly uses degrees |
| Composite shape perimeter: double‑counting boundaries | Draw and label each edge |
| Multiple angle: forgetting to adjust the range | If solving $\sin 2x = a$ for $0\le x<2\pi$, solve $\sin u = a$ for $0\le u<4\pi$ |
| R‑form: using wrong quadrant for $\alpha$ | Choose $\alpha$ so that $\cos\alpha = a/R$, $\sin\alpha = b/R$ |

---

## Key Formula Summary

| Item | Formula |
|------|---------|
| Radian definition | $\theta = s/r$ |
| Arc length | $s = r\theta$ |
| Sector area | $A = \frac12 r^2\theta$ |
| Segment area | $\frac12 r^2(\theta - \sin\theta)$ |
| Pythagorean identity | $\sin^2\theta+\cos^2\theta=1$ |
| Derived identities | $\sec^2\theta=1+\tan^2\theta,\ \csc^2\theta=1+\cot^2\theta$ |
| Period of sine/cosine | $2\pi$ |
| Period of tangent | $\pi$ |
| General sine/cosine | $y=a\sin(bx+c)+d$: amplitude $|a|$, period $2\pi/|b|$, phase shift $-c/b$, vertical shift $d$ |
| General tangent | $y=a\tan(bx+c)+d$: period $\pi/|b|$, asymptotes $bx+c=\frac{\pi}{2}+k\pi$ |
| Solutions for $\sin x = a$ | $x = \arcsin a + 2k\pi$ or $x = \pi - \arcsin a + 2k\pi$ |
| Solutions for $\cos x = a$ | $x = \pm\arccos a + 2k\pi$ |
| Solutions for $\tan x = a$ | $x = \arctan a + k\pi$ |
| R‑form: $a\sin x + b\cos x$ | $R\sin(x+\alpha)$ where $R=\sqrt{a^2+b^2}$, $\cos\alpha=a/R$, $\sin\alpha=b/R$ |
| R‑form: max/min | $\pm R + d$ for $a\sin x+b\cos x+d$ |

---

<!-- 
感谢使用这份笔记！如果你觉得它对你有帮助，请回到 GitHub 仓库页面点一个 ⭐，
这能帮助更多同学发现这个项目。仓库地址：https://github.com/LG-leo/IG0606ADD-with-CAM-coursebook-NOTE
-->
<!-- 
Thanks for using this note! If you find it helpful, please go back to the GitHub repository page and leave a ⭐.
It helps other students discover this project. Repository link: https://github.com/LG-leo/IG0606ADD-with-CAM-coursebook-NOTE
-->

This note covers **all required content** for IGCSE 0606 Topics 8 (Circular Measure) and 9 (Trigonometry) according to the 2025–2027 syllabus. It is designed to be used **without additional assistance**, assuming the learner is comfortable with basic algebra and geometry.
