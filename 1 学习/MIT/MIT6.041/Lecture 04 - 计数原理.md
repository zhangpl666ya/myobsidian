---
tags:
  - "学习/MIT6.041"
  - "学习/概率论"
  - "笔记/课程笔记"
---
#  Lecture 04: 计数原理

> **课程：** MIT 6.041 - 概率系统分析与应用概率  
> **讲师：** Prof. John Tsitsiklis  
> **教材：** 《Introduction to Probability》2nd ed. — Bertsekas & Tsitsiklis  
> **阅读：** Section 1.6

---

##  1. 核心思想

在**等可能**模型中：

$$\boxed{P(A) = \frac{|A|}{|\Omega|} = \frac{\text{事件 } A \text{ 中的Outcome数}}{\text{样本空间总Outcome数}}}$$

因此，**计数**是计算概率的关键。

---

##  2. 基本计数原理（乘法法则）

**情景：** 完成一件事需要 $r$ 个步骤，第 $i$ 步有 $n_i$ 种选择。

$$\boxed{\text{总方法数} = n_1 \cdot n_2 \cdots n_r}$$

### 例：车牌号问题

3 个字母 + 4 个数字（允许重复）：
$$26 \times 26 \times 26 \times 10 \times 10 \times 10 \times 10 = 26^3 \times 10^4$$

**禁止重复**时：
$$26 \times 25 \times 24 \times 10 \times 9 \times 8 \times 7$$

---

##  3. 排列（Permutations）

### 全排列：$n$ 个不同元素的顺序排列数

$$P(n, n) = n!$$

### $k$-排列：从 $n$ 个元素中选 $k$ 个并排序

$$\boxed{P(n, k) = n \cdot (n-1) \cdot (n-2) \cdots (n-k+1) = \frac{n!}{(n-k)!}}$$

> 先逐个选（$n$ 种，$(n-1)$ 种……），再乘积。

---

##  4. 组合（Combinations）

### 定义：从 $n$ 个元素中选 $k$ 个，**不考虑顺序**

$$\boxed{\binom{n}{k} = \frac{n!}{k!(n-k)!}}$$

读作"$n$ 选 $k$"。

### 两种构造思路（殊途同归）

1. **直接法**：逐个选取 $k$ 个元素（有序），然后除以 $k$ 种排序：
   $$\frac{n \cdot (n-1) \cdots (n-k+1)}{k!} = \frac{n!}{k!(n-k)!}$$

2. **间接法**：先从 $n$ 中挑 $k$ 个（$\binom{n}{k}$ 种），再对 $k$ 个全排列（$k!$ 种）：
   $$\binom{n}{k} \cdot k! = \frac{n!}{(n-k)!}$$

### 组合的两个重要性质

- $\binom{n}{k} = \binom{n}{n-k}$（对称性）
- $\displaystyle\sum_{k=0}^{n} \binom{n}{k} = 2^n$（二项式定理）

---

##  5. 分配问题（Partitions）

### 问题类型：将 $n$ 个不同元素分成 $r$ 组，各组大小分别为 $n_1, n_2, \ldots, n_r$（$\sum n_i = n$）。

$$\boxed{\text{方法数} = \frac{n!}{n_1! \cdot n_2! \cdots n_r!}}$$

> **证明：** 从 $n$ 个中先挑 $n_1$ 个（$\binom{n}{n_1}$），再从剩下的挑 $n_2$ 个（$\binom{n-n_1}{n_2}$），依此类推：
> $$\binom{n}{n_1}\binom{n-n_1}{n_2}\cdots\binom{n_r}{n_r} = \frac{n!}{n_1!n_2!\cdots n_r!}$$

---

##  6. 例题：掷骰子

> 掷一枚六面均匀骰子 6 次，求恰好出现 **6 个不同数字** 的概率。

### 样本空间总Outcome数

$$6^6$$

### 有利Outcome数（6 次全不同）

- 第 1 次：任意 6 种
- 第 2 次：5 种（不能与第 1 次相同）
- 第 3 次：4 种
- ……
- 第 6 次：1 种

$$6 \times 5 \times 4 \times 3 \times 2 \times 1 = 6!$$

### 答案

$$P(\text{6 个不同}) = \frac{6!}{6^6} = \frac{720}{46656} \approx 0.015$$

---

##  7. 二项概率

### 模型：独立重复 $n$ 次伯努利试验，$P(H) = p$

### 单个具体序列的概率

$$P(\text{恰好 } k \text{ 次正面，任意位置}) = p^k (1-p)^{n-k}$$

### $k$ 次正面的序列数（二项系数）

$$\boxed{P(k \text{ 次正面}) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}}$$

这就是**二项分布**：$X \sim \text{Binomial}(n, p)$

---

##  8. 例题：硬币问题（续）

> 抛 10 次偏置硬币，恰好 3 次正面。已知恰好有 3 次正面，求**前两次都是正面**的条件概率。

在条件 $B$（恰好 3 次正面）下，所有序列等概率（概率均为 $p^3(1-p)^7$）。

- $B$ 中的总序列数：$\binom{10}{3} = 120$
- $B$ 中前两次为正面的序列：还需在后 8 次中再选 1 次正面 → $\binom{8}{1} = 8$

$$P(\text{前两次} = HH \mid \text{恰好3次正面}) = \frac{8}{120} = \frac{2}{30}$$

---

##  9. 例题：四人分牌

> 将 52 张牌等分给 4 个人，求**每人恰好得到一张 A** 的概率。

### 第一步：每人一张 A 的分配方式

4 张 A 分给 4 人，每人最多 1 张：
$$4! = 24 \text{ 种分配方式}$$

### 第二步：其余 48 张牌的分法

将 48 张牌分成 4 组（每组 12 张）：
$$\frac{48!}{12! \cdot 12! \cdot 12! \cdot 12!}$$

### 第三步：总Outcome数

将全部 52 张牌分成 4 组（每组 13 张）：
$$\frac{52!}{13! \cdot 13! \cdot 13! \cdot 13!}$$

### 答案

$$P(\text{每人一张 A}) = \frac{4! \cdot \dfrac{48!}{12!^4}}{\dfrac{52!}{13!^4}}$$

---

##  本讲要点

| 计数对象 | 公式 |
|----------|------|
| 乘法原理（$r$ 步，每步 $n_i$ 种） | $n_1 \cdot n_2 \cdots n_r$ |
| $n$ 元素的全排列 | $n!$ |
| $n$ 选 $k$ 的排列（有序） | $\frac{n!}{(n-k)!}$ |
| $n$ 选 $k$ 的组合（无序） | $\displaystyle\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| $n$ 分成 $(n_1,\ldots,n_r)$ 的分配 | $\dfrac{n!}{n_1! \cdots n_r!}$ |
| 二项概率 $(n\text{ 次试验，}k\text{ 次成功})$ | $\displaystyle\binom{n}{k}p^k(1-p)^{n-k}$ |

- **计数是概率的基础**——等可能模型下，概率 = 有利数 / 总数
- 组合与排列的核心区别在于**是否考虑顺序**
- 二项分布是重复独立伯努利试验的概率模型

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 4 内容整理*

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[1 学习/MIT/MIT6.041/Lecture 03 - 独立性]]
- [[1 学习/MIT/MIT6.041/Lecture 05 - 随机变量]]
- [[1 学习/MIT/MIT6.041/课程导学]]
