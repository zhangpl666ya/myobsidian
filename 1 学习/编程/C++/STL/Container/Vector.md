
### 1. 本质与定位

- 底层是**动态分配的连续内存数组**，逻辑上元素连续存储（支持随机访问）。
- 属于 “序列容器”（sequence container），元素按插入顺序排列，无自动排序功能。
- 与静态数组（`int arr[N]`）对比：
    - 优势：动态扩容、支持自动管理内存、提供丰富成员函数。
    - 劣势：扩容时可能拷贝元素（有性能开销）、中间插入 / 删除效率低。
```cpp
template <typename T>
class vector {
private:
    T* _ptr;       // 指向堆内存的指针（存数据）——8字节（64位）
    size_t _size;  // 当前元素个数——8字节
    size_t _cap;   // 已分配的容量——8字节
    // （部分编译器会加1个标记位，比如4字节，凑够32字节）
};
```
### 2. 关键特性

| 特性        | 说明                                                                     |
| --------- | ---------------------------------------------------------------------- |
| 随机访问      | 支持 `[]` 和 `at()` 访问，时间复杂度 O (1)                                        |
| 尾部操作      | `push_back()`/`pop_back()` 高效， amortized O (1)（平均复杂度）                  |
| 中间 / 头部操作 | `insert()`/`erase()` 需移动元素，时间复杂度 O (n)                                 |
| 动态扩容      | 容量不足时自动分配更大内存（通常是原容量的 1.5 倍或 2 倍，依赖编译器），拷贝旧元素到新内存                      |
| 内存管理      | 自动释放内存（析构时销毁元素并释放底层数组），但不会自动缩容（需手动优化）                                  |
| 元素要求      | 需支持拷贝构造 / 移动构造（C++11+），不支持引用类型（需用 `vector<std::reference_wrapper<T>>`） |

### 3. 扩容机制

1. 当 `size() == capacity()` 时，执行扩容：
    - 分配新内存（容量 = 原容量 × 扩容因子，如 GCC 是 2，MSVC 是 1.5）。
    - 拷贝（C++11 前）或移动（C++11 后，元素支持移动语义）旧元素到新内存。
    - 释放旧内存。
2. 扩容开销：频繁扩容会导致多次拷贝，可通过 `reserve()` 预分配容量减少开销。

## 二、基础使用（必备语法）

### 1. 头文件与命名空间

cpp

```cpp
#include <vector>  // 必须包含
using namespace std;  // 或显式使用 std::vector
```

### 2. 初始化方式（C++98 ~ C++20）

|初始化方式|示例代码|说明|
|---|---|---|
|默认初始化|`vector<int> v;`|空向量，size=0，capacity=0（GCC）或默认小容量（MSVC）|
|指定大小 + 默认值|`vector<int> v(5);` `vector<int> v(5, 10);`|前者初始化为 5 个 0，后者初始化为 5 个 10（size=5，capacity≥5）|
|拷贝初始化|`vector<int> v1 = {1,2,3};` `vector<int> v2(v1);` `vector<int> v3 = v1;`|拷贝列表 / 另一个向量的元素|
|移动初始化（C++11+）|`vector<int> v4 = std::move(v1);`|转移 v1 的资源（v1 变为空，无拷贝开销）|
|迭代器范围初始化|`vector<int> v5(v2.begin(), v2.end());` `int arr[] = {1,2}; vector<int> v6(arr, arr+2);`|从其他容器 / 数组的迭代器范围初始化|
|列表初始化（C++11+）|`vector<int> v7{1,2,3,4};` `vector<string> v8{"a", "bc", "def"};`|直接用花括号指定元素，类型需匹配|
|填充初始化（C++20+）|`vector<int> v9(3, 100);` 同 “指定大小 + 默认值”，C++20 增强兼容性||

### 3. 核心成员函数（按功能分类）

#### （1）容量相关（Capacity）

| 函数名                       | 功能说明                                                |
| ------------------------- | --------------------------------------------------- |
| `size()`                  | 返回当前元素个数（`size_t` 类型）                               |
| `capacity()`              | 返回当前底层数组的容量（能容纳的最大元素个数，不扩容情况下）                      |
| `empty()`                 | 判断是否为空（`size() == 0`），返回 `bool`，效率比 `size() == 0` 高 |
| `reserve(n)`              | 预分配容量至少为 `n`（若 `n <= capacity()` 则无操作），仅改变容量不改变大小   |
| `shrink_to_fit()`（C++11+） | 尝试将容量缩减至与大小一致（非强制，编译器可能忽略），用于释放多余内存                 |

#### （2）元素访问（Element Access）

