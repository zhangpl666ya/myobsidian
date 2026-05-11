# std::variant：类型安全的 “多选一” 联合体

### 核心概念

`std::variant<T1, T2, ...Tn>` 是**类型安全的联合体（union）**，它可以存储指定类型列表中的**任意一种**类型的值（同一时刻只能存一种），且自动管理内存和类型信息，避免了原生 `union` 无法处理非 POD 类型（如 std::string）、类型不安全的问题。

可以理解成：“一个变量，只能是 A、B、C 类型中的一种，且知道自己当前是什么类型”。
#### 适用场景

- 处理多类型输入：比如配置项可能是 int、float、string；
- 替代不安全的原生 union：比如网络协议中的 “不同类型的数据包”；
- 状态机中的不同状态数据：比如 “成功返回 int、失败返回 string”。
#### 关键注意点

- `variant` 的类型列表中不能包含重复类型（比如 `variant<int, int>` 非法）；
- 用 `index()` 或 `std::holds_alternative<T>(var)` 判断当前类型；
- `std::get_if` 是安全取值方式，避免类型不匹配导致的异常。
### std::variant 的核心函数

`std::variant` 的函数围绕 “判断当前类型”“安全取值”“修改存储类型 / 值” 展开，核心函数如下：

|函数 / 操作符|功能说明|
|---|---|
|`index()`|成员函数，返回当前存储类型的索引（从 0 开始，对应声明时的类型列表顺序）|
|`emplace<T>(args...)`|成员函数，切换并构造指定类型的值（替代直接赋值）|
|`swap(variant& other)`|成员函数，交换两个 `variant` 的值和类型|
|`std::get<T>(variant& v)`|非成员函数，按**类型**取值；类型不匹配时抛 `std::bad_variant_access` 异常|
|`std::get<N>(variant& v)`|非成员函数，按**索引**取值（N 为类型列表的索引）；索引不匹配时抛异常|
|`std::get_if<T>(variant* v)`|非成员函数，按类型安全取值（返回指针，类型不匹配返回 `nullptr`）|
|`std::holds_alternative<T>(const variant& v)`|非成员函数，判断是否存储了指定类型的值（返回 bool）|
|`std::visit(callable, variant& v)`|非成员函数，访问 variant 的值（处理多类型分支的核心函数）|

#### 示例：核心函数使用
```cpp
#include <variant>
#include <string>
#include <iostream>

// 用于std::visit的回调函数
void print_variant(const auto& val) {
    std::cout << "当前值：" << val << std::endl;
}

int main() {
    std::variant<int, float, std::string> var = 3.14f;

    // index：获取当前类型索引（float是第1个，返回1）
    std::cout << "类型索引：" << var.index() << std::endl;

    // holds_alternative：判断类型
    if (std::holds_alternative<float>(var)) {
        // get<索引>：按索引取值
        std::cout << "float值：" << std::get<1>(var) << std::endl;
    }

    // emplace：切换类型并构造值
    var.emplace<std::string>("test");

    // get_if：安全取值（返回指针）
    if (auto* str_ptr = std::get_if<std::string>(&var)) {
        *str_ptr += " variant";
    }

    // visit：统一处理不同类型的值（无需手动判断类型）
    std::visit(print_variant, var); // 输出：当前值：test variant

    return 0;
}
```

### Visit函数
需要至少输入两个值，一个可调用对象（即访问器，包括lambda，函数，函数对象），至少一个variant类型。
会自动推导variant的具体类型，调用访问器相应逻辑

访问器必须包含处理variant所有类型的代码逻辑，不然会报错
访问器若有返回值，返回值类型必须统一

`std::visit` 没有运行时的 “类型判断开销”，核心原理是：

1. **编译期生成分发表**：编译器会根据 variant 的类型列表，为访问器生成对应每个类型的调用分支；
2. **运行时直接跳转**：运行时根据 variant 的 `index()`（当前类型索引），直接跳转到对应的分支执行，和手动写 `switch(index)` 效率一致；