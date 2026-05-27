# .iostream
## 1 cout：标准输出流
- 本质：ostream类的全局对象，关联操作系统的stdout；
- 核心操作：重载<<运算符将数据插入输出流
- 关键细节：
	- endl：等价于\n+flush（）(换行+强制刷新缓冲区)。效率低于\n
	- \n：仅换行，不刷新缓冲区
	- 支持链式（连续）调用：`cout<<"a="<<a<<endl;`
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    double b = 3.14159;
    // 链式输出
    cout << "整数：" << a << endl;          // 换行+刷新
    cout << "浮点数：" << b << "\n";       // 仅换行
    cout << "拼接：" << "a+b=" << a + b;   // 不换行，数据暂存缓冲区
    return 0;
}
```
## 2 cin：标准输入流
- 本质：istream类的全局对象，关联操作系统的stdin（标准输入）
- 核心操作：重载<<运算符，从输入流提取到数据到变量
- 关键细节：
	- 提取规则：默认按空白符（空格/换行/制表符）分隔，跳过前导空白；
	- 输入缓冲区：用户输入的内容先存到缓冲区，cin>>从缓存区读取；
	- 常用：getline（cin，str）读取整行（包括空格，直到换行），cin.get()读取单个字符
```cpp
int main() {
    int age;
    string name;
    cout << "输入姓名和年龄（空格分隔）：";
    cin >> name >> age;  // 按空格分隔读取
    cout << "姓名：" << name << "，年龄：" << age << endl;
   
	int num;
    string desc;
    cout << "输入数字：";
    cin >> num;          // 读取数字后，缓冲区残留「换行符」
    cin.ignore();        // 清空缓冲区的换行符（必须！否则 getline 会读空）
    cout << "输入描述（可含空格）：";
    getline(cin, desc);  // 读取整行，包括空格
    cout << "数字：" << num << "，描述：" << desc << endl;
    return 0;
    
}
```
std::cin是以换行符为停止标志，不读入换行符
getline也以换行符为停止标志，但读入换行符，不输入到字符串内
## 3 cerr：标准错误流（无缓冲）
- 本质：ostream类的全局对象，关联操作系统的stderr(标准错误)
- 核心特点：无缓冲区，数据立即输出（适合紧急错误提示）
- 用法与count一致，但语义上用于错误信息，非正常输出
```cpp
#include <iostream>
using namespace std;

int main() {
    int score;
    cout << "输入成绩（0-100）：";
    cin >> score;
    if (score < 0 || score > 100) {
        cerr << "错误：成绩超出合法范围！" << endl;  // 错误信息用 cerr
        return 1;
    }
    cout << "成绩：" << score << endl;
    return 0;
}
```
## 4 clog：标准日志流（有缓冲）
- **本质**：`ostream` 类的全局对象，同样关联 `stderr`；
- **核心特点**：有缓冲区，数据攒到一定量后输出（适合非紧急日志）；
- **用法**：与 `cerr` 语义区分 ——`cerr` 用于「紧急错误」，`clog` 用于「普通日志 / 调试信息」
```cpp
#include <iostream>
using namespace std;

