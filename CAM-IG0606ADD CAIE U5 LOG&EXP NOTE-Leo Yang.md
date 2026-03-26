# U5 – Logarithmic and Exponential Functions[not classify with course book]

## 5.1 Definitions & Basic Properties

### Logarithms

For \(a > 0,\ a \neq 1\) and \(x > 0\):
\[
y = \log_a x \quad\Longleftrightarrow\quad a^y = x
\]

- \(\log_a x\) is the **power** you raise \(a\) to get \(x\).  
- In IGCSE 0606, \(\log_{10}x\) is often written as \(\lg x\).  
- Natural logarithm: \(\ln x = \log_e x\), where \(e \approx 2.718\).

**Common values**:  
\(\lg 10 = 1,\quad \lg 100 = 2,\quad \ln e = 1,\quad \ln 1 = 0\)

---

### Exponential Functions

For \(a > 0,\ a \neq 1\):
\[
y = a^x
\]

---

## 5.2 Laws of Logarithms

| Rule (in symbols) | Example |
|------------------|---------|
| \(\log_a (MN) = \log_a M + \log_a N\) | \(\lg(2\times5) = \lg2 + \lg5\) |
| \(\log_a \frac{M}{N} = \log_a M - \log_a N\) | \(\lg\frac{100}{10} = \lg100 - \lg10 = 2 - 1 = 1\) |
| \(\log_a (M^k) = k \log_a M\) | \(\lg(10^3) = 3\lg10 = 3\) |
| \(\log_a a = 1\) | \(\lg10 = 1\) |
| \(\log_a 1 = 0\) | \(\lg1 = 0\) |

> **Note**: These rules work for any base \(a\) (\(a>0,\ a\neq1\)).  
> “Addition” outside the log becomes multiplication inside; “subtraction” becomes division; multiplication outside becomes power inside.

---

## 5.3 Graphs – Exponential vs Logarithmic

### Exponential \(y = a^x\)

| \(a > 1\) | \(0 < a < 1\) |
|----------|--------------|
| Passes through \((0,1)\) | Passes through \((0,1)\) |
| Increasing | Decreasing |
| \(x\)-axis (\(y=0\)) is a **horizontal asymptote** | \(x\)-axis (\(y=0\)) is a **horizontal asymptote** |
| As \(x \to -\infty,\ y \to 0^+\) | As \(x \to +\infty,\ y \to 0^+\) |
| As \(x \to +\infty,\ y \to +\infty\) | As \(x \to -\infty,\ y \to +\infty\) |

### Logarithmic \(y = \log_a x\)

| \(a > 1\) | \(0 < a < 1\) |
|----------|--------------|
| Passes through \((1,0)\) | Passes through \((1,0)\) |
| Increasing | Decreasing |
| \(y\)-axis (\(x=0\)) is a **vertical asymptote** | \(y\)-axis (\(x=0\)) is a **vertical asymptote** |
| As \(x \to 0^+,\ y \to -\infty\) | As \(x \to 0^+,\ y \to +\infty\) |
| As \(x \to +\infty,\ y \to +\infty\) | As \(x \to +\infty,\ y \to -\infty\) |

**Key symmetry**:  
\(y = \log_a x\) and \(y = a^x\) are **inverse functions**. Their graphs are reflections of each other in the line \(y = x\).

---

## 5.4 Domain and Range

| Function | Domain | Range |
|----------|--------|-------|
| \(y = a^x\) (\(a>0,\ a\neq1\)) | \(\mathbb{R}\) (all real numbers) | \(y > 0\) |
| \(y = \log_a x\) (\(a>0,\ a\neq1\)) | \(x > 0\) | \(\mathbb{R}\) |

**Important for composite functions**:
- For \(y = \ln(ax+b)\): **inside must be positive**, i.e. \(ax+b > 0\).  
- Example: \(f(x) = \ln(3-x)\) has domain \(3-x > 0 \Rightarrow x < 3\).

---

