请先看这篇：[[Iterator是什么]]

### 1. **输入迭代器 (Input Iterator)**

- **特点**：只能一次性读取元素，适用于流式读取数据。不能修改元素，且只能进行单向遍历。
    
- **支持操作**：`*it`（读取元素）、`++it`（前进到下一个元素）。
    
- **适用容器**：
    
    - **流容器**：如`std::istream_iterator`，适用于从输入流中读取数据。
        

#### **例子：**

```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <sstream>

int main() {
    std::istringstream stream("10 20 30");
    std::istream_iterator<int> it(stream), end;
    while (it != end) {
        std::cout << *it << " ";  // 逐个读取元素
        ++it;
    }
    return 0;
}
```

这里使用了`std::istream_iterator`来从`std::istringstream`读取数据，适用于按顺序读取数据的场景。

---

### 2. **输出迭代器 (Output Iterator)**

- **特点**：只能写入数据，不能读取。适用于向容器或输出流写入数据。
    
- **支持操作**：`*it`（写入数据）、`++it`（前进到下一个位置）。
    
- **适用容器**：
    
    - **流容器**：如`std::ostream_iterator`，适用于将数据写入输出流。
        
    - 适用于**所有容器**，例如将容器元素写入输出流等场景。
        

#### **例子：**

```cpp
#include <iostream>
#include <iterator>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
    std::ostream_iterator<int> out(std::cout, " ");
    for (const auto& val : v) {
        *out++ = val;  // 将数据写入标准输出流
    }
    return 0;
}
```

在这个例子中，`std::ostream_iterator`用于将`std::vector`中的数据写入标准输出。

---

### 3. **前向迭代器 (Forward Iterator)**

- **特点**：支持多次遍历，可以反复读取和修改元素。只能向前迭代，不能回溯。
    
- **支持操作**：`*it`（读取或修改元素）、`++it`（前进到下一个元素）。
    
- **适用容器**：
    
    - **`std::forward_list`**：单向链表，使用前向迭代器。
        
    - **`std::list`**：双向链表，但也支持前向迭代器。
        

#### **例子：**

```cpp
#include <iostream>
#include <forward_list>

int main() {
    std::forward_list<int> fl = {1, 2, 3, 4};
    for (auto it = fl.begin(); it != fl.end(); ++it) {
        std::cout << *it << " ";  // 遍历每个元素
    }
    return 0;
}
```

在`std::forward_list`中，前向迭代器能够顺序访问元素。对于不需要双向遍历的链表，`forward_iterator`性能较优。

---

### 4. **双向迭代器 (Bidirectional Iterator)**

- **特点**：支持双向遍历，可以同时向前和向后移动。适用于双向链表结构。
    
- **支持操作**：`*it`（读取或修改元素）、`++it`（前进到下一个元素）、`--it`（回退到上一个元素）。
    
- **适用容器**：
    
    - **`std::list`**：双向链表，支持双向迭代器。
        
    - **`std::set`、`std::map`**：基于红黑树实现的容器，支持双向迭代器。
        

#### **例子：**

```cpp
#include <iostream>
#include <list>

int main() {
    std::list<int> l = {10, 20, 30, 40};
    auto it = l.begin();
    ++it;  // 前进到第二个元素
    --it;  // 回退到第一个元素
    std::cout << *it << std::endl;  // 输出 10
    return 0;
}
```

`std::list`支持双向迭代器，允许我们在容器中前进和回退。对于频繁插入删除的场景，`std::list`表现优异。

---

### 5. **随机访问迭代器 (Random Access Iterator)**

- **特点**：支持完全随机访问，允许通过加减整数直接跳转到容器中的任意位置，类似于数组指针。
    
- **支持操作**：`*it`（读取或修改元素）、`++it`、`--it`、`it + n`、`it - n`、`it[n]`。
    
- **适用容器**：
    
    - **`std::vector`**：动态数组，支持随机访问迭代器。
        
    - **`std::deque`**：双端队列，也支持随机访问迭代器。
        
    - **`std::array`**：固定大小的数组，支持随机访问。
        

#### **例子：**

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4};
    auto it = v.begin();
    it += 2;  // 跳转到第三个元素
    std::cout << *it << std::endl;  // 输出 3
    return 0;
}
```

`std::vector`和`std::deque`都支持随机访问迭代器，允许我们高效地进行索引操作，适合需要频繁随机访问的场景。

---

### 6. **常量迭代器 (Const Iterator)**

- **特点**：与普通迭代器相似，但无法修改容器中的元素，只能读取。
    
- **支持操作**：`*it`（只读）、`++it`（前进到下一个元素）。
    
- **适用容器**：
    
    - **所有容器**：所有容器都可以使用常量迭代器。
        
    - 适用于只读操作，防止对容器进行修改。
        

#### **例子：**

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30, 40};
    for (std::vector<int>::const_iterator it = v.begin(); it != v.end(); ++it) {
        std::cout << *it << " ";  // 只能读取，不可修改
    }
    return 0;
}
```

常量迭代器常用于只读场景，确保容器元素不被修改，适合需要保护容器数据的场景。

---

### 7. **反向迭代器 (Reverse Iterator)**

- **特点**：用于反向遍历容器，从尾部开始访问。
    
- **支持操作**：`*it`（读取或修改元素）、`++it`（前进到前一个元素）、`--it`（回退到下一个元素）。
    
- **适用容器**：
    
    - **`std::vector`**、**`std::deque`**、**`std::list`** 等，支持反向遍历的容器。
        

#### **例子：**

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30, 40};
    for (auto it = v.rbegin(); it != v.rend(); ++it) {
        std::cout << *it << " ";  // 反向遍历
    }
    return 0;
}
```

通过`rbegin()`和`rend()`，我们可以在`std::vector`中使用反向迭代器进行倒序遍历。

---

### 总结

| **容器分类**   | **容器名称**              | **迭代器类型**                | **关键特性**                       |
| ---------- | --------------------- | ------------------------ | ------------------------------ |
| **序列式容器**  | `std::vector`         | **随机访问 (Random Access)** | 支持 `it + 5` 或 `it[3]`，效率最高     |
|            | `std::deque`          | **随机访问 (Random Access)** | 虽然内存不连续，但模拟了随机访问               |
|            | `std::array`          | **随机访问 (Random Access)** | 固定大小的数组                        |
|            | `std::list`           | **双向 (Bidirectional)**   | 只能 `++it` 或 `--it`，不能 `it + 2` |
|            | `std::forward_list`   | **前向 (Forward)**         | 只能 `++it`，没有 `--it`            |
| **关联式容器**  | `std::set / multiset` | **双向 (Bidirectional)**   | 元素有序，支持双向遍历                    |
|            | `std::map / multimap` | **双向 (Bidirectional)**   | 元素有序，支持双向遍历                    |
| **无序关联容器** | `unordered_set / map` | **前向 (Forward)**         | 哈希表实现，通常只支持单向向前                |
| **容器适配器**  | `stack / queue`       | **无迭代器**                 | 封闭式结构，不支持迭代器访问                 |
[[Iterator Operations]]