int main() {
    clog << "日志：程序启动" << endl;    // 日志用 clog
    int a = 5, b = 0;
    if (b == 0) {
        cerr << "错误：除数不能为0" << endl;  // 错误用 cerr
        return 1;
    }
    clog << "日志：计算结果=" << a / b << endl;
    return 0;
}
```

# 流状态与错误处理

cin/cout 等流对象内部维护「状态标志」，用于标识 I/O 操作是否成功，这是处理非法输入的核心：

#### 1. 核心状态标志（`ios::iostate` 枚举）

|标志|含义|
|---|---|
|`goodbit`|无错误，流状态正常（值为 0）|
|`failbit`|输入 / 输出格式错误（如输入字符串到 int 变量），流仍可用|
|`badbit`|严重错误（如文件损坏、流关联的设备失效），流不可用|
|`eofbit`|到达流末尾（如 cin 读取到文件结束符 Ctrl+Z，或文件流读到文件末尾）|

#### 2. 状态检查方法

|方法|作用|
|---|---|
|`good()`|返回 true：仅当 `goodbit` 为真（无任何错误）|
|`fail()`|返回 true：`failbit` 或 `badbit` 为真（最常用，判断输入是否失败）|
|`bad()`|返回 true：仅 `badbit` 为真（严重错误）|
|`eof()`|返回 true：仅 `eofbit` 为真（到达流末尾）|
|`rdstate()`|返回当前状态标志（数值）|

#### 3. 状态重置：`clear()` + `ignore()`

- `cin.clear()`：重置流状态为 `goodbit`（必须先重置，否则流会拒绝后续操作）；
- `cin.ignore(n, ch)`：清空缓冲区前 `n` 个字符，直到遇到 `ch`（默认 `n=1`，`ch='\n'`）。

# 格式控制（`<iomanip>`）

默认输出格式往往不满足需求（如保留小数、对齐、进制），需用 `<iomanip>` 提供的「操纵符」或流的「成员函数」控制格式：

#### 1. 格式控制的两种方式

|方式|示例（设置宽度 10）|特点|
|---|---|---|
|操纵符（推荐）|`cout << setw(10) << a;`|链式调用，代码简洁|
|成员函数|`cout.width(10); cout << a;`|面向对象，语义清晰|

#### 2. 常用格式操纵符（需包含 `<iomanip>`）

|操纵符|作用|
|---|---|
|`setw(n)`|设置下一个输出的宽度为 `n`（仅对**下一个**输出有效）|
|`left/right`|输出内容左 / 右对齐（配合 `setw` 使用）|
|`setfill(ch)`|设置填充字符（默认空格，配合 `setw` 使用）|
|`fixed`|浮点数固定小数格式（如 3.14 而非 3.14e+00）|
|`scientific`|浮点数科学计数法格式（如 3.1415e+00）|
|`setprecision(n)`|配合 `fixed`：保留 `n` 位小数；默认：保留 `n` 位有效数字|
|`dec/hex/oct`|整数以十进制 / 十六进制 / 八进制输出|
|`showpos`|显示正数的 `+` 号（如 +10 而非 10）|
|`noshowpos`|取消正数的 `+` 号（默认）|
```cpp
    double pi = 3.1415926;

    // 1. 宽度+对齐+填充
    cout << "宽度+对齐：" << endl;
    cout << right << setw(10) << setfill('*') << a << endl;  // 右对齐，宽度10，填充*
    cout << left << setw(10) << setfill('-') << a << endl;   // 左对齐，宽度10，填充-

    // 2. 浮点数格式
    cout << "\n浮点数格式：" << endl;
    cout << fixed << setprecision(2) << pi << endl;          // 固定2位小数：3.14
    cout << scientific << setprecision(4) << pi << endl;     // 科学计数法4位小数：3.1416e+00

    // 3. 整数进制
    cout << "\n整数进制：" << endl;
    cout << dec << a << endl;  // 十进制：123
    cout << hex << showbase << a << endl;  // 十六进制（带0x）：0x7b
    cout << oct << noshowbase << a << endl; // 八进制（不带0）：173

    return 0;
}
```

# 文件流（`<fstream>`）

文件流是 iostream 的核心扩展，实现程序与文件的 I/O，核心类有 3 个：

|类名|功能|对应流方向|
|---|---|---|
|`ifstream`|只读文件|输入流|
|`ofstream`|只写文件|输出流|
|`fstream`|可读可写文件|输入 + 输出|

#### 1. 文件打开与关闭

- **打开方式**：
    - 构造函数打开：`ofstream fout("data.txt");`
    - `open()` 成员函数：`fout.open("data.txt" , ios::app)`
- **打开模式（可选，组合用 `|`）**：


| 模式            | 作用                          |
| ------------- | --------------------------- |
| `ios::in`     | 以读模式打开（`ifstream` 默认）       |
| `ios::out`    | 以写模式打开（`ofstream` 默认，会清空文件） |
| `ios::app`    | 追加模式（写时从文件末尾追加，不清空）         |
| `ios::trunc`  | 清空文件（`ios::out` 默认包含此模式）    |
| `ios::binary` | 二进制模式（默认是文本模式）              |


- **关闭文件**：`fout.close();`（析构函数会自动关闭，但显式关闭更安全）。

#### 2. 文本文件读写（最常用）

**示例 1：写文件（追加模式）**


```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // 打开文件：追加模式，若文件不存在则创建
    ofstream fout("score.txt", ios::app);
    if (!fout.is_open()) {  // 必须检查文件是否打开成功
        cerr << "错误：无法打开文件！" << endl;
        return 1;
    }
    // 写入数据
    fout << "张三 90 85 95" << endl;
    fout << "李四 88 92 80" << endl;
    fout.close();  // 关闭文件
    cout << "数据写入成功！" << endl;
    return 0;
}
```

**示例 2：读文件（逐行读取）**


```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream fin("score.txt");
    if (!fin.is_open()) {
        cerr << "错误：文件不存在！" << endl;
        return 1;
    }
    // 逐行读取文件内容
    string line;
    while (getline(fin, line)) {  // 直到文件末尾（eofbit）
        cout << line << endl;
    }
    fin.close();
    return 0;
}
```

#### 3. 二进制文件读写（拓展）

二进制模式不转换换行符（`\n` 与 `\r\n`），适合存储结构体、二进制数据：

```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Student {
    char name[20];  // 用char数组（string不能直接二进制写入）
    int score;
};

