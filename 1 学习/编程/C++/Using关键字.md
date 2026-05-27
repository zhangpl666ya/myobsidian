在 C++ 中，`using` 关键字是一个多功能的语法元素，核心作用是**引入命名空间 / 名称、定义类型别名、继承基类成员**，不同场景下的用法和语义差异较大。下面按使用场景逐一拆解，结合示例说明：

### 一、核心场景 1：引入命名空间 / 名称（解决命名冲突 / 简化代码）

这是最常用的场景，用于将命名空间中的名称（类型、函数、变量等）引入当前作用域，避免每次都写完整的命名空间前缀。

#### 1.1 引入整个命名空间（全局 / 局部）

语法：`using namespace 命名空间名;`

- 全局作用域：在文件顶部引入，整个文件都能直接使用该命名空间的内容；
- 局部作用域：在函数 / 代码块内引入，仅在该作用域生效（推荐，避免全局污染）。

```cpp
#include <iostream>
// 全局引入std命名空间（简单程序常用，但大型项目不推荐）
using namespace std;

int main() {
    // 无需写std::cout，直接用cout
    cout << "Hello World" << endl; 
    return 0;
}
```

#### 1.2 引入命名空间中的单个名称

语法：`using 命名空间名::名称;`

仅引入指定名称，避免引入整个命名空间导致的命名冲突（大型项目推荐）。

示例：

```cpp
#include <iostream>

// 仅引入std::cout和std::endl，其他仍需加std::
using std::cout;
using std::endl;

int main() {
    cout << "Only cout/endl are imported" << endl;
    // std::cin未引入，必须加前缀
    int a;
    std::cin >> a; 
    return 0;
}
```

#### 1.3 注意事项

- 避免在头文件中全局引入 `using namespace std;`：头文件会被其他文件包含，可能导致全局命名污染，引发命名冲突；
- 局部引入优先：仅在需要的函数 / 代码块内引入，缩小作用域。

### 二、核心场景 2：定义类型别名（替代 typedef，更直观）

C++11 起，`using` 可以替代 `typedef` 定义类型别名，语法更清晰，尤其适合复杂类型（如函数指针、模板别名）。

#### 2.1 基础类型别名（与 typedef 等价）

语法：`using 别名 = 原类型;`

```cpp
// typedef写法
typedef int MyInt;
// using写法（更直观，语义是“别名 = 原类型”）
using MyInt = int;

// 指针/引用类型
typedef int* IntPtr;
using IntPtr = int*;

int main() {
    MyInt a = 10;
    IntPtr p = &a;
    return 0;
}
```
#### 2.2 模板别名（typedef 无法实现）

`typedef` 不支持模板别名，而 `using` 可以直接定义模板化的类型别名，这是核心优势。

示例：

```cpp
#include <vector>

// 定义模板别名：Vec<T> 等价于 std::vector<T>
template <typename T>
using Vec = std::vector<T>;

int main() {
    // 简化复杂模板类型的书写
    Vec<int> nums = {1,2,3}; 
    Vec<std::string> strs = {"a", "b"};
    return 0;
}
```
#### 2.3 函数指针别名（更易读）
```cpp
// typedef写法（易混淆）
typedef void (*FuncPtr)(int);
// using写法（清晰）
using FuncPtr = void (*)(int);

void print(int a) {
    std::cout << a << std::endl;
}

int main() {
    FuncPtr f = print;
    f(10); // 输出10
    return 0;
}
```
### 三、核心场景 3：继承中引入基类成员（解决隐藏问题）

当子类继承基类后，如果重定义了基类的同名成员（如函数），基类的其他重载版本会被 “隐藏”。使用 `using 基类名::成员名;` 可以将基类的成员引入子类作用域，恢复访问。

#### 3.1 恢复基类重载函数的访问
```cpp
#include <iostream>
using namespace std;

class Base {
public:
    void func(int a) { cout << "Base::func(int): " << a << endl; }
    void func(double a) { cout << "Base::func(double): " << a << endl; }
};

class Derived : public Base {
public:
    // 子类重定义func，隐藏基类的所有func重载
    void func(string a) { cout << "Derived::func(string): " << a << endl; }
    
    // 引入基类的func，恢复所有重载版本的访问
    using Base::func;
};

int main() {
    Derived d;
    d.func(10);       // 调用Base::func(int)
    d.func(3.14);     // 调用Base::func(double)
    d.func("hello");  // 调用Derived::func(string)
    return 0;
}

```

#### 3.2 引入基类的成员变量
```cpp
class Base {
protected:
    int num = 100;
};

class Derived : public Base {
public:
    // 引入基类的num，将protected改为public（仅在子类作用域生效）
    using Base::num;
};

int main() {
    Derived d;
    cout << d.num << endl; // 输出100，可直接访问
    return 0;
}
```

### 四、C++17 扩展：using 声明的聚合体初始化

C++17 允许在聚合体（如结构体）中使用 `using` 继承基类的成员，同时支持聚合初始化：
```cpp
struct Base { int a; };
struct Derived : Base {
    using Base::a;
    int b;
};

// C++17 支持
Derived d = {10, 20};
cout << d.a << ", " << d.b << endl; // 输出10, 20
```

### 五、常见误区总结

1. **混淆 using namespace 和 using 声明**：
    - `using namespace std;` 是 “指令”，引入整个命名空间；
    - `using std::cout;` 是 “声明”，仅引入单个名称，更安全。
2. **头文件中避免全局 using**：会导致命名污染，推荐仅在.cpp 文件中局部使用；
3. **模板别名 vs typedef**：`typedef` 是 “类型重命名”，`using` 是 “别名声明”，后者支持模板，语法更清晰；
4. **继承中 using 的作用域**：`using 基类::成员` 仅影响当前子类，不会修改基类的访问权限（如基类 protected 成员引入子类后，访问权限由子类的继承方式决定）。