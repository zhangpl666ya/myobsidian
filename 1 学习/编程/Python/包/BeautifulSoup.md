---
tags: [Python, 网络请求, BeautifulSoup, HTML 解析]
---

# Python - BeautifulSoup 4

> HTML/XML 解析的事实标准库，把网页文本转成可查询的 DOM 树。`pip install beautifulsoup4`

## 库的定位

- **本质**：DOM 树解析器，吃进 HTML 文本搭出节点-标签图
- **作用**：从 HTML 中提取数据，配合 `requests` 做爬虫

## 初始化

```python
import bs4
soup = bs4.BeautifulSoup(html_text, "html.parser")
```

## 节点组成：HTML 标签的解剖

每个节点对应 Python 属性：

| 属性/语法 | 含义 | C++ 类比 |
|---|---|---|
| `tag.text` | 纯文本（剥离所有标签） | — |
| `tag['attr_name']` | 属性字典查找（如 `link['href']`） | `std::map::operator[]` |
| 嵌套查询 | 先定位外层 tag，再在其 scope 内查 | 缩小范围避免数据污染 |

## 核心搜索 API

| 函数 | 返回 | 找不到时 |
|---|---|---|
| `.find(name, attrs)` | 第一个匹配节点 | `None` |
| `.find_all(name, attrs)` | 所有匹配节点（list） | `[]` |
| `.findNext(name)` | 跳到同层下一个匹配 | `None` |

**基础查询：**

```python
# 找第一个
title_tag = soup.find("h1")

# 找所有
all_links = soup.find_all("a")

# 跳到下一个
next_span = label_tag.findNext("span")
```

## 数据提取

```python
# 取文本
text = tag.text

# 取属性
url = tag['href']

# 属性存在性检查
url = tag['href'] if 'href' in tag.attrs else "default"
```

## 常见坑

- ⚠️ `class` 是 Python 关键字，直接 `find("div", "debug-info")` 会 `SyntaxError` → 必须用 `attrs={"class": "debug-info"}`
- ⚠️ `find()` 找不到时返回 `None`，直接 `.text` 会崩 → 先判断

## 自检清单

- [ ] 查询 `class` 时用了 `attrs={"class": ...}`
- [ ] 拿到 `None` 时有判空

## 关联

- 配合 [[requests 库]] 做爬虫
- 配合 [[requests 实战]] 的 GET 模板
