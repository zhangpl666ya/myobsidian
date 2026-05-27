`git checkout` 是 Git 中一个多功能的命令，主要用于切换分支、恢复文件、创建分支等操作，具体功能如下：

### 1. **切换分支**

切换到已存在的分支：

bash

```bash
git checkout <分支名>
```

例如，切换到 `main` 分支：

bash

```bash
git checkout main
```

### 2. **创建并切换到新分支**

结合 `-b` 选项，可快速创建新分支并立即切换到该分支（相当于 `git branch <新分支名>` + `git checkout <新分支名>`）：

bash

```bash
git checkout -b <新分支名>
```

例如，创建并切换到 `feature/login` 分支：

bash

```bash
git checkout -b feature/login
```

### 3. **恢复工作区文件**

将工作区中修改的文件恢复到**暂存区（index）** 的状态（若文件未暂存，则恢复到最近一次提交的状态）：

bash

```bash
git checkout -- <文件名>
```

例如，丢弃对 `app.js` 的修改：

bash

```bash
git checkout -- app.js
```

⚠️ 注意：此操作会直接覆盖工作区的修改，且无法恢复，使用前需谨慎。

### 4. **从特定提交 / 分支恢复文件**

从指定的提交（或分支）中获取文件并覆盖工作区和暂存区的对应文件：

bash

```bash
git checkout <提交ID/分支名> -- <文件名>
```

例如，从 `dev` 分支恢复 `utils.js` 到当前工作区：

bash

```bash
git checkout dev -- utils.js
```

### 5. **切换到特定提交（分离头指针状态）**

切换到历史中的某个具体提交（脱离分支，进入 “分离头指针” 状态），用于查看或基于该提交进行操作：

bash

```bash
git checkout <提交ID>
```

例如，切换到提交 `a1b2c3d`：

bash

```bash
git checkout a1b2c3d
```

⚠️ 注意：在此状态下的修改若未创建新分支保存，切换回其他分支后可能丢失。

### 注意事项

- Git 2.23+ 版本引入了 `git switch` 和 `git restore` 命令，分别替代 `git checkout` 的分支切换和文件恢复功能，使命令语义更清晰。例如：
    - 切换分支：`git switch <分支名>`
    - 创建并切换分支：`git switch -c <新分支名>`
    - 恢复文件：`git restore <文件名>`
- 但 `git checkout` 仍被广泛使用，尤其在需要兼容旧版本 Git 的场景中。