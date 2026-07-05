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

# Chapter 1: Sequences, Permutations, Combinations, and the Binomial Theorem

This chapter brings together three topics that may seem different but share a common core. **Sequences** train your ability to discover patterns and compute sums; **permutations and combinations** train your logic for systematic counting; and the **binomial theorem** is a direct application of combinations to algebraic expansions.

---

## Syllabus Mapping

| Syllabus Ref | Syllabus 2028–2030 (English) | Chinese Explanation | Section |
|:-------:|------|---------|:-------:|
| **11.1** | *Recognise the difference between permutations and combinations and know when each should be used.* | Recognise the difference between permutations and combinations and know when to use which | §1.2.4 |
| **11.2** | *Know and use the notation $n!$ and the expressions for permutations and combinations of $n$ items taken $r$ at a time. Includes $0! = 1$.* | Master the notation of $n!$, $^nP_r$, $^nC_r$ and their expressions | §1.2.2, §1.2.3 |
| **11.3** | *Solve problems on arrangement and selection using permutations or combinations. Problems will be either in an everyday context or based on an algebraic problem. Problems involving: repetition of objects; objects arranged in a circle; both permutations and combinations, are **not** included.* | Solve arrangement and selection problems using permutations or combinations (everyday or algebraic contexts). Does **not** include repetition, circular arrangements, or mixed permutation/combination. | §1.2.5 |
| **12.1** | *Use the binomial theorem for expansion of $(a+b)^n$ for positive integer $n$. Includes simplification of coefficients.* | Use the binomial theorem to expand $(a+b)^n$ ($n$ a positive integer), including simplification of coefficients | §1.3.1 |
| **12.2** | *Use the general term $\displaystyle\binom{n}{r}a^{n-r}b^r$, $0 \le r \le n$. For example: Find the term independent of $x$ in the expansion of $\left(x^2 + \frac{1}{x}\right)^{\!10}$. Knowledge of the greatest term and properties of the coefficients is **not** required.* | Use the general term formula to find specific terms (e.g., constant term). Greatest term and properties of coefficients are **not** required. | §1.3.2, §1.3.3 |
| **12.3** | *Recognise arithmetic and geometric progressions and understand the difference between them.* | Recognise arithmetic and geometric progressions and understand the differences between them | §1.1.4 |
| **12.4** | *Use the formulas for the $n$th term and for the sum of the first $n$ terms to solve problems involving arithmetic or geometric progressions. Problems may be in context.* | Use the $n$th term and sum of first $n$ terms formulas to solve arithmetic/geometric progression problems (may include real-world contexts) | §1.1.2, §1.1.3 |
| **12.5** | *Use the condition for the convergence of a geometric progression, and the formula for the sum to infinity of a convergent geometric progression. Includes explaining why a particular geometric progression has or does not have a sum to infinity.* | Use the convergence condition of a geometric progression and the sum to infinity formula, **including explaining why a given geometric series does or does not have a sum to infinity** | §1.1.3 |

---

## 1.1 Sequences (Arithmetic and Geometric)

A sequence is an ordered list of numbers. In Additional Mathematics, we focus on two fundamental types: **arithmetic sequences** (where the difference between consecutive terms is constant) and **geometric sequences** (where the ratio between consecutive terms is constant).

### 1.1.1 Summation Notation $\sum$

Before delving into sequences, we need to master summation notation $\sum$ (the Greek letter Sigma). It represents the sum of a series of numbers:

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + a_3 + \cdots + a_n
$$

The summation operation satisfies three basic rules. Their derivations follow directly from expanding the sigma notation:

**Rule 1 — Constant Factor Extraction**:

Expand the sum:
$$
\sum_{k=1}^{n} (c \cdot a_k) = c \cdot a_1 + c \cdot a_2 + \cdots + c \cdot a_n
$$
Factor out $c$ from each term:
$$
= c\,(a_1 + a_2 + \cdots + a_n) = c \cdot \sum_{k=1}^{n} a_k
$$
$$
\boxed{\sum_{k=1}^{n} (c \cdot a_k) = c \cdot \sum_{k=1}^{n} a_k}
$$

**Rule 2 — Splitting a Sum**:

Expand the sum and regroup:
$$
\begin{aligned}
\sum_{k=1}^{n} (a_k \pm b_k) &= (a_1 \pm b_1) + (a_2 \pm b_2) + \cdots + (a_n \pm b_n) \\
&= (a_1 + a_2 + \cdots + a_n) \pm (b_1 + b_2 + \cdots + b_n)
\end{aligned}
$$
$$
\boxed{\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k}
$$

**Rule 3 — Sum of a Constant**:

When each term equals the constant $c$, the sum is $c$ added $n$ times:
$$
\sum_{k=1}^{n} c = \underbrace{c + c + \cdots + c}_{n \text{ times}} = n c
$$
$$
\boxed{\sum_{k=1}^{n} c = n c}
$$

**Example**: Evaluate $\displaystyle\sum_{k=1}^{5} (3k - 2)$.

**Method 1 (Direct expansion)**: Substitute $k=1,2,3,4,5$ and add term by term:

$$
\begin{aligned}
\sum_{k=1}^{5} (3k - 2) &= (3\cdot1 - 2) + (3\cdot2 - 2) + (3\cdot3 - 2) + (3\cdot4 - 2) + (3\cdot5 - 2) \\[4pt]
&= 1 + 4 + 7 + 10 + 13 \\[4pt]
&= 35
\end{aligned}
$$

**Method 2 (Using summation rules)**: Apply the constant factor and splitting rules:

