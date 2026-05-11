# 1️⃣算法基本常识

## 什么是算法？
算法是给一个输入，能返回单个我们想要的输出的一个程序，对于同一个问题，不同的输入总是能给出一个但是是正确的输出

## 算法正确性证明
基本思路便是***数学归纳法***

> For small inputs, can use case analysis
> For arbitrarily large inputs, algorithm must be recursive or loop in some way
> Must use induction(why recursion is such a key concept in computer science)

翻译一下就是：
- 对于小型输入，可以使用案例分析
- 对于相当大型输入，算法必须以某种方式递归或循环
- 必须使用归纳法（这就是为什么递归在计算机科学中是如此关键的概念）

## 效率（复杂度）
对于小型输入，的确没有研究复杂度的必要，但是对于任意大型输入，讨论效率就很有用了
（注意：在这门课中默认输入是任意大的）

Asymptotic Notations渐进符号：
- Upper bounds（O）， lower bounds（Θ），tight bounds（Ω）
- O ：用于考虑该算法最坏情况下的时间用度
- Θ ：用于该算法在输入最好情况下的复杂度
- Ω ：用于精确计算，当Upper bounds和lower bounds相同（即夹住了），就可以用这个符号

只要是多项式复杂度，都是可取的

# 2️⃣计算模型
由于CPU字长已经达到了64位，所以没有太多需要考虑的了

基本的加减乘除、取模、逻辑运算、位运算、取地址都可以在O(1)时间内完成

# 3️⃣数据结构
本讲介绍了python中的Static array：
- `StaticArray(n)`: 分配一个全是零的大小为n的静态数组，时间复杂度Θ（n）
- `StaticArray.get_at(i)`：返回在索引i处的内容，时间复杂度Θ（1）
- `StaticArray.set_at(i,x)`：将x写入索引i处，时间复杂度Θ（1）

后续会有更多数据结构用来更高效的解决问题


