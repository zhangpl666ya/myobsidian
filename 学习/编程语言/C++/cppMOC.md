---
tags:
  - "笔记/MOC"
---
<!-- related: managed by hermes-linkbot -->
# C++ 学习地图 (Map of Content)

> 本页是这个主题的**知识地图**。所有相关笔记都汇总在这里，按主题分类，方便你从入口切入整套知识。
>
> 添加新笔记时，请到对应小节下加一行 `[[文件名|显示名]]`；不要新增散落的入口。

> C++ 笔记按 **基础语法 / 面向对象 / STL / 编译原理 / 工具链** 五大块组织。先看 [[STL/什么是STL|STL 总览]]，再看 [[STL/Template|模板]]，然后按需进入各容器/迭代器。

---


## 🎯 学习起点

- [[STL/什么是STL]] — 标准库总览，建议先读
- [[STL/Template]] — 模板是 STL 的基石
- [[编译/目录]] — 编译链全景图

## 🧱 基础语法

- [[引用]] — 引用 vs 指针
- [[智能指针]] — RAII 与内存管理
- [[类型转换]] — 4 种 cast
- [[Using关键字]] — 命名空间 / 类型别名
- [[Lambda]] — 匿名闭包
- [[重载运算符]] — operator overload
- [[Stream]] — iostream 输入输出
- [[范围for循环]] — C++11 语法糖

## 🎭 面向对象 (class/*)

- [[class/继承]] — public/protected/private 继承
- [[class/虚函数 纯虚函数 多态]] — 运行时多态核心
- [[class/构造函数和析构函数]] — 构造/析构/初始化列表
- [[class/This指针]] — 隐式 this
- [[class/Const]] — const 成员函数
- [[class/静态]] — static 成员
- [[class/类型级和对象级]] — 类层级 vs 对象层级

## 📚 STL — 容器

- [[STL/Container/Vector]] — 动态数组
- [[STL/Container/List]] — 双向链表
- [[STL/Container/Deque]] — 双端队列
- [[STL/Container/Map]] — 有序键值对（红黑树）
- [[STL/Container/Set]] — 有序集合
- [[STL/Container/String]] — std::string
- [[STL/Container/Quene]] — queue

### 单变量存多类型

- [[STL/Container/单变量存储多类型数据/Optional]] — 可选值
- [[STL/Container/单变量存储多类型数据/Variant]] — 类型安全 union
- [[STL/Container/单变量存储多类型数据/Any]] — 万能类型
- [[STL/Container/单变量存储多类型数据/函数多返回值问题]] — std::tuple 解构

## 🔁 STL — 迭代器

- [[STL/Iterator/Iterator是什么]] — 先看这篇
- [[STL/Iterator/Iterator分类]] — 输入/前向/双向/随机访问
- [[STL/Iterator/Iterator Operations]] — 基础操作
- [[STL/Iterator/迭代器统一接口函数]] — std::advance 等
- [[STL/Iterator/统一接口原理总结]] — tag dispatch

## ⚙️ 编译与构建

- [[编译/目录]] — 编译链总览
- [[编译/预处理]] — #include / #define / 条件编译
- [[编译/编译与汇编]] — 编译过程
- [[编译/链接]] — 符号解析 / 重定位
- [[编译/静态与动态链接]] — .lib / .dll

## 🔗 与其他语言对比

- [[C/指针 函数 常量 易混淆名词]] — C 的指针/函数/常量
- [[Python/python协议（protocol）/可调用协议]] — Python 的 __call__
- [[Python/python协议（protocol）/生命周期协议]] — Python 的 __init__ / __del__
