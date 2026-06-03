> 以下都用np代替Numpy
## 用Numpy处理原始/日志数据
与C++`std::vector`不同，np底层数据结构是连续的，可以较为简便的处理多维数据，这种内存块叫`ndarray`
```python
import numpy as np

dept1 = np.array([15,20,30])
dept2 = np.linspace(15,25,3)

print(dept1.dtype)
print(dept1.ndim)
print(dept1.shape)
print(dept1.size)
print(dept2.dtype)
```
- 用`np.array([...])`构建ndarray
- `np.linspace(start, end, step)`创建一个一维ndarray，从start开始到end结束，共step个数
- `.dtype`展示这个ndarray元素的类型
- `.ndim`展示这个ndarray的wei