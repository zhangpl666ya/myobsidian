---
tags:
  - "学习/MIT6.041"
  - "学习/概率论"
  - "笔记/课程笔记"
---
#  Lecture 06: 条件PMF、几何分布与联合分布

> **课程：** MIT 6.041 - 概率系统分析与应用概率  
> **讲师：** Prof. John Tsitsiklis  
> **教材：** 《Introduction to Probability》2nd ed. — Bertsekas & Tsitsiklis  
> **阅读：** Sections 2.4–2.6

---

##  1. 复习

| 概念 | 公式 |
|------|------|
| 随机变量 | $X: \Omega \to \mathbb{R}$ |
| PMF | $p_X(x) = P(X = x)$ |
| 期望 | $E[X] = \sum_x x \cdot p_X(x)$ |
| $E[g(X)]$ | $E[g(X)] = \sum_x g(x) \cdot p_X(x)$ |
| 线性性质 | $E[\alpha X + \beta] = \alpha E[X] + \beta$ |
| 方差 | $\text{var}(X) = E[X^2] - (E[X])^2$ |
| 标准差 | $\sigma_X = \sqrt{\text{var}(X)}$ |

---

##  2. 条件 PMF 与条件期望

### 定义

$$p_{X|A}(x) = P(X = x \mid A) = \frac{P(X = x \text{ 且 } A)}{P(A)}$$

$$E[X \mid A] = \sum_x x \cdot p_{X|A}(x)$$

### 例题

设 $X$ 的 PMF：

| $x$ | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|
| $p_X(x)$ | $1/4$ | $1/4$ | $1/4$ | $1/4$ |

令 $A = \{X \geq 2\}$

则：
$$p_{X|A}(x) = \frac{p_X(x)}{P(X \geq 2)} = \frac{p_X(x)}{3/4} = \frac{1}{3}, \quad x = 2, 3, 4$$

$$E[X \mid A] = \frac{1}{3}(2 + 3 + 4) = 3$$

---

##  3. 几何分布的"无记忆性"（Memoryless Property）

### 定理

对几何分布 $X \sim \text{Geometric}(p)$，有：

$$P(X > s + t \mid X > s) = P(X > t), \quad \forall s, t \geq 0$$

### 含义

已知前 $s$ 次都失败了，剩余试验次数的分布与从头开始完全相同——过去的信息对未来没有影响。

### 条件分布恒等于原始分布

$$p_{X|X>s}(k) = p_X(k) = (1-p)^{k-1}p, \quad k = 1, 2, \ldots$$

（注意：这里从 $k=1$ 开始是**相对**的剩余次数）

---

##  4. 全期望定理（Total Expectation Theorem）

### 定理

设 $A_1, A_2, \ldots, A_n$ 是样本空间的一个划分（互斥、穷举），则：

$$\boxed{E[X] = \sum_{i=1}^{n} P(A_i) \cdot E[X \mid A_i]}$$

### 证明

$$E[X] = \sum_i P(A_i) E[X \mid A_i] = \sum_i P(A_i) \sum_x x \cdot p_{X|A_i}(x) = \sum_x x \sum_i P(A_i) p_{X|A_i}(x) = \sum_x x \cdot p_X(x)$$

---

##  5. 几何分布的全期望定理应用

设 $X \sim \text{Geometric}(p)$，令：

- $A_1 = \{X = 1\}$（第一次就成功）
- $A_2 = \{X > 1\}$（第一次失败，还需要更多试验）

$$E[X] = P(X=1) \cdot E[X \mid X=1] + P(X>1) \cdot E[X \mid X>1]$$

- $P(X=1) = p$；此时 $E[X \mid X=1] = 1$
- $P(X>1) = 1-p$；第一次失败后，剩余次数还是同样的几何分布，所以 $E[X \mid X>1] = 1 + E[X]$

设 $E[X] = \mu$，则：

