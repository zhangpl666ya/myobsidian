---
tags:
  - "笔记/MOC"
---
<!-- related: managed by hermes-linkbot -->
# C++ 学习地图 (Map of Content)

> 本页是这个主题的**知识地图**。所有相关笔记都汇总在这里，按主题分类，方便你从入口切入整套知识。
>
> 添加新笔记时，请到对应小节下加一行 `[[文件名|显示名]]`；不要新增散落的入口。

> C++ 笔记按 **基础语法 / 面向对象 / STL / 编译原理 / 工具链** 五大块组织。先看 [[学习/编程语言/C++/STL/什么是STL|STL 总览]]，再看 [[学习/编程语言/C++/STL/Template|模板]]，然后按需进入各容器/迭代器。

---


## 🎯 学习起点

- [[学习/编程语言/C++/STL/什么是STL]] — 标准库总览，建议先读
- [[学习/编程语言/C++/STL/Template]] — 模板是 STL 的基石
- [[学习/编程语言/C++/编译/目录]] — 编译链全景图

## 🧱 基础语法

- [[学习/编程语言/C++/引用]] — 引用 vs 指针
- [[学习/编程语言/C++/智能指针]] — RAII 与内存管理
- [[学习/编程语言/C++/类型转换]] — 4 种 cast
- [[学习/编程语言/C++/Using关键字]] — 命名空间 / 类型别名
- [[学习/编程语言/C++/Lambda]] — 匿名闭包
- [[学习/编程语言/C++/重载运算符]] — operator overload
- [[学习/编程语言/C++/Stream]] — iostream 输入输出
- [[学习/编程语言/C++/范围for循环]] — C++11 语法糖

## 🎭 面向对象 (class/*)

- [[学习/编程语言/C++/class/继承]] — public/protected/private 继承
- [[学习/编程语言/C++/class/虚函数 纯虚函数 多态]] — 运行时多态核心
- [[学习/编程语言/C++/class/构造函数和析构函数]] — 构造/析构/初始化列表
- [[学习/编程语言/C++/class/This指针]] — 隐式 this
- [[学习/编程语言/C++/class/Const]] — const 成员函数
- [[学习/编程语言/C++/class/静态]] — static 成员
- [[学习/编程语言/C++/class/类型级和对象级]] — 类层级 vs 对象层级

## 📚 STL — 容器

- [[学习/编程语言/C++/STL/Container/Vector]] — 动态数组
- [[学习/编程语言/C++/STL/Container/List]] — 双向链表
- [[学习/编程语言/C++/STL/Container/Deque]] — 双端队列
- [[学习/编程语言/C++/STL/Container/Map]] — 有序键值对（红黑树）
- [[学习/编程语言/C++/STL/Container/Set]] — 有序集合
- [[学习/编程语言/C++/STL/Container/String]] — std::string
- [[学习/编程语言/C++/STL/Container/Quene]] — queue

### 单变量存多类型

- [[学习/编程语言/C++/STL/Container/单变量存储多类型数据/Optional]] — 可选值
- [[学习/编程语言/C++/STL/Container/单变量存储多类型数据/Variant]] — 类型安全 union
- [[学习/编程语言/C++/STL/Container/单变量存储多类型数据/Any]] — 万能类型
- [[学习/编程语言/C++/STL/Container/单变量存储多类型数据/函数多返回值问题]] — std::tuple 解构

## 🔁 STL — 迭代器

- [[学习/编程语言/C++/STL/Iterator/Iterator是什么]] — 先看这篇
- [[学习/编程语言/C++/STL/Iterator/Iterator分类]] — 输入/前向/双向/随机访问
- [[学习/编程语言/C++/STL/Iterator/Iterator Operations]] — 基础操作
- [[学习/编程语言/C++/STL/Iterator/迭代器统一接口函数]] — std::advance 等
- [[学习/编程语言/C++/STL/Iterator/统一接口原理总结]] — tag dispatch

## ⚙️ 编译与构建

- [[学习/编程语言/C++/编译/目录]] — 编译链总览
- [[学习/编程语言/C++/编译/预处理]] — #include / #define / 条件编译
- [[学习/编程语言/C++/编译/编译与汇编]] — 编译过程
- [[学习/编程语言/C++/编译/链接]] — 符号解析 / 重定位
- [[学习/编程语言/C++/编译/静态与动态链接]] — .lib / .dll

## 🔗 与其他语言对比

- [[学习/编程语言/C/指针 函数 常量 易混淆名词]] — C 的指针/函数/常量
- [[学习/编程语言/Python/python协议（protocol）/可调用协议]] — Python 的 __call__
- [[学习/编程语言/Python/python协议（protocol）/生命周期协议]] — Python 的 __init__ / __del__