int main() {
    // 写二进制文件
    Student s1 = {"张三", 90};
    ofstream fout("student.bin", ios::out | ios::binary);
    fout.write((char*)&s1, sizeof(Student));  // 强制转换为char*
    fout.close();

    // 读二进制文件
    Student s2;
    ifstream fin("student.bin", ios::in | ios::binary);
    fin.read((char*)&s2, sizeof(Student));
    fin.close();
    cout << "姓名：" << s2.name << "，成绩：" << s2.score << endl;
    return 0;
}
```

---

# 字符串流（`<sstream>`）

字符串流将「字符串」作为流的载体，核心用于：

1. 字符串拆分 / 解析（`istringstream`）；
2. 高效字符串拼接（`ostringstream`）；
3. 类型转换（如 string → int/double）。

#### 1. istringstream：字符串输入流（解析）

**示例：拆分字符串 + 类型转换**

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string str = "张三 90 85.5";
    istringstream iss(str);  // 绑定字符串
    string name;
    int math;
    double chinese;
    // 按空格拆分并转换类型
    iss >> name >> math >> chinese;
    cout << "姓名：" << name << endl;
    cout << "数学：" << math << endl;
    cout << "语文：" << chinese << endl;
    return 0;
}
```

#### 2. ostringstream：字符串输出流（拼接）

**示例：高效拼接字符串（避免 `+` 频繁拷贝）**


```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ostringstream oss;
    // 链式拼接（支持任意类型）
    oss << "总分：" << 90 + 85.5 << "，平均分：" << (90 + 85.5)/2;
    // 转换为string
    string result = oss.str();
    cout << result << endl;  // 输出：总分：175.5，平均分：87.75
    return 0;
}
```

---

### 七、iostream 常见坑与避坑指南

1. **cin >> 后 getline 读空**：原因是 `cin >>` 残留换行符 → 解决方案：`cin.ignore(numeric_limits<streamsize>::max(), '\n')`；
2. **文件打开失败**：原因可能是路径错误（相对路径 vs 绝对路径）、权限不足 → 解决方案：检查 `is_open()`，用绝对路径测试；
3. **格式控制失效**：`setw(n)` 仅对下一个输出有效 → 解决方案：每次输出前重新设置；
4. **流状态异常后无法输入**：原因是 `failbit/eofbit` 未重置 → 解决方案：先 `cin.clear()`，再清空缓冲区；
5. **字符串流内存泄漏**：无需担心，`ostringstream/istringstream` 析构时自动释放内存；
6. **cout 输出顺序异常**：缓冲区未刷新 → 解决方案：关键位置加 `flush()` 或 `endl`。