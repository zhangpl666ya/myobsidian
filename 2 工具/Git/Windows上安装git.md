
### **步骤 1：下载 Git 安装包**

首先访问 Git 官方下载页面，获取适用于 Windows 的安装程序：

👉 官方下载地址：[https://git-scm.com/download/win](https://git-scm.com/download/win)

打开页面后，网站会自动识别你的系统（Windows 11），并开始下载最新版本的安装包（通常是 `.exe` 文件，如 `Git-2.45.0-64-bit.exe`）。

### **步骤 2：运行安装程序**

找到下载好的 `.exe` 文件（默认在 “下载” 文件夹），双击运行。此时会弹出安装向导，按以下步骤选择配置：

#### **选项 1：选择安装路径**

默认路径为 `C:\Program Files\Git`，建议保持默认（无需修改），点击「Next」。

#### **选项 2：选择组件（Components）**

这一步建议保留默认选项，额外推荐勾选以下实用功能：

- **Add a Git Bash Profile to Windows Terminal**（如果使用 Windows Terminal，会添加 Git Bash 终端）
- **On the Desktop**（创建桌面快捷方式，方便快速打开 Git Bash）

其他默认选项（如 `Git LFS`、`Associate .git* files with Git` 等）无需改动，点击「Next」。

#### **选项 3：选择开始菜单文件夹**

默认即可，直接点击「Next」。

#### **选项 4：选择默认编辑器（Default Editor）**

Git 需要一个编辑器来处理提交信息、配置文件等。默认是「Vim」（新手可能不熟悉），推荐更易上手的编辑器：

- 如果你安装了 **VS Code**，选择「Use Visual Studio Code as Git's default editor」
- 或选择「Notepad++」（需提前安装）

选择后点击「Next」。

#### **选项 5：调整 PATH 环境变量（关键）**

这一步决定 Git 能否在命令提示符（CMD）、PowerShell 中直接使用，推荐选择：

👉 **Git from the command line and also from 3rd-party software**（允许在所有终端中调用 Git 命令）

点击「Next」。

#### **选项 6：选择行结束符（Line Endings）**

Windows 和 Linux 的换行符格式不同，默认选项「Checkout Windows-style, commit Unix-style line endings」是跨平台协作的最佳选择（避免文件换行符冲突），直接点击「Next」。

#### **选项 7：选择终端模拟器（Terminal Emulator）**

推荐保留默认的「Use MinTTY」（Git 自带的终端，支持右键粘贴、全屏等功能，比 Windows 默认终端更友好），点击「Next」。

#### **后续选项**

剩余选项（如「Default behavior of `git pull`」「Credential helper」等）保持默认即可，一路点击「Next」或「Install」，等待安装完成。

### **步骤 3：验证安装是否成功**

安装完成后，验证 Git 是否正常工作：

1. 按下 `Win + R`，输入 `cmd` 打开命令提示符（或打开 PowerShell、Git Bash）
2. 输入命令：
    
    bash
    
    ```bash
    git --version
    ```
    
3. 如果输出类似 `git version 2.45.0.windows.1` 的版本信息，说明安装成功。

### **步骤 4：初次配置（必须）**

Git 需要你的用户名和邮箱来标识提交记录，打开终端（CMD/PowerShell/Git Bash），输入以下命令（替换为你的信息）：

bash

```bash
# 设置用户名（如你的GitHub昵称）
git config --global user.name "Your Name"

# 设置邮箱（如你的GitHub注册邮箱）
git config --global user.email "your.email@example.com"
```

可以通过以下命令检查配置是否生效：

bash

```bash
git config --global --list
```

### 常见问题解决

- 如果输入 `git` 命令提示 “不是内部或外部命令”，说明 PATH 环境变量配置失败，重新运行安装程序，在「步骤 5」中确认选择了正确的 PATH 选项。
- 推荐日常使用「Git Bash」（安装后在开始菜单或桌面可找到），它支持 Linux 风格的命令（如 `ls`、`cd`），更适合 Git 操作。

至此，Windows 11 上的 Git 就安装配置完成了，可以开始使用 Git 进行版本控制了！