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

# 第 9 章：几何（直线与圆）

## 大纲对照

本章覆盖 Cambridge IGCSE Additional Mathematics 0606（2028–2030 考纲）以下内容：

| 考纲主题 | 本节对应 |
|----------|----------|
| **7. Straight-line graphs** – 直线方程、平行/垂直、中点、长度、垂直平分线 | 9.1 |
| **7.4** – 非线性关系线性化（$y = Ax^n$, $y = Ab^x$） | 9.2 |
| **8. Coordinate geometry of the circle** – 圆的方程、圆心与半径 | 9.3 |
| **8.2** – 直线与圆的相交（割线、切线、不相交） | 9.4 |
| **8.3** – 圆的切线（不使用微积分） | 9.4 |
| **8.4** – 两圆相交、相切、不相交、公共弦 | 9.5 |

---

## 引言

解析几何的核心思想是：**用代数方程描述几何图形**。一条直线或一个圆可以用一个坐标方程完全表示；两个图形之间的位置关系——是否相交、是否相切、距离是多少——都可以通过代数运算精确判断，而不需要尺规作图。

本章从最基本的直线方程开始，逐步建立完整的解析几何工具集：直线的方程形式与几何性质、圆的两种方程形式、直线与圆的位置关系（特别是切线的三种求法），以及两圆相交时的公共弦。此外，9.2 节介绍一种在科学实验中极其实用的技巧——**非线性关系的线性化**，它将幂函数和指数函数转化为直线形式以便分析。

每个小节都包含公式的完整推导和真题风格的例题。所有例题均采用 **Statement | Reason** 格式：每一步都先给出结论性陈述，再说明理由。

---

## 9.1 直线方程

### 9.1.1 斜率——直线的方向

**定义**：给定两点 $A(x_1, y_1)$ 和 $B(x_2, y_2)$，直线 $AB$ 的斜率 $m$ 是纵坐标差与横坐标差的比值：

$$
m = \frac{y_2 - y_1}{x_2 - x_1} \qquad (x_1 \neq x_2)
$$

**推导**：斜率衡量直线相对于水平轴的倾斜程度。设直线与 $x$ 轴正方向的夹角为 $\theta$（$0^\circ \leq \theta < 180^\circ$），则 $m = \tan\theta$。当 $\theta = 90^\circ$ 时，直线竖直，$\tan 90^\circ$ 未定义，因此竖直线没有斜率。

**几何含义**：
- $m > 0$：直线向右上方倾斜（$\theta$ 为锐角）。
- $m < 0$：直线向右下方倾斜（$\theta$ 为钝角）。
- $m = 0$：直线水平（$\theta = 0^\circ$）。
- $m$ 未定义：直线竖直（$\theta = 90^\circ$）。

---

### 9.1.2 直线方程的三种形式

**形式 1：点斜式**

已知直线上一点 $(x_1, y_1)$ 和斜率 $m$。设 $(x, y)$ 为直线上任意一点。该点与已知点连线的斜率必须等于 $m$：

$$
\frac{y - y_1}{x - x_1} = m
$$

两边乘以 $(x - x_1)$，得到点斜式：

$$
\boxed{y - y_1 = m(x - x_1)}
$$

**形式 2：斜截式**

在点斜式中，取已知点为直线与 $y$ 轴的交点 $(0, c)$（$c$ 称为 $y$ 截距），代入得：

$$
y - c = m(x - 0) \quad \Rightarrow \quad \boxed{y = mx + c}
$$

这是最常用的直线方程形式，$m$ 是斜率，$c$ 是 $y$ 截距。

**形式 3：一般式**

将直线方程的所有项移到等号一侧：

$$
\boxed{Ax + By + C = 0}
$$

其中 $A, B$ 不同时为零。当 $B \neq 0$ 时，可解出斜率：

$$
y = -\frac{A}{B}x - \frac{C}{B} \quad \Rightarrow \quad m = -\frac{A}{B}
$$

一般式的优势：它统一包含所有直线，包括竖直线（此时 $B = 0$，方程为 $Ax + C = 0$，即 $x = -\frac{C}{A}$）。

---

**示例 1**：一条直线经过点 $(3, -2)$，斜率为 $4$。求它的方程。

| Statement | Reason |
|-----------|--------|
| The point is $(3, -2)$ and the gradient is $4$. | Given. |
| Using the point-slope form $y - y_1 = m(x - x_1)$. | This is the appropriate formula when a point and the gradient are known. |
| $y - (-2) = 4(x - 3)$. | Substituting $x_1 = 3$, $y_1 = -2$, $m = 4$. |
| $y + 2 = 4x - 12$. | Expanding the brackets. |
| $y = 4x - 14$. | Subtracting 2 from both sides. |

The equation of the line is $y = 4x - 14$, or $4x - y - 14 = 0$ in general form.

---

**示例 2**：一条直线经过点 $(-1, 5)$ 和 $(2, -1)$。求它的方程。

| Statement | Reason |
|-----------|--------|
| Let $(x_1, y_1) = (-1, 5)$ and $(x_2, y_2) = (2, -1)$. | Two points on the line are given. |
| $m = \frac{-1 - 5}{2 - (-1)} = \frac{-6}{3} = -2$. | Gradient formula $m = \frac{y_2 - y_1}{x_2 - x_1}$. |
| Using $y - y_1 = m(x - x_1)$ with $(-1, 5)$. | Point-slope form requires one point and the gradient. |
| $y - 5 = -2(x + 1)$. | Substituting $m = -2$, $x_1 = -1$, $y_1 = 5$. |
| $y - 5 = -2x - 2$. | Expanding the bracket. |
| $y = -2x + 3$. | Adding 5 to both sides. |

The equation is $y = -2x + 3$, or $2x + y - 3 = 0$.

---

**示例 3**：将直线 $3x - 2y + 6 = 0$ 化为斜截式，并指出斜率和 $y$ 截距。

| Statement | Reason |
|-----------|--------|
| $3x - 2y + 6 = 0$. | Given general form. |
| $-2y = -3x - 6$. | Moving $3x$ and $6$ to the right-hand side. |
| $y = \frac{3}{2}x + 3$. | Dividing both sides by $-2$. |
| $m = \frac{3}{2}$ and $c = 3$. | In $y = mx + c$, $m$ is the gradient and $c$ is the $y$-intercept. |

The gradient is $\frac{3}{2}$ and the $y$-intercept is $3$.

---

### 9.1.3 平行与垂直的条件

**平行线**

两条直线平行的几何含义是它们的方向完全相同。因此它们的斜率相等：

$$
\boxed{m_1 = m_2}
$$

当两条直线都是竖直线时，它们的斜率都未定义，它们也互相平行。

**垂直线**

两条直线互相垂直时，一条直线旋转 $90^\circ$ 后与另一条重合。

**推导**：设两条直线的斜率分别为 $m_1 = \tan\theta_1$ 和 $m_2 = \tan\theta_2$。若两直线垂直，则 $\theta_2 = \theta_1 + 90^\circ$（或相反）。利用恒等式 $\tan(\theta + 90^\circ) = -\cot\theta$：

$$
m_2 = \tan(\theta_1 + 90^\circ) = -\cot\theta_1 = -\frac{1}{\tan\theta_1} = -\frac{1}{m_1}
$$

因此：

$$
\boxed{m_1 \cdot m_2 = -1}
$$

