# std::optional：“可有可无” 的单类型值
#### 核心概念

`std::optional<T>` 是一个**类型安全的 “可选值容器”**，它要么存储一个有效的 `T` 类型值，要么是空（表示值不存在）。可以把它理解成：“一个变量，可能有值，也可能没值”，替代了传统用 `NULL`、`-1` 等 “魔法值” 表示 “无值” 的不优雅方式。
#### 适用场景

- 函数返回值：比如查找元素时，找到则返回值，没找到则返回空（而非返回错误码）；
- 类的可选成员：比如用户信息中的 “可选手机号”；
- 可选参数：避免传递无效的默认值。

#### 关键注意点

- 用 `has_value()` 检查是否有值，避免直接 `value()` 导致异常；
- `value_or(默认值)` 是更安全的取值方式，无值时返回默认值；
- 底层是值语义，存储的是 `T` 的拷贝（也可存储引用：`std::optional<T&>`）。

`std::optional` 的函数围绕 “检查值是否存在”“取值”“修改 / 清空值” 展开，核心函数如下：

|函数 / 操作符|功能说明|
|---|---|
|`has_value()`|成员函数，返回 `bool`，判断是否存储了有效值（非空）|
|`value()`|成员函数，取出存储的值；无值时抛 `std::bad_optional_access` 异常|
|`value_or(T def)`|成员函数，有值则返回存储值，无值则返回默认值 `def`（最安全的取值方式）|
|`reset()`|成员函数，清空存储的值，使 `has_value()` 返回 `false`|
|`emplace(args...)`|成员函数，直接在 `optional` 内部构造值（避免拷贝，替代直接赋值）|
|`operator*`/`operator->`|重载操作符，直接取值（需先确认 `has_value()` 为 `true`，否则行为未定义）|
|`std::make_optional<T>(args...)`|非成员函数，创建 `optional` 对象（推荐，替代直接构造）|
|`std::nullopt`|空值常量，用于表示 `optional` 无值（如返回 `std::nullopt`）|

#### 示例：核心函数使用

```cpp
#include <optional>
#include <string>

int main() {
    std::optional<std::string> opt;
    
    // emplace：直接构造值，避免拷贝
    opt.emplace("hello");
    
    // has_value：检查是否有值
    if (opt.has_value()) {
        // operator*：直接取值
        *opt += " world";
        // value_or：安全取值（这里有值，返回存储值）
        auto val = opt.value_or("empty"); // val = "hello world"
    }

    // reset：清空值
    opt.reset();
    // value_or：无值时返回默认值
    auto val2 = opt.value_or("empty"); // val2 = "empty"

    // make_optional：创建optional
    auto opt2 = std::make_optional<int>(42);

    return 0;
}
```