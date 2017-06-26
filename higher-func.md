# 高阶函数学习笔记

#### 把函数作为参数传入，这样的函数称为高阶函数
#### 函数式编程就是指这种高度抽象的编程方式

#### 一个简单的高阶函数：
```python
'高阶函数'
>>> def absum(a,b,f):
...     return f(a)+f(b)
... 
>>> absum(-1,3,abs)
4
```
#### Python内建的高阶函数
	* map/reduce
		+ map(function,iterable...) 通过指定的函数对序列做映射
			- 简单的例子：
			```python
			>>> def f(x):
			...     return x*x
			... 
			>>> list1=[i for i in range(5)]
			>>> r = map(f,list1)
			>>> list(r)
			[0, 1, 4, 9, 16]
			```
		+ reduce(function,iterable[,initializer])对参数序列中的元素进行累积
			- 注：function必须是两个参数
			- 看下面的例子：
			```python
			>>> from functools import reduce
			>>> def add(x,y):
			...     return x+y
			... 
			>>> reduce(add,[i for i in range(10)])
			45
			```
			- 也可以用闭包函数
			```python
			>>> reduce(lambda x,y:x+y,[i for i in range(10)])
			45
			```
	* filter(function,iterable)用于过滤序列
		+ 选择10以内的偶数
		```python
		>>> def odd(x):
		...     return x%2==0
		... 
		>>> f=filter(odd,[i for i in range(11)])
	    >>> list(f)
	    [0, 2, 4, 6, 8, 10]
		```

	* sorted(iterable,key,reverse)对序列进行排序
		+ 默认排序
		```python
		>>> list1=[1,-2,-3,4,5,6,-7,8,-9]
		>>> sorted(list1)
		[-9, -7, -3, -2, 1, 4, 5, 6, 8]
		```

		+ 按照元素的绝对值进行排序
		```python
		>>> sorted(list1,key=abs)
		[1, -2, -3, 4, 5, 6, -7, 8, -9]
		```

		+ 反向排序
		```python
		>>> sorted(list1,reverse=True)
		[8, 6, 5, 4, 1, -2, -3, -7, -9]
		>>> sorted(list1,key=abs,reverse=True)
		[-9, 8, -7, 6, 5, 4, -3, -2, 1]
		```






