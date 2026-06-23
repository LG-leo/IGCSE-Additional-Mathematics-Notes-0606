# IGCSE 0606 附加数学综合笔记第二版本

本笔记严格按照 **剑桥 IGCSE 附加数学（0606）2028–2030 考纲** 编写。附加数学课程位于 IGCSE 普通数学之上，旨在拓展代数、函数、几何、三角与微积分的深度，为 AS/A Level Further Math, AP calculus BC, IB AA HL 数学打下坚实基础。

每一章的编排遵循"概念定义 → 公式推导 → 典型例题"的结构。例题选自历年真题风格，难度对标考试要求。
// 里面部分题型是有真题。引用源https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-igcse-mathematics-additional-0606/past-papers/

> **说明**：考卷的公式列表中会给出部分公式（如等差/等比数列的求和公式、二项式展开公式），但本笔记仍完整推导，以帮助理解而非机械记忆。考试中，**理解何时使用哪个公式**比背公式更重要。
---
> 本笔记基于剑桥 IGCSE 附加数学（0606）2025-2027 考纲编写，按照认知顺序排列，涵盖所有主题。包含推导过程、典型例题和常见易错点。适合自学。
- 这份笔记由 LG-leo 整理和维护。如果你觉得这份笔记对你有帮助，欢迎在 GitHub 上关注我或给我一个 ⭐，这能帮助我持续产出更多免费的学习资源。
- 我的其他课程笔记：https://github.com/LG-leo?tab=repositories

- This note is maintained by LG-leo. If you find it helpful, feel free to follow me or leave a ⭐ on GitHub. It helps me keep producing more free study resources. Check out my other notes: https://github.com/LG-leo?tab=repositories
---
---

## 目录

