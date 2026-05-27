# 1️⃣Sorted Array
sorted array 有很多优势，比如：
- 通过二分查找[^1]时间复杂度达到O（logn）
- `find_min`和`find_max`时间复杂度为O（1）

[^1]: 对于一个有序的数组，取中间值，若比需要的值大，就往前找，反之向后找，在迭代直到找到或遍历完没找到

但是怎么最高效的排序呢？

# 2️⃣sorting

一些基本排序方法：

## 1. Permutation Sort
- 对于A有n！个可能的排序，找需要的那个（这个方法蠢到我了）

```python
def permutation_sort(A):
	'''sort A'''
	for B in permutations(A):
		if is_sorted(B):
			return(B)
```

- 复杂度分析：
	- 尝试所有排序，时间为n！
	- 判断是否是需要的那个排序，时间n
	- 所以这个算法时间O(n* n!)  :(

## 2. Selection Sort
- 选择排序就是在前n个中找到最大的那个，然后放到最后面，在对前n-1个重复操作
- 这个就有一递归的感觉了
```python
def selection_sort(A,i = None):
	if i is None: i = len(A) - 1              #如果没有给i这个参数，默认全部排列
	if i > 0:                                 #如果i>0, 即有两个以上元素 
		max_idx = pre_max(A,i)                #找到前0-i中最大那项的索引
		A[max_idx], A[i] = A[(i], A[max_idx]  #交换
		selection_sort(A,i - 1)               #进行下一个迭代

def pre_max(A,i):
	#return index of maximum in A[:i+1]
	if i > 0:                                 #若有两个以上元素
		j = pre_max(A,i-1)                    #j等于0-（i-1）中最大那项的索引
		if A[j] > A[i]                        #选i和j中更大那个
			return j
	return i

```
- pre_max复杂度分析：
	- Base case： i= 0时，只有一个元素，时间为0
	- Induction：假设前i个排好了，最大的那个只会是前i个或第i+1个
	- $S(i) = \theta(i), \ S(n) = S(n-1) + \theta(1)$
	- 容易分析S（n） = Θ（n），通过带入验证或递归树很好证明

- `selection_sort`复杂度分析：
	- 对于只有一个元素，时间复杂度为Θ（1）
	- 若后n-i个排好了，遍历i找到前i个最大的，时间Θ（i），再调换，时间Θ（1）
	- $S(1) = \theta(1), \ S(n) = S(n-1)+\theta(n)$
	- 递归树或带入验证可知S(n) = Θ（$n^2$）

## 3. Insertion Sort
- 从左到右一个一个比，若左边比右边大就交换位置
- 递归处理
```python
def insertion_sort(A,i = None):
	if not i : i = len(A) - 1
	if i > 0:
		for j in range(i):
			if A[j] < A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
		insertion_sort(A, i-1)
```
- 复杂度分析：
	- 若只有一个元素，时间复杂度为常数
	- $S(1) = \theta(1), \ S(n) = S(n-1)+ \theta(n)$
	- S(n) = Θ（$n^{2}$）

## 4.Merge sort
- 递归地将前半部分和后半部分排序
- 再通过双指针法，将两部分合并在一起
- 双指针法是非常好的方法，能巧妙的将O($n^{2}$)转化为O（n）复杂度
	- 当出现反复遍历的情况，考虑双指针法
```python
def merge_sort(A):
	if len(A) > 1:
		c = len(A) // 2
		left = merge_sort(A[:c])
		right = merge_sort(A[c:])
		merge(A,left, right)
		
def merge(A,left,right):
	n = len(left)
	m = len(right)
	i, j, k, t = 0,0,0,0
	while i + j < n+m:
		if i = n:
			t = right[j]
			j += 1
		if j = m:
			t = left[i]
			i+=1
		if i != n and j != m:
			if left[i] < right[j]:
				t = left[i]
				i+=1
			else:
				t = right[j]
				j+=1
		A[k] = t
		k+=1
```
- merge_sort复杂度分析：
	- 对于只有一个元素的情况下，时间复杂度为O(1)
	- 递归树：$T(n) = 2T\left( \frac{n}{2} \right) + O(n)$
	- 带入$T(n) = O(nlogn)$ 成立，所以时间复杂度为O（nlogn）

# 3️⃣Master Theorem主定理

对于$T(n) = aT(n/b) + f(n)$形式的复杂度分析：
1. 若$O(n^\left(log_b a\right)) < O(f(n))$：$T(n) = O(f(n))$
2. 若$O(n^\left(log_b a\right)) = O(f(n))$：$T(n) = O(f(n)*logn)$
3. 若$O(n^\left(log_b a\right)) > O(f(n))$：$T(n) = O(n^\left(log_b a\right)*logn)$
