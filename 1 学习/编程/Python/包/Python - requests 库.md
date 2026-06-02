---
tags: [Python, 网络请求, requests]
---

# Python - requests 库

> requests 是 Python 处理 HTTP 通信的事实标准库。`pip install requests`

## 库的定位

- **本质**：高阶 HTTP 客户端，定位类似 `curl` 的封装
- **执行模型**：**同步阻塞** — 发起调用后程序挂起直到数据返回
- **优点**：比浏览器引擎快、配置开销低、API 简洁
- **缺点**：**不能执行 JS**，只能拿到服务器原始 HTML（抓 SPA 页面要用 Selenium/Playwright）

## 必备伪装：`fakeHeaders`

不传自定义 headers 时，`requests` 会以 `python-requests/...` 标识自己，WAF 立刻拉黑。

| Header | 作用 | 示例值 |
|---|---|---|
| `User-Agent` | 伪装成正常浏览器 | `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36` |
| `Accept` | 声明接受的 MIME 类型 | `text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8` |

```python
fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
```

## 关键响应属性

`r = requests.get(...)` 后的常用属性：

| 属性 | 含义 | 用途 |
|---|---|---|
| `r.text` | 已解码字符串 | 直接看 HTML 文本 |
| `r.content` | 原始二进制 | 存图片/视频/文件时用 |
| `r.apparent_encoding` | 从字节反推真实编码 | 不盲信 HTTP header 的编码声明 |

## 常见坑

- ⚠️ 不传 `headers=` → 默认 UA 是 `python-requests/...`，被 WAF 拦
- ⚠️ 直接读 `r.text` 不调 `apparent_encoding` → 中文网页乱码
- ⚠️ `requests.get(...)` 不设 `timeout=` → 网络挂起时无限阻塞

## 自检清单

- [ ] `requests.get/post` 带了 `headers=` 和 `timeout=`
- [ ] 读 `r.text` 前先 `r.encoding = r.apparent_encoding`

## 关联

- 实战代码见 [[Python - requests 实战]]
- HTML 解析见 [[Python - BeautifulSoup]]
- 响应处理见 [[Python - JSON 与 API 响应]]
- 错误处理见 [[Python - 网络请求 错误处理]]