$$
\begin{aligned}
\sum_{k=1}^{5} (3k - 2) 
&= 3\sum_{k=1}^{5} k - \sum_{k=1}^{5} 2 \qquad \text{(Rules 1 and 2)} \\[4pt]
&= 3 \times (1+2+3+4+5) - 5 \times 2 \qquad \text{(expand $\sum k$, apply Rule 3)} \\[4pt]
&= 3 \times 15 - 10 \\[4pt]
&= 45 - 10 = 35
\end{aligned}
$$

Both methods give the same result ✓. **Method 1** is more intuitive and good for small $n$; **Method 2** is more efficient, especially when $n$ is large.

---

### 1.1.2 Arithmetic Progression (AP)

#### Definition

A sequence is called an **arithmetic progression** if, starting from the second term, the difference between each term and its preceding term is a **constant**. This constant is called the **common difference**, denoted by $d$:

$$
a_{n+1} - a_n = d \quad (\text{for all } n \ge 1)
$$

**Example**: $5, 9, 13, 17, 21$ is an arithmetic progression, with $d=4$, $a=5$.

#### Formula for the $n$th Term — Derivation

Let the first term be $a_1 = a$. The defining property of an AP is $a_{k+1} - a_k = d$, i.e. $a_{k+1} = a_k + d$ for every $k \ge 1$.

Starting from the first term and applying the recurrence repeatedly:

$$
\begin{aligned}
a_2 &= a_1 + d = a + d \\[4pt]
a_3 &= a_2 + d = (a + d) + d = a + 2d \\[4pt]
a_4 &= a_3 + d = (a + 2d) + d = a + 3d \\[4pt]
&\;\;\vdots
\end{aligned}
$$

Observing the pattern: the coefficient of $d$ is always one less than the term index. After $(n-1)$ steps from $a_1$, we have added $d$ exactly $(n-1)$ times:

$$
\boxed{a_n = a + (n-1)d}
$$

> **Verification**: For $n=1$, $a_1 = a + 0 \cdot d = a$ ✓; for $n=2$, $a_2 = a + 1 \cdot d = a + d$ ✓.

#### Formula for the Sum of the First $n$ Terms — Derivation (Reverse Addition Method)

Let $S_n$ be the sum of the first $n$ terms:

$$
S_n = a + (a+d) + (a+2d) + \cdots + [a+(n-1)d] \tag{1}
$$

Now write the same sum in reverse order, from the last term back to the first:

$$
S_n = [a+(n-1)d] + [a+(n-2)d] + \cdots + (a+d) + a \tag{2}
$$

Add equations (1) and (2) term by term. There are $n$ columns; the $k$th column (counting from the left) pairs:

$$
\bigl[a + (k-1)d\bigr] + \bigl[a + (n-k)d\bigr] = 2a + (n-1)d
$$

Notice that each column gives the **same** sum, $2a + (n-1)d$. Since there are $n$ such columns:

$$
2S_n = \underbrace{[2a + (n-1)d] + [2a + (n-1)d] + \cdots + [2a + (n-1)d]}_{n \text{ times}} = n\,[2a + (n-1)d]
$$

Dividing both sides by $2$:

$$
\boxed{S_n = \frac{n}{2}\,[\,2a + (n-1)d\,]}
$$

If the last term is $l = a_n = a + (n-1)d$, then $2a + (n-1)d = a + l$, giving the alternative form:

$$
\boxed{S_n = \frac{n}{2}\,(a + l)}
$$

#### Examples

**Example 1**: First term $7$, common difference $3$, find the $15$th term.

$$
a_{15} = 7 + 14 \times 3 = 7 + 42 = 49
$$

---

**Example 2**: First term $2$, common difference $5$, sum of the first $n$ terms is $156$, find $n$.

**Solution** (step-by-step):

**Step 1**: Substitute into the AP sum formula.

$$
S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}[2\times2 + (n-1)\times5] = \frac{n}{2}[4 + 5(n-1)]
$$

**Step 2**: Simplify inside the brackets.

$$
4 + 5(n-1) = 4 + 5n - 5 = 5n - 1
$$

Set $S_n = 156$:

$$
\frac{n}{2}(5n - 1) = 156
$$

**Step 3**: Multiply both sides by $2$ and expand.

$$
n(5n - 1) = 312 \quad\Rightarrow\quad 5n^2 - n - 312 = 0
$$

**Step 4**: Solve the quadratic using $n = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, with $a=5$, $b=-1$, $c=-312$:

$$
n = \frac{1 \pm \sqrt{(-1)^2 - 4\cdot5\cdot(-312)}}{2\cdot5} = \frac{1 \pm \sqrt{1 + 6240}}{10} = \frac{1 \pm \sqrt{6241}}{10}
$$

Since $6241 = 79^2$ ($79 \times 79 = 6241$):

$$
n = \frac{1 \pm 79}{10}
$$

**Step 5**: $n$ represents the number of terms, so it must be a positive integer. Discard the negative root:

$$
n = \frac{1 + 79}{10} = \frac{80}{10} = 8
$$

> **Verification**: $S_8 = \dfrac{8}{2}[2\cdot2 + 7\cdot5] = 4 \times (4 + 35) = 4 \times 39 = 156$ ✓

---

**Example 3** (Real-world context): Deposit $500$ in the first year, then increase the deposit by $50$ each subsequent year. What is the total amount saved after $10$ years?

$$
S_{10} = \frac{10}{2}[2 \times 500 + 9 \times 50] = 5 \times (1000 + 450) = 7250
$$

Answer: $7250$ dollars.

---