| 函数名              | 功能说明                                        | 注意事项                               |
| ---------------- | ------------------------------------------- | ---------------------------------- |
| `operator[]`     | 随机访问第 `i` 个元素（0 索引），返回引用                    | 不做越界检查，越界行为未定义（UB）                 |
| `at(i)`          | 随机访问第 `i` 个元素，返回引用                          | 越界时抛出 `std::out_of_range` 异常，安全但略慢 |
| `front()`        | 返回第一个元素的引用                                  | 向量为空时调用未定义                         |
| `back()`         | 返回最后一个元素的引用                                 | 向量为空时调用未定义                         |
| `data()`（C++11+） | 返回底层数组的首元素指针（`T*`），可用于兼容 C 风格函数（如 `memcpy`） | 空向量返回 `nullptr`                    |

#### （3）修改操作（Modifiers）

| 函数名                                    | 功能说明                                                  | 时间复杂度                             |
| -------------------------------------- | ----------------------------------------------------- | --------------------------------- |
| `push_back(val)`                       | 在尾部添加元素 `val`（可能触发扩容）                                 | amortized O(1)                    |
| `emplace_back(args...)`（C++11+）        | 在尾部直接构造元素（传递构造函数参数），避免拷贝 / 移动开销                       | amortized O (1)（比 `push_back` 高效） |
| `pop_back()`                           | 删除尾部元素（不返回元素），不改变容量                                   | O(1)                              |
| `insert(pos, val)`                     | 在迭代器 `pos` 位置插入元素 `val`                               | O (n)（需移动 `pos` 后所有元素）            |
| `insert(pos, n, val)`                  | 在 `pos` 位置插入 `n` 个 `val`                              | O(n)                              |
| `insert(pos, first, last)`             | 在 `pos` 位置插入迭代器 `[first, last)` 范围的元素                 | O(n + (last - first))             |
| `emplace(pos, args...)`（C++11+）        | 在 `pos` 位置直接构造元素                                      | O(n)                              |
| `erase(iterator pos)`                  | 删除 `pos` 位置的元素，返回下一个元素的迭代器                            | O(n)                              |
| `erase(iterator first, iterator last)` | 删除 `[first, last)` 范围的元素，返回下一个元素的迭代器                  | O(n)                              |
| `clear()`                              | 删除所有元素（`size()` 变为 0），但不释放容量（`capacity()` 不变）         | O (n)（销毁元素，不释放内存）                 |
| `swap(v)`                              | 与另一个向量 `v` 交换内容、大小和容量（无元素拷贝，仅交换指针，O (1)）              | 比 `v1 = v2` 高效（无扩容拷贝）             |
| `assign(n, val)`                       | 清空容器，换成 `n` 个 `val`                                   | O(n)                              |
| `assign(first, last)`                  | 清空元素，换成`[first, last)` 范围的元素（可以是别的vector的迭代器，会自动补齐大小） | O(n)                              |


## 三、进阶用法

### 1. 迭代器（遍历核心）

vector 支持随机访问迭代器（最灵活的迭代器类型），遍历方式包括：

#### （1）迭代器类型

|迭代器类型|用途|示例代码|
|---|---|---|
|普通迭代器（`iterator`）|遍历并修改元素|`for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) *it = 10;`|
|常量迭代器（`const_iterator`）|遍历但不修改元素（只读）|`for (vector<int>::const_iterator it = v.cbegin(); it != v.cend(); ++it) cout << *it;`|
|反向迭代器（`reverse_iterator`）|反向遍历（从尾到头）|`for (vector<int>::reverse_iterator it = v.rbegin(); it != v.rend(); ++it) cout << *it;`|
|常量反向迭代器（`const_reverse_iterator`）|反向只读遍历|`for (auto it = v.crbegin(); it != v.crend(); ++it) cout << *it;`|

#### （2）简化遍历方式（C++11+）

- 范围 for 循环（最简洁）：
```cpp
vector<int> v = {1,2,3};
for (int x : v) cout << x;  // 只读
for (int& x : v) x *= 2;    // 可修改（需引用）
   ```

- `auto` 简化迭代器：
```cpp
   for (auto it = v.begin(); it != v.end(); ++it) { ... }
   for (auto it = v.cbegin(); it != v.cend(); ++it) { ... }  // 只读
  ```


#### （3）迭代器失效问题（重点！）

vector 迭代器在修改容器后可能失效（指向非法内存），核心规则：

1. **扩容触发时**：`push_back()`/`emplace_back()`/`reserve()` 若导致扩容，所有迭代器（`begin()`/`end()`/ 元素指针）全部失效。
2. **插入操作**：在 `pos` 位置插入元素后，`pos` 及之后的迭代器失效（元素后移），之前的迭代器有效。
3. **删除操作**：删除 `pos` 位置元素后，`pos` 及之后的迭代器失效（元素前移），返回的新迭代器指向原 `pos` 的下一个元素（有效）。
4. **clear()/assign()**：所有迭代器失效（元素被销毁）。