特殊情况：水平线（$m = 0$）与竖直线（斜率未定义）互相垂直，此时乘积条件不适用，但可通过几何直观判断。

---

**示例 1**：判断直线 $L_1: y = 3x + 2$ 和 $L_2: 6x - 2y + 5 = 0$ 是否平行。

| Statement | Reason |
|-----------|--------|
| $L_1$ has gradient $m_1 = 3$. | Equation is in slope-intercept form $y = mx + c$. |
| $L_2: 6x - 2y + 5 = 0$ ⇒ $-2y = -6x - 5$ ⇒ $y = 3x + \frac{5}{2}$. | Rearranging to slope-intercept form. |
| $m_2 = 3$. | The coefficient of $x$ is the gradient. |
| $m_1 = m_2 = 3$. | Both gradients are equal. |
| Therefore $L_1 \parallel L_2$. | Parallel lines have equal gradients. |

---

**示例 2**：一条直线经过点 $(2, -3)$ 且垂直于直线 $2x + y = 5$。求它的方程。

| Statement | Reason |
|-----------|--------|
| $2x + y = 5$ ⇒ $y = -2x + 5$. | Rearranging to slope-intercept form. |
| The given line has gradient $m_1 = -2$. | In $y = mx + c$, the coefficient of $x$ is the gradient. |
| Let the required gradient be $m_2$. | The required line is perpendicular to the given line. |
| $m_1 \cdot m_2 = -1$ ⇒ $(-2)m_2 = -1$ ⇒ $m_2 = \frac{1}{2}$. | Perpendicular lines satisfy $m_1 m_2 = -1$. |
| The line passes through $(2, -3)$ with $m = \frac{1}{2}$. | Using point-slope form $y - y_1 = m(x - x_1)$. |
| $y - (-3) = \frac{1}{2}(x - 2)$. | Substituting $x_1 = 2$, $y_1 = -3$, $m = \frac{1}{2}$. |
| $y + 3 = \frac{1}{2}x - 1$ ⇒ $y = \frac{1}{2}x - 4$. | Simplifying. |

The equation is $y = \frac{1}{2}x - 4$, or $x - 2y - 8 = 0$.

---

**示例 3**：已知 $A(1, 4)$、$B(3, 0)$、$C(5, 2)$。判断三角形 $ABC$ 是否为直角三角形。

| Statement | Reason |
|-----------|--------|
| $m_{AB} = \frac{0 - 4}{3 - 1} = \frac{-4}{2} = -2$. | Gradient formula between $A$ and $B$. |
| $m_{BC} = \frac{2 - 0}{5 - 3} = \frac{2}{2} = 1$. | Gradient formula between $B$ and $C$. |
| $m_{AC} = \frac{2 - 4}{5 - 1} = \frac{-2}{4} = -\frac{1}{2}$. | Gradient formula between $A$ and $C$. |
| $m_{AB} \cdot m_{AC} = (-2) \times \left(-\frac{1}{2}\right) = 1 \neq -1$. | Checking if $AB \perp AC$. |
| $m_{AB} \cdot m_{BC} = (-2) \times 1 = -2 \neq -1$. | Checking if $AB \perp BC$. |
| $m_{BC} \cdot m_{AC} = 1 \times \left(-\frac{1}{2}\right) = -\frac{1}{2} \neq -1$. | Checking if $BC \perp AC$. |
| No pair of gradients satisfies $m_1 m_2 = -1$. | Therefore no two sides are perpendicular. |
| Triangle $ABC$ is **not** a right-angled triangle. | A right-angled triangle requires one pair of perpendicular sides. |

---

### 9.1.4 中点公式

给定两点 $A(x_1, y_1)$ 和 $B(x_2, y_2)$，线段 $AB$ 的中点 $M$ 的坐标是两端坐标的算术平均：

$$
\boxed{M\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)}
$$

**推导**：设 $M$ 的坐标为 $(x_M, y_M)$。向量 $\overrightarrow{AM} = \frac{1}{2}\overrightarrow{AB}$，因此 $(x_M - x_1, y_M - y_1) = \frac{1}{2}(x_2 - x_1, y_2 - y_1)$。解得 $x_M = \frac{x_1 + x_2}{2}$，$y_M = \frac{y_1 + y_2}{2}$。

---

**示例 1**：求 $A(-3, 7)$ 和 $B(5, -1)$ 的中点。

| Statement | Reason |
|-----------|--------|
| $x_M = \frac{-3 + 5}{2} = \frac{2}{2} = 1$. | Midpoint formula for $x$-coordinate. |
| $y_M = \frac{7 + (-1)}{2} = \frac{6}{2} = 3$. | Midpoint formula for $y$-coordinate. |
| $M = (1, 3)$. | The midpoint of $AB$. |

---

**示例 2**：已知 $P(2, 5)$ 是线段 $QR$ 的中点，且 $Q(-1, 3)$。求 $R$ 的坐标。

| Statement | Reason |
|-----------|--------|
| Let $R = (x, y)$. | Unknown coordinates of the endpoint. |
| $\frac{-1 + x}{2} = 2$. | Midpoint formula for $x$, equating to 2. |
| $-1 + x = 4$ ⇒ $x = 5$. | Multiplying both sides by 2. |
| $\frac{3 + y}{2} = 5$. | Midpoint formula for $y$, equating to 5. |
| $3 + y = 10$ ⇒ $y = 7$. | Multiplying both sides by 2. |
| $R = (5, 7)$. | The coordinates of the other endpoint. |

---

**示例 3**：$A(2, 3)$、$B(6, -1)$、$C(4, 5)$ 是平行四边形的三个顶点。若 $A$ 和 $C$ 是对角顶点，求第四个顶点 $D$。

| Statement | Reason |
|-----------|--------|
| In a parallelogram, diagonals bisect each other. | Property of a parallelogram. |
| The midpoint of diagonal $AC$ equals the midpoint of diagonal $BD$. | Diagonals share the same midpoint. |
| Midpoint of $AC$: $\left(\frac{2 + 4}{2}, \frac{3 + 5}{2}\right) = (3, 4)$. | Midpoint formula. |
| Let $D = (x, y)$. Then midpoint of $BD$ is $\left(\frac{6 + x}{2}, \frac{-1 + y}{2}\right)$. | Midpoint formula for $BD$. |
| $\frac{6 + x}{2} = 3$ ⇒ $6 + x = 6$ ⇒ $x = 0$. | Equating $x$-coordinates of midpoints. |
| $\frac{-1 + y}{2} = 4$ ⇒ $-1 + y = 8$ ⇒ $y = 9$. | Equating $y$-coordinates of midpoints. |
| $D = (0, 9)$. | The fourth vertex of the parallelogram. |

---

### 9.1.5 两点之间的距离

给定两点 $A(x_1, y_1)$ 和 $B(x_2, y_2)$，线段 $AB$ 的长度由勾股定理给出：

$$
\boxed{AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}}
$$

**推导**：过 $A$ 和 $B$ 分别作水平线和竖直线，构成直角三角形。水平直角边长为 $|x_2 - x_1|$，竖直直角边长为 $|y_2 - y_1|$。由勾股定理，斜边长（即 $AB$）为 $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$。

---

**示例 1**：求 $A(-2, 5)$ 和 $B(4, -3)$ 之间的距离。

