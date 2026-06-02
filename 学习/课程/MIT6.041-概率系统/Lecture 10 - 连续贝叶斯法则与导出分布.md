---
tags:
  - "学习/MIT6.041"
  - "学习/概率论"
  - "笔记/课程笔记"
---
# Lecture 10: 连续贝叶斯法则与导出分布

> **课程：** MIT 6.041 - 概率系统分析与应用概率
> **讲师：** Prof. John Tsitsiklis
> **教材：** *Introduction to Probability* 2nd ed. — Bertsekas & Tsitsiklis
> **阅读：** Section 3.6; start Section 4.1

---

## 1. 连续贝叶斯法则的几种情形

### 情形 1：离散先验 + 连续似然

**场景：** $X$ 是离散信号（取值为 0 或 1，表示飞机是否出现），$Y$ 是连续观测（雷达回波强度）。

$$p_{X \mid Y}(x \mid y) = \frac{p_X(x) \, f_{Y \mid X}(y \mid x)}{f_Y(y)}, \quad x \in \{0,1\}$$

其中：

$$f_Y(y) = p_X(0) \, f_{Y \mid X}(y \mid 0) + p_X(1) \, f_{Y \mid X}(y \mid 1)$$

这与离散贝叶斯公式完全对应，只是分母是连续混合（加权求和）。

### 情形 2：连续先验 + 离散观测

**场景：** $X \sim f_X(x)$（连续信号，如光强），$Y$ 是离散光子计数。

$$f_{X \mid Y}(x \mid y) = \frac{f_X(x) \, p_{Y \mid X}(y \mid x)}{p_Y(y)}$$

其中：

$$p_Y(y) = \int f_X(x) \, p_{Y \mid X}(y \mid x) \, dx$$

### 情形 3：连续先验 + 连续似然（完全连续）

$$f_{X \mid Y}(x \mid y) = \frac{f_X(x) \, f_{Y \mid X}(y \mid x)}{f_Y(y)}$$

其中：

$$f_Y(y) = \int_{-\infty}^{+\infty} f_X(x) \, f_{Y \mid X}(y \mid x) \, dx$$

---

## 2. 导出分布（Derived Distribution）

**问题：** 已知 $X$ 的分布，$Y = g(X)$，求 $Y$ 的分布。

**何时需要：** 求某个随机变量函数的概率密度，如 $Y = X^2$，$Y = e^X$，$Y = aX+b$ 等。

**何时不需要：** 如果只求期望，可以直接用 $E[Y] = E[g(X)] = \int g(x) f_X(x) dx$，不需要先求 $f_Y$。

---

## 3. 离散情况的导出分布

对离散 $X$：

$$p_Y(y) = \sum_{x: g(x) = y} p_X(x)$$

**例：** $X \sim \text{Binomial}(n,p)$，$Y = g(X) = \text{某个映射}$，则逐值求和。

---

## 4. 单调变换的 PDF（连续情况）

设 $Y = g(X)$，$g$ **严格单调**。

