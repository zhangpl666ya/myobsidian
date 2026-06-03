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
生成一个布尔掩码，就可以直接提取内容
```python
# Create a conditional boolean matrix
mask = sales_matrix > 22 [cite: 9]
print("\nBoolean Mask (matrix > 22):\n", mask)

# Extract only elements meeting the condition into a flattened array
high_sales = sales_matrix[mask] [cite: 9]
print("Filtered high sales elements:", high_sales) [cite: 9]
```
- 这里筛选出的结果以数组形式返回

## 数据切片与视窗
这里要分清楚拷贝与视窗的区别，一个是完全复制一遍底层数据，一个是产生一个视窗，或者说C++中的引用。ndarray与python数组不一样，python数组切片为复制，而ndarray的切片为视窗，修改是会反映在原数组上的
```python
import numpy as np

# Let's create a 4x4 matrix representing 4 stores over 4 quarters
# Using np.arange to generate sequential data from 1 to 16, then reshaping it
sales_grid = np.arange(1, 17).reshape(4, 4)

print("Original 4x4 Sales Grid:\n", sales_grid)

# Slice a sub-section: Rows 1 and 2, Columns 1, 2, and 3 
# (Remember Python indexing is 0-based and upper boundaries are exclusive)
sub_view = sales_grid[1:3, 1:4]
print("\nExtracted Sub-view (Rows 1-2, Cols 1-3):\n", sub_view)

# Modifying the view modifies the original data block!
sub_view[0, 0] = 999 

print("\nGrid after modifying sub_view:\n", sales_grid)

# Create an isolated deep copy of the slice
isolated_copy = np.copy(sales_grid[1:3, 1:4]) # 
isolated_copy[0, 0] = -55

print("\nIsolated Copy altered:\n", isolated_copy)
print("Original Grid remains untouched by copy:\n", sales_grid)
```
- `.reshape`会重组形状
- 切片以0为基数，左闭右开
- 