```cpp
// 错误：删除元素后迭代器 it 失效，++it 非法
for (auto it = v.begin(); it != v.end(); ++it) {
  if (*it % 2 == 0) v.erase(it);  // 错误！it 已失效
}

// 正确：用 erase() 返回的新迭代器更新
for (auto it = v.begin(); it != v.end(); ) {
  if (*it % 2 == 0) {
    it = v.erase(it);  // 接收新迭代器，不 ++
  } else {
    ++it;
  }
}
```

### 2. 元素类型扩展

vector 支持任意可拷贝 / 移动的类型，包括：

- 基本类型（`int`/`double`/`char` 等）。
- 自定义类 / 结构体（需满足：无默认构造时初始化需指定元素，支持拷贝 / 移动）：
```cpp
   struct Person {
   string name;
   int age;
   Person(string n, int a) : name(n), age(a) {}  // 自定义构造函数
};
 vector<Person> people = {{"Alice", 20}, {"Bob", 25}};  // 列表初始化
 people.emplace_back("Charlie", 30);  // 直接构造，无需临时对象
```

- 智能指针（避免内存泄漏，推荐 `unique_ptr`/`shared_ptr`）：
  ```cpp
 vector<unique_ptr<int>> v;
 v.emplace_back(new int(10));  // 正确（C++11+）
v.push_back(make_unique<int>(20));  // 更安全（C++14+）
// 注意：unique_ptr 不可拷贝，需用 emplace_back/push_back 移动语义
```

- 容器嵌套（如二维 vector）：
 ```cpp
vector<vector<int>> matrix(3, vector<int>(4, 0));  // 3行4列的二维数组，初始值0
matrix[0][1] = 5;  // 访问第0行第1列元素
```


### 3. 内存管理技巧

#### （1）预分配容量减少扩容

频繁 `push_back()` 时，先用 `reserve(n)` 预分配足够容量，避免多次扩容拷贝：

cpp

```cpp
vector<int> v;
v.reserve(1000);  // 预分配1000个元素容量
for (int i = 0; i < 1000; ++i) {
  v.push_back(i);  // 无扩容，效率极高
}
```

#### （2）释放多余内存

`clear()` 仅清空元素，容量不变，需释放内存可结合 `shrink_to_fit()` 或 `swap()` 技巧：

cpp

```cpp
vector<int> v(1000, 0);
v.clear();  // size=0，capacity=1000
v.shrink_to_fit();  // 尝试将 capacity 缩为 0（C++11+）

// 兼容C++11前的缩容技巧（swap交换空向量）
vector<int>().swap(v);  // v 与临时空向量交换，临时对象销毁时释放内存
```

#### （3）避免浅拷贝问题

若 vector 存储指针 / 原始指针，需手动管理内存（避免内存泄漏），推荐用智能指针：

cpp

```cpp
// 错误：原始指针易泄漏（vector 析构仅销毁指针，不释放指向的内存）
vector<int*> v;
v.push_back(new int(10));
// 需手动释放：
for (int* p : v) delete p;
v.clear();

// 正确：用 unique_ptr 自动管理
vector<unique_ptr<int>> v;
v.emplace_back(new int(10));
// 无需手动释放，vector 析构时会销毁 unique_ptr，自动释放内存
```

### 4. 算法结合（STL 算法）

vector 可与 `<algorithm>` 库的算法配合使用（依赖随机访问迭代器）：

cpp

```cpp
#include <algorithm>

vector<int> v = {3,1,4,1,5,9};

// 1. 排序（默认升序）
sort(v.begin(), v.end());  // v = [1,1,3,4,5,9]
sort(v.rbegin(), v.rend());  // 降序：[9,5,4,3,1,1]

// 2. 查找
auto it = find(v.begin(), v.end(), 4);  // 查找元素4，返回迭代器
if (it != v.end()) cout << "找到：" << *it << endl;

// 3. 去重（需先排序）
sort(v.begin(), v.end());
v.erase(unique(v.begin(), v.end()), v.end());  // 去重后 v = [1,3,4,5,9]

// 4. 反转
reverse(v.begin(), v.end());  // v = [9,5,4,3,1]

// 5. 计数
int cnt = count(v.begin(), v.end(), 1);  // 统计元素1的个数

// 6. 替换
replace(v.begin(), v.end(), 3, 30);  // 将所有3替换为30
```

## 四、性能优化指南

### 1. 减少扩容次数

- 已知元素个数时，优先用 `reserve(n)` 预分配容量（如读取文件前预估数据量）。
- 批量添加元素时，用 `insert()` 一次性插入范围元素，而非多次 `push_back()`。

### 2. 优先使用 `emplace_back` 而非 `push_back`

