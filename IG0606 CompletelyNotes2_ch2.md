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

# 第 2 章：向量与变化率

## 考纲对照

本章对应剑桥 IGCSE 附加数学（0606）2028–2030 考纲的以下内容：

| 考纲编号 | 内容 | 说明 |
|---------|------|------|
| **13.1** | 理解并使用向量记号 | 列向量、$\mathbf{i}$-$\mathbf{j}$ 形式、$\overrightarrow{AB}$、$p$ 等形式 |
| **13.2** | 位置向量与单位向量 | 求单位向量 $\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$ |
| **13.3** | 向量的模、加法、减法与数乘 | 含向量相等、向量几何问题（给定图形） |
| **13.4** | 速度的合成与分解 | 求合向量、利用速度向量求位置、相撞问题 |
| **14.1** | 导函数的思想（变化率入门） | 极限的直观理解，不要求从第一原理求导 |

---

## 引言

在现实世界中，许多量不仅有大小，还有方向。从飞机航行时的风速修正，到两艘船在海上是否可能相撞，再到抛体运动的轨迹分析——这些问题的数学语言都是**向量**。

本章将从零开始构建二维向量的完整知识体系。我们先学习向量的基本表示方法和运算规则（含垂直向量的判定），然后把这些工具应用于几何问题和运动学问题（速度合成、相撞检测）。最后，我们将视角从"静态的向量"转向"动态的变化率"——当位置向量随时间变化时，它的变化率就是速度，而速度的变化率就是加速度。反过来，已知加速度，我们可通过积分求出速度和位置。这个思想将直接通向第 5 章的微分学与第 7 章的积分学。

---

## 2.1 二维向量基础

### 2.1.1 什么是向量？

向量（vector）是一个既有**大小**又有**方向**的量。与它相对的是标量（scalar），标量只有大小没有方向。例如：

- **向量**：位移、速度、力
- **标量**：距离、速率、质量、温度

在二维平面中，向量有多种等价的表示方式。

#### 表示法 1：列向量

$$
\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}
$$

其中 $x$ 是水平分量，$y$ 是垂直分量。这种表示法在解方程组时非常方便，因为我们可以直接对分量进行操作。

#### 表示法 2：$\mathbf{i}$-$\mathbf{j}$ 形式

定义两个基本单位向量：

$$
\mathbf{i} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \mathbf{j} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

$\mathbf{i}$ 指向正 $x$ 轴方向（向右），$\mathbf{j}$ 指向正 $y$ 轴方向（向上）。那么任意向量可以写为：

$$
\mathbf{v} = x\mathbf{i} + y\mathbf{j}
$$

**两种表示法的等价性**：

$$
x\mathbf{i} + y\mathbf{j} = \begin{pmatrix} x \\ y \end{pmatrix}
$$

例如，向量 $3\mathbf{i} - 2\mathbf{j}$ 与列向量 $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$ 是同一个向量。

#### 表示法 3：有向线段

从点 $A$ 到点 $B$ 的向量记作 $\overrightarrow{AB}$。它等于终点位置减去起点位置：

$$
\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A
$$

> **为什么是"终点减起点"？** 假设你想从家 $A$ 走到学校 $B$。你的位移（从 $A$ 到 $B$）就是你最终到达的位置（学校的位置）减去你出发时的位置（家的位置）。如果 $A$ 在 $(1,1)$，$B$ 在 $(4,5)$，那么你需要向右走 $3$ 个单位、向上走 $4$ 个单位，即 $\overrightarrow{AB} = (3,4)$。

---

### 2.1.2 位置向量

设 $O$ 为原点。任意点 $P(x, y)$ 的**位置向量**是：

$$
\mathbf{r} = \overrightarrow{OP} = \begin{pmatrix} x \\ y \end{pmatrix} = x\mathbf{i} + y\mathbf{j}
$$

位置向量告诉我们点 $P$ 相对于原点的位置。这里的关键区分是：**点** $P(x, y)$ 是空间中的一个位置，而**向量** $\mathbf{r} = (x, y)$ 是从原点到该点的有向线段——它包含了位移的信息。

> **点和向量的区别**：点是一个位置，像地图上的一个坐标。向量是一个位移，像"向右 3 步，向上 2 步"。同一个向量可以从任何起点出发，但同一个点只能在一个位置。

---

### 2.1.3 向量的模（大小）

向量 $\mathbf{v} = x\mathbf{i} + y\mathbf{j}$ 的模（或称长度、大小）由勾股定理给出：

$$
|\mathbf{v}| = \sqrt{x^2 + y^2}
$$

模一定是非负实数。当且仅当向量是零向量 $\mathbf{0} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ 时，模为零。

> **为什么是 $\sqrt{x^2 + y^2}$？** 把向量 $\mathbf{v}$ 看作从原点 $(0,0)$ 到点 $(x,y)$ 的线段。这条线段就是直角三角形的斜边，两条直角边的长度分别是 $|x|$ 和 $|y|$。根据勾股定理，斜边长度 $= \sqrt{x^2 + y^2}$。

---

### 2.1.4 单位向量

**单位向量**是模为 1 的向量。给定任意非零向量 $\mathbf{v}$，我们可以构造与它同方向的单位向量 $\hat{\mathbf{v}}$：

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}
$$

也就是说，将原向量除以它自己的模。这个操作称为**归一化**。

> **为什么这样定义？** 设 $\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}$，那么
> $$
> |\hat{\mathbf{v}}| = \frac{|\mathbf{v}|}{|\mathbf{v}|} = 1
> $$
> 方向保持不变，因为我们在用正标量除以原向量。
>
> **类比**：就像把一段绳子切成单位长度的小段。如果你有一根 5 米长的绳子，把它切成 5 等份，每份就是 1 米，方向与原来相同。

---

### 2.1.5 向量的加法与减法

两个向量的加法，就是将它们的对应分量分别相加：

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} + \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}
$$

减法同理：

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} - \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} = \begin{pmatrix} x_1 - x_2 \\ y_1 - y_2 \end{pmatrix}
$$

**几何意义——为什么是"平行四边形法则"？**

想象两个人同时拉一个箱子。一个人用力 $\mathbf{a}$ 向东拉，另一个人用力 $\mathbf{b}$ 向北拉。箱子实际受到的合力就是 $\mathbf{a} + \mathbf{b}$。

- **加法——平行四边形法则**：以两个向量为邻边作平行四边形，从起点出发的对角线即为它们的和。
- **减法——三角形法则**：$\mathbf{a} - \mathbf{b}$ 等于从 $\mathbf{b}$ 的终点指向 $\mathbf{a}$ 的终点的向量。

**实用的口诀**：
- 对于位移向量：**终点减起点**。从 $A$ 到 $B$ 的向量 $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$
- 对于加法：首尾相连，从第一个起点指向最后一个终点

---

### 2.1.6 向量的数乘

向量乘以一个标量 $c$，相当于每个分量都乘以 $c$：

$$
c \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} cx \\ cy \end{pmatrix}
$$

数乘的几何效果：
- 如果 $c > 0$，向量沿原方向拉伸（$c > 1$）或压缩（$0 < c < 1$）
- 如果 $c < 0$，向量反向

数乘后的模：

$$
|c\mathbf{v}| = |c| \cdot |\mathbf{v}|
$$

> **为什么模会乘以 $|c|$ 而不是 $c$？** 因为如果 $c = -2$，向量的长度变为原来的 2 倍，方向反转。长度是正数，所以取 $|c| = 2$。

---

### 2.1.7 向量相等

两个向量相等当且仅当它们的对应分量分别相等。即：

$$
\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix} \iff x_1 = x_2 \quad \text{且} \quad y_1 = y_2
$$

这称为**向量相等原理**（equating like vectors）——它是解向量方程的核心工具。

> **为什么这个原理如此有用？** 一个向量方程实际上包含了两个独立的标量方程（一个对应 $x$ 分量，一个对应 $y$ 分量）。这让我们能从两个方向分别求解未知数。

---

### 2.1.8 垂直向量（正交向量）

#### 什么是垂直？

两个非零向量 $\mathbf{u}$ 和 $\mathbf{v}$ 垂直（或称正交）当且仅当它们之间的夹角是 $90^\circ$。

#### 如何判断垂直？——点积

要判断两个向量是否垂直，我们需要一个既能用坐标计算、又能反映角度关系的运算——这就是**点积**（也称为内积或标量积）。

##### 点积的定义

两个向量的**点积（内积，dot product）** 定义为对应分量乘积之和：

$$
\boxed{\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y}
$$

> **直观理解**：点积衡量的是两个向量在"方向上的对齐程度"。
> - 如果两个向量指向大致相同的方向（夹角 $< 90^\circ$），点积为正
> - 如果两个向量**垂直**（夹角 $= 90^\circ$），点积为零
> - 如果两个向量指向大致相反的方向（夹角 $> 90^\circ$），点积为负

点积的结果是一个**标量**（不是向量），因此也称为"标量积"（scalar product）。这与向量的加减法不同——向量的加减法结果仍然是向量，而点积将两个向量"压缩"成了一个数值。

> **为什么叫"点积"？** 因为书写时在向量之间用一个点 $\cdot$ 表示乘法，区别于叉积 $\times$。

##### 垂直的判定条件

利用点积，垂直的判定变得极其简洁：

$$
\boxed{\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0}
$$

> **记忆口诀**："点积为零，垂直成立"。
>
> 这个条件之所以成立，是因为当夹角为 $90^\circ$ 时，$\cos 90^\circ = 0$，而点积的几何定义恰好包含 $\cos\theta$ 因子。下面我们来详细推导这个关系。

> **为什么点积为零代表垂直？**
>
> 从几何角度理解，点积还有另一个等价的定义：
> $$
> \mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos\theta
> $$
> 其中 $\theta$ 是两个向量之间的夹角。
>
> 推导这个等价关系：利用余弦定理。设 $\mathbf{u}$ 和 $\mathbf{v}$ 的夹角为 $\theta$，则向量 $\mathbf{u} - \mathbf{v}$ 的模满足：
> $$
> |\mathbf{u} - \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2|\mathbf{u}||\mathbf{v}|\cos\theta
> $$
> 同时展开左边：
> $$
> |\mathbf{u} - \mathbf{v}|^2 = (u_x - v_x)^2 + (u_y - v_y)^2 = (u_x^2 + u_y^2) + (v_x^2 + v_y^2) - 2(u_x v_x + u_y v_y)
> $$
> 比较两式，得：
> $$
> |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2|\mathbf{u}||\mathbf{v}|\cos\theta = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2(u_x v_x + u_y v_y)
> $$
> 因此 $u_x v_x + u_y v_y = |\mathbf{u}||\mathbf{v}|\cos\theta$。
>
> 当 $\theta = 90^\circ$ 时，$\cos 90^\circ = 0$，所以点积为零。

---

#### 点积的基本性质

点积运算满足以下重要性质（这些性质在解题中非常有用）：

**性质 1：交换律（Commutative）**

$$
\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}
$$

因为 $u_x v_x + u_y v_y = v_x u_x + v_y u_y$，实数乘法本身满足交换律。

**性质 2：分配律（Distributive）**

$$
\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}
$$

**性质 3：与数乘的结合律**

$$
(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v}) = \mathbf{u} \cdot (c\mathbf{v})
$$

**性质 4：向量与自身的点积**

$$
\mathbf{v} \cdot \mathbf{v} = v_x^2 + v_y^2 = |\mathbf{v}|^2
$$

> **为什么这个性质特别有用？** 它建立了点积与向量模长之间的桥梁。当我们想求 $|\mathbf{a} + \mathbf{b}|$ 时，可以先算 $(\mathbf{a} + \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b})$：
> $$
> |\mathbf{a} + \mathbf{b}|^2 = (\mathbf{a} + \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = \mathbf{a} \cdot \mathbf{a} + 2\mathbf{a} \cdot \mathbf{b} + \mathbf{b} \cdot \mathbf{b} = |\mathbf{a}|^2 + 2\mathbf{a} \cdot \mathbf{b} + |\mathbf{b}|^2
> $$
> 这在物理中就是**余弦定理的向量形式**。

**性质 5：零向量点积——最重要的逻辑基石**

这个性质看起来"太显然了"，以至于很多学生觉得它不值得讲。但恰恰相反，**性质5是整个点积体系中最重要的"逻辑基石"**，它和性质4（自己点自己）合在一起，定义了什么叫做"长度"和"零"。下面从四个层次把它彻底讲透。

##### 第一层：代数硬算（最直接）

设零向量为 $\mathbf{0} = (0, 0)$，任意向量 $\mathbf{v} = (v_x, v_y)$，直接代入坐标点积公式：

$$
\mathbf{0} \cdot \mathbf{v} = 0 \times v_x + 0 \times v_y = 0 + 0 = 0
$$

无论 $v_x$ 和 $v_y$ 是多大、多小的数，乘以 0 统统归零。**这就是"零向量"在代数上的绝对清零能力。**

##### 第二层：几何与物理直觉（看本质）

套用点积的几何公式：

$$
\mathbf{0} \cdot \mathbf{v} = |\mathbf{0}| \cdot |\mathbf{v}| \cdot \cos\theta
$$

因为零向量的长度 $|\mathbf{0}| = 0$，那么：

$$
0 \cdot |\mathbf{v}| \cdot \cos\theta = 0
$$

> **物理类比**：想象你用尽全力推一个箱子（力向量是 $\mathbf{v}$），但箱子的**位移为零**（位移向量是 $\mathbf{0}$）。无论你推力多大，做功（功 = 力 $\cdot$ 位移）永远是 0。**"长度为零"意味着"根本没有发生作用"，所以点积必然为零。**

##### 第三层：⚠️ 最容易踩的坑（逻辑澄清）

这是最关键的认知分水岭。**请注意区分两个完全不同的"0"：**

| 情况 | 表达式 | 含义 | 几何角度 |
| :--- | :--- | :--- | :--- |
| **性质5** | $\mathbf{0} \cdot \mathbf{v} = 0$ | 因为**零向量本身长度为0**，导致乘积为0 | 没有夹角可言（零向量没有方向） |
| **垂直判定** | $\mathbf{u} \cdot \mathbf{v} = 0$（$\mathbf{u}, \mathbf{v}$ 均非零） | 因为**夹角为90°**，$\cos 90^\circ = 0$，导致乘积为0 | 两个箭头在空间中形成直角 |

> **绝不能说"零向量与任何向量垂直"是因为夹角是90°**——零向量连方向都没有，哪来的90°？
> 严谨的数学说法是：**我们"约定"零向量与任何向量都正交（代数方便），但几何上它不指向任何角度。**
>
> 性质5的成立，靠的是"长度为0"，而不是"角度为90°"。这两者虽然在代数结果上都写成0，但**背后的物理原因截然不同**。

##### 第四层：性质5 + 性质4 = 定义了"正定性"（数学大厦的基石）

在高等数学（泛函分析、线性代数）中，点积（内积）必须满足一条铁律——**正定性（Positive-definiteness）**，即：

1. $\mathbf{v} \cdot \mathbf{v} \ge 0$（永远非负，来自性质4）
2. 且 $\mathbf{v} \cdot \mathbf{v} = 0$ **当且仅当** $\mathbf{v} = \mathbf{0}$

你发现了吗？**性质5正是为了配合性质4，来反向锁定"零向量"的。**
如果没有性质5，那么当我们算出点积为0时，就搞不清到底是因为"向量长度为0"，还是因为"夹角为90°"。有了性质5，我们就能在代数世界里准确地区分出"零元素"。

> **生动的板书总结**：
>
> **性质5：零向量是点积运算中的"吸收元"。**
> - 任何向量跟它相乘，结果必为 0。
> - 原因：**长度为 0**，而非角度为 90°。
> - 功能：与其他性质共同保证，我们可以通过 $\sqrt{\mathbf{v} \cdot \mathbf{v}}$ 唯一地确定向量的长度，并且只有当 $\mathbf{v} = \mathbf{0}$ 时长度才为 0。

---

### 利用点积求两向量夹角

将点积的代数定义和几何定义结合起来，我们可以求出两个向量之间的夹角 $\theta$（$0^\circ \leq \theta \leq 180^\circ$）：

$$
\boxed{\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}| |\mathbf{v}|}}
$$