| Statement | Reason |
|-----------|--------|
| $AB = \sqrt{(4 - (-2))^2 + (-3 - 5)^2}$. | Distance formula. |
| $= \sqrt{6^2 + (-8)^2}$. | Simplifying inside the brackets. |
| $= \sqrt{36 + 64} = \sqrt{100} = 10$. | Evaluating squares and summing. |

---

**示例 2**：点 $P$ 在 $x$ 轴上，且到 $A(1, 4)$ 的距离为 $5$。求 $P$ 的坐标。

| Statement | Reason |
|-----------|--------|
| Let $P = (p, 0)$. | Any point on the $x$-axis has $y = 0$. |
| $PA = \sqrt{(p - 1)^2 + (0 - 4)^2} = 5$. | Distance from $P$ to $A$ is given as $5$. |
| $(p - 1)^2 + 16 = 25$. | Squaring both sides. |
| $(p - 1)^2 = 9$. | Subtracting 16 from both sides. |
| $p - 1 = 3$ or $p - 1 = -3$. | Taking square root (two possibilities). |
| $p = 4$ or $p = -2$. | Solving for $p$. |
| $P = (4, 0)$ or $P = (-2, 0)$. | Two points satisfy the condition. |

---

**示例 3**：证明 $A(1, 2)$、$B(4, 6)$、$C(7, 2)$ 是一个等腰三角形。

| Statement | Reason |
|-----------|--------|
| $AB = \sqrt{(4 - 1)^2 + (6 - 2)^2} = \sqrt{9 + 16} = 5$. | Distance formula for $AB$. |
| $BC = \sqrt{(7 - 4)^2 + (2 - 6)^2} = \sqrt{9 + 16} = 5$. | Distance formula for $BC$. |
| $AC = \sqrt{(7 - 1)^2 + (2 - 2)^2} = \sqrt{36 + 0} = 6$. | Distance formula for $AC$. |
| $AB = BC = 5$, but $AB \neq AC$ and $BC \neq AC$. | Two sides are equal, the third is different. |
| Triangle $ABC$ is isosceles with $AB = BC$. | An isosceles triangle has at least two equal sides. |

---

### 9.1.6 点到直线的距离

点 $P(x_0, y_0)$ 到直线 $Ax + By + C = 0$ 的垂直距离为：

$$
\boxed{d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}}
$$

**推导**：直线 $L: Ax + By + C = 0$ 的法向量为 $(A, B)$。过 $P$ 作 $L$ 的垂线，垂足 $H$ 可表示为 $H = (x_0 + tA, y_0 + tB)$，其中 $t$ 是实数。由于 $H$ 在 $L$ 上，代入方程：

$$
A(x_0 + tA) + B(y_0 + tB) + C = 0
$$

$$
Ax_0 + By_0 + C + t(A^2 + B^2) = 0
$$

$$
t = -\frac{Ax_0 + By_0 + C}{A^2 + B^2}
$$

距离 $d = PH = \sqrt{(tA)^2 + (tB)^2} = |t|\sqrt{A^2 + B^2} = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$。

---

**示例 1**：求点 $(2, -3)$ 到直线 $3x - 4y + 5 = 0$ 的距离。

| Statement | Reason |
|-----------|--------|
| $A = 3$, $B = -4$, $C = 5$, $x_0 = 2$, $y_0 = -3$. | Identifying coefficients and point coordinates. |
| $d = \frac{|3(2) + (-4)(-3) + 5|}{\sqrt{3^2 + (-4)^2}}$. | Substituting into the distance formula. |
| $= \frac{|6 + 12 + 5|}{\sqrt{9 + 16}} = \frac{23}{5}$. | Evaluating numerator and denominator. |
| $d = \frac{23}{5} = 4.6$. | The perpendicular distance from the point to the line. |

---

**示例 2**：求两条平行线 $2x + 3y - 6 = 0$ 和 $2x + 3y + 12 = 0$ 之间的距离。

| Statement | Reason |
|-----------|--------|
| On $L_1: 2x + 3y - 6 = 0$, take $x = 0$ ⇒ $3y = 6$ ⇒ $y = 2$. | Choosing a convenient point on the first line. |
| Point $P(0, 2)$ lies on $L_1$. | Substituting gives $0 + 6 - 6 = 0$, which is true. |
| Distance from $P$ to $L_2: 2x + 3y + 12 = 0$ is required. | Parallel lines have constant separation. |
| $d = \frac{|2(0) + 3(2) + 12|}{\sqrt{2^2 + 3^2}}$. | Distance formula with $P$ and $L_2$. |
| $= \frac{|0 + 6 + 12|}{\sqrt{4 + 9}} = \frac{18}{\sqrt{13}}$. | Simplifying. |
| The distance between the two parallel lines is $\frac{18}{\sqrt{13}}$. | This is the perpendicular distance between them. |

---

**示例 3**：点 $(k, 4)$ 到直线 $5x - 12y + 3 = 0$ 的距离为 $2$。求 $k$ 的所有可能值。

| Statement | Reason |
|-----------|--------|
| $d = \frac{|5k - 12(4) + 3|}{\sqrt{5^2 + (-12)^2}} = 2$. | Distance formula, equated to 2. |
| $\frac{|5k - 48 + 3|}{13} = 2$ ⇒ $\frac{|5k - 45|}{13} = 2$. | Simplifying numerator and denominator. |
| $|5k - 45| = 26$. | Multiplying both sides by 13. |
| $5k - 45 = 26$ or $5k - 45 = -26$. | Definition of absolute value. |
| $5k = 71$ or $5k = 19$. | Adding 45 to both sides. |
| $k = \frac{71}{5}$ or $k = \frac{19}{5}$. | Dividing by 5. |

---

### 9.1.7 垂直平分线

一条线段的垂直平分线是同时满足两个条件的直线：
1. **垂直于**该线段。
2. **经过**该线段的中点。

**求法步骤**：
1. 求线段 $AB$ 的中点 $M$。
2. 求 $AB$ 的斜率 $m_{AB}$，则垂直平分线的斜率为 $-\frac{1}{m_{AB}}$（若 $m_{AB} \neq 0$）。
3. 用点斜式写出经过 $M$、斜率为 $-\frac{1}{m_{AB}}$ 的直线。

---

**示例 1**：求连接 $A(1, 3)$ 和 $B(5, -1)$ 的线段的垂直平分线方程。

| Statement | Reason |
|-----------|--------|
| $M = \left(\frac{1 + 5}{2}, \frac{3 + (-1)}{2}\right) = (3, 1)$. | Midpoint formula. |
| $m_{AB} = \frac{-1 - 3}{5 - 1} = \frac{-4}{4} = -1$. | Gradient of $AB$. |
| Perpendicular gradient $= -\frac{1}{-1} = 1$. | Perpendicular gradient is the negative reciprocal. |
| Line through $(3, 1)$ with gradient $1$: $y - 1 = 1(x - 3)$. | Point-slope form. |
| $y = x - 2$. | Simplifying. |
| The perpendicular bisector is $y = x - 2$. | In general form: $x - y - 2 = 0$. |

---

**示例 2**：点 $P(2, 5)$ 和 $Q(8, 3)$。求 $PQ$ 的垂直平分线与坐标轴的交点。