$$\mu = p \cdot 1 + (1-p) \cdot (1 + \mu) = 1 + (1-p)\mu$$

$$\mu - (1-p)\mu = 1 \implies p\mu = 1 \implies \mu = \frac{1}{p}$$

---

##  6. 联合 PMF（Joint PMF）

### 定义

$$p_{X,Y}(x, y) = P(X = x \text{ 且 } Y = y)$$

### 性质

- $p_{X,Y}(x,y) \geq 0$
- $\displaystyle\sum_x \sum_y p_{X,Y}(x,y) = 1$

### 边缘 PMF

从联合 PMF 推导出单个变量的 PMF：

$$p_X(x) = \sum_y p_{X,Y}(x, y)$$

$$p_Y(y) = \sum_x p_{X,Y}(x, y)$$

### 条件 PMF（从联合分布）

$$p_{X|Y}(x \mid y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}$$

---

##  7. 例题：联合 PMF 表

| $p_{X,Y}(x,y)$ | $Y=1$ | $Y=2$ | $Y=3$ | $Y=4$ | $p_X(x)$ |
|----------------|-------|-------|-------|-------|---------|
| $X=1$ | $1/20$ | $2/20$ | $2/20$ | $2/20$ | $7/20$ |
| $X=2$ | $2/20$ | $4/20$ | $1/20$ | $2/20$ | $9/20$ |
| $X=3$ | $1/20$ | $3/20$ | $1/20$ | $1/20$ | $6/20$ |

### 边缘分布验算（$p_Y(y)$）

每列相加：$p_Y(1) = \frac{1+2+1}{20} = \frac{4}{20}$，等等。

### 条件分布

$$p_{X|Y=2}(x) = \frac{p_{X,Y}(x, 2)}{p_Y(2)} = \frac{p_{X,Y}(x, 2)}{9/20} = \frac{2}{9}, \frac{4}{9}, \frac{3}{9}, \quad x=1,2,3$$

---

##  8. 平均速度 vs. 穿越时间

### 情景

以随机速度 $V$ 穿越 200 英里，速度 $V \sim \text{Uniform}\{1, 200\}$（但实际是离散均匀：$P(V=1) = P(V=200) = 1/2$，中间速度省略）

### 定义

- 速度 $V$：PMF 为 $p_V(1) = p_V(200) = 1/2$
- 时间 $T = t(V) = 200 / V$

### 计算

$$E[V] = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot 200 = 100.5$$

$$E[T] = E[200/V] = \frac{1}{2} \cdot 200 + \frac{1}{2} \cdot 1 = 100.5$$

**重要结论：**

$$E[T] = \frac{200}{E[V]} = \frac{200}{100.5} = E[200/V] \quad \text{—— 注意这是特殊情况，不是通式！}$$

这是因为 $V$ 只取两个值，$E[200/V] = 200 \cdot E[1/V]$ 恰好等于 $200/E[V]$ 才成立。**一般情况下 $E[1/V] \neq 1/E[V]$。**

---

##  本讲要点

| 概念     | 公式                                           |
| ------ | -------------------------------------------- |
| 条件 PMF | $p_{X\|A}(x) = P(X=x \mid A)$                |
| 几何无记忆性 | $P(X > s+t \mid X > s) = P(X > t)$           |
| 全期望定理  | $E[X] = \sum_i P(A_i)E[X \mid A_i]$          |
| 几何分布期望 | $E[X] = 1/p$                                 |
| 联合 PMF | $p_{X,Y}(x,y) = P(X=x, Y=y)$                 |
| 边缘 PMF | $p_X(x) = \sum_y p_{X,Y}(x,y)$               |
| 条件 PMF | $p_{X\|Y}(x \mid y) = p_{X,Y}(x,y) / p_Y(y)$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 6 内容整理*

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[Lecture 05 - 随机变量]]
- [[Lecture 07 - 多元随机变量与帽子问题]]
- [[课程导学]]