**推导**：由 $\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$，两边同除以 $|\mathbf{u}||\mathbf{v}|$ 即得。


**特殊角度**：

| $\theta$ | $\cos\theta$ | $\mathbf{u} \cdot \mathbf{v}$ | 关系 |
| :---: | :---: | :---: | :---: |
| $0^\circ$ | $1$ | $= \|\mathbf{u}\| \cdot \|\mathbf{v}\|$ | 同向平行 |
| $90^\circ$ | $0$ | $= 0$ | **垂直（正交）** |
| $180^\circ$ | $-1$ | $= -\|\mathbf{u}\| \cdot \|\mathbf{v}\|$ | 反向平行 |

> **记忆方法**：
> - 点积为正 $\implies$ 夹角小于 $90^\circ$（两向量方向大致相同）
> - 点积为零 $\implies$ 夹角等于 $90^\circ$（两向量垂直）
> - 点积为负 $\implies$ 夹角大于 $90^\circ$（两向量方向大致相反）

---

#### 水平向量与垂直向量

一个特殊的例子：**水平向量**的 $y$ 分量为零，即 $\mathbf{h} = (h_x, 0)$（$h_x \neq 0$），它的方向平行于 $x$ 轴。**垂直向量**的 $x$ 分量为零，即 $\mathbf{v} = (0, v_y)$（$v_y \neq 0$），它的方向平行于 $y$ 轴。

水平向量总是垂直于垂直向量。用点积验证：

$$
(h_x, 0) \cdot (0, v_y) = h_x \cdot 0 + 0 \cdot v_y = 0
$$

> **直观理解**：水平向量沿着 $x$ 轴方向，垂直向量沿着 $y$ 轴方向。在平面直角坐标系中，$x$ 轴和 $y$ 轴本身就互相垂直，因此与它们平行的向量自然也互相垂直。这就像棋盘上的横线和竖线——每条横线都与每条竖线垂直相交。

> **⚠️ 注意事项**：这里要求 $h_x \neq 0$ 且 $v_y \neq 0$。如果 $h_x = 0$，则 $\mathbf{h} = (0, 0)$ 退化为零向量；如果 $v_y = 0$，则 $\mathbf{v} = (0, 0)$ 也退化为零向量。零向量没有固定方向，不属于"水平向量"或"垂直向量"的讨论范畴。

> **💡 几何意义**：从斜率的角度看，水平向量的斜率 $k_h = \dfrac{0}{h_x} = 0$，而垂直向量的斜率 $k_v = \dfrac{v_y}{0}$ 是未定义的（无穷大）。零乘以无穷大并不等于 $-1$，因此斜率公式 $k_1 \cdot k_2 = -1$ 在这里不适用——这正是我们单独讨论"水平 $\perp$ 垂直"这一特殊情况的原因。

---

#### 通过斜率判断垂直

如果两个非零向量都不与坐标轴平行（即 $x$ 和 $y$ 分量均不为零），我们也可以用斜率来判断垂直。设向量 $\mathbf{u}$ 的斜率为 $k_1 = \frac{u_y}{u_x}$，向量 $\mathbf{v}$ 的斜率为 $k_2 = \frac{v_y}{v_x}$，那么：

$$
\boxed{\mathbf{u} \perp \mathbf{v} \iff k_1 \cdot k_2 = -1}
$$

> **推导**：由点积为零的条件：
> $$
> u_x v_x + u_y v_y = 0 \implies u_x v_x = -u_y v_y \implies \frac{u_y}{u_x} \cdot \frac{v_y}{v_x} = -1
> $$
> 即 $k_1 \cdot k_2 = -1$。

> **🔗 与坐标几何的联系**：如果你曾在坐标几何中学过"两条直线垂直当且仅当它们的斜率乘积为 $-1$"，你会发现这里完全一致。事实上，向量 $\mathbf{u}$ 所在直线的斜率正是 $\dfrac{u_y}{u_x}$，向量 $\mathbf{v}$ 所在直线的斜率正是 $\dfrac{v_y}{v_x}$。因此，**向量垂直的斜率条件与直线垂直的斜率条件本质上是同一个结论**。

> **📌 应用示例**：已知 $\mathbf{u} = (2, 4)$，$\mathbf{v} = (6, -3)$。
> - $k_1 = \dfrac{4}{2} = 2$，$k_2 = \dfrac{-3}{6} = -\dfrac{1}{2}$
> - $k_1 \cdot k_2 = 2 \times \left(-\dfrac{1}{2}\right) = -1$ ✓
> - 因此 $\mathbf{u} \perp \mathbf{v}$。用点积验证：$(2)(6) + (4)(-3) = 12 - 12 = 0$，一致。

> **⚠️ 该方法的局限性**：如果其中一个向量是水平向量（$k = 0$）或垂直向量（$k$ 未定义），斜率乘积法不适用。例如 $\mathbf{u} = (3, 0)$（水平）和 $\mathbf{v} = (0, 5)$（垂直）显然是垂直的，但 $k_1 = 0$，$k_2$ 未定义，无法计算乘积。此时应退回点积法或直接使用"水平 $\perp$ 垂直"的结论。

> **关于零向量的说明**：零向量 $\mathbf{0} = (0, 0)$ 没有固定方向。按照惯例，在技术讨论中它被视为与所有向量既平行又垂直，但在实际解题中我们通常排除它。

---

#### 垂直向量判定方法速查

| 方法 | 条件 | 适用场景 |
|:---|:---|:---|
| **点积为零** | $\mathbf{u} \cdot \mathbf{v} = 0$ | 通用（任何向量） |
| **斜率乘积为 $-1$** | $k_1 \cdot k_2 = -1$ | 两向量均不与坐标轴平行 |
| **水平 $\perp$ 垂直** | $(h_x, 0) \cdot (0, v_y) = 0$ | 特殊情况 |

---

### 📌 例题 2.1：向量基础运算

**例题 1**（向量表示、模与单位向量）

已知两点 $A(1, 2)$ 和 $B(5, -1)$。

（a）求向量 $\overrightarrow{AB}$ 用 $\mathbf{i}$-$\mathbf{j}$ 形式表示。
（b）求 $|\overrightarrow{AB}|$。
（c）求与 $\overrightarrow{AB}$ 同方向的单位向量。

**思路分析**：
- 从 $A$ 到 $B$ 的向量 = $B$ 的位置减 $A$ 的位置
- 模 = 各分量平方和的平方根
- 单位向量 = 原向量除以模

**解**：

（a）

$$
\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A = (5\mathbf{i} - \mathbf{j}) - (\mathbf{i} + 2\mathbf{j}) = (5-1)\mathbf{i} + (-1-2)\mathbf{j} = 4\mathbf{i} - 3\mathbf{j}
$$

（b）

$$
|\overrightarrow{AB}| = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

（c）同方向的单位向量为：

$$
\hat{\mathbf{v}} = \frac{4\mathbf{i} - 3\mathbf{j}}{5} = \frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}
$$

验证模长：$\sqrt{(4/5)^2 + (-3/5)^2} = \sqrt{16/25 + 9/25} = \sqrt{25/25} = 1$。✓

---

**例题 2**（向量加法、数乘与向量相等——解方程组）

已知 $\mathbf{a} = 2\mathbf{i} + 3\mathbf{j}$，$\mathbf{b} = -\mathbf{i} + 2\mathbf{j}$。求：

（a）$\mathbf{a} + \mathbf{b}$
（b）$2\mathbf{a} - 3\mathbf{b}$
（c）实数 $p$ 和 $q$ 使得 $p\mathbf{a} + q\mathbf{b} = 7\mathbf{i} + 8\mathbf{j}$

**思路分析**：
- 加法和数乘都是对分量分别操作
- 对于第（c）问，先展开左侧，利用向量相等原理（$\mathbf{i}$ 和 $\mathbf{j}$ 的系数分别相等）建立方程组

**解**：

（a）

$$
\mathbf{a} + \mathbf{b} = (2\mathbf{i} + 3\mathbf{j}) + (-\mathbf{i} + 2\mathbf{j}) = (2-1)\mathbf{i} + (3+2)\mathbf{j} = \mathbf{i} + 5\mathbf{j}
$$

（b）

$$
2\mathbf{a} - 3\mathbf{b} = 2(2\mathbf{i} + 3\mathbf{j}) - 3(-\mathbf{i} + 2\mathbf{j}) = (4\mathbf{i} + 6\mathbf{j}) + (3\mathbf{i} - 6\mathbf{j}) = 7\mathbf{i} + 0\mathbf{j} = 7\mathbf{i}
$$

（c）设 $p\mathbf{a} + q\mathbf{b} = 7\mathbf{i} + 8\mathbf{j}$，即：

$$
p(2\mathbf{i} + 3\mathbf{j}) + q(-\mathbf{i} + 2\mathbf{j}) = 7\mathbf{i} + 8\mathbf{j}
$$

先展开括号：

$$
2p\mathbf{i} + 3p\mathbf{j} - q\mathbf{i} + 2q\mathbf{j} = 7\mathbf{i} + 8\mathbf{j}
$$

合并 $\mathbf{i}$ 和 $\mathbf{j}$ 的系数：

$$
(2p - q)\mathbf{i} + (3p + 2q)\mathbf{j} = 7\mathbf{i} + 8\mathbf{j}
$$

利用向量相等原理，$\mathbf{i}$ 的系数必须相等，$\mathbf{j}$ 的系数也必须相等：

$$
\begin{cases}
2p - q = 7 \quad \text{（① $\mathbf{i}$ 系数相等）} \\[4pt]
3p + 2q = 8 \quad \text{（② $\mathbf{j}$ 系数相等）}
\end{cases}
$$

解这个方程组。从①式得 $q = 2p - 7$，代入②式：

$$
3p + 2(2p - 7) = 8 \implies 3p + 4p - 14 = 8 \implies 7p = 22 \implies p = \frac{22}{7}
$$

于是 $q = 2 \times \frac{22}{7} - 7 = \frac{44}{7} - \frac{49}{7} = -\frac{5}{7}$。

因此 $p = \frac{22}{7}$，$q = -\frac{5}{7}$。✓

---

**例题 3**（位置向量、位移与垂直向量判定）

三点 $P$、$Q$、$R$ 的位置向量分别为 $\mathbf{p} = 3\mathbf{i} + \mathbf{j}$，$\mathbf{q} = 5\mathbf{i} - 2\mathbf{j}$，$\mathbf{r} = -2\mathbf{i} + 4\mathbf{j}$。

（a）求 $\overrightarrow{PQ}$ 和 $\overrightarrow{PR}$。
（b）已知 $\overrightarrow{PS} = 2\overrightarrow{PQ}$，求 $S$ 的位置向量。
（c）判断 $\overrightarrow{PQ}$ 与 $\overrightarrow{PR}$ 是否垂直。

**思路分析**：
- $\overrightarrow{PQ} = \mathbf{q} - \mathbf{p}$（终点减起点）
- $\overrightarrow{PS} = \mathbf{s} - \mathbf{p}$，代入已知条件解出 $\mathbf{s}$
- 垂直判定：计算点积，若为零则垂直

**解**：

（a）

