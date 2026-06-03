> 以下都用np代替Numpy
## 用Numpy处理原始/日志数据
与C++`std::vector`不同，np底层数据结构是连续的，可以较为简便的处理多维数据，这种内存块叫`ndarray`
```python
import numpy as np

# Department 1: Manual entry of Q1 monthly sales (Jan, Feb, Mar)
dept1_sales = np.array([20, 30, 15]) 

# Department 2: Automatically generating a sequence of sales numbers 
# Let's say it linearly increments from 15 to 25 over 3 months
dept2_sales = np.linspace(15, 25, 3) 

print("Dept 1 Array:", dept1_sales)
print("Dept 2 Array:", dept2_sales)

print(f"Data type: {dept1_sales.dtype}") # Similar to checking primitive types
print(f"Dimensions: {dept1_sales.ndim}") # Is it 1D, 2D, etc.
print(f"Shape: {dept1_sales.shape}")     # Tuple of dimensions (size along each axis)
print(f"Total elements: {dept1_sales.size}")
```
- 用`np.array([...])`构建ndarray
- `np.linspace(start, end, step)`创建一个一维ndarray，从start开始到end结束，共step个数，发现此时数据类型为float
- `.dtype`展示这个ndarray元素的类型
- `.ndim`展示这个ndarray的维度
- `shape`展示这个ndarray的形状，一维（1，），二维比如（2，3）
- `.size`返回这个ndaray的元素数量

## 结合和修改数据
```python
import numpy as np

# Let's rebuild our initial rows cleanly
dept1 = np.array([20, 30, 15])        # Int array
dept2 = np.array([15.0, 20.0, 25.0]) # Float array

# Vectorized operation: Multiply all element values instantly!
double_dept1 = dept1 * 2 [cite: 10]
print("Vectorized multiplication (* 2):", double_dept1) [cite: 10]

# Now let's stack these 1D arrays horizontally to create a single 2D matrix
# We will use np.array() passing a list of our rows
sales_matrix = np.array([dept1, dept2]) [cite: 4]

print("\n--- Our 2D Sales Matrix ---")
print(sales_matrix)
print("New Shape:", sales_matrix.shape) # Output will be (2, 3) -> 2 rows, 3 columns
print("Unified Data Type:", sales_matrix.dtype)
```
- 直接用* 2可以翻倍所有数据
- 一维的ndarray会被解包，然后被当作两个元组合成一个高维数据结构，这个过程中基础数据结构提升统一

### 查询与过滤
生成一个布尔掩码，