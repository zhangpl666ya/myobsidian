---
tags:
  - "学习/MIT6.041"
  - "学习/概率论"
  - "笔记/课程笔记"
---
#  Lecture 05: 随机变量

> **课程：** MIT 6.041 - 概率系统分析与应用概率  
> **讲师：** Prof. John Tsitsiklis  
> **教材：** 《Introduction to Probability》2nd ed. — Bertsekas & Tsitsiklis  
> **阅读：** Sections 2.1–2.3, 2.4（部分）

---

##  1. 随机变量的定义

**随机变量**是一个函数，将样本空间中的每个Outcome映射为一个实数值：

$$X: \Omega \to \mathbb{R}$$

- 每个Outcome $\omega$ 被赋予一个数值 $X(\omega)$
- 可以有多个随机变量定义在同一个样本空间上
- 根据取值类型分为**离散**和**连续**两类

> 注意：随机变量是**确定性的函数**，不是"随机"的数——它只是每个Outcome对应一个数值。

---

##  2. 概率质量函数（PMF）

### 定义

$$p_X(x) = P(X = x) = P(\{\omega \in \Omega \mid X(\omega) = x\})$$

PMF 给出随机变量取每个特定值的概率。

### 性质

| 性质 | 公式 |
|------|------|
| 非负性 | $p_X(x) \geq 0,\ \forall x$ |
| 归一性 | $\displaystyle\sum_x p_X(x) = 1$ |

### 如何求 PMF

对每个可能的 $x$：
1. 找出所有使得 $X = x$ 的Outcome
2. 将这些Outcome的概率相加
3. 对所有 $x$ 重复

---

##  3. 离散均匀分布（0 到 n 的均匀整数）

$$p_X(x) = \frac{1}{n+1}, \quad x = 0, 1, 2, \ldots, n$$

期望：

$$E[X] = \frac{0 + 1 + \cdots + n}{n+1} = \frac{n}{2}$$

---

##  4. 几何分布（Geometric PMF）

### 定义：首次成功所需的试验次数

抛一枚成功率为 $p$ 的硬币（独立重复），$X$ = 首次出现正面所需的抛掷次数。

$$p_X(k) = P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

**验证归一性：**

$$\sum_{k=1}^{\infty} (1-p)^{k-1} p = p \cdot \frac{1}{1-(1-p)} = 1 \checkmark$$

### 几何分布的期望

用等比数列求和推导：

$$E[X] = \sum_{k=1}^{\infty} k \cdot (1-p)^{k-1} p = \frac{1}{p}$$

---

##  5. 二项分布（Binomial PMF）

### 定义：n 次独立伯努利试验中的成功次数

$X \sim \text{Binomial}(n, p)$

$$p_X(k) = P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

### 例子：n = 4 时恰好 2 次正面

$$P(X=2) = \binom{4}{2} p^2 (1-p)^2 = 6 p^2 (1-p)^2$$

其中 $\binom{4}{2} = 6$ 是 4 次抛掷中出现恰好 2 次正面的不同序列数（HHTT, HTHT, HTTH, THHT, THTH, TTHH）。

---

##  6. 期望（Expectation）

### 定义

$$E[X] = \sum_x x \cdot p_X(x)$$

### 物理含义

- **重心**：PMF 图像的"平衡点"
- **长期平均**：大量重复试验中 $X$ 的平均值

### 期望的性质

| 公式 | 说明 |
|------|------|
| $E[\alpha] = \alpha$ | 常数的期望是它本身 |
| $E[\alpha X] = \alpha E[X]$ | 线性：常数可提出 |
| $E[\alpha X + \beta] = \alpha E[X] + \beta$ | 线性：加法分配 |

### 重要警告

$$\boxed{E[g(X)] \neq g(E[X]) \text{（一般情况下）}}$$

例如：$g(X) = X^2$，有 $E[X^2] \neq (E[X])^2$。

---

##  7. 第二个瞬间：$E[X^2]$

$$E[X^2] = \sum_x x^2 \cdot p_X(x)$$

---

##  8. 方差（Variance）

### 定义

$$\text{var}(X) = E\left[(X - E[X])^2\right] = E[X^2] - (E[X])^2$$

### 性质

| 性质 | 公式 |
|------|------|
| 非负性 | $\text{var}(X) \geq 0$ |
| 常数变换 | $\text{var}(\alpha X + \beta) = \alpha^2 \text{var}(X)$ |
| $E[g(X)]$ 的计算 | $E[g(X)] = \sum_x g(x) \cdot p_X(x)$ |

### 标准差

$$\sigma_X = \sqrt{\text{var}(X)}$$

---

##  9. 例题：两个骰子的最小值

掷两次四面体骰子（各面 1–4），设 $X = \min(F, S)$。

构建 PMF：统计所有 $4 \times 4 = 16$ 个Outcome中 $\min(F,S) = k$ 的情况数。

| $k$ | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|
| $p_X(k)$ | $7/16$ | $5/16$ | $3/16$ | $1/16$ |

验证：$\frac{7+5+3+1}{16} = 1$ ✅

---

##  本讲要点

| 概念 | 公式 |
|------|------|
| 随机变量 | $X: \Omega \to \mathbb{R}$ |
| PMF | $p_X(x) = P(X=x)$，$\sum_x p_X(x) = 1$ |
| 几何分布 | $p_X(k) = (1-p)^{k-1}p$ |
| 二项分布 | $p_X(k) = \binom{n}{k}p^k(1-p)^{n-k}$ |
| 期望 | $E[X] = \sum_x x \cdot p_X(x)$ |
| 方差 | $\text{var}(X) = E[X^2] - (E[X])^2$ |
| 重要警告 | $E[g(X)] \neq g(E[X])$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 5 内容整理*

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[Lecture 04 - 计数原理]]
- [[Lecture 06 - 条件PMF与联合分布]]
- [[课程导学]]
