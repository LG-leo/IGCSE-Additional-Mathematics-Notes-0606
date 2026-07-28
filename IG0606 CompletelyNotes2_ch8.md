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
- [第 3 章：二次函数](#第-3-章二次函数)
- [第 4 章：函数（线性、三次、指数、对数）](#第-4-章函数线性三次指数对数)
- [第 5 章：微分（导数）](#第-5-章微分导数)
- [第 6 章：方程与不等式（图形法）](#第-6-章方程与不等式图形法)
- [第 7 章：积分（不定积分与定积分）](#第-7-章积分不定积分与定积分)
- [第 8 章：三角学（含弧度法）](#第-8-章三角学含弧度法)
- [第 9 章：几何（直线与圆）](#第-9-章几何直线与圆)
- [第 10 章：综合应用](#第-10-章综合应用)

---

# 第 8 章：三角学（含弧度法）

---

## 引言与考纲对照

三角学是附加数学中工具性最强、应用最广的章节之一。从几何中的角度测量，到微积分中对三角函数求导与积分，再到物理中的运动分析，三角学无处不在。本章将系统性构建你对三角函数的完整理解。

### 考纲对照（Cambridge IGCSE Additional Mathematics 0606, 2028–2030）

| 考纲条目 | 内容 | 对应本节 |
|---------|------|---------|
| 9.1 | 弧长与扇形面积（弧度制） | **8.1** |
| 10.1 | 六个任意角三角函数 | **8.2** |
| 10.2 | 三角函数的振幅与周期 | **8.3** |
| 10.3 | 绘制 $y = a\sin(bx) + c$ 等图像 | **8.3** |
| 10.4 | 使用 $\sin^2 A + \cos^2 A = 1$ 等恒等式 | **8.4** |
| 10.5 | 解三角方程（含六个函数） | **8.5** |
| 10.6 | 证明三角恒等式 | **8.6** |

> **考试信息**：Paper 1（非计算器）和 Paper 2（可用计算器）均会考察三角学。弧度制在微积分部分**强制使用**。考纲提供的公式表中仅列出 $\sin^2 A + \cos^2 A = 1$、$\sec^2 A = 1 + \tan^2 A$、$\csc^2 A = 1 + \cot^2 A$ 三个恒等式。**弧长与扇形面积公式不提供**，需牢记。

---

## 8.1 弧度制（弧长、扇形面积、组合图形）

### 8.1.1 为什么要使用弧度？

在初等几何中，我们习惯用**度**（degree）来度量角。但在高等数学中，**弧度**（radian）才是自然的单位。原因有两个：

**原因一**：弧度将角度与弧长直接联系起来。当角度用弧度表示时，弧长公式 $s = r\theta$ 极其简洁。如果用度，公式将变为 $s = \frac{\pi r\theta}{180}$，多了一个不必要的系数。

**原因二**（更重要）：微积分中三角函数的导数公式只有在弧度制下才简洁优美。例如：

$$
\frac{d}{dx}\sin x = \cos x \quad (\text{弧度制})
$$

如果使用度，公式将变为 $\frac{d}{dx}\sin x^\circ = \frac{\pi}{180}\cos x^\circ$，多出了常数因子 $\pi/180$。因此在 IGCSE 附加数学的微积分部分，**所有角度必须使用弧度制**。

### 8.1.2 弧度的定义

**定义**：一弧度是弧长等于半径时所对应的圆心角。

设圆的半径为 $r$，一段弧的长度为 $s$，该弧所对的圆心角为 $\theta$（弧度），则有：

$$
\theta = \frac{s}{r} \quad \text{或等价地} \quad s = r\theta
$$

当 $s = r$ 时，$\theta = 1$ 弧度。

**与度的换算推导**：整圆对应的圆心角为 $360^\circ$，整圆周长为 $2\pi r$。由弧长公式 $s = r\theta$，整圆对应：

$$
2\pi r = r \times (\text{整圆的弧度数})
$$

因此整圆的弧度数为 $2\pi$，即：

$$
360^\circ = 2\pi \text{ 弧度}
$$

两边除以 2：

$$
180^\circ = \pi \text{ 弧度}
$$

由此可推导出所有换算关系：

$$
1^\circ = \frac{\pi}{180} \text{ 弧度}, \qquad
1 \text{ 弧度} = \frac{180^\circ}{\pi} \approx 57.3^\circ
$$

**常见角的弧度值**：

| 角度 | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|------|-----------|------------|------------|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|
| 弧度 | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

**记忆技巧**：记住 $\pi = 180^\circ$，然后按比例推算。例如 $30^\circ = \frac{180^\circ}{6} = \frac{\pi}{6}$。

### 8.1.3 弧长公式的推导

在半径为 $r$ 的圆中，整圆周长为 $2\pi r$，对应圆心角 $2\pi$ 弧度。

设圆心角为 $\theta$ 弧度，它所对的弧长为 $s$。由于弧长与圆心角成正比：

$$
\frac{s}{2\pi r} = \frac{\theta}{2\pi}
$$

交叉相乘：

$$
s = \frac{\theta}{2\pi} \times 2\pi r = r\theta
$$

因此：

$$
\boxed{s = r\theta}
$$

其中 $\theta$ **必须为弧度**。

### 8.1.4 扇形面积公式的推导

方法一（比例法）：整圆面积为 $\pi r^2$，对应 $2\pi$ 弧度。扇形面积 $A$ 与整圆面积之比等于圆心角 $\theta$ 与 $2\pi$ 之比：

$$
\frac{A}{\pi r^2} = \frac{\theta}{2\pi}
$$

$$
A = \frac{\theta}{2\pi} \times \pi r^2 = \frac{1}{2}r^2\theta
$$

方法二（积分法，微积分视角）：将扇形视为由无数个细小的三角形组成。每个小三角形的面积近似为 $\frac{1}{2}r \cdot r\,d\theta = \frac{1}{2}r^2\,d\theta$。从 $0$ 到 $\theta$ 积分：

$$
A = \int_0^\theta \frac{1}{2}r^2\,d\theta = \frac{1}{2}r^2\theta
$$

两种方法得到相同结果：

$$
\boxed{A = \frac{1}{2}r^2\theta}
$$

### 8.1.5 弓形面积

在扇形中，连接弧的两个端点的线段称为**弦**。弦与弧之间的区域称为**弓形**（segment）。

**弓形面积的推导**：

弓形面积 $=$ 扇形面积 $-$ 三角形面积

扇形面积我们已经知道为 $\frac{1}{2}r^2\theta$。三角形是由两条半径和弦围成的等腰三角形，其面积可以用"两边夹一角"公式计算：

$$
A_{\triangle} = \frac{1}{2} \cdot r \cdot r \cdot \sin\theta = \frac{1}{2}r^2\sin\theta
$$

因此：

$$
\boxed{A_{\text{弓形}} = \frac{1}{2}r^2\theta - \frac{1}{2}r^2\sin\theta = \frac{1}{2}r^2(\theta - \sin\theta)}
$$

> ⚠️ **注意**：此公式中的 $\theta$ 必须是弧度制，且为扇形的圆心角。

### 8.1.6 组合图形的解题策略

当遇到包含圆弧、扇形、三角形的组合图形时，通用的解题思路是：

1. **分解图形**：将复杂图形拆分为若干个扇形、三角形、矩形等基本图形
2. **确定已知量**：标出所有已知的半径、角度（注意是弧度还是度）、边长
3. **统一单位**：角度全部转换为弧度（如果不是弧度的话）
4. **分别计算**：用弧长、扇形面积、三角形面积公式分别计算各部分
5. **组合结果**：根据图形关系相加或相减

### 8.1.7 例题

---

**例题 1（角度与弧度互化）**：
(a) 将 $150^\circ$ 转换为弧度。
(b) 将 $\frac{5\pi}{6}$ 弧度转换为度。

**解**：

(a) 由 $1^\circ = \frac{\pi}{180}$ 弧度：

$$
150^\circ = 150 \times \frac{\pi}{180} = \frac{150\pi}{180} = \frac{5\pi}{6} \text{ 弧度}
$$

(b) 由 $1$ 弧度 $= \frac{180^\circ}{\pi}$：

$$
\frac{5\pi}{6} \text{ 弧度} = \frac{5\pi}{6} \times \frac{180^\circ}{\pi} = \frac{5 \times 180^\circ}{6} = 150^\circ
$$

**答案**：(a) $\dfrac{5\pi}{6}$ 弧度 (b) $150^\circ$

---

**例题 2（已知半径和圆心角求弧长与扇形面积）**：一个扇形的半径为 $12$ cm，圆心角为 $\frac{2\pi}{3}$ 弧度。求：
(a) 弧长
(b) 扇形面积

**解**：

(a) 代入弧长公式 $s = r\theta$：

$$
s = 12 \times \frac{2\pi}{3} = 8\pi \text{ cm}
$$

(b) 代入扇形面积公式 $A = \frac{1}{2}r^2\theta$：

$$
A = \frac{1}{2} \times 12^2 \times \frac{2\pi}{3} = \frac{1}{2} \times 144 \times \frac{2\pi}{3} = 72 \times \frac{2\pi}{3} = 48\pi \text{ cm}^2
$$

**答案**：(a) $8\pi$ cm (b) $48\pi$ cm²

---

**例题 3（已知弧长求圆心角和扇形面积）**：一个扇形的半径为 $10$ cm，弧长为 $25$ cm。求：
(a) 扇形的圆心角（弧度）
(b) 扇形的面积

**解**：

(a) 由 $s = r\theta$ 解出 $\theta$：

$$
\theta = \frac{s}{r} = \frac{25}{10} = 2.5 \text{ 弧度}
$$

(b) 代入扇形面积公式：

$$
A = \frac{1}{2}r^2\theta = \frac{1}{2} \times 10^2 \times 2.5 = \frac{1}{2} \times 100 \times 2.5 = 125 \text{ cm}^2
$$

**答案**：(a) $2.5$ 弧度 (b) $125$ cm²

---

**例题 4（已知扇形面积求圆心角和弧长）**：一个半径为 $6$ cm 的扇形面积为 $15\pi$ cm²。求：
(a) 扇形的圆心角（弧度）
(b) 扇形的弧长

**解**：

(a) 由 $A = \frac{1}{2}r^2\theta$ 解出 $\theta$：

$$
15\pi = \frac{1}{2} \times 6^2 \times \theta = \frac{1}{2} \times 36 \times \theta = 18\theta
$$

$$
\theta = \frac{15\pi}{18} = \frac{5\pi}{6} \text{ 弧度}
$$

(b) 代入弧长公式：

$$
s = r\theta = 6 \times \frac{5\pi}{6} = 5\pi \text{ cm}
$$

**答案**：(a) $\dfrac{5\pi}{6}$ 弧度 (b) $5\pi$ cm

---

**例题 5（弓形面积）**：一个半径为 $8$ cm 的圆中，圆心角为 $\frac{\pi}{4}$ 的扇形被截去三角形部分，求剩余弓形的面积。

**解**：

**步骤 1**：计算扇形面积。

$$
A_{\text{扇}} = \frac{1}{2}r^2\theta = \frac{1}{2} \times 8^2 \times \frac{\pi}{4} = \frac{1}{2} \times 64 \times \frac{\pi}{4} = 8\pi \text{ cm}^2
$$

**步骤 2**：计算三角形面积（两边为半径 $8$ cm，夹角 $\frac{\pi}{4}$）。

$$
A_{\triangle} = \frac{1}{2}r^2\sin\theta = \frac{1}{2} \times 8^2 \times \sin\frac{\pi}{4} = \frac{1}{2} \times 64 \times \frac{\sqrt{2}}{2} = 16\sqrt{2} \text{ cm}^2
$$

**步骤 3**：弓形面积 $=$ 扇形面积 $-$ 三角形面积。

$$
A_{\text{弓}} = 8\pi - 16\sqrt{2} \text{ cm}^2
$$

**答案**：$8\pi - 16\sqrt{2}$ cm²

---

**例题 6（组合图形——两个扇形）**：下图由一个半径为 $5$ cm 的大扇形（圆心角 $\frac{\pi}{3}$）和一个半径为 $3$ cm 的小扇形（相同的圆心角）组合而成（即一个"环形扇形"）。求阴影区域（两个扇形之间的区域）的面积。

**解**：

**思路**：阴影区域面积 $=$ 大扇形面积 $-$ 小扇形面积。

**步骤 1**：大扇形面积。

$$
A_{\text{大}} = \frac{1}{2} \times 5^2 \times \frac{\pi}{3} = \frac{1}{2} \times 25 \times \frac{\pi}{3} = \frac{25\pi}{6} \text{ cm}^2
$$

**步骤 2**：小扇形面积。

$$
A_{\text{小}} = \frac{1}{2} \times 3^2 \times \frac{\pi}{3} = \frac{1}{2} \times 9 \times \frac{\pi}{3} = \frac{3\pi}{2} \text{ cm}^2
$$

**步骤 3**：阴影面积。

$$
A = A_{\text{大}} - A_{\text{小}} = \frac{25\pi}{6} - \frac{3\pi}{2} = \frac{25\pi}{6} - \frac{9\pi}{6} = \frac{16\pi}{6} = \frac{8\pi}{3} \text{ cm}^2
$$

**答案**：$\dfrac{8\pi}{3}$ cm²

---

**例题 7（组合图形——扇形与三角形）**：一个扇形的半径为 $10$ cm，圆心角为 $60^\circ$。在扇形内作一个最大的等腰三角形，其中两条边为扇形的两条半径，底边为弦。求扇形中除去三角形后的剩余面积。

**解**：

**步骤 1**：先将 $60^\circ$ 转换为弧度。

$$
\theta = 60^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{3}
$$

**步骤 2**：扇形面积。

$$
A_{\text{扇}} = \frac{1}{2} \times 10^2 \times \frac{\pi}{3} = 50 \times \frac{\pi}{3} = \frac{50\pi}{3} \text{ cm}^2
$$

**步骤 3**：三角形面积。等腰三角形的顶角为 $\frac{\pi}{3}$，腰长为 $10$ cm。

$$
A_{\triangle} = \frac{1}{2} \times 10 \times 10 \times \sin\frac{\pi}{3} = 50 \times \frac{\sqrt{3}}{2} = 25\sqrt{3} \text{ cm}^2
$$

**步骤 4**：剩余面积。

$$
A = \frac{50\pi}{3} - 25\sqrt{3} \text{ cm}^2
$$

**答案**：$\dfrac{50\pi}{3} - 25\sqrt{3}$ cm²

---

> ⚠️ **易错提醒**：
> 1. 弧长和扇形面积公式中的 $\theta$ **必须使用弧度制**，不能使用度
> 2. 弓形面积公式中 $\theta - \sin\theta$ 两项中的 $\theta$ 都是弧度值
> 3. 遇到混合了度和弧度的题目，先统一单位再计算

---

## 8.2 六个三角函数（任意角）

### 8.2.1 从锐角三角比到任意角三角函数

在直角三角形中，对于锐角 $\theta$，我们最初的定义是：

$$
\sin\theta = \frac{\text{对边}}{\text{斜边}}, \quad
\cos\theta = \frac{\text{邻边}}{\text{斜边}}, \quad
\tan\theta = \frac{\text{对边}}{\text{邻边}}
$$

但这个定义有严重的局限性——它只适用于 $0^\circ < \theta < 90^\circ$ 的角。如果角度大于 $90^\circ$ 或是负角，直角三角形就无法直接定义了。

**突破**：我们将角度放在**坐标系**中，用**单位圆**来重新定义三角函数，从而将定义域扩展到全体实数。

### 8.2.2 单位圆定义法

**单位圆**是圆心在原点、半径为 $1$ 的圆，方程为：

$$
x^2 + y^2 = 1
$$

对于任意角 $\theta$，我们按以下方式放置它：
- 角的顶点在原点
- 角的起始边沿正 $x$ 轴方向
- 角的终边从起始边逆时针旋转 $\theta$（若 $\theta$ 为负则顺时针旋转）

设角的终边与单位圆的交点为 $P(x, y)$，则定义：

$$
\boxed{\sin\theta = y}, \qquad \boxed{\cos\theta = x}, \qquad \boxed{\tan\theta = \frac{y}{x} \;(x \neq 0)}
$$

**为什么这样定义是合理的？**

当 $\theta$ 为锐角时，我们在单位圆上得到的点 $P$ 恰好构成一个直角三角形——从 $P$ 向 $x$ 轴作垂线，得到直角三角形的对边为 $y$，邻边为 $x$，斜边为 $1$。因此 $\sin\theta = y/1 = y$，$\cos\theta = x/1 = x$，与直角三角形定义完全一致。

而当 $\theta$ 为任意角时，$x$ 和 $y$ 坐标可以为正、零或负，三角函数的符号也随之变化——这正是我们想要的！

### 8.2.3 六个三角函数的完整定义

由 $\sin\theta$ 和 $\cos\theta$ 出发，可以定义另外四个函数：

**正切**：

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{y}{x}, \quad \cos\theta \neq 0
$$

**余割**（$\sin$ 的倒数）：

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{y}, \quad \sin\theta \neq 0
$$

**正割**（$\cos$ 的倒数）：

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{x}, \quad \cos\theta \neq 0
$$

**余切**（$\tan$ 的倒数）：

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta} = \frac{x}{y}, \quad \sin\theta \neq 0
$$

**六个函数一览表**：

| 函数 | 记号 | 单位圆定义 | 定义域限制 |
|------|------|-----------|-----------|
| 正弦 | $\sin\theta$ | $y$ | 全体实数 |
| 余弦 | $\cos\theta$ | $x$ | 全体实数 |
| 正切 | $\tan\theta$ | $y/x$ | $x \neq 0$，即 $\theta \neq \frac{\pi}{2} + n\pi$ |
| 余割 | $\csc\theta$ | $1/y$ | $y \neq 0$，即 $\theta \neq n\pi$ |
| 正割 | $\sec\theta$ | $1/x$ | $x \neq 0$，即 $\theta \neq \frac{\pi}{2} + n\pi$ |
| 余切 | $\cot\theta$ | $x/y$ | $y \neq 0$，即 $\theta \neq n\pi$ |

### 8.2.4 特殊角的三角函数值推导

**特殊三角形法**：

**(a) $45^\circ$（$\frac{\pi}{4}$）角的推导**

考虑一个等腰直角三角形，两直角边均为 $1$，斜边为 $\sqrt{2}$。

$$
\sin\frac{\pi}{4} = \frac{\text{对边}}{\text{斜边}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

$$
\cos\frac{\pi}{4} = \frac{\text{邻边}}{\text{斜边}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

$$
\tan\frac{\pi}{4} = \frac{\text{对边}}{\text{邻边}} = \frac{1}{1} = 1
$$

**(b) $30^\circ$（$\frac{\pi}{6}$）和 $60^\circ$（$\frac{\pi}{3}$）角的推导**

考虑一个 $30^\circ$-$60^\circ$-$90^\circ$ 的直角三角形，三边比例为 $1 : \sqrt{3} : 2$（$30^\circ$ 对边为 $1$，$60^\circ$ 对边为 $\sqrt{3}$，斜边为 $2$）。

对于 $30^\circ$：

$$
\sin\frac{\pi}{6} = \frac{1}{2}, \quad
\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}, \quad
\tan\frac{\pi}{6} = \frac{1}{\sqrt{3}}
$$

对于 $60^\circ$：

$$
\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}, \quad
\cos\frac{\pi}{3} = \frac{1}{2}, \quad
\tan\frac{\pi}{3} = \sqrt{3}
$$

**(c) $0^\circ$ 和 $90^\circ$ 的推导**

在单位圆上，$\theta = 0$ 时终边与正 $x$ 轴重合，交点为 $(1, 0)$，所以 $\sin 0 = 0$，$\cos 0 = 1$，$\tan 0 = 0/1 = 0$。

$\theta = \frac{\pi}{2}$ 时终边与正 $y$ 轴重合，交点为 $(0, 1)$，所以 $\sin\frac{\pi}{2} = 1$，$\cos\frac{\pi}{2} = 0$，$\tan\frac{\pi}{2}$ 无定义（分母为零）。

**完整特殊角值表**：

| $\theta$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ |
|----------|-----|-----------------|-----------------|-----------------|-----------------|-------|-------------------|
| $\sin\theta$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ |
| $\cos\theta$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | 无定义 | $0$ | 无定义 |

### 8.2.5 符号法则——ASTC

三角函数在四个象限中的符号由单位圆上 $x$、$y$ 坐标的符号决定。

| 象限 | 角度范围 | $x = \cos\theta$ | $y = \sin\theta$ | $\tan\theta = y/x$ | 正值函数 |
|------|---------|-----------------|-----------------|-------------------|---------|
| I | $0 < \theta < \dfrac{\pi}{2}$ | $+$ | $+$ | $+$ | **A**ll（全部） |
| II | $\dfrac{\pi}{2} < \theta < \pi$ | $-$ | $+$ | $-$ | **S**in（及 csc） |
| III | $\pi < \theta < \dfrac{3\pi}{2}$ | $-$ | $-$ | $+$ | **T**an（及 cot） |
| IV | $\dfrac{3\pi}{2} < \theta < 2\pi$ | $+$ | $-$ | $-$ | **C**os（及 sec） |

**记忆口诀**：逆时针从第一象限开始，ASTC

完整的六个函数符号表：

| 象限 | $\sin$ | $\cos$ | $\tan$ | $\sec$ | $\csc$ | $\cot$ |
|------|--------|--------|--------|--------|--------|--------|
| I | $+$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| II | $+$ | $-$ | $-$ | $-$ | $+$ | $-$ |
| III | $-$ | $-$ | $+$ | $-$ | $-$ | $+$ |
| IV | $-$ | $+$ | $-$ | $+$ | $-$ | $-$ |

### 8.2.6 参考角法

**参考角**（reference angle）是指角的终边与 $x$ 轴之间的最小夹角，通常记为 $\alpha$，且 $0 \leq \alpha \leq \frac{\pi}{2}$。

对于任意角 $\theta$，其在 $[0, 2\pi)$ 内的参考角 $\alpha$ 为：

| $\theta$ 所在象限 | 参考角 $\alpha$ |
|-----------------|---------------|
| I | $\alpha = \theta$ |
| II | $\alpha = \pi - \theta$ |
| III | $\alpha = \theta - \pi$ |
| IV | $\alpha = 2\pi - \theta$ |

> **核心性质**：任意角的三角函数值等于其参考角的三角函数值的绝对值，再根据象限确定正负号。即：
> $$
> \sin\theta = \pm\sin\alpha,\quad \cos\theta = \pm\cos\alpha,\quad \tan\theta = \pm\tan\alpha
> $$
> 其中正负号由 $\theta$ 所在象限决定。

### 8.2.7 例题

---

**例题 1（已知 $\sin$ 求其他函数——锐角情况）**：已知 $\sin\theta = \frac{4}{5}$ 且 $0 < \theta < \frac{\pi}{2}$，求 $\cos\theta$、$\tan\theta$、$\sec\theta$、$\csc\theta$、$\cot\theta$ 的值。

**解**：

**步骤 1**：利用 $\sin^2\theta + \cos^2\theta = 1$ 求 $\cos^2\theta$。

$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{4}{5}\right)^2 = 1 - \frac{16}{25} = \frac{9}{25}
$$

**步骤 2**：确定 $\cos\theta$ 的符号。$\theta$ 在第一象限，$\cos\theta > 0$，所以：

$$
\cos\theta = \sqrt{\frac{9}{25}} = \frac{3}{5}
$$

**步骤 3**：依次求其他函数。

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{4/5}{3/5} = \frac{4}{3}
$$

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{3/5} = \frac{5}{3}
$$

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{4/5} = \frac{5}{4}
$$

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{1}{4/3} = \frac{3}{4}
$$

**答案**：$\cos\theta = \frac{3}{5}$，$\tan\theta = \frac{4}{3}$，$\sec\theta = \frac{5}{3}$，$\csc\theta = \frac{5}{4}$，$\cot\theta = \frac{3}{4}$

---

**例题 2（已知 $\sin$ 求其他函数——任意角情况）**：已知 $\sin\theta = \frac{3}{5}$ 且 $\theta$ 在第二象限，求 $\cos\theta$、$\tan\theta$、$\sec\theta$、$\csc\theta$、$\cot\theta$ 的值。

**解**：

**步骤 1**：利用 $\sin^2\theta + \cos^2\theta = 1$ 求 $\cos^2\theta$。

$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}
$$

**步骤 2**：确定 $\cos\theta$ 的符号。$\theta$ 在第二象限，$\cos\theta < 0$，所以：

$$
\cos\theta = -\sqrt{\frac{16}{25}} = -\frac{4}{5}
$$

**步骤 3**：依次求其他函数。

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{3/5}{-4/5} = -\frac{3}{4}
$$

$$
\sec\theta = \frac{1}{\cos\theta} = \frac{1}{-4/5} = -\frac{5}{4}
$$

$$
\csc\theta = \frac{1}{\sin\theta} = \frac{1}{3/5} = \frac{5}{3}
$$

$$
\cot\theta = \frac{1}{\tan\theta} = \frac{1}{-3/4} = -\frac{4}{3}
$$

**答案**：$\cos\theta = -\frac{4}{5}$，$\tan\theta = -\frac{3}{4}$，$\sec\theta = -\frac{5}{4}$，$\csc\theta = \frac{5}{3}$，$\cot\theta = -\frac{4}{3}$

> **对比**：与例题 1 相比，$\theta$ 从第一象限变为第二象限，$\cos$ 和 $\tan$ 的符号发生了变化（由正变负），但绝对值相同。这正是参考角法的体现。

---

**例题 3（参考角法求任意角三角函数值）**：求 $\sin\frac{5\pi}{6}$、$\cos\frac{5\pi}{6}$、$\tan\frac{5\pi}{6}$ 的精确值。

**解**：

**步骤 1**：确定 $\theta = \frac{5\pi}{6}$ 所在的象限。

$\frac{5\pi}{6}$ 对应 $150^\circ$，在第二象限（介于 $\frac{\pi}{2}$ 和 $\pi$ 之间）。

**步骤 2**：求参考角。

第二象限的参考角为 $\alpha = \pi - \theta = \pi - \frac{5\pi}{6} = \frac{\pi}{6}$。

**步骤 3**：确定各函数的符号。

在第二象限，$\sin$ 为正，$\cos$ 为负，$\tan$ 为负。

**步骤 4**：写出答案。

$$
\sin\frac{5\pi}{6} = +\sin\frac{\pi}{6} = \frac{1}{2}
$$

$$
\cos\frac{5\pi}{6} = -\cos\frac{\pi}{6} = -\frac{\sqrt{3}}{2}
$$

$$
\tan\frac{5\pi}{6} = -\tan\frac{\pi}{6} = -\frac{1}{\sqrt{3}}
$$

---

**例题 4（参考角法——第四象限角）**：求 $\sin\frac{7\pi}{4}$、$\cos\frac{7\pi}{4}$、$\tan\frac{7\pi}{4}$ 的精确值。

**解**：

**步骤 1**：确定象限。$\frac{7\pi}{4}$ 对应 $315^\circ$，在第四象限。

**步骤 2**：求参考角。第四象限的参考角为 $\alpha = 2\pi - \theta = 2\pi - \frac{7\pi}{4} = \frac{\pi}{4}$。

**步骤 3**：确定符号。第四象限中，$\sin$ 为负，$\cos$ 为正，$\tan$ 为负。

**步骤 4**：写出答案。

$$
\sin\frac{7\pi}{4} = -\sin\frac{\pi}{4} = -\frac{\sqrt{2}}{2}
$$

$$
\cos\frac{7\pi}{4} = +\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$

$$
\tan\frac{7\pi}{4} = -\tan\frac{\pi}{4} = -1
$$

---

**例题 5（已知 $\tan$ 求其他函数）**：已知 $\tan\theta = 2$ 且 $\pi < \theta < \frac{3\pi}{2}$，求 $\sin\theta$ 和 $\cos\theta$ 的值。

**解**：

**步骤 1**：确定 $\theta$ 在第三象限（$\pi$ 到 $\frac{3\pi}{2}$）。在第三象限，$\sin$ 和 $\cos$ 均为负值。

**步骤 2**：由 $\tan\theta = \frac{\sin\theta}{\cos\theta} = 2$，可知 $\sin\theta = 2\cos\theta$。

**步骤 3**：代入 $\sin^2\theta + \cos^2\theta = 1$。

$$
(2\cos\theta)^2 + \cos^2\theta = 1
$$

$$
4\cos^2\theta + \cos^2\theta = 1
$$

$$
5\cos^2\theta = 1
$$

$$
\cos^2\theta = \frac{1}{5}
$$

**步骤 4**：确定符号。$\theta$ 在第三象限，$\cos\theta < 0$，所以：

$$
\cos\theta = -\sqrt{\frac{1}{5}} = -\frac{1}{\sqrt{5}}
$$

**步骤 5**：求 $\sin\theta$。

$$
\sin\theta = 2\cos\theta = 2 \times \left(-\frac{1}{\sqrt{5}}\right) = -\frac{2}{\sqrt{5}}
$$

**答案**：$\sin\theta = -\dfrac{2}{\sqrt{5}}$，$\cos\theta = -\dfrac{1}{\sqrt{5}}$

---

**例题 6（已知 $\sec$ 求其他函数）**：已知 $\sec\theta = 3$ 且 $\frac{3\pi}{2} < \theta < 2\pi$，求 $\sin\theta$、$\cos\theta$、$\tan\theta$。

**解**：

**步骤 1**：由 $\sec\theta = \frac{1}{\cos\theta} = 3$ 得 $\cos\theta = \frac{1}{3}$。$\theta$ 在第四象限，$\cos\theta > 0$，符号一致。

**步骤 2**：由 $\sin^2\theta + \cos^2\theta = 1$：

$$
\sin^2\theta = 1 - \cos^2\theta = 1 - \frac{1}{9} = \frac{8}{9}
$$

**步骤 3**：确定符号。$\theta$ 在第四象限，$\sin\theta < 0$，所以：

$$
\sin\theta = -\sqrt{\frac{8}{9}} = -\frac{2\sqrt{2}}{3}
$$

**步骤 4**：求 $\tan\theta$。

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-2\sqrt{2}/3}{1/3} = -2\sqrt{2}
$$

**答案**：$\sin\theta = -\dfrac{2\sqrt{2}}{3}$，$\cos\theta = \dfrac{1}{3}$，$\tan\theta = -2\sqrt{2}$

---

**例题 7（已知 $\cot$ 求角度）**：已知 $\cot\theta = \sqrt{3}$ 且 $\pi < \theta < 2\pi$，求 $\theta$ 的可能值（弧度）。

**解**：

**步骤 1**：$\cot\theta = \sqrt{3}$ 意味着 $\tan\theta = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$。

**步骤 2**：求参考角。$\tan\alpha = \frac{\sqrt{3}}{3}$ 时，$\alpha = \frac{\pi}{6}$。

**步骤 3**：确定 $\tan\theta > 0$ 的象限。正切为正发生在第一和第三象限。

**步骤 4**：给定范围 $\pi < \theta < 2\pi$（第三和第四象限），结合 $\tan\theta > 0$，$\theta$ 只能在第三象限：

$$
\theta = \pi + \alpha = \pi + \frac{\pi}{6} = \frac{7\pi}{6}
$$

**答案**：$\theta = \dfrac{7\pi}{6}$

---

## 8.3 三角函数的图像（振幅、周期、渐近线）

### 8.3.1 基本三角函数的图像

#### $y = \sin x$

先列出 $[0, 2\pi]$ 区间内的关键点：

| $x$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-------|-------------------|--------|
| $\sin x$ | $0$ | $1$ | $0$ | $-1$ | $0$ |

**性质总结**：

- **定义域**：$\mathbb{R}$（全体实数）
- **值域**：$[-1, 1]$
- **周期性**：周期为 $2\pi$，即 $\sin(x + 2\pi) = \sin x$
- **奇偶性**：奇函数，$\sin(-x) = -\sin x$，图像关于原点对称
- **零点**：$x = n\pi$（$n \in \mathbb{Z}$）
- **最大值**：在 $x = \frac{\pi}{2} + 2n\pi$ 处取 $1$
- **最小值**：在 $x = \frac{3\pi}{2} + 2n\pi$ 处取 $-1$

图像形态：从 $0$ 开始上升，像波浪般周期性振荡。

#### $y = \cos x$

关键点：

| $x$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-------|-------------------|--------|
| $\cos x$ | $1$ | $0$ | $-1$ | $0$ | $1$ |

**性质总结**：

- **定义域**：$\mathbb{R}$
- **值域**：$[-1, 1]$
- **周期性**：周期 $2\pi$
- **奇偶性**：偶函数，$\cos(-x) = \cos x$，图像关于 $y$ 轴对称
- **零点**：$x = \frac{\pi}{2} + n\pi$
- **最大值**：在 $x = 2n\pi$ 处取 $1$
- **最小值**：在 $x = \pi + 2n\pi$ 处取 $-1$

**正弦与余弦的关系**：

$$
\cos x = \sin\left(x + \frac{\pi}{2}\right), \qquad
\sin x = \cos\left(x - \frac{\pi}{2}\right)
$$

即余弦曲线是正弦曲线向左平移 $\frac{\pi}{2}$ 的结果。

#### $y = \tan x$

关键点和渐近线：

| $x$ | $-\dfrac{\pi}{2}$ | $0$ | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ |
|-----|-------------------|-----|-----------------|-------|-------------------|
| $\tan x$ | 无定义 | $0$ | 无定义 | $0$ | 无定义 |

**性质总结**：

- **定义域**：$x \neq \frac{\pi}{2} + n\pi$（在这些点 $\cos x = 0$，正切无定义）
- **值域**：$\mathbb{R}$（全体实数）
- **周期性**：周期 $\pi$，即 $\tan(x + \pi) = \tan x$
- **奇偶性**：奇函数，$\tan(-x) = -\tan x$，关于原点对称
- **零点**：$x = n\pi$
- **渐近线**：$x = \frac{\pi}{2} + n\pi$（垂直渐近线）

图像形态：在每个周期 $(-\frac{\pi}{2}, \frac{\pi}{2})$ 内，从负无穷经过 $0$ 上升到正无穷。

#### $y = \sec x$、$y = \csc x$、$y = \cot x$ 的图像概要

- $y = \sec x = \frac{1}{\cos x}$：在 $\cos x = 0$（$x = \frac{\pi}{2} + n\pi$）处有垂直渐近线，值域 $(-\infty, -1] \cup [1, \infty)$，周期 $2\pi$，偶函数
- $y = \csc x = \frac{1}{\sin x}$：在 $\sin x = 0$（$x = n\pi$）处有垂直渐近线，值域 $(-\infty, -1] \cup [1, \infty)$，周期 $2\pi$，奇函数
- $y = \cot x = \frac{\cos x}{\sin x}$：在 $\sin x = 0$（$x = n\pi$）处有垂直渐近线，值域 $\mathbb{R}$，周期 $\pi$，奇函数

### 8.3.2 三角函数的变换

考虑一般形式 $y = a\sin(bx + c) + d$（对 $\cos$ 和 $\tan$ 也适用，虽然 $\tan$ 没有振幅的概念）。

#### 振幅（Amplitude）

参数 $a$ 控制垂直方向的拉伸或压缩。对于正弦和余弦，$|a|$ 是波形偏离中心线的最大距离。

**推导**：$\sin x$ 的值域为 $[-1, 1]$，乘以 $a$ 后值域变为 $[-|a|, |a|]$（若 $a > 0$）或 $[|a|, -|a|]$（若 $a < 0$）。因此振幅为 $|a|$。

**示例**：$y = 3\sin x$ 的振幅为 $3$，最大值 $3$，最小值 $-3$。

#### 周期（Period）

参数 $b$ 控制水平方向的拉伸或压缩。

**推导**：$\sin x$ 的周期为 $2\pi$，即 $\sin(x + 2\pi) = \sin x$。对于 $y = \sin(bx)$，我们希望找到最小的正数 $T$ 使得 $\sin(b(x + T)) = \sin(bx)$。由于 $\sin$ 的周期为 $2\pi$，我们需要 $bT = 2\pi$，即：

$$
T = \frac{2\pi}{|b|}
$$

对 $\tan(bx)$，由于 $\tan x$ 的周期为 $\pi$，所以：

$$
T = \frac{\pi}{|b|}
$$

**示例**：$y = \sin(2x)$ 的周期为 $T = \frac{2\pi}{2} = \pi$。$y = \tan\left(\frac{x}{2}\right)$ 的周期为 $T = \frac{\pi}{1/2} = 2\pi$。

#### 相移（Phase Shift）

参数 $c$ 引起水平平移。

**推导**：

$$
y = \sin(bx + c) = \sin\left[b\left(x + \frac{c}{b}\right)\right]
$$

这相当于将 $y = \sin(bx)$ 的图像向左平移 $\frac{c}{b}$ 个单位。若 $\frac{c}{b} > 0$ 则左移，$\frac{c}{b} < 0$ 则右移。**相移量**通常定义为 $-\frac{c}{b}$（正数表示右移）。

#### 垂直平移（Vertical Shift）

参数 $d$ 将整个图像向上（$d > 0$）或向下（$d < 0$）平移 $|d|$ 个单位。$d$ 也是新图像的中心线（中轴线）的纵坐标。

**综合公式**：对于 $y = a\sin(bx + c) + d$：

| 参数 | 名称 | 计算公式 |
|------|------|---------|
| $|a|$ | 振幅 | 最大值 $= d + |a|$，最小值 $= d - |a|$ |
| $T = \dfrac{2\pi}{|b|}$ | 周期 | 对 $\tan$ 为 $\dfrac{\pi}{|b|}$ |
| $-\dfrac{c}{b}$ | 相移 | $>0$ 右移，$<0$ 左移 |
| $d$ | 垂直平移 | 新中心线为 $y = d$ |

### 8.3.3 图像绘制方法

**绘制 $y = a\sin(bx + c) + d$ 的步骤**：

1. 确定振幅 $|a|$、周期 $T = \frac{2\pi}{|b|}$、相移 $-\frac{c}{b}$、垂直平移 $d$
2. 找出一个完整周期内的关键点（通常取 5 个点：起点、峰点、中点、谷点、终点）
3. 标出中心线 $y = d$，标出最大值 $d + |a|$ 和最小值 $d - |a|$
4. 从相移后的起点开始，每隔 $T/4$ 取一个关键点
5. 用平滑曲线连接各点

### 8.3.4 例题

---

**例题 1（确定变换参数）**：对于函数 $y = 4\cos\left(3x + \frac{\pi}{2}\right) - 2$，求振幅、周期、相移和垂直平移，并写出其最大值和最小值。

**解**：

与标准形式 $y = a\cos(bx + c) + d$ 对比：

$$
a = 4,\quad b = 3,\quad c = \frac{\pi}{2},\quad d = -2
$$

**振幅**：$|a| = |4| = 4$

**周期**：$T = \frac{2\pi}{|b|} = \frac{2\pi}{3}$

**相移**：$-\frac{c}{b} = -\frac{\pi/2}{3} = -\frac{\pi}{6}$（负值表示向左平移 $\frac{\pi}{6}$）

**垂直平移**：$d = -2$（向下平移 $2$ 个单位）

**最大值**：$d + |a| = -2 + 4 = 2$

**最小值**：$d - |a| = -2 - 4 = -6$

---

**例题 2（由图像特征求函数表达式）**：一个正弦型函数的图像满足以下条件：振幅为 $3$，周期为 $4\pi$，在 $x = 0$ 处的函数值为 $0$ 且正在上升，图像被垂直平移使得中轴线为 $y = 2$。写出该函数的一个可能表达式。

**解**：

**步骤 1**：设函数为 $y = a\sin(bx + c) + d$。

**步骤 2**：由振幅 $3$ 得 $|a| = 3$，取 $a = 3$。

**步骤 3**：由周期 $T = 4\pi$ 得 $T = \frac{2\pi}{|b|} = 4\pi$，所以 $|b| = \frac{2\pi}{4\pi} = \frac{1}{2}$，取 $b = \frac{1}{2}$。

**步骤 4**：由中轴线 $y = 2$ 得 $d = 2$。

**步骤 5**：由 $x = 0$ 时 $y = 0$ 且正在上升：

$$
y(0) = 3\sin\left(\frac{1}{2} \times 0 + c\right) + 2 = 3\sin c + 2 = 0
$$

$$
\sin c = -\frac{2}{3}
$$

这个条件给出的 $c$ 不是一个标准角，看起来不太对。让我重新思考——题目说"在 $x = 0$ 处的函数值为 $0$ 且正在上升"，对于正弦函数，$x = 0$ 处为 $0$ 且上升意味着没有相移（$\sin 0 = 0$，且在 $0$ 附近 $\sin x$ 上升）。但由于 $d = 2$，$x = 0$ 时函数值为 $0$，所以 $\sin c$ 需要满足 $3\sin c + 2 = 0$。

等等，让我换一种思路。如果我们使用 $y = a\sin(b(x - \phi)) + d$，其中 $\phi$ 是相移。

取 $a = 3$，$b = \frac{1}{2}$，$d = 2$。

函数在 $x = 0$ 处值为 $0$ 且上升：

$$
y = 3\sin\left(\frac{1}{2}(x - \phi)\right) + 2
$$

$$
3\sin\left(-\frac{1}{2}\phi\right) + 2 = 0 \Rightarrow \sin\left(-\frac{\phi}{2}\right) = -\frac{2}{3}
$$

这有点复杂。其实更简单的方法是：标准正弦函数 $y = \sin x$ 在 $x = 0$ 处为 $0$ 且上升。如果 $d = 2$ 且 $a = 3$，那么在 $x = 0$ 时 $y = 0$ 意味着 $3\sin(-\phi b) + 2 = 0$。

让我用更简单的方法。如果使用余弦型函数 $y = a\cos(bx + c) + d$，标准余弦在 $x = 0$ 处取最大值。但这不符合"值为 0 且上升"的条件。

实际上，用 $y = 3\sin\left(\frac{x}{2}\right) + 2$ 的话，在 $x = 0$ 时 $y = 3\sin 0 + 2 = 2 \neq 0$，不符合条件。

题目的条件说"在 $x = 0$ 处的函数值为 $0$ 且正在上升"，这说明正弦函数在 $x = 0$ 时经过中心线并上升。

对于 $y = a\sin(bx + c) + d$，经过 $(0, 0)$：
$$
a\sin c + d = 0 \Rightarrow \sin c = -\frac{d}{a} = -\frac{2}{3}
$$

这个 $c$ 不是标准角。让我们用一个更简单的设定。取 $a = 3$，$b = \frac{1}{2}$，$d = 2$，且要求 $y(0) = 0$：

$$
3\sin(c) + 2 = 0 \Rightarrow \sin c = -\frac{2}{3}
$$

$c = \arcsin(-2/3)$ 不是一个特殊角。这对于例题来说不太理想。

让我换一个更简洁的设定。将条件改为"图像经过 $(0, 2)$ 且正在上升"（即在中轴线上），这样 $c = 0$ 即可。或者用另一种方式满足条件。

让我重新构造这个例题使其更简洁：

---

**例题 2（由图像特征求函数表达式——修正版）**：一个正弦型函数的图像满足以下条件：振幅为 $2$，周期为 $\pi$，在 $x = 0$ 处函数值为 $1$（中轴线位置），且正在上升，图像垂直平移使得中轴线为 $y = 1$。写出该函数的一个可能表达式。

**解**：

**步骤 1**：设函数为 $y = a\sin(bx + c) + d$。

**步骤 2**：由振幅 $2$ 得 $|a| = 2$，取 $a = 2$。

**步骤 3**：由周期 $T = \pi$ 得 $T = \frac{2\pi}{|b|} = \pi$，所以 $|b| = 2$，取 $b = 2$。

**步骤 4**：由中轴线 $y = 1$ 得 $d = 1$。

**步骤 5**：由 $x = 0$ 时 $y = 1$（中轴线上）且正在上升——说明此时正弦的自变量为 $0$（因为 $\sin 0 = 0$ 且在 $0$ 附近上升）：

$$
2\sin(2 \times 0 + c) + 1 = 1 \Rightarrow 2\sin c + 1 = 1 \Rightarrow \sin c = 0
$$

$\sin c = 0$ 的解为 $c = n\pi$。当 $c = 0$ 时，$y = 2\sin(2x) + 1$，在 $x = 0$ 处：
- $y = 1$（中轴线）
- 导数 $y' = 4\cos(2x)$，在 $x = 0$ 处 $y' = 4 > 0$，正在上升 ✓

**答案**：$y = 2\sin(2x) + 1$

---

**例题 3（正切函数的渐近线）**：求函数 $y = 3\tan\left(2x - \frac{\pi}{3}\right) + 1$ 的周期和在一个周期内的渐近线方程。

**解**：

**步骤 1**：求周期。对于 $\tan$，$T = \frac{\pi}{|b|} = \frac{\pi}{2}$。

**步骤 2**：求渐近线。$\tan(u)$ 在 $u = \frac{\pi}{2} + n\pi$ 处有渐近线。

令 $2x - \frac{\pi}{3} = \frac{\pi}{2} + n\pi$：

$$
2x = \frac{\pi}{2} + \frac{\pi}{3} + n\pi = \frac{3\pi}{6} + \frac{2\pi}{6} + n\pi = \frac{5\pi}{6} + n\pi
$$

$$
x = \frac{5\pi}{12} + \frac{n\pi}{2}
$$

**步骤 3**：取 $n = 0$ 和 $n = 1$（覆盖一个周期 $\frac{\pi}{2}$ 内的两条渐近线）：

$$
x = \frac{5\pi}{12},\quad x = \frac{5\pi}{12} + \frac{\pi}{2} = \frac{5\pi}{12} + \frac{6\pi}{12} = \frac{11\pi}{12}
$$

**答案**：周期为 $\dfrac{\pi}{2}$，渐近线为 $x = \dfrac{5\pi}{12} + \dfrac{n\pi}{2}$（$n \in \mathbb{Z}$）

---

**例题 4（图像变换——从 $y = \sin x$ 到 $y = 2\sin(3x) + 1$）**：描述如何通过变换 $y = \sin x$ 的图像得到 $y = 2\sin(3x) + 1$ 的图像。

**解**：

**步骤 1**：水平压缩。$y = \sin x \to y = \sin(3x)$：将周期从 $2\pi$ 压缩为 $\frac{2\pi}{3}$，频率变为原来的 $3$ 倍。

**步骤 2**：垂直拉伸。$y = \sin(3x) \to y = 2\sin(3x)$：振幅从 $1$ 变为 $2$，最大值从 $1$ 变为 $2$，最小值从 $-1$ 变为 $-2$。

**步骤 3**：垂直平移。$y = 2\sin(3x) \to y = 2\sin(3x) + 1$：整个图像向上平移 $1$ 个单位，新的中轴线为 $y = 1$。

**变换顺序**：先水平变换（周期），再垂直变换（振幅），最后垂直平移。

---

**例题 5（由图像求函数——已知点）**：一个余弦型函数 $y = a\cos(bx) + d$ 的图像经过点 $(0, 5)$ 和 $(\pi, -1)$，且周期为 $2\pi$。求 $a$、$b$、$d$ 的值。

**解**：

**步骤 1**：由周期 $T = 2\pi$ 得 $T = \frac{2\pi}{|b|} = 2\pi$，所以 $|b| = 1$，取 $b = 1$。

**步骤 2**：代入 $(0, 5)$：$y = a\cos(0) + d = a + d = 5$

**步骤 3**：代入 $(\pi, -1)$：$y = a\cos(\pi) + d = -a + d = -1$

**步骤 4**：解联立方程组：

$$
\begin{cases}
a + d = 5 \\
-a + d = -1
\end{cases}
$$

两式相加：$2d = 4 \Rightarrow d = 2$
代入第一式：$a + 2 = 5 \Rightarrow a = 3$

**答案**：$a = 3$，$b = 1$，$d = 2$，函数为 $y = 3\cos x + 2$

---

**例题 6（绘制图像要点）**：对于函数 $y = 2\sin\left(\frac{x}{2}\right) - 1$，在区间 $[0, 4\pi]$ 内：
(a) 求振幅、周期和垂直平移
(b) 写出关键点的坐标
(c) 描述绘制图像的步骤

**解**：

(a)

- 振幅：$|a| = 2$
- 周期：$T = \frac{2\pi}{|b|} = \frac{2\pi}{1/2} = 4\pi$
- 垂直平移：$d = -1$（向下 $1$ 个单位）
- 最大值：$d + |a| = -1 + 2 = 1$
- 最小值：$d - |a| = -1 - 2 = -3$
- 中轴线：$y = -1$

(b) 一个周期 $[0, 4\pi]$ 内的 $5$ 个关键点（间隔 $T/4 = \pi$）：

| $x$ | $0$ | $\pi$ | $2\pi$ | $3\pi$ | $4\pi$ |
|-----|-----|-------|--------|--------|--------|
| $\frac{x}{2}$ | $0$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
| $\sin(\frac{x}{2})$ | $0$ | $1$ | $0$ | $-1$ | $0$ |
| $y = 2\sin(\frac{x}{2}) - 1$ | $-1$ | $1$ | $-1$ | $-3$ | $-1$ |

(c) **绘制步骤**：

1. 画出中轴线 $y = -1$（虚线）
2. 标出最大值 $y = 1$ 和最小值 $y = -3$ 的水平线（虚线）
3. 标出 $5$ 个关键点：$(0, -1)$、$(\pi, 1)$、$(2\pi, -1)$、$(3\pi, -3)$、$(4\pi, -1)$
4. 用平滑的波浪线连接各点

---

**例题 7（正切图像的渐近线和关键点）**：在区间 $[0, \pi]$ 内，找出函数 $y = \tan\left(2x - \frac{\pi}{4}\right)$ 的渐近线方程和与 $x$ 轴的交点。

**解**：

**步骤 1**：求渐近线。$\tan u$ 在 $u = \frac{\pi}{2} + n\pi$ 处有渐近线。

令 $2x - \frac{\pi}{4} = \frac{\pi}{2} + n\pi$：

$$
2x = \frac{\pi}{2} + \frac{\pi}{4} + n\pi = \frac{3\pi}{4} + n\pi
$$

$$
x = \frac{3\pi}{8} + \frac{n\pi}{2}
$$

在 $[0, \pi]$ 内，$n = 0$ 和 $n = 1$：

$$
x = \frac{3\pi}{8},\quad x = \frac{3\pi}{8} + \frac{\pi}{2} = \frac{3\pi}{8} + \frac{4\pi}{8} = \frac{7\pi}{8}
$$

**步骤 2**：求与 $x$ 轴的交点。令 $y = 0$：

$$
\tan\left(2x - \frac{\pi}{4}\right) = 0
$$

$\tan u = 0$ 时 $u = n\pi$：

$$
2x - \frac{\pi}{4} = n\pi
$$

$$
2x = \frac{\pi}{4} + n\pi
$$

$$
x = \frac{\pi}{8} + \frac{n\pi}{2}
$$

在 $[0, \pi]$ 内，$n = 0$ 和 $n = 1$：

$$
x = \frac{\pi}{8},\quad x = \frac{\pi}{8} + \frac{\pi}{2} = \frac{\pi}{8} + \frac{4\pi}{8} = \frac{5\pi}{8}
$$

**答案**：渐近线为 $x = \dfrac{3\pi}{8}$ 和 $x = \dfrac{7\pi}{8}$；与 $x$ 轴交点为 $x = \dfrac{\pi}{8}$ 和 $x = \dfrac{5\pi}{8}$

---

## 8.4 三角恒等式

### 8.4.1 三个基本勾股恒等式

**恒等式一：$\sin^2\theta + \cos^2\theta = 1$**

**推导**：在单位圆上，点 $(\cos\theta, \sin\theta)$ 在圆 $x^2 + y^2 = 1$ 上，代入即得：

$$
(\cos\theta)^2 + (\sin\theta)^2 = 1
$$

即 $\sin^2\theta + \cos^2\theta = 1$。

**恒等式二：$\sec^2\theta = 1 + \tan^2\theta$**

**推导**：将 $\sin^2\theta + \cos^2\theta = 1$ 两边除以 $\cos^2\theta$（假设 $\cos\theta \neq 0$）：

$$
\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}
$$

$$
\tan^2\theta + 1 = \sec^2\theta
$$

即 $\sec^2\theta = 1 + \tan^2\theta$。

**恒等式三：$\csc^2\theta = 1 + \cot^2\theta$**

**推导**：将 $\sin^2\theta + \cos^2\theta = 1$ 两边除以 $\sin^2\theta$（假设 $\sin\theta \neq 0$）：

$$
\frac{\sin^2\theta}{\sin^2\theta} + \frac{\cos^2\theta}{\sin^2\theta} = \frac{1}{\sin^2\theta}
$$

$$
1 + \cot^2\theta = \csc^2\theta
$$

即 $\csc^2\theta = 1 + \cot^2\theta$。

> ✅ **考试提示**：这三个恒等式在考纲的**公式表**中提供，考试时可以直接引用。

### 8.4.2 二倍角公式

虽然考纲未明确列出二倍角公式，但这些公式可以从基本恒等式中推导出来，并且在解方程和证明恒等式中极为常用。

**$\sin(2\theta)$ 的推导**：

从和角公式 $\sin(A + B) = \sin A\cos B + \cos A\sin B$ 出发，令 $A = B = \theta$：

$$
\sin(2\theta) = \sin\theta\cos\theta + \cos\theta\sin\theta = 2\sin\theta\cos\theta
$$

因此：

$$
\boxed{\sin(2\theta) = 2\sin\theta\cos\theta}
$$

**$\cos(2\theta)$ 的推导**：

从和角公式 $\cos(A + B) = \cos A\cos B - \sin A\sin B$，令 $A = B = \theta$：

$$
\cos(2\theta) = \cos\theta\cos\theta - \sin\theta\sin\theta = \cos^2\theta - \sin^2\theta
$$

再利用 $\sin^2\theta + \cos^2\theta = 1$，可以得到另外两种形式：

由 $\sin^2\theta = 1 - \cos^2\theta$ 代入：

$$
\cos(2\theta) = \cos^2\theta - (1 - \cos^2\theta) = 2\cos^2\theta - 1
$$

由 $\cos^2\theta = 1 - \sin^2\theta$ 代入：

$$
\cos(2\theta) = (1 - \sin^2\theta) - \sin^2\theta = 1 - 2\sin^2\theta
$$

因此 $\cos(2\theta)$ 有三种等价形式：

$$
\boxed{\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta}
$$

**$\tan(2\theta)$ 的推导**：

从和角公式 $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A\tan B}$，令 $A = B = \theta$：

$$
\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}
$$

即：

$$
\boxed{\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}}
$$

