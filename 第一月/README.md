# Python3学习笔记

#### python3与python2 的区别

	1、print()添加第二个参数end,如：print('hello',end='')表示不换行

#### pythonx3数据类型：	
* 标准数据类型：
	+ Number(数字)
	+ String(字符串)
	+ List(列表)
	+ Tuple(元组)
	+ Sets(集合)---Python3新增
	+ Dictionary(字典)

* 判断变量的类型：type()|isinstance()
	
	区别：
		+ type()不会认为子类是父类的类型
		+ isinstance()认为子类是父类的类型
	[详细](http://www.runoob.com/python3/python3-data-type.html)
	
* 获取对象的地址
	+ id()

* 几种遍历技巧：
	+ 遍历字典：items()
	```python
	info = {'name':'liushuaicai','age':'25'}
	for key,val in info.items():
		print(key,val)
	```
	+ 遍历列表、元组、集合
	```python
	list1 = ['hello','python']
	list2 = ['vary','good']
	for i,j in enumerate(list1):
		print(i.j)
	```
	+ 同时遍历两个或者多个序列：zip()
	```python
	for i,j in zip(list1,list2):
		print('{0}{1}').format(i,j))
	```
	+ 倒序排列
	```python
	for i in reversed(range(1,10,2)):
		print(i)
	```
	+ 给列表去重：

		set()函数

#### 迭代器和生成器
* 迭代器的两个基本方法：
	+ iter() 创建迭代器对象
	+ next() 输出迭代器的下一个元素

* 生成器：yield()
	+ 用于迭代操作，返回数据，类似于return，不同的是yield可以在循环中连续返回数据。
	+ 简单的迭代器：
		- 用元组代替列表，如：
		```python
		>>> g=(i for i in range(10))
		>>> g
		<generator object <genexpr> at 0x7f9fd7492d58>	
		```


