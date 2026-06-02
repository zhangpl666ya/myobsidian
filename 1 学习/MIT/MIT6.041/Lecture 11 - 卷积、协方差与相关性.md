---
tags:
  - "学习/MIT6.041"
  - "学习/概率论"
  - "笔记/课程笔记"
---
# Lecture 11: 多元函数导出分布、卷积、协方差与相关性

> **课程：** MIT 6.041 - 概率系统分析与应用概率
> **讲师：** Prof. John Tsitsiklis
> **教材：** *Introduction to Probability* 2nd ed. — Bertsekas & Tsitsiklis
> **阅读：** Finish Section 4.1; Section 4.2

---

## 1. 一般情形：$Z = g(X,Y)$ 的分布

### 两步法（通用）

1. 求 $Z$ 的 CDF：$F_Z(z) = P(g(X,Y) \leq z)$
2. 求导得 PDF：$f_Z(z) = \dfrac{dF_Z(z)}{dz}$

### 例：$Z = Y/X$，$X,Y$ 在 $[0,1] \times [0,1]$ 上均匀独立

$$F_Z(z) = P(Y/X \leq z) = \int_0^1 \int_0^{\min(1, zx)} dy \, dx$$

几何理解：$(X,Y)$ 在单位正方形中，$Y \leq zX$ 区域为三角形/梯形，$F_Z(z)$ 为该区域面积。

---

## 2. 卷积：$W = X + Y$ 的分布

### 离散情况（独立）

若 $X,Y$ 独立离散：

$$p_W(w) = \sum_x p_X(x) \, p_Y(w-x) = \sum_y p_X(w-y) \, p_Y(y)$$

**操作：** 将两个 PMF "重叠"、翻转其中一个、逐点相乘求和——这就是卷积的本质。

### 连续情况（独立）

若 $X,Y$ 独立连续：

$$\boxed{f_W(w) = \int_{-\infty}^{+\infty} f_X(x) \, f_Y(w-x) \, dx}$$

**推导：** $f_W(w) = \int f_{W \mid X}(w \mid x) \, f_X(x) \, dx = \int f_Y(w-x) \, f_X(x) \, dx$

几何理解：对每个固定的 $w$，$Y = w - X$ 是一条直线，沿该线"扫描"联合密度并积分。

**另一种形式（交换 $X,Y$）：**

$$f_W(w) = \int_{-\infty}^{+\infty} f_Y(y) \, f_X(w-y) \, dy$$

两个式子本质相同。

---

## 3. 正态分布对卷积封闭

### 关键结论

若 $X \sim N(\mu_X, \sigma_X^2)$，$Y \sim N(\mu_Y, \sigma_Y^2)$，且独立，则：

$$W = X + Y \sim N(\mu_X + \mu_Y, \; \sigma_X^2 + \sigma_Y^2)$$

**证明思路：** 利用卷积公式和指数函数的性质，通过积分得到正态密度。

**注意：** 这里要求 $X$ 与 $Y$ 独立。不独立时，方差不再是简单相加。

**扩展：** $aX+b \sim N(a\mu+b, a^2\sigma^2)$；独立正态的和仍为正态，参数直接相加。

---

## 4. 协方差（Covariance）

### 定义

$$\text{cov}(X,Y) = E\!\left[(X - E[X])(Y - E[Y])\right] = E[XY] - E[X]E[Y]$$

**零均值情形：** $\text{cov}(X,Y) = E[XY]$

### 性质

| 性质 | 公式 |
|------|------|
| 对称 | $\text{cov}(X,Y) = \text{cov}(Y,X)$ |
| 与自身 | $\text{cov}(X,X) = \text{var}(X)$ |
| 线性性 | $\text{cov}(aX+b, Y) = a \, \text{cov}(X,Y)$ |
| 相加性 | $\text{cov}(X+Y, Z) = \text{cov}(X,Z) + \text{cov}(Y,Z)$ |

### 协方差与方差的加法

$$\text{var}(X+Y) = \text{var}(X) + \text{var}(Y) + 2\,\text{cov}(X,Y)$$

更一般地，对多个变量：

$$\text{var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{var}(X_i) + 2\sum_{i<j} \text{cov}(X_i, X_j)$$

---

## 5. 相关系数（Correlation Coefficient）

### 定义

$$\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y}$$

**注意：** 相关系数是**无量纲**（ dimensionless）的，消除了量纲影响。

### 性质：$-1 \leq \rho \leq 1$

**$\rho = 1$：** 完全正线性相关 $X - E[X] = c(Y - E[Y])$（$c > 0$）

**$\rho = -1$：** 完全负线性相关 $X - E[X] = -c(Y - E[Y])$（$c > 0$）

**$|\rho| = 1$：** $X$ 与 $Y$ 呈**完全线性关系**（在一条直线上）

---

## 6. 不相关（Uncorrelated）vs 独立（Independent）

### 核心区别

| 关系 | 含义 | 公式 |
|------|------|------|
| **独立** | 联合分布 = 边际分布的乘积 | $p_{X,Y} = p_X p_Y$ 或 $f_{X,Y} = f_X f_Y$ |
| **不相关** | 协方差为零 | $E[XY] = E[X]E[Y]$，即 $\text{cov}(X,Y) = 0$ |

### 关键蕴涵关系

$$X, Y \text{ 独立} \quad \Rightarrow \quad X, Y \text{ 不相关}$$

（独立 → 联合分布可分解 → $E[XY] = E[X]E[Y]$ → 协方差为 0）

**但反过来不一定成立！**

**不相关 ≠ 独立 的反例：**

设 $X \sim U[-1,1]$，$Y = X^2$。则：
- $E[X] = 0$，$E[Y] = E[X^2] = \frac{1}{3}$
- $E[XY] = E[X^3] = 0$（奇函数对称）
- $\text{cov}(X,Y) = 0$（不相关）
- 但 $Y = X^2$ 完全由 $X$ 决定，**不独立**

**另一个反例：** $X \sim \text { Bernoulli}(0.5)$，$Y = 1-X$（完全负相关，$\rho = -1$，但不独立，因为 $P(X=0, Y=0) = 0 \neq P(X=0)P(Y=0) = 0.25$）

---

## 7. 独立与不相关的记忆要点

**独立 = 联合分布可分解 = 一切条件下的概率都可以分解**

**不相关 = 协方差为零 = 只要求 $E[XY] = E[X]E[Y]$**

判断关系时，从强到弱：

$$\text{独立} \Rightarrow \text{不相关} \quad \text{（反向不一定成立）}$$

---

## 本讲要点

| 概念 | 公式 |
|------|------|
| 卷积（连续） | $f_W(w) = \int f_X(x) f_Y(w-x) dx$ |
| 正态 + 卷积 | $N(\mu_1,\sigma_1^2) + N(\mu_2,\sigma_2^2) \sim N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ |
| 协方差 | $\text{cov}(X,Y) = E[XY] - E[X]E[Y]$ |
| 相关系数 | $\rho = \text{cov}(X,Y) / (\sigma_X\sigma_Y)$ |
| $-1 \leq \rho \leq 1$ | $\rho = \pm 1$ 当且仅当完全线性相关 |
| $\text{var}(X+Y)$ | $\text{var}(X) + \text{var}(Y) + 2\text{cov}(X,Y)$ |
| 独立 → 不相关 | 独立 $ \Rightarrow E[XY] = E[X]E[Y]$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 11 内容整理*

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[1 学习/MIT/MIT6.041/Lecture 10 - 连续贝叶斯法则与导出分布]]
- [[1 学习/MIT/MIT6.041/课程导学]]
