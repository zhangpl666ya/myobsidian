---
tags:
  - "学习/编程/Python"
  - "工具/JSON"
  - "工具/API"
  - "笔记/速查"
tags: [Python, 网络请求, JSON, AI API]
---

# Python - JSON 与 API 响应

> 处理网络请求的响应：序列化（发送前）+ 解析（拿到响应后）。

## `json.dumps()` 关键参数

把 Python `dict` / `list` 压成 JSON 字符串。

| 参数 | 作用 |
|---|---|
| `indent=4` | 缩进换行，便于阅读（C++ pretty-print 风格） |
| `ensure_ascii=False` | **保留 Unicode 原字符**（如中文），不转成 `\u5e2e\u52a9` |

```python
import json
print(json.dumps(data, indent=4, ensure_ascii=False))
```

## OpenAI / MiniMax 响应结构陷阱

输入 payload 和服务器响应的键名**单复数不一致**：

```python
# 1. 输入 payload（复数：提交历史上下文）
payload = {"messages": [{"role": "user", "content": "..."}]}

# 2. 输出响应路径
# response["choices"]                          -> 复数数组（取 index 0）
# response["choices"][0]["message"]           -> 单数结构帧
# response["choices"][0]["message"]["content"] -> 目标文本
ai_text = response.json()["choices"][0]["message"]["content"]
```

> ⚠️ **核心陷阱**：复数 `messages` 进去，单数 `message` 出来。

## 常见坑

- ⚠️ `json.dumps` 不写 `ensure_ascii=False` → 中文被转义成 `\uXXXX`
- ⚠️ AI 响应里把 `messages`/`message` 写错 → 调试半天

## 自检清单

- [ ] 中文输出用 `json.dumps(..., ensure_ascii=False, indent=4)`
- [ ] AI API 响应取文本用 `response.json()["choices"][0]["message"]["content"]`

## 关联

- 配合 [[requests 实战]] 的 POST 模板
- 错误处理见 [[网络请求 错误处理]]

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[学习/编程语言/Python/快速看懂json结构]]
- [[requests 库]]
