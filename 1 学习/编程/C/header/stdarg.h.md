# stdarg.h内容
`stdarg.h` 是 C 语言标准库中用于处理**可变参数函数**的头文件，核心作用是让函数能够接收数量和类型不固定的参数（如 `printf`、`scanf` 这类函数）。它通过一组宏来实现对可变参数的遍历和访问，底层依赖编译器的参数传递规则（通常是栈布局）。

#### 1. 核心宏定义

`stdarg.h` 提供了 4 个核心宏（C99 新增 `va_copy`，C89 仅前 3 个）：
  

|宏|作用|
|---|---|
|`va_list`|定义一个**可变参数列表类型**的变量，用于存储可变参数的 “指针”（实际是栈指针）|
|`va_start`|初始化 `va_list` 变量，使其指向第一个可变参数的起始位置|
|`va_arg`|从 `va_list` 中提取下一个参数，指定参数类型并返回对应值|
|`va_end`|清理 `va_list` 变量，释放相关资源（部分平台仅为宏占位，无实际操作）|
|`va_copy`|复制一个已初始化的 `va_list`（避免直接赋值导致的指针混乱）|

#### 2. 可变参数函数的编写规则
要使用 `stdarg.h`，函数必须满足**固定参数 + 可变参数**的结构：

- 固定参数至少有一个（用于定位可变参数的起始位置）；
- 函数声明时，可变参数用 `...` 表示（必须放在参数列表最后）。

#### 3. 基础使用示例（自定义可变参数求和函数）
要使用 `stdarg.h`，函数必须满足**固定参数 + 可变参数**的结构：

- 固定参数至少有一个（用于定位可变参数的起始位置）；
- 函数声明时，可变参数用 `...` 表示（必须放在参数列表最后）。

#### 3. 基础使用示例（自定义可变参数求和函数）
```c
#include <stdio.h>
#include <stdarg.h>

// 功能：计算 n 个整数的和（n 是固定参数，后续是可变参数）
int sum(int n, ...) {
    int total = 0;
    va_list ap;  // 1. 定义可变参数列表变量

    // 2. 初始化 ap：第一个参数是 ap，第二个是最后一个固定参数（n）
    va_start(ap, n);

    // 3. 遍历可变参数（共 n 个）
    for (int i = 0; i < n; i++) {
        // va_arg(ap, 类型)：提取下一个参数，类型必须匹配实际传入的类型
        total += va_arg(ap, int);
    }

    // 4. 清理 ap
    va_end(ap);

    return total;
}

int main() {
    // 调用：n=3，后续 3 个整数参数
    printf("sum(1,2,3) = %d\n", sum(3, 1, 2, 3));  // 输出 6
    // n=5，后续 5 个整数参数
    printf("sum(10,20,30,40,50) = %d\n", sum(5, 10,20,30,40,50));  // 输出 150
    return 0;
}
```
#### 4. 关键注意事项

- **类型匹配**：`va_arg` 指定的类型必须与实际传入的参数类型一致（如传入 `short` 会被提升为 `int`，需用 `va_arg(ap, int)` 提取）；
- **参数数量**：必须通过固定参数（如示例中的 `n`）明确可变参数的数量，否则会导致栈越界；
- **va_copy 的使用**：若需要多次遍历可变参数，需用 `va_copy` 复制 `va_list`，避免原指针被移动后无法复用：
- ```c
void print_twice(int n, ...) {
    va_list ap1, ap2;
    va_start(ap1, n);
    va_copy(ap2, ap1);  // 复制 ap1 到 ap2

    // 第一次遍历（ap1）
    for (int i=0; i<n; i++) printf("%d ", va_arg(ap1, int));
    printf("\n");

    // 第二次遍历（ap2）
    for (int i=0; i<n; i++) printf("%d ", va_arg(ap2, int));
    printf("\n");

    va_end(ap2);
    va_end(ap1);
}
```
# 标准库vprintf
>定义在stdio.h中

`vprintf` 是标准库中专门配合 `stdarg.h` 使用的格式化输出函数，核心作用是**接收可变参数列表（va_list）而非直接的可变参数**，常用于封装自定义的格式化输出函数。
```c
#include <stdio.h>
#include <stdarg.h>

int vprintf(const char *format, va_list ap);
```
- **参数**：
    - `format`：格式化字符串（与 `printf` 完全一致，如 `%d`、`%s`）；
    - `ap`：已初始化的 `va_list` 变量；
- **返回值**：成功输出的字符数，失败返回负数。

#### 2. 核心用途

当你需要封装一个自定义的格式化输出函数（比如 “带前缀的日志打印”），直接用 `printf` 无法接收 `va_list`，此时必须用 `vprintf`（或其变体：`vfprintf` 输出到文件、`vsprintf` 输出到字符串、`vsnprintf` 安全输出到字符串）。

#### 3. 基础使用示例（自定义日志函数）

需求：封装一个 `log_print` 函数，自动添加 `[LOG]` 前缀，支持格式化输出。
```c
#include <stdio.h>
#include <stdarg.h>

// 自定义日志函数：带 [LOG] 前缀的格式化输出
void log_print(const char *format, ...) {
    va_list ap;

    // 1. 初始化 va_list（最后一个固定参数是 format）
    va_start(ap, format);

    // 2. 先输出前缀
    printf("[LOG] ");

    // 3. 用 vprintf 处理可变参数列表
    vprintf(format, ap);

    // 4. 清理 va_list
    va_end(ap);
}

int main() {
    // 调用自定义日志函数（用法与 printf 完全一致）
    log_print("数值：%d，字符串：%s\n", 100, "hello");
    log_print("浮点数：%.2f\n", 3.1415);
    return 0;
}
//输出结果：
//[LOG] 数值：100，字符串：hello
//[LOG] 浮点数：3.14

```
#### 4. vprintf 变体函数

|函数|功能|适用场景|
|---|---|---|
|`vfprintf`|输出到指定文件流（FILE*）|日志写入文件|
|`vsprintf`|输出到字符数组（char*）|格式化拼接字符串（有溢出风险）|
|`vsnprintf`|输出到字符数组，指定最大长度|安全的字符串格式化（推荐）|

**示例：vsnprintf 安全拼接字符串**
```c
#include <stdio.h>
#include <stdarg.h>

// 安全格式化字符串（避免缓冲区溢出）
int safe_sprintf(char *buf, size_t buf_size, const char *format, ...) {
    va_list ap;
    va_start(ap, format);
    // vsnprintf：第三个参数指定缓冲区最大长度（含 '\0'）
    int len = vsnprintf(buf, buf_size, format, ap);
    va_end(ap);
    return len;
}

int main() {
    char buf[20];
    // 仅写入前 19 个字符 + '\0'
    safe_sprintf(buf, sizeof(buf), "数字：%d，文本：%s", 123, "这是一段很长的文本");
    printf("结果：%s\n", buf);  // 输出：结果：数字：123，文本：这是一段很长的文
    return 0;
}
```