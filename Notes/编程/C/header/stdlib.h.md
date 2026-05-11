在 C 语言中，`stdlib.h`（Standard Library Header）是标准库中非常重要的头文件之一，提供了内存管理、类型转换、随机数生成、程序控制等基础功能。以下是对其核心函数和功能的详细解析：

### **一、内存管理函数**

`stdlib.h`提供了动态内存分配与释放的核心函数，是 C 语言中手动管理内存的基础。

1. **`malloc(size_t size)`**
    
    - 功能：在堆区分配一块大小为`size`字节的连续内存，未初始化（内容随机）。
    - 返回值：成功返回指向内存块的指针；失败返回`NULL`（需检查返回值）。
    - 示例：

        ```c
        int *arr = (int*)malloc(5 * sizeof(int));  // 分配5个int的内存
        if (arr == NULL) { /* 内存分配失败处理 */ }
        ```
        
2. **`calloc(size_t nmemb, size_t size)`**
    
    - 功能：分配`nmemb`个大小为`size`字节的连续内存，**初始化为 0**。
    - 适用场景：需要初始化的数组（如清零的缓冲区）。
    - 示例：
        
        c
        
        ```c
        int *nums = (int*)calloc(10, sizeof(int));  // 10个int，全部初始化为0
        ```
        
3. **`realloc(void *ptr, size_t size)`**
    
    - 功能：调整已分配内存块的大小（扩大或缩小）。
    - 注意：
        - 若`ptr`为`NULL`，等价于`malloc(size)`。
        - 若`size`为 0，等价于`free(ptr)`（部分实现）。
        - 可能会移动内存块（返回新地址），原指针可能失效。
    - 示例：
        
        c
        
        ```c
        int *new_arr = (int*)realloc(arr, 10 * sizeof(int));  // 将arr扩大到10个int
        if (new_arr != NULL) arr = new_arr;  // 更新指针
        ```
        
4. **`free(void *ptr)`**
    
    - 功能：释放`ptr`指向的动态内存（必须是`malloc/calloc/realloc`分配的内存）。
    - 注意：
        - 释放后`ptr`成为野指针，建议置为`NULL`（避免二次释放）。
        - 不可释放非动态分配的内存（如栈上变量）。
    - 示例：
        
        c
        
        ```c
        free(arr);
        arr = NULL;  // 避免野指针
        ```
        

### **二、类型转换函数**

用于字符串与数值之间的转换。

1. **`atoi(const char *str)`**
    
    - 功能：将字符串`str`转换为`int`类型（忽略前导空格，遇到非数字字符停止）。
    - 示例：
        
        c
        
        ```c
        int num = atoi("123");  // num = 123
        int num2 = atoi("  45abc");  // num2 = 45（忽略空格和后续非数字）
        ```
        
2. **`atol(const char *str)` / `atoll(const char *str)`**
    
    - 功能：分别转换为`long`和`long long`类型，用法同`atoi`。
3. **`strtod(const char *str, char **endptr)`**
    
    - 功能：将字符串转换为`double`类型，`endptr`指向转换终止的位置（可用于检测无效字符）。
    - 示例：

```c
        char *str = "3.14abc";
        char *end;
        double val = strtod(str, &end);  // val = 3.14，end指向"abc"
```


4.**`strtol(const char *str, char **endptr, int base)`**- 功能：按`base`进制（2-36）将字符串转换为`long`类型。

- 示例：
    
    c
    
    ```c
    long hex = strtol("1A3", NULL, 16);  // 16进制"1A3" → 419（十进制）
    ```
    

### 三、随机数生成函数  提供伪随机数（需种子初始化）。

1.**`rand(void)`**- 功能：返回一个`0`到`RAND_MAX`（通常为`2^31-1`）之间的伪随机整数。

2.**`srand(unsigned int seed)`**- 功能：设置随机数种子（相同种子产生相同序列）。

- 常用做法：用当前时间作为种子（确保每次运行序列不同）。
- 示例：
    
    c
    
    ```c
    #include <time.h>  // 需配合time()函数
    srand((unsigned int)time(NULL));  // 初始化种子
    int r = rand() % 100;  // 生成0-99的随机数
    ```
    

### 四、程序控制函数  用于程序的退出、环境变量操作等。

1.**`exit(int status)`**- 功能：终止程序运行，释放所有资源（关闭文件、刷新缓冲区）。

- `status`：退出状态码（`0`表示正常退出，非 0 表示异常）。
- 示例：
    
    c
    
    ```c
    if (error_occurred) {
        exit(1);  // 异常退出
    }
    ```
    

2.**`abort(void)`**- 功能：异常终止程序（不清理资源，可能产生核心转储文件用于调试）。

3.**`system(const char *command)`**- 功能：执行系统命令（依赖操作系统，跨平台性差）。

- 返回值：命令的退出状态（不同系统实现可能不同）。
- 示例：

    ```c
    system("ls");  // Linux：列出目录内容
    system("dir"); // Windows：列出目录内容
    ```
    

### 五、其他常用函数
**1.**`void* bsearch(const void *key, const void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *))`**- 功能：对有序数组进行二分查找（需提供比较函数）。
- 给的数组必须已经排列好
- key：搜索对象
- base：要搜索的数组
- nmumb：数组元素个数
- size：元素大小
- compar：函数指针 第一个参数是要找的 第二个是数组中某个的元素

2.**`void* qsort(void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *))`**- 功能：快速排序（可排序任意类型数组，需自定义比较函数）。
* `void* base`：要查找的数组，void* 是无类型指针
* `size_t nmemb`：数组元素数量
* `size_t size`：元素大小
* compar：函数指针 ，输入的两个是数组中的元素

- 示例（排序 int 数组）：
    
    c
    
    ```c
    int compare(const void *a, const void *b) {
        return *(int*)a - *(int*)b;  // 升序
    }
    int arr[] = {3, 1, 4};
    qsort(arr, 3, sizeof(int), compare);  // 排序后：1,3,4
    ```
    

3.**`abs(int n)` / `labs(long n)` / `llabs(long long n)`**- 功能：计算整数的绝对值。

###** 使用注意事项 **1. 动态内存分配后必须检查`NULL`，避免空指针访问。

2. 内存使用完毕后需用`free`释放，否则导致内存泄漏。

3. `rand()`是伪随机数，需用`srand()`初始化种子（通常结合`time(NULL)`）。

4. `system()`函数有安全风险（如命令注入），谨慎使用。