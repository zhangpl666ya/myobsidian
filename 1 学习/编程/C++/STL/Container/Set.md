# 是什么
包含在头文件set中
set类型本质是容器，由红黑树实现的自动排序容器，可指定类型和排序依据
存的数据不会重复，自动去重
对于int, double这种数据类型，由大到小排序
对于std::string，则是按字符串比较的方式进行
```cpp
#include<set>

std::set<int> a{1,2,5,4,2,3}//会自动排序+去重成1 2 3 4 5
```

# 内容
## 迭代器
==没有下标访问！==
红黑树不连续存储，不能用原生指针直接访问和修改
- iterator：可读写，不能修改
- const_iterator：只读
- reverse_iterator：反向遍历的双向迭代器，可以++/--

## 成员函数
### 1、insert 插入元素
`std::pair<iterator , bool>insert(const T& value)
#### 返回值：`std::pair`
包含两个部分：
- first：指向插入元素或已存在的重复元素的迭代器
- second：bool类型，表示插入成功与否，有重复返回false
```cpp
std::set<int> s;
auto ret - s.insert(5);
if(ret.second){
	std::cout<<"success"<<std::endl;
}
```
### 2、erase 删除元素
有三种重载：
#### 重载 1，按迭代器删除：
```cpp
void erase(iterator pos)
```
返回值：void（无）
#### 重载 2，按值删除：
```cpp
size_type erase(const T& value)
```
返回值：size_t，表示成功删除的元素个数（只有0和1）

#### 重载 3，按迭代器范围删除：
```cpp
void erase(iterator first, iterator last)
```
返回值：void

### find 查找元素
```cpp
iterator find(const T& value);
const_iterator find(const T& value) const
```

#### 返回值：
- 找到返回指向该元素的迭代器
- 没找到返回end（）

### lower_bound()/upper_bound：范围查找
- lower_bound(int value)：返回第一个**不小于**value的元素的迭代器
- upper_bound(int value)：返回第一个**大于**value的元素的迭代器
```cpp
std::set<int> s = {1,2,3,4,5};
auto lb = s.lower_bound(3); //指向3
auto ub = s.upper_bound(3); //指向4
```

