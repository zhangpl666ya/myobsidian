## 一、什么是 `std::deque`？

`std::deque`（double-ended queue，双端队列）是 **顺序容器**，它支持从队列的 **两端**进行高效的插入和删除操作。

- 它是一个 **双端容器**，可以在 **两端**（头部和尾部）进行 **插入（push）和删除（pop）** 操作。
    
- **随机访问**：`std::deque` 支持随机访问（类似于 `std::vector`），通过下标 `[]` 可以访问容器中的任意元素。
    

---

## 二、deque 的特点

### ✅ 特点：

- 支持 **头尾插入和删除** 操作（O(1) 时间复杂度）
    
- 支持 **随机访问**，即可以通过下标访问任意元素（O(1) 时间复杂度）
    
- 它的底层实现是由 **多个块（block）组成的**，每个块都是一块固定大小的内存空间。与 `std::vector` 不同的是，`std::deque` 不是一个单一的连续内存块，而是一个内存块链表结构。
    

### ❌ 限制：

- 相比 `std::vector`，`std::deque` 的 **中间插入和删除** 操作的时间复杂度是 O(n)，因为要移动元素。
    
- 它的内存管理稍微复杂一些，由于其底层由多个内存块组成，因此会比 `std::vector` 多一些管理开销。
    

---

## 三、deque 常用接口

|函数|作用|
|---|---|
|`push_front(x)`|在队列前端插入元素|
|`push_back(x)`|在队列后端插入元素|
|`pop_front()`|移除队列前端元素|
|`pop_back()`|移除队列后端元素|
|`front()`|获取队列前端元素|
|`back()`|获取队列后端元素|
|`empty()`|判断队列是否为空|
|`size()`|获取队列中元素个数|
|`operator[]`|随机访问元素|
|`at()`|安全的访问元素（会检查越界）|
|`insert()`|插入元素（支持中间插入）|
|`erase()`|删除指定元素|

---

## 四、基本使用示例

### 1️⃣ 向前和向后插入元素

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;

    dq.push_back(10);   // 插入尾部
    dq.push_front(5);   // 插入头部
    dq.push_back(20);   // 插入尾部

    // 输出：5 10 20
    for (int x : dq) {
        cout << x << " ";
    }

    return 0;
}
```

### 2️⃣ 随机访问和删除元素

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;

    dq.push_back(10);
    dq.push_back(20);
    dq.push_back(30);

    // 随机访问
    cout << dq[1] << endl;  // 20
    cout << dq.at(2) << endl;  // 30

    // 删除元素
    dq.pop_front();  // 删除头部元素
    dq.pop_back();   // 删除尾部元素

    // 输出：20
    cout << dq.front() << endl;

    return 0;
}
```

### 3️⃣ 使用 `insert()` 和 `erase()` 插入和删除中间元素

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;

    dq.push_back(10);
    dq.push_back(20);
    dq.push_back(30);

    // 插入元素
    dq.insert(dq.begin() + 1, 15);  // 在第二个位置插入 15

    // 删除元素
    dq.erase(dq.begin() + 2);  // 删除第三个位置的元素

    // 输出：10 15 30
    for (int x : dq) {
        cout << x << " ";
    }

    return 0;
}
```

---

## 五、`deque` 的底层实现

`std::deque` 并不像 `std::vector` 那样是一个连续的内存块，它是由多个 **固定大小的块** 组成的。这使得它可以支持 **两端高效的插入和删除**。

具体来说，`std::deque` 的底层实现是：

- 维护一个指向多个块的指针数组。
    
- 每个块内部是一个连续的内存区域。
    
- 插入和删除操作时，`deque` 会在头尾添加或删除内存块。
    

这种结构的优势是：

- **尾部和头部操作**：在队列的两端插入或删除元素时，由于每个块都是独立的，操作时间复杂度为 O(1)。
    
- **随机访问**：每个块都能提供 **O(1)** 的随机访问。
    

---

## 六、`deque` 的应用场景

### 1️⃣ **双端队列**

当你需要从队列的两端进行插入和删除操作时，`std::deque` 是一个非常合适的选择。

### 2️⃣ **实现队列/栈**

`std::deque` 既可以当作队列（FIFO）使用，也可以当作栈（LIFO）使用。  
例如：

- 使用 `push_back()` 和 `pop_front()` 可以实现队列。
    
- 使用 `push_back()` 和 `pop_back()` 可以实现栈。
    

### 3️⃣ **滑动窗口问题**

在一些算法题中，例如滑动窗口问题，`std::deque` 用来维护一个滑动窗口，既能够从两端快速插入删除，又能支持快速访问。

---

## 七、`deque` vs `vector`

|特性|`std::vector`|`std::deque`|
|---|---|---|
|访问元素|O(1) 随机访问|O(1) 随机访问|
|插入/删除|O(n)（中间插入/删除）|O(1)（两端插入/删除）|
|内存管理|连续的内存块|多个固定大小的内存块组成|
|内存开销|较低|较高（需要更多的内存管理开销）|

---

## 八、注意事项

⚠️ **内存管理**：虽然 `std::deque` 支持高效的头尾操作，但由于其底层结构，内存管理的开销比 `std::vector` 稍大。如果你不需要两端的插入删除操作，优先考虑使用 `std::vector`。

⚠️ **插入和删除的时间复杂度**：尽管头尾的插入和删除是 O(1)，但 **中间的插入和删除** 时间复杂度为 O(n)。

>deque的迭代器分为iterator、const_iterator、reverse_iterator、const_reverse_iterator
>迭代器标签为bidirectional_iterator
---

## 九、一句话总结

> `std::deque` 是一个 **双端队列**，支持高效的两端插入和删除操作，且提供 **随机访问**，非常适合需要在两端频繁操作的场景。

---