| Statement | Reason |
|-----------|--------|
| $M = \left(\frac{2 + 8}{2}, \frac{5 + 3}{2}\right) = (5, 4)$. | Midpoint of $PQ$. |
| $m_{PQ} = \frac{3 - 5}{8 - 2} = \frac{-2}{6} = -\frac{1}{3}$. | Gradient of $PQ$. |
| Perpendicular gradient $= 3$. | Negative reciprocal of $-\frac{1}{3}$. |
| Equation: $y - 4 = 3(x - 5)$. | Point-slope form with $(5, 4)$ and $m = 3$. |
| $y = 3x - 11$. | Simplifying to slope-intercept form. |
| $x$-intercept: set $y = 0$ ⇒ $0 = 3x - 11$ ⇒ $x = \frac{11}{3}$. | The line crosses the $x$-axis where $y = 0$. |
| $y$-intercept: set $x = 0$ ⇒ $y = -11$. | The line crosses the $y$-axis where $x = 0$. |
| The perpendicular bisector meets the axes at $\left(\frac{11}{3}, 0\right)$ and $(0, -11)$. | These are the required intersection points. |

---

**示例 3**：$A(0, 0)$、$B(6, 2)$、$C(4, 8)$ 是三角形的顶点。求边 $AB$ 的垂直平分线方程，并证明它经过 $AC$ 的中点。

| Statement | Reason |
|-----------|--------|
| $M_{AB} = \left(\frac{0 + 6}{2}, \frac{0 + 2}{2}\right) = (3, 1)$. | Midpoint of $AB$. |
| $m_{AB} = \frac{2 - 0}{6 - 0} = \frac{1}{3}$. | Gradient of $AB$. |
| Perpendicular gradient $= -3$. | Negative reciprocal of $\frac{1}{3}$. |
| Equation: $y - 1 = -3(x - 3)$. | Point-slope form. |
| $y = -3x + 10$. | Simplifying. |
| Midpoint of $AC$: $\left(\frac{0 + 4}{2}, \frac{0 + 8}{2}\right) = (2, 4)$. | Midpoint formula for $AC$. |
| Does $(2, 4)$ satisfy $y = -3x + 10$? | LHS: $4$, RHS: $-3(2) + 10 = 4$. |
| $4 = 4$, so the point lies on the line. | Therefore the perpendicular bisector of $AB$ passes through the midpoint of $AC$. |

---

## 9.2 非线性关系线性化

在科学实验中，两个变量之间往往不是线性关系，而是幂函数关系 $y = Ax^n$ 或指数函数关系 $y = Ab^x$。通过适当的变量代换，我们可以将这些非线性关系**转化为直线形式**，然后用线性回归（计算斜率和截距）确定未知参数。

### 9.2.1 幂函数 $y = Ax^n$

对 $y = Ax^n$ 两边取自然对数：

$$
\ln y = \ln(Ax^n) = \ln A + \ln(x^n) = \ln A + n \ln x
$$

令 $Y = \ln y$，$X = \ln x$，则：

$$
\boxed{Y = nX + \ln A}
$$

这是一个关于 $X$ 和 $Y$ 的直线方程，斜率 $m = n$，$Y$ 截距 $c = \ln A$。

**实际操作**：对每组实验数据 $(x, y)$，计算 $(\ln x, \ln y)$；以 $\ln x$ 为横坐标、$\ln y$ 为纵坐标作图；读出斜率（即 $n$）和 $Y$ 截距（即 $\ln A$），再取指数得到 $A$。

### 9.2.2 指数函数 $y = Ab^x$

对 $y = Ab^x$ 两边取自然对数：

$$
\ln y = \ln(Ab^x) = \ln A + \ln(b^x) = \ln A + x \ln b
$$

令 $Y = \ln y$，$X = x$（注意这里 $X$ 就是原来的 $x$，不需要变换），则：

$$
\boxed{Y = (\ln b)X + \ln A}
$$

这是一个关于 $X$ 和 $Y$ 的直线方程，斜率 $m = \ln b$，$Y$ 截距 $c = \ln A$。

**实际操作**：对每组 $(x, y)$，计算 $(x, \ln y)$；以 $x$ 为横坐标、$\ln y$ 为纵坐标作图；读出斜率（即 $\ln b$，取指数得 $b$）和 $Y$ 截距（即 $\ln A$，取指数得 $A$）。

---

**示例 1**：变量 $x$ 和 $y$ 满足 $y = Ax^n$。实验数据经 $(\ln x, \ln y)$ 变换后得到一条直线，其斜率为 $2.5$，$\ln y$ 截距为 $1.2$。求 $A$ 和 $n$。

| Statement | Reason |
|-----------|--------|
| $Y = nX + \ln A$, where $Y = \ln y$ and $X = \ln x$. | Linearised form of $y = Ax^n$. |
| The graph of $Y$ against $X$ has slope $2.5$ and $Y$-intercept $1.2$. | Given experimental results. |
| $n = 2.5$. | The slope equals $n$ in the linearised equation. |
| $\ln A = 1.2$ ⇒ $A = e^{1.2}$. | The $Y$-intercept equals $\ln A$. |
| The relationship is $y = e^{1.2} x^{2.5}$. | Substituting the values of $A$ and $n$. |

---

**示例 2**：变量 $x$ 和 $y$ 满足 $y = Ab^x$。实验数据经 $(x, \ln y)$ 变换后得到直线，斜率为 $0.75$，$\ln y$ 截距为 $2.3$。求 $A$ 和 $b$。

| Statement | Reason |
|-----------|--------|
| $Y = (\ln b)X + \ln A$, where $Y = \ln y$ and $X = x$. | Linearised form of $y = Ab^x$. |
| $\ln b = 0.75$ ⇒ $b = e^{0.75}$. | The slope equals $\ln b$. |
| $\ln A = 2.3$ ⇒ $A = e^{2.3}$. | The $Y$-intercept equals $\ln A$. |
| $y = e^{2.3} \cdot (e^{0.75})^x = e^{2.3 + 0.75x}$. | The exponential relationship. |

---

**示例 3**：已知 $y = 5x^3$。将它线性化，并说明若以 $\ln x$ 为横坐标、$\ln y$ 为纵坐标作图，斜率和截距各是多少。

| Statement | Reason |
|-----------|--------|
| $\ln y = \ln(5x^3) = \ln 5 + 3\ln x$. | Taking natural log of both sides. |
| $Y = 3X + \ln 5$, where $Y = \ln y$, $X = \ln x$. | The linearised equation. |
| The slope is $3$. | This equals the exponent $n$. |
| The $Y$-intercept is $\ln 5 \approx 1.609$. | This equals $\ln A$. |

---

## 9.3 圆的方程

圆是平面上到定点（圆心）的距离等于定长（半径）的所有点的集合。这个定义直接给出了圆的标准方程。

### 9.3.1 标准式

设圆心为 $C(a, b)$，半径为 $r$。对于圆上任意一点 $P(x, y)$，由距离公式有 $PC = r$：

$$
\sqrt{(x - a)^2 + (y - b)^2} = r
$$

两边平方，得到标准式：

$$
\boxed{(x - a)^2 + (y - b)^2 = r^2}
$$

圆心在原点时，$a = b = 0$，方程为 $x^2 + y^2 = r^2$。

### 9.3.2 一般式

将标准式展开：

$$
x^2 - 2ax + a^2 + y^2 - 2by + b^2 = r^2
$$

移项并合并常数项：

$$
x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - r^2) = 0
$$