## 5.5 Solving Equations with Logs and Exponentials

### 5.5.1 Exponential Equations

**Method**: Take logs of both sides (usually \(\lg\) or \(\ln\)), then use the power rule.

**Example**: Solve \(5^x = 65\).

\[
\begin{aligned}
5^x &= 65 \\
\lg(5^x) &= \lg 65 \\
x \lg 5 &= \lg 65 \\
x &= \frac{\lg 65}{\lg 5} \approx 2.593
\end{aligned}
\]

### 5.5.2 Logarithmic Equations

**Method**: Combine logs using the laws, then convert to exponential form. **Always check the domain** (arguments of logs must be positive).

**Example**: Solve \(2\lg(4+x) = \lg(8+2x)\).

\[
\begin{aligned}
\lg(4+x)^2 &= \lg(8+2x) \\
(4+x)^2 &= 8+2x \\
x^2 + 8x + 16 &= 8 + 2x \\
x^2 + 6x + 8 &= 0 \\
(x+2)(x+4) &= 0 \\
x &= -2 \quad\text{or}\quad x = -4
\end{aligned}
\]

**Check domain**:  
\(4+x > 0 \Rightarrow x > -4\)  
\(8+2x > 0 \Rightarrow x > -4\)  

- \(x = -2\) is valid (\(-2 > -4\)) ✅  
- \(x = -4\) is **not** valid (\(4+(-4)=0\), log undefined) ❌  

**Solution**: \(x = -2\).

---

## 5.6 Change of Base Formula

\[
\log_a b = \frac{\log_c b}{\log_c a} \qquad (c > 0,\ c \neq 1)
\]

Commonly we use \(c = 10\) or \(c = e\):

\[
\log_a b = \frac{\lg b}{\lg a} \quad\text{or}\quad \log_a b = \frac{\ln b}{\ln a}
\]

**Special case**: \(\log_a b = \dfrac{1}{\log_b a}\) (when the two bases are swapped).

---

## 5.7 Transformations (Shifts)

### Exponential: \(y = a^{x} + c\)  
- Horizontal asymptote moves from \(y=0\) to \(y=c\).  
- Example: \(y = 2^x + 3\) has asymptote \(y=3\).

### Logarithmic: \(y = \log_a (x - h)\)  
- Vertical asymptote moves from \(x=0\) to \(x=h\).  
- Example: \(y = \ln(x-2)\) has asymptote \(x=2\).

---

## 5.8 A Typical “Mixed” Log Equation (from past papers)

**Problem**: Solve \(\displaystyle \frac{\ln(2x+3)}{\ln 5} = 2\).

**Solution**:

\[
\begin{aligned}
\frac{\ln(2x+3)}{\ln 5} &= 2 \\
\ln(2x+3) &= 2\ln 5 \\
\ln(2x+3) &= \ln(5^2) \\
2x+3 &= 25 \\
2x &= 22 \\
x &= 11
\end{aligned}
\]

**Check domain**: \(2x+3 > 0 \Rightarrow 11 > -1.5\) ✅.

---

## 5.9 Inverse Functions

For \(y = a^x\): swap \(x\) and \(y\) → \(x = a^y\) → \(y = \log_a x\).  
So \(f(x) = a^x\) and \(f^{-1}(x) = \log_a x\) are inverses.

**Example**: Find the inverse of \(f(x) = e^{2x}\).

\[
\begin{aligned}
y &= e^{2x} \\
x &= e^{2y} \quad\text{(swap)}\\
\ln x &= 2y \\
y &= \frac{1}{2}\ln x
\end{aligned}
\]
Thus \(f^{-1}(x) = \frac12 \ln x\).

---

## 5.10 Summary – Key Points to Remember

