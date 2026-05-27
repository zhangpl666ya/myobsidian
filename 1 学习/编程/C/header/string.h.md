# 字符串操作
`char* strcpy( char* dest, const char* src )`
`errno_t strcpy_s( char* restrict dest, rsize_t destsz, const char* restrict src )`
* 将src所指向的以空字符结尾的字符串复制到dest指向的首个元素的字符数组中
* 参数：
	* dest：要写入的字符数组的指针
	* src：要复制的的字符串的指针
	* destsz：要写入的最大字符
* 返回值：返回dest副本

`char *strncpy( char *dest, const char *src, size_t count）`（跟上一个差不多）
* 复制src指定数量字符到dest
* 参数
	* dest ：要复制到的字符数组指针
	* src：指向要复制的字符数组的指针
	* count：要复制到最大字符数
* 返回值：返回dest副本

`char *strcat( char *dest, const char *src )`
`errno_t strcat_s(char *restrict dest, rsize_t destsz, const char *restrict src)`
* 将src指向的空字符结尾的字符串的**副本**追加到dest末尾 ***src[0]会替换dest末尾的空字符***
* 参数：
	* dest：被追加的字符串的指针
	* src：要复制的字符串指针
	* destsz：要写入的最大字符数
* 返回值：返回dest的副本

`char *strncat( char *dest, const char *src, size_t count )`(跟上一个差不多)
* 将src指向的空字符结尾的字符串的**副本**追加到dest末尾 ***src[0]会替换dest末尾的空字符***
* 参数：
	* dest：被追加的字符串的指针
	* src：要复制的字符串指针
	* destsz：要写入的最大字符数
* 返回值：返回dest的副本

