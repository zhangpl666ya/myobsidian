# `with`的根本作用
你可以把`with`看作一个“**结构化资源管理器**”。
他的目标是：
- 确保你在使用资源（文件、网络链接、数据库链接等）时，他的使用会被自动管理
- 并且它的释放是有保障的

## 背后做了什么
```python
with open("test.txt","w") as f:
	f.write("hello")
```

等价于：

```python
f = open("test.txt","w")
try:
	f.write("hello")
finally:
	f.close()
```
## **重要：`with` 自动管理“打开”和“关闭”操作**

- `__enter__()` 会在 `with` 语句块执行之前调用，它返回的对象（这里是 `f`）会绑定到 `as` 后面的变量（`f`）。
    
- `__exit__()` 会在 `with` 语句块执行完成后调用，不管语句块内是否有异常，都会执行 `__exit__()` 来释放资源。


# `__enter__()` 和 `__exit__()` 详解

`with` 的核心是通过实现了 **上下文管理器**（context manager）的对象来进行资源管理。  
上下文管理器对象就是拥有 `__enter__()` 和 `__exit__()` 方法的类。

### `__enter__()` 方法

`__enter__()` 方法会在 `with` 语句块开始之前执行。  
**它的主要作用是：初始化资源、准备工作，并返回资源对象**，这个对象就可以在 `as` 后使用。
```python
class MyContext:
	def __enter__(self):
		print("Entering the context")
		return "hello"
	def __exit__(self, exc_type, exc_val, exc_tb):
		print("Exiting the context)
		
with MyContext() as x:
	print(x)
```
输出：
```text
Entering the context
hello
Exiting the context
```
>__enter__返回的对象赋值给x

### `__exit__()` 方法

`__exit__()` 方法会在 `with` 语句块执行完后自动调用。  
它有四个参数：``def __exit__(self, exc_type, exc_val, exc_tb):
1. `self`：类的实例
2. `exc_type`：是异常类型，若with语块内没有抛出异常，它的值是None。若有异常，那么值是异常类
3. `exc_val`：是异常的具体值，若有异常，他会是异常的对象，没有异常为None
4. `exc_tb` ：是异常的 **traceback**，也就是异常堆栈信息。它是一个对象，包含异常的追踪信息，如果没有异常，它的值是 `None`

- 如果 `__exit__()` 返回 `True`，表示**吞掉异常**，即异常不会被抛出到外面。
    
- 如果返回 `False`（或者没有 `return`），表示**不吞掉异常**，异常会继续抛出。
