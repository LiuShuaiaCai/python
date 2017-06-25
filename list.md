# 列表学习笔记

* 特点：
	+ 可以修改

* 常用方法：
	+ list = ['hello','python'] tuple = ('hello','pyhton')
	+ 获取列表长度：len(list)
	+ 将数组转换为列表：list(tuple)
	+ 在列表末尾添加新的对象：
		- list.append('!')
		- list.insert(len(list),'!')
	+ 删除列表中的值：
		- 默认最后一个，可以指定索引：list.pop(index)
		- 移除列表中匹配的第一项：list.remove('!')
		- 清空列表：list.clear()
	+ 判断列表中是否存在某个对象：
		- 对象出现的次数count()	list.count('h')
		- 索引的位置 index(),不存在会报错
	+ 对列表排序：
		- 翻转列表中的元素：list.reverse()
		- 自然排序：list.sort()

