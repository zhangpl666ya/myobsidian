 Insert Mode
* 也就是所谓的编辑模式，插入模式
* 此模式下，可以对文本内容进行自由编辑
 [[Vim#Command Mode|Command Mode]]
 *  以“：”开始，通常用于文件的批量操作、保存与退出

![[vim模式示意图]]



## Normal Mode 

如果需要通过vi/vim编辑器编辑文件，通过一下命令（仅限[[bash]]）：
```
vi 文件路径
vim 文件路径
```
* 如果文件路径表示的文件不存在，此命令用于编辑新文件
* 如果文件存在，编辑已有文件

用vim命令编辑文件，会打开新窗口，此时窗口是Normal Mode

* 按下i键，进入Insert Mode
* 按：进入Command Mode



### 进入Insert Mode

| 命令    | 描述                  | 助记             |
| ----- | ------------------- | -------------- |
| `i`   | 在当前光标位置进入==Insert Mode==   | insert         |
| `a`   | 在当前光标位置之后进入==Insert Mode== | append         |
| `I`   | 在当前行的开头进入==Insert Mode==   |                |
| `A`   | 在当前行的结尾进入==Insert Mode==   |                |
| `o`   | 在当前光标下一行进入==Insert Mode==  | open a new row |
| `O`   | 在当前光标下一行进入==Insert Mode==  |                |
| `s`   | 删除当前光标字符，进入==Insert Mode== |                |
| `S`   | 删除当前光标行，进入==Insert Mode==  |                |
| `esc` | 任何情况下输入都能回到==Normal Mode== |                |
### 基本移动
* `hjkl`：上下左右移动光标
* `gg`：跳到第一行
* `G`：跳到最后一行
* `<ctrl-u>/<ctrl-b>`：往上翻半页/一页
* `<ctrl-d>/<ctrl-f>`：往下翻半页/一页
* `{lineno}gg`：跳到第lineno行
* `zz/zt/zb`：光标行设置为屏幕居中/屏幕第一行/屏幕最后一行

### 基于单词的移动
* `w`：word，跳转到下一个单词的开头
* `b`：back，跳转到上一个单词的开头
* `e`：end，跳转到下一处单词的结尾
* `ge`：e的反向，跳转到上一处单词的结尾
wbe大写版本WBE对应单词是连续的非空字符，会跳过空格和标点

### 基于搜索的移动
行内搜索：
* `f{char}/t{char}`：跳转到本行下一个char字符出现处/出现前
* `;/,`：快速向后/向前重复ft查找
* `F{char}/T{char}`：往前搜索
文件中搜索：
* `/{pattern}`：跳转到本文件中下一个出现pattern的地方
* `?{pattern}`：跳转到本文件中上一个出现的地方
* ``：可以是正则表达式
* `*`：跳转到下一个当前光标所在的词出现的位置
* `nN`：快速重复查找，N是反向查找

### 基于标记的移动
* `m{mark}`：把当前位置标记为mark
* `反引号+{mark}`：跳转到名为mark的标记位置
mark是a-z字符
内置标记：
* `反引号+反引号`：回到上次跳转的位置
* `反引号+.`：上次修改的位置
* `反引号+^`：上次插入的位置
其他跳转：
* `0/$`：跳转到本行的开始结尾
* `%`：跳转到匹配的配对符
### Operator+Motion=Action
{operator}{motion}：一次编辑动作
常见操作符：
* `c`：代表change，修改，删除内容并进入编辑模式
* `d`：代表delete，删除
* `y`：代表yank，复制
* `v`：代表visual，选中文本，进入可视模式
例子
* `dgg`：删除到第一行
* `ye`：复制到单词结尾
* `d$`：删除到行尾
* `dt;`：删除到分号为止的东西
大部分操作符按两次：将其作用在这一行上

### 批量操作：数字+动作
{count}{action}：重复count次action动作
动作可以是移动动作或是编辑动作
* 4j：向下4hang
* 3dw：删除3个单词
* 2yy：复制两行
* 4p：粘贴4次

### 文本对象操作
textobjects：语义化的文本片段
格式：i/a+对象
常见对象：
* w/W，s，p：单词，句子，段落
* （/），【/】，{/}，‘/“：配对符
i代表inner；a额外包括周围的空格或配对符

`[count]{operator}{textobjects}`
* `diw`:删除一个单词
* `ci(`：修改小括号内部
* `yi{`：复制大括号内部

### 操作符与命令补充
* `gu/gU/g~`：操作符，转小写/转大写/翻转大小写
* `J`：join，链接两行
* `<ctrl-a>/<ctrl-x>`：增加数字/减少数字
* `g<ctrl-A>`：创建递增序列
* `</>`：左/右缩进

### visual模式
按v可进入visual模式
进入visual模式后可以使用Normal Mode下的移动命令移动
* x：剪切
* y:复制；回到Normal Mode按p粘贴
esc回到Normal Mode

### 寄存器
vim提供了许多寄存器用于存放内容，可以理解为剪贴板，一个字符对应一个寄存器

特别的寄存器：
* “：默认寄存器，平时复制、删除的内容都在里面
* %：当前文件名
* .：上一次插入的内容
* : ：上一次执行的内容

通过`:h register`查看所有寄存器种类
通过`:reg {register}`查看对应寄存器中的内容

在复制删除粘贴等操作前加上”{register}就可以指定本次操作所用的寄存器
只要涉及寄存器操作的都可以这样指定
* "ayy：将这一行复制到a寄存器中
* "bdiw：将单词删除，保存到b寄存器中
* "cp：将c寄存器中的内容粘贴出来
寄存器字符大写：添加（append）至寄存器而非覆盖


### 宏
宏（macro）：录制一系列键盘操作，并允许重放这些操作
操作序列保存在指定寄存器中
* `q{register}`：开始录制宏，存在寄存器register中
* 录制过程按q退出录制
* `@{register}`：重放寄存器register中的操作
* @@：重放上一次宏操作
***注意：`.`命令对宏不生效
### 建议：让你的命令更模块化
尽量让命令模块化，具有清晰的含义与作用范围，以便与 `.`等命令协同


---

## Command Mode

### Ex命令格式
`:[range][excommand][args]`
* range：作用范围，不给的话就默认本行
* excommand：特殊命令
* args：后续参数

一些Excommand（[x]是寄存器，可选）
* `:[range] copy {address}`：把range中的行复制到address后面
* `:[range] move {address}`：把range中的行移动到address后面
* `:{address} p [x]`：把寄存器x的内容粘贴到address后面
* `:[range] d [x]`：删除range中的行（到寄存器x）
* `:[range] y [x]`：复制range中的行（到寄存器x）

range与address：指定范围
range由两个address构成，即{address}或{address},{address}
address可以是：
* {lineno}：行号（零代表第一行上面的虚拟行）
* $：最后一行
* . ：光标所在行
* /{pattern}/：下一个pattern所在的行
address可以做加减法，.+3表示光标向下第三行，$-3表示倒数第四行

### 批量操作
normal命令
格式：`:[range] normal {command}
含义：对range中的所有行执行Normal Mode下的命令command
* 将range设置为%，可以对文件的所有行执行
* `:[range] normal .`：配合`.`命令
* command可以是宏记录的操作 `:[range] normal @{register}`
```vim
:1,10normal A;

:%normal ^x

```

global命令
格式：`:[range] global/{pattern}/[cmd]`
含义：对range中包含pattern的所有行执行Ex命令
	normal也是Ex命令，不给默认为打印
	`:[range] global/{pattern}/normal{command}`
```vim
:g/^$/normal i-- 分隔线 -- 

:g/^print/normal A;
```
### 替换命令
`:[range]s/{pattern}/{string}/[flags]`
将pattern替换为string
flags：
* g：替换每一行的所有匹配
* i：忽略大小写
* c：替换前进行确认
* n：计数而不是替换
`:%s/Vim//gn`统计文件中所有Vim出现的次数

### 外部命令
1. : ! command用于执行一个外部命令
2. : w FILENAME 可将当前Vim中正在编辑的文件保存到名为FILENAME的文件中
3. v motion : w FILENAME可将当前编辑文件中可视模式下选中的内容保存到文件FILENAME中
4. : r FILENAME可提取磁盘文件FILENAME并将其插入到当前光标位置后面
5. : r ! dir 可以读取dir命令的输出并将其放置到当前文件的光标后面

| 命令                    | 描述     | 助记     |
| --------------------- | ------ | ------ |
| ：wq                   | 保存并提出  |        |
| ：q                    | 仅退出    | quit   |
| ：q！                   | 强制退出   |        |
| ：w                    | 仅保存    |        |
| ：set number           | 显示行号   |        |
| ：set relativenumber   | 开启相对行号 |        |
| ：set norelativenumber | 关闭相对行号 |        |
| ：set paste            | 设置粘贴模式 |        |
| ：%s/旧内容/新内容/g         | 全局替换文本 | global |
设置粘贴模式确保从外面复制的内容粘贴不会有格式错乱