令 $g = -a$，$f = -b$，$c = a^2 + b^2 - r^2$，得到一般式：

$$
\boxed{x^2 + y^2 + 2gx + 2fy + c = 0}
$$

从一般式反推圆心和半径：

- 圆心：$(-g, -f)$
- 半径：$r = \sqrt{g^2 + f^2 - c}$

**存在条件**：$g^2 + f^2 - c > 0$ 表示实圆；$= 0$ 表示点圆；$< 0$ 表示虚圆（无实图形）。

---

**示例 1**：写出圆心为 $(-3, 4)$、半径为 $6$ 的圆的方程。

| Statement | Reason |
|-----------|--------|
| $(x - (-3))^2 + (y - 4)^2 = 6^2$. | Standard form $(x - a)^2 + (y - b)^2 = r^2$. |
| $(x + 3)^2 + (y - 4)^2 = 36$. | Simplifying. |
| $x^2 + 6x + 9 + y^2 - 8y + 16 = 36$. | Expanding the brackets. |
| $x^2 + y^2 + 6x - 8y - 11 = 0$. | Collecting terms and subtracting 36. |

---

**示例 2**：已知圆的方程为 $x^2 + y^2 - 10x + 4y + 13 = 0$。求圆心和半径。

| Statement | Reason |
|-----------|--------|
| $2g = -10$ ⇒ $g = -5$. | Comparing with $x^2 + y^2 + 2gx + 2fy + c = 0$. |
| $2f = 4$ ⇒ $f = 2$. | Coefficient of $y$. |
| $c = 13$. | Constant term. |
| Centre $= (-g, -f) = (5, -2)$. | Centre formula. |
| $r = \sqrt{g^2 + f^2 - c} = \sqrt{(-5)^2 + 2^2 - 13}$. | Radius formula. |
| $= \sqrt{25 + 4 - 13} = \sqrt{16} = 4$. | Evaluating. |
| Centre is $(5, -2)$ and radius is $4$. | Final answer. |

---

**示例 3**：通过配方法将 $x^2 + y^2 + 6x - 2y - 6 = 0$ 化为标准式，并求圆心和半径。

| Statement | Reason |
|-----------|--------|
| $(x^2 + 6x) + (y^2 - 2y) = 6$. | Grouping $x$ and $y$ terms, moving constant to RHS. |
| $(x^2 + 6x + 9) + (y^2 - 2y + 1) = 6 + 9 + 1$. | Completing the square: add $(\frac{6}{2})^2 = 9$ and $(\frac{-2}{2})^2 = 1$ to both sides. |
| $(x + 3)^2 + (y - 1)^2 = 16$. | Factorising the perfect squares. |
| Centre $= (-3, 1)$ and radius $= \sqrt{16} = 4$. | Reading from standard form $(x - a)^2 + (y - b)^2 = r^2$. |

---

## 9.4 圆与直线

### 9.4.1 位置关系的判别

将直线方程代入圆的方程，得到关于 $x$（或 $y$）的二次方程。该二次方程的判别式 $\Delta$ 决定交点个数：

- $\Delta > 0$：两个不同的实根 $\Rightarrow$ 两个交点（直线是**割线**）
- $\Delta = 0$：一个重根 $\Rightarrow$ 一个交点（直线是**切线**）
- $\Delta < 0$：无实根 $\Rightarrow$ 无交点（直线与圆**相离**）

### 9.4.2 切线的三种求法

**情形 1：已知切点 $(x_1, y_1)$ 在圆上**

对于圆 $(x - a)^2 + (y - b)^2 = r^2$，在点 $(x_1, y_1)$ 处的切线方程为：

