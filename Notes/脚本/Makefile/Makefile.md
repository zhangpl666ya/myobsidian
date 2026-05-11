Makefile是一个脚本工具，makefile makes your life easier
# 基本格式
## 目标是文件名
Makefile第一个字母大写，其余小写，编辑器才能识别出来
Makefile的基本格式如下：
```explain
目标：依赖项
	命令
```
其中，目标是要生成的文件名，依赖项是指生成这个文件名所需要的源头文件，命令是生成这个文件所需的命令。执行时，在终端输入：`make 目标`即可执行

命令前一定是一个TAB键，不能用空格代替，Makefile对格式有非常严格的要求

生成文件时，make会检查目标和依赖项的时间戳，若上一次生成后有时间戳的更新或没有这个文件，就会再次生成；若文件存在且时间戳没有更新就不会再次编译文件

## .PHONY
然而有时候你的一个命令的目标会与某些文件冲突，可以不用管那么多，只要记住：
如果你写的是行为而不是文件，就将他加入到.PHONY中去
```Makefile
.PHONY: clean
clean:
	rm * .o app
```
# 定义变量
## 宏变量
Makefile中反复输入同一个字符串，若后期修改起来非常麻烦，这时引入变量（理解为宏更好）顶替复杂的一大串，最后用$将内容展开，这只是简单的字符串替换：
```Makefile
CXX = g++
CXXFLAGS = -std=c++20 -Wall

app: main.o add.o
	$(CXX) main.o add.o -o app #简单的字符串替换
main.o: main.cpp add.h
	$(CXX) $(CXXFLAGS) -c main.cpp add.h -o main.o  
#等价于g++ -std=c++20 -Wall -c main.cpp add.h -o main.o

```
## 活动变量
虽然有简化，但单个命令写起来依然麻烦
还有一种make提供的变量， 只在单个命令环境中生效
- $@ : 代表目标
- $< : 代表第一个依赖项
- $^ : 代表所有依赖项
```Makefile
main.o : main.cpp add.h
	$(CXX) $(CXXFLAGS) -c $^ -o $@
#等价于上面那个式子
```

对于main.o有一个命令， 那么对于别的也会有极其相似的命令，又是重复工作
引入%占位符，极大简化内容
```Makefile
%.o : %.cpp add.h
	$(CXX) $(CXXFLAGS) -c $^ -o $@
```
这样，输入任意.o命令就会自动配对

# 自动匹配依赖项

当然这还是有问题，不同cpp文件肯定有不同的头文件，那么这样就不好处理了
自动匹配依赖项功能解决这个问题，会自动识别cpp文件中包含了哪些头文件（系统提供的头文件除外），然后自动依赖。
这就是-MMD 、-MP 、-include 的功能了：
- -MMD是编译选项，可以同时生成后缀为.d的文件，记录该文件有哪些依赖项
- -MP是编译选项，防止如果依赖项被删报错问题，它告诉make如果在文件夹中没找到这个依赖项，将它视为空即可
- 在Makefile最后写一行-include : * .h ，告诉make哪些.h文件要考虑(* 表示任意)
```Makefile
CXXFLAGS += -MMD -MP
%.o : %.cpp add.h
	$(CXX) $(CXXFLAGS) -c $^ -o $@
	
-include : * .d
```

# 多文件夹工作

为了管理简便，一般用src文件夹存放源文件，用build文件夹存放.o 和 .h 文件 ，用lib存放库
project结构如下：
```explain
project
	|Makefile
	|src ：储存源文件
	|build/release（debug）：储存.o文件和.d文件
	|lib :储存库

```
所以在写的时候记得把文件名前面加路径，不然系统找不到的
```Makefile
SRC_DIR = src
BUILD_DIR = build/release

SRC = $(SRC_DIR)/*.cpp
OBJ = $(SRC:$(SRC_DIR)/%.cpp = $(BUILD_DIR)/%.o)

app: $(OBJ)
	$(CXX) $(CXXFLAGS) $^ -o %@

$(BUILD_DIR)/%.o : $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o %@
```