- \(\log_a x\) is defined only for \(x>0\).  
- \(\log_a 1 = 0\), \(\log_a a = 1\).  
- Laws: \(\log(MN)=\log M+\log N\), \(\log(M/N)=\log M-\log N\), \(\log(M^k)=k\log M\).  
- Exponential \(y=a^x\) has horizontal asymptote \(y=0\); logarithmic \(y=\log_a x\) has vertical asymptote \(x=0\).  
- Transformations shift asymptotes: \(y=a^x+c\) shifts asymptote to \(y=c\); \(y=\log_a(x-h)\) shifts asymptote to \(x=h\).  
- When solving logarithmic equations, **always check domain** (arguments > 0).

---
---
# IGCSE 0606 Exponential and Logarithmic Functions (Chapter 5) – Problem-Solving Guide (Revised Edition)
-我真的服了，教辅书的编辑真的不知道真题考啥，怎么考吗？真的不知道这些东西怎么做才是对的吗，这个章节怎么只教释义啊！
---

## Step 1: Exponential Equations

**Core Goal**: Either make the bases the same, or take logarithms to bring the exponent down.

### 1. Same Base Method

- **When to use**: Both sides can be written as powers of the same number (e.g., 2, 3, e, 10).
- **Method**: If \(a^m = a^n\) (with \(a > 0\) and \(a \neq 1\)), then \(m = n\).
- **Tip**: When you see numbers like 2, 4, 8 or 3, 9, 27, rewrite them as powers of the same base (e.g., \(8 = 2^3\), \(27 = 3^3\)).
- **Example**: \(2^{x+1} = 8\) → \(2^{x+1} = 2^3\) → \(x+1 = 3\) → \(x = 2\).

### 2. Taking Logarithms Method

- **When to use**: Bases cannot be made the same (e.g., \(2^x = 5\), \(e^{2x} = 10\)).
- **Method**: Take \(\ln\) (natural log) or \(\lg\) (common log) of both sides. Then use the power rule: \(\ln(a^b) = b \ln a\).
- **Tip**: If the equation contains \(e\) (the natural exponential), use \(\ln\) because \(\ln e = 1\) simplifies the working.
- **Important**: You must take logs of **both sides** together. You cannot take logs of only one side.
  - ✅ Correct: \(2^x = 5\) → \(\lg(2^x) = \lg 5\) → \(x \lg 2 = \lg 5\) → \(x = \frac{\lg 5}{\lg 2}\)
  - ❌ Wrong: \(2^x = 5\) → \(x = \lg 5\) (this loses the factor \(\lg 2\))

---

## Step 2: Logarithmic Equations

**Core Goal**: Use logarithm laws to combine or split terms. **Always check the domain** – the argument of every logarithm must be positive.

### 1. Change of Base

- **Formula**: \(\displaystyle \log_a b = \frac{\log_c b}{\log_c a}\) (usually choose \(c = 10\) or \(c = e\)).
- **Useful form**: \(\displaystyle \log_a b = \frac{1}{\log_b a}\).
- **Example**: Simplify \(\log_5 10\) → \(\frac{\lg 10}{\lg 5} = \frac{1}{\lg 5}\).

### 2. Laws of Logarithms

| Law | Formula | Example |
|-----|---------|---------|
| Addition | \(\log_a M + \log_a N = \log_a (MN)\) | \(\lg 2 + \lg 5 = \lg(2\times5) = \lg 10 = 1\) |
| Subtraction | \(\log_a M - \log_a N = \log_a \left(\frac{M}{N}\right)\) | \(\lg 100 - \lg 10 = \lg(100/10) = \lg 10 = 1\) |
| Power rule | \(\log_a (M^k) = k \log_a M\) | \(\lg(10^3) = 3\lg 10 = 3\) |

- **Exam focus**: Many questions ask you to simplify an expression into the form \(c + d\log y\). To do this, you split products and quotients using addition/subtraction rules, then use the power rule to move coefficients.

### 3. ⚠️ Critical Warning: Extraneous Solutions

