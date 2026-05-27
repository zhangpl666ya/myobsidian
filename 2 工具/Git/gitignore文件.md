`.gitignore` 是 Git 版本控制系统中用于指定不需要纳入版本管理的文件或目录的配置文件。它的作用是告诉 Git 哪些文件应该被忽略，不被跟踪（track），从而避免这些文件被误提交到代码仓库中，保持仓库的整洁和专注。

### **核心作用**

1. **排除临时文件**：如编译生成的 `.class`、`.o` 文件，日志文件（`.log`），缓存文件等。
2. **排除个人配置**：如 IDE 生成的项目配置（`.idea/`、`.vscode/`）、本地环境变量文件（`.env.local`）等。
3. **保护敏感信息**：如包含密码、密钥的文件（`config.ini` 中的私密配置），避免泄露到公开仓库。
4. **减少仓库体积**：排除大文件（如数据库备份、视频等），避免仓库臃肿。

### **基本规则**

`.gitignore` 文件通过**模式匹配**来指定需要忽略的文件 / 目录，常用规则如下：

|规则示例|说明|
|---|---|
|`*.log`|忽略所有以 `.log` 结尾的文件|
|`tmp/`|忽略名为 `tmp` 的目录（及其下所有内容）|
|`build`|忽略名为 `build` 的文件或目录（若为目录，需确保末尾无 `/` 时也能匹配）|
|`!important.log`|否定匹配：不忽略 `important.log`（覆盖前面的 `*.log` 规则）|
|`src/*.txt`|只忽略 `src` 目录下的 `.txt` 文件，不忽略子目录中的 `.txt`|
|`src/**/*.txt`|忽略 `src` 目录及其所有子目录中的 `.txt` 文件（`**` 表示任意层级目录）|
|`# 这是注释`|以 `#` 开头的行是注释，会被 Git 忽略|
|`*.swp`|忽略 Vim 编辑器的临时交换文件|
|`.idea/`|忽略 IntelliJ IDEA 的配置目录|

### **使用方式**

1. **创建 `.gitignore` 文件**
    
    在 Git 仓库的根目录（与 `.git` 文件夹同级）创建一个名为 `.gitignore` 的文件，然后写入上述规则。
    
    示例内容：
```gitignore
    # 忽略日志文件
    *.log
    
    # 忽略编译目录
    dist/
    build/
    
    # 忽略 IDE 配置
    .idea/
    .vscode/
    *.sublime-*
    
    # 忽略环境变量文件
    .env.local
    .env.*.local
    
    # 不忽略关键配置（否定规则）
    !.env.example
```
    
2. **生效范围**
    
    - `.gitignore` 只对**未被跟踪**的文件有效。如果文件已被 `git add` 或 `git commit` 过（即已纳入版本管理），修改 `.gitignore` 不会自动忽略它，需要先移除跟踪：
        

        
```bash
# 移除文件的跟踪（但不删除本地文件）
git rm --cached 文件名
# 提交修改
git commit -m "移除已跟踪的忽略文件"
```


### **全局 `.gitignore`**

如果某些规则（如个人编辑器配置）需要在所有 Git 仓库中生效，可以配置**全局 `.gitignore`**：

1. 创建全局忽略文件（如 `~/.gitignore_global`）。
2. 配置 Git 识别该文件：
```bash
   git config --global core.excludesfile ~/.gitignore_global
```


### **注意事项**

- 区分**文件**和**目录**：目录名后加 `/`（如 `tmp/`）可明确指定忽略目录，避免误判为文件。
- 否定规则（`!`）的优先级：后出现的规则会覆盖前面的冲突规则。
- 不要忽略必要的配置模板：例如 `.env.example`（不含敏感信息的示例配置）应该提交，方便他人参考。
- 部分项目有通用模板：如 Java 项目可使用 `*.class`，Python 项目可使用 `__pycache__/`、`*.pyc` 等，可参考 [GitHub 的 `.gitignore` 模板库](https://github.com/github/gitignore)。

通过合理配置 `.gitignore`，可以有效提升 Git 仓库的管理效率，避免不必要的文件干扰。


下面是用于obsidian的.gitignore文件，复制进去就行了

```gitignore
# 系统自动生成的文件
.DS_Store          # Mac系统文件
Thumbs.db          # Windows缩略图缓存
*.lnk              # Windows快捷方式

# 编辑器/工具临时文件
*~                 # 各种编辑器的备份文件（如Vim、VS Code）
.*.swp             # Vim交换文件
.*.swo             # Vim交换文件（二次保存）
*.tmp              # 临时文件
*.bak              # 备份文件
*.cache            # 缓存文件

# Obsidian自身生成的非必要文件
.obsidian/workspace          # 工作区配置（包含本地窗口布局等）
.obsidian/workspace.json     # 工作区JSON配置
.obsidian/cache/             #  Obsidian缓存目录
.obsidian/themes/            # 主题文件（如需同步主题可删除此行）
.obsidian/snippets/          # CSS代码片段（如需同步可删除此行）
.obsidian/app.json           # 应用配置（包含本地路径等）
.obsidian/community-plugins.json  # 插件列表（插件文件已在plugins目录保留）

# 只保留插件目录（忽略.obsidian下其他文件，但保留plugins）
.obsidian/*                  # 先忽略.obsidian下所有内容
!.obsidian/plugins/          # 但不忽略plugins目录
!.obsidian/plugins/**/*      # 不忽略plugins目录下的所有文件和子目录

# 其他可能的非笔记文件（根据需要调整）
*.exe
*.dll
*.zip
*.rar
*.7z
```