### 8.4.3 半角公式（由二倍角公式反推）

从 $\cos(2\theta) = 2\cos^2\theta - 1$ 解出 $\cos^2\theta$：

$$
2\cos^2\theta = 1 + \cos(2\theta) \;\Rightarrow\; \boxed{\cos^2\theta = \frac{1 + \cos(2\theta)}{2}}
$$

从 $\cos(2\theta) = 1 - 2\sin^2\theta$ 解出 $\sin^2\theta$：

$$
2\sin^2\theta = 1 - \cos(2\theta) \;\Rightarrow\; \boxed{\sin^2\theta = \frac{1 - \cos(2\theta)}{2}}
$$

这两个公式在**积分**中非常重要——它们用来降低三角函数的幂次。

### 8.4.4 例题

---

**例题 1（利用恒等式求值）**：已知 $\cos\theta = \frac{3}{5}$ 且 $\theta$ 在第四象限，求 $\sin\theta$、$\tan\theta$、$\sin(2\theta)$、$\cos(2\theta)$ 的值。

**解**：

**步骤 1**：由 $\sin^2\theta + \cos^2\theta = 1$ 求 $\sin^2\theta$。

$$
\sin^2\theta = 1 - \cos^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}
$$

**步骤 2**：确定 $\sin\theta$ 的符号。$\theta$ 在第四象限，$\sin\theta < 0$。

