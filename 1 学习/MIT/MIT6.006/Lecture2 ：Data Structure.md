# 1️⃣数据结构接口
- 数据结构是一种存储数据的方式，python中内置了许多支持对这些数据操作的算法
- 这些支持的操作的集合即接口（也叫API和ADT）
- 接口是一种规格说明，告诉我们哪些操作支持，但不考虑具体实现
- 而数据结构是一种表现形式，告诉我们哪些操作可以实现

有两个种抽象数据结构（ADT），分别是：
## Sequence Interface
- 维护一个序列，其顺序是显式的
- 支持的操作：
	- Container:
		- `build(X)`: 给一个可迭代的X，用X中的项创建一个序列
		- `len()`：返回序列元素个数
	- Static：
		- `iter_seq`：按顺序返回序列中的内容
		- `get_at(i)`：返回索引i的项
		- `set_at(i)`：将索引i的项替换成x
	- Dynamic：
		- `insert_at(i,x)`：将x插入到索引i处
		- `delete_at(i)`：将索引i处删除
		- `insert_first(x)`：将x加到开头
		- `delete_first()`：将开头元素删去
		- `insert_last(x)`：将x加入到末尾
		- `delete_last()`：将末尾删去

## Set Interface
- Sequence是显示顺序，set是隐式顺序
- 维护集合，每个元素有一个独一无二的键值
- 支持的操作：
	- Container:
		- `build(x)`：同上
		- `len()`：同上
	- Static:
		- `find(k)`：返回键值为k的项
	- Dynamic:
		- `insert(x)`：将x添加到集合（如果已经存在就替换掉）
		- `delete(k)`：移除并返回键值为k的项
	- Order:
		- `iter_ord`：一个一个返回项
		- `find_min`：返回键值最小的项
		- `find_max`：返回键值最大的项
		- `find_next`：返回比k大但最小的项
		- `find_prev`：返回比k小但最大的项

前者记录位置顺序，由索引查找项；后者不保证逻辑顺序，由键值查找项
# 2️⃣数据结构方法复杂度分析比较
## Array Sequence
- 静态数组对于静态操作太完美了，`get_at set_at`都是常数时间
- 但动态操作非常致命

## Linked List Sequence
- 指针数据结构
- 每一个项都存储在一个节点中，这个节点也保存有下一个节点的位置
- 可以简单通过改变指向进行操作
- 可以在开头常数时间内完成增加和删除项
- 但是`get_at(i) set_at(i,x)`却占用O（i）时间:(
- 双链表有更好的性质，你自主探索

## Dynamic Array Sequence
- python中list就是一种动态数据结构
- 解决方案就是预留一部分内存，当要满的时候就扩容一次，删到留下很多空间时缩容一次
- 虽然有额外消耗，但是均摊（amortized）到每一次操作上依然为常数时间
- python list `append`and `pop`在均摊下O（1）



| Data Structure |            |                      |                                      |       Operation,Worst Case(·)       |                                   |
| :------------: | :--------: | :------------------: | :----------------------------------: | :---------------------------------: | :-------------------------------: |
|                | Container  |        static        |                                      |               Dynamic               |                                   |
|                | `build(x)` | `get_at`<br>`set_at` | `inset_first(x)`<br>`delete_first()` | `insert_last(x)`<br>`delete_last()` | `insert_at(i,k)`<br>`delet_at(i)` |
|     Array      |     n      |          1           |                  n                   |                  n                  |                 n                 |
|  Linked List   |     n      |          n           |                  1                   |                  n                  |                 n                 |
| Dynamic Array  |     n      |          1           |                  n                   |                1(a)                 |                 n                 |



