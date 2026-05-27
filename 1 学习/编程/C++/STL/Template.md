模板是 C++ **泛型编程（Generic Programming）** 的核心基石，其本质是「编译器的代码生成规则」—— 通过将类型 / 数值抽象为参数，让代码与具体类型解耦，实现**类型无关的通用代码复用**。模板解决了传统 “重复写相似代码（如针对 int/string 分别写排序函数）” 的问题，同时保证类型安全（区别于宏的文本替换），是 STL（如 `std::vector`、`std::sort`）的实现基础。

# 模板的作用和价值
### 1. 泛型编程的核心思想

泛型编程的目标是：**让算法 / 数据结构独立于具体类型**，比如一个排序算法既能排序 `int`，也能排序 `string` 或自定义结构体，无需为每种类型重写逻辑。模板是实现这一目标的核心工具。
### 2. 模板的本质

模板不是可执行代码，而是**编译器生成代码的 “蓝图”**：

- 编写模板时，你定义的是 “规则”（比如 “一个能存任意类型的容器”）；
- 当你用具体类型 / 数值实例化模板时（如 `vector<int>`），编译器会根据模板规则，生成针对该类型的具体代码（“模板实例化”）；
- 模板的类型检查发生在**实例化阶段**（而非定义阶段），这是模板最易踩坑的点。

### 3. 模板的分类
C++ 模板主要分三类（按 C++ 标准演进）：

|模板类型|引入标准|核心用途|示例|
|---|---|---|---|
|函数模板|C++98|通用函数（如通用 swap、排序）|`template<typename T> void swap(T&, T&);`|
|类模板|C++98|通用数据结构（如 vector、map）|`template<typename T> class Vector;`|
|变量模板|C++14|通用常量 / 变量（如通用 π 值）|`template<typename T> constexpr T pi = T(3.14);`|

此外还有进阶的「模板模板参数」「可变参数模板」等特性，属于上述基础类型的扩展。

## 函数模板

函数模板是 “能处理不同类型参数的通用函数”，语法上通过 `template` 关键字声明模板参数，再在函数中使用该参数。
### 1. 基本语法
```cpp
// 模板参数声明：template <模板参数列表>
// 模板参数：typename/class 表示类型参数，也可写非类型参数
template <typename T>  // typename 等价于 class（C++ 早期只用 class，typename 是后来补充的）
T max(T a, T b) {      // T 是类型参数，代表任意类型
    return a > b ? a : b;
}
```
- `template <>`：模板参数列表的固定前缀，必须放在函数 / 类定义前；
- `typename T`：声明一个名为 `T` 的**类型参数**（可理解为 “类型占位符”），实例化时会被具体类型（如 `int`、`string`）替换；
- 函数参数 / 返回值中使用 `T`：表示该位置的类型由实例化时的参数决定。
### 2. 模板实例化（编译器生成具体函数）

函数模板不会直接编译成机器码，只有 “实例化” 后才会生成针对具体类型的函数。实例化分两种：
#### （1）隐式实例化（编译器自动推导）

调用函数时，编译器根据传入的参数类型，自动推导模板参数 `T` 的类型，并生成对应代码：
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 隐式推导 T 为 int，生成 int max(int, int)
    cout << max(1, 2) << endl; 

    // 隐式推导 T 为 string，生成 string max(string, string)
    cout << max(string("apple"), string("banana")) << endl; 

    return 0;
}
```

#### （2）显式实例化（手动指定类型）

当编译器无法推导类型（如函数无参数），或需要强制生成特定类型的函数时，手动指定模板参数：
```cpp
// 显式实例化：强制生成 T=double 的 max 函数
template double max<double>(double a, double b);

// 调用时显式指定类型（即使能推导，也可手动指定）
cout << max<double>(3.14, 2.71) << endl;
```

### 3. 模板参数的分类

函数模板的参数分两类：**类型参数** 和 **非类型参数**：

#### （1）类型参数（最常用）

用 `typename/class` 声明，代表 “任意类型”（int、string、自定义结构体等）：
```cpp
// T 是类型参数，代表任意类型
template <typename T>
void swap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}
```
#### （2）非类型参数（数值参数）

用具体类型（如 int、size_t、指针）声明，代表 “常量数值”（实例化时必须传入常量表达式）：
```cpp
// N 是非类型参数（整型常量），代表数组大小
template <int N>
void print_array(int (&arr)[N]) {  // 接收大小为 N 的 int 数组
    for (int i = 0; i < N; ++i) {
        cout << arr[i] << " ";
    }
}