$$
\sin\theta = -\sqrt{\frac{16}{25}} = -\frac{4}{5}
$$

**步骤 3**：求 $\tan\theta$。

$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-4/5}{3/5} = -\frac{4}{3}
$$

**步骤 4**：求 $\sin(2\theta)$。

$$
\sin(2\theta) = 2\sin\theta\cos\theta = 2 \times \left(-\frac{4}{5}\right) \times \frac{3}{5} = -\frac{24}{25}
$$

**步骤 5**：求 $\cos(2\theta)$（用 $\cos^2\theta - \sin^2\theta$ 形式）。

$$
\cos(2\theta) = \cos^2\theta - \sin^2\theta = \left(\frac{3}{5}\right)^2 - \left(-\frac{4}{5}\right)^2 = \frac{9}{25} - \frac{16}{25} = -\frac{7}{25}
$$

**答案**：$\sin\theta = -\dfrac{4}{5}$，$\tan\theta = -\dfrac{4}{3}$，$\sin(2\theta) = -\dfrac{24}{25}$，$\cos(2\theta) = -\dfrac{7}{25}$

---

**例题 2（化简表达式并用恒等式求值）**：化简 $\frac{\sin(2\theta)}{1 - \cos(2\theta)}$，并用此结果求当 $\theta = \frac{\pi}{6}$ 时的值。

