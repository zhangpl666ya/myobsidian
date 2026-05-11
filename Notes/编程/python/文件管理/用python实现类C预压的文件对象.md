知识补充：
- 传入时写：`s:str`是说期望s是个str，并没有强制作用
- `isinstance(object,classinfo)`：python内置函数，用于判断类型
- 支持[[上下文管理协议（with关键字]]

```python
class BufferedWriter:
	def __init__(self, filename, buffersize=4096, encoding='utf-8):
	self.file = open(filename,"w",encoding=encoding)
	self.buffer = []
	self.buffersize = buffersize
	self.buffer_len = 0
	
	def write(self, s: str):
		if not ininstance(s, str):
			raise TypeError("write() expects str")
		self.buffer.append(s)
		self.buffer_len += len(s.encode('utf-8'))
		
		if self.buffer_len >= self.buffersize:
			self._flush_buffer()	
			
	def _flush_buffer(self):
	'''这个是将自己的缓冲区写入file的python缓冲区'''
		if not self.buffer:
			return
		self.file.write("".join(self.buffer))
		self.buffer.clear()
		self.buffer_len = 0
		
	def flush(self):
	'''这个是将缓冲区写入python缓冲区再写入系统缓冲区'''
		self._flush_buffer()
		self.file.flush()
		
	def close(self):
	'''关闭文件，写入缓冲区'''
		self.flush()
		self.file.close()
		
	def __enter__(self):
		return self
		
	def __exit__(self,exc_type,exc_val,exc_tb):
		self.close()
		
```
