---
tags:
  - "工具/Obsidian"
  - "工具/YAML"
  - "概念/Frontmatter"
  - "笔记/速查"
aliases:
  - "--- 分隔符"
  - "YAML 元数据"
  - "Frontmatter"
---

# YAML Frontmatter 与 `---` 分隔符

> 三个 `-` 在 Obsidian 里是**双重身份**：
> 1. **在文件最顶部** → YAML 元数据边界（Frontmatter）
> 2. **在正文里** → 水平分隔线 `<hr>`

## 🪪 一句话区分

| 位置 | 身份 | 例子 |
|---|---|---|
| 文件最顶（前面无空行） | YAML Frontmatter 边界 | 笔记元数据 |
| 文件中任何位置 | 水平分隔线 | 章节切分 |

**判断方法**：看 `---` 是不是紧跟在文件第一行。

---

## 1. YAML Frontmatter 是什么

文件开头用一对 `---` 包裹的 YAML 块，存放笔记的元数据：

```yaml
---
tags:
  - "学习/Python"
  - "状态/进行中"
aliases:
  - "别名1"
created: 2026-06-02
---

# 笔记标题
正文从这里开始...
```

---

## 2. YAML 基本语法速查

### 键值对
```yaml
key: value
```

### 字符串加引号
中文、含特殊字符、纯数字字符串必须加引号：

```yaml
title: "我的笔记"            # ✓ 安全
title: 2026-01-01            # ✗ 会被解析成日期类型
title: "2026-01-01"          # ✓ 强制当字符串
title: "学习/AI"             # ✓ 含 / 必须引
```

### 列表（两种写法）

```yaml
# 写法 1：换行 + 缩进
tags:
  - 学习
  - Python
  - AI

# 写法 2：行内（紧凑）
tags: [学习, Python, AI]
```

### 嵌套对象

```yaml
author:
  name: "月月鸟"
  email: "yy@example.com"
```

### 注释

```yaml
# 这是注释，Obsidian 会忽略
tags: [学习]   # 行尾也能加注释
```

---

## 3. Obsidian 原生识别的字段

| 字段 | 作用 | 例子 |
|---|---|---|
| `tags` | 标签列表（出现在标签面板） | `["学习/AI", "状态/进行中"]` |
| `aliases` | 别名（任何别名都能 wikilink 跳过来） | `["AI对话", "多轮对话"]` |
| `cssclass` | 给整篇笔记附加 CSS class（用于 snippet 主题） | `"wide"` / `"callout-right"` |
| `permalink` | 内部永久链接路径 | `/notes/foo` |
| `publish` | 是否发布到 Obsidian Publish | `true` / `false` |

> **未识别的字段** Obsidian 直接忽略，不报错。所以乱填不碍事。

---

## 4. 插件扩展的字段

> 装对应插件才生效，否则只是普通元数据

| 字段 | 插件 | 用途 |
|---|---|---|
| `created`, `modified` | Templater / core | 时间戳，Dataview 里能按时间排序 |
| `date`, `status`, `priority`, `due` | Dataview, Tasks | 任务管理，自动列表 |
| `author`, `cover`, `summary` | Dataview | 文档元信息 |
| 任意自定义字段 | Dataview | 都能在查询里当筛选条件 |

---

## 5. 🌟 实战：推荐的最小 frontmatter

4 个维度管住一篇笔记，够用 90% 场景：

```yaml
---
tags:
  - "学习/AI"
  - "工具/API"
  - "状态/已完成"
aliases:
  - "AI 多轮对话"
  - "多轮对话"
created: 2026-06-02
modified: 2026-06-02
status: "已完成"
---
```

| 维度 | 字段 | 作用 |
|---|---|---|
| 分类 | `tags` | 标签面板能查 |
| 搜索 | `aliases` | 多入口能跳 |
| 时间 | `created` / `modified` | 知道什么时候写的 |
| 状态 | `status` | Dataview 自动列待办 |

---

## 6. ⭐ aliases 的妙用

`aliases` 是**额外的小名**，任何别名都能 wikilink 跳到这篇笔记。

```yaml
---
title: "AI 调用的多轮对话实现"
aliases:
  - "多轮对话"
  - "AI Chat"
  - "Chatbot 实现"
---
```

那么在 vault 里下面 **4 个** wikilink 都能跳到这篇笔记：

| 写法 | 来源 |
|---|---|
| `[[AI 调用的多轮对话实现]]` | 真名 |
| `[[多轮对话]]` | 别名 1 |
| `[[AI Chat]]` | 别名 2 |
| `[[Chatbot 实现]]` | 别名 3 |

**妙处**：
- **重命名友好**：文件改名后，旧的别名依然有效，老链接不失效
- **多入口命中**：一个概念有多个常用名时，别名都管用
- **模糊搜索友好**：忘了全名时，记住任一别名就能跳

---

## 7. 正文里的 `---`：水平分隔线

`---` 出现在**正文**里（非文件顶部），是 Markdown 的水平分隔线：

```markdown
## 章节 1
内容 A

---

## 章节 2
内容 B
```

渲染成一条横线。`***` 和 `___` 效果一样。

> **常见误用**：把 `---` 写在第一行（`# 标题` 之前）会触发 frontmatter 解析，导致整篇笔记没有正文。

---

## 8. Templater 模板（装了 Templater 才生效）

Templater 模板里可以用 `<%...%>` 动态字段，配合 `---` 的 YAML：

```yaml
---
created: <% tp.date.now("YYYY-MM-DD") %>
title: <% tp.file.title %>
tags:
  - "<% tp.date.now('YYYY/MM') %>"
---
```

新建笔记时自动填：
- `created` → 当前日期
- `title` → 文件名
- `tags` → 当前年月（自动归档）

---

## ⚠️ 易错点

- ❌ **frontmatter 前面有空行** → Obsidian 识别不到，会被当成正文第一行
- ❌ **YAML 缩进出错**（列表项 `-` 后没空格 / 用 tab）→ 整块变成正文显示
- ❌ **中文 / 含 `/` / 数字开头不加引号** → 解析成其他类型或报错
- ❌ **把 frontmatter 放在正文里** → 它会变成一段普通文字，不生效
- ❌ **`aliases` 里写 `[[xx]]`** → 写纯文本名字，不要加双链语法
- ❌ **把 `---` 写在第一行**（`# 标题` 之前）→ 触发 frontmatter 解析

## ✅ 自检清单

- [ ] `---` 在文件**最顶**（前面无空行）
- [ ] YAML 缩进用 2 空格（**不要**用 tab）
- [ ] 列表项 `-` 后有一个空格
- [ ] 字符串含中文 / 特殊字符 / 数字开头时加引号
- [ ] `aliases` 用纯文本，不要加 `[[]]`
- [ ] `tags` 放最后或最早位置都行，Obsidian 都能识别
- [ ] 文件结尾可加一个 `---` 收尾（也可省略）

---

## 📚 关联

- Obsidian 基础目录: [[obsidian学习笔记]]
- Markdown 语法: [[obsidian语法]]
- 双链用法: [[双链]]
- 模板机制: [[工具/笔记软件/Obsidian/模板]]
- 插件一览: [[插件介绍]]

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[obsidian学习笔记]]
- [[双链]]
- [[工具/笔记软件/Obsidian/模板]]
