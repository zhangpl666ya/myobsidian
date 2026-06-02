---
tags:
  - "工具/Docker"
  - "概念/容器化"
  - "笔记/概念入门"
---
# Docker 基础概念

## Docker 是什么？

Docker 是一个**容器化平台**，用来打包、分发和运行应用程序。

### 解决的问题

| 传统方式 | Docker 方式 |
|---------|------------|
| 在电脑上安装 Python 环境 | Docker 帮你准备好的"干净房间"里跑 |
| 版本可能和其他项目冲突 | 跟其他项目完全隔离 |
| 换个电脑又要重新配置环境 | 镜像一份，哪里都能跑 |
| 卸载可能留残留 | 容器一删，干干净净 |

### 类比

> Docker 就像给每个程序发一个**独立集装箱**，里面有自己的工具和环境，互不干扰。

---

## 三个核心概念

### 1. 镜像 (Image)

- **定义**：一个只读的模板，包含运行应用程序所需的一切（代码、依赖、环境配置）
- **类比**：菜谱（告诉你怎么建）
- **特性**：不可变，构建后不能修改

### 2. 容器 (Container)

- **定义**：镜像的"实例"，一个正在运行的隔离环境
- **类比**：按照菜谱做出来的菜，正在吃的那碗
- **特性**：可创建、启动、停止、删除

### 3. 仓库 (Registry)

- **定义**：存放镜像的地方，最常用的是 Docker Hub
- **类比**：菜市场，去买别人做好的菜谱（镜像）
- **常见仓库**：
  - Docker Hub（官方公共仓库）
  - 阿里云容器镜像服务
  - 自建私有仓库

---

## 生活化类比总结

| 概念 | 生活例子 |
|------|---------|
| 镜像 (Image) | 泡面包装上的配料表说明书（告诉你加多少水、放什么料） |
| 容器 (Container) | 按说明书泡出来的那碗泡面（正在吃的那碗） |
| 仓库 (Registry) | 超市货架，有各种品牌的泡面（别人做好的镜像） |

---

## 常见 Docker 命令速查

```bash
# 查看 Docker 版本
docker --version

# 查看 Docker 详细信息
docker info

# 查看本地有哪些镜像
docker images

# 查看有哪些容器（包括已停止的）
docker ps -a

# 运行一个容器
docker run <镜像名>

# 交互式运行容器
docker run -it <镜像名> bash

# 启动已存在的容器
docker start <容器名或ID>

# 进入运行中的容器
docker exec -it <容器名或ID> bash

# 查看容器日志
docker logs <容器名或ID>

# 停止容器
docker stop <容器名或ID>

# 删除容器
docker rm <容器名或ID>

# 删除镜像
docker rmi <镜像名或ID>
```

---

## hello-world 例子详解

执行 `docker run hello-world` 时，Docker 发生了什么：

```
1. Docker 客户端 联系 Docker 守护进程（daemon）
2. daemon 检查本地有没有 hello-world 镜像
3. 没有找到，从 Docker Hub 拉取镜像
4. daemon 用这个镜像创建一个新容器
5. 容器执行 /hello 命令
6. 输出结果返回给客户端，显示在终端
```

---

## 补充：Windows 上的 Docker 特殊性

### Docker Desktop for Windows 架构

- Windows 上的 Docker Desktop 使用 **WSL2** 或 **Hyper-V** 创建一个 Linux 虚拟机（MobyLinuxVM）
- 容器实际上是运行在这个虚拟机里的 Linux 系统
- 容器文件存在虚拟机的虚拟硬盘里，**不在 Windows 的 C:\ 盘**

### WSL2 vs Hyper-V

- **WSL2**（Windows Subsystem for Linux 2）：更轻量，推荐使用
- **Hyper-V**：更传统，某些场景下更稳定

---

_最后更新：2026-05-25_

<!-- related: managed by hermes-linkbot -->
## 相关笔记

- [[2 工具/CentOS/虚拟机快照]] — 容器 vs 虚拟机
- [[2 工具/Docker/00-Docker学习笔记导航]]
