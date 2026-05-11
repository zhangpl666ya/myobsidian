# 1️⃣首先抄上去的话

在你的CMakelists.txt中，有几句话先写上：
```cmake
cmake_minium_required(VERSION 3.20)
progect(工程名)
```
第一行告诉CMake用什么版本，直接抄

第二行进行初始化，程序会自动记录**项目名**，启用默认语言，创建这些隐式变量。

没有`project()`
- CMake会发出警告
- 某些命令行为不完整
- 语言不启用

# 2️⃣为我们的target添加属性！
## 可执行文件篇：
### `add_executable`

这个命令初始化定义一个target，属性为可执行文件，并初始化记录可执行文件的依赖项

```cmake
add_executable(hello ...)
# 给名为hello的target添加依赖的源文件
```

在CMake内部中：
- 绑定源文件
- 绑定including路径
- 绑定编译选项
- 绑定链接库

>“我要一个叫hello的最终产物，它的编译链接规则以后就这样”

编译过程中的.o被底层管理，不用操心

>[!warning]
>同一个target只能被add_executable**定义一次**！！

那我像继续添加依赖项呢？
### `target_sources`

不是重定义，而是修改（更准确的说是添加）属性

```cmake {4} 
add_executable(hello main.c)

target_sources(hello
	PRIVATE # 先不用管这个关键字
	add.c
)
```

这段代码意思是给hello添加add.c源文件依赖

## 库篇：
### `add_library`

>库（动/静）在CMake中和可执行文件有什么本质区别？

首先：**都是target**！

初始化一个target的时候，你希望它最后成为库，使用：

```cmake
add_library(math add.c)
# 创建了一个叫`math`的库target
```

这和签名的`add_executate`在对象模型层面是同一类东西

### `STATIC|SHARED`
配合前面的`add_library`，确定动/静库
```cmake
add_library(math STATIC add.c) # 静态库
add_library(math SHARED add.c) # 动态库
```

## target之间的依赖篇：
### `target_link_libraries`

```cmake
target_link_libraries(hello math)
# 可执行文件hello依赖于库math
```

声明target之间的依赖关系，库的路径已经在自己的属性中记录，可以自动追踪

### `PUBILC|PRIVATE|INTERFACE`

**先给一句“压缩结论”**

> **`PUBLIC / PRIVATE / INTERFACE` 决定的是：  
> 一个 target 的哪些属性，会不会“传递”给依赖它的 target**

📌 **不是权限**  
📌 **不是访问控制**  
📌 **是“属性传播规则”**

现在问三个问题：

1. `math` 自己编译时，用不用它的 include 路径？
    
2. `hello` 编译时，用不用 `math` 的 include 路径？
    
3. 别人依赖 `hello` 时，要不要再看到这些信息？
    

👉 **`PUBLIC / PRIVATE / INTERFACE` 就是回答这三个问题的**

#### 🔒 PRIVATE

> **只给我自己用，不往外传**

- `math` 自己用
    
- `hello` 看不到
    

---

#### 🌍 PUBLIC

> **我自己要用，依赖我的也要用**

- `math` 用
    
- `hello` 也用
    

---

#### 📡 INTERFACE

> **我自己不用，只给依赖我的人用**

- `math` 不用
    
- `hello` 用

# 3️⃣多目录工程target联动

```text
project/
├── CMakeLists.txt
├── app/
│   ├── CMakeLists.txt
│   └── main.c
└── math/
    ├── CMakeLists.txt
    ├── add.c
    └── add.h
```

## `add_subdirectory`
每个`CMaketext.txt`都管理自己的target，所以在主文件夹中的`CMaketext.txt`无法直接管理子文件夹中的target

所以需要在主文件夹的CMake中**引入**target：
当你在根目录中写：

```cmake
add_subdirectory(math)
add_subdirectory(app)
```

CMake实际做的是：
>执行`.../CMakelists.txt`，
>让里面自定义的target注册到“整个工程中”

# 4️⃣引入第三方库

## `find_package`

当你写：`find_package(ZLIB REQUIRED)`

现代 CMake 期望发生的是：

> **CMake 帮你“引入一些已经定义好的 target”**
### 什么是 IMPORTED target?

> **IMPORTED target =  
> “我不负责构建，但我知道它长什么样、怎么用”**

它内部记录了：

- `.a / .so` 在哪里
    
- include 路径
    
- 必须的编译选项
    
- 它依赖谁
    

📌 和你自己写的 target **用法完全一致**