### 1.1.3 Geometric Progression (GP)

#### Definition

A sequence is called a **geometric progression** if, starting from the second term, the ratio of each term to its preceding term is a **constant**. This constant is called the **common ratio**, denoted by $r$:

$$
\frac{a_{n+1}}{a_n} = r \quad (\text{for all } n \ge 1)
$$

**Example**: $2, 6, 18, 54, 162$ is a geometric progression, with $r=3$, $a=2$.

#### Formula for the $n$th Term — Derivation

Let the first term be $a_1 = a$. The defining property of a GP is $\dfrac{a_{k+1}}{a_k} = r$, i.e. $a_{k+1} = a_k \cdot r$ for every $k \ge 1$.

Starting from the first term and applying the recurrence repeatedly:

$$
\begin{aligned}
a_2 &= a_1 \cdot r = a r \\[4pt]
a_3 &= a_2 \cdot r = (a r) \cdot r = a r^2 \\[4pt]
a_4 &= a_3 \cdot r = (a r^2) \cdot r = a r^3 \\[4pt]
&\;\;\vdots
\end{aligned}
$$

Observing the pattern: the exponent of $r$ is always one less than the term index. After $(n-1)$ multiplications by $r$ starting from $a_1$, we obtain:

$$
\boxed{a_n = a r^{\,n-1}}
$$

> **Verification**: For $n=1$, $a_1 = a r^{0} = a$ ✓; for $n=2$, $a_2 = a r^{1} = a r$ ✓.

#### Formula for the Sum of the First $n$ Terms — Derivation (Subtraction Method)

Let $S_n$ be the sum of the first $n$ terms:

$$
S_n = a + a r + a r^2 + \cdots + a r^{\,n-1} \tag{1}
$$

Multiply both sides of (1) by the common ratio $r$:

$$
r S_n = a r + a r^2 + a r^3 + \cdots + a r^{\,n-1} + a r^{\,n} \tag{2}
$$

Now compare (1) and (2) by aligning them term by term:

$$
\begin{array}{cccccccccc}
S_n   & = & a      & + & a r    & + & a r^2  & + & \cdots & + & a r^{\,n-1} &   \\[4pt]
r S_n & = &        &   & a r    & + & a r^2  & + & a r^3  & + & \cdots        & + & a r^{\,n}
\end{array}
$$

This alignment reveals the "shift" effect:
- The first term $a$ appears only in $S_n$.
- The last term $a r^{\,n}$ appears only in $r S_n$.
- All middle terms ($a r$ through $a r^{\,n-1}$) appear in **both** sums, perfectly aligned.

Therefore, subtract (2) from (1) — all middle terms cancel out, leaving only the first and last:

$$
\begin{aligned}
S_n - r S_n &= \bigl(a + a r + a r^2 + \cdots + a r^{\,n-1}\bigr) - \bigl(a r + a r^2 + \cdots + a r^{\,n-1} + a r^{\,n}\bigr) \\[4pt]
&= a \;+\; \underbrace{(a r - a r)}_{=0} \;+\; \underbrace{(a r^2 - a r^2)}_{=0} \;+\; \cdots \;+\; \underbrace{(a r^{\,n-1} - a r^{\,n-1})}_{=0} \;-\; a r^{\,n} \\[4pt]
&= a - a r^{\,n}
\end{aligned}
$$

> **💡 The essence of the subtraction method**: Because the $n-1$ middle terms ($a r$ to $a r^{\,n-1}$) are identical in both sums, they cancel out completely. This is why the method is called the **"shift and subtract" method** — multiplying by $r$ shifts the terms so the middle ones align, and subtracting leaves only the first and last terms.

Factor out $S_n$ on the left and $a$ on the right:

$$
S_n(1 - r) = a(1 - r^{\,n})
$$

Now consider two cases:

- **If $r = 1$**: Every term equals $a$, so $S_n = \underbrace{a + a + \cdots + a}_{n \text{ times}} = n a$.

- **If $r \neq 1$**: Divide both sides by $(1-r)$:

$$
\boxed{S_n = a \cdot \frac{1 - r^{\,n}}{1 - r}}
$$

An equivalent form (multiply numerator and denominator by $-1$) is:

$$
\boxed{S_n = a \cdot \frac{r^{\,n} - 1}{r - 1}}
$$

> **Why does $r=1$ need special treatment?** Substituting $r=1$ into the formula $S_n = a\dfrac{1-r^n}{1-r}$ gives $\dfrac{0}{0}$, which is undefined. So we must handle this case separately. In an exam, if a geometric progression might have $r=1$ (e.g., $3, 3, 3, 3, \ldots$), remember to write $S_n = n a$ directly.

#### Convergence Condition and Sum to Infinity of an Infinite Geometric Series (**Syllabus 12.5 Key Point**)

$$
S_\infty = \lim_{n \to \infty} S_n = \lim_{n \to \infty} a \cdot \frac{1 - r^{\,n}}{1 - r}
$$

The behaviour of $r^{\,n}$ as $n \to \infty$ determines whether the series converges:

| Range of $r$ | Behaviour of $r^{\,n}$ as $n \to \infty$ | Does the series converge? | Sum to Infinity |
|:-------------:|----------------------------------|:-----------:|:------:|
| $\lvert r\rvert < 1$ | $r^{\,n} \to 0$ | ✅ **Converges** | $\displaystyle S_\infty = \frac{a}{1-r}$ |
| $\lvert r\rvert > 1$ | $\lvert r\rvert^{\,n} \to \infty$ | ❌ **Diverges** | No finite sum |
| $r = 1$ | $r^{\,n} = 1$ (constant) | ❌ **Diverges** | $S_n = n a \to \infty$ |
| $r = -1$ | Oscillates between $1$ and $-1$ | ❌ **Diverges** | Sum is undefined |

