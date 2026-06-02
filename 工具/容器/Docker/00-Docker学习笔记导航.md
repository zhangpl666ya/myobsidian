---
tags:
  - "工具/Docker"
  - "笔记/MOC"
---
# Docker 学习笔记

> 从零开始学习 Docker，手把手教程，2026-05-25 整理

---

## 📚 目录

### 基础概念
- [[01-Docker基础概念]] — 镜像、容器、仓库，核心概念解释
- [[02-Dockerfile基础]] — 常用指令：FROM、RUN、COPY、CMD、WORKDIR
- [[03-Dockerfile进阶-多阶段构建]] — Multi-Stage Build，减少镜像体积
- [[04-Docker-Compose入门]] — 多容器管理，一键启动整套应用

---

## 🗺️ 学习路径

```
第1步：理解基础概念
         ↓
第2步：docker run hello-world 第一次体验
         ↓
第3步：docker run -it ubuntu bash 交互式容器
         ↓
第4步：docker commit 手动制作镜像
         ↓
第5步：Dockerfile + docker build 自动构建镜像
         ↓
第6步：多阶段构建优化镜像体积
         ↓
第7步：Docker Compose 管理多容器
```

---

## 💡 核心命令速查

```bash
# 镜像操作
docker images                    # 查看本地镜像
docker pull <镜像名>             # 拉取镜像
docker rmi <镜像名>              # 删除镜像
docker build -t <镜像名> .       # 构建镜像

# 容器操作
docker ps -a                     # 查看所有容器
docker run <镜像名>              # 运行容器
docker run -it <镜像名> bash     # 交互式运行
docker start <容器名>            # 启动已停止的容器
docker stop <容器名>             # 停止容器
docker rm <容器名>               # 删除容器
docker logs <容器名>             # 查看日志
docker exec -it <容器名> bash   # 进入容器

# Docker Compose
docker compose up -d             # 启动所有服务
docker compose down               # 停止所有服务
docker compose ps                 # 查看服务状态
docker compose logs -f            # 查看日志
docker compose build              # 重新构建
```

---

## 📊 概念对比

| 概念 | 说明 |
|------|------|
| 镜像 (Image) | 只读模板，菜谱 |
| 容器 (Container) | 镜像的实例，做出来的菜 |
| 仓库 (Registry) | 存放镜像的地方，Docker Hub |

| Dockerfile 指令 | 何时执行 |
|----------------|---------|
| FROM | 构建开始 |
| RUN | 构建时 |
| COPY | 构建时 |
| WORKDIR | 构建时 + 运行时 |
| CMD | 运行时 |

---

## 🔗 相关资源

- [Docker 官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Alpine 镜像](https://alpinelinux.org/) — 超轻量 Linux 发行版

---

_最后更新：2026-05-25_

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[01-Docker基础概念]]
- [[02-Dockerfile基础]]
- [[03-Dockerfile进阶-多阶段构建]]
- [[04-Docker-Compose入门]]
