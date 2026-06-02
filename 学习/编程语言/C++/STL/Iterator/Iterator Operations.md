---
tags:
  - "学习/编程/C++"
  - "概念/迭代器"
  - "概念/操作"
  - "笔记/速查"
---
先看：[[Iterator分类]]
下面我**不再从容器讲起**，而是**从“迭代器能做什么操作”出发**，系统讲清楚这些 _operations_，以及**哪些迭代器类型支持哪些操作**，这是标准库真正关心的东西。

---

## 一、Iterator Operations 的总体框架（非常重要）

C++ 标准并不是按“容器”定义迭代器，而是按**“能力逐级叠加”**来定义迭代器操作：

```
Input
  ↓
Forward
  ↓
Bidirectional
  ↓
Random Access
  ↓
Contiguous (C++20)
```

👉 **每往下一层，支持的 operations 只多不少**

---

## 二、最基础的一组：所有迭代器都必须支持的操作

### 1️⃣ 解引用（Dereference）

```cpp
*it
it->member
```

**含义**

- `*it`：访问当前元素
    
- `it->x`：访问元素成员（等价于 `(*it).x`）
    

**注意**

- Input Iterator：`*it` 只能读，且**可能是一次性的**
    
- Output Iterator：`*it = value`
    
- 非 const iterator：`*it` 可修改
    
- const_iterator：`*it` 只读
    

---

### 2️⃣ 递增（Increment）

```cpp
++it    // 前置
it++    // 后置
```

**含义**

- 指向“下一个”元素
    
- 后置递增可能返回旧值，**效率通常更低**
    

✅ **所有迭代器类型都支持 `++it`**

---

### 3️⃣ 相等 / 不等比较

```cpp
it1 == it2
it1 != it2
```

**含义**

- 判断是否指向同一位置
    
- 通常用于循环结束条件
    

---

## 三、Input / Output Iterator 专属操作差异

### 🔹 Input Iterator（读）

```cpp
auto x = *it;  // OK
++it;          // OK
```

🚫 不保证：

- 多次解引用结果一致
    
- 拷贝后还能独立使用
    

📌 典型例子：

```cpp
istream_iterator<int>
```

---

### 🔹 Output Iterator（写）

```cpp
*it = value;
++it;
```

🚫 不支持：

- `auto x = *it`
    
- 比较两个 output iterator 的值语义
    

📌 典型例子：

```cpp
back_inserter(vec)
ostream_iterator<int>
```

---

## 四、Forward Iterator：**“能反复遍历”是关键**

### 新增语义（不是新语法）

```cpp
*it      // 多次解引用结果一致
++it     // 多次遍历 OK
```

📌 **这是第一个“多遍可用”的迭代器**

✅ 支持：

- 拷贝
    
- 多次遍历同一区间
    

📌 容器：

- `forward_list`
    
- `unordered_*`
    

---

## 五、Bidirectional Iterator：新增 `--`

### 4️⃣ 递减（Decrement）

```cpp
--it
it--
```

**含义**

- 指向前一个元素
    

📌 容器：

- `list`
    
- `set / map`
    
- `multiset / multimap`
    

🚫 不支持随机跳跃

---

## 六、Random Access Iterator：真正“像指针”

这是 operations **最多、也是最容易考/面试问错的一类**

### 5️⃣ 算术运算

```cpp
it + n
it - n
it += n
it -= n
```

**含义**

- O(1) 跳转 n 个元素
    

---

### 6️⃣ 两个迭代器求距离

```cpp
it2 - it1   // 返回 difference_type
```

📌 **只有 Random Access 才支持**

---

### 7️⃣ 下标访问

```cpp
it[n]   // 等价于 *(it + n)
```

📌 这就是 `vector` 能 `it[3]`，`list` 不行的原因

---

### 8️⃣ 关系比较

```cpp
it1 < it2
it1 > it2
it1 <= it2
it1 >= it2
```

📌 表示**位置顺序**

---

📌 容器：

- `vector`
    
- `deque`
    
- `array`
    

---

## 七、Contiguous Iterator（C++20，新但很重要）

### 新增能力：**内存连续**

```cpp
std::to_address(it)
```

**语义**

- 迭代器指向真实连续内存
    
- 可安全转换为指针
    

📌 容器：

- `vector`
    
- `array`
    
- `string`
    

🚫 `deque` **不是 contiguous**（虽然是 random access）

---

## 八、反向迭代器的特殊 operations（容易踩坑）

```cpp
reverse_iterator rit;
```
反向迭代器的减相当于正向迭代器的加
### 关键区别

```cpp
*rit        // 实际访问的是前一个元素
rit.base()  // 返回“正向迭代器”
```

📌 关系：

```cpp
rit.base() == it
*rit == *(it - 1)
```

⚠️ 这是面试和调试中**最常出错的点**

---

## 九、Iterator Operations 与算法的关系（本质）

标准算法是这样写的：

```cpp
template<class It>
void algo(It first, It last);
```

但内部会**按 operations 选择实现策略**：

| 算法         | 最低要求              |
| ---------- | ----------------- |
| `find`     | Input             |
| `copy`     | Input + Output    |
| `sort`     | Random Access     |
| `reverse`  | Bidirectional     |
| `advance`  | Input（但随机访问更快）    |
| `distance` | Input（但随机访问 O(1)） |

👉 **算法不是按容器限制，而是按 iterator operations 限制**

---

[[迭代器统一接口函数]]

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[学习/编程语言/C++/STL/Iterator/Iterator是什么]]
- [[学习/编程语言/C++/STL/Iterator/Iterator分类]]
- [[学习/编程语言/C++/STL/Iterator/迭代器统一接口函数]]