$$
\overrightarrow{PQ} = \mathbf{q} - \mathbf{p} = (5\mathbf{i} - 2\mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = 2\mathbf{i} - 3\mathbf{j}
$$

$$
\overrightarrow{PR} = \mathbf{r} - \mathbf{p} = (-2\mathbf{i} + 4\mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = -5\mathbf{i} + 3\mathbf{j}
$$

（b）设 $S$ 的位置向量为 $\mathbf{s}$。由 $\overrightarrow{PS} = \mathbf{s} - \mathbf{p}$ 且 $\overrightarrow{PS} = 2\overrightarrow{PQ}$，得：

$$
\mathbf{s} - \mathbf{p} = 2(2\mathbf{i} - 3\mathbf{j}) = 4\mathbf{i} - 6\mathbf{j}
$$

所以：

$$
\mathbf{s} = \mathbf{p} + (4\mathbf{i} - 6\mathbf{j}) = (3\mathbf{i} + \mathbf{j}) + (4\mathbf{i} - 6\mathbf{j}) = 7\mathbf{i} - 5\mathbf{j}
$$

因此 $S$ 的坐标为 $(7, -5)$。

（c）计算点积：

$$
\overrightarrow{PQ} \cdot \overrightarrow{PR} = (2)(-5) + (-3)(3) = -10 - 9 = -19 \neq 0
$$

因为点积不为零，所以 $\overrightarrow{PQ}$ 与 $\overrightarrow{PR}$ **不垂直**。

> **如果用斜率法验证**：
> $k_{PQ} = \dfrac{-3}{2} = -1.5$
> $k_{PR} = \dfrac{3}{-5} = -0.6$
> $k_{PQ} \cdot k_{PR} = (-1.5)(-0.6) = 0.9 \neq -1$
> 同样得出不垂直。✓

---

## 2.2 向量的实际运用

### 2.2.1 向量几何——深度解析

向量是解决平面几何问题的强大工具。通过将几何关系转化为向量方程，我们可以用代数方法精确求解，避免画图的不精确性。

#### 核心思想

**向量几何的本质**：用向量运算（加减、数乘）来表示几何关系。

| 几何关系 | 向量表达 |
|:---|:---|
| 从 $A$ 到 $B$ 的线段 | $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$ |
| $A$ 和 $B$ 的中点 $M$ | $\mathbf{r}_M = \dfrac{\mathbf{r}_A + \mathbf{r}_B}{2}$ |
| $P$ 分 $AB$ 为 $m:n$ | $\mathbf{r}_P = \dfrac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}$ |
| $AB \parallel CD$ | $\overrightarrow{AB} = k \cdot \overrightarrow{CD}$ |
| $AB \perp CD$ | $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$ |
| $A,B,C$ 共线 | $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$（存在 $k$） |

#### 中点公式——为什么是这样？

设 $M$ 是 $AB$ 的中点。从 $A$ 到 $M$ 的位移是 $\overrightarrow{AB}$ 的一半：

$$
\mathbf{r}_M = \mathbf{r}_A + \frac{1}{2}\overrightarrow{AB} = \mathbf{r}_A + \frac{1}{2}(\mathbf{r}_B - \mathbf{r}_A) = \frac{2\mathbf{r}_A + \mathbf{r}_B - \mathbf{r}_A}{2} = \frac{\mathbf{r}_A + \mathbf{r}_B}{2}
$$

#### 分点公式——详细推导

设点 $P$ 分线段 $AB$ 为 $AP:PB = m:n$（即 $P$ 靠近 $A$ 的方向上，$AP$ 占 $m$ 份，$PB$ 占 $n$ 份）。

这意味着 $P$ 位于从 $A$ 到 $B$ 的 $\dfrac{m}{m+n}$ 处（从 $A$ 算起）。所以：

$$
\begin{aligned}
\mathbf{r}_P &= \mathbf{r}_A + \frac{m}{m+n}\overrightarrow{AB} \\
&= \mathbf{r}_A + \frac{m}{m+n}(\mathbf{r}_B - \mathbf{r}_A) \\
&= \frac{(m+n)\mathbf{r}_A + m\mathbf{r}_B - m\mathbf{r}_A}{m+n} \\
&= \frac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}
\end{aligned}
$$

> **记忆技巧**：分点公式中，$A$ 的系数是 $n$（对面那段的比例），$B$ 的系数是 $m$（对面那段的比例）。交叉相乘！
>
> 例如 $AP:PB = 2:3$（$m=2, n=3$），则：
> $$\mathbf{r}_P = \frac{3\mathbf{r}_A + 2\mathbf{r}_B}{5}$$
> $A$ 的系数是 $3$（对面的 $PB$ 是 $3$ 份），$B$ 的系数是 $2$（对面的 $AP$ 是 $2$ 份）。

#### 平行向量——为什么写成 $\overrightarrow{AB} = k \cdot \overrightarrow{CD}$？

两个非零向量 $\mathbf{a}$ 和 $\mathbf{b}$ **平行**（即方向相同或相反）当且仅当存在一个实数 $k$ 使得：

$$
\boxed{\mathbf{a} = k\mathbf{b}}
$$

即一个向量是另一个向量的标量倍。

> **🔍 深入理解**：这个式子的含义可以从两个角度解读：
>
> **几何角度**：平行意味着两个向量的方向线重合或平行。方向相同（$k > 0$）时，两个向量指向同一侧；方向相反（$k < 0$）时，两个向量指向相反侧。$|k|$ 的大小决定了两向量长度的比值：$|\mathbf{a}| = |k| \cdot |\mathbf{b}|$。
>
> **代数角度**：写成坐标形式，$\mathbf{a} = (a_x, a_y)$，$\mathbf{b} = (b_x, b_y)$，则 $\mathbf{a} = k\mathbf{b}$ 给出：
> $$
> (a_x, a_y) = (k b_x, k b_y)
> $$
> 因此 $\dfrac{a_x}{b_x} = \dfrac{a_y}{b_y} = k$（分母不为零）。也就是说，**对应分量成比例**。
>
> **为什么要用 $\overrightarrow{AB} = k \cdot \overrightarrow{CD}$ 来表示 $AB \parallel CD$？**
>
> 线段 $AB$ 的方向由向量 $\overrightarrow{AB}$ 决定，线段 $CD$ 的方向由向量 $\overrightarrow{CD}$ 决定。两条线段平行，意味着这两个方向向量平行（即存在标量 $k$ 使 $\overrightarrow{AB} = k \cdot \overrightarrow{CD}$）。
>
> > **注意**：这里的 $k$ 可以是任何非零实数。
> > - $k > 0$：$\overrightarrow{AB}$ 与 $\overrightarrow{CD}$ **同向**
> > - $k < 0$：$\overrightarrow{AB}$ 与 $\overrightarrow{CD}$ **反向**（但仍平行）
> > - 如果同时要求两线段长度相等（如平行四边形的对边），则 $|k| = 1$

> **📌 示例**：已知 $\overrightarrow{AB} = (6, 9)$，$\overrightarrow{CD} = (2, 3)$。
> 因为 $\dfrac{6}{2} = \dfrac{9}{3} = 3$，所以 $\overrightarrow{AB} = 3 \cdot \overrightarrow{CD}$，故 $AB \parallel CD$。此时 $k = 3 > 0$，两线段同向，且 $AB$ 的长度是 $CD$ 的 $3$ 倍。

---

#### 垂直——为什么写成 $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$？

两条线段 $AB$ 和 $CD$ 垂直（即夹角为 $90^\circ$）当且仅当它们的方向向量点积为零：

$$
\boxed{\overrightarrow{AB} \cdot \overrightarrow{CD} = 0}
$$

> **🔍 与点积的联系**：在 2.1.8 节中我们已经学过，两个非零向量 $\mathbf{u}$ 和 $\mathbf{v}$ 垂直 $\iff$ $\mathbf{u} \cdot \mathbf{v} = 0$。这里完全相同，只是将 $\mathbf{u}$ 替换为 $\overrightarrow{AB}$，将 $\mathbf{v}$ 替换为 $\overrightarrow{CD}$。
>
> 回顾点积的几何定义：
> $$
> \overrightarrow{AB} \cdot \overrightarrow{CD} = |\overrightarrow{AB}| \cdot |\overrightarrow{CD}| \cdot \cos\theta
> $$
> 其中 $\theta$ 是两向量之间的夹角。当 $\theta = 90^\circ$ 时，$\cos 90^\circ = 0$，因此点积为零。
>
> **注意**：点积的结果是**标量**（一个数），不是向量。因此 $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$ 是一个标量方程。

> **⚠️ 与平行条件的对比**：
> - **平行**：$\overrightarrow{AB} = k \cdot \overrightarrow{CD}$（向量方程，涉及比例关系）
> - **垂直**：$\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$（标量方程，仅要求乘积为零）
>
> 平行条件需要找到一个具体的 $k$ 值，而垂直条件只需要计算一个数值并检查是否为零——通常比平行条件更容易验证。

> **📌 示例**：已知 $\overrightarrow{AB} = (3, 1)$，$\overrightarrow{CD} = (2, -6)$。
> 计算点积：$3 \times 2 + 1 \times (-6) = 6 - 6 = 0$。
> 因此 $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$，故 $AB \perp CD$。✓

---

#### 三点共线的判定——为什么是 $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$？

三点 $A$、$B$、$C$ 共线（即位于同一直线上）当且仅当存在一个实数 $k$ 使得：

$$
\boxed{\overrightarrow{AB} = k \cdot \overrightarrow{BC}}
$$

或等价地，$\overrightarrow{AB}$ 与 $\overrightarrow{AC}$ 平行（或 $\overrightarrow{AB}$ 与 $\overrightarrow{BC}$ 平行）。

> **🔍 为什么？** 如果 $A$、$B$、$C$ 三点共线，那么从 $A$ 到 $B$ 的位移和从 $B$ 到 $C$ 的位移沿着同一条直线。这意味着 $\overrightarrow{AB}$ 和 $\overrightarrow{BC}$ 的方向要么相同（$k > 0$），要么相反（$k < 0$）。因此存在标量 $k$ 使 $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$。
>
> 反过来，如果 $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$，则两个向量平行。又因为它们共享点 $B$（$\overrightarrow{AB}$ 的终点是 $B$，$\overrightarrow{BC}$ 的起点是 $B$），所以 $A$、$B$、$C$ 必然在同一直线上。
>
> **关键点**：平行 + 公共点 $\implies$ 共线。如果没有公共点，平行只能说明两线段方向相同，不能保证三点共线。

> **💡 三种等价判定方式**（根据已知条件灵活选用）：
>
> | 判定方式 | 条件 | 说明 |
> |:---|:---|:---|
> | 方式一 | $\overrightarrow{AB} = k \cdot \overrightarrow{BC}$ | 需要 $B$ 是公共点（最常用） |
> | 方式二 | $\overrightarrow{AB} = k \cdot \overrightarrow{AC}$ | 需要 $A$ 是公共点 |
> | 方式三 | $\overrightarrow{AC} = k \cdot \overrightarrow{BC}$ | 需要 $C$ 是公共点 |
>
> 三种方式本质上一样——都利用了"平行 + 公共点"的原理。选择哪种方式通常取决于哪组向量更容易计算。

> **📌 示例**：已知 $A(1, 2)$，$B(3, 4)$，$C(7, 8)$。
> $$
> \overrightarrow{AB} = (3-1, 4-2) = (2, 2), \quad \overrightarrow{BC} = (7-3, 8-4) = (4, 4)
> $$
> 观察发现 $\overrightarrow{BC} = 2 \cdot (2, 2) = 2 \cdot \overrightarrow{AB}$，即 $\overrightarrow{AB} = \frac{1}{2} \cdot \overrightarrow{BC}$（取 $k = \frac{1}{2}$）。因此 $A$、$B$、$C$ 三点共线。
>
> **验证**：也可用 $\overrightarrow{AC}$ 验证。
> $\overrightarrow{AC} = (7-1, 8-2) = (6, 6) = 3 \cdot (2, 2) = 3 \cdot \overrightarrow{AB}$，同样得出共线。✓

---

### 📌 例题 2.2：向量几何应用

**例题 1**（平行四边形与中点——配图说明）

在平行四边形 $ABCD$ 中，$A$、$B$、$C$ 的位置向量分别为 $\mathbf{a} = \mathbf{i} + 2\mathbf{j}$，$\mathbf{b} = 4\mathbf{i} + 3\mathbf{j}$，$\mathbf{c} = 6\mathbf{i} + \mathbf{j}$。求：

（a）$D$ 的位置向量
（b）对角线 $AC$ 与 $BD$ 的交点 $M$ 的位置向量

**思路分析**：

> 先理解平行四边形的结构。顶点按 $A \to B \to C \to D \to A$ 的顺序排列。
>
> **平行四边形的关键性质**：对边平行且相等。
> - $AB \parallel DC$ 且 $AB = DC$
> - $AD \parallel BC$ 且 $AD = BC$
>
> 这意味着 $\overrightarrow{AD} = \overrightarrow{BC}$ 或 $\overrightarrow{AB} = \overrightarrow{DC}$。
>
> 另外，平行四边形的对角线**互相平分**，即 $AC$ 的中点 = $BD$ 的中点。

**解**：

（a）在平行四边形 $ABCD$ 中，对边 $AD$ 和 $BC$ 平行且相等，所以 $\overrightarrow{AD} = \overrightarrow{BC}$。

先求 $\overrightarrow{BC} = \mathbf{c} - \mathbf{b}$：

$$
\overrightarrow{BC} = (6\mathbf{i} + \mathbf{j}) - (4\mathbf{i} + 3\mathbf{j}) = 2\mathbf{i} - 2\mathbf{j}
$$

因为 $\overrightarrow{AD} = \overrightarrow{BC} = 2\mathbf{i} - 2\mathbf{j}$，而 $\overrightarrow{AD} = \mathbf{d} - \mathbf{a}$，所以：

$$
\mathbf{d} = \mathbf{a} + \overrightarrow{AD} = (\mathbf{i} + 2\mathbf{j}) + (2\mathbf{i} - 2\mathbf{j}) = 3\mathbf{i}
$$

所以 $D$ 的坐标为 $(3, 0)$。

**验证**：也可用 $\overrightarrow{AB} = \overrightarrow{DC}$ 来求。
$\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (4\mathbf{i} + 3\mathbf{j}) - (\mathbf{i} + 2\mathbf{j}) = 3\mathbf{i} + \mathbf{j}$
$\overrightarrow{DC} = \mathbf{c} - \mathbf{d}$，所以 $\mathbf{c} - \mathbf{d} = 3\mathbf{i} + \mathbf{j}$，解得 $\mathbf{d} = \mathbf{c} - (3\mathbf{i} + \mathbf{j}) = (6\mathbf{i} + \mathbf{j}) - (3\mathbf{i} + \mathbf{j}) = 3\mathbf{i}$，一致。✓

（b）平行四边形的对角线互相平分。因此 $M$ 既是 $AC$ 的中点，也是 $BD$ 的中点。

用 $AC$ 的中点计算：

$$
\mathbf{m} = \frac{\mathbf{a} + \mathbf{c}}{2} = \frac{(\mathbf{i} + 2\mathbf{j}) + (6\mathbf{i} + \mathbf{j})}{2} = \frac{7\mathbf{i} + 3\mathbf{j}}{2} = 3.5\mathbf{i} + 1.5\mathbf{j}
$$

验证用 $BD$ 的中点：$\frac{\mathbf{b} + \mathbf{d}}{2} = \frac{(4\mathbf{i} + 3\mathbf{j}) + 3\mathbf{i}}{2} = \frac{7\mathbf{i} + 3\mathbf{j}}{2}$，一致。✓

---

**例题 2**（共线判定与比值——如何证明三点共线）

三点 $A$、$B$、$C$ 的位置向量分别为 $\mathbf{a} = 2\mathbf{i} + \mathbf{j}$，$\mathbf{b} = 5\mathbf{i} + 4\mathbf{j}$，$\mathbf{c} = 8\mathbf{i} + 7\mathbf{j}$。

