# Dockerfile 进阶：多阶段构建

## 什么是多阶段构建？

多阶段构建（Multi-Stage Build）是一种 Dockerfile 写法，使用**多个 `FROM` 指令**将构建过程分成多个阶段，最终镜像只保留"运行所需"的内容。

---

## 为什么需要多阶段构建？

### 问题：构建产物包含太多冗余内容

| 构建方式 | 包含内容 | 最终体积 |
|---------|---------|---------|
| 普通构建 | 源码 + 编译器 + 依赖库 + 构建工具 | 很大 |
| 多阶段构建 | 只复制最终需要的文件 | 很小 |

### 典型场景

- **编译型语言**：C、C++、Go、Rust 需要编译，源码和编译器对运行没有价值
- **前端构建**：Node.js 构建产物（dist/）需要 nginx Serving，但不需要 node_modules

---

## 怎么写多阶段构建？

### 语法：`AS <阶段名>`

```dockerfile
# ===== 第一阶段：构建 =====
FROM ubuntu:latest AS builder

RUN apt update && apt install -y python3 python3-pip
WORKDIR /app
RUN echo 'print("Hello")' > hello.py

# ===== 第二阶段：运行 =====
FROM ubuntu:latest

COPY --from=builder /app/hello.py /app/hello.py
CMD ["cat", "/app/hello.py"]
```

关键点：
- `FROM ... AS builder`：给第一阶段起名 `builder`
- `COPY --from=builder`：从第一阶段复制文件，而不是从主机

---

## 实例：Go 应用多阶段构建

### 普通写法（体积巨大）

```dockerfile
FROM golang:latest

WORKDIR /app
COPY . .
RUN go build -o myapp .

CMD ["./myapp"]
```

最终镜像体积：**800MB+**（包含整个 Go 开发环境）

### 多阶段写法（极简）

```dockerfile
# ===== 第一阶段：编译 =====
FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o myapp .

# ===== 第二阶段：运行 =====
FROM alpine:latest

WORKDIR /app
COPY --from=builder /app/myapp /app/myapp

CMD ["/app/myapp"]
```

最终镜像体积：**10MB 左右**

---

## 原理图解

### 普通构建

```
┌─────────────────────────────────┐
│ ubuntu:latest          (~77MB)  │
│ + apt install golang  (~1GB)   │
│ + 源码、编译过程                │
│ + 最终二进制 myapp             │
└─────────────────────────────────┘
最终镜像: 1GB+
```

### 多阶段构建

```
第一阶段（builder）：
┌─────────────────────────────────┐
│ golang:1.21-alpine   (~300MB)  │
│ + 源码                          │
│ + 编译出 myapp                 │
│ + 构建工具、依赖库              │  ← 最终不要
└─────────────────────────────────┘

第二阶段（运行）：
┌─────────────────────────────────┐
│ alpine:latest        (~7MB)    │
│ COPY --from=builder /myapp     │  ← 只复制二进制
└─────────────────────────────────┘
最终镜像: ~10MB
```

---

## 常见语言的多阶段构建模板

### Python（解释型，不需要编译）

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "app.py"]
```

> 注意：Python 不需要多阶段，因为运行时也需要 Python 本身。

### Node.js 前端构建

```dockerfile
# ===== 第一阶段：构建 =====
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ===== 第二阶段：nginx Serving =====
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
```

### Rust

```dockerfile
# ===== 第一阶段：编译 =====
FROM rust:1.75-alpine AS builder

WORKDIR /app
COPY . .
RUN cargo build --release

# ===== 第二阶段：运行 =====
FROM alpine:latest

COPY --from=builder /app/target/release/myapp /myapp

CMD ["/myapp"]
```

---

## 多阶段构建 vs 单阶段构建对比

| 维度 | 单阶段 | 多阶段 |
|------|-------|--------|
| 镜像体积 | 大 | 小 |
| 构建复杂度 | 简单 | 稍复杂 |
| 适用场景 | 解释型语言练手 | 生产环境、编译型语言 |
| 构建缓存 | 好 | 需要合理安排 stages |

---

## .dockerignore 优化

不管单阶段还是多阶段，都应该排除无关文件：

```
# .dockerignore
.git
.gitignore
*.md
node_modules
.env
__pycache__
*.log
.DS_Store
```

---

## 总结：什么时候用多阶段？

| 场景 | 推荐做法 |
|------|---------|
| Python/Node.js 练手项目 | 单阶段即可 |
| Node.js 前端（需要构建） | 多阶段，nginx 部署构建产物 |
| Go/Rust/C++ 生产服务 | **强烈推荐多阶段** |
| Java/Kotlin (JAR/WAR) | 多阶段，JRE 运行不需要 JDK |

---

_最后更新：2026-05-25_