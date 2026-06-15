# IGCSE 0606 Additional Mathematics 考纲深度解读与扩展 — 主题 9~14

> 本文档基于 **Cambridge IGCSE Additional Mathematics (0606) 2025–2027 考纲**，对主题 9–14 进行逐条解读、公式梳理、典型例题与易错点分析。
> 适合考前复习与知识体系梳理。

---

## 目录

- [9 Circular Measure 圆弧度量](#9-circular-measure-圆弧度量)
- [10 Trigonometry 三角学](#10-trigonometry-三角学)
- [11 Permutations and Combinations 排列与组合](#11-permutations-and-combinations-排列与组合)
- [12 Series 数列与级数](#12-series-数列与级数)
- [13 Vectors in Two Dimensions 二维向量](#13-vectors-in-two-dimensions-二维向量)
- [14 Calculus 微积分](#14-calculus-微积分)

---

# 9 Circular Measure 圆弧度量

## 9.1 弧长与扇形面积（弧度制）

> **考纲要求**: Solve problems involving the arc length and sector area of a circle, including knowledge and use of radian measure. Use of radian measure is expected in the solution of problems which may involve compound shapes. **Formulas are not given.**

### 📌 核心公式（必须牢记！）

| 公式 | 表达式 | 说明 |
|:----|:-------|:-----|
| 弧度定义 | $\theta = \dfrac{s}{r}$ | $\theta$ 为圆心角（弧度），$s$ 为弧长，$r$ 为半径 |
| 弧长 | $s = r\theta$ | $\theta$ **必须为弧度** |
| 扇形面积 | $A = \dfrac{1}{2}r^2\theta$ | $\theta$ **必须为弧度** |
| 弓形面积 | $A = \dfrac{1}{2}r^2(\theta - \sin\theta)$ | 扇形减三角形 |
| 角度↔弧度 | $180^\circ = \pi\ \text{rad}$ | $1^\circ = \dfrac{\pi}{180}\ \text{rad}$，$1\ \text{rad} = \dfrac{180^\circ}{\pi}$ |

### 🔍 常见角度换算

| 度 | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|:--:|:---------:|:----------:|:----------:|:----------:|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| 弧度 | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

### 📝 典型例题

**例1**：扇形半径 $12$ cm，圆心角 $\dfrac{2\pi}{3}$，求弧长和扇形面积。

解：
$$
s = r\theta = 12 \times \frac{2\pi}{3} = 8\pi\ \text{cm}
$$
$$
A = \frac{1}{2}r^2\theta = \frac{1}{2} \times 144 \times \frac{2\pi}{3} = 48\pi\ \text{cm}^2
$$

**例2**（复合图形）：一个大扇形半径 $5$ cm，小扇形半径 $3$ cm，共圆心角 $\dfrac{\pi}{3}$，求两扇形之间的面积。

解：
$$
A_{\text{large}} = \frac{1}{2} \times 5^2 \times \frac{\pi}{3} = \frac{25\pi}{6},\quad
A_{\text{small}} = \frac{1}{2} \times 3^2 \times \frac{\pi}{3} = \frac{3\pi}{2}
$$
$$
A = \frac{25\pi}{6} - \frac{3\pi}{2} = \frac{8\pi}{3}\ \text{cm}^2
$$

### ⚠️ 易错点

1. **$\theta$ 必须用弧度！** 如果用度数，公式需加上 $\dfrac{\pi}{180}$ 因子
2. **弓形面积**中 $\theta - \sin\theta$ 两个 $\theta$ 都是弧度
3. 复合图形中注意**统一单位**后再计算

---

# 10 Trigonometry 三角学

## 10.1 六种三角函数（任意角）

> **考纲要求**: Know and use the six trigonometric functions of angles of any magnitude. sine, cosine, tangent, secant, cosecant, cotangent.

### 📌 单位圆定义

对于角 $\theta$，终边与单位圆 $x^2 + y^2 = 1$ 交于 $P(x, y)$：

$$
\sin\theta = y,\quad \cos\theta = x,\quad \tan\theta = \frac{y}{x}\ (x \neq 0)
$$

### 📌 六种三角函数

| 函数 | 符号 | 定义 | 定义域限制 |
|:----|:----|:----|:----------|
| 正弦 | $\sin\theta$ | $y$ | 所有实数 |
| 余弦 | $\cos\theta$ | $x$ | 所有实数 |
| 正切 | $\tan\theta$ | $\dfrac{y}{x} = \dfrac{\sin\theta}{\cos\theta}$ | $\theta \neq \dfrac{\pi}{2} + n\pi$ |
| 余割 | $\csc\theta$ | $\dfrac{1}{y} = \dfrac{1}{\sin\theta}$ | $\theta \neq n\pi$ |
| 正割 | $\sec\theta$ | $\dfrac{1}{x} = \dfrac{1}{\cos\theta}$ | $\theta \neq \dfrac{\pi}{2} + n\pi$ |
| 余切 | $\cot\theta$ | $\dfrac{x}{y} = \dfrac{\cos\theta}{\sin\theta}$ | $\theta \neq n\pi$ |

### 📌 特殊角精确值

| $\theta$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ |
|:---------|:---:|:----------------:|:----------------:|:----------------:|:----------------:|:-----:|:-----------------:|
| $\sin$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ |
| $\cos$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\tan$ | $0$ | $\dfrac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | 无定义 | $0$ | 无定义 |

### 📌 ASTC 符号法则

| 象限 | 范围 | $\sin$ | $\cos$ | $\tan$ | 正号函数 |
|:----:|:-----|:------:|:------:|:------:|:---------|
| I | $0 < \theta < \dfrac{\pi}{2}$ | $+$ | $+$ | $+$ | **A**ll (全部) |
| II | $\dfrac{\pi}{2} < \theta < \pi$ | $+$ | $-$ | $-$ | **S**in (及 csc) |
| III | $\pi < \theta < \dfrac{3\pi}{2}$ | $-$ | $-$ | $+$ | **T**an (及 cot) |
| IV | $\dfrac{3\pi}{2} < \theta < 2\pi$ | $-$ | $+$ | $-$ | **C**os (及 sec) |

**记忆口诀**: **A**ll **S**tudents **T**ake **C**alculus

---

## 10.2 三角函数的振幅与周期

> **考纲要求**: Understand and use the amplitude and period of a trigonometric function, including the relationship between graphs of related trigonometric functions. For example: $y = \sin x$ and $y = 3\sin 2x$. The period may be in either degrees or radians.

### 📌 关键概念

对于 $y = a\sin(bx) + c$ 和 $y = a\cos(bx) + c$：

| 参数 | 含义 | 效果 |
|:----|:-----|:-----|
| $a$ | **振幅** (Amplitude) | 垂直方向拉伸/压缩，$a > 0$ |
| $b$ | **角频率** | 水平方向压缩/拉伸，周期 $T = \dfrac{2\pi}{b}$（弧度）或 $T = \dfrac{360^\circ}{b}$（度） |
| $c$ | **垂直位移** | 整个图像向上/下平移 |

对于 $y = a\tan(bx) + c$：
- 周期 $T = \dfrac{\pi}{b}$（弧度）或 $T = \dfrac{180^\circ}{b}$（度）
- 无振幅概念（$\tan$ 值域为 $\mathbb{R}$）

### 📝 示例

| 函数 | 振幅 | 周期 | 垂直位移 |
|:----|:----:|:----:|:--------:|
| $y = 3\sin 2x$ | $3$ | $\pi$（$180^\circ$） | $0$ |
| $y = -2\cos\frac{x}{2}$ | $2$ | $4\pi$（$720^\circ$） | $0$ |
| $y = 4\sin(3x) - 1$ | $4$ | $\frac{2\pi}{3}$（$120^\circ$） | $-1$ |
| $y = \tan\frac{x}{4}$ | — | $4\pi$（$720^\circ$） | $0$ |

---

## 10.3 三角函数图像绘制

> **考纲要求**: Draw and use the graphs of $y = a\sin bx + c$, $y = a\cos bx + c$, $y = a\tan bx + c$ where $a$ is a positive integer, $b$ is a simple fraction or integer, and $c$ is an integer. Graphs will be drawn over a given domain which may be in either degrees or radians. For $y = a\tan bx + c$, the $x$-coordinate of any asymptote should be clearly labelled. Fractions will have a denominator of $2, 3, 4, 6$ or $8$ only.

### 📌 绘图步骤

1. **确定周期**: $T = \dfrac{2\pi}{b}$（$\sin$/$\cos$）或 $T = \dfrac{\pi}{b}$（$\tan$）
2. **确定振幅**（仅 $\sin$/$\cos$）: $a$
3. **确定垂直位移**: $c$
4. **找出关键点**: 最大值、最小值、零点、渐近线（$\tan$）
5. **在给定定义域内绘制**

### 📝 示例

**例**：绘制 $y = 3\sin 2x + 1$ 在 $0 \leq x \leq 2\pi$ 的图像。

- 振幅 $= 3$，周期 $= \pi$，垂直位移 $= 1$
- 最大值 $= 4$，最小值 $= -2$
- 关键点间距 $= \dfrac{\pi}{4}$

**例**：绘制 $y = 2\tan\frac{x}{2}$，标出渐近线。

- 周期 $= 2\pi$，渐近线在 $x = \pi, 3\pi, 5\pi, \dots$

---

## 10.4 三角恒等式

> **考纲要求**: Use the relationships: $\sin^2 A + \cos^2 A = 1$, $\sec^2 A = 1 + \tan^2 A$, $\csc^2 A = 1 + \cot^2 A$. Trigonometric identities are given in the List of formulas.

### 📌 三大恒等式（公式表已给出）

1. **$\boxed{\sin^2 A + \cos^2 A = 1}$**
2. **$\boxed{\sec^2 A = 1 + \tan^2 A}$**
3. **$\boxed{\csc^2 A = 1 + \cot^2 A}$**

### 🔍 推导关系

由 $\sin^2 A + \cos^2 A = 1$ 两边除以 $\cos^2 A$：
$$
\tan^2 A + 1 = \sec^2 A \quad\Rightarrow\quad \sec^2 A = 1 + \tan^2 A
$$

由 $\sin^2 A + \cos^2 A = 1$ 两边除以 $\sin^2 A$：
$$
1 + \cot^2 A = \csc^2 A \quad\Rightarrow\quad \csc^2 A = 1 + \cot^2 A
$$

### ⚠️ 易错点

- $\sin^2 A$ 表示 $(\sin A)^2$，不是 $\sin(A^2)$
- $\sec A = \dfrac{1}{\cos A}$，$\csc A = \dfrac{1}{\sin A}$，$\cot A = \dfrac{1}{\tan A}$
- 不要混淆 $\sec$ 和 $\csc$ 的倒数关系

---

## 10.5 解三角方程

> **考纲要求**: Solve, for a given domain, trigonometric equations involving the six trigonometric functions. Includes the use of the relationships in 10.4.

### 📌 解题策略

1. **利用恒等式化简**为一个三角函数
2. **换元**（令 $u = \text{trig function}$）转化为代数方程
3. **求基本角**（参考角）
4. **利用 ASTC 确定所有解**（在给定定义域内）

### 📝 典型例题

**例1**：解 $4\cot\theta = \tan\theta$，$0^\circ < \theta < 360^\circ$。

解：
$$
4\cot\theta = \tan\theta \quad\Rightarrow\quad \frac{4}{\tan\theta} = \tan\theta \quad\Rightarrow\quad \tan^2\theta = 4 \quad\Rightarrow\quad \tan\theta = \pm 2
$$

$\tan\theta = 2$：参考角 $\alpha = \arctan 2 \approx 63.43^\circ$，解在 I、III 象限
$\tan\theta = -2$：参考角 $\alpha = \arctan 2 \approx 63.43^\circ$，解在 II、IV 象限

综合：$\theta \approx 63.43^\circ, 116.57^\circ, 243.43^\circ, 296.57^\circ$

**例2**：解 $2\sec^2\theta + \tan\theta - 3 = 0$，$0 \leq \theta \leq 2\pi$。

解：利用 $\sec^2\theta = 1 + \tan^2\theta$：
$$
2(1 + \tan^2\theta) + \tan\theta - 3 = 0 \quad\Rightarrow\quad 2\tan^2\theta + \tan\theta - 1 = 0
$$
令 $u = \tan\theta$：$2u^2 + u - 1 = 0 \quad\Rightarrow\quad (2u-1)(u+1) = 0$
$$
\tan\theta = \frac{1}{2} \quad\text{或}\quad \tan\theta = -1
$$

再分别求解，注意 ASTC。

**例3**：解 $5\sin 3\theta + 2\cos 3\theta = 0$，$0 \leq \theta \leq \pi$。

解：
$$
5\sin 3\theta = -2\cos 3\theta \quad\Rightarrow\quad \frac{\sin 3\theta}{\cos 3\theta} = -\frac{2}{5} \quad\Rightarrow\quad \tan 3\theta = -\frac{2}{5}
$$

参考角 $\alpha = \arctan(0.4) \approx 0.3805$ rad
$3\theta = \pi - \alpha, 2\pi - \alpha, 3\pi - \alpha, \dots$
$\theta = \dfrac{\pi - \alpha}{3}, \dfrac{2\pi - \alpha}{3}, \dfrac{3\pi - \alpha}{3}, \dots$，再筛选在 $[0, \pi]$ 内的解。

**例4**：解 $3\csc\left(2\theta - \dfrac{\pi}{2}\right) = 4$。

解：
$$
\csc\left(2\theta - \frac{\pi}{2}\right) = \frac{4}{3} \quad\Rightarrow\quad \sin\left(2\theta - \frac{\pi}{2}\right) = \frac{3}{4}
$$

令 $u = 2\theta - \dfrac{\pi}{2}$，解 $\sin u = \dfrac{3}{4}$，再回代求 $\theta$。

---

## 10.6 三角恒等式证明

> **考纲要求**: Prove trigonometric relationships involving the six trigonometric functions. Includes the use of the relationships in 10.4.

### 📌 证明策略

1. 从较复杂的一边开始
2. 将所有函数转化为 $\sin$ 和 $\cos$
3. 通分、合并、因式分解
4. 利用恒等关系（$\sin^2 + \cos^2 = 1$ 等）

### 📝 典型例题

**例1**：证明 $\sin x\tan x + \cos x = \sec x$。

证明：
$$
\text{LHS} = \sin x \cdot \frac{\sin x}{\cos x} + \cos x = \frac{\sin^2 x}{\cos x} + \cos x = \frac{\sin^2 x + \cos^2 x}{\cos x} = \frac{1}{\cos x} = \sec x = \text{RHS}
$$

**例2**：证明 $\dfrac{\cos\theta}{1 + \sin\theta} + \dfrac{1 + \sin\theta}{\cos\theta} = 2\sec\theta$。

证明：
$$
\text{LHS} = \frac{\cos^2\theta + (1 + \sin\theta)^2}{\cos\theta(1 + \sin\theta)} = \frac{\cos^2\theta + 1 + 2\sin\theta + \sin^2\theta}{\cos\theta(1 + \sin\theta)} = \frac{2 + 2\sin\theta}{\cos\theta(1 + \sin\theta)} = \frac{2(1 + \sin\theta)}{\cos\theta(1 + \sin\theta)} = \frac{2}{\cos\theta} = 2\sec\theta
$$

### ⚠️ 易错点

- 不能假设结论成立，必须从一边推导到另一边
- 分式化简时注意通分
- 不要忘记 $\sin^2\theta + \cos^2\theta = 1$ 的灵活运用

---

# 11 Permutations and Combinations 排列与组合

## 11.1 排列与组合的区别

> **考纲要求**: Recognise the difference between permutations and combinations and know when each should be used.

### 📌 核心区别

| | **排列 (Permutation)** | **组合 (Combination)** |
|:----|:---------------------|:---------------------|
| **关键概念** | **顺序重要** (Order matters) | **顺序不重要** (Order doesn't matter) |
| **典型问题** | 排队、密码、排列座位 | 选委员会、抽奖、选球队 |
| **关键词** | arrange, order, sequence | choose, select, group |

### 📝 判断方法

问自己：**"交换两个元素会得到不同的结果吗？"**
- 会 → 排列 (Permutation)
- 不会 → 组合 (Combination)

---

## 11.2 阶乘与排列组合公式

> **考纲要求**: Know and use the notation $n!$ and the expressions for permutations and combinations of $n$ items taken $r$ at a time. Includes $0! = 1$.

### 📌 核心公式

$$
\begin{aligned}
n! &= n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1 \\
0! &= 1 \quad \text{(规定)} \\
{}^nP_r &= \frac{n!}{(n-r)!} \quad \text{（从 $n$ 个中选 $r$ 个排列）} \\
{}^nC_r &= \binom{n}{r} = \frac{n!}{r!(n-r)!} \quad \text{（从 $n$ 个中选 $r$ 个组合）}
\end{aligned}
$$

### 📝 示例

$$
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
$$
$$
{}^6P_2 = \frac{6!}{4!} = 6 \times 5 = 30
$$
$$
\binom{8}{3} = \frac{8!}{3!5!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56
$$

---

## 11.3 排列组合应用问题

> **考纲要求**: Solve problems on arrangement or selection using permutations or combinations. Problems will be either in an everyday context or based on an algebraic problem.
>
> **不考**：重复元素、圆形排列、排列组合混合使用。

### 📌 解题步骤

1. **确定是排列还是组合**（顺序是否重要）
2. **确定 $n$ 和 $r$**
3. **代入公式**
4. **检查合理性**

### 📝 典型例题

**例1（排列）**：5 本书放在书架上，有多少种排法？

解：$5! = 120$ 种

**例2（排列）**：从 10 个学生中选 3 个分别担任班长、副班长、学习委员，有多少种选法？

解：${}^{10}P_3 = 10 \times 9 \times 8 = 720$ 种

**例3（组合）**：从 10 个学生中选 3 个组成委员会，有多少种选法？

解：$\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$ 种

**例4（代数背景）**：展开 $(x + y)^5$ 中 $x^3y^2$ 的系数是多少？

解：$\binom{5}{3} = 10$（或 $\binom{5}{2} = 10$）

**例5（限制条件）**：从 7 男 5 女中选 4 人，要求至少 2 名女生，有多少种选法？

解：分类讨论：
- 2 女 2 男：$\binom{5}{2} \times \binom{7}{2} = 10 \times 21 = 210$
- 3 女 1 男：$\binom{5}{3} \times \binom{7}{1} = 10 \times 7 = 70$
- 4 女：$\binom{5}{4} = 5$

总计 $210 + 70 + 5 = 285$ 种

### ⚠️ 易错点

1. 混淆排列与组合——始终问"顺序是否重要"
2. 忘记 $0! = 1$
3. ${}^nP_r$ 与 ${}^nC_r$ 公式记混

---

# 12 Series 数列与级数

## 12.1 二项式定理

> **考纲要求**: Use the binomial theorem for expansion of $(a + b)^n$ for positive integer $n$. Includes simplification of coefficients. Formula is given in the List of formulas.

### 📌 二项式展开公式（公式表已给出）

$$
(a + b)^n = a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{r}a^{n-r}b^r + \cdots + b^n
$$

其中 $\displaystyle\binom{n}{r} = \frac{n!}{r!(n-r)!}$，$n \in \mathbb{Z}^+$。

---

## 12.2 通项公式

> **考纲要求**: Use the general term $\displaystyle\binom{n}{r}a^{n-r}b^r$, $0 \le r \le n$. Knowledge of the greatest term and properties of the coefficients is not required.

### 📌 通项

$$
T_{r+1} = \binom{n}{r} a^{n-r} b^r
$$

### 📝 典型例题

**例**：求 $\left(x^2 + \frac{1}{x}\right)^{10}$ 的展开式中常数项。

解：
通项：$T_{r+1} = \binom{10}{r}(x^2)^{10-r}\left(\frac{1}{x}\right)^r = \binom{10}{r} x^{20-2r} x^{-r} = \binom{10}{r} x^{20-3r}$

令 $20 - 3r = 0 \Rightarrow r = \frac{20}{3}$，非整数 ⇒ **无常数项**。

**例2**：求 $\left(2x^3 - \frac{1}{x}\right)^8$ 中 $x^8$ 的系数。

解：
通项：$T_{r+1} = \binom{8}{r}(2x^3)^{8-r}\left(-\frac{1}{x}\right)^r = \binom{8}{r} 2^{8-r} (-1)^r x^{24-3r} x^{-r} = \binom{8}{r} 2^{8-r} (-1)^r x^{24-4r}$

令 $24 - 4r = 8 \Rightarrow r = 4$

系数：$\binom{8}{4} \times 2^{4} \times (-1)^4 = 70 \times 16 \times 1 = 1120$

---

## 12.3 等差数列与等比数列的识别

> **考纲要求**: Recognise arithmetic and geometric progressions and understand the difference between them.

### 📌 对比

| 特征 | **等差数列 (AP)** | **等比数列 (GP)** |
|:----|:----------------|:----------------|
| 定义 | $a_{n+1} - a_n = d$（公差常数） | $\dfrac{a_{n+1}}{a_n} = r$（公比常数） |
| 检验方法 | 相邻项相减，差为常数 | 相邻项相除，比为常数 |
| 增长模式 | **线性增长** | **指数增长/衰减** |

---

## 12.4 通项与求和公式

> **考纲要求**: Use the formulas for the $n$th term and for the sum of the first $n$ terms to solve problems involving arithmetic or geometric progressions. Problems may be in context. Formulas are given in the List of formulas.

### 📌 公式汇总

**等差数列 (AP)**：
$$
\begin{aligned}
a_n &= a + (n-1)d \\
S_n &= \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + l) \quad (\text{其中 } l = a_n)
\end{aligned}
$$

**等比数列 (GP)**：
$$
\begin{aligned}
a_n &= a r^{\,n-1} \\
S_n &= \begin{cases}
a \cdot \dfrac{1 - r^n}{1 - r}, & r \neq 1 \\
na, & r = 1
\end{cases}
\end{aligned}
$$

### 📝 示例

**例1（AP）**：首项 $7$，公差 $3$，求第 $15$ 项。
$$
a_{15} = 7 + 14 \times 3 = 49
$$

**例2（AP 实际应用）**：第一年存 $500$，以后每年增加 $50$，$10$ 年共存多少？
$$
S_{10} = \frac{10}{2}[2 \times 500 + 9 \times 50] = 5 \times (1000 + 450) = 7250
$$

**例3（GP）**：首项 $3$，公比 $2$，求第 $6$ 项。
$$
a_6 = 3 \times 2^5 = 96
$$

---

## 12.5 无穷等比级数的收敛性与和

> **考纲要求**: Use the condition for the convergence of a geometric progression, and the formula for the sum to infinity of a convergent geometric progression. Includes explaining why a particular geometric progression has or does not have a sum to infinity. Formula is given in the List of formulas.

### 📌 收敛条件

无穷等比级数 $\displaystyle\sum_{k=0}^{\infty} a r^{\,k}$ 收敛当且仅当 $|r| < 1$。

$$
S_\infty = \frac{a}{1-r} \quad (|r| < 1)
$$

### 📝 解释收敛/发散的标准答案模板

> "当 $|r| < 1$ 时，$n \to \infty$ 时 $r^{\,n} \to 0$，所以 $S_n \to \dfrac{a}{1-r}$；当 $|r| \ge 1$ 时，$r^{\,n}$ 不趋近于 $0$，所以 $S_n$ 不趋近于有限值。"

### 📝 示例

**例**：$12 + 6 + 3 + \frac{3}{2} + \cdots$ 是否收敛？若收敛，求和。

解：$a = 12$，$r = \frac{6}{12} = \frac{1}{2}$
因 $|r| = \frac{1}{2} < 1$，$n \to \infty$ 时 $(\frac{1}{2})^n \to 0$，级数收敛。

$$
S_\infty = \frac{12}{1 - \frac{1}{2}} = \frac{12}{\frac{1}{2}} = 24
$$

### ⚠️ 易错点

- 只有 $|r| < 1$ 时无穷等比级数才有和
- $S_\infty$ 公式中 $a$ 是**首项**
- 解释收敛性时须说明 $r^{\,n} \to 0$ 的过程

---

# 13 Vectors in Two Dimensions 二维向量

## 13.1 向量表示法

> **考纲要求**: Understand and use vector notation.

### 📌 向量形式

向量可以用多种方式表示：
$$
\mathbf{a} = \begin{pmatrix}a_1 \\ a_2\end{pmatrix} = a_1\mathbf{i} + a_2\mathbf{j} = \overrightarrow{AB}
$$

其中 $\mathbf{i} = \begin{pmatrix}1 \\ 0\end{pmatrix}$ 为 $x$ 方向单位向量，$\mathbf{j} = \begin{pmatrix}0 \\ 1\end{pmatrix}$ 为 $y$ 方向单位向量。

---

## 13.2 位置向量与单位向量

> **考纲要求**: Know and use position vectors and unit vectors. For example: The unit vector in the same direction as $\mathbf{a}$ is $\dfrac{\mathbf{a}}{|\mathbf{a}|}$.

### 📌 关键概念

- **位置向量 (Position vector)**：$\overrightarrow{OP} = \begin{pmatrix}x \\ y\end{pmatrix}$，表示点 $P$ 相对于原点 $O$ 的位置
- **单位向量 (Unit vector)**：$\hat{\mathbf{a}} = \dfrac{\mathbf{a}}{|\mathbf{a}|}$，方向相同、长度为 $1$
- **向量模长 (Magnitude)**：$|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$

---

## 13.3 向量运算与几何应用

> **考纲要求**: Find the magnitude of a vector; add and subtract vectors and multiply vectors by scalars. Includes: equating like vectors; solving problems using vector geometry, with a diagram given in more complex cases.

### 📌 基本运算

**加法**：
$$
\begin{pmatrix}a_1 \\ a_2\end{pmatrix} + \begin{pmatrix}b_1 \\ b_2\end{pmatrix} = \begin{pmatrix}a_1 + b_1 \\ a_2 + b_2\end{pmatrix}
$$

**减法**：
$$
\begin{pmatrix}a_1 \\ a_2\end{pmatrix} - \begin{pmatrix}b_1 \\ b_2\end{pmatrix} = \begin{pmatrix}a_1 - b_1 \\ a_2 - b_2\end{pmatrix}
$$

**数乘**：
$$
k\begin{pmatrix}a_1 \\ a_2\end{pmatrix} = \begin{pmatrix}ka_1 \\ ka_2\end{pmatrix}
$$

**模长**：
$$
|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}
$$

### 📝 向量几何解题技巧

1. 用位置向量表示各点
2. $\overrightarrow{AB} = \mathbf{b} - \mathbf{a}$（重点！）
3. 平行条件：$\overrightarrow{AB} = k\overrightarrow{CD}$
4. 三等分点：$\overrightarrow{OP} = \frac{1}{3}\mathbf{a} + \frac{2}{3}\mathbf{b}$ 等

### 📝 典型例题

**例**：已知 $A(1,2)$，$B(4,6)$，求 $\overrightarrow{AB}$ 及其模长。

解：
$$
\overrightarrow{AB} = \begin{pmatrix}4-1 \\ 6-2\end{pmatrix} = \begin{pmatrix}3 \\ 4\end{pmatrix}, \quad |\overrightarrow{AB}| = \sqrt{3^2 + 4^2} = 5
$$

---

## 13.4 速度的合成与分解

> **考纲要求**: Compose and resolve velocities. Determine a resultant vector by adding two or more vectors together. Includes the use of a velocity vector to determine position and solve problems in context such as particles colliding.

### 📌 关键概念

- **合速度 (Resultant velocity)**：多个速度向量的和
- **相对速度**：$\mathbf{v}_{A \text{ relative to } B} = \mathbf{v}_A - \mathbf{v}_B$
- 位置 $= \text{初始位置} + \text{速度} \times \text{时间}$

### 📝 典型例题

**例**：船在静水中速度 $3\ \text{m/s}$ 向东，河水速度 $2\ \text{m/s}$ 向南，求合速度大小和方向。

解：
$$
\mathbf{v} = \begin{pmatrix}3 \\ 0\end{pmatrix} + \begin{pmatrix}0 \\ -2\end{pmatrix} = \begin{pmatrix}3 \\ -2\end{pmatrix}
$$
$$
|\mathbf{v}| = \sqrt{3^2 + (-2)^2} = \sqrt{13} \approx 3.61\ \text{m/s}
$$
方向：$\theta = \arctan\left(\frac{2}{3}\right) \approx 33.7^\circ$ 南偏东

### ⚠️ 易错点

1. $\overrightarrow{AB} = \mathbf{b} - \mathbf{a}$，不是 $\mathbf{a} - \mathbf{b}$
2. 区分位置向量与位移向量
3. 向量平行不等于向量相等（方向相同或相反）

---

# 14 Calculus 微积分

> **⚠️ 考纲特别说明**: No formulas will be given in the List of formulas for the Calculus section. 所有公式**必须熟记**！

## 14.1 导数的概念

> **考纲要求**: Understand the idea of a derived function. Only an informal understanding of the idea of a limit is expected, and the technique of differentiation from first principles is not required.

### 📌 导数的含义

导数表示函数在某一点的变化率：
$$
f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

- **几何意义**：切线斜率
- **物理意义**：变化率（速度是位移的导数）

---

## 14.2 导数符号

> **考纲要求**: Use the notations $f'(x)$, $f''(x)$, $\dfrac{dy}{dx}$, $\dfrac{d^2y}{dx^2} = \dfrac{d}{dx}\left(\dfrac{dy}{dx}\right)$, $\delta x$, $\delta x \to 0$, $\dfrac{dy}{dx}$.

### 📌 常见记号

| 符号 | 含义 |
|:----|:-----|
| $f'(x)$ | 一阶导数 |
| $f''(x)$ | 二阶导数 |
| $\dfrac{dy}{dx}$ | 莱布尼茨记号 |
| $\dfrac{d^2y}{dx^2}$ | 二阶导数 |
| $\delta x$ | $x$ 的微小增量 |
| $\delta x \to 0$ | 表示极限过程 |

---

## 14.3 基本函数的导数

> **考纲要求**: Know and use the derivatives of the standard functions $x^n$ (for any rational $n$), $\sin x$, $\cos x$, $\tan x$, $e^x$, $\ln x$. Includes constant multiples, sums and composite functions (use of chain rule). For trigonometric functions angles will always be in radians.

### 📌 基本导数公式（必须熟记！）

$$
\begin{aligned}
\frac{d}{dx}(x^n) &= n x^{n-1} \quad (n \in \mathbb{Q}) \\
\frac{d}{dx}(\sin x) &= \cos x \\
\frac{d}{dx}(\cos x) &= -\sin x \\
\frac{d}{dx}(\tan x) &= \sec^2 x \\
\frac{d}{dx}(e^x) &= e^x \\
\frac{d}{dx}(\ln x) &= \frac{1}{x}
\end{aligned}
$$

### 📌 运算法则

**常数倍**：$\dfrac{d}{dx}[cf(x)] = cf'(x)$

**和差**：$\dfrac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$

**链式法则（复合函数）**：
$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

**例**：
$$
\frac{d}{dx}\left[(3x^2 + 4)^{\frac{1}{3}}\right] = \frac{1}{3}(3x^2 + 4)^{-\frac{2}{3}} \cdot 6x = 2x(3x^2 + 4)^{-\frac{2}{3}}
$$

---

## 14.4 乘积法则与商法则

> **考纲要求**: Differentiate products and quotients of functions.

### 📌 公式

**乘积法则 (Product Rule)**：
$$
\frac{d}{dx}(uv) = u'v + uv'
$$

**商法则 (Quotient Rule)**：
$$
\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2}
$$

### 📝 示例

**乘积法则**：$y = x^2\sin x$
$$
y' = 2x\sin x + x^2\cos x
$$

**商法则**：$y = \dfrac{\ln x}{x}$
$$
y' = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}
$$

---

## 14.5 切线、法线与梯度

> **考纲要求**: Use differentiation to find gradients, tangents and normals.

### 📌 方法

1. 求 $f'(x)$ 得到梯度函数
2. 代入 $x_0$ 得切线斜率 $m = f'(x_0)$
3. 切线方程：$y - y_0 = m(x - x_0)$
4. 法线斜率 $= -\dfrac{1}{m}$（$m \neq 0$）

### 📝 示例

**例**：求曲线 $y = x^3 - 2x$ 在 $(1, -1)$ 处的切线与法线方程。

解：$y' = 3x^2 - 2$，在 $x=1$ 处 $m = 3 - 2 = 1$

切线：$y + 1 = 1(x - 1) \Rightarrow y = x - 2$

法线斜率 $= -1$：$y + 1 = -1(x - 1) \Rightarrow y = -x$

---

## 14.6 驻点（Stationary Points）

> **考纲要求**: Use differentiation to find stationary points. Points of inflexion are not included.

### 📌 方法

驻点满足 $f'(x) = 0$。

---

## 14.7 变化率、小增量与近似

> **考纲要求**: Apply differentiation to connected rates of change, small increments and approximations.

### 📌 小增量公式

$$
\delta y \approx \frac{dy}{dx} \cdot \delta x
$$

当 $\delta x$ 很小时，用切线近似函数值：
$$
f(x + \delta x) \approx f(x) + f'(x)\delta x
$$

### 📝 示例

**例**：$y = x^3$，$x$ 从 $2$ 增加到 $2.01$，求 $y$ 的近似增量。

解：$\dfrac{dy}{dx} = 3x^2$，在 $x=2$ 处 $\dfrac{dy}{dx} = 12$

$\delta y \approx 12 \times 0.01 = 0.12$

精确值：$2.01^3 - 2^3 = 8.120601 - 8 = 0.120601$，近似很好。

---

## 14.8 最值问题

> **考纲要求**: Apply differentiation to practical problems involving maxima and minima.

### 📌 解题步骤

1. 建立目标函数 $f(x)$
2. 求导 $f'(x)$，令 $f'(x) = 0$ 找驻点
3. 判断极大/极小（一阶或二阶导数法）
4. 检查定义域、边界值

### 📝 示例

**例**：用 $100$ m 篱笆围一个矩形鸡舍，靠墙一面不需要篱笆，求最大面积。

解：设宽 $x$，长 $100 - 2x$，面积 $A = x(100-2x) = 100x - 2x^2$

$A' = 100 - 4x = 0 \Rightarrow x = 25$

$A'' = -4 < 0$，所以 $x=25$ 时取极大值。

最大面积 $= 25 \times 50 = 1250$ m²

---

## 14.9 极大值与极小值的判定

> **考纲要求**: Use the first and second derivative tests to discriminate between maxima and minima. Points of inflexion are not included. Full justification of conclusions is expected.

### 📌 一阶导数检验

| $x$ 左侧 | $x$ 处 | $x$ 右侧 | 结论 |
|:--------:|:------:|:--------:|:----:|
| $f' > 0$ | $f' = 0$ | $f' < 0$ | **极大值** |
| $f' < 0$ | $f' = 0$ | $f' > 0$ | **极小值** |

### 📌 二阶导数检验

$$
f''(x_0) < 0 \Rightarrow \text{极大值},\quad f''(x_0) > 0 \Rightarrow \text{极小值}
$$

---

## 14.10 积分作为微分的逆运算

> **考纲要求**: Understand integration as the reverse process of differentiation. Solutions for indefinite integrals should include an arbitrary constant.

### 📌 定义

如果 $F'(x) = f(x)$，则 $\displaystyle\int f(x)\,dx = F(x) + C$，$C$ 为积分常数。

---

## 14.11 幂函数与 $\dfrac{1}{x}$ 的积分

> **考纲要求**: Integrate sums of terms in powers of $x$, including $\dfrac{1}{x}$ and $\dfrac{1}{ax+b}$.

### 📌 公式

$$
\int x^n\,dx = \begin{cases}
\dfrac{x^{n+1}}{n+1} + C, & n \neq -1 \\[8pt]
\ln|x| + C, & n = -1
\end{cases}
$$

$$
\int \frac{1}{ax+b}\,dx = \frac{1}{a}\ln|ax+b| + C
$$

---

## 14.12 复合函数的积分

> **考纲要求**: Integrate functions of the form: $(ax+b)^n$ for any rational $n$; $\sin(ax+b)$; $\cos(ax+b)$; $\sec^2(ax+b)$; $e^{ax+b}$. Includes the case where $n = -1$. For trigonometric functions angles will always be in radians.

### 📌 公式（必须熟记！）

$$
\begin{aligned}
\int (ax+b)^n\,dx &= \frac{1}{a}\cdot\frac{(ax+b)^{n+1}}{n+1} + C \quad (n \neq -1) \\[6pt]
\int \frac{1}{ax+b}\,dx &= \frac{1}{a}\ln|ax+b| + C \\[6pt]
\int \sin(ax+b)\,dx &= -\frac{1}{a}\cos(ax+b) + C \\[6pt]
\int \cos(ax+b)\,dx &= \frac{1}{a}\sin(ax+b) + C \\[6pt]
\int \sec^2(ax+b)\,dx &= \frac{1}{a}\tan(ax+b) + C \\[6pt]
\int e^{ax+b}\,dx &= \frac{1}{a}e^{ax+b} + C
\end{aligned}
$$

### ⚠️ 易错点

- $n = -1$ 时用 $\ln$，不能用幂函数公式
- 不定积分别忘 $+C$
- 三角函数角度必须用弧度

---

## 14.13 定积分与面积

> **考纲要求**: Evaluate definite integrals and apply integration to the evaluation of plane areas. Plane areas include: between a line and a curve; between two curves; a sum of two areas.

### 📌 定积分

$$
\int_a^b f(x)\,dx = F(b) - F(a)
$$

### 📌 面积计算

**曲线与 $x$ 轴**：
$$
\text{Area} = \int_a^b |f(x)|\,dx
$$

**两条曲线之间**：
$$
\text{Area} = \int_a^b [f(x) - g(x)]\,dx \quad (f(x) \geq g(x))
$$

### 📝 示例

**例**：求曲线 $y = x^2$ 和直线 $y = x + 2$ 所围成的面积。

解：先求交点：$x^2 = x + 2 \Rightarrow x^2 - x - 2 = 0 \Rightarrow x = -1, 2$

$$
A = \int_{-1}^2 [(x+2) - x^2]\,dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^2
$$

$$
= \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right) = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{9}{2} = 4.5
$$

### ⚠️ 易错点

- 积分上限在下、下限在上时面积会为负，要取绝对值
- 两曲线相交时，注意确定哪条曲线在上方
- 面积分割为多个区间时分别积分再相加

---

## 14.14 运动学应用

> **考纲要求**: Apply differentiation and integration to kinematics problems that involve displacement, velocity and acceleration of a particle moving in a straight line with variable or constant acceleration.

### 📌 核心关系

$$
v = \frac{ds}{dt}, \quad a = \frac{dv}{dt} = \frac{d^2s}{dt^2}
$$

$$
v = \int a\,dt, \quad s = \int v\,dt
$$

### 📝 示例

**例**：质点速度 $v = 3t^2 - 30t + 72$，求 $t=2$ 时的加速度。

解：$a = \dfrac{dv}{dt} = 6t - 30$，$a(2) = 12 - 30 = -18$（减速）

---

## 14.15 运动学图像

> **考纲要求**: Make use of the relationships in 14.14 to draw and use the following graphs: displacement–time, distance–time, velocity–time, speed–time, acceleration–time.

### 📌 图像关系

| 图像类型 | 斜率含义 | 面积含义 |
|:---------|:---------|:---------|
| 位移-时间 ($s$-$t$) | 速度 $v$ | — |
| 速度-时间 ($v$-$t$) | 加速度 $a$ | 位移变化量 |
| 加速度-时间 ($a$-$t$) | — | 速度变化量 |

### 📝 示例

**例**：质点位移 $s = 3t^3 - 10t^2 + 4t + 8$，$0 \leq t \leq 3$。画出位移-时间、速率-时间、加速度-时间图像。

解：
$$
v = \frac{ds}{dt} = 9t^2 - 20t + 4
$$
$$
a = \frac{dv}{dt} = 18t - 20
$$

计算关键点后即可绘图。

### ⚠️ 易错点

- **距离 (distance)** 与 **位移 (displacement)** 不同——距离是标量，位移是矢量（含方向）
- **速率 (speed)** 是速度的绝对值
- $v$-$t$ 图线下方面积 = 位移，但**距离**需要取绝对值后再积分

---

# 附录：公式速查表（按考纲主题）

## 主题 9 — Circular Measure（公式未给出，必须记忆）

| 公式 | 表达式 |
|:----|:-------|
| 弧长 | $s = r\theta$ |
| 扇形面积 | $A = \dfrac{1}{2}r^2\theta$ |
| 弓形面积 | $A = \dfrac{1}{2}r^2(\theta - \sin\theta)$ |

## 主题 10 — Trigonometry

| 公式 | 说明 |
|:----|:-----|
| $\sin^2 A + \cos^2 A = 1$ | ✓ 公式表给出 |
| $\sec^2 A = 1 + \tan^2 A$ | ✓ 公式表给出 |
| $\csc^2 A = 1 + \cot^2 A$ | ✓ 公式表给出 |

## 主题 11 — Permutations & Combinations

| 公式 | 表达式 |
|:----|:-------|
| 阶乘 | $n! = n \times (n-1) \times \cdots \times 1$，$0! = 1$ |
| 排列 | ${}^nP_r = \dfrac{n!}{(n-r)!}$ |
| 组合 | ${}^nC_r = \dbinom{n}{r} = \dfrac{n!}{r!(n-r)!}$ |

## 主题 12 — Series

| 公式 | 表达式 | 是否给出 |
|:----|:-------|:--------:|
| 二项式定理 | $(a+b)^n = \sum_{r=0}^n \binom{n}{r}a^{n-r}b^r$ | ✓ 给出 |
| 通项 | $T_{r+1} = \binom{n}{r}a^{n-r}b^r$ | — |
| AP 通项 | $a_n = a + (n-1)d$ | ✓ 给出 |
| AP 求和 | $S_n = \frac{n}{2}[2a+(n-1)d]$ | ✓ 给出 |
| GP 通项 | $a_n = ar^{n-1}$ | ✓ 给出 |
| GP 求和 | $S_n = a\frac{1-r^n}{1-r}$ | ✓ 给出 |
| GP 无穷和 | $S_\infty = \frac{a}{1-r}$，$|r|<1$ | ✓ 给出 |

## 主题 13 — Vectors（公式未给出）

| 概念 | 公式 |
|:----|:-----|
| 模长 | $|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$ |
| 单位向量 | $\hat{\mathbf{a}} = \dfrac{\mathbf{a}}{|\mathbf{a}|}$ |
| 位置差 | $\overrightarrow{AB} = \mathbf{b} - \mathbf{a}$ |

## 主题 14 — Calculus（**全部不给出**，必须记忆）

| 导数 | 积分 |
|:----|:-----|
| $\frac{d}{dx}(x^n) = nx^{n-1}$ | $\int x^n\,dx = \frac{x^{n+1}}{n+1}+C\ (n\neq-1)$ |
| $\frac{d}{dx}(\sin x) = \cos x$ | $\int \sin(ax+b)\,dx = -\frac1a\cos(ax+b)+C$ |
| $\frac{d}{dx}(\cos x) = -\sin x$ | $\int \cos(ax+b)\,dx = \frac1a\sin(ax+b)+C$ |
| $\frac{d}{dx}(\tan x) = \sec^2 x$ | $\int \sec^2(ax+b)\,dx = \frac1a\tan(ax+b)+C$ |
| $\frac{d}{dx}(e^x) = e^x$ | $\int e^{ax+b}\,dx = \frac1a e^{ax+b}+C$ |
| $\frac{d}{dx}(\ln x) = \frac1x$ | $\int \frac1x\,dx = \ln|x|+C$ |
| 链式法则：$\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}$ | $\int (ax+b)^n\,dx = \frac1a\cdot\frac{(ax+b)^{n+1}}{n+1}+C$ |
| 乘积法则：$(uv)' = u'v + uv'$ | 分部积分：$\int u\,dv = uv - \int v\,du$ |
| 商法则：$(\frac{u}{v})' = \frac{u'v-uv'}{v^2}$ | 定积分：$\int_a^b f(x)\,dx = F(b)-F(a)$ |

---

> **最后提示**：
> - Calculus 部分**所有公式都不在公式表中**，必须熟练掌握
> - 三角函数的微积分**角度必须用弧度**
> - 不定积分别忘了 $+C$
> - 考试中解释 GP 收敛性时需说明 $|r| < 1$ 时 $r^n \to 0$
> - 扇形弧长与面积公式不在公式表中，要熟记

---

*本文档由 LG-leo 整理维护，基于 Cambridge IGCSE Additional Mathematics (0606) 2025–2027 考纲。*
