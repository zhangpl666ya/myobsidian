>[!Reminder]
>queue不暴露迭代器！！！


---

## 一、什么是 STL 队列（`std::queue`）

`std::queue` 是 **容器适配器（Container Adapter）**，  
特点是：**先进先出（FIFO，First In First Out）**

📌 类似现实中的排队：

- 先来的人 → 先服务
    
- 后来的人 → 后服务
    

---

## 二、queue 的底层实现

`queue` 本身不是一个“真正的容器”，  
它是对 **其他容器的封装**，默认底层使用：

```cpp
deque
```

也可以指定为：

- `list`
    
- 其他支持相关接口的容器
    

```cpp
queue<int, list<int>> q;
```

---

## 三、queue 的特点和限制

### ✅ 特点

- 只能访问：
    
    - 队头（front）
        
    - 队尾（back）
        
- 不支持随机访问（没有 `[]`）
    

### ❌ 限制

- 不能遍历
    
- 不能直接访问中间元素
    

---

## 四、queue 常用接口（重点）

| 函数        | 作用     |
| --------- | ------ |
| `push(x)` | 入队（尾部） |
| `pop()`   | 出队（头部） |
| `front()` | 获取队头元素 |
| `back()`  | 获取队尾元素 |
| `empty()` | 是否为空   |
| `size()`  | 元素个数   |

---

## 五、基本使用示例

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    q.push(10);
    q.push(20);
    q.push(30);

    cout << q.front() << endl; // 10
    cout << q.back() << endl;  // 30

    q.pop(); // 移除 10

    cout << q.front() << endl; // 20
    cout << q.size() << endl;  // 2

    return 0;
}
```

---

## 六、入队 & 出队示意

```text
push(10) → [10]
push(20) → [10, 20]
push(30) → [10, 20, 30]

pop()    → [20, 30]
```

---

## 七、queue 的典型应用场景

### 1️⃣ 广度优先搜索（BFS）

```cpp
queue<int> q;
q.push(start);

while (!q.empty()) {
    int cur = q.front();
    q.pop();

    // 处理 cur
}
```

### 2️⃣ 任务调度 / 消息队列

- 操作系统任务队列
    
- 打印任务
    
- 网络请求缓冲
    

### 3️⃣ 模拟排队问题

- 银行叫号
    
- 食堂排队
    

---

## 八、queue vs deque vs stack（对比）

| 容器      | 特点          |
| ------- | ----------- |
| `queue` | FIFO，只能头删尾加 |
| `stack` | LIFO，先进后出   |
| `deque` | 双端队列，可前后插删  |

---

## 九、注意事项（常考点）

⚠️ **pop() 不返回值**

```cpp
q.pop();       // ❌ 没有返回值
int x = q.front();
q.pop();       // ✅ 正确做法
```

⚠️ **空队列不能访问 front/back**

```cpp
if (!q.empty()) {
    cout << q.front();
}
```

---

## 十、一句话总结

> `std::queue` 是一个 **先进先出（FIFO）** 的容器适配器，  
> 常用于 **BFS、任务调度、排队模拟** 等场景。