（a）证明 $A$、$B$、$C$ 三点共线。
（b）求 $AB:BC$ 的比值。

**思路分析**：

> 证明三点共线的标准方法：
> 1. 计算 $\overrightarrow{AB}$ 和 $\overrightarrow{BC}$（或 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$）
> 2. 判断它们是否平行（即是否存在标量 $k$ 使得一个等于另一个乘以 $k$）
> 3. 如果平行且有一个公共点（$B$ 是 $\overrightarrow{AB}$ 和 $\overrightarrow{BC}$ 的公共点），则三点共线

**解**：

（a）计算向量：

$$
\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 4\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 3\mathbf{i} + 3\mathbf{j}
$$

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (8\mathbf{i} + 7\mathbf{j}) - (5\mathbf{i} + 4\mathbf{j}) = 3\mathbf{i} + 3\mathbf{j}
$$

观察发现 $\overrightarrow{BC} = \overrightarrow{AB}$，即 $\overrightarrow{BC} = 1 \cdot \overrightarrow{AB}$。存在标量 $k = 1$ 使得 $\overrightarrow{BC} = k\overrightarrow{AB}$，所以 $\overrightarrow{AB} \parallel \overrightarrow{BC}$。又因为这两个向量都通过点 $B$，故 $A$、$B$、$C$ 共线。

> **注意**：也可以验证 $\overrightarrow{AC}$ 与 $\overrightarrow{AB}$ 的关系。
> $\overrightarrow{AC} = \mathbf{c} - \mathbf{a} = (8\mathbf{i} + 7\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 6\mathbf{i} + 6\mathbf{j} = 2(3\mathbf{i} + 3\mathbf{j}) = 2\overrightarrow{AB}$
> 同样得出共线结论。

（b）因为 $\overrightarrow{BC} = \overrightarrow{AB}$，且方向相同，所以 $\overrightarrow{AB}$ 和 $\overrightarrow{BC}$ 的长度相等。即 $AB = BC$，因此 $AB:BC = 1:1$。

换句话说，$B$ 是线段 $AC$ 的中点。

---

**例题 3**（分点公式 + 垂直验证——综合应用）

在 $\triangle OAB$ 中，$C$ 在 $OA$ 上且 $OC:CA = 2:1$，$D$ 在 $AB$ 上且 $AD:DB = 3:1$。设 $\overrightarrow{OA} = \mathbf{a}$，$\overrightarrow{OB} = \mathbf{b}$。

（a）用 $\mathbf{a}$ 和 $\mathbf{b}$ 表示 $\overrightarrow{OD}$。
（b）用 $\mathbf{a}$ 和 $\mathbf{b}$ 表示 $\overrightarrow{CD}$。
（c）已知 $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$，$\mathbf{b} = \mathbf{i} + 6\mathbf{j}$，判断 $\overrightarrow{OC}$ 与 $\overrightarrow{OD}$ 是否垂直。

**思路分析**：

> 这是一个"用基底表示向量"的典型问题。$\mathbf{a}$ 和 $\mathbf{b}$ 是基底，所有其他向量都要用它们表示。
>
> 关键步骤：
> 1. 确定分点 $C$ 在 $OA$ 上的位置：$OC:CA = 2:1$ 意味着 $OC = \frac{2}{3}OA$
> 2. 确定分点 $D$ 在 $AB$ 上的位置：$AD:DB = 3:1$ 意味着 $AD = \frac{3}{4}AB$
> 3. 用分点公式或直接加减法表示向量
> 4. 垂直判定：代入具体数值后计算点积

**解**：

（a）先表示 $D$ 的位置。

方法一（分点公式）：$D$ 分 $AB$ 为 $AD:DB = 3:1$，即从 $A$ 到 $B$ 的方向上，$D$ 位于 $\frac{3}{4}$ 处。

由分点公式（$m=3, n=1$）：

$$
\mathbf{r}_D = \frac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n} = \frac{1 \cdot \mathbf{a} + 3 \cdot \mathbf{b}}{3+1} = \frac{\mathbf{a} + 3\mathbf{b}}{4}
$$

方法二（直接法）：从 $A$ 出发走到 $B$ 的 $\frac{3}{4}$ 处。

$$
\overrightarrow{OD} = \overrightarrow{OA} + \frac{3}{4}\overrightarrow{AB}
$$

而 $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \mathbf{b} - \mathbf{a}$，所以：

$$
\overrightarrow{OD} = \mathbf{a} + \frac{3}{4}(\mathbf{b} - \mathbf{a}) = \mathbf{a} + \frac{3}{4}\mathbf{b} - \frac{3}{4}\mathbf{a} = \frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}
$$

注意 $\frac{\mathbf{a} + 3\mathbf{b}}{4} = \frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}$，两种方法结果一致。✓

（b）$C$ 在 $OA$ 上且 $OC:CA = 2:1$，所以 $C$ 分 $\overrightarrow{OA}$ 为 $2:1$（从 $O$ 算起）。因此：

$$
\overrightarrow{OC} = \frac{2}{3}\overrightarrow{OA} = \frac{2}{3}\mathbf{a}
$$

于是：

$$
\overrightarrow{CD} = \overrightarrow{OD} - \overrightarrow{OC} = \left(\frac{1}{4}\mathbf{a} + \frac{3}{4}\mathbf{b}\right) - \frac{2}{3}\mathbf{a}
$$

通分计算 $\mathbf{a}$ 的系数：$\frac{1}{4} - \frac{2}{3} = \frac{3}{12} - \frac{8}{12} = -\frac{5}{12}$。

所以：

$$
\overrightarrow{CD} = -\frac{5}{12}\mathbf{a} + \frac{3}{4}\mathbf{b}
$$

（c）代入 $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$，$\mathbf{b} = \mathbf{i} + 6\mathbf{j}$：

先求 $\overrightarrow{OC}$：

$$
\overrightarrow{OC} = \frac{2}{3}(3\mathbf{i} + 2\mathbf{j}) = 2\mathbf{i} + \frac{4}{3}\mathbf{j}
$$

再求 $\overrightarrow{OD}$：

$$
\begin{aligned}
\overrightarrow{OD} &= \frac{1}{4}(3\mathbf{i} + 2\mathbf{j}) + \frac{3}{4}(\mathbf{i} + 6\mathbf{j}) \\
&= \left(\frac{3}{4} + \frac{3}{4}\right)\mathbf{i} + \left(\frac{1}{2} + \frac{9}{2}\right)\mathbf{j} \\
&= \frac{6}{4}\mathbf{i} + \frac{10}{2}\mathbf{j} \\
&= \frac{3}{2}\mathbf{i} + 5\mathbf{j}
\end{aligned}
$$

计算点积：

$$
\overrightarrow{OC} \cdot \overrightarrow{OD} = \left(2\right)\left(\frac{3}{2}\right) + \left(\frac{4}{3}\right)(5) = 3 + \frac{20}{3} = \frac{9}{3} + \frac{20}{3} = \frac{29}{3} \neq 0
$$

点积不为零，所以 $\overrightarrow{OC}$ 与 $\overrightarrow{OD}$ **不垂直**。

---

### 2.2.2 速度的合成与分解

速度是一个向量。当一个物体同时参与两个或更多运动时，它的合速度是这些速度的向量和。

#### 相对速度公式

设物体 $A$ 相对于参考系 $C$ 的速度为 $\mathbf{v}_{A/C}$，物体 $A$ 相对于物体 $B$ 的速度为 $\mathbf{v}_{A/B}$，物体 $B$ 相对于参考系 $C$ 的速度为 $\mathbf{v}_{B/C}$，则：

$$
\mathbf{v}_{A/C} = \mathbf{v}_{A/B} + \mathbf{v}_{B/C}
$$

> **直观理解**：
> - 你在火车上行走，速度为 $\mathbf{v}_{A/B}$（你相对于火车）
> - 火车相对于地面行驶，速度为 $\mathbf{v}_{B/C}$（火车相对于地面）
> - 你相对于地面的速度 $\mathbf{v}_{A/C}$ 就是两者之和
>
> **另一个例子**：一艘船在河中行驶。
> - 船在静水中的速度 = $\mathbf{v}_{B/W}$（船相对于水）
> - 水流速度 = $\mathbf{v}_{W/G}$（水相对于地面）
> - 船相对于地面的实际速度 = $\mathbf{v}_{B/W} + \mathbf{v}_{W/G}$

#### 速度的分解

与合成相反，将一个速度向量分解为两个互相垂直的分量（通常沿水平方向和垂直方向）称为**速度的分解**（resolution of velocities）。

##### 为什么要分解速度？

在实际问题中，我们经常需要分别考察运动在不同方向上的行为。例如：

- **抛体运动**：水平方向不受力（匀速直线运动），垂直方向受重力（匀加速运动）——只有将初速度分解为水平和垂直分量，才能分别分析这两个方向的运动。
- **斜面上的运动**：需要将速度分解为沿斜面方向和垂直于斜面方向。
- **导航**：飞机需要将速度分解为平行和垂直于航线的分量，以修正风的影响。

分解的**核心思想**是：**一个向量可以用两个互相垂直的分量唯一表示**，这两个分量的作用相互独立，可以分别分析后再合成。

##### 标准分解：水平与垂直

设速度 $\mathbf{v}$ 的大小为 $v$（速率），与水平方向的夹角为 $\theta$，则：

$$
\boxed{\mathbf{v} = (v\cos\theta)\mathbf{i} + (v\sin\theta)\mathbf{j}}
$$

其中 $v_x = v\cos\theta$ 是水平分量，$v_y = v\sin\theta$ 是垂直分量。

> **🎯 核心直觉——一根棍子的故事**
>
> 想象你有一根长度为 $v$ 的棍子，一端靠在地板上，另一端靠在墙上，棍子与地板（水平方向）的夹角为 $\theta$。
>
> ```
>     墙
>     |\
>     | \
>     |  \  棍子（长度 v）
>     |   \
>     |    \
>     |θ    \
>     ———————— 地板
> ```
>
> 这根棍子在**地板上的影子**（水平投影）的长度就是 $v\cos\theta$——这是**水平分量**。
> 这根棍子在**墙上的影子**（垂直投影）的长度就是 $v\sin\theta$——这是**垂直分量**。
>
> 这正是三角函数的几何定义：
> - **$\cos\theta$ = 邻边 / 斜边**：在直角三角形中，邻边（水平投影）= 斜边（棍子长度）$\times \cos\theta$
> - **$\sin\theta$ = 对边 / 斜边**：在直角三角形中，对边（垂直投影）= 斜边（棍子长度）$\times \sin\theta$
>
> 无论棍子怎么倾斜，它在墙上和地板上的影子长度之和的平方（勾股定理）始终等于棍子长度的平方：
> $$
> (v\cos\theta)^2 + (v\sin\theta)^2 = v^2(\cos^2\theta + \sin^2\theta) = v^2
> $$
> 这正是三角恒等式 $\cos^2\theta + \sin^2\theta = 1$ 的几何来源！
>
> > **💡 记忆方法**：把速度向量想象成这根棍子。
> > - **$\cos$ 连着水平方向**（地板）——$\cos$ 开头是 c，像"地"板的英文 "ground" 的 g 的镜像？更简单的记法：**"cos 是 contact（接触），紧贴地面"**
> > - **$\sin$ 连着垂直方向**（墙）——$\sin$ 开头是 s，像"上"（shàng）的拼音首字母
> > - 角度 $\theta$ 是从水平方向（地板）开始测量的
>
> **正式推导**：将速度向量 $\mathbf{v}$ 置于坐标系中，起点在原点，与水平方向（$x$ 轴正方向）夹角为 $\theta$。从终点向 $x$ 轴和 $y$ 轴分别作垂线，得到一个直角三角形。棍子就是斜边，地板上的影子是水平直角边，墙上的影子是垂直直角边。
>
> - 水平分量 $v_x$（地板上的影子）：$v_x = v \cdot \cos\theta$
> - 垂直分量 $v_y$（墙上的影子）：$v_y = v \cdot \sin\theta$
>
> 根据勾股定理验证：
> $$
> v_x^2 + v_y^2 = (v\cos\theta)^2 + (v\sin\theta)^2 = v^2(\cos^2\theta + \sin^2\theta) = v^2
> $$
> 因此 $|\mathbf{v}| = \sqrt{v_x^2 + v_y^2} = v$，与原速率一致。✓

##### 分量符号的判断

分量的正负由角度 $\theta$ 所在的象限决定：

| $\theta$ 范围 | 象限 | $\cos\theta$ | $\sin\theta$ | $v_x$ | $v_y$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0^\circ < \theta < 90^\circ$ | 第一象限 | $+$ | $+$ | $+$（向右） | $+$（向上） |
| $90^\circ < \theta < 180^\circ$ | 第二象限 | $-$ | $+$ | $-$（向左） | $+$（向上） |
| $180^\circ < \theta < 270^\circ$ | 第三象限 | $-$ | $-$ | $-$（向左） | $-$（向下） |
| $270^\circ < \theta < 360^\circ$ | 第四象限 | $+$ | $-$ | $+$（向右） | $-$（向下） |

> **记忆口诀**："**右正左负，上正下负**"。$+\mathbf{i}$ 指向右，$-\mathbf{i}$ 指向左；$+\mathbf{j}$ 指向上，$-\mathbf{j}$ 指向下。

##### 由分量求合速度的大小和方向

分解的逆过程——已知两个分量 $v_x$ 和 $v_y$，求原速度的大小和方向：

$$
\boxed{v = \sqrt{v_x^2 + v_y^2}}, \qquad
\boxed{\theta = \arctan\left(\frac{v_y}{v_x}\right)}
$$

其中 $\theta$ 为速度与水平方向的夹角。

> **⚠️ 注意事项**：
>
> **1. 反正切的角度范围**
>
> 函数 $\arctan$ 的返回值范围是 $(-90^\circ, 90^\circ)$，仅覆盖第一和第四象限。如果 $v_x < 0$（即速度指向左方），直接计算 $\arctan(v_y/v_x)$ 会得到第二或第三象限的角度，但 $\arctan$ 会返回一个负角（第四象限）。**此时需要加 $180^\circ$（$\pi$ 弧度）来修正**。
>
> 正确的处理方法：
> $$
> \theta = \begin{cases}
> \arctan\left(\dfrac{v_y}{v_x}\right), & v_x > 0 \\[8pt]
> \arctan\left(\dfrac{v_y}{v_x}\right) + 180^\circ, & v_x < 0
> \end{cases}
> $$
>
> 如果 $v_x = 0$，则速度沿垂直方向：
> - $v_y > 0 \implies \theta = 90^\circ$
> - $v_y < 0 \implies \theta = 270^\circ$（或 $-90^\circ$）
>
> 许多计算器有 $\text{atan2}(y, x)$ 函数，它自动处理象限问题，推荐使用。
>
> **2. 分解与合成是互逆运算**
>
> $$
> \boxed{\text{分解：}\quad (v, \theta) \xrightarrow{\text{投影}} (v\cos\theta, v\sin\theta)}
> $$
> $$
> \boxed{\text{合成：}\quad (v_x, v_y) \xrightarrow{\text{勾股定理+反正切}} (v, \theta)}
> $$
>
> 两者互为逆运算，构成了向量分析的基本操作循环。