Therefore, **the necessary and sufficient condition for a geometric series to converge is $|r| < 1$**.

---

**Intuitive understanding**: Why does the series converge when $|r| < 1$?

Take $r = \dfrac{1}{2}$ as an example:
$$
\left(\frac{1}{2}\right)^1 = \frac{1}{2},\; \left(\frac{1}{2}\right)^2 = \frac{1}{4},\; \left(\frac{1}{2}\right)^3 = \frac{1}{8},\; \ldots
$$

Each successive term is half of the previous one, so the terms get smaller and smaller, approaching $0$. The new terms added become negligible, and the total sum approaches a **finite value**.

Conversely, if $|r| > 1$ (e.g., $r = 2$):
$$
2^1 = 2,\; 2^2 = 4,\; 2^3 = 8,\; \ldots
$$

The terms grow larger and larger, the sum increases without bound, and the series diverges.

---

**Step-by-step derivation of $S_\infty$ when $|r| < 1$**:

**Step 1**: Start with the formula for $S_n$:
$$
S_n = a \cdot \frac{1 - r^{\,n}}{1 - r}
$$

**Step 2**: Take the limit as $n \to \infty$. Since $|r| < 1$, we have $r^{\,n} \to 0$:
$$
S_\infty = \lim_{n \to \infty} S_n = \lim_{n \to \infty} a \cdot \frac{1 - r^{\,n}}{1 - r}
$$

**Step 3**: The constants $a$ and $1-r$ do not depend on $n$, so they can be factored out of the limit:
$$
S_\infty = \frac{a}{1-r} \cdot \lim_{n \to \infty} (1 - r^{\,n})
$$

**Step 4**: Since $r^{\,n} \to 0$, we have $(1 - r^{\,n}) \to 1$:
$$
S_\infty = \frac{a}{1-r} \cdot 1
$$

**Step 5**: The final result:
$$
\boxed{S_\infty = \frac{a}{1-r}}
$$

---

**📝 Exam answer template** (when asked to "explain why a particular geometric series has or does not have a sum to infinity"):

1. **Has** a sum to infinity: When $|r| < 1$, as $n \to \infty$, $r^{\,n} \to 0$. Substituting into $S_n = a\dfrac{1-r^n}{1-r}$ gives $S_n \to \dfrac{a}{1-r}$ (the limit exists and is finite), so the series converges to $\dfrac{a}{1-r}$.
2. **Does not have** a sum to infinity: When $|r| \ge 1$, $r^{\,n}$ does not approach $0$ (for $|r|>1$ it grows without bound, for $r=1$ it stays constant at $1$, for $r=-1$ it oscillates between $\pm1$). Therefore $S_n$ does not approach any finite value, the limit does not exist, and the series diverges.

---

#### Examples

**Example 1**: First term $3$, common ratio $2$, find the $6$th term.

$$
a_6 = 3 \times 2^5 = 3 \times 32 = 96
$$

---

**Example 2** (Convergence check + sum to infinity): $12 + 6 + 3 + \dfrac{3}{2} + \cdots$

**Solution** (step-by-step):

**Step 1**: Identify the first term $a$ and common ratio $r$.

The first term is $12$, so $a = 12$. Divide the second term by the first to find $r$:
$$
r = \frac{6}{12} = \frac{1}{2}
$$

**Step 2**: Check convergence.

$|r| = \dfrac{1}{2} < 1$, which satisfies the convergence condition. Therefore the series converges and has a finite sum to infinity.

**Step 3**: Apply the sum to infinity formula.

$$
S_\infty = \frac{a}{1-r} = \frac{12}{1 - \frac{1}{2}}
$$

**Step 4**: Simplify.

$$
S_\infty = \frac{12}{\frac{1}{2}} = 12 \times 2 = 24
$$

Thus the sum to infinity is $\boxed{24}$.

> **Verification**: The first few terms are $12 + 6 + 3 + 1.5 + 0.75 + 0.375 + \cdots$ The sum of the first $5$ terms is $12+6+3+1.5+0.75 = 23.25$, already close to $24$. Each additional term adds a smaller and smaller amount, and the total approaches $24$ ✓

---

**Example 3** (Given $S_\infty$ to find $r$): An infinite geometric series converges, its sum is $8$, and its first term is $4$. Find the common ratio $r$.

**Solution** (step-by-step):

**Step 1**: Write down the known values.

$a = 4$, $S_\infty = 8$, and the series converges (so $|r| < 1$).

**Step 2**: Substitute into the sum to infinity formula and set up the equation.

$$
S_\infty = \frac{a}{1-r} \quad\Rightarrow\quad 8 = \frac{4}{1 - r}
$$

**Step 3**: Solve for $r$.

Multiply both sides by $(1-r)$:
$$
8(1 - r) = 4
$$

Expand:
$$
8 - 8r = 4
$$

Rearrange:
$$
-8r = 4 - 8 = -4
$$

Divide by $-8$:
$$
r = \frac{-4}{-8} = \frac{1}{2}
$$

**Step 4**: Verify the convergence condition.

$|r| = \dfrac{1}{2} < 1$, which satisfies the convergence condition, confirming the answer is valid.

Thus the common ratio is $\boxed{r = \dfrac{1}{2}}$.

---

### 1.1.4 Comparison: Arithmetic vs Geometric Progressions (**Syllabus 12.3 Key Point**)

