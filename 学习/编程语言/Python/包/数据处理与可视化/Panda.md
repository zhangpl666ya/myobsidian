`panda`以下简称pd
其用一种数据结构`DataFrame`来存储数据，这是一张二维表格，想象成excel表格，每一列像一维数组一样处理，叫做`series`

# 创建和观察DataFrame
```python
import pandas as pd

# 1. Prepare raw matrix values (mixed tracking data)
sales_data = [
    ['Dept-A', 150, 115.5],
    ['Dept-B', 200, 87.0],
    ['Dept-C', 100, 60.5],
    ['Dept-D', 112, 140.0]
]

# 2. Define row identifiers and column descriptions
store_names = ['Store_1', 'Store_2', 'Store_3', 'Store_4']
metrics = ['Department', 'Units_Sold', 'Profit_Margin']

# 3. Create the unified DataFrame
df = pd.DataFrame(data=sales_data, index=store_names, columns=metrics)

print("--- Our Pandas Sales Dashboard DataFrame ---")
print(df)

print("\nRow Indexes:", list(df.index))      # Access row names 
print("Column Names:", list(df.columns))   # Access column attributes 
print("Raw NumPy Matrix Behind It:\n", df.values) # Extracts underlying ndarray 
print("Underlying Type of Matrix Values:", type(df.values)) #
```
- 这里先准备表格数据`sales_data`
- 然后用list由上到下存储每一行的名字
- 用list存储每一列的名字
- 创建一个DataFrame需要三个参数，这些东西的size要对齐。
- 用`df.index`和`df.columns`获取行列名称。

# 行列操作
```python
units = df['Units_Sold']

# --- Fixing the Series Access Error ---
print("Using .iloc for absolute location position:", units.iloc[0]) # Fixes your KeyError!
print("Using .loc for explicit string labels:", units.loc['Store_1'])

# --- DataFrame Rows Querying ---
print("\n--- Extracting Full Data Rows ---")
# Get entire row data for Store_2 as a Series
store2_row = df.loc['Store_2'] [cite: 9]
print("Store_2 Row via .loc:\n", store2_row)

# Get the same exact data by index sequence row number 1
store2_row_idx = df.iloc[1]
```
- 可以用中括号的行列名获取行、列，**但是中括号不支持索引提取！**
- 用`.loc[] .iloc[]`分别通过字符串和索引获取行列