int main() {
    int arr[5] = {1,2,3,4,5};
    print_array(arr); // 隐式推导 N=5，生成 print_array<5>
    return 0;
}
```
##### 非类型参数的限制：

- C++11 及之前：仅支持 **整型 / 枚举类型、指针 / 引用（指向静态存储期对象）、std::nullptr_t**；
- C++17：支持 `auto` 推导非类型参数类型；
- C++20：支持更多类型（如浮点数、字符串字面量，但不同编译器支持度不同）；
- 实例化时必须传入 **常量表达式**（不能是运行时变量）：
```cpp
int n = 5;
// 错误：n 是运行时变量，非类型参数必须是常量表达式
// print_array<n>(arr); 

const int m = 5;
print_array<m>(arr); // 正确：m 是常量表达式
```
### 4. 函数模板的重载与特化
#### （1）函数模板的重载

函数模板可与普通函数、其他模板重载，编译器按「更具体者优先」的规则匹配：
```cpp
// 模板1：通用 max
template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}

// 模板2：重载（支持三个参数）
template <typename T>
T max(T a, T b, T c) {
    return max(max(a, b), c);
}

// 普通函数：重载（针对 const char* 优化）
const char* max(const char* a, const char* b) {
    return strcmp(a, b) > 0 ? a : b;
}

int main() {
    max(1,2);          // 匹配模板1
    max(1,2,3);        // 匹配模板2
    max("apple", "banana"); // 匹配普通函数（更具体）
    return 0;
}
```
#### （2）函数模板的特化（针对特定类型定制实现）

当通用模板对某类类型不适用时，为该类型定制 “特化版本”（全特化，无偏特化）：
```cpp
// 通用模板
template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}

// 对 const char* 的全特化（定制字符串比较逻辑）
template <>
const char* max<const char*>(const char* a, const char* b) {
    return strcmp(a, b) > 0 ? a : b;
}

int main() {
    max("apple", "banana"); // 调用特化版本
    return 0;
}
```
### 5. 函数模板的注意点

- **分离编译问题**：模板的定义（实现）必须在实例化的可见范围内（通常放在头文件），不能像普通函数那样 “声明放头文件，实现放源文件”（除非显式实例化）。原因：编译器实例化时需要看到完整的模板定义；
- **类型推导规则**：编译器仅根据函数参数推导模板参数，返回值不参与推导；
- **隐式类型转换**：隐式实例化时，参数类型必须**完全匹配**（普通函数支持隐式转换，模板不支持）：

```cpp
max(1, 2.0); // 错误：参数类型 int 和 double 不匹配，无法推导 T
max<double>(1, 2.0); // 正确：显式指定 T=double，1 隐式转换为 double
```

## 类模板

类模板是 “能处理不同类型的通用类”，语法与函数模板类似，但实例化规则更严格，支持偏特化。
### 1. 基本语法
```cpp
// 模板参数声明：template <模板参数列表>
template <typename T>
class Vector { // Vector 是类模板名，Vector<T> 是具体类型
private:
    T* data;    // 用类型参数 T 定义成员变量
    size_t size;
public:
    // 构造函数：使用 T
    Vector(size_t n, const T& val) : size(n) {
        data = new T[n];
        for (size_t i = 0; i < n; ++i) {
            data[i] = val;
        }
    }

    // 成员函数：返回值/参数用 T
    T& operator[](size_t idx) {
        return data[idx];
    }

    ~Vector() {
        delete[] data;
    }
};
```

### 2. 类模板的实例化

类模板必须**显式实例化**（编译器无法推导类型），实例化时在类模板名后指定模板参数：
```cpp
int main() {
    // 实例化：T=int，生成 Vector<int> 类
    Vector<int> v1(5, 10); 
    cout << v1[0] << endl; // 10

    // 实例化：T=string，生成 Vector<string> 类
    Vector<string> v2(3, "hello");
    cout << v2[1] << endl; // hello

    return 0;
}
```
- `Vector` 是类模板名，不是具体类型；`Vector<int>`、`Vector<string>` 是不同的具体类型；
- 类模板的成员函数只有在**被调用时**才会实例化（未调用的成员函数不会生成代码）。
### 3. 类模板的模板参数

类模板支持 **类型参数、非类型参数、默认模板参数**：

#### （1）默认模板参数（C++11 后支持）

为模板参数指定默认值，实例化时可省略该参数：
```cpp
// 为 Alloc 指定默认值 std::allocator<T>（STL 容器的常用写法）
template <typename T, typename Alloc = std::allocator<T>>
class Vector {
    // ...
};

