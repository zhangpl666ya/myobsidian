---
tags:
  - "笔记/MOC"
---
<!-- related: managed by hermes-linkbot -->
# C 语言学习地图 (Map of Content)

> 本页是这个主题的**知识地图**。所有相关笔记都汇总在这里，按主题分类，方便你从入口切入整套知识。
>
> 添加新笔记时，请到对应小节下加一行 `[[文件名|显示名]]`；不要新增散落的入口。

> C 笔记按 **概念辨析 / 头文件速查 / 进阶** 三块组织。[[指针 函数 常量 易混淆名词|指针/函数/常量]] 是最容易踩坑的入口；[[函数指针的意义|函数指针]] 是 C 模拟 OOP 的钥匙。

---


## 🎯 学习起点

- [[指针 函数 常量 易混淆名词]] — 必读，避坑指南
- [[函数指针的意义]] — 行为抽象的核心
- [[C语言中的面向对象编程]] — C 模拟 OOP

## 📂 标准头文件 (header/)

- [[header/stdio.h]] — 文件 IO / stdin/out/err
- [[header/stdlib.h]] — 内存管理 / 类型转换
- [[header/string.h]] — 字符串操作
- [[header/errno.h]] — 错误码
- [[header/stdarg.h]] — 可变参数 (printf)
- [[header/time.h]] — 时间

## 🔗 跨语言对照

- [[指针 函数 常量 易混淆名词]] ↔ [[C++/引用]]
- [[函数指针的意义]] ↔ [[C++/Lambda]]
- [[header/stdio.h]] ↔ [[C++/Stream]]
- [[header/stdlib.h|malloc]] ↔ [[C++/智能指针]]
- [[header/string.h]] ↔ [[C++/STL/Container/String]]
- [[header/errno.h]] ↔ [[Python/错误处理]]