$$
\boxed{(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2}
$$

**推导**：圆心 $C(a, b)$ 到切点 $P(x_1, y_1)$ 的向量为 $(x_1 - a, y_1 - b)$。切线与半径 $CP$ 垂直。设 $Q(x, y)$ 为切线上任意一点，则向量 $\overrightarrow{PQ} = (x - x_1, y - y_1)$ 与 $\overrightarrow{CP}$ 的点积为零：

$$
(x_1 - a)(x - x_1) + (y_1 - b)(y - y_1) = 0
$$

整理为 $(x_1 - a)(x - a) + (y_1 - b)(y - b) = (x_1 - a)^2 + (y_1 - b)^2 = r^2$。

对于圆心在原点的圆 $x^2 + y^2 = r^2$，切线简化为：

$$
\boxed{x_1 x + y_1 y = r^2}
$$

---

**示例 1（已知切点）**：圆 $x^2 + y^2 = 25$，求在点 $(3, -4)$ 处的切线方程。

| Statement | Reason |
|-----------|--------|
| Centre is $(0, 0)$, $r^2 = 25$, point is $(3, -4)$. | Identifying from $x^2 + y^2 = r^2$ form. |
| Tangent formula: $x_1 x + y_1 y = r^2$. | Formula for a circle centred at the origin. |
| $3x + (-4)y = 25$ ⇒ $3x - 4y = 25$. | Substituting $x_1 = 3$, $y_1 = -4$, $r^2 = 25$. |
| $3x - 4y - 25 = 0$. | The equation of the tangent in general form. |

---

**示例 2（已知切点）**：圆 $(x - 2)^2 + (y + 1)^2 = 16$，求在点 $(6, -1)$ 处的切线方程。

| Statement | Reason |
|-----------|--------|
| Centre $(a, b) = (2, -1)$, $r^2 = 16$, point $(x_1, y_1) = (6, -1)$. | Given in standard form. |
| Formula: $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$. | Tangent at a point on the circle. |
| $(6 - 2)(x - 2) + (-1 + 1)(y + 1) = 16$. | Substituting values. |
| $4(x - 2) + 0 \cdot (y + 1) = 16$. | Simplifying. |
| $4x - 8 = 16$ ⇒ $4x = 24$ ⇒ $x = 6$. | Solving. |
| The tangent is the vertical line $x = 6$. | This is consistent: $(6, -1)$ is the rightmost point of the circle. |

---

**情形 2：已知斜率 $m$**

对于圆心 $(a, b)$、半径 $r$ 的圆，斜率为 $m$ 的切线方程为：

$$
\boxed{y - b = m(x - a) \pm r\sqrt{1 + m^2}}
$$

**推导**：设切线为 $y = mx + k$。圆心到直线的距离等于半径：

$$
\frac{|ma - b + k|}{\sqrt{m^2 + 1}} = r
$$

解得 $k = b - ma \pm r\sqrt{m^2 + 1}$。代入 $y = mx + k$ 即得。

当圆心在原点时，简化为 $y = mx \pm r\sqrt{1 + m^2}$。

---

**示例 3（已知斜率）**：求圆 $x^2 + y^2 = 9$ 的斜率为 $2$ 的切线方程。

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, $r = 3$, $m = 2$. | Given. |
| $y = mx \pm r\sqrt{1 + m^2} = 2x \pm 3\sqrt{1 + 4}$. | Formula for tangent with given slope, centre at origin. |
| $y = 2x \pm 3\sqrt{5}$. | Simplifying. |
| The two tangents are $y = 2x + 3\sqrt{5}$ and $y = 2x - 3\sqrt{5}$. | The $\pm$ gives two parallel tangents, one above and one below. |

---

**情形 3：从圆外一点 $(x_0, y_0)$ 引切线**

解法：
1. 设切线斜率为 $m$，方程 $y - y_0 = m(x - x_0)$。
2. 化为一般式 $mx - y + (y_0 - mx_0) = 0$。
3. 令圆心到该直线的距离等于半径，解出 $m$。
4. 检查竖直线 $x = x_0$ 是否也是切线。

---

**示例 4（圆外一点）**：圆 $x^2 + y^2 = 5$ 和圆外点 $P(4, 3)$。求从 $P$ 引出的切线方程。

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, radius $r = \sqrt{5}$. | Given circle. |
| Let the tangent be $y - 3 = m(x - 4)$. | Point-slope form through $P(4, 3)$. |
| $mx - y + (3 - 4m) = 0$. | Rearranging to general form. |
| $\frac{|m(0) - 0 + (3 - 4m)|}{\sqrt{m^2 + 1}} = \sqrt{5}$. | Distance from centre $(0,0)$ to line equals radius. |
| $|3 - 4m| = \sqrt{5}\sqrt{m^2 + 1}$. | Multiplying both sides by $\sqrt{m^2 + 1}$. |
| $(3 - 4m)^2 = 5(m^2 + 1)$. | Squaring both sides. |
| $9 - 24m + 16m^2 = 5m^2 + 5$. | Expanding. |
| $11m^2 - 24m + 4 = 0$. | Collecting like terms. |
| $(11m - 2)(m - 2) = 0$ ⇒ $m = \frac{2}{11}$ or $m = 2$. | Factorising. |
| For $m = 2$: $y - 3 = 2(x - 4)$ ⇒ $y = 2x - 5$. | First tangent. |
| For $m = \frac{2}{11}$: $y - 3 = \frac{2}{11}(x - 4)$ ⇒ $11y - 33 = 2x - 8$ ⇒ $2x - 11y + 25 = 0$. | Second tangent. |
| Check $x = 4$: distance from $(0,0)$ to $x = 4$ is $4 \neq \sqrt{5}$. | Vertical line is not a tangent. |
| The two tangents are $y = 2x - 5$ and $2x - 11y + 25 = 0$. | Final answer. |

---

### 9.4.3 综合判断与求值

**示例 5**：直线 $y = x + k$ 与圆 $x^2 + y^2 = 8$ 相切。求 $k$ 的值。

| Statement | Reason |
|-----------|--------|
| Substitute $y = x + k$ into $x^2 + y^2 = 8$. | Finding intersection points. |
| $x^2 + (x + k)^2 = 8$. | Substituting. |
| $x^2 + x^2 + 2kx + k^2 = 8$. | Expanding. |
| $2x^2 + 2kx + (k^2 - 8) = 0$. | Collecting terms. |
| For tangency, $\Delta = 0$. | A tangent touches at exactly one point. |
| $\Delta = (2k)^2 - 4(2)(k^2 - 8) = 4k^2 - 8k^2 + 64$. | Discriminant of the quadratic. |
| $\Delta = -4k^2 + 64 = 0$. | Setting discriminant to zero. |
| $k^2 = 16$ ⇒ $k = \pm 4$. | Solving for $k$. |
| The line $y = x + 4$ or $y = x - 4$ is tangent to the circle. | Two parallel tangents with slope $1$. |

---

**示例 6**：判断直线 $y = 2x - 1$ 与圆 $(x - 1)^2 + (y + 2)^2 = 5$ 的位置关系。

| Statement | Reason |
|-----------|--------|
| Centre $(1, -2)$, radius $r = \sqrt{5}$. | From standard form. |
| Substitute $y = 2x - 1$: $(x - 1)^2 + (2x - 1 + 2)^2 = 5$. | Substituting into circle equation. |
| $(x - 1)^2 + (2x + 1)^2 = 5$. | Simplifying inside brackets. |
| $x^2 - 2x + 1 + 4x^2 + 4x + 1 = 5$. | Expanding. |
| $5x^2 + 2x + 2 = 5$ ⇒ $5x^2 + 2x - 3 = 0$. | Collecting terms. |
| $\Delta = 2^2 - 4(5)(-3) = 4 + 60 = 64 > 0$. | Discriminant is positive. |
| Since $\Delta > 0$, the line intersects the circle at two distinct points. | The line is a secant. |

---

## 9.5 两圆的位置关系

### 9.5.1 五种位置关系

设圆 $C_1$ 圆心 $O_1$、半径 $r_1$；圆 $C_2$ 圆心 $O_2$、半径 $r_2$；圆心距 $d = O_1O_2$。

| 关系 | 条件 | 示意图描述 |
|------|------|-----------|
| **外离** | $d > r_1 + r_2$ | 两圆无公共点，互不重叠 |
| **外切** | $d = r_1 + r_2$ | 两圆恰好相切于一点，在外部接触 |
| **相交** | $\|r_1 - r_2\| < d < r_1 + r_2$ | 两个公共点 |
| **内切** | $d = \|r_1 - r_2\|$ | 两圆恰好相切于一点，一个在另一个内部 |
| **内含** | $d < \|r_1 - r_2\|$ | 一个圆完全在另一个内部，无公共点 |
| **同心圆** | $d = 0$（且 $r_1 \neq r_2$） | 圆心重合（属于内含的特例） |

### 9.5.2 公共弦（公弦）

当两圆相交于两点时，这两个交点的连线称为**公共弦**。

设两圆方程为：

$$
C_1: x^2 + y^2 + 2g_1x + 2f_1y + c_1 = 0
$$

$$
C_2: x^2 + y^2 + 2g_2x + 2f_2y + c_2 = 0
$$

交点同时满足两个方程。两式相减，$x^2 + y^2$ 项消去，得到一条直线：

$$
\boxed{2(g_1 - g_2)x + 2(f_1 - f_2)y + (c_1 - c_2) = 0}
$$

因为两个交点都满足两圆方程，它们必然也满足相减后的方程，因此这条直线就是通过两个交点的直线——公共弦。当两圆相切时，该直线变为**公切线**。

---

**示例 1（判断位置关系）**：判断圆 $C_1: x^2 + y^2 = 4$ 和 $C_2: (x - 4)^2 + y^2 = 1$ 的位置关系。

| Statement | Reason |
|-----------|--------|
| $C_1$: centre $O_1(0, 0)$, radius $r_1 = 2$. | From standard form. |
| $C_2$: centre $O_2(4, 0)$, radius $r_2 = 1$. | From standard form. |
| $d = \sqrt{(4 - 0)^2 + (0 - 0)^2} = 4$. | Distance between centres. |
| $r_1 + r_2 = 2 + 1 = 3$. | Sum of radii. |
| $d = 4 > 3 = r_1 + r_2$. | Since the centre distance exceeds the sum of radii. |
| The circles are **separate** (externally disjoint). | They have no common points. |

---

**示例 2（相切条件）**：圆 $C_1: x^2 + y^2 = 9$ 与 $C_2: (x - 5)^2 + y^2 = r^2$ 外切。求 $r$。

| Statement | Reason |
|-----------|--------|
| $C_1$: $(0, 0)$, $r_1 = 3$. $C_2$: $(5, 0)$, $r_2 = r$. | Identifying centres and radii. |
| $d = \sqrt{(5 - 0)^2 + 0^2} = 5$. | Distance between centres. |
| For external tangency: $d = r_1 + r_2$. | Definition of externally tangent circles. |
| $5 = 3 + r$ ⇒ $r = 2$. | Solving for $r$. |
| The radius of $C_2$ must be $2$. | So the circles touch at exactly one point. |

---

**示例 3（求公共弦）**：两圆 $C_1: x^2 + y^2 - 6x + 4y - 3 = 0$ 和 $C_2: x^2 + y^2 + 2x - 8y + 5 = 0$ 相交。求公共弦方程。

| Statement | Reason |
|-----------|--------|
| $C_1 - C_2$: $(x^2 + y^2 - 6x + 4y - 3) - (x^2 + y^2 + 2x - 8y + 5) = 0$. | Subtracting the equations eliminates $x^2 + y^2$. |
| $-6x + 4y - 3 - 2x + 8y - 5 = 0$. | Removing brackets and simplifying signs. |
| $-8x + 12y - 8 = 0$. | Collecting like terms. |
| Divide by $-4$: $2x - 3y + 2 = 0$. | Simplifying. |
| The common chord is $2x - 3y + 2 = 0$. | This line passes through both intersection points. |

---

## 9.6 综合例题（解答见章末）

以下例题综合运用本章的多个知识点。建议先独立尝试，再对照章末的详细解答。

---

**例题 1**：圆 $C$ 的圆心在直线 $y = 2x + 1$ 上，且经过点 $A(1, 4)$ 和 $B(3, 0)$。求圆 $C$ 的方程。

---

**例题 2**：已知直线 $y = 2x + k$ 与圆 $x^2 + y^2 - 2x + 4y - 4 = 0$ 相交于两个不同的点。求 $k$ 的取值范围。

---

**例题 3**：圆 $C_1: (x - 1)^2 + (y - 3)^2 = 25$ 和圆 $C_2: (x + 2)^2 + (y - 7)^2 = 4$。
(a) 判断两圆的位置关系。
(b) 若相交，求公共弦的方程。

---

**例题 4**：圆 $x^2 + y^2 = 10$ 和圆外一点 $P(5, 5)$。求从 $P$ 向该圆所作的两条切线方程。

---

**例题 5**：点 $A(2, 5)$、$B(6, 1)$、$C(8, 5)$。
(a) 求 $AB$ 的垂直平分线方程。
(b) 求 $BC$ 的垂直平分线方程。
(c) 证明这两条垂直平分线的交点就是过 $A$、$B$、$C$ 三点的圆的圆心。

---

## 9.7 综合例题解答

### 例题 1 解答

| Statement | Reason |
|-----------|--------|
| Let the centre be $(h, 2h + 1)$. | The centre lies on $y = 2x + 1$. |
| $A(1, 4)$ and $B(3, 0)$ are on the circle. | Given. |
| $CA = CB$ (both equal the radius). | All points on a circle are equidistant from the centre. |
| $(h - 1)^2 + (2h + 1 - 4)^2 = (h - 3)^2 + (2h + 1 - 0)^2$. | Using distance formula: $CA^2 = CB^2$. |
| $(h - 1)^2 + (2h - 3)^2 = (h - 3)^2 + (2h + 1)^2$. | Simplifying $y$-differences. |
| $h^2 - 2h + 1 + 4h^2 - 12h + 9 = h^2 - 6h + 9 + 4h^2 + 4h + 1$. | Expanding all squares. |
| $5h^2 - 14h + 10 = 5h^2 - 2h + 10$. | Collecting like terms on both sides. |
| $-14h + 10 = -2h + 10$ ⇒ $-12h = 0$ ⇒ $h = 0$. | Subtracting $5h^2$ and $10$ from both sides. |
| Centre $= (0, 1)$. | Substituting $h = 0$ into $(h, 2h + 1)$. |
| $r^2 = (0 - 1)^2 + (1 - 4)^2 = 1 + 9 = 10$. | Distance from centre to $A(1, 4)$. |
| The circle equation is $(x - 0)^2 + (y - 1)^2 = 10$, i.e. $x^2 + (y - 1)^2 = 10$. | Final answer. |

---

### 例题 2 解答

| Statement | Reason |
|-----------|--------|
| $x^2 + y^2 - 2x + 4y - 4 = 0$ ⇒ $(x - 1)^2 + (y + 2)^2 = 9$. | Completing the square to find centre and radius. |
| Centre $(1, -2)$, radius $r = 3$. | From standard form. |
| Substitute $y = 2x + k$: $(x - 1)^2 + (2x + k + 2)^2 = 9$. | Substituting into circle equation. |
| $x^2 - 2x + 1 + 4x^2 + 4(k + 2)x + (k + 2)^2 = 9$. | Expanding. |
| $5x^2 + [4(k + 2) - 2]x + [1 + (k + 2)^2 - 9] = 0$. | Grouping $x^2$, $x$ and constant terms. |
| $5x^2 + (4k + 6)x + (k^2 + 4k + 4 - 8) = 0$. | Simplifying coefficients. |
| $5x^2 + (4k + 6)x + (k^2 + 4k - 4) = 0$. | Final quadratic in $x$. |
| For two distinct intersections, $\Delta > 0$. | A quadratic with $\Delta > 0$ has two distinct real roots. |
| $\Delta = (4k + 6)^2 - 4(5)(k^2 + 4k - 4) > 0$. | Discriminant condition. |
| $16k^2 + 48k + 36 - 20k^2 - 80k + 80 > 0$. | Expanding. |
| $-4k^2 - 32k + 116 > 0$. | Collecting terms. |
| Divide by $-4$ (reverse inequality): $k^2 + 8k - 29 < 0$. | Note: dividing by a negative flips the inequality. |
| Roots of $k^2 + 8k - 29 = 0$: $k = \frac{-8 \pm \sqrt{64 + 116}}{2} = \frac{-8 \pm \sqrt{180}}{2} = -4 \pm 3\sqrt{5}$. | Quadratic formula. |
| Since the quadratic in $k$ opens upward, $k^2 + 8k - 29 < 0$ between the roots. | The inequality is satisfied for values between the roots. |
| $-4 - 3\sqrt{5} < k < -4 + 3\sqrt{5}$. | The range of $k$ for which the line intersects the circle at two points. |

---

### 例题 3 解答

**Part (a)**

| Statement | Reason |
|-----------|--------|
| $C_1$: centre $O_1(1, 3)$, $r_1 = 5$. | From $(x - 1)^2 + (y - 3)^2 = 25$. |
| $C_2$: centre $O_2(-2, 7)$, $r_2 = 2$. | From $(x + 2)^2 + (y - 7)^2 = 4$. |
| $d = \sqrt{(1 - (-2))^2 + (3 - 7)^2} = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = 5$. | Distance between centres. |
| $r_1 + r_2 = 5 + 2 = 7$, $|r_1 - r_2| = 3$. | Sum and difference of radii. |
| $3 < 5 < 7$, i.e. $|r_1 - r_2| < d < r_1 + r_2$. | $d$ lies between the difference and the sum. |
| Therefore the circles **intersect at two points**. | Condition for two intersections. |

**Part (b)**

| Statement | Reason |
|-----------|--------|
| $C_1$ in general form: $x^2 + y^2 - 2x - 6y - 15 = 0$. | Expanding $(x - 1)^2 + (y - 3)^2 = 25$. |
| $C_2$ in general form: $x^2 + y^2 + 4x - 14y + 49 - 4 = 0$ ⇒ $x^2 + y^2 + 4x - 14y + 45 = 0$. | Expanding $(x + 2)^2 + (y - 7)^2 = 4$.
Wait — $(x+2)^2 = x^2 + 4x + 4$, $(y-7)^2 = y^2 - 14y + 49$, sum $= x^2 + y^2 + 4x - 14y + 53 = 4$ ⇒ $x^2 + y^2 + 4x - 14y + 49 = 0$. | Checking: $53 - 4 = 49$, so $c_2 = 49$. |
| Subtract $C_2$ from $C_1$: $(-2x - 6y - 15) - (4x - 14y + 49) = 0$. | $x^2 + y^2$ terms cancel. |
| $-2x - 6y - 15 - 4x + 14y - 49 = 0$ ⇒ $-6x + 8y - 64 = 0$. | Simplifying. |
| Divide by $-2$: $3x - 4y + 32 = 0$. | The common chord equation. |

---

### 例题 4 解答

| Statement | Reason |
|-----------|--------|
| Centre $(0, 0)$, radius $r = \sqrt{10}$. | Circle $x^2 + y^2 = 10$. |
| Let tangent have slope $m$, equation $y - 5 = m(x - 5)$. | Point-slope form through $P(5, 5)$. |
| $mx - y + (5 - 5m) = 0$. | General form. |
| Distance from $(0,0)$ to line $= \frac{|5 - 5m|}{\sqrt{m^2 + 1}} = \sqrt{10}$. | Distance equals radius. |
| $|5 - 5m| = \sqrt{10}\sqrt{m^2 + 1}$. | Multiplying both sides. |
| $(5 - 5m)^2 = 10(m^2 + 1)$. | Squaring both sides. |
| $25 - 50m + 25m^2 = 10m^2 + 10$. | Expanding. |
| $15m^2 - 50m + 15 = 0$. | Collecting terms. |
| Divide by $5$: $3m^2 - 10m + 3 = 0$. | Simplifying. |
| $(3m - 1)(m - 3) = 0$ ⇒ $m = 3$ or $m = \frac{1}{3}$. | Factorising. |
| For $m = 3$: $y - 5 = 3(x - 5)$ ⇒ $y = 3x - 10$. | First tangent. |
| For $m = \frac{1}{3}$: $y - 5 = \frac{1}{3}(x - 5)$ ⇒ $3y - 15 = x - 5$ ⇒ $x - 3y + 10 = 0$. | Second tangent. |
| Check $x = 5$: distance from $(0,0)$ to $x = 5$ is $5 \neq \sqrt{10}$. | Not a tangent. |
| The two tangents are $y = 3x - 10$ and $x - 3y + 10 = 0$. | Final answer. |

---

### 例题 5 解答

**Part (a)**

| Statement | Reason |
|-----------|--------|
| $A(2, 5)$, $B(6, 1)$. | Given. |
| Midpoint $M_{AB} = \left(\frac{2 + 6}{2}, \frac{5 + 1}{2}\right) = (4, 3)$. | Midpoint formula. |
| $m_{AB} = \frac{1 - 5}{6 - 2} = \frac{-4}{4} = -1$. | Gradient of $AB$. |
| Perpendicular gradient $= 1$. | Negative reciprocal of $-1$. |
| Equation: $y - 3 = 1(x - 4)$ ⇒ $y = x - 1$. | Perpendicular bisector of $AB$. |

**Part (b)**

| Statement | Reason |
|-----------|--------|
| $B(6, 1)$, $C(8, 5)$. | Given. |
| Midpoint $M_{BC} = \left(\frac{6 + 8}{2}, \frac{1 + 5}{2}\right) = (7, 3)$. | Midpoint formula. |
| $m_{BC} = \frac{5 - 1}{8 - 6} = \frac{4}{2} = 2$. | Gradient of $BC$. |
| Perpendicular gradient $= -\frac{1}{2}$. | Negative reciprocal of $2$. |
| Equation: $y - 3 = -\frac{1}{2}(x - 7)$. | Perpendicular bisector of $BC$. |
| $y - 3 = -\frac{1}{2}x + \frac{7}{2}$ ⇒ $y = -\frac{1}{2}x + \frac{13}{2}$. | Simplifying. |

**Part (c)**

| Statement | Reason |
|-----------|--------|
| Intersection of the two bisectors: $x - 1 = -\frac{1}{2}x + \frac{13}{2}$. | Equating $y$ from both equations. |
| $x + \frac{1}{2}x = \frac{13}{2} + 1$ ⇒ $\frac{3}{2}x = \frac{15}{2}$ ⇒ $x = 5$. | Solving for $x$. |
| $y = 5 - 1 = 4$. | Substituting $x = 5$ into $y = x - 1$. |
| Intersection $O = (5, 4)$. | The common point of the two perpendicular bisectors. |
| $OA = \sqrt{(5 - 2)^2 + (4 - 5)^2} = \sqrt{9 + 1} = \sqrt{10}$. | Distance from $O$ to $A$. |
| $OB = \sqrt{(5 - 6)^2 + (4 - 1)^2} = \sqrt{1 + 9} = \sqrt{10}$. | Distance from $O$ to $B$. |
| $OC = \sqrt{(5 - 8)^2 + (4 - 5)^2} = \sqrt{9 + 1} = \sqrt{10}$. | Distance from $O$ to $C$. |
| $OA = OB = OC = \sqrt{10}$. | $O$ is equidistant from all three vertices. |
| Therefore $O(5, 4)$ is the centre of the circle passing through $A$, $B$ and $C$, with radius $\sqrt{10}$. | The perpendicular bisectors of any two chords of a circle intersect at the centre. |

---

## 9.8 本章总结

| 主题 | 核心公式 / 方法 |
|------|----------------|
| **直线方程** | 斜截式 $y = mx + c$，点斜式 $y - y_1 = m(x - x_1)$，一般式 $Ax + By + C = 0$ |
| **平行条件** | $m_1 = m_2$ |
| **垂直条件** | $m_1 \cdot m_2 = -1$ |
| **中点公式** | $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ |
| **两点距离** | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| **点到直线距离** | $d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$ |
| **垂直平分线** | 斜率 $= -\frac{1}{m_{AB}}$，过 $AB$ 中点 |
| **线性化——幂函数** | $y = Ax^n \Rightarrow \ln y = n\ln x + \ln A$ |
| **线性化——指数函数** | $y = Ab^x \Rightarrow \ln y = (\ln b)x + \ln A$ |
| **圆的标准式** | $(x - a)^2 + (y - b)^2 = r^2$，圆心 $(a, b)$，半径 $r$ |
| **圆的一般式** | $x^2 + y^2 + 2gx + 2fy + c = 0$，圆心 $(-g, -f)$，半径 $\sqrt{g^2 + f^2 - c}$ |
| **直线与圆** | 代入 $\rightarrow$ 二次方程 $\rightarrow$ $\Delta > 0$ 相交，$\Delta = 0$ 相切，$\Delta < 0$ 相离 |
| **切线（已知切点）** | $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$ |
| **切线（已知斜率）** | $y - b = m(x - a) \pm r\sqrt{1 + m^2}$ |
| **两圆关系** | 比较 $d$ 与 $r_1 + r_2$、$\|r_1 - r_2\|$ |
| **公共弦** | 两圆方程相减所得直线 |

---
---

