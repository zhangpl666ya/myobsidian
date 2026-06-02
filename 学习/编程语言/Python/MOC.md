---
tags:
  - "笔记/MOC"
---
<!-- related: managed by hermes-linkbot -->
# Python 学习地图 (Map of Content)

> 本页是这个主题的**知识地图**。所有相关笔记都汇总在这里，按主题分类，方便你从入口切入整套知识。
>
> 添加新笔记时，请到对应小节下加一行 `[[文件名|显示名]]`；不要新增散落的入口。

> Python 笔记按 **导言 / 数据结构 / 文件IO / 自定义函数 / 协议 / 工具包 / 环境** 组织。[[学习/编程语言/Python/导言|导言]] 是入口；[[学习/编程语言/Python/python协议（protocol）/什么是python的协议|协议总览]] 是核心。

---


## 🎯 学习起点

- [[学习/编程语言/Python/导言]] — Python 语法速览，与 C/C++ 对比
- [[学习/编程语言/Python/python协议（protocol）/什么是python的协议]] — 协议总览（必读）
- [[学习/编程语言/Python/模块与封装]] — import 体系

## 🔌 协议 (Protocol)

- [[学习/编程语言/Python/python协议（protocol）/迭代协议（迭代器）]] — `__iter__` / `__next__`
- [[学习/编程语言/Python/python协议（protocol）/上下文管理协议（with关键字]] — `__enter__` / `__exit__`
- [[学习/编程语言/Python/python协议（protocol）/容器、序列协议]] — `__len__` / `__getitem__`
- [[学习/编程语言/Python/python协议（protocol）/可调用协议]] — `__call__`
- [[学习/编程语言/Python/python协议（protocol）/属性访问协议]] — `__getattr__` / `__getattribute__`
- [[学习/编程语言/Python/python协议（protocol）/描述符协议]] — `__get__` / `__set__`
- [[学习/编程语言/Python/python协议（protocol）/运算符重载协议]] — `__add__` / `__eq__`
- [[学习/编程语言/Python/python协议（protocol）/生命周期协议]] — `__new__` / `__init__` / `__del__`

## 📦 数据结构

- [[学习/编程语言/Python/数据结构/基础数据结构]] — list / dict / set / tuple
- [[学习/编程语言/Python/数据结构/List 列表进阶]] — 推导式
- [[学习/编程语言/Python/数据结构/字典删去对应值]] — del / pop
- [[学习/编程语言/Python/数据结构/Generator Expressions]] — 生成器表达式

## 📄 文件管理

- [[学习/编程语言/Python/文件管理/一、基础方法]] — open/read/write
- [[学习/编程语言/Python/文件管理/二、上下文管理器]] — with 关键字
- [[学习/编程语言/Python/文件管理/三、将文件当作可迭代对象]] — for line in f
- [[学习/编程语言/Python/文件管理/文件指针]] — seek / tell
- [[学习/编程语言/Python/文件管理/编码]] — encoding 参数
- [[学习/编程语言/Python/文件管理/二进制模式]] — rb / wb
- [[学习/编程语言/Python/文件管理/用python实现类C预压的文件对象]] — 自定义文件类

## 🛠️ 自定义函数

- [[学习/编程语言/Python/自定义函数/python自定义函数初步]] — def / 形参 / 默认值
- [[学习/编程语言/Python/自定义函数/Lambda]] — 匿名函数
- [[学习/编程语言/Python/自定义函数/Yield关键字]] — 生成器

## 📚 工具包 (包/)

- [[学习/编程语言/Python/包/requests 库]] — HTTP 客户端
- [[学习/编程语言/Python/包/requests 实战]] — 实战模板
- [[学习/编程语言/Python/包/网络请求 错误处理]] — try/except 模板
- [[学习/编程语言/Python/包/BeautifulSoup]] — HTML 解析
- [[学习/编程语言/Python/包/JSON 与 API 响应]] — json.dumps / loads
- [[学习/编程语言/Python/包/PySide6/信号槽机制]] — Qt GUI 信号/槽
- [[学习/编程语言/Python/包/Regex|Regex]] — 正则
- [[学习/编程语言/Python/快速看懂json结构]] — JSON 速查

## 🧰 环境与错误处理

- [[学习/编程语言/Python/环境管理/虚拟环境enve]] — venv
- [[学习/编程语言/Python/环境管理/conda]] — conda
- [[学习/编程语言/Python/错误处理]] — try/except

## 🔗 与 C/C++ 对比

- [[学习/编程语言/Python/迭代协议（迭代器）]] ↔ [[学习/编程语言/C++/STL/Iterator/Iterator是什么]]
- [[学习/编程语言/Python/可调用协议]] ↔ [[学习/编程语言/C++/Lambda]]
- [[学习/编程语言/Python/生命周期协议]] ↔ [[学习/编程语言/C++/class/构造函数和析构函数]]
- [[学习/编程语言/Python/运算符重载协议]] ↔ [[学习/编程语言/C++/重载运算符]]
