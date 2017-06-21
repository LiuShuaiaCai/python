# 字典学习笔记

* 特点：可变容器模型
* 注意：
	+ 字典的键是唯一的
	+ 键必须为不可改变的，如：字符串、数字、元组
* 常用的方法：
	info = {'name':'liushuaicai','age','25'}
	+ 删除字典：
		- 删除所有的元素 info.clear()
		- 删除对象：del info['age']
		- 删除指定的键值,如果没给键，返回第二个参数：pop('name','liu')
	+ 获取键的值：
		- 直接获取：info['name']
		- get()方法，第二个参数为默认值：info.get('name','liu')
	+ 判断键是否存在：
		- 'name' in info,存在返回TRUE，否则FALSE
	+ 以列表返回可遍历的元组数组：info.items()
	+ 返回所有的键：info.keys()
	+ 返回所有的值：info.values()
	