**解**：

**步骤 1**：代入二倍角公式化简。

$$
\frac{\sin(2\theta)}{1 - \cos(2\theta)} = \frac{2\sin\theta\cos\theta}{1 - (1 - 2\sin^2\theta)}
$$

**步骤 2**：化简分母。

$$
1 - \cos(2\theta) = 1 - (1 - 2\sin^2\theta) = 2\sin^2\theta
$$

**步骤 3**：化简整个表达式。

$$
\frac{2\sin\theta\cos\theta}{2\sin^2\theta} = \frac{\cos\theta}{\sin\theta} = \cot\theta
$$

**步骤 4**：代入 $\theta = \frac{\pi}{6}$。

$$
\cot\frac{\pi}{6} = \frac{\cos\frac{\pi}{6}}{\sin\frac{\pi}{6}} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3}
$$

**答案**：化简结果为 $\cot\theta$，当 $\theta = \frac{\pi}{6}$ 时值为 $\sqrt{3}$

---

**例题 3（利用 $\sec^2\theta = 1 + \tan^2\theta$ 化简）**：化简 $\frac{\sec^2\theta - 1}{\sec^2\theta}$。

**解**：

**方法一**：

$$
\frac{\sec^2\theta - 1}{\sec^2\theta} = \frac{(1 + \tan^2\theta) - 1}{\sec^2\theta} = \frac{\tan^2\theta}{\sec^2\theta}
$$

因为 $\tan\theta = \frac{\sin\theta}{\cos\theta}$，$\sec\theta = \frac{1}{\cos\theta}$：

$$
\frac{\tan^2\theta}{\sec^2\theta} = \frac{\sin^2\theta/\cos^2\theta}{1/\cos^2\theta} = \sin^2\theta
$$

**方法二**（更直接）：

$$
\frac{\sec^2\theta - 1}{\sec^2\theta} = 1 - \frac{1}{\sec^2\theta} = 1 - \cos^2\theta = \sin^2\theta
$$

**答案**：$\sin^2\theta$

---

**例题 4（用 $\cos(2\theta)$ 表示 $4\sin^2\theta - 3\cos^2\theta$）**：用 $\cos(2\theta)$ 表示 $4\sin^2\theta - 3\cos^2\theta$。

**解**：

**步骤 1**：代入半角公式。

$$
\sin^2\theta = \frac{1 - \cos(2\theta)}{2}, \quad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}
$$

**步骤 2**：代入原式。

$$
4\sin^2\theta - 3\cos^2\theta = 4 \times \frac{1 - \cos(2\theta)}{2} - 3 \times \frac{1 + \cos(2\theta)}{2}
$$

**步骤 3**：化简。

$$
= 2(1 - \cos(2\theta)) - \frac{3}{2}(1 + \cos(2\theta))
$$

$$
= 2 - 2\cos(2\theta) - \frac{3}{2} - \frac{3}{2}\cos(2\theta)
$$

$$
= \left(2 - \frac{3}{2}\right) + \left(-2 - \frac{3}{2}\right)\cos(2\theta)
$$

$$
= \frac{1}{2} - \frac{7}{2}\cos(2\theta)
$$

**答案**：$\dfrac{1}{2} - \dfrac{7}{2}\cos(2\theta)$

---

**例题 5（求证恒等式并求值）**：证明 $\sin^4\theta - \cos^4\theta = \sin^2\theta - \cos^2\theta$，并由此求当 $\theta = \frac{\pi}{3}$ 时的值。

**解**：

**证明**：

左边 $= \sin^4\theta - \cos^4\theta = (\sin^2\theta)^2 - (\cos^2\theta)^2$

利用平方差公式：

$$
= (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta)
$$

因为 $\sin^2\theta + \cos^2\theta = 1$：

$$
= (\sin^2\theta - \cos^2\theta) \times 1 = \sin^2\theta - \cos^2\theta
$$

左边 $=$ 右边，恒等式得证。

**求值**：代入 $\theta = \frac{\pi}{3}$。

$$
\sin^2\frac{\pi}{3} - \cos^2\frac{\pi}{3} = \left(\frac{\sqrt{3}}{2}\right)^2 - \left(\frac{1}{2}\right)^2 = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}
$$

**答案**：恒等式得证，$\theta = \frac{\pi}{3}$ 时值为 $\frac{1}{2}$

---

**例题 6（利用 $\csc^2\theta = 1 + \cot^2\theta$ 解方程的准备）**：化简表达式 $\frac{\csc^2\theta - \cot^2\theta}{\csc^2\theta}$。

**解**：

**步骤 1**：由 $\csc^2\theta = 1 + \cot^2\theta$ 得 $\csc^2\theta - \cot^2\theta = 1$。

**步骤 2**：代入原式。

$$
\frac{\csc^2\theta - \cot^2\theta}{\csc^2\theta} = \frac{1}{\csc^2\theta} = \sin^2\theta
$$

**答案**：$\sin^2\theta$

---



## 8.5 解三角方程

### 8.5.1 解题总策略（复习）

解三角方程的核心流程如下：

```
原方程
   │
   ▼
是否含不同名的函数？──是──→ 用恒等式化为同名函数
   │                               │
   否                               ▼
   │                           化简后的方程
   ▼                               │
化为基本形式：sin x = k,            │
cos x = k, tan x = k               │
   │                               │
   ▼                               ▼
求参考角 α
   │
   ▼
根据 k 的符号确定解所在象限（对 tan 直接加周期）
   │
   ▼
写出给定区间内的所有解
   │
   ▼
检查定义域，排除无效解
```

> **核心思想**：无论多复杂的三角方程，最终目标都是通过恒等变换和代数运算，将其化简为一个或多个基本形式（$\sin x = k$、$\cos x = k$、$\tan x = k$），然后利用参考角法系统性地求出所有解。

---

### 8.5.2 基本形式 $\sin x = k$（$-1 \leq k \leq 1$）

#### 几何推导——从单位圆理解

在单位圆上，$\sin\theta = y$ 表示终边与单位圆交点的纵坐标。因此，方程 $\sin x = k$ 等价于：**在单位圆上，寻找终边与水平线 $y = k$ 相交的所有角度 $x$**。

**情形一**：当 $0 < k < 1$ 时。

水平线 $y = k$ 与单位圆相交于两个点（对称于 $y$ 轴）：
- 一个在第一象限，对应的角为 $\alpha$（锐角）
- 另一个在第二象限，对应的角为 $\pi - \alpha$

为什么第二象限的解是 $\pi - \alpha$？

我们可以用诱导公式来理解。在单位圆上，角 $\pi - \alpha$ 的终边与角 $\alpha$ 的终边关于 $y$ 轴对称。因此，它们的 $y$ 坐标相同：

$$
\sin(\pi - \alpha) = \sin\alpha
$$

当 $\sin\alpha = |k|$ 时，$\sin(\pi - \alpha) = |k|$。而 $k > 0$，所以 $\sin(\pi - \alpha) = k$。

**情形二**：当 $-1 < k < 0$ 时。

水平线 $y = k$ 位于 $x$ 轴下方，同样与单位圆相交于两个点：
- 一个在第三象限，对应的角为 $\pi + \alpha$
- 另一个在第四象限，对应的角为 $2\pi - \alpha$

**推导 $\pi + \alpha$**：角 $\pi + \alpha$ 的终边与角 $\alpha$ 的终边关于原点对称。因此：

$$
\sin(\pi + \alpha) = -\sin\alpha = -|k|
$$

由于 $k < 0$，$-|k| = k$，所以 $\sin(\pi + \alpha) = k$。

**推导 $2\pi - \alpha$**：角 $2\pi - \alpha$ 的终边与角 $\alpha$ 的终边关于 $x$ 轴对称：

$$
\sin(2\pi - \alpha) = -\sin\alpha = -|k| = k
$$

#### 完整的解法步骤

**步骤 1**：检查可行性。确认 $|k| \leq 1$。若 $|k| > 1$，则方程无解（因为 $\sin$ 的值域为 $[-1, 1]$）。

**步骤 2**：求参考角。

$$
\alpha = \arcsin(|k|), \quad \alpha \in \left[0, \frac{\pi}{2}\right]
$$

参考角 $\alpha$ 是一个介于 $0$ 和 $\frac{\pi}{2}$ 之间的锐角（或边界角），表示终边与 $x$ 轴之间的最小夹角。

**步骤 3**：根据 $k$ 的符号确定解所在的象限。

| $k$ 的符号 | 解所在的象限 | 对应的角 |
|-----------|-------------|---------|
| $k > 0$ | 第一、第二象限 | $x = \alpha$, $x = \pi - \alpha$ |
| $k = 0$ | $x$ 轴正负方向 | $x = 0$, $x = \pi$（在 $[0, 2\pi)$ 内） |
| $k < 0$ | 第三、第四象限 | $x = \pi + \alpha$, $x = 2\pi - \alpha$ |

**步骤 4**：写出通解。由于 $\sin$ 的周期为 $2\pi$，所有解可表示为：

$$
x = x_0 + 2n\pi, \quad n \in \mathbb{Z}
$$

其中 $x_0$ 是步骤 3 中求出的基本解。

#### 特殊情况

**(a) $k = 0$**：$\sin x = 0$ 的解。

在 $[0, 2\pi)$ 内，$\sin x = 0$ 发生在 $x = 0$ 和 $x = \pi$。通解为：

$$
x = n\pi, \quad n \in \mathbb{Z}
$$

**(b) $k = 1$**：$\sin x = 1$ 的解。

在 $[0, 2\pi)$ 内，$\sin x = 1$ 只在 $x = \frac{\pi}{2}$ 处成立。通解为：

$$
x = \frac{\pi}{2} + 2n\pi, \quad n \in \mathbb{Z}
$$

**(c) $k = -1$**：$\sin x = -1$ 的解。

在 $[0, 2\pi)$ 内，$\sin x = -1$ 只在 $x = \frac{3\pi}{2}$ 处成立。通解为：

$$
x = \frac{3\pi}{2} + 2n\pi, \quad n \in \mathbb{Z}
$$

#### 例题

---

**例题 1（$\sin x = k$，$k > 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = \frac{\sqrt{3}}{2}$。

**解**：

**步骤 1**：确认可行性。$\frac{\sqrt{3}}{2} \approx 0.866 \leq 1$，有解。

**步骤 2**：求参考角。$\alpha = \arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$。

**步骤 3**：$k = \frac{\sqrt{3}}{2} > 0$，解在第一和第二象限。

第一象限：$x = \alpha = \dfrac{\pi}{3}$

第二象限：$x = \pi - \alpha = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

**步骤 4**：验证。$\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ ✓，$\sin\frac{2\pi}{3} = \sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ ✓

**答案**：$x = \dfrac{\pi}{3}$ 和 $x = \dfrac{2\pi}{3}$

---

**例题 2（$\sin x = k$，$k < 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = -\frac{1}{2}$。

**解**：

**步骤 1**：确认可行性。$\left|-\frac{1}{2}\right| = \frac{1}{2} \leq 1$，有解。

**步骤 2**：求参考角。$\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

**步骤 3**：$k = -\frac{1}{2} < 0$，解在第三和第四象限。

第三象限：$x = \pi + \alpha = \pi + \dfrac{\pi}{6} = \dfrac{7\pi}{6}$

第四象限：$x = 2\pi - \alpha = 2\pi - \dfrac{\pi}{6} = \dfrac{11\pi}{6}$

**步骤 4**：验证。$\sin\frac{7\pi}{6} = -\sin\frac{\pi}{6} = -\frac{1}{2}$ ✓，$\sin\frac{11\pi}{6} = -\sin\frac{\pi}{6} = -\frac{1}{2}$ ✓

**答案**：$x = \dfrac{7\pi}{6}$ 和 $x = \dfrac{11\pi}{6}$

---

**例题 3（$\sin x = k$，通解形式）**：求方程 $\sin x = \frac{\sqrt{2}}{2}$ 的通解。

**解**：

**步骤 1**：参考角 $\alpha = \arcsin\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4}$。

**步骤 2**：$k > 0$，基本解为：

$$
x_1 = \frac{\pi}{4}, \quad x_2 = \pi - \frac{\pi}{4} = \frac{3\pi}{4}
$$

**步骤 3**：通解为基本解加上 $2\pi$ 的整数倍：

$$
x = \frac{\pi}{4} + 2n\pi \quad \text{或} \quad x = \frac{3\pi}{4} + 2n\pi, \quad n \in \mathbb{Z}
$$

**答案**：$x = \dfrac{\pi}{4} + 2n\pi$ 或 $x = \dfrac{3\pi}{4} + 2n\pi$（$n \in \mathbb{Z}$）

---

**例题 4（$\sin x = k$，$k = 0$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = 0$。

**解**：

**方法一（单位圆法）**：在单位圆上，$\sin x = 0$ 意味着 $y = 0$，即终边在 $x$ 轴上。在 $[0, 2\pi)$ 内，$x = 0$ 和 $x = \pi$。

**方法二（参考角法）**：$k = 0$，参考角 $\alpha = 0$。

- 在 $x$ 轴正半轴（可视为第一和第四象限的交界）：$x = 0$
- 在 $x$ 轴负半轴（可视为第二和第三象限的交界）：$x = \pi$

**答案**：$x = 0$ 和 $x = \pi$

---

**例题 5（$\sin x = k$，$k = \pm 1$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = -1$。

**解**：

在单位圆上，$\sin x = -1$ 意味着 $y = -1$，即终边与负 $y$ 轴重合。

在 $[0, 2\pi)$ 内，只有 $x = \frac{3\pi}{2}$ 满足条件。

**验证**：$\sin\frac{3\pi}{2} = -1$ ✓

**答案**：$x = \dfrac{3\pi}{2}$

---

**例题 6（$\sin x = k$，非特殊角）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = 0.4$，结果保留三位有效数字。

**解**：

**步骤 1**：$0.4 \leq 1$，有解。

**步骤 2**：求参考角。使用计算器（弧度模式）：

$$
\alpha = \arcsin(0.4) \approx 0.4115 \text{ 弧度}
$$

**步骤 3**：$k = 0.4 > 0$，解在第一和第二象限。

第一象限：$x_1 = \alpha \approx 0.412$

第二象限：$x_2 = \pi - \alpha \approx 3.1416 - 0.4115 = 2.7301 \approx 2.73$

**答案**：$x \approx 0.412$ 和 $x \approx 2.73$（三位有效数字）

---

### 8.5.3 基本形式 $\cos x = k$（$-1 \leq k \leq 1$）

#### 几何推导——从单位圆理解

在单位圆上，$\cos\theta = x$ 表示终边与单位圆交点的横坐标。方程 $\cos x = k$ 等价于：**在单位圆上，寻找终边与竖直线 $x = k$ 相交的所有角度 $x$**。

**情形一**：当 $0 < k < 1$ 时。

竖直线 $x = k$ 与单位圆相交于两个点（对称于 $x$ 轴）：
- 一个在第一象限，对应的角为 $\alpha$（锐角）
- 另一个在第四象限，对应的角为 $2\pi - \alpha$（或 $-\alpha$）

**推导 $2\pi - \alpha$**：角 $2\pi - \alpha$ 的终边与角 $\alpha$ 的终边关于 $x$ 轴对称：

$$
\cos(2\pi - \alpha) = \cos\alpha = |k|
$$

由于 $\cos$ 在第四象限为正，$\cos(2\pi - \alpha) = |k| = k$。

**情形二**：当 $-1 < k < 0$ 时。

竖直线 $x = k$（位于 $y$ 轴左侧）与单位圆相交于两点：
- 一个在第二象限，对应的角为 $\pi - \alpha$
- 另一个在第三象限，对应的角为 $\pi + \alpha$

**推导 $\pi - \alpha$**：角 $\pi - \alpha$ 的终边与角 $\alpha$ 的终边关于 $y$ 轴对称：

$$
\cos(\pi - \alpha) = -\cos\alpha = -|k|
$$

由于 $k < 0$，$-|k| = k$，所以 $\cos(\pi - \alpha) = k$。

**推导 $\pi + \alpha$**：角 $\pi + \alpha$ 的终边与角 $\alpha$ 的终边关于原点对称：

$$
\cos(\pi + \alpha) = -\cos\alpha = -|k| = k
$$

#### 完整的解法步骤

**步骤 1**：检查可行性。确认 $|k| \leq 1$。

**步骤 2**：求参考角。

$$
\alpha = \arccos(|k|), \quad \alpha \in [0, \pi]
$$

注意：$\arccos$ 的值域是 $[0, \pi]$，这与 $\arcsin$ 不同。因此 $\alpha$ 直接取 $\arccos(|k|)$，它一定在 $[0, \pi]$ 内。

**步骤 3**：根据 $k$ 的符号确定解所在的象限。

| $k$ 的符号 | 解所在的象限 | 对应的角 |
|-----------|-------------|---------|
| $k > 0$ | 第一、第四象限 | $x = \alpha$, $x = 2\pi - \alpha$ |
| $k = 0$ | $y$ 轴正负方向 | $x = \frac{\pi}{2}$, $x = \frac{3\pi}{2}$（在 $[0, 2\pi)$ 内） |
| $k < 0$ | 第二、第三象限 | $x = \pi - \alpha$, $x = \pi + \alpha$ |

**步骤 4**：写出通解。由于 $\cos$ 的周期为 $2\pi$，一个简洁的通解形式为：

$$
x = \pm\alpha + 2n\pi, \quad n \in \mathbb{Z}
$$

其中：
- 取 $+$ 号时对应第一象限（或第二象限，取决于 $k$ 的符号）
- 取 $-$ 号时对应第四象限（或第三象限）

#### 特殊情况

**(a) $k = 0$**：$\cos x = 0$ 的解。

