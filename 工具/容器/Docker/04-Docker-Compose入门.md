---
tags:
  - "工具/Docker"
  - "工具/Docker-Compose"
  - "概念/多容器"
  - "笔记/概念入门"
---
# Docker Compose 入门

## 什么是 Docker Compose？

Docker Compose 是一个**定义和运行多容器应用**的工具。通过一个 `docker-compose.yml` 配置文件，定义多个服务（容器），然后一键启动/停止/管理它们。

---

## docker run vs docker compose

| 操作 | docker run | docker compose |
|------|-----------|----------------|
| 启动 | `docker run my-web` | `docker compose up -d` |
| 停止 | `docker stop my-web` | `docker compose down` |
| 查看状态 | `docker ps` | `docker compose ps` |
| 查看日志 | `docker logs my-web` | `docker compose logs web` |
| 进入容器 | `docker exec -it my-web bash` | `docker compose exec web bash` |
| 扩展副本 | 手动复制命令 | `docker compose up -d --scale web=3` |

---

## 基本概念

### services（服务）

一个服务就是一个**容器**。可以定义多个服务，Docker Compose 会同时管理它们。

### networks（网络）

容器之间可以通过服务名互相访问（在同一个 network 下）。

### volumes（卷）

持久化数据，即使容器删了，数据还在。

---

## 快速入门：一个 Node.js + Redis 应用

### 项目结构

```
my-app/
├── app.js
├── package.json
├── Dockerfile
└── docker-compose.yml
```

### app.js

```javascript
const express = require('express');
const redis = require('redis');

const app = express();
const client = redis.createClient({ socket: { host: 'redis' } });

client.on('error', (err) => console.log('Redis Client Error', err));

app.get('/', async (req, res) => {
  const visits = await client.incr('visits');
  res.send(`Visitor #${visits}`);
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

### package.json

```json
{
  "name": "web-app",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.0",
    "redis": "^4.6.0"
  }
}
```

### Dockerfile

```dockerfile
FROM node:20-slim

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY app.js .

CMD ["node", "app.js"]
```

### docker-compose.yml

```yaml
version: "3.8"

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

---

## docker-compose.yml 字段详解

### version

```yaml
version: "3.8"
```

- 指定 compose 文件格式版本
- `3.x` 是目前最常用的版本
- 不同版本支持的特性略有不同

### build

```yaml
web:
  build:
    context: .                 # Dockerfile 所在目录
    dockerfile: Dockerfile.app # 指定 Dockerfile 文件名
```

- 从 Dockerfile 构建镜像
- 如果只需要直接用现成镜像，用 `image`

### image

```yaml
redis:
  image: redis:7-alpine        # 使用 Docker Hub 的 redis 镜像
```

- 直接使用已有的镜像，不自己构建

### ports

```yaml
ports:
  - "3000:3000"                # 宿主机端口:容器端口
```

- 端口映射
- 容器内端口在左，宿主机端口在右

### depends_on

```yaml
depends_on:
  - redis                      # 等 redis 服务先启动
```

- 启动顺序依赖
- 注意：这只是启动顺序，**不等待服务完全就绪**

### environment

```yaml
environment:
  - NODE_ENV=production
  - REDIS_HOST=redis
```

- 设置环境变量
- 简写形式（数组）或者对象形式都可以

---

## 常用命令

### 启动所有服务

```bash
docker compose up -d
```

- `-d`：后台运行（detached）

### 启动并重新构建

```bash
docker compose up -d --build
```

### 停止所有服务

```bash
docker compose down
```

### 停止并删除镜像

```bash
docker compose down --rmi local
```

### 查看服务状态

```bash
docker compose ps
```

### 查看日志

```bash
docker compose logs          # 所有服务日志
docker compose logs web      # 指定服务日志
docker compose logs -f web   # 实时跟踪
```

### 进入容器

```bash
docker compose exec web bash
```

### 查看服务的网络

```bash
docker compose exec web ping redis
```

### 扩展服务副本

```bash
docker compose up -d --scale web=3
```

- 启动 3 个 web 容器副本
- 注意：如果没有 `ports` 配置，需要配合 `nginx` 做负载均衡

### 强制停止所有服务

```bash
docker compose kill
```

---

## 多阶段项目示例：前端 + 后端 + 数据库

```yaml
version: "3.8"

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      - DB_HOST=postgres
      - REDIS_HOST=redis
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"

volumes:
  postgres_data:
  redis_data:
```

---

## volumes 详解

### 为什么要用 volumes？

| 情况 | 行为 |
|------|------|
| 不用 volumes | 容器删除后，数据永久丢失 |
| 用 volumes | 容器删除后，数据还在 |

### volumes 语法

```yaml
volumes:
  postgres_data:/var/lib/postgresql/data
```

在文件底部定义：

```yaml
volumes:
  postgres_data:   # 具名 volume，Docker 自动管理存储位置
  redis_data:
```

### 挂载主机目录

```yaml
volumes:
  - /host/path:/container/path        # 绝对路径
  - ./relative/path:/container/path  # 相对路径（相对于 compose 文件目录）
```

---

## 多容器架构的好处

### 独立更新

```
场景：Redis 要升级到新版本

分开部署：  只重启 redis 容器，web 完全不受影响
合并部署：  整个应用都要重新构建
```

### 独立扩缩容

```
场景：访问量暴涨，web 服务压力大

docker compose up -d --scale web=3  ← 扩 3 个 web 副本
```

### 资源隔离

```
web:      限制 500MB 内存
redis:    限制 256MB 内存
postgres: 限制 1GB 内存
```

### 独立调试

```
docker compose logs web      ← 只有 web 的日志
docker compose logs postgres ← 只有数据库的日志
```

---

## 生产环境建议

### 使用 .env 文件

创建 `.env` 文件存储敏感配置（不提交到 git）：

```
POSTGRES_USER=user
POSTGRES_PASSWORD=secret123
```

在 compose 文件中引用：

```yaml
environment:
  - POSTGRES_USER=${POSTGRES_USER}
  - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

### healthcheck

```yaml
services:
  postgres:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5
```

---

## 总结

```
docker run    → 单个容器，手动管理
docker compose → 多个容器，配置文件管理，适合开发和中小型部署
Kubernetes    → 大规模生产环境，集群管理
```

---

_最后更新：2026-05-25_

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[00-Docker学习笔记导航]]