##### 沿任意方向的分解

虽然水平和垂直分解是最常用的，但在某些问题中，将速度沿**其他互相垂直的方向**分解更方便。

例如，一个物体沿倾角为 $\alpha$ 的斜面运动，速度大小为 $v$，方向沿斜面向上。此时分解为**沿斜面方向**和**垂直于斜面方向**更为自然：

- 沿斜面方向的分量：$v_{\parallel} = v$（全部沿斜面）
- 垂直于斜面的分量：$v_{\perp} = 0$

但如果物体的速度方向与斜面夹角为 $\phi$，则需要将速度向这两个方向投影：

> 设 $x'$ 轴沿斜面向上，$y'$ 轴垂直于斜面向上。速度 $\mathbf{v}$ 与 $x'$ 轴夹角为 $\phi$，则：
> $$
> \mathbf{v} = (v\cos\phi)\,\mathbf{i}' + (v\sin\phi)\,\mathbf{j}'
> $$
> 其中 $\mathbf{i}'$ 是沿斜面方向的单位向量，$\mathbf{j}'$ 是垂直斜面方向的单位向量。

**一般原则**：选择分解方向时，应使尽可能多的分量在后续计算中保持简单（例如，使某个方向上的加速度为零，或使某个方向上的运动为匀速）。

##### 任意方向速度分量的通用公式

更一般地，对于任意方向（与 $x$ 轴夹角为 $\theta$）的速度 $\mathbf{v}$，我们可以将其分解到**任意两个互相垂直的方向**上。

设 $\mathbf{u}$ 是某个方向的单位向量（与 $x$ 轴夹角为 $\alpha$），$\mathbf{u}_\perp$ 是垂直于 $\mathbf{u}$ 的单位向量（与 $x$ 轴夹角为 $\alpha + 90^\circ$）。那么 $\mathbf{v}$ 在 $\mathbf{u}$ 方向上的分量大小为：

$$
v_{\parallel} = \mathbf{v} \cdot \mathbf{u} = |\mathbf{v}| \cos(\theta - \alpha)
$$

在 $\mathbf{u}_\perp$ 方向上的分量大小为：

$$
v_{\perp} = \mathbf{v} \cdot \mathbf{u}_\perp = |\mathbf{v}| \sin(\theta - \alpha)
$$

> **证明**：$\mathbf{v}$ 与 $\mathbf{u}$ 的夹角为 $|\theta - \alpha|$，因此 $\mathbf{v}$ 在 $\mathbf{u}$ 上的投影长度为 $|\mathbf{v}|\cos(\theta - \alpha)$。同理，$\mathbf{v}$ 与 $\mathbf{u}_\perp$ 的夹角为 $|\theta - \alpha - 90^\circ|$，投影长度为 $|\mathbf{v}|\sin(\theta - \alpha)$。

##### 分解的验证——分量合成回去

分解是否正确，可以通过将分量重新合成来验证。任何正确的分解都必须满足：

$$
v_x^2 + v_y^2 = v^2 \quad \text{（模长不变）}
$$

以及方向的一致性。这为我们提供了一种检验分解是否正确的便捷方法。

> **📌 验证示例**：设 $\mathbf{v} = 20\,\text{m/s}$，$\theta = 30^\circ$。
>
> 分解得 $v_x = 20\cos 30^\circ = 10\sqrt{3} \approx 17.32$，$v_y = 20\sin 30^\circ = 10$。
>
> 验证模长：$\sqrt{(10\sqrt{3})^2 + 10^2} = \sqrt{300 + 100} = \sqrt{400} = 20$ ✓
>
> 验证角度：$\tan\theta = \frac{10}{10\sqrt{3}} = \frac{1}{\sqrt{3}} \implies \theta = 30^\circ$ ✓

##### 常见特殊角度的分解速查

| 角度 $\theta$ | $\cos\theta$ | $\sin\theta$ | 水平分量 $v_x$ | 垂直分量 $v_y$ |
|:---:|:---:|:---:|:---:|:---:|
| $0^\circ$ | $1$ | $0$ | $v$ | $0$ |
| $30^\circ$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}v$ | $\dfrac{1}{2}v$ |
| $45^\circ$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}v$ | $\dfrac{\sqrt{2}}{2}v$ |
| $60^\circ$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}v$ | $\dfrac{\sqrt{3}}{2}v$ |
| $90^\circ$ | $0$ | $1$ | $0$ | $v$ |
| $180^\circ$ | $-1$ | $0$ | $-v$ | $0$ |

> **记忆技巧**：
> - 当 $\theta = 0^\circ$（水平向右运动）时，速度全部在水平方向，垂直分量为零
> - 当 $\theta = 90^\circ$（竖直向上运动）时，速度全部在垂直方向，水平分量为零
> - 当 $\theta = 45^\circ$ 时，水平分量等于垂直分量，均为 $\dfrac{v}{\sqrt{2}}$

---

#### 相撞问题（追及相遇问题）

相撞问题是速度合成与分解的一个直接应用。它在现实生活中无处不在：

- **导弹拦截**：拦截弹需要在特定时刻飞到目标位置，才能击中目标
- **空中交通管制**：航管员需要判断两架飞机是否会在空中相撞，并提前调整航线
- **海上搜救**：搜救船需要计算出与遇险船只的相遇时间和位置
- **自动驾驶**：车辆需要预测其他车辆的轨迹，避免碰撞

所有这些问题的核心都是同一个数学问题——判断两个运动物体是否会在**同一时刻到达同一位置**。

##### 1. 核心逻辑——用"GPS定位"来理解

想象你打开手机地图，上面有两个行人的实时位置在移动：

- **物体的位置** $\mathbf{r}(t)$：就是它在地图上的 **"实时坐标"**。这个坐标会随时间 $t$ 变化——$t$ 不同，位置就不同。
- **初始位置** $\mathbf{r}_0$：是它在 **"0 秒时"**（即开始计时的那一刻）的出发坐标。这是整个运动的"起点"。
- **速度向量** $\mathbf{v}$：就是它 **"每秒移动多少米"**，并且指明了移动的方向。速度向量就像 GPS 上的"方向箭头"——箭头的长度是速率，箭头的指向是运动方向。

因此，匀速直线运动的位置公式 $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$ 翻译成人话就是：

> **"现在的坐标 = 出发时的坐标 + 走了多长时间 × 每秒走多少"**

> **🌰 一个具体的例子**：假设一艘船从点 $(2, 1)$ 出发，以速度 $\mathbf{v} = (3, 4)$ 航行。
> - $t = 0$ 秒时：位置是 $(2, 1)$（还没出发）
> - $t = 1$ 秒时：位置是 $(2+3, 1+4) = (5, 5)$（向右走了 3，向上走了 4）
> - $t = 2$ 秒时：位置是 $(2+6, 1+8) = (8, 9)$
> - 一般地：$\mathbf{r}(t) = (2, 1) + (3, 4)t = (2+3t, 1+4t)$
>
> 你看，每过 1 秒，$x$ 坐标增加 3，$y$ 坐标增加 4——速度向量 $(3, 4)$ 就是在告诉我们"每秒怎么走"。

##### 2. 相撞的数学条件——"同时同地"

两个运动物体相撞，说白了就是两个要求：**同一时刻 + 同一位置**。缺一不可。

用数学语言说：存在某个时刻 $t$，使得两个物体的位置向量**相等**。即：

$$
\boxed{\mathbf{r}_1(t) = \mathbf{r}_2(t)}
$$

> **💡 直觉理解**：你在微信上和朋友约见面。
> - "同一位置" = 你们都到了咖啡店
> - "同一时刻" = 你们同时推门进去
> - 如果你下午 2 点到咖啡店，朋友下午 3 点才来——你们确实都到了咖啡店（同一位置），但没碰上（不同时刻）。这不叫"撞见"，这叫"错过"。

对于匀速直线运动，位置向量满足 $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$，因此相撞条件展开为：

$$
\mathbf{r}_{01} + \mathbf{v}_1 t = \mathbf{r}_{02} + \mathbf{v}_2 t
$$

这个方程看起来只是一个式子，但它实际上**同时管着两个方向**——$x$ 方向和 $y$ 方向。这就引出了下一个关键问题。

##### 3. 为什么会有"两个分量方程"？——"两把锁一把钥匙"

你可能觉得奇怪：为什么一个等式 $\mathbf{r}_1(t) = \mathbf{r}_2(t)$ 会变成两个方程？

这是因为位置向量 $\mathbf{r}$ 是一个 **二维坐标** $(x, y)$。两个向量相等，意味着它们的**每个分量都必须对应相等**——这就像两把锁需要同一把钥匙同时打开：

$$
\begin{pmatrix} x_1(t) \\ y_1(t) \end{pmatrix} = \begin{pmatrix} x_2(t) \\ y_2(t) \end{pmatrix}
\quad\Longleftrightarrow\quad
\begin{cases}
x_1(t) = x_2(t) \\[4pt]
y_1(t) = y_2(t)
\end{cases}
$$

这背后的底层逻辑其实就是**速度分解**——把"斜着跑"的运动拆成"水平跑"和"竖直跑"，然后分别判断两个物体是否能在同一时刻到达同一 $x$ 坐标和同一 $y$ 坐标：

$$
\begin{cases}
x\text{方向：} & x_{01} + v_{1x}\,t = x_{02} + v_{2x}\,t \\[4pt]
y\text{方向：} & y_{01} + v_{1y}\,t = y_{02} + v_{2y}\,t
\end{cases}
$$

> **🎯 几何直观**：
> - **第一个方程（$x$ 方向）**：两个物体在水平方向上的投影——它们是否会在同一时刻经过同一竖直线？
> - **第二个方程（$y$ 方向）**：两个物体在竖直方向上的投影——它们是否会在同一时刻经过同一水平线？
>
> 只有**同时**满足这两个条件，两个物体才会在**同一时刻到达平面上的同一点**。
>
> 这就好比两个人要在三维空间中的某一点握手——他们的 $x$ 坐标要在同一时间相等 **且** $y$ 坐标也要在同一时间相等。两个条件就像两把独立的锁，必须用同一把钥匙（同一个 $t$）同时打开。

**用生活的例子来想：**

假设你和朋友约在某个路口见面。路口有确定的 $x$ 坐标和 $y$ 坐标。

- 如果你在 $t=2$ 分钟时走到了那个 $x$ 坐标，但朋友在 $t=5$ 分钟时才走到那个 $x$ 坐标——你们在 $x$ 方向上错过了
- 就算你们同时走到了同一个 $x$，但如果 $y$ 方向上差了 10 米——你们还是没碰上
- **只有 $x$ 和 $y$ 都在同一时刻对齐了，才算真正撞上了**

##### 4. 考场三步走（不跳步完整版）

**第一步：拆速度**

如果题目给的是速度的大小 $v$ 和方向角 $\theta$，先用速度分解求出分量：

$$
v_x = v\cos\theta, \qquad v_y = v\sin\theta
$$

如果题目直接给坐标形式（如 $\mathbf{v} = 3\mathbf{i} + 4\mathbf{j}$），则 $v_x = 3$，$v_y = 4$。

**第二步：写出两个"时间方程"**

设物体 1 的初始坐标为 $(x_1, y_1)$，速度分量为 $(u_x, u_y)$；
物体 2 的初始坐标为 $(x_2, y_2)$，速度分量为 $(v_x, v_y)$。

$$
\begin{cases}
x_1 + u_x \cdot t = x_2 + v_x \cdot t \quad &\text{（水平方程）} \\[4pt]
y_1 + u_y \cdot t = y_2 + v_y \cdot t \quad &\text{（竖直方程）}
\end{cases}
$$

分别解出 $t_1$（来自水平方程）和 $t_2$（来自竖直方程）。

**第三步：判定结果**

$$
\boxed{\text{相撞} \iff t_1 = t_2 \geq 0}
$$

- 如果 $t_1 = t_2$ 且 $\geq 0$：**相撞**！它们在水平方向和竖直方向同时重合。
- 如果 $t_1 \neq t_2$：**不相撞**。即使它们经过了同一个坐标点，也是**一前一后**错过的——这叫"路过"（相遇），不叫"相撞"。

> **🔑 关键区分**："相撞"要求同时在同一位置。如果两船在不同时间到达同一点，那只叫"相遇"而非"相撞"。

##### 5. ⚠️ 最容易丢分的"送命题"陷阱

考试中，如果解出 $t_1 \neq t_2$，**千万别直接写"不相撞"就收工！** 出题人在这里埋了三个常见坑，每一个都能让你丢掉整道题的分数：

---

**坑 1：追问最短距离**

如果两个物体不相撞，接下来 99% 的几率会问：**"求它们之间的最短距离"**。

为什么不相撞还要算距离？因为出题人想考你：**虽然它们永远不会碰到，但它们在运动过程中会有一个"最近的时候"**——就像两艘船在海上交错而过，最近的时候可能只差几米。

此时需要用勾股定理写出距离函数：

$$
d(t) = \sqrt{[x_1(t) - x_2(t)]^2 + [y_1(t) - y_2(t)]^2}
$$

这个 $d(t)$ 是两物体在时刻 $t$ 的**直线距离**。然后求这个函数的最小值：

- **方法一（配方法）**：如果 $d^2(t)$ 是 $t$ 的二次函数，可以用配方法求最小值（适用于第 3 章学过的二次函数）
- **方法二（求导法）**：对 $d(t)$ 或 $d^2(t)$ 求导，令导数为零（将在第 5 章微分中系统学习）

> **💡 注意**：距离是**横坐标差的平方 + 纵坐标差的平方 再开根号**——**绝对不要直接把横纵距离加起来！** 这是勾股定理的基本要求，但考场上紧张时最容易犯这个低级错误。