| Feature | Arithmetic Progression (AP) | Geometric Progression (GP) |
|:----|:-------------|:-------------|
| **Defining Property** | $a_{n+1} - a_n = d$ (constant difference) | $\dfrac{a_{n+1}}{a_n} = r$ (constant ratio) |
| **How to check** | Subtract consecutive terms, check if constant | Divide consecutive terms, check if constant |
| **$n$th term** | $a_n = a + (n-1)d$ | $a_n = a r^{\,n-1}$ |
| **Sum of first $n$ terms** | $S_n = \dfrac{n}{2}[2a + (n-1)d]$ | $S_n = a\dfrac{1-r^n}{1-r}$ ($r \neq 1$) |
| **Growth pattern** | **Linear growth** (add constant each time) | **Exponential growth/decay** (multiply by constant each time) |
| **Sum to infinity** | Does not exist (except constant sequence with $d=0$) | Converges to $\dfrac{a}{1-r}$ when $|r| < 1$ |

**Practice identifying (with detailed analysis)**:

1. **$5, 8, 11, 14, 17, \ldots$**
   - Check AP: $8-5=3$, $11-8=3$, $14-11=3$, $17-14=3$ → constant difference of $3$ ✓
   - Check GP: $\dfrac{8}{5}=1.6$, $\dfrac{11}{8}=1.375$, $\dfrac{14}{11}\approx1.273$, → not constant ✗
   - **Conclusion**: **AP** ✓ ($a=5,\; d=3$)

2. **$5, 10, 20, 40, 80, \ldots$**
   - Check AP: $10-5=5$, $20-10=10$, $40-20=20$ → not constant ✗
   - Check GP: $\dfrac{10}{5}=2$, $\dfrac{20}{10}=2$, $\dfrac{40}{20}=2$, $\dfrac{80}{40}=2$ → constant ratio of $2$ ✓
   - **Conclusion**: **GP** ✓ ($a=5,\; r=2$)

3. **$1, 4, 9, 16, 25, \ldots$**
   - Check AP: $4-1=3$, $9-4=5$, $16-9=7$, $25-16=9$ → differences increase, not constant ✗
   - Check GP: $\dfrac{4}{1}=4$, $\dfrac{9}{4}=2.25$, $\dfrac{16}{9}\approx1.78$, $\dfrac{25}{16}=1.5625$ → ratios decrease, not constant ✗
   - **Conclusion**: **Neither** ✗ (this is the square number sequence $a_n = n^2$)

4. **$100, 50, 25, 12.5, \ldots$**
   - Check AP: $50-100=-50$, $25-50=-25$ → not constant ✗
   - Check GP: $\dfrac{50}{100}=0.5$, $\dfrac{25}{50}=0.5$, $\dfrac{12.5}{25}=0.5$ → constant ratio of $\dfrac{1}{2}$ ✓
   - **Conclusion**: **GP** ✓ ($a=100,\; r=\dfrac{1}{2}$), and $|r| = \dfrac{1}{2} < 1$, so it is **convergent**

---

## 1.2 Permutations and Combinations

Permutations and combinations answer the same fundamental question: "How many different ways are there?" The key difference lies in **whether order matters**.

### 1.2.1 Multiplication Principle

If a task can be broken down into $k$ sequential steps, and the $i$th step has $m_i$ ways to be performed, then the total number of ways is:

$$
\boxed{m_1 \times m_2 \times \cdots \times m_k}
$$

**Example**: There are $3$ routes from A to B, and $4$ routes from B to C. The number of routes from A to B to C is $3 \times 4 = 12$.

### 1.2.2 Permutations — Order Matters


FIRST we need to understand what is "!"

Factorial notation:
$$
1! = 1
$$
$$
2! = 1 \times 2
$$
$$
3! = 1 \times 2 \times 3
$$
$$
4! = 1 \times 2 \times 3 \times 4
$$
$$
5! = 1 \times 2 \times 3 \times 4 \times 5
$$
In general,
$$
n! = 1 \times 2 \times \cdots \times n
$$

Now we count the number of ways to arrange \(r\) distinct objects chosen from \(n\) distinct objects, where order matters. This number is denoted by \({}^{n}P_r\).

We fill \(r\) positions one by one:

- 1st position: \(n\) choices  
- 2nd position: \(n-1\) choices (one already used)  
- 3rd position: \(n-2\) choices  
- …  
- r‑th position: \(n - (r-1) = n - r + 1\) choices  

By the multiplication principle, the total number of arrangements is the product of all these choices:
$$
{}^{n}P_r = n \times (n-1) \times (n-2) \times \cdots \times (n-r+1)
$$

This product has \(r\) factors. To express it as a fraction of factorials, multiply and divide by the missing factors from \((n-r)\) down to 1:
$$
{}^{n}P_r = \frac{n \times (n-1) \times \cdots \times 2 \times 1}{(n-r) \times (n-r-1) \times \cdots \times 2 \times 1}
$$

The numerator is exactly \(n!\), and the denominator is \((n-r)!\). Therefore:
$$
{}^{n}P_r = \frac{n!}{(n-r)!}
$$

Special cases:
- When \(r=0\), we choose nothing, only one way:
$$
{}^{n}P_0 = \frac{n!}{n!} = 1
$$
- When \(r=n\), we arrange all objects:
$$
{}^{n}P_n = \frac{n!}{0!} = n!
$$

This completes the derivation.

---
---

**Definition**: Selecting $r$ objects ($r \le n$) from $n$ distinct objects and arranging them in a specific order. Different orders count as different permutations. Denoted by $^nP_r$ or $P(n,r)$.