在 $[0, 2\pi)$ 内，$\cos x = 0$ 发生在 $x = \frac{\pi}{2}$ 和 $x = \frac{3\pi}{2}$。通解为：

$$
x = \frac{\pi}{2} + n\pi, \quad n \in \mathbb{Z}
$$

**(b) $k = 1$**：$\cos x = 1$ 的解。

在 $[0, 2\pi)$ 内，$\cos x = 1$ 只在 $x = 0$ 处成立。通解为：

$$
x = 2n\pi, \quad n \in \mathbb{Z}
$$

**(c) $k = -1$**：$\cos x = -1$ 的解。

在 $[0, 2\pi)$ 内，$\cos x = -1$ 只在 $x = \pi$ 处成立。通解为：

$$
x = \pi + 2n\pi = (2n + 1)\pi, \quad n \in \mathbb{Z}
$$

#### 对比 $\sin$ 和 $\cos$ 的解分布

| | $\sin x = k$ | $\cos x = k$ |
|--|-------------|-------------|
| $k > 0$ | 第一、二象限：$\alpha$, $\pi - \alpha$ | 第一、四象限：$\alpha$, $2\pi - \alpha$ |
| $k < 0$ | 第三、四象限：$\pi + \alpha$, $2\pi - \alpha$ | 第二、三象限：$\pi - \alpha$, $\pi + \alpha$ |
| 周期 | $2\pi$ | $2\pi$ |
| 通解简洁形式 | $x = n\pi + (-1)^n\alpha$ | $x = \pm\alpha + 2n\pi$ |

> **记忆技巧**：$\sin$ 的正解在"上"（第一、二象限），$\cos$ 的正解在"右"（第一、四象限）。这个"上"和"右"对应了单位圆上 $y$ 和 $x$ 坐标为正的区域。

#### 例题

---

**例题 1（$\cos x = k$，$k > 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = \frac{\sqrt{2}}{2}$。

**解**：

**步骤 1**：确认可行性。$\frac{\sqrt{2}}{2} \leq 1$，有解。

**步骤 2**：求参考角。$\alpha = \arccos\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4}$。

注意这里直接得到 $\alpha = \frac{\pi}{4}$ 而不是 $\frac{\pi}{4}$……实际上 $\arccos(\frac{\sqrt{2}}{2}) = \frac{\pi}{4}$，因为 $\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$。

**步骤 3**：$k = \frac{\sqrt{2}}{2} > 0$，解在第一和第四象限。

第一象限：$x = \alpha = \dfrac{\pi}{4}$

第四象限：$x = 2\pi - \alpha = 2\pi - \dfrac{\pi}{4} = \dfrac{8\pi}{4} - \dfrac{\pi}{4} = \dfrac{7\pi}{4}$

**步骤 4**：验证。$\cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ ✓，$\cos\frac{7\pi}{4} = \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$ ✓

**答案**：$x = \dfrac{\pi}{4}$ 和 $x = \dfrac{7\pi}{4}$

---

**例题 2（$\cos x = k$，$k < 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = -\frac{1}{2}$。

**解**：

**步骤 1**：$|-\frac{1}{2}| = \frac{1}{2} \leq 1$，有解。

**步骤 2**：求参考角。$\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$。

**步骤 3**：$k = -\frac{1}{2} < 0$，解在第二和第三象限。

第二象限：$x = \pi - \alpha = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

第三象限：$x = \pi + \alpha = \pi + \dfrac{\pi}{3} = \dfrac{4\pi}{3}$

**步骤 4**：验证。$\cos\frac{2\pi}{3} = -\cos\frac{\pi}{3} = -\frac{1}{2}$ ✓，$\cos\frac{4\pi}{3} = -\cos\frac{\pi}{3} = -\frac{1}{2}$ ✓

**答案**：$x = \dfrac{2\pi}{3}$ 和 $x = \dfrac{4\pi}{3}$

---

**例题 3（$\cos x = k$，通解形式）**：求方程 $\cos x = \frac{\sqrt{3}}{2}$ 的通解。

**解**：

**步骤 1**：参考角 $\alpha = \arccos\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{6}$。

**步骤 2**：$k > 0$，基本解为：

$$
x_1 = \frac{\pi}{6}, \quad x_2 = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}
$$

**步骤 3**：通解为：

$$
x = \pm\frac{\pi}{6} + 2n\pi, \quad n \in \mathbb{Z}
$$

其中 $x = \frac{\pi}{6} + 2n\pi$ 对应第一象限的解，$x = -\frac{\pi}{6} + 2n\pi$ 对应第四象限的解。

**答案**：$x = \pm\dfrac{\pi}{6} + 2n\pi$（$n \in \mathbb{Z}$）

---

**例题 4（$\cos x = k$，$k = 0$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = 0$。

**解**：

**方法一（单位圆法）**：$\cos x = 0$ 意味着 $x = 0$，即终边在 $y$ 轴上。在 $[0, 2\pi)$ 内，$x = \frac{\pi}{2}$ 和 $x = \frac{3\pi}{2}$。

**方法二（参考角法）**：$\alpha = \arccos(0) = \frac{\pi}{2}$。

由于 $k = 0$，解在第二象限和第三象限之间（即 $y$ 轴正方向和负方向）：

$x = \frac{\pi}{2}$ 和 $x = \pi + \frac{\pi}{2} = \frac{3\pi}{2}$

或者直接用通解：$x = \frac{\pi}{2} + n\pi$，在 $[0, 2\pi)$ 内取 $n = 0, 1$。

**答案**：$x = \dfrac{\pi}{2}$ 和 $x = \dfrac{3\pi}{2}$

---

**例题 5（$\cos x = k$，$k = -1$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = -1$。

**解**：

在单位圆上，$\cos x = -1$ 意味着 $x = -1$，即终边与负 $x$ 轴重合。

在 $[0, 2\pi)$ 内，只有 $x = \pi$ 满足条件。

**验证**：$\cos\pi = -1$ ✓

**答案**：$x = \pi$

---

**例题 6（$\cos x = k$，非特殊角）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = 0.6$，结果保留三位有效数字。

**解**：

**步骤 1**：$0.6 \leq 1$，有解。

**步骤 2**：求参考角。使用计算器（弧度模式）：

$$
\alpha = \arccos(0.6) \approx 0.9273 \text{ 弧度}
$$

**步骤 3**：$k = 0.6 > 0$，解在第一和第四象限。

第一象限：$x_1 = \alpha \approx 0.927$

第四象限：$x_2 = 2\pi - \alpha \approx 6.2832 - 0.9273 = 5.3559 \approx 5.36$

**答案**：$x \approx 0.927$ 和 $x \approx 5.36$（三位有效数字）

---

**例题 7（$\cos$ 和 $\sin$ 的对比）**：比较方程 $\sin x = \frac{\sqrt{3}}{2}$ 和 $\cos x = \frac{\sqrt{3}}{2}$ 在 $[0, 2\pi)$ 内的解。

**解**：

$\frac{\sqrt{3}}{2} \approx 0.866$，参考角 $\alpha = \frac{\pi}{6}$（因为 $\sin\frac{\pi}{6} = \frac{1}{2}$……等等，$\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$，$\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$）。

所以对 $\sin x = \frac{\sqrt{3}}{2}$：$\alpha = \frac{\pi}{3}$

对 $\cos x = \frac{\sqrt{3}}{2}$：$\alpha = \frac{\pi}{6}$

| 方程 | 参考角 $\alpha$ | 解（$[0, 2\pi)$） |
|-----|---------------|------------------|
| $\sin x = \frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{3}$, $\frac{2\pi}{3}$ |
| $\cos x = \frac{\sqrt{3}}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{6}$, $\frac{11\pi}{6}$ |

**启示**：$\sin$ 和 $\cos$ 的解分布模式不同，需要注意区分。

---

### 8.5.4 基本形式 $\tan x = k$（$k \in \mathbb{R}$）

#### 与 $\sin$ 和 $\cos$ 的本质区别

正切函数 $\tan x = \frac{\sin x}{\cos x}$ 有三个重要特性，使得解 $\tan x = k$ 的方式与 $\sin$ 和 $\cos$ 不同：

1. **值域为全体实数**：$k$ 可以取任意实数值，没有 $-1$ 到 $1$ 的限制
2. **周期为 $\pi$（而不是 $2\pi$）**：$\tan(x + \pi) = \tan x$，因此每隔 $\pi$ 重复一次
3. **有垂直渐近线**：在 $x = \frac{\pi}{2} + n\pi$ 处 $\tan x$ 无定义

#### 几何推导——从单位圆理解

在单位圆上，$\tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}$。从几何角度看，$\tan\theta$ 也可以看作是**过点 $(1, 0)$ 的竖直线与终边延长线的交点**的纵坐标。

方程 $\tan x = k$ 意味着寻找终边使得 $\frac{y}{x} = k$，即 $y = kx$。这等价于寻找终边与直线 $y = kx$ 重合（或反向重合）的所有角度。

**关键观察**：如果 $\tan\alpha = k$（$\alpha$ 为锐角），那么：
- 在第一象限，$x = \alpha$ 满足条件
- 在第三象限，$x = \pi + \alpha$ 也满足条件，因为 $\frac{y}{x}$ 的比值相同
- 更一般地，$x = \alpha + n\pi$ 全部满足条件

这正是 $\tan$ 周期为 $\pi$ 的几何体现。

#### 完整的解法步骤

**步骤 1**：求参考角。

$$
\alpha = \arctan(|k|), \quad \alpha \in \left(0, \frac{\pi}{2}\right)
$$

**步骤 2**：确定主值（principal value）。

如果不需要分象限讨论，可以直接使用计算器求出 $\arctan(k)$ 的主值（在 $-\frac{\pi}{2}$ 到 $\frac{\pi}{2}$ 之间），然后加上 $\pi$ 的整数倍。

**步骤 3**：写出通解。

$$
x = \arctan(k) + n\pi, \quad n \in \mathbb{Z}
$$

或者，如果使用参考角 $\alpha$ 和象限法：
- $k > 0$：第一象限 $x = \alpha$，第三象限 $x = \pi + \alpha$，通解 $x = \alpha + n\pi$
- $k < 0$：第二象限 $x = \pi - \alpha$，第四象限 $x = 2\pi - \alpha$，通解 $x = -\alpha + n\pi$（或 $x = \pi - \alpha + n\pi$）

**简化提示**：直接使用 $x = \arctan(k) + n\pi$ 是最简洁的方法，不需要分象限讨论。

#### 定义域检查

$\tan x$ 在 $x = \frac{\pi}{2} + n\pi$ 处无定义。如果解恰好等于这些值（理论上不会，因为 $\tan$ 在这些点趋向无穷大），需要排除。

#### 特殊情况

**(a) $k = 0$**：$\tan x = 0$ 的解。

$\tan x = 0$ 发生在 $\sin x = 0$ 且 $\cos x \neq 0$ 时，即 $x = n\pi$。

在 $[0, 2\pi)$ 内：$x = 0$，$x = \pi$。

**(b) $k$ 不存在（$\tan x$ 无定义）**：当 $x = \frac{\pi}{2} + n\pi$ 时，$\tan x$ 无定义，$\cos x = 0$。这种情况不包含在 $\tan x = k$ 的解中。

#### 例题

---

**例题 1（$\tan x = k$，$k > 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = \sqrt{3}$。

**解**：

**方法一（参考角法）**：

**步骤 1**：$\alpha = \arctan(\sqrt{3}) = \frac{\pi}{3}$。

**步骤 2**：$k = \sqrt{3} > 0$，通解为 $x = \frac{\pi}{3} + n\pi$。

**步骤 3**：在 $[0, 2\pi)$ 内，取 $n = 0, 1$：

$$
x = \frac{\pi}{3}, \quad x = \frac{\pi}{3} + \pi = \frac{4\pi}{3}
$$

**方法二（直接主值法）**：

$\arctan(\sqrt{3}) = \frac{\pi}{3}$，通解 $x = \frac{\pi}{3} + n\pi$，在 $[0, 2\pi)$ 内取 $n = 0, 1$。

**步骤 4**：验证。$\tan\frac{\pi}{3} = \sqrt{3}$ ✓，$\tan\frac{4\pi}{3} = \tan\frac{\pi}{3} = \sqrt{3}$ ✓

**答案**：$x = \dfrac{\pi}{3}$ 和 $x = \dfrac{4\pi}{3}$

---

**例题 2（$\tan x = k$，$k < 0$ 标准情形）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = -1$。

**解**：

**方法一（参考角法）**：

**步骤 1**：$\alpha = \arctan(1) = \frac{\pi}{4}$。

**步骤 2**：$k = -1 < 0$，解在第二和第四象限。

第二象限：$x = \pi - \alpha = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$

第四象限：$x = 2\pi - \alpha = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}$

通解：$x = \frac{3\pi}{4} + n\pi$ 或 $x = -\frac{\pi}{4} + n\pi$。

**方法二（直接主值法）**：

$\arctan(-1) = -\frac{\pi}{4}$，通解 $x = -\frac{\pi}{4} + n\pi$。

在 $[0, 2\pi)$ 内，取 $n = 1, 2$：

$$
x = -\frac{\pi}{4} + \pi = \frac{3\pi}{4}, \quad x = -\frac{\pi}{4} + 2\pi = \frac{7\pi}{4}
$$

**步骤 3**：验证。$\tan\frac{3\pi}{4} = -1$ ✓，$\tan\frac{7\pi}{4} = -1$ ✓

**答案**：$x = \dfrac{3\pi}{4}$ 和 $x = \dfrac{7\pi}{4}$

---

**例题 3（$\tan x = k$，$k = 0$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = 0$。

**解**：

**方法一**：$\tan x = 0$ 意味着 $\sin x = 0$ 且 $\cos x \neq 0$。

$\sin x = 0$ 在 $[0, 2\pi)$ 内的解为 $x = 0$ 和 $x = \pi$。

检查 $\cos x$：$\cos 0 = 1 \neq 0$ ✓，$\cos\pi = -1 \neq 0$ ✓

**方法二**：$\arctan(0) = 0$，通解 $x = 0 + n\pi = n\pi$。

在 $[0, 2\pi)$ 内：$x = 0$，$x = \pi$。

**答案**：$x = 0$ 和 $x = \pi$

---

**例题 4（$\tan x = k$，确认解不包括渐近线）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = 2$，结果保留三位有效数字。

**解**：

**步骤 1**：求主值。使用计算器（弧度模式）：

$$
\arctan(2) \approx 1.1071 \text{ 弧度}
$$

**步骤 2**：通解 $x = 1.1071 + n\pi$。

在 $[0, 2\pi)$ 内：

| $n$ | $x$ | 是否在 $[0, 2\pi)$ |
|-----|-----|-------------------|
| $0$ | $1.1071$ | ✓ |
| $1$ | $1.1071 + \pi \approx 4.2487$ | ✓ |
| $2$ | $1.1071 + 2\pi \approx 7.3903$ | ✗（$\geq 2\pi$） |

**步骤 3**：检查定义域。$\tan x$ 的渐近线在 $x = \frac{\pi}{2} \approx 1.5708$ 和 $x = \frac{3\pi}{2} \approx 4.7124$。两个解 $1.1071$ 和 $4.2487$ 均不在渐近线上。

**答案**：$x \approx 1.11$ 和 $x \approx 4.25$（三位有效数字）

---

**例题 5（$\tan x = k$，非特殊角负值）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = -0.5$，结果保留三位有效数字。

**解**：

**步骤 1**：求主值。

$$
\arctan(-0.5) \approx -0.4636 \text{ 弧度}
$$

**步骤 2**：通解 $x = -0.4636 + n\pi$。

在 $[0, 2\pi)$ 内：

| $n$ | $x$ | 是否在 $[0, 2\pi)$ |
|-----|-----|-------------------|
| $1$ | $-0.4636 + \pi \approx 2.6780$ | ✓ |
| $2$ | $-0.4636 + 2\pi \approx 5.8196$ | ✓ |
| $0$ | $-0.4636$ | ✗ |
| $3$ | $-0.4636 + 3\pi \approx 8.9612$ | ✗ |

**步骤 3**：检查渐近线。$x = 2.6780$ 和 $x = 5.8196$ 均不在 $\frac{\pi}{2} \approx 1.5708$ 或 $\frac{3\pi}{2} \approx 4.7124$ 附近。

**答案**：$x \approx 2.68$ 和 $x \approx 5.82$（三位有效数字）

---

**例题 6（三种基本形式的对比总结）**：在 $0 \leq x < 2\pi$ 范围内，分别解以下三个方程，并对比解的数量和分布：
(a) $\sin x = \frac{1}{2}$
(b) $\cos x = \frac{1}{2}$
(c) $\tan x = \frac{1}{2}$

**解**：

**(a) $\sin x = \frac{1}{2}$**

参考角 $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

$k > 0$，第一、二象限：$x = \frac{\pi}{6}$，$x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$

**2 个解**。

**(b) $\cos x = \frac{1}{2}$**

参考角 $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$。

$k > 0$，第一、四象限：$x = \frac{\pi}{3}$，$x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$

**2 个解**。

**(c) $\tan x = \frac{1}{2}$**

$\arctan\left(\frac{1}{2}\right) \approx 0.4636$，通解 $x = 0.4636 + n\pi$。

在 $[0, 2\pi)$ 内：$n = 0$ 得 $0.4636$，$n = 1$ 得 $0.4636 + \pi \approx 3.6052$。

**2 个解**。

**对比总结**：

| 方程 | 参考角 | 解（弧度） | 解的数量 |
|------|-------|-----------|---------|
| $\sin x = \frac{1}{2}$ | $\frac{\pi}{6}$ | $\frac{\pi}{6}$, $\frac{5\pi}{6}$ | 2 |
| $\cos x = \frac{1}{2}$ | $\frac{\pi}{3}$ | $\frac{\pi}{3}$, $\frac{5\pi}{3}$ | 2 |
| $\tan x = \frac{1}{2}$ | $0.4636$ | $0.4636$, $3.6052$ | 2 |

在 $[0, 2\pi)$ 内，三种基本形式均有 2 个解（除非 $k = \pm 1$ 或 $k = 0$ 等特殊情况）。

---

### 8.5.5 含 $\sec$、$\csc$、$\cot$ 的基本方程

$\sec x$、$\csc x$、$\cot x$ 分别是 $\cos x$、$\sin x$、$\tan x$ 的倒数。解这类方程时，通常先取倒数转化为基本形式，但需要额外注意**定义域**。

#### 转化方法

| 方程形式 | 转化步骤 | 注意 |
|---------|---------|------|
| $\sec x = k$ | $\cos x = \frac{1}{k}$ | $k \neq 0$；$\cos x \neq 0$ |
| $\csc x = k$ | $\sin x = \frac{1}{k}$ | $k \neq 0$；$\sin x \neq 0$ |
| $\cot x = k$ | $\tan x = \frac{1}{k}$ | $k \neq 0$；$\sin x \neq 0$ |

#### 例题

---

