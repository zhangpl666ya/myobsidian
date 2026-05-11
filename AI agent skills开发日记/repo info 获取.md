# requests库
requests库用于发送网页请求，可以获取和上传：

## API调用
是HTTP请求的一种，专门用于信息的传输而不是给人看。
一般API的网站和官网名字不一样
使用`requests.get("url")`获得的是JSON字典列表
可用JSON解析将其转化为python字典列表


```python
r = requests.get("url")
data = r.json()
#获取
requests.post("url",data = data)
#上传
```