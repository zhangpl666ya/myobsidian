---
tags:
  - "学习/AI"
  - "学习/编程/Python"
  - "工具/API"
  - "工具/HTTP"
  - "笔记/速查"
---

# AI 多轮对话实现 (MiniMax)

> 每次 `POST` 完服务器立刻失忆；让 AI "记住"前面的话，全靠**客户端**在内存里维护一个滚动增长的 `messages` 列表。



## 🎯 核心问题：无状态 HTTP

调用 AI API 用的就是普通 `requests.post(...)`，跟打开一个网页没区别。

- 服务器 **两次调用之间没有任何关联**
- 它不知道你 3 秒前问了啥，也不知道 5 分钟前的对话
- AI 的"记忆力"完全是你 **客户端在本地伪造出来的**

## 💡 解决方案：客户端 messages 列表

每次请求都把**完整对话历史**打包发过去。AI 看到的 `messages` 数组是连贯的，所以它表现得像有记忆。

**C++ 类比**：整个对话历史就是 `std::vector<Message>`，每次有人发言就 `push_back`。

## 🔑 三个 role 字段

| role | 谁 | 什么时候用 |
|---|---|---|
| `system` | 你 | **只在程序启动时**发一次，设定人设/语气/任务 |
| `user` | 用户 | 每轮用户输入后追加 |
| `assistant` | AI | 每轮 AI 回复后**必须追加**，否则下一轮 AI 完全失忆 |

## 📜 完整模板

```python
import requests

url = "https://api.minimax.chat/v1/text/chatcompletion_v2"
API_KEY = "your_real_api_key_here"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 1. 初始化「对话历史」容器 — 只放 system 一次
chat_history = [
    {"role": "system", "content": "You are a concise senior C++ engineer."}
]

print("=== MiniMax C++ Architect Chat Active ===")
print("Type 'exit' or 'quit' to terminate.\n")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ['exit', 'quit']:
        print("Bye!")
        break
    if not user_input:
        continue

    # 2. 追加 user
    chat_history.append({"role": "user", "content": user_input})

    payload = {
        "model": "abab6.5s",
        "messages": chat_history,   # 把整个历史发过去
        "temperature": 0.3
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()

        ai_reply = resp.json()["choices"][0]["message"]["content"]
        print(f"\nAI Architect:\n{ai_reply}")

        # 3. 追加 assistant — 不加这行下次就失忆
        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print(f"\n[错误]: {e}")
        # 4. 出错时把 user 那条 pop 掉，别让失败请求污染历史
        chat_history.pop()
```

## 🧠 工作流图

```
┌─────────────────────────────────────┐
│  chat_history = [system 消息]        │  ← 启动时只放一次
└─────────────────────────────────────┘
              ↓
   ┌──────────────────────────┐
   │  while True:              │
   │   读 user_input            │
   │   exit/quit? break        │
   │                           │
   │   history.append(user)    │ ← 第 1 步：长
   │   POST(history)            │ ← 第 2 步：发
   │   ai = response           │ ← 第 3 步：取
   │   history.append(ai)      │ ← 第 4 步：长  ★★★
   │   (失败时 pop user)        │
   └──────────────────────────┘
              ↓
  history 越来越长 = AI 记忆越来越远
```

## ⚠️ 易错点 (避坑清单)

- ❌ **忘 append assistant** → 下一轮 AI 完全失忆，分不清"上次/这次"
- ❌ **出错时不 pop user** → 失败请求留在历史里，下次重试又把脏数据发一次
- ❌ **system 消息每次循环都重发** → 浪费 token，污染角色设定
- ❌ **history 无上限** → 长对话会爆 token / 超时，要做窗口截断（只保留最近 N 条）
- ❌ **把 system 放错位置** → system 必须是 `messages[0]`，不能夹在中间

## 🧪 验证记忆的测试套路

第 1 问：「What is RAII in C++?」
第 2 问：「Give me a 3-line code example of what you just explained.」 ← 注意：没提 RAII

- AI 还是给你 RAII 例子 → ✅ 多轮记忆成功
- AI 让你澄清 "what do you mean" → ❌ 状态断了，去查 `append(assistant)` 那行

## 📚 关联

- HTTP POST 基础: [[requests 实战]]
- 错误处理模板: [[网络请求 错误处理]]
- 实际项目: [[调用本地大模型读取网页内容（基础版）]]
- 库的概念: [[requests 库]]

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[requests 实战]]
- [[调用本地大模型读取网页内容（基础版）]]