**例题 1（$\sec x = k$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sec x = 2$。

**解**：

**步骤 1**：转化为 $\cos x$。$\sec x = \frac{1}{\cos x} = 2$，所以 $\cos x = \frac{1}{2}$。

**步骤 2**：解 $\cos x = \frac{1}{2}$。

参考角 $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$。

$k > 0$，第一和第四象限：

$$
x = \frac{\pi}{3}, \quad x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}
$$

**步骤 3**：检查定义域。$\sec x$ 在 $\cos x = 0$ 处无定义。两个解均使 $\cos x = \frac{1}{2} \neq 0$，有效。

**答案**：$x = \dfrac{\pi}{3}$ 和 $x = \dfrac{5\pi}{3}$

---

**例题 2（$\csc x = k$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\csc x = -2$。

**解**：

**步骤 1**：$\csc x = \frac{1}{\sin x} = -2$，所以 $\sin x = -\frac{1}{2}$。

**步骤 2**：解 $\sin x = -\frac{1}{2}$。

参考角 $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

$k < 0$，第三和第四象限：

$$
x = \pi + \frac{\pi}{6} = \frac{7\pi}{6}, \quad x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}
$$

**步骤 3**：检查定义域。$\csc x$ 在 $\sin x = 0$ 处无定义。两个解均使 $\sin x = -\frac{1}{2} \neq 0$，有效。

**答案**：$x = \dfrac{7\pi}{6}$ 和 $x = \dfrac{11\pi}{6}$

---

**例题 3（$\cot x = k$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cot x = \sqrt{3}$。

**解**：

**步骤 1**：$\cot x = \frac{1}{\tan x} = \sqrt{3}$，所以 $\tan x = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$。

**步骤 2**：解 $\tan x = \frac{\sqrt{3}}{3}$。

$\arctan\left(\frac{\sqrt{3}}{3}\right) = \frac{\pi}{6}$，通解 $x = \frac{\pi}{6} + n\pi$。

在 $[0, 2\pi)$ 内：

$$
x = \frac{\pi}{6}, \quad x = \frac{\pi}{6} + \pi = \frac{7\pi}{6}
$$

**步骤 3**：检查定义域。$\cot x$ 在 $\sin x = 0$ 处无定义。两个解均使 $\sin x \neq 0$，有效。

**答案**：$x = \dfrac{\pi}{6}$ 和 $x = \dfrac{7\pi}{6}$

---

**例题 4（$\csc x = k$，$k = 1$ 特殊情况）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\csc x = 1$。

**解**：

**步骤 1**：$\csc x = \frac{1}{\sin x} = 1$，所以 $\sin x = 1$。

**步骤 2**：解 $\sin x = 1$。在 $[0, 2\pi)$ 内，$x = \frac{\pi}{2}$。

**步骤 3**：检查定义域。$\csc x$ 在 $\sin x = 0$ 处无定义。$x = \frac{\pi}{2}$ 使 $\sin x = 1 \neq 0$，有效。

**答案**：$x = \dfrac{\pi}{2}$

---

### 8.5.6 运用恒等式的方程（考纲重点）

当方程中包含不同名的三角函数或高次项时，需要先用恒等式统一函数名称或降低次数。这是考纲中明确要求的重点内容。

#### 常见转化策略大全

| 方程特征 | 转化方法 | 示例 |
|---------|---------|------|
| 含 $\tan$ 和 $\sec$ | 用 $\sec^2 = 1 + \tan^2$ 化为单一变量 | $2\sec^2 x + \tan x - 3 = 0$ |
| 含 $\cot$ 和 $\csc$ | 用 $\csc^2 = 1 + \cot^2$ 化为单一变量 | $3\csc^2 x - 2\cot^2 x = 4$ |
| 含 $\cot$ 和 $\tan$ | 用 $\cot = \frac{1}{\tan}$ 相互转化 | $4\cot\theta = \tan\theta$ |
| $a\sin(k\theta) + b\cos(k\theta) = 0$ | 两边除以 $\cos(k\theta)$ 得 $\tan(k\theta) = -\frac{b}{a}$ | $5\sin 3\theta + 2\cos 3\theta = 0$ |
| 含 $\sin^2$ 和 $\cos^2$ | 用 $\sin^2 + \cos^2 = 1$ 消去一个变量 | $\sin^2 x + \cos x = 1$ |
| 含 $\sin(2\theta)$ 或 $\cos(2\theta)$ | 用二倍角公式展开或降次 | $\cos 2\theta + \sin\theta = 0$ |
| 含 $\csc^2(\frac{\theta}{2})$ 等复合角 | 换元 $u = \frac{\theta}{2}$ | $3\csc^2(\frac{\theta}{2}) = 4$ |

#### 详细推导与例题

---

**类型一：$\cot$ 与 $\tan$ 互化**

**例题 1**（考纲举例）：在 $0 \leq \theta < 2\pi$ 范围内解方程 $4\cot\theta = \tan\theta$。

**分析**：方程两边含有 $\cot$ 和 $\tan$，它们是倒数关系。我们可以用 $\cot\theta = \frac{1}{\tan\theta}$ 将它们统一为 $\tan$。

**解**：

**步骤 1**：代入 $\cot\theta = \frac{1}{\tan\theta}$。

$$
4 \times \frac{1}{\tan\theta} = \tan\theta
$$

**步骤 2**：两边乘以 $\tan\theta$（注意：$\tan\theta \neq 0$，否则左边无定义）。

$$
4 = \tan^2\theta
$$

**步骤 3**：两边开平方。

$$
\tan\theta = \pm 2
$$

**步骤 4**：分别解两个方程。

**子情形一**：$\tan\theta = 2$。

$\alpha_1 = \arctan(2) \approx 1.1071$。

通解 $\theta = 1.1071 + n\pi$。

在 $[0, 2\pi)$ 内：$n = 0$ 得 $1.1071$，$n = 1$ 得 $1.1071 + \pi \approx 4.2487$。

**子情形二**：$\tan\theta = -2$。

$\alpha_2 = \arctan(-2) \approx -1.1071$。

通解 $\theta = -1.1071 + n\pi$。

在 $[0, 2\pi)$ 内：$n = 1$ 得 $-1.1071 + \pi \approx 2.0344$，$n = 2$ 得 $-1.1071 + 2\pi \approx 5.1760$。

**步骤 5**：检查定义域。原方程中 $\cot\theta$ 要求 $\sin\theta \neq 0$（即 $\theta \neq n\pi$），$\tan\theta$ 要求 $\cos\theta \neq 0$（即 $\theta \neq \frac{\pi}{2} + n\pi$）。

四个解均不在此列，全部有效。

**答案**：$\theta \in \{1.1071,\; 2.0344,\; 4.2487,\; 5.1760\}$

---

**类型二：利用 $\sec^2 = 1 + \tan^2$**

**例题 2**（考纲举例）：在 $0 \leq x < 2\pi$ 范围内解方程 $2\sec^2 x + \tan x - 3 = 0$。

**分析**：方程同时包含 $\sec^2$ 和 $\tan$。利用恒等式 $\sec^2 x = 1 + \tan^2 x$，可以将方程转化为关于 $\tan x$ 的二次方程。

**解**：

**步骤 1**：代入 $\sec^2 x = 1 + \tan^2 x$。

$$
2(1 + \tan^2 x) + \tan x - 3 = 0
$$

**步骤 2**：展开整理。

$$
2 + 2\tan^2 x + \tan x - 3 = 0
$$

$$
2\tan^2 x + \tan x - 1 = 0
$$

**步骤 3**：令 $u = \tan x$，解二次方程 $2u^2 + u - 1 = 0$。

因式分解：$(2u - 1)(u + 1) = 0$

$$
u = \frac{1}{2} \quad\text{或}\quad u = -1
$$

即 $\tan x = \frac{1}{2}$ 或 $\tan x = -1$。

**步骤 4**：解 $\tan x = \frac{1}{2}$。

$\alpha_1 = \arctan\left(\frac{1}{2}\right) \approx 0.4636$。

通解 $x = 0.4636 + n\pi$。

在 $[0, 2\pi)$ 内：$n = 0$ 得 $0.4636$，$n = 1$ 得 $0.4636 + \pi \approx 3.6052$。

**步骤 5**：解 $\tan x = -1$。

$\arctan(-1) = -\frac{\pi}{4}$。

通解 $x = -\frac{\pi}{4} + n\pi$。

在 $[0, 2\pi)$ 内：$n = 1$ 得 $-\frac{\pi}{4} + \pi = \frac{3\pi}{4}$，$n = 2$ 得 $-\frac{\pi}{4} + 2\pi = \frac{7\pi}{4}$。

**步骤 6**：检查定义域。$\sec x$ 在 $\cos x = 0$（$x = \frac{\pi}{2} + n\pi$）处无定义。

四个解均不在此列，全部有效。

**答案**：$x \in \{0.4636,\; 3.6052,\; \dfrac{3\pi}{4},\; \dfrac{7\pi}{4}\}$

---

**类型三：$a\sin(k\theta) + b\cos(k\theta) = 0$ 型**

**例题 3**（考纲举例）：在 $0 \leq \theta < 2\pi$ 范围内解方程 $5\sin 3\theta + 2\cos 3\theta = 0$。

**分析**：方程同时包含 $\sin 3\theta$ 和 $\cos 3\theta$，且两项次数相同。两边除以 $\cos 3\theta$ 可化为 $\tan$ 形式。但需要注意 $\cos 3\theta = 0$ 的情况需要单独检查。

**解**：

**步骤 1**：移项。

$$
5\sin 3\theta = -2\cos 3\theta
$$

**步骤 2**：两边除以 $\cos 3\theta$（先假设 $\cos 3\theta \neq 0$）。

$$
5\tan 3\theta = -2
$$

$$
\tan 3\theta = -\frac{2}{5}
$$

**步骤 3**：解 $\tan 3\theta = -\frac{2}{5}$。

$\alpha = \arctan\left(-\frac{2}{5}\right) \approx -0.3805$。

通解：$3\theta = -0.3805 + n\pi$，即 $\theta = -\frac{0.3805}{3} + \frac{n\pi}{3} \approx -0.1268 + \frac{n\pi}{3}$。

**步骤 4**：在 $[0, 2\pi)$ 内取适当的 $n$ 值。

| $n$ | $\theta = -0.1268 + \frac{n\pi}{3}$ | 是否 $\in [0, 2\pi)$ |
|-----|--------------------------------------|---------------------|
| $1$ | $-0.1268 + \frac{\pi}{3} \approx 0.9204$ | ✓ |
| $2$ | $-0.1268 + \frac{2\pi}{3} \approx 1.9676$ | ✓ |
| $3$ | $-0.1268 + \pi \approx 3.0148$ | ✓ |
| $4$ | $-0.1268 + \frac{4\pi}{3} \approx 4.0620$ | ✓ |
| $5$ | $-0.1268 + \frac{5\pi}{3} \approx 5.1092$ | ✓ |
| $6$ | $-0.1268 + 2\pi \approx 6.1564$ | ✓ |
| $0$ | $-0.1268$ | ✗（负） |
| $7$ | $-0.1268 + \frac{7\pi}{3} \approx 7.2036$ | ✗（$\geq 2\pi$） |

共 6 个解。

**步骤 5**：检查 $\cos 3\theta = 0$ 的情况。

当 $\cos 3\theta = 0$ 时，$3\theta = \frac{\pi}{2} + n\pi$，即 $\theta = \frac{\pi}{6} + \frac{n\pi}{3}$。

代入原方程左端：$5\sin 3\theta + 2\cos 3\theta = 5\sin\left(\frac{\pi}{2} + n\pi\right) + 2 \times 0 = 5(\pm 1) = \pm 5 \neq 0$。

因此 $\cos 3\theta = 0$ 的解不是原方程的解，无需额外添加。

**答案**：$\theta \in \{0.9204,\; 1.9676,\; 3.0148,\; 4.0620,\; 5.1092,\; 6.1564\}$

---

**类型四：含 $\csc^2$ 和复合角的方程**

**例题 4**（考纲举例）：在 $0 \leq \theta < 2\pi$ 范围内解方程 $3\csc^2\left(\frac{\theta}{2}\right) = 4$。

**分析**：方程含 $\csc^2$（$\sin$ 的倒数的平方）和复合角 $\frac{\theta}{2}$。需要先处理 $\csc$，再处理复合角。

**解**：

**步骤 1**：用 $\csc = \frac{1}{\sin}$ 转化。

$$
3 \times \frac{1}{\sin^2(\theta/2)} = 4
$$

**步骤 2**：整理。

$$
\sin^2\left(\frac{\theta}{2}\right) = \frac{3}{4}
$$

**步骤 3**：开平方，注意正负号。

$$
\sin\left(\frac{\theta}{2}\right) = \pm\frac{\sqrt{3}}{2}
$$

**步骤 4**：先处理复合角。令 $u = \frac{\theta}{2}$。

由于 $\theta \in [0, 2\pi)$，$u \in [0, \pi)$。

**子情形一**：$\sin u = \frac{\sqrt{3}}{2}$。

参考角 $\alpha = \arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$。

$k > 0$，解在第一和第二象限：

在 $[0, \pi)$ 内：$u = \frac{\pi}{3}$，$u = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$

注意第二象限的解 $\frac{2\pi}{3}$ 在 $[0, \pi)$ 内，有效。

**子情形二**：$\sin u = -\frac{\sqrt{3}}{2}$。

$k < 0$，解在第三和第四象限。但 $u \in [0, \pi)$ 只覆盖第一、二象限，所以在 $[0, \pi)$ 内无解。

**步骤 5**：由 $u = \frac{\theta}{2}$ 得 $\theta = 2u$。

$$
\theta = 2 \times \frac{\pi}{3} = \frac{2\pi}{3}, \quad \theta = 2 \times \frac{2\pi}{3} = \frac{4\pi}{3}
$$

**步骤 6**：检查定义域。$\csc\left(\frac{\theta}{2}\right)$ 在 $\sin\left(\frac{\theta}{2}\right) = 0$ 处无定义。两个解均使 $\sin\left(\frac{\theta}{2}\right) = \pm\frac{\sqrt{3}}{2} \neq 0$，有效。

**答案**：$\theta = \dfrac{2\pi}{3}$ 和 $\theta = \dfrac{4\pi}{3}$

---

**类型五：含 $\csc^2$ 和 $\cot^2$ 的方程**

**例题 5**：在 $0 \leq x < 2\pi$ 范围内解方程 $\csc^2 x - 2\cot^2 x = 1$。

**分析**：方程含 $\csc^2$ 和 $\cot^2$，可以用恒等式 $\csc^2 x = 1 + \cot^2 x$ 统一变量。

**解**：

**步骤 1**：代入 $\csc^2 x = 1 + \cot^2 x$。

$$
(1 + \cot^2 x) - 2\cot^2 x = 1
$$

**步骤 2**：化简。

$$
1 + \cot^2 x - 2\cot^2 x = 1
$$

$$
1 - \cot^2 x = 1
$$

$$
-\cot^2 x = 0
$$

$$
\cot x = 0
$$

**步骤 3**：$\cot x = 0$ 意味着 $\cos x = 0$（且 $\sin x \neq 0$）。

$\cos x = 0$ 在 $[0, 2\pi)$ 内的解为 $x = \frac{\pi}{2}$ 和 $x = \frac{3\pi}{2}$。

**步骤 4**：检查定义域。$\cot x$ 在 $\sin x = 0$ 处无定义。两个解均使 $\sin x = \pm 1 \neq 0$，有效。

**答案**：$x = \dfrac{\pi}{2}$ 和 $x = \dfrac{3\pi}{2}$

---

**类型六：含 $\sin^2$ 和 $\cos$ 的方程（利用 $\sin^2 + \cos^2 = 1$）**

**例题 6**：在 $0 \leq x < 2\pi$ 范围内解方程 $2\sin^2 x + 3\cos x = 0$。

**分析**：方程同时含 $\sin^2$ 和 $\cos$。利用 $\sin^2 x = 1 - \cos^2 x$ 可以将方程化为关于 $\cos x$ 的二次方程。

**解**：

**步骤 1**：代入 $\sin^2 x = 1 - \cos^2 x$。

$$
2(1 - \cos^2 x) + 3\cos x = 0
$$

**步骤 2**：展开整理。

$$
2 - 2\cos^2 x + 3\cos x = 0
$$

$$
-2\cos^2 x + 3\cos x + 2 = 0
$$

两边乘以 $-1$：

$$
2\cos^2 x - 3\cos x - 2 = 0
$$

**步骤 3**：令 $u = \cos x$，解二次方程 $2u^2 - 3u - 2 = 0$。

因式分解：$(2u + 1)(u - 2) = 0$

$$
u = -\frac{1}{2} \quad\text{或}\quad u = 2
$$

$u = 2$ 超出 $\cos$ 的值域 $[-1, 1]$，舍去。

**步骤 4**：解 $\cos x = -\frac{1}{2}$。

参考角 $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$。

$k < 0$，解在第二和第三象限：

$$
x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}, \quad x = \pi + \frac{\pi}{3} = \frac{4\pi}{3}
$$

**答案**：$x = \dfrac{2\pi}{3}$ 和 $x = \dfrac{4\pi}{3}$

---

**类型七：含 $\sin$ 和 $\sin^2$ 的二次方程**

**例题 7**：在 $0 \leq x < 2\pi$ 范围内解方程 $2\sin^2 x - \sin x - 1 = 0$。

**解**：

**步骤 1**：令 $u = \sin x$，得二次方程 $2u^2 - u - 1 = 0$。

因式分解：$(2u + 1)(u - 1) = 0$

$$
u = -\frac{1}{2} \quad\text{或}\quad u = 1
$$

**步骤 2**：解 $\sin x = 1$。

在 $[0, 2\pi)$ 内：$x = \frac{\pi}{2}$。

**步骤 3**：解 $\sin x = -\frac{1}{2}$。

参考角 $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

$k < 0$，第三和第四象限：

$$
x = \pi + \frac{\pi}{6} = \frac{7\pi}{6}, \quad x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}
$$

**答案**：$x \in \left\{\dfrac{\pi}{2},\; \dfrac{7\pi}{6},\; \dfrac{11\pi}{6}\right\}$

---

**类型八：含 $\cos(2\theta)$ 的方程（用二倍角公式展开）**

**例题 8**：在 $0 \leq \theta < 2\pi$ 范围内解方程 $\cos 2\theta + \sin\theta = 0$。

**分析**：方程含 $\cos 2\theta$ 和 $\sin\theta$，角度不同。用二倍角公式 $\cos 2\theta = 1 - 2\sin^2\theta$ 将 $\cos 2\theta$ 展开为 $\sin\theta$ 的表达式。

**解**：

**步骤 1**：代入 $\cos 2\theta = 1 - 2\sin^2\theta$。

$$
(1 - 2\sin^2\theta) + \sin\theta = 0
$$

