> [!remind]
> 相信我，你不会使用它的


# std::any：“万能” 的单值容器

#### 核心概念

`std::any` 是**类型安全的 “任意类型” 容器**，它可以存储**任意类型**的单个值（不受类型列表限制），在运行时保存值的类型信息，通过 `std::any_cast` 取值。

可以理解成：“一个变量，能装任何类型的值，但同一时刻只能装一个”。它的灵活性最高，但开销也最大（因为需要存储类型信息和动态内存分配）。

#### 适用场景

- 动态类型场景：比如脚本绑定、通用的配置存储、第三方库的回调参数；
- 容器中存储任意类型：比如 `std::vector<std::any>` 存储不同类型的数据；
- 注意：尽量少用，因为丢失了编译期类型检查，容易出错。

#### 关键注意点

- `std::any` 不支持直接修改内部值，需先 `any_cast` 取出再修改；
- 存储的类型必须是可拷贝的（或用 `std::any::emplace` 构造）；
- 性能开销比 `optional`/`variant` 大，优先用前两者，仅在 “完全不确定类型” 时用 `any`。

### 函数
`std::any` 的函数围绕 “检查是否有值”“判断类型”“安全取值” 展开，核心函数如下：

|函数 / 操作符|功能说明|
|---|---|
|`has_value()`|成员函数，返回 `bool`，判断是否存储了值（非空）|
|`type()`|成员函数，返回 `std::type_info` 对象，获取当前存储值的类型（配合 `typeid` 使用）|
|`reset()`|成员函数，清空存储的值，释放内存|
|`emplace<T>(args...)`|成员函数，替换为指定类型的值（直接构造，避免拷贝）|
|`std::any_cast<T>(any& a)`|非成员函数，按类型取值；类型不匹配时抛 `std::bad_any_cast` 异常|
|`std::any_cast<T*>(any* a)`|非成员函数，安全取值（返回指针，类型不匹配返回 `nullptr`）|

#### 示例：核心函数使用
```cpp
#include <any>
#include <string>
#include <iostream>

int main() {
    std::any a;

    // emplace：构造值
    a.emplace<int>(42);

    // has_value：检查是否有值
    if (a.has_value()) {
        // type：判断类型
        if (a.type() == typeid(int)) {
            // any_cast：取值
            std::cout << "int值：" << std::any_cast<int>(a) << std::endl;
        }
    }

    // 切换类型
    a.emplace<std::string>("hello any");

    // any_cast<指针>：安全取值
    auto* str_ptr = std::any_cast<std::string>(&a);
    if (str_ptr) {
        std::cout << "string值：" << *str_ptr << std::endl;
    }

    // reset：清空值
    a.reset();
    std::cout << "是否有值：" << std::boolalpha << a.has_value() << std::endl;

    return 0;
}
```