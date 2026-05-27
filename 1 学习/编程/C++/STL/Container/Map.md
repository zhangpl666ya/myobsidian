定义在map头文件中
# 是什么?
道理和[[Set]]有相似之处，
底层由红黑树实现，元素是`std::pair<const Key, T>`类型
## 核心特点
- **键值对存储**：元素为`std::pair<const Key, T>`类型，key不可修改，value可以修改
- **键唯一**：不允许重复键，插入冲附件会被忽略（insert返回值判断）
- **自动排序**：默认按key的升序排列（也可以自定义比较函数修改规则）
- **高效操作**：插入、删除、查找的时间复杂度仅为logn
- **非连续存储**：元素在内存中分布不连续，迭代器是双向迭代器，支持++/--，不支持随机访问

key可以是自定义类型，但一定要[[重载运算符]]<，否则无法排序
# 怎么用
## 构造与初始化
### 1、空构造
```cpp
std::map<int, string> m; //空std::map，键为int，值为string
```
### 2、初始化列表（c++11及以上）
```cpp
std::map<int,string> m = {
	{1, "a"},
	{2, "b"},
	{3, "c"}
};//初始化后：1->a, 2->b, 3->c
```
### 3、拷贝构造
```cpp
std::map<int, string> m2(m1);//m1构造m2
```
### 4、自定义排序规则
默认排序是`std::less<key>`升序，可修改：
```cpp
std::map<int, string, greater<int>> m_desc //按降序排列

struct StrlenCmp{
	bool operator()(cont string& s1, const string& s2) const{
		return s1.size() < s2.size();//按字符串长度升序
	}
}
std::map<string, int, StrLenCmp> m;
```
但这个伪函数实在难写，可以用std::function包装lambda传入
但能写尽量写
## 核心操作
### 1、插入元素
- []运算符：最简洁，不存在插入，存在就修改值（若键不存在会默认构造一个值）
- `insert()`函数：插入键值对，返回`pair<iterator, bool>`（bool表示是否成功，iterator指向插入位置或已有键的位置）
- `emplace()`函数：直接在容器内构造元素（C++11以上）
- 范围插入：插入另一个map的部分元素
```cpp
std::map<int, string> m;
m[1] = "a";//1->a
m[2] = "b";//2->b
m[1] = "c";//修改为1->c

auto ret1 = m.insert{{3,"c"}}; //插入成功，ret1.second = true
auto ret2 = m.insert{{3,"cc"}};//失败，ret2.second = false

m.emplace(4,"d");//效率更高

std::map<int, string> m2 = {{5,"e"},{6,"f"}};
m.insert(m2.begin(),m2.end());//插入迭代器中的元素
```

#### 2. 删除元素

- 按 **键删除**：`erase(key)`，返回删除的元素个数（0 或 1）；
- 按 **迭代器删除**：`erase(iterator)`，返回下一个迭代器；
- 按 **范围删除**：`erase(begin, end)`，删除 \[ begin, end) 区间的元素。(左开右闭)
```cpp
map<int, string> m = {{1, "a"}, {2, "b"}, {3, "c"}, {4, "d"}};

// 1. 按键删除
m.erase(2); // 删除键 2，返回 1（删除成功）
m.erase(5); // 键 5 不存在，返回 0

// 2. 按迭代器删除
auto it = m.find(3); // 先找到键 3 的迭代器
if (it != m.end()) {
    m.erase(it); // 删除迭代器指向的元素（3→c）
}

// 3. 范围删除（删除所有元素）
m.erase(m.begin(), m.end()); // 等价于 m.clear()
```

#### 3. 查找元素

- **`find(key)`**：返回指向键 `key` 的迭代器，若不存在则返回 `m.end()`；
- `at(key)`：和别的at用法一样，不存在抛出`std::out_of_range`异常；
- **`count(key)`**：返回键 `key` 的个数（0 或 1，因为键唯一）；
- **`lower_bound(key)`**：返回第一个 **大于等于** `key` 的元素迭代器；
- **`upper_bound(key)`**：返回第一个 **大于** `key` 的元素迭代器。
```cpp
map<int, string> m = {{1, "a"}, {2, "b"}, {3, "c"}};

// 1. find() 查找
auto it = m.find(2);
if (it != m.end()) {
    cout << "键 2 的值：" << it->second << endl; // 输出：b
} else {
    cout << "键 2 不存在" << endl;
}

// 2. count() 判断是否存在
if (m.count(3)) {
    cout << "键 3 存在" << endl;
}

// 3. lower_bound/upper_bound（常用于范围查询）
auto it_low = m.lower_bound(2);  // 指向 2→b
auto it_high = m.upper_bound(2); // 指向 3→c
// 遍历 [2, 3) 区间（即键 2）
for (auto it = it_low; it != it_high; ++it) {
    cout << it->first << "→" << it->second << endl;
}
```
#### 4. 修改元素

- 直接通过 **迭代器修改**：`it->second = 新值`（`key` 不可修改，因为 `it->first` 是 `const`）；
- 通过 **`[]` 运算符修改**：`m[key] = 新值`（键不存在则插入）。
- ```cpp
map<int, string> m = {{1, "a"}};

// 1. 迭代器修改
auto it = m.find(1);
if (it != m.end()) {
    it->second = "modified"; // 键 1 的值改为 "modified"
}

// 2. [] 运算符修改
m[1] = "updated"; // 直接修改
```
### 五、常用成员函数

|函数名|功能描述|
|---|---|
|`size()`|返回元素个数|
|`empty()`|判断容器是否为空（空返回 true）|
|`clear()`|清空所有元素|
|`begin()`/`end()`|返回首 / 尾迭代器（`end()` 是尾后位置，不指向元素）|
|`rbegin()`/`rend()`|返回反向迭代器（从尾到头遍历）|
|`swap(map&)`|交换两个 map 的内容（同类型）|
### 六、遍历 map 的 3 种方式

#### 1. 迭代器遍历（兼容所有 C++ 版本）
```cpp
map<int, string> m = {{1, "a"}, {2, "b"}, {3, "c"}};
for (auto it = m.begin(); it != m.end(); ++it) {
    cout << it->first << "→" << it->second << endl; // 键：it->first，值：it->second
}
```
#### 2. 范围 for 遍历（C++11 及以上，简洁）
```cpp
for (const auto& pair : m) {
    cout << pair.first << "→" << pair.second << endl; // pair 是 std::pair<const int, string>
}
```

### 七、`std::map` 与 `std::unordered_map` 的区别

| 特性         | `std::map`    | `std::unordered_map` |
| ---------- | ------------- | -------------------- |
| 底层实现       | 红黑树（有序）       | 哈希表（无序）              |
| 排序         | 自动按 key 排序    | 无序                   |
| 时间复杂度（增删查） | O(log n)      | O (1)（平均），O (n)（最坏）  |
| 键的要求       | 需支持比较运算符（`<`） | 需支持哈希函数和 ==          |
| 迭代器类型      | 双向迭代器         | 前向迭代器                |
| 内存开销       | 较小（红黑树结构）     | 较大（哈希表的桶和链表）         |

**使用场景**：
- 需有序存储、范围查询（如 `lower_bound`）→ 用 `std::map`；
- 追求极致查询效率、无需排序 → 用 `std::unordered_map`。
