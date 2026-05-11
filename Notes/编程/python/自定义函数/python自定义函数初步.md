
# 自定义函数语法
>C/C++函数基本语法：`返回值类型 函数签名（参数）{内容}`

## 格式
由于python是弱类型编程语言，函数无返回值类型
基本语法：`def 函数名（参数）:内容`
没有大括号形成的代码块，py用缩进代表代码块

## 多返回值
在python中自定义函数可以有多返回值，用逗号隔开
然而其本质是返回了一个tuple元组，所以还是只有一个返回值
在接收返回值的时候用变量按顺序一次接收
```python
def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

r, i, c = real_imag_conj(3 + 4j)
print(r, i, c)
```
## 默认参数值
对于函数的参数，可以在定义的时候给它先赋值，这样如果不指定，会默认使用这些值。同时也意味着调用函数的时候可以少传入一些项。
**指定参数传入**：
	对于添加了默认值的函数参数，可以在调用的时候明确点出该形参，可以忽略传参顺序
```python
def fibonacci(N, a=0, b=1):#这里给出默认值，后续可以不传入
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
    
fibonacci(10)

fibonacci(10, a=1, b=2)
fibonacci(10,1,2)#这和上面这个相等

fibonacci(10,b=1,a=2)#这和上面的结果不同，真实传入形参的值
```

---

# 不确定参数的函数
有时你可能想写一个函数，在函数中你最初不知道用户会传递多少个参数。在这种情况下，你可以使用特殊形式和来捕捉所有传递的参数。
### * args : 位置参数
在定义函数的时候，若不确定函数需要的参数数量，就用* args占位，调用函数的时候就可以随便传了，会被**打包**成元组

在C/C++中你需要至少一个固定参数，才能使用...，在python中不是这样
```python
def add (*arg):
    sum = 0
    for i in [arg]:
        sum += i
    print(sum)
    return sum    

a = sum(1,2,3,4,5)
```

**解包：把容器中的元素拆成位置参数**：
函数调用时加*，可以把列表/元组/迭代器的元素拆成单个位置参数
```python

def add(x, y):
    return x + y

nums = (3, 5)
print(add(*nums))  # 等价于add(3,5)，输出8
```

### ** kwargs : 关键字参数打包/解包

**打包：把多个关键字参数收进字典dict**
函数定义时用`**kwargs`，会把**除了固定参数外的所有关键字参数**打包成字典（key 是参数名字符串，value 是参数值）：
```python
def func(a, **kwargs):
    print("固定参数a:", a)
    print("kwargs的类型:", type(kwargs))  # <class 'dict'>
    print("kwargs的内容:", kwargs)

func(1, b=2, c=3)
# 输出：
# 固定参数a: 1
# kwargs的类型: <class 'dict'>
# kwargs的内容: {'b': 2, 'c': 3}
```
**解包：把字典拆成关键字参数**

函数调用时用`**`，会把字典的 key-value 拆成`key=value`形式的关键字参数：
```python
def person(name, age):
    print(f"姓名：{name}，年龄：{age}")

info = {"name": "张三", "age": 20}
person(**info)  # 等价于person(name="张三", age=20)
```

>[!warning]
>**顺序问题**：函数定义时，参数顺序必须是：`固定参数 > *args > 关键字参数 > **kwargs`

---

