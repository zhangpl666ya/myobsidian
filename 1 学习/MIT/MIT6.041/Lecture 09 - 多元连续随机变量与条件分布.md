# Lecture 09: 多元连续随机变量、条件分布、独立性与 Buffon 针

> **课程：** MIT 6.041 - 概率系统分析与应用概率
> **讲师：** Prof. John Tsitsiklis
> **教材：** *Introduction to Probability* 2nd ed. — Bertsekas & Tsitsiklis
> **阅读：** Sections 3.4–3.5

---

## 1. 联合 PDF 回顾

对两个连续随机变量 $(X,Y)$：

$$P((X,Y) \in S) = \iint_S f_{X,Y}(x,y) \, dx \, dy$$

**归一化：** $\iint_{-\infty}^{+\infty} f_{X,Y}(x,y) \, dx \, dy = 1$

**概率近似：** $P(x \leq X \leq x+\delta_x, \; y \leq Y \leq y+\delta_y) \approx f_{X,Y}(x,y) \cdot \delta_x \cdot \delta_y$

---

## 2. 边缘 PDF

从联合分布求出单个变量的分布：

$$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) \, dy$$

$$f_Y(y) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y) \, dx$$

几何理解：对联合密度曲面"压扁"（在 $y$ 方向积分），得到 $x$ 的边缘密度。

---

## 3. 条件 PDF

类比离散情况：

$$\boxed{f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}}, \quad f_Y(y) > 0$$

本质：固定 $Y=y$ 时，$X$ 的条件分布是联合 PDF 在 $y$ 处的"截面"经归一化后的结果。

**条件期望：** $E[X \mid Y=y] = \int_{-\infty}^{+\infty} x \, f_{X \mid Y}(x \mid y) \, dx$

---

## 4. 独立连续随机变量

$X$ 与 $Y$ **独立**当且仅当：

$$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y), \quad \forall x,y$$

等价的条件：$f_{X \mid Y}(x \mid y) = f_X(x)$（条件分布等于边缘分布）

---

## 5. Buffon 针问题（经典几何概率）

### 问题描述

地面上画等距平行线，间距为 $d$。随机投掷一根长度为 $\ell$（$\ell < d$）的针，求针与某条线相交的概率。

### 建立模型

设：
- $X$ = 针的中点到最近直线的距离，$X \sim \text{Uniform}(0, d/2)$
- $\Theta$ = 针与直线的夹角，$\Theta \sim \text{Uniform}(0, \pi/2)$
- $X$ 与 $\Theta$ 独立

联合 PDF：

$$f_{X,\Theta}(x,\theta) = f_X(x) \cdot f_\Theta(\theta) = \frac{2}{d} \cdot \frac{2}{\pi} = \frac{4}{\pi d}, \quad 0 \leq x \leq \frac{d}{2}, \; 0 \leq \theta \leq \frac{\pi}{2}$$

### 相交条件

针与线相交当且仅当：

$$X \leq \frac{\ell}{2} \sin\Theta$$

### 计算概率

$$P(\text{相交}) = \iint_{\text{相交区域}} f_{X,\Theta}(x,\theta) \, dx \, d\theta = \int_0^{\pi/2} \int_0^{(\ell/2)\sin\theta} \frac{4}{\pi d} \, dx \, d\theta$$

$$= \frac{4}{\pi d} \int_0^{\pi/2} \frac{\ell}{2} \sin\theta \, d\theta = \frac{2\ell}{\pi d} \int_0^{\pi/2} \sin\theta \, d\theta = \frac{2\ell}{\pi d}$$

> **结论：** $P(\text{相交}) = \dfrac{2\ell}{\pi d}$

这是历史上第一个**几何概率**问题（1777 年 Buffon 提出），也是用积分几何解决实际问题的经典范例。

---

## 6. 棍子折断问题（Stick-Breaking，条件分布实例）

### 问题描述

将长度为 1 的棍子在 $X$ 处折断，$X \sim \text{Uniform}(0,1)$。然后将较长的那段在 $Y$ 处再折断，$Y \sim \text{Uniform}(0,X)$。求 $Y$ 的（无条件）分布。

### 分析

联合 PDF：

$$f_X(x) = 1, \quad 0 \leq x \leq 1$$

$$f_{Y \mid X}(y \mid x) = \frac{1}{x}, \quad 0 \leq y \leq x$$

$$f_{X,Y}(x,y) = f_X(x) \cdot f_{Y \mid X}(y \mid x) = \frac{1}{x}, \quad 0 \leq y \leq x \leq 1$$

### 求边缘密度 $f_Y(y)$

$$f_Y(y) = \int_y^1 \frac{1}{x} \, dx = \ln\!\frac{1}{y} = -\ln y, \quad 0 < y \leq 1$$

**注意：** $f_Y(y)$ 在 $y \to 0$ 时趋于 $\infty$（密度可以大于 1，只要积分归一）。

### 求条件期望 $E[Y \mid X = x]$

$$E[Y \mid X = x] = \int_0^x y \cdot \frac{1}{x} \, dy = \frac{x}{2}$$

### 求无条件期望 $E[Y]$

两种方法：

**方法 1（直接积分）：**

$$E[Y] = \int_0^1 y \cdot (-\ln y) \, dy = \left[ -\frac{y^2}{2}\ln y \right]_0^1 + \int_0^1 \frac{y^2}{2} \cdot \frac{1}{y} \, dy = 0 + \frac{1}{2} \int_0^1 y \, dy = \frac{1}{4}$$

**方法 2（迭代期望定律）：**

$$E[Y] = E[E[Y \mid X]] = E\left[\frac{X}{2}\right] = \frac{1}{2} \cdot E[X] = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

两种方法结果一致 $\checkmark$

---

## 7. 多变量函数的条件化

对多个连续随机变量，条件化的思想完全一样：

$$f_{X,Y \mid Z}(x,y \mid z) = \frac{f_{X,Y,Z}(x,y,z)}{f_Z(z)}$$

边缘和条件的关系可以推广到任意维度。

---

## 本讲要点

| 概念 | 公式 |
|------|------|
| 联合 PDF | $P((X,Y) \in S) = \iint_S f_{X,Y}(x,y)dxdy$ |
| 边缘 PDF | $f_X(x) = \int f_{X,Y}(x,y)dy$ |
| 条件 PDF | $f_{X \mid Y}(x \mid y) = f_{X,Y}(x,y)/f_Y(y)$ |
| 独立性 | $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ |
| Buffon 针 | $P(\text{相交}) = 2\ell / (\pi d)$ |
| 棍子折断 $f_Y(y)$ | $-\ln y,\; 0 < y \leq 1$ |
| 迭代期望 | $E[Y] = E[E[Y \mid X]]$ |

---

*本笔记基于 MIT 6.041 Fall 2010 Lecture 9 内容整理*