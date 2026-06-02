---
tags: [Python, 网络请求, requests, 代码模板]
---

# Python - requests 实战代码

> 爬虫用 GET、调 AI API 用 POST — 两套直接可复用的模板。

## GET 蓝图（爬虫）

```python
import requests

fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

r = requests.get("https://target-url.com", headers=fake_headers, timeout=10)

# ⚠️ 总是先做编码探测再读 text!
r.encoding = r.apparent_encoding

# 状态码非 2xx 抛异常
r.raise_for_status()
html_text = r.text
```

## POST 蓝图（AI API，如 OpenAI / MiniMax）

```python
api_headers = {
    "Authorization": f"Bearer {API_KEY}",   # ⚠️ 'Bearer ' 后有空格
    "Content-Type": "application/json"
}

payload = {
    "model": "abab6.5s",
    "messages": [                           # ⚠️ 复数 messages
        {"role": "system", "content": "Instructions..."},
        {"role": "user", "content": "Question..."}
    ],
    "temperature": 0.1
}

# ⚠️ 用关键字参数 json=（自动序列化），不要用 data=
response = requests.post(url, headers=api_headers, json=payload, timeout=30)
response.raise_for_status()
```

## 常见坑

- ⚠️ 不调用 `r.raise_for_status()` → 服务器 500/404 你还以为成功
- ⚠️ POST 用 `data=` 而不是 `json=` → 不会自动序列化，服务器解析失败

## 自检清单

- [ ] GET 后调了 `r.raise_for_status()`
- [ ] POST 用关键字参数 `json=payload`（不是 `data=`）

## 关联

- 库的基础概念见 [[Python - requests 库]]
- AI API 响应解析见 [[Python - JSON 与 API 响应]]
- 错误处理见 [[Python - 网络请求 错误处理]]