> **🔑 小技巧**：求 $d(t)$ 的最小值，其实等价于求 $[d(t)]^2$ 的最小值（因为平方函数是单调递增的，最小值点相同）。而 $[d(t)]^2$ 没有根号，求导或配方都更方便。

---

**坑 2：速度分解时忘用 $\sin$ 和 $\cos$**

这是新手最常犯的错误，没有之一！

如果题目给的是速度的大小 $v$ 和方向角 $\theta$（比如 "$10\,\text{m/s}$，与水平方向成 $30^\circ$"），你必须先用 $\sin$、$\cos$ 拆成 $x$ 和 $y$ 分量：

$$
v_x = v\cos\theta, \qquad v_y = v\sin\theta
$$

**直接拿 $\theta$ 或者 $v$ 去代入方程**是完全错误的！

> **❌ 典型错误**：
> - 把 $\theta$ 当成速度：$x_1 + \theta \cdot t = x_2 + \dots$ ❌
> - 直接用 $v$ 而不分解：$x_1 + v \cdot t = x_2 + \dots$ ❌（这是把速度当成纯水平方向了）
>
> **✅ 正确做法**：
> - 先写出 $\mathbf{v} = (v\cos\theta)\mathbf{i} + (v\sin\theta)\mathbf{j}$
> - 然后 $v_x = v\cos\theta$，$v_y = v\sin\theta$
> - 最后代入两个分量方程

**记住**：速度分解是解决一切向量运动问题的第一步——就像穿衣服先系第一颗扣子，第一颗歪了后面全歪。

---

**坑 3：$t$ 为负数的情况**

解出的 $t$ 如果为负，说明它们在**出发之前**曾经在同一位置——这就像说"你们昨天在那个路口碰见过"，但问题问的是"今天出发后会不会相撞"，昨天的相遇不算数！

必须要求 $t \geq 0$ 才算是未来的相撞。

> **完整判定逻辑**：
> $$
> \text{相撞} \iff t_1 = t_2 \;\text{且}\; t_1 \geq 0
> $$
>
> - $t_1 = t_2 < 0$：它们在出发**前**就在一起（比如停在同一个起点），但这不叫未来的相撞
> - $t_1 = t_2 = 0$：它们在起点就重合了（一开始就撞上了），这算相撞
> - $t_1 = t_2 > 0$：标准相撞情况
> - $t_1 \neq t_2$：无论正负，都不相撞

---

### 📌 例题 2.3：速度合成与相撞问题

**例题 1**（速度合成——船与水流）

一艘船在静水中的速度是 $6\,\text{m/s}$ 向东。水流以 $4\,\text{m/s}$ 的速度向北流动。求船相对于地面的速度的大小和方向。

**思路分析**：
- 船相对于水的速度 $\mathbf{v}_{B/W}$ = 向东 $6$ m/s
- 水相对于地面的速度 $\mathbf{v}_{W/G}$ = 向北 $4$ m/s
- 船相对于地面的速度 $\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G}$

**解**：

设正东方向为 $+x$ 轴，正北方向为 $+y$ 轴。

船相对于水的速度：$\mathbf{v}_{B/W} = 6\mathbf{i}$
水流相对于地面的速度：$\mathbf{v}_{W/G} = 4\mathbf{j}$

由速度合成公式：

$$
\mathbf{v}_{B/G} = \mathbf{v}_{B/W} + \mathbf{v}_{W/G} = 6\mathbf{i} + 4\mathbf{j}
$$

合速度的大小（速率）：

$$
|\mathbf{v}_{B/G}| = \sqrt{6^2 + 4^2} = \sqrt{36 + 16} = \sqrt{52} = 2\sqrt{13} \approx 7.21\,\text{m/s}
$$

合速度的方向：设 $\theta$ 为与正东方向的夹角（逆时针为正）。

$$
\tan\theta = \frac{4}{6} = \frac{2}{3} \implies \theta = \arctan\left(\frac{2}{3}\right) \approx 33.69^\circ
$$

因此船相对于地面的速度大小为 $2\sqrt{13}\,\text{m/s}$，方向为北偏东 $33.69^\circ$（即从正东方向逆时针旋转 $33.69^\circ$）。

> **生活实例**：这就是为什么船过河时，如果直接朝对岸开，会被水流冲偏。要想直接到达正对岸，船头必须朝上游方向倾斜。

---

**例题 2**（速度分解——斜抛的初速度）

一个球以初速度 $20\,\text{m/s}$、与水平方向成 $30^\circ$ 角斜向上抛出。

（a）求初速度的水平分量和垂直分量。
（b）写出初速度的向量形式。

**思路分析**：
- 速度的大小是 $20$，方向是 $30^\circ$ 仰角
- 水平分量 $v_x = v\cos\theta$，垂直分量 $v_y = v\sin\theta$

**解**：

（a）设水平向右为 $+x$ 轴，竖直向上为 $+y$ 轴。

水平分量：

$$
v_x = v\cos\theta = 20 \times \cos 30^\circ = 20 \times \frac{\sqrt{3}}{2} = 10\sqrt{3} \approx 17.32\,\text{m/s}
$$

垂直分量：

$$
v_y = v\sin\theta = 20 \times \sin 30^\circ = 20 \times \frac{1}{2} = 10\,\text{m/s}
$$

（b）初速度的向量形式：

$$
\mathbf{v}_0 = 10\sqrt{3}\,\mathbf{i} + 10\,\mathbf{j}\,\text{m/s}
$$

> **物理意义**：
> - 如果没有空气阻力，水平分量 $v_x$ 在整个运动过程中保持不变（因为水平方向不受力）
> - 而垂直分量 $v_y$ 受重力影响以 $-g$ 的加速度变化（$g \approx 9.8\,\text{m/s}^2$）
> - 所以任意时刻的速度为 $\mathbf{v}(t) = 10\sqrt{3}\,\mathbf{i} + (10 - gt)\,\mathbf{j}$
> - 这为第 10 章的运动学问题奠定了基础

---

**例题 3**（相撞问题——两船是否会相撞）

船 $P$ 从点 $(0, 0)$ 出发，以速度 $\mathbf{v}_P = (3\mathbf{i} + 4\mathbf{j})\,\text{km/h}$ 航行。船 $Q$ 从点 $(10, 5)\,\text{km}$ 出发，以速度 $\mathbf{v}_Q = (-2\mathbf{i} + \mathbf{j})\,\text{km/h}$ 航行。两船同时出发，判断它们是否会相撞。

**思路分析**：
1. 写出两船的位置向量（都是 $\mathbf{r}_0 + \mathbf{v}t$ 的形式）
2. 令 $\mathbf{r}_P(t) = \mathbf{r}_Q(t)$
3. 得到两个分量方程，分别解 $t$
4. 如果 $t$ 值一致且 $\geq 0$，相撞；否则不相撞

**解**：

设 $t$ 为出发后的时间（小时）。

$P$ 的位置向量（从原点出发）：

$$
\mathbf{r}_P(t) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 3 \\ 4 \end{pmatrix} t = \begin{pmatrix} 3t \\ 4t \end{pmatrix}
$$

$Q$ 的位置向量（从 $(10,5)$ 出发）：

$$
\mathbf{r}_Q(t) = \begin{pmatrix} 10 \\ 5 \end{pmatrix} + \begin{pmatrix} -2 \\ 1 \end{pmatrix} t = \begin{pmatrix} 10 - 2t \\ 5 + t \end{pmatrix}
$$

如果两船相撞，则存在某个 $t \geq 0$ 使得 $\mathbf{r}_P(t) = \mathbf{r}_Q(t)$，即：

$$
\begin{pmatrix} 3t \\ 4t \end{pmatrix} = \begin{pmatrix} 10 - 2t \\ 5 + t \end{pmatrix}
$$

这给出两个分量方程：

$$
\begin{cases}
x\text{分量：} & 3t = 10 - 2t \implies 5t = 10 \implies t = 2 \\[4pt]
y\text{分量：} & 4t = 5 + t \implies 3t = 5 \implies t = \dfrac{5}{3}
\end{cases}
$$

两个 $t$ 值不相等（$2 \neq \frac{5}{3}$），因此不存在同时满足两个分量方程的时刻。两船不会相撞。

> **为什么不相撞？** 即使 $x$ 坐标在 $t=2$ 时相等，$y$ 坐标在 $t=2$ 时分别为 $4\times 2 = 8$ 和 $5+2=7$，不相等。所以两船永远不会在同一时刻到达同一点。

---

## 2.3 变化率入门（微积分铺垫）

### 2.3.1 为何研究变化率？

在物理世界中，很少有事物是静止的。一辆行驶的汽车，它的位置在变化；一个充气的气球，它的体积在变化；一个加热的金属棒，它的温度在变化。**变化率**就是描述"一个量随另一个量变化得有多快"的数学工具。

在 2.1 和 2.2 节中，我们用向量描述了位置、速度和加速度。现在我们要问一个更深入的问题：**如何精确地定义"瞬时"变化率？**

---

### 2.3.2 从平均变化率到瞬时变化率

让我们从一个具体的运动学例子开始。

一个质点沿直线运动，它的位移 $s$（单位：米）与时间 $t$（单位：秒）的关系为：

$$
s(t) = t^2
$$

我们想知道 $t = 1$ 秒这一**瞬间**的速度。

#### 第一步：平均速度

如果取一个时间区间 $[1, 1 + \Delta t]$，质点在区间内的平均速度是：

$$
\text{平均速度} = \frac{s(1 + \Delta t) - s(1)}{\Delta t}
$$

代入 $s(t) = t^2$：

$$
\frac{(1 + \Delta t)^2 - 1^2}{\Delta t} = \frac{1 + 2\Delta t + (\Delta t)^2 - 1}{\Delta t} = \frac{2\Delta t + (\Delta t)^2}{\Delta t} = 2 + \Delta t
$$

#### 第二步：让 $\Delta t$ 越来越小

我们让 $\Delta t$ 逐渐趋近于 0，观察平均速度的变化：

| $\Delta t$（秒） | 平均速度（m/s） |
|:---:|:---:|
| 0.1 | $2 + 0.1 = 2.1$ |
| 0.01 | $2 + 0.01 = 2.01$ |
| 0.001 | $2 + 0.001 = 2.001$ |
| 0.0001 | $2 + 0.0001 = 2.0001$ |
| $\to 0$ | $\to 2$ |

随着 $\Delta t$ 越来越接近 0，平均速度越来越接近 **2**。

#### 第三步：极限

当 $\Delta t$ 趋近于 0 时，平均速度 $2 + \Delta t$ 趋近于 2。我们记：

$$
v(1) = \lim_{\Delta t \to 0} \frac{s(1 + \Delta t) - s(1)}{\Delta t} = \lim_{\Delta t \to 0} (2 + \Delta t) = 2
$$

这个极限值就是质点在 $t = 1$ 时的**瞬时速度**。

> **重要理解**：我们从不令 $\Delta t = 0$（那样会得到 $0/0$，没有意义）。我们让 $\Delta t$ 无限趋近于 0，观察比值趋近于哪个固定值。这个"趋近的目标"就是导数。
>
> 用极限的语言说：**当 $\Delta t$ 趋近于 0 时，平均速度的极限就是瞬时速度。**

---

### 2.3.3 导数的一般定义

一般地，对于函数 $y = f(x)$，它在 $x = a$ 处的**导数**（即瞬时变化率）定义为：

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

其中 $h$ 就是前面例子中的 $\Delta x$ 或 $\Delta t$。

如果这个极限存在，我们就说 $f$ 在 $x = a$ 处**可导**。

**导数的记号**：
- 莱布尼茨记号：$\dfrac{dy}{dx}$ 或 $\dfrac{d}{dx}f(x)$
- 拉格朗日记号：$f'(x)$
- 牛顿记号（常用于物理）：$\dot{y}$

> 在考纲 14.1 中，只要求对极限有直观理解，不要求从第一原理求导。但我们这里仍会展示几个基本推导，帮助你建立直觉。

---

### 2.3.4 用定义求导——基础推导

让我们用极限定义推导几个基本函数的导数。

#### 推导 1：$f(x) = x^2$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} \\
&= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h} \\
&= \lim_{h \to 0} \frac{2xh + h^2}{h} \\
&= \lim_{h \to 0} (2x + h) \\
&= 2x
\end{aligned}
$$

因此 $\dfrac{d}{dx}(x^2) = 2x$。

**几何意义**：函数 $y = x^2$ 在任意点 $x$ 处的切线斜率为 $2x$。在 $x = 1$ 处斜率为 $2$，在 $x = 3$ 处斜率为 $6$。

#### 推导 2：$f(x) = x^3$

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{(x + h)^3 - x^3}{h}
\end{aligned}
$$

展开 $(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$：

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{x^3 + 3x^2h + 3xh^2 + h^3 - x^3}{h} \\
&= \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3}{h} \\
&= \lim_{h \to 0} (3x^2 + 3xh + h^2) \\
&= 3x^2
\end{aligned}
$$

因此 $\dfrac{d}{dx}(x^3) = 3x^2$。

#### 推导 3：$f(x) = \dfrac{1}{x}$（$x \neq 0$）

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{\frac{1}{x + h} - \frac{1}{x}}{h}
\end{aligned}
$$

先通分分子：

$$
\frac{1}{x + h} - \frac{1}{x} = \frac{x - (x + h)}{x(x + h)} = \frac{-h}{x(x + h)}
$$

所以：

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{-h}{x(x + h)} \cdot \frac{1}{h} \\
&= \lim_{h \to 0} \frac{-1}{x(x + h)} \\
&= -\frac{1}{x^2}
\end{aligned}
$$

因此 $\dfrac{d}{dx}\left(\dfrac{1}{x}\right) = -\dfrac{1}{x^2}$。

---

### 2.3.5 幂法则

从上面的推导中，我们可以观察出一个模式：

| $f(x)$ | $f'(x)$ |
|:---:|:---:|
| $x^2$ | $2x$ |
| $x^3$ | $3x^2$ |
| $x^1$ | $1$（即 $1 \cdot x^0$） |
| $\dfrac{1}{x} = x^{-1}$ | $-\dfrac{1}{x^2} = -x^{-2}$ |

这个模式就是**幂法则**：对任意实数 $n$，

$$
\boxed{\frac{d}{dx}(x^n) = n x^{n-1}}
$$

