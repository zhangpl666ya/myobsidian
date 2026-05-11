# 匿名函数lambda
python中还有另一种定义短暂、一次性函数的方法，C++中也有的lambda。 它看起来大致是这样的：
```python
add = lambda x, y: x + y
add(1, 2)
```
该λ函数大致等价于
```python
def add(x, y):
    return x + y
```

## 基本语法
```python
lambda 参数列表: 表达式
```
- **参数列表**：和普通函数一样，可以是 0 个、1 个或多个参数（支持默认参数、可变参数等）。
- **表达式**：函数的返回值（只能是单个表达式，不能包含复杂逻辑如循环、条件分支（简单三元表达式除外））。
- 本质：lambda 表达式返回一个函数对象，可赋值给变量，也可直接调用。
## 核心特点

1. **匿名性**：默认没有函数名，需赋值给变量或直接使用。
2. **简洁性**：仅适用于单行表达式逻辑，无法写多行代码。
3. **返回值**：表达式的结果就是函数的返回值，无需写 `return`。


## 用lambda实现sorted自定义排序规则
举个例子，假设我们有一组词典中存储了一些数据：
```python
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]
```
现在假设我们想对这些数据进行排序。Python 有一个函数可以做到：`sorted`
```python
sorted([2,4,3,5,1,6])#结果【1，2，3，4，5，6】
```
但词典时不可以排序到底，需要一种特殊方法告诉函数如何排序我们的数据，我们可以通过指定函数实现这一点，函数是给定的一个项目时返回该项目排序键的函数：`key`
```python
# 按字母表排第一个名字
sorted(data, key=lambda item: item['first'])
#输出：
#[{'YOB': 1912, 'first': 'Alan', 'last': 'Turing'},
#{'YOB': 1906, 'first': 'Grace', 'last': 'Hopper'},
#{'YOB': 1956, 'first': 'Guido', 'last': 'Van Rossum'}]

## 按出生年月排序
sorted(data, key=lambda item: item['YOB'])
#输出：
#[{'YOB': 1906, 'first': 'Grace', 'last': 'Hopper'},
#{'YOB': 1912, 'first': 'Alan', 'last': 'Turing'},
#{'YOB': 1956, 'first': 'Guido', 'last': 'Van Rossum'}]
```

### 核心规则：
```python
sorted(可迭代对象, key=排序规则函数, reverse=是否降序)
```
- key：**关键**，接收一个【函数】，这个函数用于告诉sorted按“每个元素的什么特征”来排序
- reverse：bool值，默认False（升序），设置为True则降序
#### 场景1：普通元素，按“元素的衍生值排序
```python

words = ["apple", "banana", "cat", "dog"]
# key=lambda x: len(x) → 按每个字符串的长度排序；reverse=True → 降序
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)  # 输出：['banana', 'apple', 'cat', 'dog']
```
#### 场景 2：对 “容器元素”（元组 / 列表）按指定位置排序
前面举的例子就属于这种
#### 进阶场景：多条件排序（优先级排序）
如果想按 “第一个条件排序，第一个条件相同则按第二个条件”，只需让 lambda 返回**多个值的元组**，元组内的顺序就是优先级。

```python
# 示例：列表元素是 (姓名, 班级, 成绩)，先按「班级」升序，再按「成绩」降序
students = [
    ("小明", 2, 90),
    ("小红", 1, 95),
    ("小刚", 2, 85),
    ("小丽", 1, 90)
]
# key=lambda x: (x[1], -x[2]) → 优先级1：班级（x[1]）升序；优先级2：成绩（-x[2]）降序
# （也可以写成 key=lambda x: (x[1], x[2]), reverse=(False, True)，但不如负号直观）
sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))
print(sorted_students)
# 输出：[('小红', 1, 95), ('小丽', 1, 90), ('小明', 2, 90), ('小刚', 2, 85)]
```

#### 对字典排序：
字典本身不能直接排序，但可以取 `items()`（返回 (键，值) 元组的可迭代对象），再按键或值排序。
```python
# 示例1：按字典的「值」升序排序
student_score = {"小明": 88, "小红": 95, "小刚": 90}
# key=lambda x: x[1] → x 是 (键, 值) 元组，x[1] 取“值”作为排序依据
sorted_by_value = sorted(student_score.items(), key=lambda x: x[1])
print(sorted_by_value)  # 输出：[('小明', 88), ('小刚', 90), ('小红', 95)]

# 示例2：按字典的「键」降序排序（键是字符串，按字母/汉字排序）
sorted_by_key = sorted(student_score.items(), key=lambda x: x[0], reverse=True)
print(sorted_by_key)  # 输出：[('小刚', 90), ('小明', 88), ('小红', 95)]
```

>[!notice]
>1. lambda中x代表”可迭代对象的每个元素
>2. 降序的两种实现：
>	1. reverse=True（py中T必须大写）
>	2. 对数值型排序依据取负
>3. 不要搞太复杂的逻辑！


