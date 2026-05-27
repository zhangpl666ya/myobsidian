生成元包括*generator expression*s 和 *generator functions*
（翻译一下，生成器表达式和生成函数？）
关于generator function：[[Yield关键字]]
# *Generator Expressions*
list comprehensions 和generator expressions 的区别有时候时很难把握的，试着列出一些区别
## 1️⃣List comprehensions 方括号，generator expressions 圆括号
这是一个由代表性的list：
```python
[n ** 2 for n in range(12)]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
```

这是一个有代表性的generator expression：
```python
(n ** 2 for n in range(12))
#<generator object <genexpr> at 0x104a60518>
```
如果你去print这个generator expression，你会发现不会打印出内容。
想打印内容，要给print传入他的constructor（构造函数），也就是list
```python
G = (n ** 2 for n in range(12))
list(G)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
```

## 2️⃣list是一群值的集合，而generator是生成值的方法
当你创造一个list，你实际上建造了一堆值，这也就产生了一些内存消耗。当你创造一个generator时，你没有创造一堆值，但创造了产生这些值的方法。这两者都暴露了同样的迭代器接口：
```python
#list:
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')
#generator: 
G = (n ** 2 for n in range(12))
for val in G:
    print(val, end=' ')

```
区别是：generator在这些值需要之前没有真的计算出这些值。这不不仅仅是内存高效，也是计算高效。

## 列表内容可以多次迭代，生成元表达式是一次性使用的
list可以做到：
```python
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')
print()

for val in L:
    print(val, end=' ')
#0 1 4 9 16 25 36 49 64 81 100 121 
#0 1 4 9 16 25 36 49 64 81 100 121
```
但生成元表达式在迭代一次后会被用掉：
```python
G = (n ** 2 for n in range(12))
list(G)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
list(G)
#[]
```

这非常有用，因为这意味着可以停止和开始迭代：
```python
G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30: break

print("\ndoing something in between")

for n in G:
    print(n, end=' ')
```