**步骤 2**：整理为关于 $\sin\theta$ 的二次方程。

$$
-2\sin^2\theta + \sin\theta + 1 = 0
$$

两边乘以 $-1$：

$$
2\sin^2\theta - \sin\theta - 1 = 0
$$

**步骤 3**：令 $u = \sin\theta$，解 $2u^2 - u - 1 = 0$。

因式分解：$(2u + 1)(u - 1) = 0$

$$
u = -\frac{1}{2} \quad\text{或}\quad u = 1
$$

**步骤 4**：解 $\sin\theta = 1$。

$\theta = \frac{\pi}{2}$。

**步骤 5**：解 $\sin\theta = -\frac{1}{2}$。

$$
\theta = \pi + \frac{\pi}{6} = \frac{7\pi}{6}, \quad \theta = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}
$$

**答案**：$\theta \in \left\{\dfrac{\pi}{2},\; \dfrac{7\pi}{6},\; \dfrac{11\pi}{6}\right\}$

---

**类型九：利用 $\cos 2\theta$ 降次**

**例题 9**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos^2 x = \frac{3}{4}$。

**解法一（直接开方）**：

$$
\cos x = \pm\frac{\sqrt{3}}{2}
$$

解 $\cos x = \frac{\sqrt{3}}{2}$：$x = \frac{\pi}{6}$，$x = \frac{11\pi}{6}$

解 $\cos x = -\frac{\sqrt{3}}{2}$：$x = \frac{5\pi}{6}$，$x = \frac{7\pi}{6}$

共 4 个解。

**解法二（用 $\cos 2\theta$ 降次）**：

由 $\cos^2 x = \frac{1 + \cos 2x}{2}$：

$$
\frac{1 + \cos 2x}{2} = \frac{3}{4}
$$

$$
1 + \cos 2x = \frac{3}{2}
$$

$$
\cos 2x = \frac{1}{2}
$$

令 $u = 2x$，$u \in [0, 4\pi)$。

解 $\cos u = \frac{1}{2}$，参考角 $\alpha = \frac{\pi}{3}$。

$k > 0$，第一和第四象限。

在 $[0, 2\pi)$ 内：$u = \frac{\pi}{3}$，$u = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$

在 $[2\pi, 4\pi)$ 内：$u = \frac{\pi}{3} + 2\pi = \frac{7\pi}{3}$，$u = \frac{5\pi}{3} + 2\pi = \frac{11\pi}{3}$

由 $x = \frac{u}{2}$ 得：

$$
x = \frac{\pi}{6},\; \frac{5\pi}{6},\; \frac{7\pi}{6},\; \frac{11\pi}{6}
$$

两种方法结果一致。

**答案**：$x \in \left\{\dfrac{\pi}{6},\; \dfrac{5\pi}{6},\; \dfrac{7\pi}{6},\; \dfrac{11\pi}{6}\right\}$

---

**类型十：综合运用多种恒等式**

**例题 10**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sec x + \tan x = 1$。

**分析**：方程同时含 $\sec x$ 和 $\tan x$。将它们统一为 $\sin$ 和 $\cos$，然后通过代数变换求解。

**解**：

**步骤 1**：将 $\sec x$ 和 $\tan x$ 用 $\sin$ 和 $\cos$ 表示。

$$
\frac{1}{\cos x} + \frac{\sin x}{\cos x} = 1
$$

**步骤 2**：合并左边。

$$
\frac{1 + \sin x}{\cos x} = 1
$$

**步骤 3**：两边乘以 $\cos x$（注意 $\cos x \neq 0$）。

$$
1 + \sin x = \cos x
$$

**步骤 4**：移项。$1 + \sin x - \cos x = 0$。这不太容易直接处理，我们换一种方法。

由 $1 + \sin x = \cos x$，两边平方：

$$
(1 + \sin x)^2 = \cos^2 x
$$

**步骤 5**：用 $\cos^2 x = 1 - \sin^2 x$ 代入。

$$
1 + 2\sin x + \sin^2 x = 1 - \sin^2 x
$$

$$
2\sin x + \sin^2 x = -\sin^2 x
$$

$$
2\sin x + 2\sin^2 x = 0
$$

$$
2\sin x(1 + \sin x) = 0
$$

**步骤 6**：$\sin x = 0$ 或 $\sin x = -1$。

**步骤 7**：检查各候选解。

$\sin x = 0$ 在 $[0, 2\pi)$ 内的解：$x = 0$，$x = \pi$。

代入原方程验证：
- $x = 0$：$\sec 0 + \tan 0 = 1 + 0 = 1$ ✓
- $x = \pi$：$\sec\pi + \tan\pi = -1 + 0 = -1 \neq 1$ ✗（平方引入了增根）

$\sin x = -1$ 在 $[0, 2\pi)$ 内的解：$x = \frac{3\pi}{2}$。

代入原方程验证：
- $x = \frac{3\pi}{2}$：$\sec\frac{3\pi}{2}$ 无定义（$\cos\frac{3\pi}{2} = 0$）✗

**步骤 8**：唯一有效解为 $x = 0$。

**答案**：$x = 0$

---

> ⚠️ **重要提醒**：本题展示了平方可能引入增根，因此**平方后必须验根**。同时也展示了检查定义域的重要性。

---

### 8.5.7 解三角方程——常见错误与防范

| 错误类型 | 错误示例 | 正确做法 |
|---------|---------|---------|
| 忽略周期性 | 解 $\sin x = \frac{1}{2}$ 只得到 $\frac{\pi}{6}$ | 正确定出两个解 $\frac{\pi}{6}$ 和 $\frac{5\pi}{6}$ |
| 忽略换元后的周期加倍 | 解 $\cos 2x = \frac{1}{2}$ 只找到 2 个解 | $2x$ 在 $[0, 4\pi)$ 内，应有 4 个解 |
| 平方后不验根 | 解 $\sin x + \cos x = 1$ 直接平方得到增根 | 平方后的解必须代入原方程验证 |
| 除以可能为零的表达式 | 解 $5\sin 3\theta + 2\cos 3\theta = 0$ 忘记检查 $\cos 3\theta = 0$ | 先假设 $\cos 3\theta \neq 0$，再单独验证 |
| 忽略定义域 | 解 $\sec x = 2$ 不检查 $\cos x \neq 0$ | 确保解不在 $\frac{\pi}{2} + n\pi$ 处 |
| $\sin$ 和 $\cos$ 的解分布混淆 | 用 $\sin$ 的模式解 $\cos$ 方程 | $\sin k > 0$ 在一、二象限；$\cos k > 0$ 在一、四象限 |
| 忘记 $\tan$ 周期为 $\pi$ | 解 $\tan x = 1$ 只得到 $\frac{\pi}{4}$ | $\tan$ 周期 $\pi$，通解为 $\frac{\pi}{4} + n\pi$ |

---

### 8.5.8 解三角方程——方法总结流程图

```
                    ┌─────────────────────────────┐
                    │      给定的三角方程          │
                    └─────────────┬───────────────┘
                                  │
                    ┌─────────────▼───────────────┐
                    │ 方程是否包含不同名的函数？    │
                    └────────┬──────────┬─────────┘
                         是 │          │ 否
                   ┌────────▼──┐  ┌────▼─────┐
                   │ 用恒等式  │  │ 已为基本 │
                   │ 统一变量  │  │ 单一形式 │
                   └────────┬──┘  └────┬─────┘
                            │          │
                   ┌────────▼──────────▼───────┐
                   │ 化为基本形式              │
                   │ sin x = k / cos x = k     │
                   │ / tan x = k + 其他        │
                   └────────┬──────────────────┘
                            │
               ┌────────────▼────────────┐
               │ 选择解法                │
               └────────┬───────────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
   ┌─────────┐   ┌──────────┐   ┌──────────┐
   │ sin x=k │   │ cos x=k  │   │ tan x=k  │
   │ 参考角  │   │ 参考角   │   │ arctan(k)│
   │ α=arcsin│   │ α=arccos │   │ + nπ    │
   │ 分象限  │   │ 分象限   │   │          │
   └────┬────┘   └────┬─────┘   └────┬─────┘
        │             │              │
        └─────────────┼──────────────┘
                      ▼
          ┌──────────────────────┐
          │ 写出给定区间内的所有解 │
          └──────────┬───────────┘
                     ▼
          ┌──────────────────────┐
          │ 检查定义域，排除无效解 │
          └──────────────────────┘
```


**常用转化策略**：

| 方程特征 | 转化方法 |
|---------|---------|
| 含 $\sec$、$\csc$、$\cot$ | 转化为 $\sin$、$\cos$：$\sec = 1/\cos$ 等 |
| 含 $\tan$ 和 $\sec$ | 用 $\sec^2 = 1 + \tan^2$ 化为单一变量 |
| 含 $\cot$ 和 $\csc$ | 用 $\csc^2 = 1 + \cot^2$ 化为单一变量 |
| 含 $\sin$ 和 $\cos$ 的二次式 | 用 $\sin^2 + \cos^2 = 1$ 化为单一变量 |
| 含 $a\sin(k\theta) + b\cos(k\theta) = 0$ | 两边除以 $\cos(k\theta)$ 得 $\tan(k\theta) = -\frac{b}{a}$ |
| 含 $\sin(2\theta)$ 或 $\cos(2\theta)$ | 用二倍角公式展开或降次 |

### 8.5.6 注意事项

1. **定义域**：排除函数无定义的点。例如 $\tan x$ 在 $x = \frac{\pi}{2} + n\pi$ 处无定义，$\sec x$ 同样。
2. **平方增根**：如果方程两边平方，可能引入增根，需要验根。
3. **两边乘以表达式**：如果乘以可能为零的表达式，可能会丢失解或引入增根。
4. **周期性**：注意在给定区间内，每个周期都会产生新的解。

### 8.5.7 例题

---

**例题 1（基本正弦方程——$k > 0$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = \frac{\sqrt{3}}{2}$。

**解**：

**步骤 1**：求参考角。$\alpha = \arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$。

**步骤 2**：$k = \frac{\sqrt{3}}{2} > 0$，解在第一和第二象限。

**步骤 3**：写出解。

第一象限：$x = \alpha = \dfrac{\pi}{3}$

第二象限：$x = \pi - \alpha = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}$

**答案**：$x = \dfrac{\pi}{3}$ 和 $x = \dfrac{2\pi}{3}$

---

**例题 2（基本正弦方程——$k < 0$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\sin x = -\frac{1}{2}$。

**解**：

**步骤 1**：求参考角。$\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

**步骤 2**：$k = -\frac{1}{2} < 0$，解在第三和第四象限。

**步骤 3**：写出解。

第三象限：$x = \pi + \alpha = \pi + \dfrac{\pi}{6} = \dfrac{7\pi}{6}$

第四象限：$x = 2\pi - \alpha = 2\pi - \dfrac{\pi}{6} = \dfrac{11\pi}{6}$

**答案**：$x = \dfrac{7\pi}{6}$ 和 $x = \dfrac{11\pi}{6}$

---

**例题 3（基本余弦方程）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\cos x = -\frac{\sqrt{2}}{2}$。

**解**：

**步骤 1**：求参考角。$\alpha = \arccos\left(\frac{\sqrt{2}}{2}\right) = \frac{\pi}{4}$。

**步骤 2**：$k = -\frac{\sqrt{2}}{2} < 0$，解在第二和第三象限。

**步骤 3**：写出解。

第二象限：$x = \pi - \alpha = \pi - \dfrac{\pi}{4} = \dfrac{3\pi}{4}$

第三象限：$x = \pi + \alpha = \pi + \dfrac{\pi}{4} = \dfrac{5\pi}{4}$

**答案**：$x = \dfrac{3\pi}{4}$ 和 $x = \dfrac{5\pi}{4}$

---

**例题 4（基本正切方程）**：在 $0 \leq x < 2\pi$ 范围内解方程 $\tan x = \sqrt{3}$。

**解**：

**步骤 1**：求参考角。$\alpha = \arctan(\sqrt{3}) = \frac{\pi}{3}$。

**步骤 2**：$\tan$ 的周期为 $\pi$，通解为 $x = \frac{\pi}{3} + n\pi$。

**步骤 3**：在 $[0, 2\pi)$ 内取 $n = 0, 1$：

$$
x = \frac{\pi}{3},\quad x = \frac{\pi}{3} + \pi = \frac{4\pi}{3}
$$

**答案**：$x = \dfrac{\pi}{3}$ 和 $x = \dfrac{4\pi}{3}$

---

**例题 5（含 $\cot$ 的方程——转化为 $\tan$）**：在 $0 \leq x < 2\pi$ 范围内解方程 $4\cot x = \tan x$。

**解**：

**步骤 1**：将 $\cot x = \frac{1}{\tan x}$ 代入。

$$
\frac{4}{\tan x} = \tan x
$$

**步骤 2**：两边乘以 $\tan x$（注意 $\tan x \neq 0$）。

$$
4 = \tan^2 x
$$

**步骤 3**：所以 $\tan x = \pm 2$。

**步骤 4**：求参考角。$\alpha = \arctan(2)$（非特殊角，保留小数）。

使用计算器：$\alpha \approx 1.1071$ 弧度。

**步骤 5**：$\tan x = 2$（正）：解在第一和第三象限。

$$
x = \alpha \approx 1.1071,\quad x = \pi + \alpha \approx 4.2487
$$

**步骤 6**：$\tan x = -2$（负）：解在第二和第四象限。

$$
x = \pi - \alpha \approx 2.0344,\quad x = 2\pi - \alpha \approx 5.1760
$$

**步骤 7**：检查定义域。$\tan x \neq 0$，所有解均满足。

**答案**：$x \in \{1.1071,\; 2.0344,\; 4.2487,\; 5.1760\}$

---

**例题 6（利用 $\sec^2 = 1 + \tan^2$ 化为一元二次方程）**：在 $0 \leq x < 2\pi$ 范围内解方程 $2\sec^2 x + \tan x - 3 = 0$。

**解**：

**步骤 1**：用恒等式 $\sec^2 x = 1 + \tan^2 x$ 代入。

$$
2(1 + \tan^2 x) + \tan x - 3 = 0
$$

**步骤 2**：展开整理。

$$
2 + 2\tan^2 x + \tan x - 3 = 0
$$

$$
2\tan^2 x + \tan x - 1 = 0
$$

**步骤 3**：令 $u = \tan x$，解二次方程。

$$
2u^2 + u - 1 = 0
$$

因式分解：$(2u - 1)(u + 1) = 0$

$$
u = \frac{1}{2} \quad\text{或}\quad u = -1
$$

**步骤 4**：解 $\tan x = \frac{1}{2}$。

$\alpha_1 = \arctan\left(\frac{1}{2}\right) \approx 0.4636$。

$\tan x > 0$，解在第一和第三象限：

$$
x_1 \approx 0.4636,\quad x_2 \approx \pi + 0.4636 = 3.6052
$$

**步骤 5**：解 $\tan x = -1$。

$\alpha_2 = \arctan(1) = \frac{\pi}{4}$。

$\tan x < 0$，解在第二和第四象限：

$$
x_3 = \pi - \frac{\pi}{4} = \frac{3\pi}{4},\quad x_4 = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}
$$

**步骤 6**：检查定义域。$\sec x$ 在 $x = \frac{\pi}{2} + n\pi$ 处无定义。检查各解：

- $0.4636$：$\cos(0.4636) \neq 0$ ✓
- $3.6052$：$\cos(3.6052) \neq 0$ ✓
- $\frac{3\pi}{4}$：$\cos(\frac{3\pi}{4}) \neq 0$ ✓
- $\frac{7\pi}{4}$：$\cos(\frac{7\pi}{4}) \neq 0$ ✓

全部有效。

**答案**：$x \in \{0.4636,\; 3.6052,\; \dfrac{3\pi}{4},\; \dfrac{7\pi}{4}\}$

---

**例题 7（$a\sin(k\theta) + b\cos(k\theta) = 0$ 型）**：在 $0 \leq \theta < 2\pi$ 范围内解方程 $5\sin(3\theta) + 2\cos(3\theta) = 0$。

**解**：

**步骤 1**：将含有 $\cos$ 的项移到右边。

$$
5\sin(3\theta) = -2\cos(3\theta)
$$

**步骤 2**：两边除以 $\cos(3\theta)$（注意 $\cos(3\theta) \neq 0$ 的情况需单独检查）。

$$
5\tan(3\theta) = -2
$$

$$
\tan(3\theta) = -\frac{2}{5}
$$

**步骤 3**：求参考角。$\alpha = \arctan\left(\frac{2}{5}\right) \approx 0.3805$。

**步骤 4**：$\tan(3\theta) = -0.4$（负），通解为 $3\theta = n\pi - \alpha$（或 $3\theta = \pi n - \alpha$）。

更规范地：$\tan u = -0.4$ 的通解为 $u = \arctan(-0.4) + n\pi = -\alpha + n\pi$。

$$
3\theta = -\alpha + n\pi
$$

$$
\theta = -\frac{\alpha}{3} + \frac{n\pi}{3}
$$

**步骤 5**：在 $[0, 2\pi)$ 内取适当的 $n$ 值。

$\frac{\alpha}{3} \approx 0.1268$。

| $n$ | $\theta = -\frac{\alpha}{3} + \frac{n\pi}{3}$ | 是否在 $[0, 2\pi)$ |
|----|----------------------------------------------|-------------------|
| $1$ | $-\frac{\alpha}{3} + \frac{\pi}{3} \approx 1.0472 - 0.1268 \approx 0.9204$ | ✓ |
| $2$ | $-\frac{\alpha}{3} + \frac{2\pi}{3} \approx 2.0944 - 0.1268 \approx 1.9676$ | ✓ |
| $3$ | $-\frac{\alpha}{3} + \pi \approx 3.1416 - 0.1268 \approx 3.0148$ | ✓ |
| $4$ | $-\frac{\alpha}{3} + \frac{4\pi}{3} \approx 4.1888 - 0.1268 \approx 4.0620$ | ✓ |
| $5$ | $-\frac{\alpha}{3} + \frac{5\pi}{3} \approx 5.2360 - 0.1268 \approx 5.1092$ | ✓ |
| $6$ | $-\frac{\alpha}{3} + 2\pi \approx 6.2832 - 0.1268 \approx 6.1564$ | ✓（$< 2\pi$） |
| $0$ | $-\frac{\alpha}{3} \approx -0.1268$ | ✗ |
| $7$ | $-\frac{\alpha}{3} + \frac{7\pi}{3} \approx 7.3304 - 0.1268 \approx 7.2036$ | ✗（$\geq 2\pi$） |

**步骤 6**：检查 $\cos(3\theta) = 0$ 的情况。

当 $\cos(3\theta) = 0$ 时，$3\theta = \frac{\pi}{2} + n\pi$，即 $\theta = \frac{\pi}{6} + \frac{n\pi}{3}$。