> **幂法则的完整推导**（利用二项式定理，仅对正整数 $n$）：
>
> 考虑 $f(x) = x^n$，其中 $n$ 为正整数。利用二项式定理展开 $(x + h)^n$：
> $$
> (x + h)^n = x^n + n x^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \binom{n}{3}x^{n-3}h^3 + \dots + h^n
> $$
> 因此：
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{x^n + n x^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \dots + h^n - x^n}{h} \\
> &= \lim_{h \to 0} \left( n x^{n-1} + \binom{n}{2}x^{n-2}h + \binom{n}{3}x^{n-3}h^2 + \dots + h^{n-1} \right) \\
> &= n x^{n-1}
> \end{aligned}
> $$
> 因为所有含 $h$ 的项在 $h \to 0$ 时都趋于 0。

---

### 2.3.6 变化率在向量中的应用：运动学

现在回到向量的语境中。如果质点的位置向量 $\mathbf{r}(t)$ 随时间变化，那么它的速度向量和加速度向量就是位置向量对时间的变化率。

设 $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$，则：

$$
\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j}
$$

$$
\mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d^2\mathbf{r}}{dt^2} = \frac{d^2x}{dt^2}\mathbf{i} + \frac{d^2y}{dt^2}\mathbf{j}
$$

也就是说，对向量函数求导，就是对它的各个分量分别求导。

---

### 2.3.7 从加速度到速度和位置（积分铺垫）

在物理中，加速度 $\mathbf{a}(t)$ 是速度 $\mathbf{v}(t)$ 的变化率。如果我们知道加速度并想恢复出速度，需要做微分的逆运算——这称为**积分**（将在第 7 章详细学习）。

基本关系是：

- 速度 $\mathbf{v}(t) = \int \mathbf{a}(t) \, dt + \mathbf{v}_0$（其中 $\mathbf{v}_0$ 是初始速度）
- 位置 $\mathbf{r}(t) = \int \mathbf{v}(t) \, dt + \mathbf{r}_0$（其中 $\mathbf{r}_0$ 是初始位置）

或者用定积分的形式（更适合已知确定时间段的问题）：

$$
\mathbf{v}(t) = \mathbf{v}_0 + \int_0^t \mathbf{a}(u) \, du,
\quad
\mathbf{r}(t) = \mathbf{r}_0 + \int_0^t \mathbf{v}(u) \, du
$$

这里先建立直观理解：**微分**是求变化率（位置 → 速度 → 加速度），**积分**是求累积量（加速度 → 速度 → 位置），两者互为逆运算。

---

### 📌 例题 2.4：变化率入门

**例题 1**（用极限定义求瞬时速度）

一个质点的位移（单位：米）与时间（单位：秒）的关系为 $s(t) = 3t^2 - 2t + 1$。

（a）求从 $t = 2$ 到 $t = 2 + h$ 的平均速度。
（b）利用极限求 $t = 2$ 时的瞬时速度。

**思路分析**：
- 平均速度 = $\dfrac{s(2+h) - s(2)}{h}$
- 瞬时速度 = $\displaystyle\lim_{h \to 0}$ 平均速度

**解**：

（a）

$$
\begin{aligned}
\text{平均速度} &= \frac{s(2 + h) - s(2)}{h} \\
&= \frac{[3(2+h)^2 - 2(2+h) + 1] - [3(4) - 4 + 1]}{h} \\
&= \frac{[3(4 + 4h + h^2) - 4 - 2h + 1] - [12 - 4 + 1]}{h} \\
&= \frac{[12 + 12h + 3h^2 - 4 - 2h + 1] - 9}{h} \\
&= \frac{[9 + 10h + 3h^2] - 9}{h} \\
&= \frac{10h + 3h^2}{h} = 10 + 3h
\end{aligned}
$$

（b）瞬时速度是 $h \to 0$ 时平均速度的极限：

$$
v(2) = \lim_{h \to 0} (10 + 3h) = 10\,\text{m/s}
$$

因此质点在 $t = 2$ 秒时的瞬时速度为 $10\,\text{m/s}$。

> **验证**：用幂法则直接求导：$s'(t) = 6t - 2$，$s'(2) = 12 - 2 = 10$，一致。✓

---

**例题 2**（用极限定义求一般导数 + 幂法则验证）

用导数的极限定义求 $f(x) = 4x - x^2$ 的导数 $f'(x)$。

**解**：

$$
\begin{aligned}
f'(x) &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{[4(x + h) - (x + h)^2] - [4x - x^2]}{h} \\
&= \lim_{h \to 0} \frac{4x + 4h - (x^2 + 2xh + h^2) - 4x + x^2}{h} \\
&= \lim_{h \to 0} \frac{4h - 2xh - h^2}{h} \\
&= \lim_{h \to 0} (4 - 2x - h) \\
&= 4 - 2x
\end{aligned}
$$

因此 $f'(x) = 4 - 2x$。

**验证**：使用幂法则对 $f(x) = 4x - x^2$ 逐项求导：
- $\dfrac{d}{dx}(4x) = 4 \cdot 1 \cdot x^{0} = 4$
- $\dfrac{d}{dx}(-x^2) = -2x^{1} = -2x$
- 相加得 $f'(x) = 4 - 2x$，与极限结果一致。✓

---

**例题 3**（向量的变化率 + 积分逆运算）

一个质点在平面内运动，它的位置向量为：

$$
\mathbf{r}(t) = (t^3 - 3t)\mathbf{i} + (t^2 - 2t)\mathbf{j}
$$

其中 $t$ 以秒为单位，位置以米为单位。

（a）求速度向量 $\mathbf{v}(t)$。
（b）求加速度向量 $\mathbf{a}(t)$。
（c）求 $t = 2$ 秒时的速度和加速度向量。
（d）已知该质点的加速度恒为 $\mathbf{a}(t) = 6t\mathbf{i} + 2\mathbf{j}$，初速度 $\mathbf{v}_0 = -3\mathbf{i} - 2\mathbf{j}$，初始位置 $\mathbf{r}_0 = \mathbf{0}$。用积分求 $\mathbf{v}(t)$ 和 $\mathbf{r}(t)$，验证与（a）（b）一致。

**思路分析**：
- 速度 = 位置的导数（分量分别求导）
- 加速度 = 速度的导数（分量分别求导）
- 积分是微分的逆运算：已知加速度，积分一次得速度（加常数），再积分一次得位置（加常数）
- 常数由初始条件确定

**解**：

（a）速度是位置对时间的导数，对各分量分别求导：

$$
\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{d}{dt}(t^3 - 3t)\,\mathbf{i} + \frac{d}{dt}(t^2 - 2t)\,\mathbf{j}
$$

使用幂法则：
- $\dfrac{d}{dt}(t^3) = 3t^2$
- $\dfrac{d}{dt}(-3t) = -3$
- $\dfrac{d}{dt}(t^2) = 2t$
- $\dfrac{d}{dt}(-2t) = -2$

因此：

$$
\mathbf{v}(t) = (3t^2 - 3)\mathbf{i} + (2t - 2)\mathbf{j}
$$

（b）加速度是速度对时间的导数：

$$
\mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}(3t^2 - 3)\,\mathbf{i} + \frac{d}{dt}(2t - 2)\,\mathbf{j}
$$

$$
\mathbf{a}(t) = (6t)\mathbf{i} + 2\mathbf{j}
$$

（c）代入 $t = 2$：

$$
\mathbf{v}(2) = (3 \times 4 - 3)\mathbf{i} + (4 - 2)\mathbf{j} = 9\mathbf{i} + 2\mathbf{j}\,\text{m/s}
$$

速度的大小：$|\mathbf{v}(2)| = \sqrt{9^2 + 2^2} = \sqrt{81 + 4} = \sqrt{85} \approx 9.22\,\text{m/s}$

$$
\mathbf{a}(2) = (6 \times 2)\mathbf{i} + 2\mathbf{j} = 12\mathbf{i} + 2\mathbf{j}\,\text{m/s}^2
$$

加速度的大小：$|\mathbf{a}(2)| = \sqrt{12^2 + 2^2} = \sqrt{144 + 4} = \sqrt{148} = 2\sqrt{37} \approx 12.17\,\text{m/s}^2$

（d）已知 $\mathbf{a}(t) = (6t)\mathbf{i} + 2\mathbf{j}$，对加速度积分求速度：

$$
\mathbf{v}(t) = \int \mathbf{a}(t) \, dt = \left(\int 6t \, dt\right)\mathbf{i} + \left(\int 2 \, dt\right)\mathbf{j}
$$

$$
= (3t^2 + C_1)\mathbf{i} + (2t + C_2)\mathbf{j}
$$

由 $\mathbf{v}_0 = \mathbf{v}(0) = -3\mathbf{i} - 2\mathbf{j}$，代入 $t = 0$ 得 $C_1 = -3$，$C_2 = -2$。所以：

$$
\mathbf{v}(t) = (3t^2 - 3)\mathbf{i} + (2t - 2)\mathbf{j}
$$

与（a）一致。✓

再对速度积分求位置：

$$
\mathbf{r}(t) = \int \mathbf{v}(t) \, dt = \left(\int (3t^2 - 3) \, dt\right)\mathbf{i} + \left(\int (2t - 2) \, dt\right)\mathbf{j}
$$

$$
= (t^3 - 3t + D_1)\mathbf{i} + (t^2 - 2t + D_2)\mathbf{j}
$$

由 $\mathbf{r}_0 = \mathbf{r}(0) = \mathbf{0}$，代入 $t = 0$ 得 $D_1 = 0$，$D_2 = 0$。所以：

$$
\mathbf{r}(t) = (t^3 - 3t)\mathbf{i} + (t^2 - 2t)\mathbf{j}
$$

与原始位置函数一致。✓

---

## 2.4 本章练习题

以下练习题按考试难度编写，涵盖本章所有知识点，题号前面标注了对应的考纲编号。

---

**13.1–13.3 题组：向量基础与几何**

**1.** 已知 $\mathbf{a} = 2\mathbf{i} - \mathbf{j}$，$\mathbf{b} = \mathbf{i} + 3\mathbf{j}$。

（a）求 $\mathbf{a} + 2\mathbf{b}$。
（b）求 $|2\mathbf{a} - \mathbf{b}|$。
（c）求与 $3\mathbf{a} + \mathbf{b}$ 同方向的单位向量。

---

**2.** 在 $\triangle ABC$ 中，$P$ 是 $BC$ 的中点，$Q$ 是 $CA$ 的中点。设 $\overrightarrow{AB} = \mathbf{p}$，$\overrightarrow{AC} = \mathbf{q}$。

（a）用 $\mathbf{p}$ 和 $\mathbf{q}$ 表示 $\overrightarrow{BC}$。
（b）用 $\mathbf{p}$ 和 $\mathbf{q}$ 表示 $\overrightarrow{PQ}$。
（c）证明 $PQ \parallel AB$ 且 $PQ = \frac{1}{2} AB$。

---

**3.** 三点 $A$、$B$、$C$ 的位置向量分别为 $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j}$，$\mathbf{b} = 5\mathbf{i} + 6\mathbf{j}$，$\mathbf{c} = 9\mathbf{i} + 14\mathbf{j}$。

（a）证明 $A$、$B$、$C$ 三点共线。
（b）求 $AB:BC$ 的比值。

---

**13.3–13.4 题组：向量几何与运动**

**4.** 在 $\triangle OAB$ 中，$P$ 在 $OA$ 上且 $OP:PA = 1:2$，$Q$ 在 $AB$ 上且 $AQ:QB = 2:3$。设 $\overrightarrow{OA} = \mathbf{a}$，$\overrightarrow{OB} = \mathbf{b}$。

（a）用 $\mathbf{a}$ 和 $\mathbf{b}$ 表示 $\overrightarrow{OP}$。
（b）用 $\mathbf{a}$ 和 $\mathbf{b}$ 表示 $\overrightarrow{OQ}$。
（c）用 $\mathbf{a}$ 和 $\mathbf{b}$ 表示 $\overrightarrow{PQ}$。

---

**5.** 船 $A$ 从点 $(0, 5)$ 出发，以速度 $\mathbf{v}_A = (2\mathbf{i} + 3\mathbf{j})\,\text{km/h}$ 航行。船 $B$ 从点 $(10, 0)$ 出发，以速度 $\mathbf{v}_B = (-3\mathbf{i} + 4\mathbf{j})\,\text{km/h}$ 航行。两船同时出发。

（a）写出两船的位置向量 $\mathbf{r}_A(t)$ 和 $\mathbf{r}_B(t)$。
（b）判断两船是否会相撞。

---

**6.** 一艘船在静水中的速度为 $10\,\text{m/s}$，船头指向正北方向。水流的速度为 $6\,\text{m/s}$ 流向正东方向。

（a）求船相对于地面的合速度向量。
（b）求合速度的大小和方向（与正北方向的夹角）。

---

**14.1 题组：变化率入门**

**7.** 一个质点的位移 $s$（米）与时间 $t$（秒）的关系为 $s(t) = 4t^2 + 3t$。

（a）求从 $t = 1$ 到 $t = 1 + h$ 的平均速度。
（b）利用极限求 $t = 1$ 时的瞬时速度。

---

**8.** 一个质点在平面内运动，它的位置向量为：

$$
\mathbf{r}(t) = (2t^2 + t)\mathbf{i} + (3t - 1)\mathbf{j}
$$

（a）求速度向量 $\mathbf{v}(t)$。
（b）求加速度向量 $\mathbf{a}(t)$。
（c）求 $t = 2$ 时速度的大小。

---

**综合题**

**9.** 在平行四边形 $ABCD$ 中，$A$、$B$、$C$ 的位置向量分别为 $\mathbf{a} = 2\mathbf{i} + \mathbf{j}$，$\mathbf{b} = 5\mathbf{i} + 3\mathbf{j}$，$\mathbf{c} = 4\mathbf{i} + 6\mathbf{j}$。

（a）求 $D$ 的位置向量。
（b）判断 $\overrightarrow{AB}$ 与 $\overrightarrow{AD}$ 是否垂直。
（c）求平行四边形 $ABCD$ 的面积。

> 提示：平行四边形的面积 $= |\overrightarrow{AB}| \times |\overrightarrow{AD}| \times \sin\theta$，其中 $\theta$ 是两边的夹角。或者用行列式公式：面积 $= |x_1 y_2 - x_2 y_1|$，其中 $\overrightarrow{AB} = (x_1, y_1)$，$\overrightarrow{AD} = (x_2, y_2)$。

---

## 练习题答案

**1.**