**核心思路：** 概率不变——$X$ 落在小区间 $[x, x+\delta]$ 的概率 $\approx f_X(x)\delta$，等于 $Y$ 落在对应区间 $[y, y+\delta']$ 的概率 $\approx f_Y(y)\delta'$。

由 $y = g(x)$，$\delta' \approx \left|\frac{dg}{dx}(x)\right| \delta$，得到：

$$\boxed{f_Y(y) = \frac{f_X(x)}{\left|\frac{dg}{dx}(x)\right|}, \quad x = g^{-1}(y)}$$

**直观：** 概率守恒——密度被导数重新"拉伸"了。

### 例：$Y = 3X$，$X \sim \text{Uniform}[0,2]$

- $g(x) = 3x$，$\frac{dg}{dx} = 3$
- $g^{-1}(y) = y/3$，取值范围 $0 \leq y \leq 6$

$$f_Y(y) = f_X(y/3) \cdot \frac{1}{3} = 1 \cdot \frac{1}{3} = \frac{1}{3}, \quad 0 \leq y \leq 6$$

验证：$\int_0^6 \frac{1}{3} dy = 2 \neq 1$？等等…… $X \in [0,2]$，所以 $Y \in [0,6]$，长度 6，均匀密度 $1/3$，$\int_0^6 \frac{1}{3} dy = 2$，这还是不对。

让我重新算：$f_X(x) = 1/2$（因为 $X \sim U[0,2]$）。所以：

$$f_Y(y) = \frac{1/2}{3} = \frac{1}{6}, \quad 0 \leq y \leq 6 \checkmark$$

（$\int_0^6 \frac{1}{6} dy = 1$）

### 例：$Y = aX + b$（线性变换）

$$f_Y(y) = \frac{1}{|a|} f_X\!\left(\frac{y-b}{a}\right)$$

**特别地：** 若 $X \sim N(\mu, \sigma^2)$，则 $Y = aX+b \sim N(a\mu+b, a^2\sigma^2)$。

---

## 5. 非单调变换的导出分布（两步法）

**步骤：**

1. 求 $Y$ 的 CDF：$F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$
2. 对 CDF 求导：$f_Y(y) = \dfrac{dF_Y(y)}{dy}$

### 例：$Y = X^2$，$X \sim \text{Uniform}[0,2]$

1. $F_Y(y) = P(X^2 \leq y) = P(X \leq \sqrt{y}) = \dfrac{\sqrt{y}}{2}$，$0 \leq y \leq 4$
2. $f_Y(y) = \dfrac{d}{dy}\left(\dfrac{\sqrt{y}}{2}\right) = \dfrac{1}{4\sqrt{y}}$，$0 < y \leq 4$

验证：$\int_0^4 \frac{1}{4\sqrt{y}} dy = \frac{1}{2} \cdot [2\sqrt{y}]_0^4 = \frac{1}{2} \cdot 4 = 2 \neq 1$... 哪里出错了？

**重新检查：** $\int_0^4 \frac{1}{4\sqrt{y}} dy = \frac{1}{4} \cdot [2\sqrt{y}]_0^4 = \frac{1}{4} \cdot 4 = 1$ ✓

---

## 6. 逆 CDF 方法（指数分布例子）

**例：** $X \sim \text{Uniform}[0,1]$，$Y = -\frac{1}{\lambda} \ln(1-X)$

**验证：** 先求 CDF
$$F_Y(y) = P(Y \leq y) = P\left(-\frac{1}{\lambda}\ln(1-X) \leq y\right) = P(1-X \geq e^{-\lambda y}) = P(X \leq 1-e^{-\lambda y})$$
由于 $X \sim U[0,1]$：
$$F_Y(y) = 1-e^{-\lambda y}, \quad y \geq 0$$
对 $y$ 求导：$f_Y(y) = \lambda e^{-\lambda y}$，即 $Y \sim \text{Exp}(\lambda)$ ✓

**核心洞察：** 如果 $X \sim U[0,1]$，$F^{-1}(X) \sim F$（逆变换采样法）

---

## 7. 实际应用：行程时间问题

**问题：** 从波士顿开车去纽约，速度 $V \sim \text{Uniform}[30,60]$ mph，路程 200 英里。求行程时间 $T = 200/V$ 的分布。

**分析：** $V$ 均匀，$T = 200/V$ 是单调递减函数（非单调！）。用 CDF 法：

- $v \in [30,60]$，$t = 200/v \in [200/60, 200/30] = [3.33, 6.67]$
- $F_T(t) = P(T \leq t) = P(200/V \leq t) = P(V \geq 200/t) = 1 - F_V(200/t)$
- $f_T(t) = \frac{d}{dt}F_T(t) = -f_V(200/t) \cdot (-200/t^2) = \frac{200}{t^2} \cdot \frac{1}{30}$（当 $3.33 \leq t \leq 6.67$）

---

## 本讲要点

| 概念 | 公式 |
|------|------|
| 连续贝叶斯（混合） | $f_{X \mid Y}(x \mid y) = f_X(x) f_{Y \mid X}(y \mid x) / f_Y(y)$ |
| 导出分布条件 | 不需要 $f_Y$ 时可直接算期望 |
| 单调变换 PDF | $f_Y(y) = f_X(x) / \|g'(x)\|$，$x = g^{-1}(y)$ |
| 线性变换 | $f_Y(y) = \frac{1}{\|a\|} f_X((y-b)/a)$ |
| 两步法 | $F_Y(y) = P(g(X) \leq y)$，$f_Y = dF_Y/dy$ |
| $N(\mu,\sigma^2)$ 线性变换 | $aX+b \sim N(a\mu+b, a^2\sigma^2)$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 10 内容整理*

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[Lecture 09 - 多元连续随机变量与条件分布]]
- [[Lecture 11 - 卷积、协方差与相关性]]
- [[课程导学]]
