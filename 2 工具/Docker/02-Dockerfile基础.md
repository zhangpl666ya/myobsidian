---
tags:
  - "工具/Docker"
  - "工具/Dockerfile"
  - "笔记/速查"
---
# Dockerfile 基础

## 什么是 Dockerfile？

Dockerfile 是一个**文本文件**，包含构建 Docker 镜像的所有指令。类似于菜谱的配方表，告诉你一步步需要做什么。

---

## 第一个 Dockerfile

```dockerfile
FROM ubuntu:latest

RUN apt update && apt install -y python3

WORKDIR /app
COPY hello.py .

CMD ["python3", "hello.py"]
```

---

## 指令详解

### FROM — 基于哪个镜像

```dockerfile
FROM ubuntu:latest
```

- `FROM` 是每个 Dockerfile 必须有的第一条指令
- 指定**基础镜像**，所有后续操作都基于它进行
- `:latest` 表示标签（tag），不写默认是 latest
- 常见基础镜像：`ubuntu`、`python:3.11`、`node:20`、`golang:1.21`、`alpine`

**类比**：盖楼的地基

---

### RUN — 在构建时执行命令

```dockerfile
RUN apt update && apt install -y python3
```

- 在**镜像构建过程**中执行命令
- 执行的**结果会固化成镜像的一层**
- 适合安装依赖、配置环境

**示例：**
```dockerfile
# 安装软件包
RUN apt update && apt install -y nginx

# 创建目录
RUN mkdir -p /app/data

# 下载文件
RUN curl -o file.tar.gz https://example.com/file.tar.gz
```

---

### WORKDIR — 设置工作目录

```dockerfile
WORKDIR /app
```

- 设置后续指令的工作目录
- 如果目录不存在，会**自动创建**
- 类似于 `cd` 命令
- 路径是绝对路径，不会基于上一次 WORKDIR

**示例：**
```dockerfile
WORKDIR /app          # 切换到 /app 目录
COPY . .              # 复制文件到这里
WORKDIR /app/src      # 再切换到 /app/src
```

---

### COPY — 复制文件到镜像

```dockerfile
COPY hello.py .
```

- 把**主机上的文件**复制到**镜像里**
- 格式：`COPY <源路径> <目标路径>`
- `.` 表示当前构建上下文目录

**示例：**
```dockerfile
COPY package*.json /app/        # 复制 json 文件
COPY src /app/src                # 复制整个目录
COPY . /app                      # 复制所有文件
```

**注意：** `COPY` 和 `RUN` 的区别：
- `RUN` 在镜像里执行命令
- `COPY` 把主机的文件放进镜像

---

### CMD — 容器启动命令

```dockerfile
CMD ["python3", "hello.py"]
```

- 定义**容器启动时**默认执行的命令
- **镜像构建时不执行**，只有 `docker run` 时执行
- 一个 Dockerfile 只能有一个 CMD（多个只最后一个生效）
- 可以被 `docker run` 后面的参数**覆盖**

**示例：**
```dockerfile
CMD ["python3", "app.py"]                    # 运行 Python
CMD ["node", "server.js"]                    # 运行 Node.js
CMD ["nginx", "-g", "daemon off;"]          # 运行 Nginx
CMD ["bash"]                                 # 进入交互式 bash
```

**两种写法（推荐数组形式）：**
```dockerfile
# 推荐：exec 形式（JSON 数组）
CMD ["python3", "hello.py"]

# 不推荐：shell 形式
CMD python3 hello.py
```

---

## docker build 命令详解

```bash
docker build -t my-image:v1 .
```

| 部分 | 含义 |
|------|------|
| `docker build` | 构建镜像 |
| `-t` | 给镜像打标签（tag） |
| `my-image:v1` | 镜像名:版本号 |
| `.` | 构建上下文目录（在此目录找 Dockerfile） |

---

## 构建上下文（Build Context）

### 什么是构建上下文？

`.` 表示"当前目录"，Docker 把这个目录的内容打包发送给 Docker daemon 来构建镜像。

```
执行 docker build -t my-app .
    ↓
当前目录的所有文件被 tar 打包
    ↓
发送给 Docker daemon
    ↓
daemon 按照 Dockerfile 执行构建
    ↓
COPY hello.py . 中的 hello.py 来自这里
```

### .dockerignore 文件

类似 `.gitignore`，排除不需要的文件：

```
# .dockerignore
node_modules
.git
*.log
__pycache__
.env
```

---

## RUN vs CMD vs COPY 对比

| 指令 | 什么时候执行 | 作用 |
|------|------------|------|
| `RUN` | **构建时** | 在镜像里执行命令，结果固化成镜像层 |
| `CMD` | **容器启动时** | 容器跑起来后才执行，可以被覆盖 |
| `COPY` | **构建时** | 把文件从主机复制进镜像 |

---

## 一个完整例子：Python Web 应用

### 项目结构

```
my-app/
├── Dockerfile
├── hello.py
└── requirements.txt
```

### hello.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### requirements.txt

```
flask==3.0.0
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello.py .

EXPOSE 5000

CMD ["python", "hello.py"]
```

### 构建并运行

```bash
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
```

访问 http://localhost:5000 就能看到 "Hello from Docker!"

---

## 常见问题

### Q: 为什么用 `python:3.11-slim` 而不是 `ubuntu`？

`slim` 是官方提供的精简版，去掉了不需要的工具和文档，体积小很多：

| 镜像 | 大小 |
|------|------|
| `ubuntu` | ~77MB |
| `python:3.11` | ~1GB |
| `python:3.11-slim` | ~150MB |
| `python:3.11-alpine` | ~50MB |

### Q: `&&` 和 `;` 有什么区别？

```dockerfile
# && 的特点：前一个命令失败，后续不执行
RUN apt update && apt install -y python3

# ; 的特点：不管前一个成功失败，都执行下一个
RUN apt update ; apt install -y python3
```

### Q: `pip install` 前为什么要 `--no-cache-dir`？

减少镜像体积。pip 默认会缓存下载的文件，但这些缓存在镜像里没用，反而占空间。

---

_最后更新：2026-05-25_

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[2 工具/Docker/03-Dockerfile进阶-多阶段构建]]
- [[2 工具/Docker/00-Docker学习笔记导航]]