代入原方程：$5\sin(3\theta) = 5\sin(\frac{\pi}{2} + n\pi) = 5(\pm 1) \neq 0$，而 $\cos(3\theta) = 0$，所以 $\theta = \frac{\pi}{6} + \frac{n\pi}{3}$ 不是解。

**答案**：$\theta \in \{0.9204,\; 1.9676,\; 3.0148,\; 4.0620,\; 5.1092,\; 6.1564\}$

---

**例题 8（含二次 $\sin$ 的方程）**：在 $0 \leq x < 2\pi$ 范围内解方程 $2\sin^2 x - 3\sin x + 1 = 0$。

**解**：

**步骤 1**：令 $u = \sin x$，得二次方程。

$$
2u^2 - 3u + 1 = 0
$$

**步骤 2**：因式分解。

$$
(2u - 1)(u - 1) = 0
$$

**步骤 3**：$u = \frac{1}{2}$ 或 $u = 1$。

**情况 1**：$\sin x = 1$。

$x = \frac{\pi}{2}$（在 $[0, 2\pi)$ 内只有一个解，因为 $\sin x = 1$ 只在 $x = \frac{\pi}{2}$ 处成立）。

**情况 2**：$\sin x = \frac{1}{2}$。

参考角 $\alpha = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$。

$k > 0$，解在第一和第二象限：

$$
x = \frac{\pi}{6},\quad x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}
$$

**答案**：$x \in \left\{\dfrac{\pi}{6},\; \dfrac{\pi}{2},\; \dfrac{5\pi}{6}\right\}$

---

**例题 9（含 $\cos(2\theta)$ 的方程——先换元再求解）**：在 $0 \leq \theta < 2\pi$ 范围内解方程 $\cos(2\theta) = \frac{1}{2}$。

**解**：

**步骤 1**：令 $u = 2\theta$，则 $u \in [0, 4\pi)$。

解 $\cos u = \frac{1}{2}$。

**步骤 2**：参考角 $\alpha = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}$。

$k > 0$，解在第一和第四象限：

在 $[0, 2\pi)$ 内：$u = \frac{\pi}{3}$ 和 $u = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$

**步骤 3**：由于周期为 $2\pi$，在 $[2\pi, 4\pi)$ 内还有两个解：

$u = \frac{\pi}{3} + 2\pi = \frac{7\pi}{3}$ 和 $u = \frac{5\pi}{3} + 2\pi = \frac{11\pi}{3}$

**步骤 4**：由 $\theta = \frac{u}{2}$ 得四个解：

$$
\theta = \frac{\pi}{6},\quad \theta = \frac{5\pi}{6},\quad \theta = \frac{7\pi}{6},\quad \theta = \frac{11\pi}{6}
$$

**答案**：$\theta \in \left\{\dfrac{\pi}{6},\; \dfrac{5\pi}{6},\; \dfrac{7\pi}{6},\; \dfrac{11\pi}{6}\right\}$

---

**例题 10（含 $\csc^2$ 的方程）**：在 $0 \leq x < 2\pi$ 范围内解方程 $3\csc^2 x - 4 = 0$。

**解**：

**步骤 1**：整理方程。

$$
3\csc^2 x = 4 \;\Rightarrow\; \csc^2 x = \frac{4}{3}
$$

**步骤 2**：因为 $\csc x = \frac{1}{\sin x}$，所以：

$$
\frac{1}{\sin^2 x} = \frac{4}{3} \;\Rightarrow\; \sin^2 x = \frac{3}{4}
$$

**步骤 3**：因此 $\sin x = \pm\frac{\sqrt{3}}{2}$。

**情况 1**：$\sin x = \frac{\sqrt{3}}{2}$。

参考角 $\alpha = \arcsin\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$。

$k > 0$，解在第一和第二象限：

$$
x = \frac{\pi}{3},\quad x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}
$$

**情况 2**：$\sin x = -\frac{\sqrt{3}}{2}$。

参考角 $\alpha = \frac{\pi}{3}$。

$k < 0$，解在第三和第四象限：

$$
x = \pi + \frac{\pi}{3} = \frac{4\pi}{3},\quad x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}
$$

**步骤 4**：检查定义域。$\csc x$ 在 $\sin x = 0$ 处无定义。四个解均使 $\sin x \neq 0$，全部有效。

**答案**：$x \in \left\{\dfrac{\pi}{3},\; \dfrac{2\pi}{3},\; \dfrac{4\pi}{3},\; \dfrac{5\pi}{3}\right\}$

---

> ⚠️ **易错提醒**：
> 1. **忘记周期性**：在 $[0, 2\pi)$ 内，$\sin$ 和 $\cos$ 最多有 2 个解，但经过换元（如 $2\theta$）后，解的个数会增加
> 2. **忽略定义域**：$\tan$、$\sec$、$\csc$、$\cot$ 在某些点无定义，这些点必须从解集中排除
> 3. **两边除以变量**：如例题 7 中除以 $\cos(3\theta)$ 时，需要单独检查 $\cos(3\theta) = 0$ 的情况
> 4. **符号错误**：使用 ASTC 法则时注意每个象限的符号

---

## 8.6 三角恒等式的证明

### 8.6.1 证明策略总览

证明三角恒等式没有固定的算法，但以下策略通常有效：

| 策略 | 适用场景 | 操作 |
|------|---------|------|
| **策略 1：从复杂端入手** | 两边不对称 | 选择项数更多、结构更复杂的一边进行化简 |
| **策略 2：统一化为 $\sin$ 和 $\cos$** | 含 $\tan$、$\sec$、$\csc$、$\cot$ | 用基本关系替换：$\tan = \frac{\sin}{\cos}$，$\sec = \frac{1}{\cos}$ 等 |
| **策略 3：通分合并** | 分式加减 | 找到公分母，合并分子 |
| **策略 4：利用 $\sin^2 + \cos^2 = 1$** | 出现 $1$ 或平方项 | 用恒等式替换或合并 |
| **策略 5：因式分解** | 分子分母可分解 | 提取公因式、平方差公式 |
| **策略 6：分子分母同乘共轭式** | 分母含 $1 \pm \sin\theta$ 或 $1 \pm \cos\theta$ | 乘以 $1 \mp \sin\theta$ 或 $1 \mp \cos\theta$ |
| **策略 7：利用二倍角公式** | 角度不一致 | 将 $2\theta$ 展开或降次 |

### 8.6.2 证明的书写规范

在书写证明过程时，应遵循以下规范：

1. 明确写出从哪一边开始（"左边 $=$" 或 "右边 $=$"）
2. 每一步变换都基于已知恒等式或代数运算
3. 最终得到与另一边完全相同的形式
4. 以"$\blacksquare$"或"得证"结束

### 8.6.3 详细证明示例

---

**例题 1（策略：化为 $\sin$ 和 $\cos$）**：证明 $\tan x + \cot x = \sec x \csc x$。

**证明**：

从左边开始：

$$
\tan x + \cot x = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}
$$

通分，公分母为 $\sin x \cos x$：

$$
= \frac{\sin^2 x + \cos^2 x}{\sin x \cos x}
$$

由 $\sin^2 x + \cos^2 x = 1$：

$$
= \frac{1}{\sin x \cos x}
$$

再看右边：

$$
\sec x \csc x = \frac{1}{\cos x} \cdot \frac{1}{\sin x} = \frac{1}{\sin x \cos x}
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 2（策略：通分合并）**：证明 $\dfrac{\sin\theta}{1 + \cos\theta} + \dfrac{1 + \cos\theta}{\sin\theta} = 2\csc\theta$。

**证明**：

从左边开始，通分：

$$
\frac{\sin\theta}{1 + \cos\theta} + \frac{1 + \cos\theta}{\sin\theta}
= \frac{\sin^2\theta + (1 + \cos\theta)^2}{\sin\theta(1 + \cos\theta)}
$$

展开分子：

$$
\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta
$$

利用 $\sin^2\theta + \cos^2\theta = 1$ 合并：

$$
= (\sin^2\theta + \cos^2\theta) + 1 + 2\cos\theta = 1 + 1 + 2\cos\theta = 2 + 2\cos\theta
$$

提取公因式 $2(1 + \cos\theta)$：

$$
= \frac{2(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)}
$$

约去 $1 + \cos\theta$（注意 $1 + \cos\theta \neq 0$）：

$$
= \frac{2}{\sin\theta} = 2\csc\theta
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 3（策略：分子分母同乘共轭式）**：证明 $\dfrac{1 - \sin\theta}{\cos\theta} = \dfrac{\cos\theta}{1 + \sin\theta}$。

**证明**：

从左边开始，分子分母同乘以 $1 + \sin\theta$：

$$
\frac{1 - \sin\theta}{\cos\theta} = \frac{(1 - \sin\theta)(1 + \sin\theta)}{\cos\theta(1 + \sin\theta)}
$$

分子展开得 $1 - \sin^2\theta = \cos^2\theta$：

$$
= \frac{\cos^2\theta}{\cos\theta(1 + \sin\theta)}
$$

约去 $\cos\theta$（假设 $\cos\theta \neq 0$）：

$$
= \frac{\cos\theta}{1 + \sin\theta}
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

**另一种证法**（从右边开始）：

$$
\frac{\cos\theta}{1 + \sin\theta} = \frac{\cos\theta(1 - \sin\theta)}{(1 + \sin\theta)(1 - \sin\theta)} = \frac{\cos\theta(1 - \sin\theta)}{1 - \sin^2\theta}
$$

$$
= \frac{\cos\theta(1 - \sin\theta)}{\cos^2\theta} = \frac{1 - \sin\theta}{\cos\theta}
$$

同样得证。$\blacksquare$

---

**例题 4（策略：利用 $\sec^2 = 1 + \tan^2$）**：证明 $\sec^2\theta + \csc^2\theta = \sec^2\theta\csc^2\theta$。

**证明**：

从左边开始，将 $\sec$ 和 $\csc$ 转化为 $\sin$ 和 $\cos$：

$$
\sec^2\theta + \csc^2\theta = \frac{1}{\cos^2\theta} + \frac{1}{\sin^2\theta}
$$

通分，公分母为 $\sin^2\theta\cos^2\theta$：

$$
= \frac{\sin^2\theta + \cos^2\theta}{\sin^2\theta\cos^2\theta}
$$

利用 $\sin^2\theta + \cos^2\theta = 1$：

$$
= \frac{1}{\sin^2\theta\cos^2\theta}
$$

再看右边：

$$
\sec^2\theta\csc^2\theta = \frac{1}{\cos^2\theta} \cdot \frac{1}{\sin^2\theta} = \frac{1}{\sin^2\theta\cos^2\theta}
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 5（策略：因式分解 + 恒等式）**：证明 $\cos^4\theta - \sin^4\theta = \cos(2\theta)$。

**证明**：

从左边开始，利用平方差公式：

$$
\cos^4\theta - \sin^4\theta = (\cos^2\theta)^2 - (\sin^2\theta)^2
$$

$$
= (\cos^2\theta - \sin^2\theta)(\cos^2\theta + \sin^2\theta)
$$

由 $\cos^2\theta + \sin^2\theta = 1$：

$$
= (\cos^2\theta - \sin^2\theta) \times 1 = \cos^2\theta - \sin^2\theta
$$

由二倍角公式 $\cos(2\theta) = \cos^2\theta - \sin^2\theta$：

$$
= \cos(2\theta)
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 6（策略：利用 $\csc^2 = 1 + \cot^2$）**：证明 $\dfrac{1 + \tan^2\theta}{1 + \cot^2\theta} = \tan^2\theta$。

**证明**：

从左边开始，分子由 $\sec^2\theta = 1 + \tan^2\theta$，分母由 $\csc^2\theta = 1 + \cot^2\theta$：

$$
\frac{1 + \tan^2\theta}{1 + \cot^2\theta} = \frac{\sec^2\theta}{\csc^2\theta}
$$

将 $\sec$ 和 $\csc$ 转化为 $\sin$ 和 $\cos$：

$$
= \frac{1/\cos^2\theta}{1/\sin^2\theta} = \frac{\sin^2\theta}{\cos^2\theta} = \tan^2\theta
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 7（策略：二倍角公式）**：证明 $\dfrac{\sin(2\theta)}{1 - \cos(2\theta)} = \cot\theta$。

**证明**：

从左边开始，代入二倍角公式 $\sin(2\theta) = 2\sin\theta\cos\theta$，$\cos(2\theta) = 1 - 2\sin^2\theta$：

$$
\frac{\sin(2\theta)}{1 - \cos(2\theta)} = \frac{2\sin\theta\cos\theta}{1 - (1 - 2\sin^2\theta)}
$$

化简分母：

$$
= \frac{2\sin\theta\cos\theta}{2\sin^2\theta}
$$

约去 $2\sin\theta$（假设 $\sin\theta \neq 0$）：

$$
= \frac{\cos\theta}{\sin\theta} = \cot\theta
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 8（综合策略）**：证明 $\sin x \tan x + \cos x = \sec x$。

> 这是考纲中明确列出的例题类型。

**证明**：

从左边开始，将 $\tan x$ 化为 $\frac{\sin x}{\cos x}$：

$$
\sin x \tan x + \cos x = \sin x \cdot \frac{\sin x}{\cos x} + \cos x
$$

$$
= \frac{\sin^2 x}{\cos x} + \cos x
$$

将 $\cos x$ 写为 $\frac{\cos^2 x}{\cos x}$，通分：

$$
= \frac{\sin^2 x + \cos^2 x}{\cos x}
$$

由 $\sin^2 x + \cos^2 x = 1$：

$$
= \frac{1}{\cos x} = \sec x
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 9（综合策略——含分式）**：证明 $\dfrac{\cos\theta}{1 - \tan\theta} + \dfrac{\sin\theta}{1 - \cot\theta} = \sin\theta + \cos\theta$。

**证明**：

从左边开始。先将 $\tan\theta = \frac{\sin\theta}{\cos\theta}$ 和 $\cot\theta = \frac{\cos\theta}{\sin\theta}$ 代入：

第一项：

$$
\frac{\cos\theta}{1 - \frac{\sin\theta}{\cos\theta}} = \frac{\cos\theta}{\frac{\cos\theta - \sin\theta}{\cos\theta}} = \frac{\cos\theta \cdot \cos\theta}{\cos\theta - \sin\theta} = \frac{\cos^2\theta}{\cos\theta - \sin\theta}
$$

第二项：

$$
\frac{\sin\theta}{1 - \frac{\cos\theta}{\sin\theta}} = \frac{\sin\theta}{\frac{\sin\theta - \cos\theta}{\sin\theta}} = \frac{\sin\theta \cdot \sin\theta}{\sin\theta - \cos\theta} = \frac{\sin^2\theta}{\sin\theta - \cos\theta}
$$

注意第二项的分母 $\sin\theta - \cos\theta = -(\cos\theta - \sin\theta)$。

因此左边为：

$$
\frac{\cos^2\theta}{\cos\theta - \sin\theta} + \frac{\sin^2\theta}{-(\cos\theta - \sin\theta)}
$$

$$
= \frac{\cos^2\theta - \sin^2\theta}{\cos\theta - \sin\theta}
$$

利用平方差公式：

$$
= \frac{(\cos\theta - \sin\theta)(\cos\theta + \sin\theta)}{\cos\theta - \sin\theta}
$$

约去 $\cos\theta - \sin\theta$（假设 $\cos\theta \neq \sin\theta$）：

$$
= \cos\theta + \sin\theta
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

**例题 10（考纲举例题——第二种形式）**：证明 $\dfrac{\cos\theta}{1 + \sin\theta} + \dfrac{1 + \sin\theta}{\cos\theta} = 2\sec\theta$。

**证明**：

从左边开始，通分：

$$
\frac{\cos\theta}{1 + \sin\theta} + \frac{1 + \sin\theta}{\cos\theta}
= \frac{\cos^2\theta + (1 + \sin\theta)^2}{\cos\theta(1 + \sin\theta)}
$$

展开分子：

$$
\cos^2\theta + 1 + 2\sin\theta + \sin^2\theta
$$

利用 $\cos^2\theta + \sin^2\theta = 1$：

$$
= (\cos^2\theta + \sin^2\theta) + 1 + 2\sin\theta = 1 + 1 + 2\sin\theta = 2 + 2\sin\theta
$$

提取公因式 $2(1 + \sin\theta)$：

$$
= \frac{2(1 + \sin\theta)}{\cos\theta(1 + \sin\theta)} = \frac{2}{\cos\theta} = 2\sec\theta
$$

左边 $=$ 右边，恒等式得证。$\blacksquare$

---

> **证明总结**：三角恒等式的证明本质上是一个"化简-转化"的过程。最重要的是熟悉三个基本恒等式和代数运算技巧，从较复杂的一边开始，逐步向另一边靠拢。如果一种方法行不通，试试从另一边开始，或者换一种转化策略。

---

## 本章知识结构总览

```
第8章：三角学（含弧度法）
│
├── 8.1 弧度制
│   ├── 定义：1 弧度 = 弧长等于半径时的圆心角
│   ├── 换算：180° = π 弧度
│   ├── 弧长公式：s = rθ（θ 必须为弧度）
│   ├── 扇形面积：A = ½r²θ
│   └── 弓形面积：A = ½r²(θ - sinθ)
│
├── 8.2 六个三角函数（任意角）
│   ├── 单位圆定义：sinθ = y, cosθ = x, tanθ = y/x
│   ├── secθ = 1/cosθ, cscθ = 1/sinθ, cotθ = 1/tanθ
│   ├── 特殊角的值（0, π/6, π/4, π/3, π/2 等）
│   ├── ASTC 符号法则
│   └── 参考角法：求任意角三角函数值
│
├── 8.3 三角函数的图像
│   ├── y = sin x（周期 2π，值域 [-1,1]，奇函数）
│   ├── y = cos x（周期 2π，值域 [-1,1]，偶函数）
│   ├── y = tan x（周期 π，渐近线 x = π/2 + nπ）
│   ├── y = sec x, csc x, cot x 的图像
│   └── 变换：y = a sin(bx + c) + d 的参数分析
│
├── 8.4 三角恒等式
│   ├── sin²θ + cos²θ = 1
│   ├── sec²θ = 1 + tan²θ
│   ├── csc²θ = 1 + cot²θ
│   ├── 二倍角公式（推导及应用）
│   └── 半角公式（降次用）
│
├── 8.5 解三角方程
│   ├── 基本形式：sin x = k, cos x = k, tan x = k
│   ├── 利用恒等式转化（化为同名函数）
│   ├── 二次型方程（换元法）
│   ├── a sin(kθ) + b cos(kθ) = 0 型
│   └── 含复合角（如 cos(2θ) = k）的方程
│
└── 8.6 三角恒等式的证明
    ├── 策略 1：化为 sin 和 cos
    ├── 策略 2：通分合并
    ├── 策略 3：分子分母同乘共轭式
    ├── 策略 4：利用基本恒等式
    ├── 策略 5：因式分解
    └── 策略 6：利用二倍角公式
```

---
---

---