- After solving a logarithmic equation, **substitute your solutions back into the original equation**.
- Any solution that makes any logarithm’s argument ≤ 0 must be rejected.
- **Example**: Solve \(\lg(x-1) + \lg(x+1) = 0\)  
  → \(\lg[(x-1)(x+1)] = 0\) → \((x-1)(x+1) = 1\) → \(x^2 - 1 = 1\) → \(x^2 = 2\) → \(x = \sqrt{2}\) or \(x = -\sqrt{2}\).
  - \(x = \sqrt{2} \approx 1.41\) → \(x-1 > 0\), \(x+1 > 0\) ✅
  - \(x = -\sqrt{2} \approx -1.41\) → \(x-1 < 0\) ❌ (argument of first log is negative) → reject.

---

## Step 3: Quadratic-Type Exponential/Logarithmic Equations

**Core Goal**: Use substitution to turn the equation into a quadratic.

### Substitution Method

- **When to use**: The equation contains a term and its square, e.g., \(5^x\) and \(5^{2x} = (5^x)^2\), or \(\ln x\) and \((\ln x)^2\).
- **Method**:
  1. Let \(y = 5^x\) (or \(y = \ln x\), etc.).
  2. The equation becomes a quadratic in \(y\): \(ay^2 + by + c = 0\).
  3. Solve for \(y\).
  4. **Replace \(y\) back**: solve \(5^x = y\) (or \(e^x = y\), etc.) for \(x\).
- **Important**: If \(y = 5^x\), then \(y\) must be **positive** (exponential functions only give positive outputs). If you get a negative \(y\), discard it.
- **Example**: \(3^{2x} - 4\cdot3^x + 3 = 0\)  
  Let \(y = 3^x\). Then \(y^2 - 4y + 3 = 0\) → \((y-1)(y-3)=0\) → \(y = 1\) or \(y = 3\).  
  - \(3^x = 1\) → \(x = 0\)  
  - \(3^x = 3\) → \(x = 1\)  
  Both solutions are valid (no negative \(y\)).

---

## Step 4: Simultaneous Exponential Equations

**Core Goal**: Reduce to a system of linear equations by expressing everything with the same prime base.

### Method: Prime Base Reduction

- **When to use**: Equations like \(8^q = 2^{p+1}\) and \(4^p = 2^{q}\).
- **Steps**:
  1. Write each number as a power of a prime (2, 3, 5, etc.).
  2. Use the power rule: \((a^m)^n = a^{mn}\).
  3. Equate exponents to form linear equations.
  4. Solve the linear system.
- **Example**: \(8^q = 2^{p+1}\) and \(4^p = 2^{q}\).
  - \(8^q = (2^3)^q = 2^{3q}\) → so \(3q = p+1\)
  - \(4^p = (2^2)^p = 2^{2p}\) → so \(2p = q\)
  - Solve: \(q = 2p\) → substitute into \(3(2p) = p+1\) → \(6p = p+1\) → \(5p = 1\) → \(p = 0.2\), \(q = 0.4\).

---

## Step 5: Domain, Graphs and Transformations

**Core Goal**: Understand the restrictions on \(x\) and how shifting changes the graph.

### 1. Domain Restrictions for Logarithms

- For \(\log_b(f(x))\), we require \(f(x) > 0\).
- If there are multiple logarithms, **take the intersection** of all their domain conditions.
- **Example**: \(\ln(x-2) + \ln(5-x)\) requires \(x-2 > 0\) AND \(5-x > 0\) → \(x > 2\) and \(x < 5\) → domain \(2 < x < 5\).

### 2. Finding Intersections Graphically

- If you see a problem like \(a^x = kx + b\), it often asks for the number of solutions.
- Sketch \(y = a^x\) and \(y = kx + b\) (a line). Count their intersection points.
- For exact intersection (e.g., \(\log_a x = c\)), convert to exponential form: \(x = a^c\).

### 3. Transformations (Shifting Asymptotes)

- **Exponential**: \(y = a^x + c\)  
  - Horizontal asymptote moves from \(y = 0\) to \(y = c\).  
  - Example: \(y = 2^x + 3\) has asymptote \(y = 3\).