**Derivation**:

$$
^nP_r = n(n-1)(n-2)\cdots(n-r+1)
$$

Expressed using factorials:

$$
\boxed{^nP_r = \frac{n!}{(n-r)!}}
$$

**Special values**: $^nP_n = n!$, $^nP_0 = 1$, $0! = 1$.

### 1.2.3 Combinations — Order Does Not Matter

**Definition**: Selecting $r$ objects ($r \le n$) from $n$ distinct objects without considering the order. Denoted by $^nC_r$, $C(n,r)$, or $\binom{n}{r}$.

**Derivation**: Number of permutations divided by the number of internal arrangements:

$$
\boxed{^nC_r = \binom{n}{r} = \frac{^nP_r}{r!} = \frac{n!}{r!\,(n-r)!}}
$$

**Properties**:

- Symmetry: $\displaystyle\binom{n}{r} = \binom{n}{n-r}$
- Boundary values: $\displaystyle\binom{n}{0} = \binom{n}{n} = 1$, $\displaystyle\binom{n}{1} = \binom{n}{n-1} = n$

### 1.2.4 How to Choose? (**Syllabus 11.1 Key Point**)

Ask yourself: **If I swap any two selected elements, does the result change?**

| Scenario | Does order matter? | Use | Example |
|:----|:---------:|:----|:-----|
| Queuing, rankings, passwords, rankings | ✅ Yes | **Permutation** $^nP_r$ | Choose 3 out of 6 people to stand in a row |
| Committees, subject selection, lottery draws, team formation | ❌ No | **Combination** $^nC_r$ | Choose 3 out of 6 people to form a committee |

### 1.2.5 Worked Examples

**Example 1** (Permutation — everyday context): From 6 different books, choose 4 to arrange on a shelf (left to right). How many arrangements?

$$
^6P_4 = \frac{6!}{(6-4)!} = \frac{6!}{2!} = 6 \times 5 \times 4 \times 3 = 360
$$

Answer: $360$ ways.

---

**Example 2** (Combination — everyday context): From 7 men and 5 women, select a committee of 4 that must include at least 2 women. How many ways?

- $2$ women $2$ men: $\displaystyle\binom{5}{2} \times \binom{7}{2} = 10 \times 21 = 210$
- $3$ women $1$ man: $\displaystyle\binom{5}{3} \times \binom{7}{1} = 10 \times 7 = 70$
- $4$ women $0$ men: $\displaystyle\binom{5}{4} \times \binom{7}{0} = 5 \times 1 = 5$

Total: $210 + 70 + 5 = 285$.

> **Verification by complement**: Total $\displaystyle\binom{12}{4}=495$, subtract "at most 1 woman" ($0$ women $4$ men $= \binom{5}{0}\binom{7}{4}=35$, $1$ woman $3$ men $= \binom{5}{1}\binom{7}{3}=5\times35=175$, total $210$), $495 - 210 = 285$ ✓

---

**Example 3** (Algebraic context — combinatorial identity): Prove that $\displaystyle\binom{n}{r} + \binom{n}{r-1} = \binom{n+1}{r}$, and use this to compute $\displaystyle\binom{8}{3} + \binom{8}{2}$.

**Proof**:

$$
\begin{aligned}
\binom{n}{r} + \binom{n}{r-1}
&= \frac{n!}{r!(n-r)!} + \frac{n!}{(r-1)!(n-r+1)!} \\[4pt]
&= \frac{n!}{r!(n-r+1)!}\Big[(n-r+1) + r\Big] \\[4pt]
&= \frac{n! \cdot (n+1)}{r!(n-r+1)!}
= \frac{(n+1)!}{r!(n+1-r)!}
= \binom{n+1}{r}
\end{aligned}
$$

**Application**:

$$
\binom{8}{3} + \binom{8}{2} = \binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84
$$

### 1.2.5.1 0606 Exam Pitfalls: The "Selection vs Arrangement" Nature

Many mistakes in exams come not from the formulas themselves, but from **deciding whether to use permutations or combinations**. Remember the core criterion:

- **Permutation** $^nP_r$: First select $r$ items, then **arrange** them into distinct positions (e.g., seats, rankings, order, passwords).
- **Combination** $^nC_r$: Only select $r$ items, **without** considering internal order.

For **"at least/at most"** problems, if the complement has few cases, use the **complement method**:

$$
\text{Required} = \text{Total} - \text{Complement}
$$

For example, when a problem says "at least 2 women", the complement is only "0 women" and "1 woman" — this is more efficient than enumerating "2 women, 3 women, 4 women" directly.

**Quick self-check**: After computing a combination, verify the symmetry property:

$$
\binom{n}{r} = \binom{n}{n-r}
$$

For instance, $\binom{5}{2}$ should equal $10$, not $20$. If you get an unusual result, you likely missed a step in the factorial calculation.

---

### 1.2.6 ⚠️ Topics NOT Examined

According to the syllabus, the following types **will not appear**:

| Not Examined | English Original |
|---------|---------|
| ❌ Permutations with repetition of objects | *repetition of objects* |
| ❌ Circular arrangements | *objects arranged in a circle* |
| ❌ Mixed use of permutations and combinations in the same problem | *both permutations and combinations* |

In the exam, each problem is either purely about permutations or purely about combinations.

---

## 1.3 Binomial Theorem

### 1.3.1 Binomial Expansion (**Syllabus 12.1**)

