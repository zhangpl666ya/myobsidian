Review：
Hash Table：
- `build(x)` in $O(n_{(e)})$
- `find(x)` in $O(1_{(e)})$
- `insert(x) delete(k)` in $O(1_{(a)(e)})$
- `find_min find_max find_prev find_mext` in $O(n)$

既然通过哈希可以将查找效率降到常数，那么排序呢？

# 1️⃣比较模型的极限
通过比较模型的决策树：
- 每次返回两个值：True or False， 树节点分两个叉
- 共有$n!$种结果，故叶节点有$n!$ 个
- 树高就是$O(nlogn)$ 水准
- merge sort就是最好的了

# 2️⃣直接访问数组排序
- 将n个元素数组按顺序排在一个零到u-1的容器中（元素最大值为u），索引就是其键值
- 然后再按顺序取出来就可以排好序了

```python
def direct_access_sort(A):
	u = 1 + max([x.key for x in A])
	D = [None] * u
	for x in A:
		D[x.key] = x
	i = 0
	for key in range(u):
		if D[key]:
			A[i] = D[key]
			i += 1
```


但是若有很多重复的怎么办呢？

## counting sort

我们创建的新列表元素变成链表，存储多个值即可

```python
def counting_sort(A):
	u = 1 + max([x.key for x in A])
	D = [None] * u
	for x in A:
		D[x.key].append(x)
	i = 0
	for chain in D:
		for x in D:
			A[i] = x
			i+=1
```

- 时间复杂度分析：
	- 创建一个D消耗$O(u)$
	- 遍历一遍A消耗$O(n)$
	- 遍历一遍D消耗$O(n)$
	- 总时间复杂度为$O(n+u)$
# 3️⃣Radix sort
这样是很好，但若u非常大那不就炸了？
这时候就需要哈希一下

以$u<n^{2}$ 举例：
- 存储一个元组，包含两个数a ，b，其中`a,b = divmod(x,n)`
- `divmod(x,n)`返回两个数，一个整除和一个余数
- 这样就将一个比较大的数哈希成一个数组（也是n进制下数的大小）
- 先对低位计数排序，再对高位计数排序
- 这种情况下，$u = O(n)$, 时间复杂度降为$O(n)$

讨论$u < n^{c}$ ：
- 分成包含c个元素的 数组，进行c次计数排序
- 时间复杂度$O(n+nlog_{n}u)\  =\ O(n)$

```python
def counting_sort(A):
	pass

def radix_sort(A):
	n = len(A)
	u = 1 + max([x.key for x in A])
	c = 0
	k = 1
	while k < u:
		k = k * u
		c += 1
	class Obj : pass
	D = [Obj() for a in A]
	for i in range(n):
		D[i].item = A[i]
		D[i].digits = []
		a = A[i].key
		for _ in range(c):
			a, b = divmod(a,n)
			D[i].digits.append(b)
	for i in range(c):
		for j in range(n):
			D[j].key = D[j].digits[i]
			counting_sort(D)
	for i in range(n):
		A[i] = D[i].item
```