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
```
- 这里先准备表格数据`sales_data`
- 然后用list由上到下存储每一行的名字
- 用list存储每一列的名字
- 创建一个DataFrame需要三个参数，