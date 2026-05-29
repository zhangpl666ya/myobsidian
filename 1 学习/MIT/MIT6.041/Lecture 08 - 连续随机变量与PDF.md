# Lecture 08: 连续随机变量与 PDF

> **课程：** MIT 6.041 - 概率系统分析与应用概率
> **讲师：** Prof. John Tsitsiklis
> **教材：** *Introduction to Probability* 2nd ed. — Bertsekas & Tsitsiklis
> **阅读：** Sections 3.1–3.3

---

## 1. 连续随机变量 vs 离散随机变量

| | 离散 R.V. | 连续 R.V. |
|---|---|---|
| 概率描述 | PMF $p_X(x) = P(X=x)$ | PDF $f_X(x)$（密度，非概率） |
| 概率计算 | $P(X \in S) = \sum_{x \in S} p_X(x)$ | $P(X \in S) = \int_S f_X(x)dx$ |
| 归一化 | $\sum_x p_X(x) = 1$ | $\int_{-\infty}^{+\infty} f_X(x)dx = 1$ |
| 单点概率 | $P(X=a) > 0$ | $P(X=a) = 0$（**注意！**） |

---

## 2. PDF 的定义与直观理解

**定义：** 若 $P(x \leq X \leq x+\delta) \approx f_X(x) \cdot \delta$，则 $f_X(x)$ 是 $X$ 的 PDF。

即：**PDF 在 $x$ 处的值 = 概率密度**。区间越小，概率近似等于密度乘以区间长度。

**注意：** $f_X(x)$ 可以大于 1（只要积分归一）。它是"单位长度上的概率"，不是概率本身。

---

## 3. 累积分布函数（CDF）

$$F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t)dt$$

**性质：**

$$f_X(x) = \frac{dF_X(x)}{dx}$$

$$P(a < X \leq b) = F_X(b) - F_X(a)$$

连续情况下 $P(a \leq X \leq b) = P(a < X < b) = F_X(b) - F_X(a)$（因为单点概率为 0）。

---

## 4. 连续均匀分布 Uniform(a, b)

$$f_X(x) = \begin{cases} \dfrac{1}{b-a}, & a \leq x \leq b \\ 0, & \text{otherwise} \end{cases}$$

$$E[X] = \frac{a+b}{2}, \quad \text{var}(X) = \frac{(b-a)^2}{12}$$

---

## 5. 正态（高斯）分布 Normal($\mu, \sigma^2$)

### 标准正态 $N(0,1)$

$$f_Y(y) = \frac{1}{\sqrt{2\pi}} e^{-y^2/2}$$

对称于 $y=0$，峰值为 $1/\sqrt{2\pi}$。

### 一般正态 $N(\mu, \sigma^2)$

$$f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/2\sigma^2}$$

**性质：**

$$E[X] = \mu, \quad \text{var}(X) = \sigma^2$$

**线性变换：** 若 $X \sim N(\mu, \sigma^2)$，则

$$Y = aX + b \sim N(a\mu + b, \; a^2\sigma^2)$$

### 计算正态概率

若 $X \sim N(\mu, \sigma^2)$：

$$P(X \leq x) = \Phi\!\left(\frac{x-\mu}{\sigma}\right)$$

其中 $\Phi$ 是标准正态 CDF（查表）。

**例：** $X \sim N(2, 16)$（$\sigma = 4$），求 $P(X \leq 3)$：

$$\frac{3-2}{4} = 0.25 \quad \Rightarrow \quad \Phi(0.25) \approx 0.5987$$

### 对称公式

$$\Phi(-z) = 1 - \Phi(z)$$

---

## 6. 混合分布（Mixed Distributions）

离散和连续成分的混合，既有 PDF 又有 PMF。

**例：** $P(X=0) = \tfrac{1}{2}$，$X$ 在 $(0,1)$ 上连续均匀时 $P(X \in (0,1)) = \tfrac{1}{2}$。

对应 CDF：

$$F_X(x) = \begin{cases} 0, & x < 0 \\ \frac{1}{2}, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

混合分布在实际中常见（如保险理赔金额：大部分为 0，少量大幅赔偿）。

---

## 7. 连续随机变量的期望与方差

### 一般公式

$$E[X] = \int_{-\infty}^{+\infty} x \, f_X(x) \, dx$$

$$E[g(X)] = \int_{-\infty}^{+\infty} g(x) \, f_X(x) \, dx$$

> **警告：** $E[g(X)] \neq g(E[X])$（Jensen 不等式：若 $g$ 为凸函数，$E[g(X)] \geq g(E[X])$）

### 方差

$$\text{var}(X) = E[X^2] - (E[X])^2 = \int (x - E[X])^2 f_X(x) \, dx$$

---

## 8. 正态分布的"星火"（Key Insight）

正态分布在自然界极为普遍，原因是：**大量独立小效应之和趋近正态分布**（中心极限定理）。

这也解释了为什么正态分布在统计中无处不在。

---

## 本讲要点

| 概念 | 公式 |
|------|------|
| PDF 定义 | $P(x \leq X \leq x+\delta) \approx f_X(x)\delta$ |
| 归一化 | $\int_{-\infty}^{+\infty} f_X(x)dx = 1$ |
| CDF | $F_X(x) = \int_{-\infty}^{x} f_X(t)dt$ |
| 期望 | $E[X] = \int x f_X(x)dx$ |
| $E[g(X)]$ | $\int g(x) f_X(x)dx$ |
| 均匀分布 | $E[X] = (a+b)/2$，$\text{var} = (b-a)^2/12$ |
| 正态分布 $N(\mu,\sigma^2)$ | $f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/2\sigma^2}$ |
| 正态线性变换 | $aX+b \sim N(a\mu+b, a^2\sigma^2)$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 8 内容整理*