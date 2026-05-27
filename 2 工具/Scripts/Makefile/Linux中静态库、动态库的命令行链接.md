在 Linux 环境下，通过命令行手动配置 C++ 的库文件（静态库与动态库）是理解编译原理的基础。

为了方便演示，我们假设有以下文件结构：

- **`math.h`** / **`math.cpp`**: 库的源代码（实现一个加法函数）。
    
- **`main.cpp`**: 调用库函数的主程序。
    

---

## 1. 静态库 (.a) 的配置

静态库在编译时会被完整地复制到可执行文件中。

### 第一步：编译生成目标文件 (.o)

Bash

```
g++ -c math.cpp -o math.o
```

### 第二步：打包成静态库

使用 `ar` (archiver) 工具：

Bash

```
ar rcs libmymath.a math.o
```

> **注意**：库文件名必须以 `lib` 开头。

### 第三步：编译主程序并链接

Bash

```
g++ main.cpp -L. -lmymath -o main_static
```

- `-L.`：告诉编译器在当前目录查找库文件。
    
- `-lmymath`：链接名为 `libmymath.a` 的库（去掉 lib 前缀和后缀）。
    

---

## 2. 动态库 (.so) 的配置

动态库在运行时才被加载，文件体积小，且易于更新。

### 第一步：生成位置无关代码的目标文件

Bash

```
g++ -c -fPIC math.cpp -o math.o
```

- `-fPIC`：生成位置无关代码（Position Independent Code），这是动态库的要求。
    

### 第二步：生成动态库

Bash

```
g++ -shared -o libmymath.so math.o
```

### 第三步：编译并链接

Bash

```
g++ main.cpp -L. -lmymath -o main_dynamic
```

### 第四步：运行（关键点)
编译时硬编码：使用 `rpath` 

这是最省心的方法。在编译时就把库的路径“写死”在可执行文件中，这样程序移动到哪里都能运行（只要相对路径对）。

在 `g++` 命令或 `Makefile` 中添加 `-Wl,-rpath` 参数：

Bash

```
g++ main.cpp -L. -lmymath -Wl,-rpath='./' -o app
```

- `-Wl,`：表示后面的参数传递给链接器（linker）。
    
- `-rpath='./'`：指定程序运行时优先从当前目录寻找库。

---

## 3. 结合 Makefile 自动化

手动输入命令非常低效，`Make` 工具可以自动化这个过程。

### 编写 Makefile

创建一个名为 `Makefile` 的文件，内容如下：

Makefile

```
# 定义编译器和参数
CXX = g++
CXXFLAGS = -Wall -I.

# 目标文件名
STATIC_LIB = libmymath.a
DYNAMIC_LIB = libmymath.so
TARGET = app

# 默认构建动态库版本
all: $(TARGET)

# 1. 构建静态库
$(STATIC_LIB): math.cpp
	$(CXX) $(CXXFLAGS) -c math.cpp -o math.o
	ar rcs $(STATIC_LIB) math.o

# 2. 构建动态库
$(DYNAMIC_LIB): math.cpp
	$(CXX) $(CXXFLAGS) -fPIC -shared math.cpp -o $(DYNAMIC_LIB)

CXXFLAGS += -Wl -rpath='./lib'
# 3. 编译主程序 (链接动态库示例)
$(TARGET): main.cpp $(DYNAMIC_LIB)
	$(CXX) $(CXXFLAGS) main.cpp -L. -lmymath -o $(TARGET)

# 清理文件
clean:
	rm -f *.o *.a *.so $(TARGET)
```


---

## 总结与对比

|**特性**|**静态库 (.a)**|**动态库 (.so)**|
|---|---|---|
|**链接时间**|编译时|运行时|
|**文件大小**|可执行文件较大|可执行文件较小|
|**部署**|简单（只需一个可执行文件）|复杂（需带上 .so 文件）|
|**更新**|需重新编译整个项目|只需替换 .so 文件|
