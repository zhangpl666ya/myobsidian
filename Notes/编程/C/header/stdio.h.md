
# stdio.h：文件操作
## 特殊文件
三个默认打开的文件流
* `stdin`：标准输入，从键盘读取数据
* `stdout`：标准输出，写数据到屏幕
* `stderr`：标准错误，也是屏幕但专门用来输出错误信息

---

## 文件管理：打开、关闭和删改文件
1. `fopen`：打开文件
	* 功能：打开文件，返回一个FILE* 指针，后续对该文件操作依靠该指针
	* `FILE* fp = fopen(const char* filename,const char* mode)
	* 打开模式：“a”追加、“w“写入（清空所有内容）、”r“只读、带+则可读可写
	* 成功返回指向FILE的指针，失败返回NULL，同时设置errno
2. `fclose`：关闭文件
	* 用完文件后一定要关，不然会丢失数据
	* `FILE* fclose(FILE* stream)`
	* 成功返回0；失败EOF，并设置errno
3. `freopen`：重定向文件流
	* 功能：关闭`stream`原有文件，打开`filename`并重新关联到`stream`
	* `FILE* freopen(const char* filename, const char* mode,FILE* stream)`
	* 成功返原指针；失败返回NULL，设置errno
	* 先调用fclose关闭原有文件，再以mode打开filename，将新文件的FILE信息覆盖到stream指向的结构体
4. `remove`：删除文件
	* 功能：直接删掉文件
	* `int remove(const char* filename)`
5. `rename`：重命名/移动文件
	* 给文件改名，或者挪到别的文件夹
	* `int rename(const char* old, const char* new)`

---

## 格式化输入输出
### 标准I/O函数
#### 整行输入：`fgets`

- **功能**：从键盘（或文件）读取整行数据（包括空格和换行符），安全无溢出。
- **原型**：`char *fgets(char *str, int size, FILE *stream);`
- **参数**：
    - `str`：存储输入的字符数组；
    - `size`：数组最大长度（实际读取 `size-1` 个字符，留 1 位存字符串结束符 `\0`）；
    - `stream`：输入流（控制台输入用 `stdin`）。
- **返回值**：成功返回 `str` 指针（失败 / 读到文件尾返回 `NULL`）。
```c
char str[50];
printf("输入一句话（可含空格）：");
fgets(str, sizeof(str), stdin);  // 输入：I love C → 读取完整句子
str[strcspn(str, "\n")] = '\0';  // 去除换行符（关键！）
printf("你输入的是：%s\n", str);
```

#### 整行输出：`fputs`

- **功能**：向控制台（或文件）输出字符串（不含自动换行，需手动加 `\n`）。
- **原型**：`int fputs(const char *str, FILE *stream);`
- **参数**：
    - `str`：要输出的字符串；
    - `stream`：输出流（控制台输出用 `stdout`）。
- **返回值**：成功返回非负数（失败返回 `EOF`）。
```c
fputs("Hello World", stdout);  // 输出：Hello World（无换行）
fputs("Hello\n", stdout);      // 输出：Hello（带换行）
```

### 文件I/O函数
#### 文件格式化读写：`fprintf`/`fscanf`

- **功能**：与 `printf`/`scanf` 用法一致，只是读写对象是文件（而非控制台）。
- **原型**：
```c
int fprintf(FILE *stream, const char *format, ...);  // 写文件
int fscanf(FILE *stream, const char *format, ...);   // 读文件
```

#### 文件行读写：`fgets`/`fputs`（复用控制台函数）

- **功能**：与控制台 `fgets`/`fputs` 用法一致，仅需将 `stdin`/`stdout` 替换为文件指针。
- **示例**：读取文件的每一行并打印：
```c
FILE *fp = fopen("test.txt", "r");
if (fp == NULL) { /* 错误处理 */ }

char buf[1024];
// 逐行读取文件（buf 存储一行内容）
while (fgets(buf, sizeof(buf), fp) != NULL) {
    fputs(buf, stdout);  // 打印到控制台
}

fclose(fp);
```
#### 文件二进制读写（效率最好）
##### 1. `fwrite`：把内存数据写入文件
```c
size_t fwrite(
    const void *ptr,    // 要写入的内存数据的地址（比如结构体/数组的首地址）
    size_t size,        // 单个数据的字节大小（比如 sizeof(struct Project)）
    size_t count,       // 要写入的数据个数（比如有5个Project，count=5）
    FILE *stream        // 文件指针（打开的文件）
);
```
- 返回值：实际成功写入的**数据个数**（不是字节数）；如果失败，返回值小于 `count`。
##### 2. `fread`：从文件读取数据到内存
```c
size_t fread(
    void *ptr,          // 接收数据的内存地址（比如结构体数组的首地址）
    size_t size,        // 单个数据的字节大小
    size_t count,       // 要读取的数据个数
    FILE *stream        // 文件指针
);
```
- 返回值：实际成功读取的**数据个数**；如果文件末尾，返回值小于 `count`
### 字符串I/O函数
#### 1. 字符串格式化写入：`sprintf`
```c
char buf[50];
int a = 100;
sprintf(buf, "数值：%d，字符串：%s", a, "test");
printf("%s\n", buf);  // 输出：数值：100，字符串：test
```

- **功能**：按格式将数据写入字符串数组（而非控制台 / 文件）。
- **原型**：`int sprintf(char *str, const char *format, ...);`
- **示例**：拼接字符串和数字：

#### 2. 字符串格式化读取：`sscanf`

- **功能**：按格式从字符串中读取数据到变量。
- **原型**：`int sscanf(const char *str, const char *format, ...);`
- **示例**：从字符串解析数据
```c
char str[] = "张三 22 95.5";
char name[20];
int age;
float score;
sscanf(str, "%s %d %f", name, &age, &score);
printf("姓名：%s，年龄：%d，成绩：%.1f\n", name, age, score);
// 输出：姓名：张三，年龄：22，成绩：95.5
```

## 文件定位
打开文件后，读写位置在开头（除了追加模式在末尾）


1. `fseek`：跳转位置
	* 功能：告诉电脑“接下来从文件的XX位置开始读写”（将文件流stream的文件位置指示器设置为offset所指向的值）
	* `int fseek(FILE* stream,long offset,int origin)`
		* offset：偏移量，相对于起点偏移的数量
		* stream：流，要修改的文件流
		* origin：起点，添加偏移量的位置，有以下值：SEEK_SET、SEEK_CUR、DEEK_END
	* 成功时返回0，否则返回非零值
2. `ftell`：查看当前位置
	* 功能：告诉你现在的读写位置在相对开头的第几个字节
	* `long ftell(FILE* stream)`
	* 成功时返回文件位置指示器，失败时返回-1L
3. `rewind`：回到开头
	* 功能：直接把读写位置跳回文件最开头
	* `void rewind(FILE* stream)`
---

## 缓冲控制函数

`fflush`：刷新缓冲区
* `int fflush(FILE* stream)`
* stream应是输出流
* 将缓冲区已有的数据强制输出，并清空缓冲区