（a）$\mathbf{a} + 2\mathbf{b} = (2\mathbf{i} - \mathbf{j}) + 2(\mathbf{i} + 3\mathbf{j}) = (2\mathbf{i} - \mathbf{j}) + (2\mathbf{i} + 6\mathbf{j}) = 4\mathbf{i} + 5\mathbf{j}$

（b）$2\mathbf{a} - \mathbf{b} = 2(2\mathbf{i} - \mathbf{j}) - (\mathbf{i} + 3\mathbf{j}) = (4\mathbf{i} - 2\mathbf{j}) - (\mathbf{i} + 3\mathbf{j}) = 3\mathbf{i} - 5\mathbf{j}$

$|2\mathbf{a} - \mathbf{b}| = \sqrt{3^2 + (-5)^2} = \sqrt{9 + 25} = \sqrt{34}$

（c）$3\mathbf{a} + \mathbf{b} = 3(2\mathbf{i} - \mathbf{j}) + (\mathbf{i} + 3\mathbf{j}) = (6\mathbf{i} - 3\mathbf{j}) + (\mathbf{i} + 3\mathbf{j}) = 7\mathbf{i}$

$|7\mathbf{i}| = 7$，所以单位向量 $= \frac{7\mathbf{i}}{7} = \mathbf{i}$

---

**2.**

（a）$\overrightarrow{BC} = \overrightarrow{BA} + \overrightarrow{AC} = -\overrightarrow{AB} + \overrightarrow{AC} = -\mathbf{p} + \mathbf{q}$

（b）$P$ 是 $BC$ 的中点，所以 $\mathbf{r}_P = \frac{\mathbf{r}_B + \mathbf{r}_C}{2}$。$Q$ 是 $CA$ 的中点，所以 $\mathbf{r}_Q = \frac{\mathbf{r}_C + \mathbf{r}_A}{2}$。

$$
\begin{aligned}
\overrightarrow{PQ} &= \mathbf{r}_Q - \mathbf{r}_P \\
&= \frac{\mathbf{r}_C + \mathbf{r}_A}{2} - \frac{\mathbf{r}_B + \mathbf{r}_C}{2} \\
&= \frac{\mathbf{r}_A - \mathbf{r}_B}{2} \\
&= \frac{1}{2}\overrightarrow{BA} = -\frac{1}{2}\overrightarrow{AB} = -\frac{1}{2}\mathbf{p}
\end{aligned}
$$

（c）由（b）得 $\overrightarrow{PQ} = -\frac{1}{2}\mathbf{p} = -\frac{1}{2}\overrightarrow{AB}$，所以 $\overrightarrow{PQ} \parallel \overrightarrow{AB}$ 且 $|\overrightarrow{PQ}| = \frac{1}{2}|\overrightarrow{AB}|$，即 $PQ = \frac{1}{2}AB$。✓

> 这条性质叫做**三角形中位线定理**：三角形两边中点的连线平行于第三边且等于第三边的一半。

---

**3.**

（a）

$$
\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 6\mathbf{j}) - (3\mathbf{i} + 2\mathbf{j}) = 2\mathbf{i} + 4\mathbf{j}
$$

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (9\mathbf{i} + 14\mathbf{j}) - (5\mathbf{i} + 6\mathbf{j}) = 4\mathbf{i} + 8\mathbf{j}
$$

$\overrightarrow{BC} = 2(2\mathbf{i} + 4\mathbf{j}) = 2\overrightarrow{AB}$，存在 $k = 2$ 使得 $\overrightarrow{BC} = k\overrightarrow{AB}$，所以 $A$、$B$、$C$ 共线。

（b）$|\overrightarrow{AB}| = \sqrt{2^2 + 4^2} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$

$|\overrightarrow{BC}| = \sqrt{4^2 + 8^2} = \sqrt{16 + 64} = \sqrt{80} = 4\sqrt{5}$

所以 $AB:BC = 2\sqrt{5}:4\sqrt{5} = 1:2$

---

**4.**

（a）$OP:PA = 1:2$，所以 $OP:OA = 1:3$，即 $\overrightarrow{OP} = \frac{1}{3}\mathbf{a}$

（b）$AQ:QB = 2:3$，所以 $AQ:AB = 2:5$，$Q$ 从 $A$ 到 $B$ 的 $\frac{2}{5}$ 处。

$$
\begin{aligned}
\overrightarrow{OQ} &= \overrightarrow{OA} + \frac{2}{5}\overrightarrow{AB} \\
&= \mathbf{a} + \frac{2}{5}(\mathbf{b} - \mathbf{a}) \\
&= \mathbf{a} + \frac{2}{5}\mathbf{b} - \frac{2}{5}\mathbf{a} \\
&= \frac{3}{5}\mathbf{a} + \frac{2}{5}\mathbf{b}
\end{aligned}
$$

（c）

$$
\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = \left(\frac{3}{5}\mathbf{a} + \frac{2}{5}\mathbf{b}\right) - \frac{1}{3}\mathbf{a} = \left(\frac{3}{5} - \frac{1}{3}\right)\mathbf{a} + \frac{2}{5}\mathbf{b}
$$

通分：$\frac{3}{5} - \frac{1}{3} = \frac{9}{15} - \frac{5}{15} = \frac{4}{15}$

所以 $\overrightarrow{PQ} = \frac{4}{15}\mathbf{a} + \frac{2}{5}\mathbf{b}$

---

**5.**

（a）

$$
\mathbf{r}_A(t) = \begin{pmatrix} 0 \\ 5 \end{pmatrix} + \begin{pmatrix} 2 \\ 3 \end{pmatrix} t = \begin{pmatrix} 2t \\ 5 + 3t \end{pmatrix}
$$

$$
\mathbf{r}_B(t) = \begin{pmatrix} 10 \\ 0 \end{pmatrix} + \begin{pmatrix} -3 \\ 4 \end{pmatrix} t = \begin{pmatrix} 10 - 3t \\ 4t \end{pmatrix}
$$

（b）令 $\mathbf{r}_A(t) = \mathbf{r}_B(t)$：

$$
\begin{cases}
2t = 10 - 3t \implies 5t = 10 \implies t = 2 \\[4pt]
5 + 3t = 4t \implies 5 = t \implies t = 5
\end{cases}
$$

两个 $t$ 值不相等（$2 \neq 5$），所以两船不会相撞。

---

**6.**

（a）设正北为 $+y$ 轴，正东为 $+x$ 轴。

船相对于水的速度：$\mathbf{v}_{B/W} = 10\mathbf{j}$
水相对于地面的速度：$\mathbf{v}_{W/G} = 6\mathbf{i}$

合速度：$\mathbf{v}_{B/G} = 6\mathbf{i} + 10\mathbf{j}$

（b）大小：$|\mathbf{v}_{B/G}| = \sqrt{6^2 + 10^2} = \sqrt{36 + 100} = \sqrt{136} = 2\sqrt{34} \approx 11.66\,\text{m/s}$

方向：设 $\theta$ 为与正北方向的夹角。

$$
\tan\theta = \frac{6}{10} = 0.6 \implies \theta = \arctan(0.6) \approx 30.96^\circ
$$

所以方向为东偏北 $30.96^\circ$（或北偏东 $59.04^\circ$）。

---

**7.**

（a）

$$
\begin{aligned}
\frac{s(1+h) - s(1)}{h} &= \frac{[4(1+h)^2 + 3(1+h)] - [4 + 3]}{h} \\
&= \frac{[4(1 + 2h + h^2) + 3 + 3h] - 7}{h} \\
&= \frac{4 + 8h + 4h^2 + 3 + 3h - 7}{h} \\
&= \frac{11h + 4h^2}{h} = 11 + 4h
\end{aligned}
$$

（b）$v(1) = \displaystyle\lim_{h \to 0} (11 + 4h) = 11\,\text{m/s}$

验证：$s'(t) = 8t + 3$，$s'(1) = 8 + 3 = 11$ ✓

---

**8.**

（a）$\mathbf{v}(t) = \dfrac{d\mathbf{r}}{dt} = (4t + 1)\mathbf{i} + 3\mathbf{j}$

（b）$\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = 4\mathbf{i}$

（c）$\mathbf{v}(2) = (4 \times 2 + 1)\mathbf{i} + 3\mathbf{j} = 9\mathbf{i} + 3\mathbf{j}$

$|\mathbf{v}(2)| = \sqrt{9^2 + 3^2} = \sqrt{81 + 9} = \sqrt{90} = 3\sqrt{10} \approx 9.49\,\text{m/s}$

---

**9.**

（a）平行四边形 $ABCD$ 中，$\overrightarrow{AD} = \overrightarrow{BC}$。

$$
\overrightarrow{BC} = \mathbf{c} - \mathbf{b} = (4\mathbf{i} + 6\mathbf{j}) - (5\mathbf{i} + 3\mathbf{j}) = -\mathbf{i} + 3\mathbf{j}
$$

所以 $\mathbf{d} = \mathbf{a} + \overrightarrow{BC} = (2\mathbf{i} + \mathbf{j}) + (-\mathbf{i} + 3\mathbf{j}) = \mathbf{i} + 4\mathbf{j}$

（b）$\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (5\mathbf{i} + 3\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = 3\mathbf{i} + 2\mathbf{j}$

$\overrightarrow{AD} = \mathbf{d} - \mathbf{a} = (\mathbf{i} + 4\mathbf{j}) - (2\mathbf{i} + \mathbf{j}) = -\mathbf{i} + 3\mathbf{j}$

点积：$\overrightarrow{AB} \cdot \overrightarrow{AD} = (3)(-1) + (2)(3) = -3 + 6 = 3 \neq 0$

所以 $\overrightarrow{AB}$ 与 $\overrightarrow{AD}$ **不垂直**。

（c）方法一（用叉积的行列式公式）：

$$
\text{面积} = |x_1 y_2 - x_2 y_1|
$$

其中 $\overrightarrow{AB} = (3, 2)$，$\overrightarrow{AD} = (-1, 3)$。

$$
\text{面积} = |3 \times 3 - 2 \times (-1)| = |9 + 2| = 11
$$

方法二（用 $|\overrightarrow{AB}| \cdot |\overrightarrow{AD}| \cdot \sin\theta$）：

$$
|\overrightarrow{AB}| = \sqrt{3^2 + 2^2} = \sqrt{13}, \quad |\overrightarrow{AD}| = \sqrt{(-1)^2 + 3^2} = \sqrt{10}
$$

由点积 $\overrightarrow{AB} \cdot \overrightarrow{AD} = |\overrightarrow{AB}||\overrightarrow{AD}|\cos\theta$：

$$
3 = \sqrt{13} \cdot \sqrt{10} \cdot \cos\theta \implies \cos\theta = \frac{3}{\sqrt{130}}
$$

$$
\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \frac{9}{130}} = \sqrt{\frac{121}{130}} = \frac{11}{\sqrt{130}}
$$

$$
\text{面积} = \sqrt{13} \cdot \sqrt{10} \cdot \frac{11}{\sqrt{130}} = \sqrt{130} \cdot \frac{11}{\sqrt{130}} = 11
$$

平行四边形的面积为 $11$ 平方单位。✓

---

## 本章总结

### 考纲覆盖核对

| 考纲编号 | 内容 | 对应节次 | 例题 | 练习题 |
|:---:|------|:---:|:---:|:---:|
| 13.1 | 向量记号 | 2.1.1 | 2.1(1) | 1 |
| 13.2 | 位置向量与单位向量 | 2.1.2, 2.1.4 | 2.1(1) | 1(c) |
| 13.3 | 模、加减、数乘、向量几何 | 2.1.3, 2.1.5–2.1.8, 2.2.1 | 2.1, 2.2 | 1–4, 9 |
| 13.4 | 速度合成与分解、相撞问题 | 2.2.2 | 2.3 | 5, 6 |
| 14.1 | 变化率与极限思想 | 2.3 | 2.4 | 7, 8 |

### 核心公式速查表

**向量部分**：

| 概念 | 公式 |
|:---|:---|
| 向量表示 | $\mathbf{v} = x\mathbf{i} + y\mathbf{j} = \begin{pmatrix} x \\ y \end{pmatrix}$ |
| 模 | $|\mathbf{v}| = \sqrt{x^2 + y^2}$ |
| 单位向量 | $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{|\mathbf{v}|}$ |
| 位移 | $\overrightarrow{AB} = \mathbf{r}_B - \mathbf{r}_A$ |
| 中点 | $\mathbf{r}_M = \dfrac{\mathbf{r}_A + \mathbf{r}_B}{2}$ |
| 分点（$AP:PB = m:n$） | $\mathbf{r}_P = \dfrac{n\mathbf{r}_A + m\mathbf{r}_B}{m+n}$ |
| 平行条件 | $\mathbf{a} = k\mathbf{b}$（存在标量 $k$） |
| 垂直条件（点积） | $\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y = 0$ |
| 斜率法判垂直 | $k_1 \cdot k_2 = -1$ |
| 速度合成 | $\mathbf{v}_{A/C} = \mathbf{v}_{A/B} + \mathbf{v}_{B/C}$ |
| 速度分解 | $\mathbf{v} = (v\cos\theta)\mathbf{i} + (v\sin\theta)\mathbf{j}$ |
| 匀速直线运动 | $\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}t$ |
| 相撞条件 | $\mathbf{r}_1(t) = \mathbf{r}_2(t)$ |

**变化率部分**：

| 概念 | 公式 |
|:---|:---|
| 导数定义 | $f'(a) = \displaystyle\lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$ |
| 幂法则 | $\dfrac{d}{dx}(x^n) = n x^{n-1}$ |
| 速度（向量） | $\mathbf{v}(t) = \dfrac{d\mathbf{r}}{dt} = \dfrac{dx}{dt}\mathbf{i} + \dfrac{dy}{dt}\mathbf{j}$ |
| 加速度（向量） | $\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = \dfrac{d^2x}{dt^2}\mathbf{i} + \dfrac{d^2y}{dt^2}\mathbf{j}$ |
| 积分求速度 | $\mathbf{v}(t) = \int \mathbf{a}(t) \, dt + \mathbf{v}_0$ |
| 积分求位置 | $\mathbf{r}(t) = \int \mathbf{v}(t) \, dt + \mathbf{r}_0$ |

### 学习路线图

从本章出发，后续章节将这样深化你的理解：

- **第 5 章（微分）**：系统学习求导法则（链式法则、积法则、商法则），以及用导数求切线、法线和极值
- **第 7 章（积分）**：学习微分的逆运算——积分，掌握从加速度求速度和位置的完整方法
- **第 10 章（综合应用）**：将向量和微积分结合，解决完整的运动学问题

---
---