- [第 1 章：数列、排列、组合与二项式定理](#第-1-章数列排列组合与二项式定理)
- [第 2 章：向量与变化率](#第-2-章向量与变化率)
- [第 3 章：二次函数（含多项式因式）](#第-3-章二次函数含多项式因式)
- [第 4 章：函数（线性、三次、指数、对数）](#第-4-章函数线性三次指数对数)
- [第 5 章：微分（导数）](#第-5-章微分导数)
- [第 6 章：方程与不等式（图形法）](#第-6-章方程与不等式图形法)
- [第 7 章：积分（不定积分与定积分）](#第-7-章积分不定积分与定积分)
- [第 8 章：三角学（含弧度法）](#第-8-章三角学含弧度法)
- [第 9 章：几何（直线与圆）](#第-9-章几何直线与圆)
- [第 10 章：综合应用](#第-10-章综合应用)

---

# 第 1 章：数列、排列、组合与二项式定理

本章将三个看似不同但内核相通的主题放在一起。**数列**训练你发现规律和求和的能力；**排列与组合**训练你系统化计数的逻辑；**二项式定理**则是排列组合在代数展开中的直接应用。

---

## 考纲对照表（Syllabus Mapping）

| 考纲编号 | 英文原文（Syllabus 2028–2030） | 中文说明 | 覆盖章节 |
|:-------:|------|---------|:-------:|
| **11.1** | *Recognise the difference between permutations and combinations and know when each should be used.* | 识别排列与组合的区别，知道何时使用哪个 | §1.2.4 |
| **11.2** | *Know and use the notation $n!$ and the expressions for permutations and combinations of $n$ items taken $r$ at a time. Includes $0! = 1$.* | 掌握 $n!$、$^nP_r$、$^nC_r$ 的记号与表达式 | §1.2.2, §1.2.3 |
| **11.3** | *Solve problems on arrangement and selection using permutations or combinations. Problems will be either in an everyday context or based on an algebraic problem. Problems involving: repetition of objects; objects arranged in a circle; both permutations and combinations, are **not** included.* | 用排列或组合解决排列与选择问题（日常生活或代数背景）。不考重复元素、圆排列、排列组合混合。 | §1.2.5 |
| **12.1** | *Use the binomial theorem for expansion of $(a+b)^n$ for positive integer $n$. Includes simplification of coefficients.* | 使用二项式定理展开 $(a+b)^n$（$n$ 为正整数），包含系数的化简 | §1.3.1 |
| **12.2** | *Use the general term $\displaystyle\binom{n}{r}a^{n-r}b^r$, $0 \le r \le n$. For example: Find the term independent of $x$ in the expansion of $\left(x^2 + \frac{1}{x}\right)^{\!10}$. Knowledge of the greatest term and properties of the coefficients is **not** required.* | 使用通项公式求特定项（如常数项）。不考最大项和系数性质。 | §1.3.2, §1.3.3 |
| **12.3** | *Recognise arithmetic and geometric progressions and understand the difference between them.* | 识别等差数列与等比数列，理解它们之间的区别 | §1.1.4 |
| **12.4** | *Use the formulas for the $n$th term and for the sum of the first $n$ terms to solve problems involving arithmetic or geometric progressions. Problems may be in context.* | 使用第 $n$ 项和前 $n$ 项和公式解决等差/等比数列问题（可能含实际情境） | §1.1.2, §1.1.3 |
| **12.5** | *Use the condition for the convergence of a geometric progression, and the formula for the sum to infinity of a convergent geometric progression. Includes explaining why a particular geometric progression has or does not have a sum to infinity.* | 使用等比数列的收敛条件及无穷和公式，**包含解释为什么某个等比级数有/无无穷和** | §1.1.3 |

---

## 1.1 数列（等差与等比）

数列是按顺序排列的一列数。附加数学中重点考察两种最基本的数列：**等差数列**（相邻两项的差固定）和**等比数列**（相邻两项的比固定）。

### 1.1.1 求和符号 $\sum$

在深入讨论数列之前，我们需要掌握求和符号 $\sum$（希腊字母 Sigma）。它表示将一系列数相加：

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + a_3 + \cdots + a_n
$$

求和运算满足三条基本法则，其推导均可直接从展开求和符号得出：

**法则 1——常数因子提取**：

展开求和：
$$
\sum_{k=1}^{n} (c \cdot a_k) = c \cdot a_1 + c \cdot a_2 + \cdots + c \cdot a_n
$$
从每一项提取公因子 $c$：
$$
= c\,(a_1 + a_2 + \cdots + a_n) = c \cdot \sum_{k=1}^{n} a_k
$$
$$
\boxed{\sum_{k=1}^{n} (c \cdot a_k) = c \cdot \sum_{k=1}^{n} a_k}
$$

**法则 2——和的拆分**：

展开求和并重新分组：
$$
\begin{aligned}
\sum_{k=1}^{n} (a_k \pm b_k) &= (a_1 \pm b_1) + (a_2 \pm b_2) + \cdots + (a_n \pm b_n) \\
&= (a_1 + a_2 + \cdots + a_n) \pm (b_1 + b_2 + \cdots + b_n)
\end{aligned}
$$
$$
\boxed{\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k}
$$

**法则 3——常数的和**：

当每一项都等于常数 $c$ 时，求和即为 $c$ 累加 $n$ 次：
$$
\sum_{k=1}^{n} c = \underbrace{c + c + \cdots + c}_{n \text{ 次}} = n c
$$
$$
\boxed{\sum_{k=1}^{n} c = n c}
$$

**示例**：计算 $\displaystyle\sum_{k=1}^{5} (3k - 2)$。

$$
\sum_{k=1}^{5} (3k - 2) = 3\sum_{k=1}^{5} k - \sum_{k=1}^{5} 2 = 3 \times (1+2+3+4+5) - 5 \times 2 = 3 \times 15 - 10 = 45 - 10 = 35
$$

---

### 1.1.2 等差数列（Arithmetic Progression）

#### 定义

一个数列如果从第二项起，每一项与它的前一项的差等于**同一个常数**，则称为**等差数列**。这个常数叫做**公差**，记作 $d$：

$$
a_{n+1} - a_n = d \quad (\text{对所有 } n \ge 1\text{ 成立})
$$

**示例**：$5, 9, 13, 17, 21$ 是等差数列，$d=4$，$a=5$。

#### 第 $n$ 项公式（推导）

设首项 $a_1 = a$。等差数列的定义性质是 $a_{k+1} - a_k = d$，即对于每个 $k \ge 1$，有 $a_{k+1} = a_k + d$。

从首项出发，反复应用递推关系：

$$
\begin{aligned}
a_2 &= a_1 + d = a + d \\[4pt]
a_3 &= a_2 + d = (a + d) + d = a + 2d \\[4pt]
a_4 &= a_3 + d = (a + 2d) + d = a + 3d \\[4pt]
&\;\;\vdots
\end{aligned}
$$

观察规律：$d$ 的系数始终比项的下标少 $1$。从 $a_1$ 出发经过 $(n-1)$ 步，恰好加了 $(n-1)$ 次公差：

$$
\boxed{a_n = a + (n-1)d}
$$

> **验证**：$n=1$ 时 $a_1 = a + 0 \cdot d = a$ ✓；$n=2$ 时 $a_2 = a + 1 \cdot d = a + d$ ✓。

#### 前 $n$ 项和公式（推导——倒序相加法）

设 $S_n$ 为前 $n$ 项的和：

$$
S_n = a + (a+d) + (a+2d) + \cdots + [a+(n-1)d] \tag{1}
$$

现在将同一求和从末项反向写回首项：

$$
S_n = [a+(n-1)d] + [a+(n-2)d] + \cdots + (a+d) + a \tag{2}
$$

将 (1) 和 (2) 逐项相加。共有 $n$ 列；第 $k$ 列（从左数起）配对为：

$$
\bigl[a + (k-1)d\bigr] + \bigl[a + (n-k)d\bigr] = 2a + (n-1)d
$$

注意每一列的和都**相同**，均为 $2a + (n-1)d$。共 $n$ 列：

$$
2S_n = \underbrace{[2a + (n-1)d] + [2a + (n-1)d] + \cdots + [2a + (n-1)d]}_{n \text{ 次}} = n\,[2a + (n-1)d]
$$

两边除以 $2$：

$$
\boxed{S_n = \frac{n}{2}\,[\,2a + (n-1)d\,]}
$$

若末项 $l = a_n = a + (n-1)d$，则 $2a + (n-1)d = a + l$，得到等价形式：

$$
\boxed{S_n = \frac{n}{2}\,(a + l)}
$$

#### 例题

**例题 1**：首项 $7$，公差 $3$，求第 $15$ 项。

$$
a_{15} = 7 + 14 \times 3 = 7 + 42 = 49
$$

---

**例题 2**：首项 $2$，公差 $5$，前 $n$ 项和 $156$，求 $n$。

$$
\frac{n}{2}[4 + (n-1) \times 5] = 156 \quad\Rightarrow\quad \frac{n}{2}(5n - 1) = 156
$$

$$
5n^2 - n - 312 = 0 \quad\Rightarrow\quad n = \frac{1 \pm \sqrt{1 + 6240}}{10} = \frac{1 \pm 79}{10}
$$

$n$ 为正整数，$n = \frac{80}{10} = 8$。

---

**例题 3**（实际情境）：第一年存 $500$ 元，之后每年多存 $50$ 元。$10$ 年共存多少钱？

$$
S_{10} = \frac{10}{2}[2 \times 500 + 9 \times 50] = 5 \times (1000 + 450) = 7250
$$

答：$7250$ 元。

---

### 1.1.3 等比数列（Geometric Progression）

#### 定义

一个数列如果从第二项起，每一项与它的前一项的比值等于**同一个常数**，则称为**等比数列**。这个常数叫做**公比**，记作 $r$：

$$
\frac{a_{n+1}}{a_n} = r \quad (\text{对所有 } n \ge 1\text{ 成立})
$$

**示例**：$2, 6, 18, 54, 162$ 是等比数列，$r=3$，$a=2$。

#### 第 $n$ 项公式（推导）

设首项 $a_1 = a$。等比数列的定义性质是 $\dfrac{a_{k+1}}{a_k} = r$，即对于每个 $k \ge 1$，有 $a_{k+1} = a_k \cdot r$。

从首项出发，反复应用递推关系：

$$
\begin{aligned}
a_2 &= a_1 \cdot r = a r \\[4pt]
a_3 &= a_2 \cdot r = (a r) \cdot r = a r^2 \\[4pt]
a_4 &= a_3 \cdot r = (a r^2) \cdot r = a r^3 \\[4pt]
&\;\;\vdots
\end{aligned}
$$

观察规律：$r$ 的指数始终比项的下标少 $1$。从 $a_1$ 出发经过 $(n-1)$ 次乘以 $r$，得到：

$$
\boxed{a_n = a r^{\,n-1}}
$$

> **验证**：$n=1$ 时 $a_1 = a r^{0} = a$ ✓；$n=2$ 时 $a_2 = a r^{1} = a r$ ✓。

#### 前 $n$ 项和公式（推导——错位相减法）

设 $S_n$ 为前 $n$ 项的和：

$$
S_n = a + a r + a r^2 + \cdots + a r^{\,n-1} \tag{1}
$$

将 (1) 式两边同时乘以公比 $r$：

$$
r S_n = a r + a r^2 + a r^3 + \cdots + a r^{\,n-1} + a r^{\,n} \tag{2}
$$

对比 (1) 和 (2)，大部分项在两式中都出现——唯一的区别是：
- $a$ 只出现在 (1) 中（首项）
- $a r^{\,n}$ 只出现在 (2) 中（末项）

因此，(1) 减 (2)：

$$
S_n - r S_n = a - a r^{\,n}
$$

左边提取 $S_n$，右边提取 $a$：

$$
S_n(1 - r) = a(1 - r^{\,n})
$$

分两种情况讨论：

- **若 $r = 1$**：每一项都等于 $a$，故 $S_n = \underbrace{a + a + \cdots + a}_{n \text{ 次}} = n a$。

- **若 $r \neq 1$**：两边除以 $(1-r)$：

$$
\boxed{S_n = a \cdot \frac{1 - r^{\,n}}{1 - r}}
$$

等价形式（分子分母同乘 $-1$）：

$$
\boxed{S_n = a \cdot \frac{r^{\,n} - 1}{r - 1}}
$$

#### 无穷等比级数的收敛条件与和（**考纲 12.5 重点**）

$$
S_\infty = \lim_{n \to \infty} S_n = \lim_{n \to \infty} a \cdot \frac{1 - r^{\,n}}{1 - r}
$$

$r^{\,n}$ 在 $n \to \infty$ 时的行为决定了级数是否收敛：

| $r$ 的取值范围 | $n \to \infty$ 时 $r^{\,n}$ 的行为 | 级数是否收敛 | 无穷和 |
|:-------------:|----------------------------------|:-----------:|:------:|
| $\lvert r\rvert < 1$ | $r^{\,n} \to 0$ | ✅ **收敛** | $\displaystyle S_\infty = \frac{a}{1-r}$ |
| $\lvert r\rvert > 1$ | $\lvert r\rvert^{\,n} \to \infty$ | ❌ **发散** | 无有限和 |
| $r = 1$ | $r^{\,n} = 1$（恒定） | ❌ **发散** | $S_n = n a \to \infty$ |
| $r = -1$ | 在 $1$ 和 $-1$ 之间振荡 | ❌ **发散** | 和不确定 |

因此，**等比级数收敛的充要条件是 $|r| < 1$**。

考试中如果被要求"解释为什么某个等比级数有/没有无穷和"，你需要说明：当 $|r| < 1$ 时，$n \to \infty$ 使 $r^{\,n} \to 0$，因此 $S_n \to \dfrac{a}{1-r}$；当 $|r| \ge 1$ 时，$r^{\,n}$ 不趋近于 $0$，$S_n$ 不趋近于有限值。

#### 例题

**例题 1**：首项 $3$，公比 $2$，求第 $6$ 项。

$$
a_6 = 3 \times 2^5 = 3 \times 32 = 96
$$

---

**例题 2**（收敛判断 + 无穷和）：$12 + 6 + 3 + \dfrac{3}{2} + \cdots$

首项 $a = 12$，公比 $r = \dfrac{6}{12} = \dfrac{1}{2}$。

因为 $|r| = \dfrac{1}{2} < 1$，当 $n \to \infty$ 时 $\left(\dfrac{1}{2}\right)^{\!n} \to 0$，所以级数收敛。

$$
S_\infty = \frac{12}{1 - \frac{1}{2}} = \frac{12}{\frac{1}{2}} = 24
$$

---

**例题 3**（已知 $S_\infty$ 求 $r$）：无穷等比级数收敛，和为 $8$，首项为 $4$，求公比 $r$。

$$
8 = \frac{4}{1 - r} \quad\Rightarrow\quad 8(1 - r) = 4 \quad\Rightarrow\quad 1 - r = \frac{1}{2} \quad\Rightarrow\quad r = \frac{1}{2}
$$

验证：$|r| = \dfrac{1}{2} < 1$，满足收敛条件。

---

### 1.1.4 对照：等差数列 vs 等比数列（**考纲 12.3 重点**）

| 特征 | 等差数列 (AP) | 等比数列 (GP) |
|:----|:-------------|:-------------|
| **定义性质** | $a_{n+1} - a_n = d$（差恒定） | $\dfrac{a_{n+1}}{a_n} = r$（比恒定） |
| **检查方法** | 相邻项相减，看是否恒等 | 相邻项相除，看是否恒等 |
| **第 $n$ 项** | $a_n = a + (n-1)d$ | $a_n = a r^{\,n-1}$ |
| **前 $n$ 项和** | $S_n = \dfrac{n}{2}[2a + (n-1)d]$ | $S_n = a\dfrac{1-r^n}{1-r}$（$r \neq 1$） |
| **增长模式** | **线性增长**（每次加固定值） | **指数增长/衰减**（每次乘固定值） |
| **无穷和** | 不存在（除 $d=0$ 常数数列） | $|r| < 1$ 时收敛于 $\dfrac{a}{1-r}$ |

**判断练习**：

1. $5, 8, 11, 14, 17, \ldots$ → 差恒为 $3$ → **AP** ✓
2. $5, 10, 20, 40, 80, \ldots$ → 比恒为 $2$ → **GP** ✓
3. $1, 4, 9, 16, 25, \ldots$ → 差为 $3,5,7,9$（不恒定），比为 $4, 2.25, 1.78,\ldots$（不恒定）→ **两者都不是** ✗
4. $100, 50, 25, 12.5, \ldots$ → 比恒为 $\dfrac{1}{2}$ → **GP**（收敛）✓

---

## 1.2 排列与组合

排列与组合回答同一个基本问题："有多少种不同的方式？"二者的核心区别在于 **顺序是否重要**。

### 1.2.1 乘法原理

如果一项任务可以分解为 $k$ 个依次进行的步骤，第 $i$ 步有 $m_i$ 种方法，则总方法数为：

$$
\boxed{m_1 \times m_2 \times \cdots \times m_k}
$$

**示例**：A→B 有 $3$ 条路，B→C 有 $4$ 条路，A→B→C 共有 $3 \times 4 = 12$ 条路线。

### 1.2.2 排列——顺序重要（Permutations）

首先需要理解阶乘记号「$!$」：

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
一般地，
$$
n! = 1 \times 2 \times \cdots \times n
$$

现在我们来计算从 $n$ 个不同元素中选取 $r$ 个并按顺序排列的方法数。这个数记作 ${}^{n}P_r$。

我们逐个填充 $r$ 个位置：

- 第 1 个位置：有 $n$ 种选择
- 第 2 个位置：有 $n-1$ 种选择（已用掉一个）
- 第 3 个位置：有 $n-2$ 种选择
- ……
- 第 $r$ 个位置：有 $n - (r-1) = n - r + 1$ 种选择

由乘法原理，总的排列数为所有这些选择的乘积：
$$
{}^{n}P_r = n \times (n-1) \times (n-2) \times \cdots \times (n-r+1)
$$

该乘积有 $r$ 个因子。为将其表示为阶乘的商，乘以并除以从 $(n-r)$ 到 $1$ 的缺失因子：
$$
{}^{n}P_r = \frac{n \times (n-1) \times \cdots \times 2 \times 1}{(n-r) \times (n-r-1) \times \cdots \times 2 \times 1}
$$

分子恰好是 $n!$，分母是 $(n-r)!$。因此：
$$
\boxed{^nP_r = \frac{n!}{(n-r)!}}
$$

特殊情况：
- 当 $r=0$ 时，什么都不选，只有一种方式：
$$
{}^{n}P_0 = \frac{n!}{n!} = 1
$$
- 当 $r=n$ 时，排列所有元素：
$$
{}^{n}P_n = \frac{n!}{0!} = n!
$$

推导完毕。

---

**定义**：从 $n$ 个不同元素中取出 $r$ 个（$r \le n$），按一定顺序排成一列。顺序不同算不同排列。记作 $^nP_r$ 或 $P(n,r)$。

**特殊值**：$^nP_n = n!$，$^nP_0 = 1$，$0! = 1$。

### 1.2.3 组合——顺序不重要（Combinations）

**定义**：从 $n$ 个不同元素中取出 $r$ 个（$r \le n$），不考虑顺序。记作 $^nC_r$、$C(n,r)$ 或 $\binom{n}{r}$。

**推导**：排列数除以内部排列数：

$$
\boxed{^nC_r = \binom{n}{r} = \frac{^nP_r}{r!} = \frac{n!}{r!\,(n-r)!}}
$$

**性质**：

- 对称性：$\displaystyle\binom{n}{r} = \binom{n}{n-r}$
- 边界值：$\displaystyle\binom{n}{0} = \binom{n}{n} = 1$，$\displaystyle\binom{n}{1} = \binom{n}{n-1} = n$

### 1.2.4 如何选择？（**考纲 11.1 重点**）

问自己：**交换任意两个已选元素，结果是否不同？**

| 情境 | 顺序重要？ | 使用 | 示例 |
|:----|:---------:|:----|:-----|
| 排队、名次、密码、排名 | ✅ 是 | **排列** $^nP_r$ | 6 人选 3 人站一排 |
| 委员会、选科、抽奖、组队 | ❌ 否 | **组合** $^nC_r$ | 6 人选 3 人组委员会 |

### 1.2.5 应用题例题

**例题 1**（排列——日常生活）：6 本不同的书选 4 本排上书架（从左到右），多少种摆法？

$$
^6P_4 = \frac{6!}{(6-4)!} = \frac{6!}{2!} = 6 \times 5 \times 4 \times 3 = 360
$$

答：$360$ 种。

---

**例题 2**（组合——日常生活）：7 男 5 女中选 4 人组委员会，要求至少 2 名女生，多少种选法？

- $2$ 女 $2$ 男：$\displaystyle\binom{5}{2} \times \binom{7}{2} = 10 \times 21 = 210$
- $3$ 女 $1$ 男：$\displaystyle\binom{5}{3} \times \binom{7}{1} = 10 \times 7 = 70$
- $4$ 女 $0$ 男：$\displaystyle\binom{5}{4} \times \binom{7}{0} = 5 \times 1 = 5$

总方法数：$210 + 70 + 5 = 285$。

> **补集法验证**：总数 $\displaystyle\binom{12}{4}=495$，减去"至多 1 名女生"（$0$ 女 $4$ 男 $= \binom{5}{0}\binom{7}{4}=35$，$1$ 女 $3$ 男 $= \binom{5}{1}\binom{7}{3}=5\times35=175$，共 $210$），$495 - 210 = 285$ ✓

---

**例题 3**（代数背景——组合恒等式）：证明 $\displaystyle\binom{n}{r} + \binom{n}{r-1} = \binom{n+1}{r}$，并用此计算 $\displaystyle\binom{8}{3} + \binom{8}{2}$。

**证明**：

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

**应用**：

$$
\binom{8}{3} + \binom{8}{2} = \binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84
$$

### 1.2.6 ⚠️ 考试不考的内容

根据考纲，以下类型**不会出现**：

| 不考内容 | 英文原文 |
|---------|---------|
| ❌ 重复元素的排列 | *repetition of objects* |
| ❌ 圆排列 | *objects arranged in a circle* |
| ❌ 排列与组合在同一题中混合使用 | *both permutations and combinations* |

考试中每道题要么是纯排列，要么是纯组合。

---

## 1.3 二项式定理（Binomial Theorem）

### 1.3.1 二项式展开（**考纲 12.1**）

$(a+b)^n$ 可看作 $n$ 个 $(a+b)$ 相乘。展开时，每一项是分别从每个因子选 $a$ 或 $b$ 的乘积。要得到 $a^{\,n-r}b^{\,r}$，需从 $r$ 个因子中选 $b$，从 $n-r$ 个因子中选 $a$。选择方式数为 $\binom{n}{r}$。

对 $r = 0, 1, \ldots, n$ 求和：

$$
\boxed{(a+b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{\,n-r} b^{\,r}}
$$

**示例**：展开 $(x+3)^4$。

$$
\begin{aligned}
(x+3)^4 &= \binom{4}{0}x^4(3)^0 + \binom{4}{1}x^3(3)^1 + \binom{4}{2}x^2(3)^2 + \binom{4}{3}x^1(3)^3 + \binom{4}{4}x^0(3)^4 \\
&= 1 \cdot x^4 + 4 \cdot 3x^3 + 6 \cdot 9x^2 + 4 \cdot 27x + 1 \cdot 81 \\
&= x^4 + 12x^3 + 54x^2 + 108x + 81
\end{aligned}
$$

注意：每一项的系数都经过了**化简**（如 $4 \times 3 = 12$，$6 \times 9 = 54$），这是考纲明确要求的。

### 1.3.2 通项公式与特定项（**考纲 12.2**）

展开式中的第 $(r+1)$ 项（从 $r=0$ 开始计数）：

$$
\boxed{T_{r+1} = \binom{n}{r} a^{\,n-r} b^{\,r}}
$$

常见题型：

| 题型 | 方法 |
|:----|:----|
| 求 $x^k$ 的系数 | 设通项中 $x$ 的指数 $= k$，解出 $r$ |
| 求常数项（不含 $x$） | 设 $x$ 的指数 $= 0$，解出 $r$ |
| 求 $x^p y^q$ 的系数 | 分别设 $x$ 和 $y$ 的指数匹配 |

> **⚠️ 重要区分**：
> - **二项式系数** = $\binom{n}{r}$（只与 $n,r$ 有关）
> - **完整系数** = $\binom{n}{r}$ × $a$ 和 $b$ 中的常数因子及符号
>
> 例如 $(2x-3)^5$ 中 $r=2$：二项式系数 $\binom{5}{2}=10$，完整系数 $= 10 \cdot (2)^3 \cdot (-3)^2 = 720$

### 1.3.3 例题

**例题 1**（求指定幂次的系数）：求 $\left(2x + \dfrac{1}{x}\right)^7$ 展开式中 $x$ 的系数。

**解**：

$$
T_{r+1} = \binom{7}{r} (2x)^{7-r} \left(\frac{1}{x}\right)^{\!r}
= \binom{7}{r} 2^{7-r} x^{7-r} \cdot x^{-r}
= \binom{7}{r} 2^{7-r} x^{7-2r}
$$

令 $7-2r = 1$，得 $r = 3$。

$$
T_4 = \binom{7}{3} 2^{4} x = 35 \times 16 \times x = 560x
$$

所以 $x$ 的系数为 $560$。

---

**例题 2**（求常数项——考纲典型）：求 $\left(x^2 - \dfrac{2}{x}\right)^6$ 展开式中的常数项。

**解**：

$$
\begin{aligned}
T_{r+1} &= \binom{6}{r} (x^2)^{6-r} \left(-\frac{2}{x}\right)^{\!r} \\
&= \binom{6}{r} (-2)^r x^{12-2r} \cdot x^{-r} \\
&= \binom{6}{r} (-2)^r x^{12-3r}
\end{aligned}
$$

令 $12 - 3r = 0$，得 $r = 4$。

$$
T_5 = \binom{6}{4} (-2)^4 = 15 \times 16 = 240
$$

所以常数项为 $240$。

---

**例题 3**（两个二项式乘积的系数）：求 $(1+x)^5 (2-x)^4$ 展开式中 $x^2$ 的系数。

**解**：

$(1+x)^5$ 通项：$\displaystyle\binom{5}{r} x^r$
$(2-x)^4$ 通项：$\displaystyle\binom{4}{k} 2^{4-k} (-1)^k x^k$

需要 $r + k = 2$：

| $r$ | $k$ | 计算 | 贡献 |
|:--:|:--:|:----|:----:|
| $0$ | $2$ | $\binom{5}{0} \cdot \binom{4}{2} 2^{2} (-1)^2 = 1 \times 6 \times 4 \times 1$ | $24$ |
| $1$ | $1$ | $\binom{5}{1} \cdot \binom{4}{1} 2^{3} (-1)^1 = 5 \times 4 \times 8 \times (-1)$ | $-160$ |
| $2$ | $0$ | $\binom{5}{2} \cdot \binom{4}{0} 2^{4} (-1)^0 = 10 \times 1 \times 16 \times 1$ | $160$ |

总和：$24 + (-160) + 160 = 24$。

答：$x^2$ 的系数为 $24$。

---

### 1.3.4 二项式系数的性质（杨辉三角）

**对称性**：

$$
\boxed{\binom{n}{r} = \binom{n}{n-r}}
$$

**杨辉法则**（递推关系）：

$$
\boxed{\binom{n}{r} + \binom{n}{r-1} = \binom{n+1}{r}}
$$

**杨辉三角**：

```
n=0:        1
n=1:       1 1
n=2:      1 2 1
n=3:     1 3 3 1
n=4:    1 4 6 4 1
n=5:   1 5 10 10 5 1
```

> **考试提示**：$n \le 5$ 时可用杨辉三角直接写系数，$n \ge 6$ 时用组合数公式 $\binom{n}{r}$。

> **不考内容**（考纲明确说明）：最大项（greatest term）和系数的性质（properties of the coefficients）不考。

---

## 本章公式速查表

| 主题 | 公式 | 条件 |
|:----|:----|:----|
| AP 第 $n$ 项 | $a_n = a + (n-1)d$ | — |
| AP 前 $n$ 项和 | $S_n = \dfrac{n}{2}[2a + (n-1)d]$ | — |
| GP 第 $n$ 项 | $a_n = a r^{\,n-1}$ | — |
| GP 前 $n$ 项和 | $S_n = a\dfrac{1-r^n}{1-r}$ | $r \neq 1$ |
| GP 无穷和 | $S_\infty = \dfrac{a}{1-r}$ | $\lvert r\rvert < 1$ |
| 排列数 | $^nP_r = \dfrac{n!}{(n-r)!}$ | 顺序重要 |
| 组合数 | $\displaystyle\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | 顺序不重要 |
| 二项式定理 | $(a+b)^n = \displaystyle\sum_{r=0}^{n}\binom{n}{r}a^{n-r}b^{r}$ | $n \in \mathbb{Z}^+$ |
| 通项 | $T_{r+1} = \displaystyle\binom{n}{r}a^{n-r}b^{r}$ | 用于求特定项 |

---
---

