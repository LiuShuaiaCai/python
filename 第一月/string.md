# 字符串学习笔记

* 特点：
	+ 不能修改

* 常用：
	+ str1 = 'hello' str2 = 'python' tuple1 = ('hello','python')
	+ 字符串长度：
		- len() 
	+ 字符串替换：
		- replace(old, new[,max])
	+ 字符串截取：
		- 切片: str1[1:3]
		- 字符串分割：split() 如：str1.split('l')
	+ 字符串连接：
		- 通过+连接两个字符串：str1 + str2
		- join连接对象元素：''.join(tuple1) 
	+ 判断字符串是否包含另一个字符串：
		- in|not in			 如：'he' in str1
		- count				如：str1.count('l')
		- find|rfind        如：str1.find('l')
		- index|rindex      如：str1.index('l')，和find一样，只不过如果不存在时，会报错
		- 正则：re.search();re.match()
	+ 判断字符串第一个|最后一个字符：
		- 切片：str1[0]|str1[-1]
		- startswith() str1.startswith('h')
		- endswith() str1.endswith('o')
		- 正则
	+ 去除字符串的空格：
		- lstrip | rstrip | strip
		- 正则
	+ 字符串的几个判断：
		- isalnum() 检查字符串是否是由数字和字母组成
		- isalpha() 是否都是字母
		- isdigit()|isnumeric() 是否都是数字
		- islower() 是否都是小写（可以包含数字）
		- isupper() 是否是大写
		- isspace() 是否都是空格
		- istitle() 是否是title
	+ 字符串的大小写转换：
		- capitalize() 字符串第一个字符大写
		- lower() 转换为小写
		- upper() 转化为大写
		- swapcase() 大小写反转
	+ 字符串的格式化：
		- c、s、d、f