$(a+b)^n$ can be thought of as multiplying $n$ copies of $(a+b)$. When expanding, each term is the product of choosing either $a$ or $b$ from each factor. To obtain $a^{\,n-r}b^{\,r}$, we need to choose $b$ from $r$ factors and $a$ from the remaining $n-r$ factors. The number of ways to make this choice is $\binom{n}{r}$.

Summing over $r = 0, 1, \ldots, n$:

$$
\boxed{(a+b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{\,n-r} b^{\,r}}
$$

**Example**: Expand $(x+3)^4$.

$$
\begin{aligned}
(x+3)^4 &= \binom{4}{0}x^4(3)^0 + \binom{4}{1}x^3(3)^1 + \binom{4}{2}x^2(3)^2 + \binom{4}{3}x^1(3)^3 + \binom{4}{4}x^0(3)^4 \\
&= 1 \cdot x^4 + 4 \cdot 3x^3 + 6 \cdot 9x^2 + 4 \cdot 27x + 1 \cdot 81 \\
&= x^4 + 12x^3 + 54x^2 + 108x + 81
\end{aligned}
$$

Note that each coefficient has been **simplified** (e.g., $4 \times 3 = 12$, $6 \times 9 = 54$), as explicitly required by the syllabus.

---
**Example 2** — Understanding the summation formula step by step:

The formula $\displaystyle\sum_{r=0}^{n} \binom{n}{r} a^{\,n-r} b^{\,r}$ consists of four components:

1. **$\displaystyle\sum_{r=0}^{n}$** — The summation counter. Let $r$ take values $0, 1, 2, \ldots, n$. For each $r$, compute the remaining parts and add all results together.

2. **$\displaystyle\binom{n}{r}$** — The binomial coefficient (the number of ways to choose $r$ items from $n$).

3. **$a^{\,n-r}$** — The power of $a$, which decreases as $r$ increases.

4. **$b^{\,r}$** — The power of $b$, which increases as $r$ increases.

**Key invariant**: In every term, the exponents satisfy $(n-r) + r = n$, so the sum of the exponents of $a$ and $b$ always equals $n$.

**Walkthrough for $n=4$**:

| $r$ | Binomial Coefficient | Letter Part | Resulting Term |
|:---:|:---|:---|:---|
| $r=0$ | $\binom{4}{0}=1$ | $a^{4-0}b^0 = a^4$ | $1a^4$ |
| $r=1$ | $\binom{4}{1}=4$ | $a^{4-1}b^1 = a^3b$ | $4a^3b$ |
| $r=2$ | $\binom{4}{2}=6$ | $a^{4-2}b^2 = a^2b^2$ | $6a^2b^2$ |
| $r=3$ | $\binom{4}{3}=4$ | $a^{4-3}b^3 = ab^3$ | $4ab^3$ |
| $r=4$ | $\binom{4}{4}=1$ | $a^{4-4}b^4 = b^4$ | $1b^4$ |

Adding all terms together:

$$
(a+b)^4 = 1a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + 1b^4
$$

This matches the result from Example 1.

---

### 1.3.2 General Term and Specific Terms (**Syllabus 12.2**)

The $(r+1)$th term in the expansion (counting from $r=0$):

$$
\boxed{T_{r+1} = \binom{n}{r} a^{\,n-r} b^{\,r}}
$$

Common question types:

| Type | Method |
|:----|:----|
| Find the coefficient of $x^k$ | Set the exponent of $x$ in the general term $= k$, solve for $r$ |
| Find the constant term (independent of $x$) | Set the exponent of $x$ $= 0$, solve for $r$ |
| Find the coefficient of $x^p y^q$ | Match the exponents of $x$ and $y$ respectively |

> **⚠️ Important distinction**:
> - **Binomial coefficient** = $\binom{n}{r}$ (depends only on $n$ and $r$)
> - **Full coefficient** = $\binom{n}{r}$ × constant factors and signs from $a$ and $b$
>
> For example, in $(2x-3)^5$, for $r=2$: binomial coefficient $\binom{5}{2}=10$, full coefficient $= 10 \cdot (2)^3 \cdot (-3)^2 = 720$

### 1.3.3 Worked Examples

**Example 1** (Finding the coefficient of a specified power): Find the coefficient of $x$ in the expansion of $\left(2x + \dfrac{1}{x}\right)^7$.

**Solution**:

$$
T_{r+1} = \binom{7}{r} (2x)^{7-r} \left(\frac{1}{x}\right)^{\!r}
= \binom{7}{r} 2^{7-r} x^{7-r} \cdot x^{-r}
= \binom{7}{r} 2^{7-r} x^{7-2r}
$$

Set $7-2r = 1$, giving $r = 3$.

$$
T_4 = \binom{7}{3} 2^{4} x = 35 \times 16 \times x = 560x
$$

Therefore, the coefficient of $x$ is $560$.

---

**Example 2** (Finding the constant term — typical syllabus question): Find the constant term in the expansion of $\left(x^2 - \dfrac{2}{x}\right)^6$.

**Solution**:

$$
\begin{aligned}
T_{r+1} &= \binom{6}{r} (x^2)^{6-r} \left(-\frac{2}{x}\right)^{\!r} \\
&= \binom{6}{r} (-2)^r x^{12-2r} \cdot x^{-r} \\
&= \binom{6}{r} (-2)^r x^{12-3r}
\end{aligned}
$$

Set $12 - 3r = 0$, giving $r = 4$.

$$
T_5 = \binom{6}{4} (-2)^4 = 15 \times 16 = 240
$$

Thus the constant term is $240$.

---

**Example 3** (Coefficient in the product of two binomials): Find the coefficient of $x^2$ in the expansion of $(1+x)^5 (2-x)^4$.

**Solution**:

$(1+x)^5$ general term: $\displaystyle\binom{5}{r} x^r$
$(2-x)^4$ general term: $\displaystyle\binom{4}{k} 2^{4-k} (-1)^k x^k$

We need $r + k = 2$:

| $r$ | $k$ | Calculation | Contribution |
|:--:|:--:|:----|:----:|
| $0$ | $2$ | $\binom{5}{0} \cdot \binom{4}{2} 2^{2} (-1)^2 = 1 \times 6 \times 4 \times 1$ | $24$ |
| $1$ | $1$ | $\binom{5}{1} \cdot \binom{4}{1} 2^{3} (-1)^1 = 5 \times 4 \times 8 \times (-1)$ | $-160$ |
| $2$ | $0$ | $\binom{5}{2} \cdot \binom{4}{0} 2^{4} (-1)^0 = 10 \times 1 \times 16 \times 1$ | $160$ |

Sum: $24 + (-160) + 160 = 24$.

Answer: The coefficient of $x^2$ is $24$.

---

### 1.3.3.1 0606 Exam Pitfalls: Splitting the General Term, Signs, and Coefficient Distinctions

Binomial theorem mistakes most often arise from **splitting the general term** and **confusing coefficient types**, not from the formula itself.

#### 1. Split the general term down to the smallest unit

When finding a term in $\left(2x + \dfrac{1}{x}\right)^7$, first break $a$ and $b$ into "numeric constant × power of $x$":

- $a = 2x$ → numeric part $2$, $x$-power $x^1$
- $b = \dfrac{1}{x}$ → numeric part $1$, $x$-power $x^{-1}$

Then the general term becomes:

$$
T_{r+1} = \binom{7}{r}(2)^{7-r}(1)^r x^{(7-r)\cdot 1 + r\cdot(-1)}
= \binom{7}{r}2^{7-r}x^{7-2r}
$$

Note: the exponent of $x$ in $\dfrac{1}{x}$ is $-1$, not $0$. If solving for $r$ gives a non-integer or a value outside $0 \le r \le n$, that term does not exist — do not force it.

#### 2. Don't forget the negative sign when multiplying two binomials

For example, when finding the coefficient of $x^2$ in $(1+x)^5(2-x)^4$, the second binomial's general term contains $(-x)^k$, so you **must** keep $(-1)^k$. Forgetting the sign will give a completely wrong answer.

The safest approach:
1. Write out the two general terms separately.
2. Let the total exponent match the required power.
3. Use a table or systematic enumeration to list all possible $(r,k)$ pairs.

#### 3. Binomial coefficient vs full coefficient of a term

This is where many students lose marks:

- **Binomial coefficient**: only $\binom{n}{r}$
- **Full coefficient**: $\binom{n}{r}$ multiplied by any constant factors and signs from $a$ and $b$

For example, in $(1-2x)^5$, the $x^3$ term:

- Binomial coefficient: $\binom{5}{3}=10$
- Full coefficient: $\binom{5}{3}(1)^2(-2)^3 = 10\times(-8) = -80$

So if the question asks for the "coefficient of $x^3$", the answer is $-80$; if it asks for the "binomial coefficient of $x^3$", the answer is $10$.

#### 4. Speed tips for non-calculator exams

- See "queuing, ranking, passwords, seating" → think **permutation** $^nP_r$
- See "selecting people, forming teams, committees, lottery" → think **combination** $^nC_r$
- To find the constant term, set the total exponent of $x$ to $0$
- Substitute $x=1$ to verify: the sum of all coefficients equals the original expression evaluated at $x=1$

---

### 1.3.4 Properties of Binomial Coefficients (Pascal's Triangle)

**Symmetry**:

$$
\boxed{\binom{n}{r} = \binom{n}{n-r}}
$$

**Pascal's Rule** (Recurrence relation):

$$
\boxed{\binom{n}{r} + \binom{n}{r-1} = \binom{n+1}{r}}
$$

**Pascal's Triangle**:

```
n=0:        1
n=1:       1 1
n=2:      1 2 1
n=3:     1 3 3 1
n=4:    1 4 6 4 1
n=5:   1 5 10 10 5 1
```

> **Exam tip**: For $n \le 5$, you can write coefficients directly using Pascal's Triangle; for $n \ge 6$, use the combination formula $\binom{n}{r}$.

> **Not examined** (syllabus explicitly states): Greatest term and properties of coefficients are **not** required.

---

## Chapter Formula Reference Table

| Topic | Formula | Conditions |
|:----|:----|:----|
| AP $n$th term | $a_n = a + (n-1)d$ | — |
| AP sum of first $n$ terms | $S_n = \dfrac{n}{2}[2a + (n-1)d]$ | — |
| GP $n$th term | $a_n = a r^{\,n-1}$ | — |
| GP sum of first $n$ terms | $S_n = a\dfrac{1-r^n}{1-r}$ | $r \neq 1$ |
| GP sum to infinity | $S_\infty = \dfrac{a}{1-r}$ | $\lvert r\rvert < 1$ |
| Permutations | $^nP_r = \dfrac{n!}{(n-r)!}$ | Order matters |
| Combinations | $\displaystyle\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | Order does not matter |
| Binomial theorem | $(a+b)^n = \displaystyle\sum_{r=0}^{n}\binom{n}{r}a^{n-r}b^{r}$ | $n \in \mathbb{Z}^+$ |
| General term | $T_{r+1} = \displaystyle\binom{n}{r}a^{n-r}b^{r}$ | For finding specific terms |

---
---