- **Logarithmic**: \(y = \ln(x - h)\)  
  - Vertical asymptote moves from \(x = 0\) to \(x = h\).  
  - Example: \(y = \ln(x-2)\) has asymptote \(x = 2\), domain \(x > 2\).

---

## Step 6: Solving Quadratic Forms (Again, but with Logs)

**Core Goal**: Recognize when a substitution turns a logarithmic equation into a quadratic.

### Factoring After Substitution

- **When to use**: The equation contains \(\ln(5x)\) and \((\ln(5x))^2\).
- **Method**: Let \(u = \ln(5x)\). Solve \(au^2 + bu + c = 0\) by factoring or the quadratic formula.
- **Important trap**: \(\ln(5x)\) is **not** equal to \(\ln 5 \cdot \ln x\). The power rule only applies when the **argument** is raised to a power, not when the whole logarithm is multiplied.

- **Example**: \(3(\ln 5x)^2 + 2\ln 5x - 1 = 0\)  
  Let \(u = \ln 5x\). Then \(3u^2 + 2u - 1 = 0\) → \((3u - 1)(u + 1) = 0\) → \(u = \frac{1}{3}\) or \(u = -1\).  
  - \(\ln 5x = \frac13\) → \(5x = e^{1/3}\) → \(x = \frac{1}{5}e^{1/3}\)  
  - \(\ln 5x = -1\) → \(5x = e^{-1}\) → \(x = \frac{1}{5e}\)

---

## Additional Topics

### Parameter Problems (Equations with Unknown Constants)

- **When to use**: The problem says “the equation has exactly one solution”, “no real solution”, etc.
- **Strategy**:
  - For equations like \(2^x = k - x\), think about the graphs: \(y = 2^x\) (exponential) and \(y = k - x\) (a straight line with slope -1). The number of solutions is the number of intersection points.
  - For quadratic forms after substitution, use the discriminant: \(\Delta = 0\) gives one solution, \(\Delta > 0\) gives two, etc., **but** remember to check domain restrictions on the substituted variable (e.g., \(y = 5^x > 0\)).

### Applications: Exponential Growth/Decay

- **Standard forms**:  
  - \(N = N_0 e^{kt}\) (continuous growth, e.g., bacteria, radioactive decay)  
  - \(N = N_0 a^t\) (discrete growth, e.g., compound interest)
- **How to solve**:
  1. Identify \(N_0\) (initial value) from the context.
  2. Use one data point to find the growth factor \(k\) or \(a\).
  3. Answer the question (find a value, find time, etc.).
- **Example**: A population starts at 100 and triples every 2 hours. Find a formula and the population after 5 hours.  
  - \(P = 100 \cdot 3^{t/2}\) (because after 2 hours, multiply by 3)  
  - After 5 hours: \(P = 100 \cdot 3^{2.5} = 100 \cdot 3^{5/2} = 100 \cdot 3^2 \cdot \sqrt{3} = 900\sqrt{3}\)

---

## Exam Checklist

Before you start, ask yourself:

1. **Bases**: Are the bases the same? If yes, equate exponents. If not, take logs.
2. **Structure**: Do you see \(a^x\) and \(a^{2x}\)? Use substitution to form a quadratic.
3. **Operations**: Are you adding/subtracting logs? Combine them into a single log.
4. **Domain**: If it’s a logarithmic equation, **always check** that solutions make all arguments positive.
5. **Coefficients**: In simultaneous equations, write everything with prime bases, then compare exponents.
6. **Graphs**: If the question asks for number of solutions or parameter ranges, sketch the two graphs.
7. **Applications**: For growth/decay, identify the initial value and use one data point to find the growth constant.

---

## One‑Line Summary

> **Exponentials take logs, logarithms need domain checks, change of base simplifies, graphs focus on asymptotes, substitution solves quadratics, and simultaneous equations reduce to prime bases.**
