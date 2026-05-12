用逐步探查法——像剥洋葱一样一层层看：
```python

import requests
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello')
data = response.json()
# 第1步：看整体类型
print(type(data))              # <class 'list'> - 是列表
# 第2步：看长度
print(len(data))               # 1 - 列表里有一个元素
# 第3步：看第一个元素的键
print(data[0].keys())          # dict_keys(['word', 'phonetics', 'meanings', ...])
# 第4步：看中意的键的内容
print(data[0]['meanings'])     # 列表，有3个元素
# 第5步：看具体某个元素
print(data[0]['meanings'][0])  # {'partOfSpeech': 'noun', 'definitions': [...]}
# 第6步：看更深层
print(data[0]['meanings'][0]['definitions'][0])  # {'definition': '...', ...}

```

核心技巧：
- type(x) — 看清类型（dict / list / str）
- len(x) — 看长度
- dict.keys() — 看所有键
- list[0] — 按索引取值
- 一层层往下走，不要跳步