
## yield 核心含义

`yield` 可以理解为函数的 “暂停键 + 返回键”：

1. 当函数执行到 `yield` 时，会**暂停执行**，并将 `yield` 后的值返回给调用者；
2. 当调用者再次触发迭代（如 `next()` 或 `for` 循环），函数会从暂停的位置**继续执行**，直到遇到下一个 `yield`（或函数结束）。
3. 所有yield返回出来的值都存储在生成器对象中

## 生成器函数 vs 普通函数

| 特性   | 普通函数             | 生成器函数（含 yield）     |
| ---- | ---------------- | ------------------ |
| 返回值  | 用 `return` 一次性返回 | 用 `yield` 逐个返回（惰性） |
| 执行状态 | 调用即执行完，无状态       | 暂停 - 恢复，保留执行状态     |
| 内存占用 | 生成所有数据，占用高       | 按需生成，占用极低          |
| 调用方式 | 直接调用 `func()`    | 调用后返回生成器对象，需迭代     |

## yield 基础用法示例

### 1. 最简生成器函数

```python
# 定义生成器函数（含yield）
def num_generator():
    print("开始生成第一个数")
    yield 1  # 暂停，返回1
    print("继续生成第二个数")
    yield 2  # 暂停，返回2
    print("生成结束")

# 调用函数→得到生成器对象（不会立即执行函数体）
gen = num_generator()

# 第一次迭代：执行到第一个yield，返回1
print(next(gen))  # 输出：开始生成第一个数 → 1
# 第二次迭代：从暂停处继续，执行到第二个yield，返回2
print(next(gen))  # 输出：继续生成第二个数 → 2
# 第三次迭代：函数执行完，无yield，抛出StopIteration
# print(next(gen))  # 报错：StopIteration
```

### 2. 用 for 循环遍历（自动处理 StopIteration）

```python
def num_generator(n):
    for i in range(n):
        yield i  # 逐个生成0,1,2...

# for循环会自动迭代生成器，直到结束
for num in num_generator(3):
    print(num)  # 输出：0 → 1 → 2
```

### 3. 对比列表推导式（内存差异）

```python
# 列表推导式：一次性生成100万个数据，占用大量内存
lst = [x for x in range(1000000)]
print(type(lst))  # <class 'list'>

# 生成器表达式（元组推导式的底层）：惰性生成，几乎不占内存
gen = (x for x in range(1000000))
print(type(gen))  # <class 'generator'>

# 元组需要用tuple()消费生成器，才会生成所有数据
tup = tuple(gen)
print(type(tup))  # <class 'tuple'>
```

## 进阶用法
`yield` 的进阶能力源于：生成器对象不仅能**产出（yield）值**，还能**接收（send）值**。

### yield双向通信
yield可以作为“表达式”使用，接收外部通过send()传入的数据，实现生成器与调用者的双向交互

- gen.send(value) 会把value传给yield表达式，然后回复生成器的运行
- 第一次调用生成器只能传None或用next（），此时没有暂停的yield接收数据。

对话器：
```python
def chat_gen():
	print("生成器运行，等待接收消息")
	while True:
		#yield作为表达式，接收外部纯如的数据
		msg = yield
		if msg == "exit":
			yield "收到退出指令，结束对话"
			break
		yield f"你说{msg}，收到了"

chat = char_gen()
next(chat)
print(char.send("你好")
print(char.send("exit"))
```
无限生成器：
```python
# 无限生成斐波那契数列 
def fib_generator(): 
	a, b = 0, 1 
	while True: 
		yield a # 无限yield，永不结束 
		a, b = b, a + b 
# 取前10个斐波那契数（不会无限循环，因为只迭代10次） 
fib = fib_generator() 
for _ in range(10): 
	print(next(fib), end=" ") 
	# 输出：0 1 1 2 3 5 8 13 21 34 
# 扩展：生成自增唯一ID 
def id_generator(start=1): 
	while True: 
		yield start 
		start += 1 
		
id_gen = id_generator(100) 
print("\n", next(id_gen)) # 100 
print(next(id_gen)) # 101
```

>还有很多高级用法，但对于现在的我来说太困难了，以后再战