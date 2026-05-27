C语言也可以有面向对象编程，核心是函数指针

# 结构体中函数指针赋值
类似C++，C语言用结构体封装函数指针，再对函数指针赋值，可实现面向对象编程风格的封装、回调函数、多态等特性

## 函数指针的定义
函数指针基本语法：
`返回值类型 （*指针名）（参数列表）`
将其嵌入结构体即可
```c
#include <stdio.h>
#include <string.h>

// 第一步：定义函数指针类型（可选，但能简化代码）
typedef int (*CalcFunc)(int, int);  // 指向“接收两个int、返回int”的函数的指针类型

// 第二步：定义包含函数指针的结构体
typedef struct {
    char name[20];
    CalcFunc calc;  // 结构体成员：函数指针
} Calculator;

// 定义匹配函数指针的普通函数
int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}
```
##  函数指针的赋值方式

结构体中函数指针的赋值有**直接赋值**和**初始化赋值**两种核心方式：

### 方式 1：初始化时赋值
```c
// 结构体初始化时直接绑定函数
Calculator cal1 = {
    .name = "加法器",
    .calc = add  // 直接赋值函数名（函数名本质是函数首地址）
};

Calculator cal2 = {
    .name = "减法器",
    .calc = sub
};
```
### 方式 2：运行时动态赋值（灵活，支持回调 / 切换行为）
```c
Calculator cal3;
strcpy(cal3.name, "动态赋值加法器");
cal3.calc = add;  // 运行时修改函数指针指向

// 甚至可以动态切换
cal3.calc = sub;  // 从加法切换为减法
```
##  调用结构体中的函数指针

通过结构体变量 / 指针访问函数指针，语法为 `结构体.函数指针(参数)` 或 `结构体指针->函数指针(参数)`：
```c
int main() {
    // 直接调用
    printf("%s: 3+5=%d\n", cal1.name, cal1.calc(3, 5));  // 加法器：3+5=8
    printf("%s: 3-5=%d\n", cal2.name, cal2.calc(3, 5));  // 减法器：3-5=-2

    // 结构体指针调用
    Calculator *p = &cal3;
    p->calc = add;
    printf("%s: 10+20=%d\n", p->name, p->calc(10, 20));  // 动态赋值加法器：10+20=30

    return 0;
}
```