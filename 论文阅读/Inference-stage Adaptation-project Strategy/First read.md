Abstract
↓
Introduction
↓
Figure 1
↓
Conclusion

目标：
知道故事

# 1. Abstract（摘要）怎么读

## 阅读目标：

不要试图理解细节，只回答：

> 这篇论文想解决什么大问题？

填空：

```
这篇论文研究的问题是：

答：如何提升diffusion policy的泛化能力

过去的方法主要存在的问题是：

答：为了让diffusion policy适应新场景需要昂贵的数据采集和训练代价

作者提出的方法叫：

答：adaptation-projection strategy

核心思想是一句话：

答：让diffusion policy拥有上手新场景的能力

作者声称取得的效果：

答：在各个硬件下取得高成功率

```
# 2. Introduction（引言）

这是论文最重要部分。

不要急着看公式。

读 Introduction 时，画一条逻辑链：

```
现实问题
    ↓
已有方法
    ↓
已有方法为什么失败
    ↓
作者提出新方向
```

填写：

- 现实问题：Deep imitation learning在新硬件情况下表现极差
- 已有方法：Multi-embodiment learning strategies
- 为什么不好：需要大量数据，不适合应用落地
- 新方向：Adaptation-projection strategy

## 2.1 Problem（问题）

```
作者观察到的现实问题：

答：深度模仿学习无法适应新的机械手配置，且目前的解决方案代价巨大

为什么这个问题重要：

答：不解决限制现实场景的灵活性

如果解决，可以带来什么：

答：可以让模型不再因为新机器手配置问题无法解决问题

```

---

## 2.2 Previous Work（过去方法）

```
以前主要有哪几类方法：

方法A：Multi-embodiment learning strategies
核心思想：训练多个操作器的统一规则

缺点：训练代价巨大


方法B：
核心思想：

缺点：
```

---

## 2.3 Gap（研究空白）

这是论文灵魂。

填写：

```
以前方法不能解决的问题：上述方法会产生耗时的适应成本并限制了现实场景中的部署灵活性

原因是什么：训练代价大

作者认为突破点在哪里：
```

---

## 2.4 Contribution（贡献）

通常 Introduction 最后会列：

"We make three contributions"

不要直接复制。

翻译成自己的话：

```
贡献1：面对不同配置无需重新训练扩散策略

贡献2：设置了安全约束

贡献3：在不同任务中都非常有效
```

判断：

```
真正创新的是：引入新策略，且为不同配置都设置了安全约束
```

---

# 3.Conclusion
```
Conclusion

作者总结的问题
:

核心方法（一句话）
:

最大贡献
:

实验最终证明
:

没有证明
:

作者承认的限制
:

我的评价
:

后续研究想法
:
```
