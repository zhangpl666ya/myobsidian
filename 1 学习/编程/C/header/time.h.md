
# 数据类型k
1. time_t
	* 本质：通常是long long 类型数据
	* 含义:以纪元时间（1970-01-01 00：00：00 UTC）以来的秒数
	* 用途：作为时间的原始数值，用于时间存储、传递和计算
2. clock_t
	* 本质：一种算术类型，表示CPU时间
	* 含义：衡量程序运行时占用的CPU资源时间
	* 用途：计算程序执行时CPU耗时
3. struct tm
	* 本质：机构体类型，用于分解时间（将时间拆分为组件）
	* 成员说明：
		```c
		struct tm{
		int tm_sec; //秒，0-60，60为闰秒
		int tm_min;  //分，0-59
		int tm_hour; //时，0-23
		int tm_mday; //日，1-31
		int tm_mon;  //月，0-11
		int tm_year;  //年，相对于1900的差
		int tm_wday;  //星期，0-6，0代表周日
		int tm_yday;  //年内天数，0-365，0代表1月1日
		int tm_isdst;  //夏令时表示 正数:启用；0：不启用；负数：未知
		}
		```
	* 用途：方便获取时间的具体组件 


# 宏定义
1. CLOCKS_PER_SEC
	* 含义：1秒包含的clock_t单位数量，即clock_t与秒的换算因子
	* 用途：将clock（）返回的clock_t值换算为秒
2. NULL
	* 含义：空指针常量



# 核心函数
## 获取时间
1. time_t time(time_t* timer)
	* 获取当前系统的日历时间（时间戳）
	* 参数：若timer非NULL，则将结果存入timer指向的地址；同时返回该时间戳
	* 失败返回（time_t）-1
	* 示例：
```c
time_t now;
time(&now);//将当前时间存入now
//或者另一种表示方式
time_t now = time(NULL);
```
2. clock_t clock(void)
	* 功能：获取程序从启动到当前的CPU时间
	* 失败：返回（clock_t）-1
	* 示例
```c
clock_t start = clock();
clock_t end = clock();
double cpu_time = (double)(end-start)/CLOCK_PER_SEC;//转换为秒
```
## 时间戳与分解时间的转换
1. struct tm* localtime(const time_t* timer)
	* 功能：将time_t时间转换为本地时间（考虑时区和夏令时）的struct tm
	* 返回：指向静态分配的struct tm的指针（多次调用会覆盖之前的结果）
	* 失败返回NULL
```c
time_t now = time(NULL);  //获取当前时间戳
struct tm* local_tm = localtime(&now);   //转换为本地时间的struct tm
if(local_tm==NULL){
	printf("fail")
	return;
}


```
2. time_t mktime(struct tm* tm)
	* 功能：将struct tm表示的本地时间转换回time_t时间戳
	* 特性：会自动修正struct tm中不合理的值，并更新tm_wday和tm_yday
	* 失败：返回（time_t)-1
```c

  struct tm tm = {
        .tm_sec = 70,    // 秒：70（超过60）
        .tm_min = 61,    // 分：61（超过59）
        .tm_hour = 25,   // 时：25（超过23）
        .tm_mday = 32,   // 日：32（超过当月最大天数）
        .tm_mon = 13,    // 月：13（超过11）
        .tm_year = 123   // 年：2023（123 + 1900）
    };
    time_t t = mktime(&tm);//转换时间戳，同时修正tm不合理值并给出tm_mday和tm_wday
```

3. struct tm* gmtime(const time_t* timer)
	* 功能：类似localtime，但转换为UTC时间（总之用不到）


## 时间格式化（转换为字符串）
1. char* asctime(const struct tm* tm)
	* 功能：将struct tm转换为固定格式的字符串（Wed Oct 29 21:49:08 2025/n）
	* 格式：共26个字符（包括换行符和终止符）
	* 返回：指向静态字符串指针
```c
time_t now = time(NULL);
struct tm* local_tm=localtime(&now);

char* time_str = asctime(local_tm);
printf("%s",time_str);
```

2. char* ctime(const time_t* timer)
	* 功能：等价于asctime（localtime(timer)），即先将时间戳转为本地指针struct tm，再转为固定格式字符串
	* 返回：静态字符串指针


3. size_t strftime(char* str, size_t maxsize,const char* format,const struct tm* tm)
	* 功能：***自定义格式化***时间为字符串
	* 参数：
		* str：存储结果的缓冲区
		* maxsize：缓冲区最大容量
		* format：格式化控制字符串
		* tm：待格式化的struct tm
	* 返回：成功写入返回写入的字符数（不含\0）
	* 常用转换说明符：
		* %Y：4位年份；
		* %y：2位年份；
		* %m：2位月份；
		* %d：2位日期；
		* %H：24小时制小时；
		* %M：分钟，00-59；
		* %S：秒；
```c
struct tm* local=localtime(&now)
char buf[100];
strftime(buf,sizeof(buf),"现在是%Y年%m月%d日 %H:%M:%S",local);
printf("%s\n",buf);
```

## 时间差计算
* double difftime(time_t time1,time_t0)
	* 功能：计算时间戳差值
	* 返回：以秒为单位的**double**值
```c
time_t start = time(NULL);
//等待一段时间
time_t end =time(NULL);
double diff = difftime(end,start);
```