`emplace_back` 直接在容器尾部构造元素，避免 `push_back` 可能产生的临时对象拷贝 / 移动开销：

cpp

```cpp
// 自定义类
struct Person {
  string name;
  int age;
  Person(string n, int a) : name(n), age(a) {}
};

vector<Person> v;
v.push_back(Person("Alice", 20));  // 先构造临时对象，再移动/拷贝到容器
v.emplace_back("Bob", 25);         // 直接在容器内构造，无临时对象
```

### 3. 避免不必要的拷贝

- 传递 vector 时，优先用**引用**（`const vector<T>&` 只读，`vector<T>&` 可修改），避免值传递导致的深拷贝。
- 返回 vector 时，依赖 C++11+ 的**返回值优化（RVO/NRVO）**，无需手动 `std::move`（编译器自动优化）：
    
    cpp
    
    ```cpp
    vector<int> createVector() {
      vector<int> v = {1,2,3};
      return v;  // 编译器优化为直接构造到调用者，无拷贝
    }
    ```
    

### 4. 合理选择遍历方式

- 只读遍历：优先用 `const_iterator` 或范围 for 循环（`const auto& x : v`），避免无意修改且可能提升缓存效率。
- 频繁访问元素时，避免用 `at()`（异常检查开销），优先用 `[]`（确保不越界的前提下）。

### 5. 避免中间插入 / 删除

vector 中间插入 / 删除需移动大量元素，若需频繁在头部 / 中间操作，考虑用 `std::list` 或 `std::deque`；若必须用 vector，可批量操作后排序（如先 `push_back` 所有元素，再 `sort`，比插入时保持有序更高效）。

## 五、常见误区与注意事项

### 1. 迭代器失效踩坑

- 扩容后迭代器失效：`push_back` 后若容量变化，之前的迭代器 / 指针 / 引用全部失效，不可再使用。
- 删除元素后未更新迭代器：如前文 “迭代器失效” 示例，需用 `erase()` 返回的新迭代器。

### 2. 混淆 `size()` 与 `capacity()`

- `size()` 是当前元素个数，`capacity()` 是最大容纳个数（不扩容），`size() <= capacity()` 恒成立。
- `clear()` 仅重置 `size()` 为 0，`capacity()` 不变，内存未释放。

### 3. 存储引用或不可拷贝类型

- vector 不支持存储引用（引用无默认构造和赋值操作），需用 `std::reference_wrapper<T>`：

    ```cpp
    vector<reference_wrapper<int>> v;
    int a = 10, b = 20;
    v.push_back(a);
    v.push_back(b);
    v[0].get() = 100;  // a 变为 100
    ```
    
- 存储不可拷贝类型（如 `unique_ptr`）时，不可用 `copy` 算法或 `v1 = v2`（需用 `move` 语义）：

    ```cpp
    vector<unique_ptr<int>> v1, v2;
    v1.emplace_back(new int(10));
    // v2 = v1;  // 错误：unique_ptr 不可拷贝
    v2 = std::move(v1);  // 正确：移动语义，v1 变为空
    ```
    

### 4. 二维 vector 初始化效率

直接初始化 `vector<vector<int>> mat(m, vector<int>(n))` 效率较高，避免手动嵌套 `push_back`：
```cpp
// 低效：多次扩容
vector<vector<int>> mat;
mat.reserve(m);
for (int i = 0; i < m; ++i) {
  vector<int> row;
  row.reserve(n);
  for (int j = 0; j < n; ++j) row.push_back(0);
  mat.push_back(row);
}

// 高效：一次性初始化
vector<vector<int>> mat(m, vector<int>(n, 0));
```

### 5. 跨编译器扩容因子差异

不同编译器的 vector 扩容因子不同（GCC 2 倍，MSVC 1.5 倍），依赖扩容后迭代器有效性的代码可能跨平台出错，需避免。

## 六、与其他容器的对比

| 容器       | 随机访问 | 尾部操作 | 中间插入 / 删除 | 内存连续性 | 适用场景             |
| -------- | ---- | ---- | --------- | ----- | ---------------- |
| `vector` | O(1) | O(1) | O(n)      | 连续    | 随机访问、尾部增删、批量操作   |
| `list`   | O(n) | O(1) | O(1)      | 不连续   | 频繁中间插入 / 删除      |
| `deque`  | O(1) | O(1) | O (n)（中间） | 分段连续  | 头部 / 尾部增删频繁、随机访问 |
| `array`  | O(1) | 不支持  | 不支持       | 连续    | 固定大小、无需动态扩容      |
|          |      |      |           |       |                  |

**结论**：大部分场景下 vector 是最优选择，仅当需要频繁中间插入 / 删除时考虑 list，头部操作频繁时考虑 deque。