// 实例化：省略 Alloc，使用默认值 std::allocator<int>
Vector<int> v;
```
#### （2）非类型参数（通用固定大小容器）
```cpp
// T：类型参数，Size：非类型参数（数组大小）
template <typename T, size_t Size>
class Array {
private:
    T data[Size];
public:
    T& operator[](size_t idx) {
        return data[idx];
    }
};

int main() {
    // 实例化：T=int，Size=5
    Array<int, 5> arr;
    arr[0] = 1;
    return 0;
}
```
### 4. 类模板的特化

类模板支持 **全特化** 和 **偏特化**（部分模板参数指定具体类型），这是实现 “类型定制” 的核心方式。
#### （1）全特化（针对所有模板参数定制）

为所有模板参数指定具体类型，完全替换通用模板：
```cpp
// 通用类模板
template <typename T>
class MyClass {
public:
    void print() {
        cout << "通用类型：" << typeid(T).name() << endl;
    }
};

// 全特化：T=bool（定制 bool 类型的实现）
template <>
class MyClass<bool> {
public:
    void print() {
        cout << "特化类型：bool" << endl;
    }
};

int main() {
    MyClass<int> m1;
    m1.print(); // 输出：通用类型：int

    MyClass<bool> m2;
    m2.print(); // 输出：特化类型：bool
    return 0;
}
```
#### （2）偏特化（针对部分模板参数定制）

仅指定部分模板参数，或对参数做 “类型限制”（如指针、引用）：
```cpp
// 通用模板：两个类型参数
template <typename T, typename U>
class MyClass {
public:
    void print() { cout << "通用：T=" << typeid(T).name() << ", U=" << typeid(U).name() << endl; }
};

// 偏特化1：第二个参数固定为 int
template <typename T>
class MyClass<T, int> {
public:
    void print() { cout << "偏特化：T=" << typeid(T).name() << ", U=int" << endl; }
};

// 偏特化2：第一个参数为指针类型
template <typename T, typename U>
class MyClass<T*, U> {
public:
    void print() { cout << "偏特化：T=指针, U=" << typeid(U).name() << endl; }
};

int main() {
    MyClass<string, double> m1; // 通用版本
    m1.print(); // 通用：T=string, U=double

    MyClass<string, int> m2;    // 偏特化1
    m2.print(); // 偏特化：T=string, U=int

    MyClass<int*, double> m3;   // 偏特化2
    m3.print(); // 偏特化：T=指针, U=double
    return 0;
}
```
### 5. 类模板的成员模板

类（无论是否是模板）的成员函数可以是模板（称为 “成员模板”），用于实现更灵活的类型适配：
```cpp
template <typename T>
class Pair {
private:
    T first;
    T second;
public:
    Pair(T a, T b) : first(a), second(b) {}

    // 成员模板：转换构造函数（支持不同类型的 Pair 转换）
    template <typename U>
    Pair(const Pair<U>& other) : first(other.first), second(other.second) {
        // U 可隐式转换为 T 时生效
    }

    void print() {
        cout << first << ", " << second << endl;
    }
};

int main() {
    Pair<int> p1(1, 2);
    // 成员模板：Pair<int> 转换为 Pair<double>
    Pair<double> p2 = p1;
    p2.print(); // 1, 2
    return 0;
}
```
## 五、模板进阶特性

### 1. 模板模板参数（模板的参数是模板）

模板参数本身是另一个模板（而非类型 / 数值），用于实现 “容器的容器” 等通用逻辑
```cpp
// 模板模板参数：Container 是一个类模板（接收一个类型参数）
template <template <typename> class Container, typename T>
class Wrapper {
private:
    Container<T> c; // 用模板模板参数实例化容器
public:
    void add(const T& val) {
        c.push_back(val); // 假设 Container 有 push_back 方法
    }

    void print() {
        for (const auto& v : c) {
            cout << v << " ";
        }
    }
};

int main() {
    // 实例化：Container=vector，T=int → Wrapper<vector, int>
    Wrapper<vector, int> w;
    w.add(1);
    w.add(2);
    w.print(); // 1 2
    return 0;
}
```

C++14的东西**谁爱研究谁研究去**