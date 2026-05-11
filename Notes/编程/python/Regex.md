3️⃣正则表达式简称Regex，定义在模块`re`中，用`import re`导入

# 1️⃣基础结构
## 创建regex对象
函数`re.complie()`接收一个正则表达式，返回一个正则对象：
```python
import re
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #r标记原始字符串，不转义
mo = phoneNumber.search('my phone number is 213-533-9834')
```
`phoneNumber`此时包含一个regex对象，你可以理解为正则表达式所代表的所有可能的permutations
`phoneNumber.search()`输入想要查找匹配的字符串，匹配结果存放在变量`mo`中

## 分组
在写正则表达式时，可以用括号进行分组，那前面的例子：
```python
import re
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #r标记原始字符串，不转义
mo = phoneNumber.search('my phone number is 213-533-9834')
print(mo.group())  # 213-533-9834
print(mo.group(0)) # 213-533-9834
print(mo.group(1)) # 213
print(mo.group(2)) # 533
print(mo.group(3)) # 9834

```
这样正则表达式分为三组，匹配出的mo实际上包含三个分组的匹配结果
使用`mo.group()`方法调出匹配的结果
其中：括号内的数字对应第几组，若不输入或输入零就是全部调出
使用`mo.groups()`方法（不用传入）会返回所有组的匹配，以元组形式
若括号中还有括号，那么计数先算大的，再算内部括号

# 2️⃣进阶操作
## 管道符
当希望两个或多个情况匹配一个即可，就是用管道符（相当于C/C++中的或）
```python
import re
Myfriend = re.compile(r'Alice|Bob')
mo1 = Myfriend.search('Alice went shopping')              # Alice
mo2 = Myfriend.search('Bob likes playing')                # Bob
mo3 = Myfriend.search('Both Alice and Bob hates math')    # Alice
mo4 = Myfriend.search('Carol loves math')                 # None
```
这里注意：
- 查找出现Alice或Bob都会产生结果
- 只会匹配最先出现的一个
## 问号
在分组后面添加问好实现可选匹配
```python
import re
Hero = re.compile(r'Super(wo)?man')
mo1 = Hero.search('my hero is Superman')     # Superman
mo2 = Hero.search('my hero is Superwoman')   # Superwoman
```
可以认为，问号是将该分组匹配一次或零次

## 星号&加号
在分组后面加星号匹配零次或多次
```python
import re
Ha = re.compile(r'she laughed:(Ha)*')
mo1 = Ha.search('she laughed:')               # she laughed:
mo2 = Ha.search('she laughed:HaHa!')          # she laughed:HaHa
mo3 = Ha.search('she laughted:HaHaHaHaHa!')   # she laughted:HaHaHaHaHa
```
加号的区别是匹配一次或多次，不可以是零次

## 花括号匹配特定次数
在分组后面使用花括号，可以指定匹配分组重复次数
- 可以只加一个数字，精确匹配重复次数
- 可以{a,b}，表示重复次数在{a, b}这个范围之间都满足要求
- 也可以不写前面或者后面的数字，表示没有上限或下限

# 3️⃣贪心匹配和非贪心匹配
## 贪心
匹配都是贪心的，在较短和较长都符合要求的情况下系统总是会想要最多，选长的那个，比如：
```python
Ha = re.compile(r'Ha{3,5}')
mo = Ha.search('HaHaHaHaHa')
# HaHaHaHaHa
```
在Ha重复出现五次是最多最长的，返回最复杂的匹配的版本

## 非贪心
想要系统见好就收，匹配最先满足条件的版本，就需要在后面添加问号：
- 前面我们说问号代表匹配一次或零次
- 这里的问号表示告诉系统进行非贪心匹配
```python
Ha = re.compile(r'Ha{3,5}?')
mo = Ha.search('HaHaHaHaHa')
# HaHaHa
```
这里非贪心匹配就会返回Ha最快符合条件的情况

# 4️⃣字符分类
系统提供了一些字符分类：

| 缩写字符分类 | 表示的含义                   |
| ------ | ----------------------- |
| \d     | 0-9的 数字                 |
| \D     | 除了0-9外的任意字符             |
| \w     | 任何字母、数字、下划线（理解为匹配单词的字符） |
| \W     | 除上面外的任意字符               |
| \s     | 空格、制表符、换行符（空白字符）        |
| \S     | 除空白字符外所有字符              |
| .      | 点号表示换行符外所有字符（通配符）       |
## 创建自己的字符分类
若你想有自己的分类，比如字母和数字，你可以用中括号将需要的字符列举进入，也可以使用“-”表示从哪里到哪里，这是基于ASCII码的：
```python
lower_word = re.compile(r'[A-Za-z0-9]*')
mo = lower_word.search('Hello3917_361200，welcome')
# Hello3917
```
- 提醒：由于“-”表示链接，所以不要将他作为需要匹配的字符塞在中括号中

## 插入字符和美元字符
- 在正则表达式开头写"^"表示强制匹配从开头开始的字符
- 在正则表达式末尾写“$”表示强制匹配末尾结尾的字符


# 5️⃣进阶方法
## `findall()`
前面提过`search`只会匹配第一个出现的，但如果要所有的呢？使用`findall()`可以返回所有匹配
- 若正则表达式没有分组，则用列表返回所有匹配
- 若正则表达式分组了，则列表返回所有分组匹配结果，各分组放在元组中
```python
phoneNum1 = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNum2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
content = 'you can call me at 234-573-3823 or 123-345-5678'
phoneNum1.findall(content)  # ['234-573-3823','123-345-5678']
phoneNum2.findall(content)  # [('234','573','3823'),('123','345','5678')]
```

## `sub()`
Regex对象的字符串替换方法。这个方法需要两个参数，第一个是需要替换成的字符串，第二个是要查找的对象，返回替换完成之后的字符串
```python
nameRe = re.compile(r'Agent \w+')
nameRe.sub('CENSORED','Agent Alice and Agent Bob find a secret document')
	# CENSORED and CENSORED find a secret document
```
# 6️⃣更多选项
在`search() findall()`中还可以传入一个选项。很可惜这个函数的选项位置只有一个。当然你可以用“|”来将他们同时使用
## `re.IGNORECASE` or `re.I`
这个选项可以让正则匹配忽略字母大小写
```python
Friend = re.compile(r'Alice|Bob',re.I)
Friend.findall('ALICE likes apple,but bob hates it')
# ['ALICE','bob']
```

## `re.DOTALL`
点号可以代替除换行符外所有的字符。这个选项就是可以让点号代替所有字符

## `re.VERBOSE
正则表达式是空符号敏感的，可以用这个选项让Regex对象不再敏感空符号，而是需要用\s手动匹配。我们可以用来写注释
```python
Email = re.compile(r'''
	[a-zA-Z0-9]+       #用户邮箱前缀名
	@                  #@符号
	[a-zA-Z]+          #域名
	(\.[a-zA-Z]{2,5})
	''',re.VERBOSE)
```