`char *strdup( const char *src );`
`char *strndup( const char *src, size_t size )`
* 返回一个指向以空字符结尾的字节字符串的指针，该字符串包含从`src`指向的字符串中最多`size`字节的副本。新字符串的空间获取方式如同调用了 [malloc](https://en.cppreference.com/w/c/memory/malloc.html "c/memory/malloc") 。如果在前`size`字节中未遇到空终止符，则会将其附加到复制的字符串后面。
* 参数：
	* src：指向要复制的字符串指针
	* size：从src复制的最大字节数
* 返回值：指向新分配的指针，失败返回NULL

---

# 字符串检查
[size_t](https://en.cppreference.com/w/c/types/size_t.html) strlen( const char* str )
[size_t](https://en.cppreference.com/w/c/types/size_t.html) strnlen_s( const char* str, [size_t](https://en.cppreference.com/w/c/types/size_t.html) strsz )
* 返回给定的以空字符结尾的字节字符串的长度，即由str指向第一个元素的字符数组中，直至（但不包括）第一个空字符的字符数量
* 参数
	* str：要检查的字符串的指针
	* strsz：要检查的最大字符数
* 返回值：str的长度

`int strcmp( const char* lhs, const char* rhs )
`int strncmp( const char* lhs, const char* rhs, size_t count )`
* 比较两个可能以空字符结尾的数组中最多count个字符。比较按字典顺序进行。空字符后面的字符不参与比较。
* 参数：
	* lhs：第一个字符串指针
	* rhs：第二个字符串指针
	* count：比较数
* 返回值：如果lhs在字典序中位于rhs之前，则返回负值；如果lhs和rhs比较相等，或者计数为零，则返回零；。如果lhs在字典顺序中位于rhs之后，则返回正值。

`int strcoll( const char* lhs, const char* rhs )`
* 根据由[LC_COLLATE](https://en.cppreference.com/w/c/locale/LC_categories.html "c/locale/LC categories")类别定义的当前区域设置，比较两个以空字符结尾的字节字符串
* 参数
	* lhs：第一个字符串指针
	* rhs：第二个字符串指针
* 返回值同上
* 与strcmp区别：
	- `strcmp`/`strncmp`：基于字符编码的原始比较，速度快，适合简单场景
	- `strcoll`：基于本地化规则的智能比较，适合多语言环境，但性能略低

`char* strchr( const char* str, int ch )`
* 在str所指向的以空字符结尾的字节字符串中，查找ch的首次出现。终止的空字符被视为字符串的一部分，并且在搜索'\0'时可以被找到。
* 参数：
	* str：被查找的字符串的指针
	* ch：要搜索的字符
* 返回值：指向str中被找到的字符的指针，未找到NULL

`char* strrchr( const char* str, int ch )
* 在str所指向的以空字符结尾的字节字符串中，查找ch的最后一次出现。终止的空字符被视为字符串的一部分，并且在搜索'\0'时可以被找到。就是上面的反向查找
* 参数：
	* str：被查找的字符串的指针
	* ch：要搜索的字符
* 返回值：指向str中被找到的字符的指针，未找到返回NULL

`size_t strspn( const char* dest, const char* src )
	* 返回由dest指向的以空字符结尾的字节字符串中最大初始段的长度，该初始段仅包含src指向的以空字符结尾的字节字符串中的字符。人话：从 `dest`的起始位置开始检查，逐个字符判断是否在 `str` 中，当遇到第一个不在 `str` 中的字符时停止，返回已匹配的字符数，如果 `dest` 为空或首字符不在 `str` 中，返回 `0`
* 参数：
	* dest：指向要分析的字符串指针
	* src：指向要搜索的字符串指针
* 返回值：仅包含由src指向的以空字符结尾的字节字符串中的字符的最大初始段的长度

`size_t strcspn( const char *dest, const char *src )
- 功能：
	- 从 `str1` 的起始位置开始检查，逐个字符判断是否**不在** `str2` 中。
	- 当遇到第一个**在** `str2` 中的字符时停止，返回已检查的字符数。
	- 如果 `str1` 为空或首字符在 `str2` 中，返回 `0`。
- 参数：
	* dest：指向要分析的字符串指针
	* src：指向要搜索的字符串指针
* 返回值：仅包含`src`所指向的以空字符结尾的字节字符串中未出现的字符的最长初始段的长度

`char* strstr( const char* str, const char* substr )
 - 在由str指向的以空字符结尾的字节字符串中查找由substr指向的以空字符结尾的字节字符串的首次出现。终止的空字符不参与比较。
 - 参数：
	 - str：指向要检查的字符串的指针
	 - substr：指向要搜索的字符串的指针
- 返回值：指向str中找到的子字符串的第一个字符的指针；如果未找到该子字符串，则返回空指针。如果substr指向空字符串，则返回str

`char* strtok( char* str, const char* delim )
- 按照delim中的符号切割字符串，会将str中匹配的符号修改为\0，输出前面的指针。该函数记忆上一次切割的位置，如果要对后面的继续切割，str传入NULL即可。
- 参数
	- str：指向要进行标记化的以空字符结尾的字节字符串的指针
	- delim：指向标识分隔符的以空字符结尾的字节字符串的指针
- 返回值：返回指向下一个标记的第一个字符的指针，如果没有标记，则返回空指针
- 问题：该函数只能记忆最近一次的切除地点，若有多个函数需要操作会出现错误
以下cppconference提供的解决方案：
`char* strtok_s( char* restrict str, rsize_t* restrict strmax, const char* restrict delim, char** restrict ptr )
- 进阶版，需要传入一个地址用于记忆，不容易出错
- 参数：
    -  str：指向要进行标记化的以空字符结尾的字节字符串的指针
	- delim：指向标识分隔符的以空字符结尾的字节字符串的指针
	- strmax：str剩余缓冲区大小
	- ptr：自主传入保存切割地址
-  返回值：返回指向下一个标记的第一个字符的指针，如果没有标记，则返回空指针
然而实际在VS里，没有strmax这个输入，改为：`char* strtok_s(char* restrict str,const char* restrict delim, char** restrict ptr)`
---

# 内存操作
这些函数与第一个标题的区别：
前面的只用于以`\0`结尾的字符串，这里的用于连续内存块，不仅限与字符串，二进制和结构体都可以。意味着mem不会因为\0停下来

`void* memchr( const void* ptr, int ch, size_t  count )`
- 在ptr所指向对象的前count个字节（每个字节都被解释为无符号字符）中，查找（无符号字符）ch的首次出现
- 参数：
	- ptr：指向待检查对象的指针
	- ch：要搜索的字节
	- 要检查的最大字节数
- 返回值：指向该字节位置的指针，如果未找到此类字节，则为 null 指针

`int memcmp( const void* lhs, const void* rhs, size_t count )`
- 功能strcmp，比较类型为无符号字符
* 参数：
	* lhs：第一个字符串指针
	* rhs：第二个字符串指针
	* count：要检查的字符数
* 返回值：如果lhs在字典序中位于rhs之前，则返回负值；如果lhs和rhs比较相等，或者计数为零，则返回零；。如果lhs在字典顺序中位于rhs之后，则返回正值。

`void *memset( void *dest, int ch, size_t count )
- 将一块连续内存的每个字节设置为指定的值
- 参数：
	- dest：只想要填充的对象的指针
	- ch：填充字节
	- count：要填充的字节数
- 返回值：dest的副本

`void* memcpy( void *dest, const void *src, size_t count )
- 从`src`所指向的对象复制`count`个字符到`dest`所指向的对象。这两个对象都被解释为无符号字符数组
- 参数：
	- dest：指向要复制到的对象的指针
	- src：指向要复制到对象的指针
	- count：要复制的字节数
- 返回值：dest副本

`void* memmove( void* dest, const void* src, size_t count )
- 从src所指向的对象中复制count个字符到dest所指向的对象中，这两个对象都被解释为无符号字符数组
- 参数：
	- dest：指向要复制到的对象的指针
	- src：指向要从中复制的对象指针
	- count：要复制到字节数
- 返回值：dest副本