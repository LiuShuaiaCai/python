# 正则re模块学习笔记

	Python 正则re模块分两步：
	1、[compile]编译正则表达式，如果正则表达式的字符串本身有错误，会报错；
	2、[match|search]用编译后的正则表达式匹配字符串

#### 转义
	* 在表达式前边加'r';

#### 分割字符串[split]
	```python
	>>> 'a b       c  d'.split()
	['a', 'b', 'c', 'd']

	>>> re.split(r'\s+','a b       c  d')
	['a', 'b', 'c', 'd']
	```

#### 分组[group|groups]
	```python
	>>> import re
	>>> g = re.search(r'(\d+)-(\d+)','123-234')
	>>> g.groups()
	('123', '234')
	>>> g.group(0)
	'123-234'
	>>> g.group(1)
	'123'
	>>> g.group(2)
	'234'
	>>> g.group(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: no such group
	```

#### match 与 search的区别
	* match 从字符串的开始位置开始匹配
	* search 扫描整个字符串并返回第一个匹配成功的匹配

#### 检索和替换
* re.sub(pattern,repl,str,count=0)

	pattern：正则中的模式字符串
	repl：替换的字符串，也可以是一个函数
	str：要匹配的字符串
	count：替换的最大次数，默认0表示替换所有的匹配

* 删除非数字字符
```python
>>> sub = re.sub(r"\D",'','123abc456def')
>>> sub
'123456'
```
* repl 为函数(去掉字符串中的逗号)
```python
import re

def replace(matched):
    return ''

s = 'A23,G4HF,D,567'
print(re.sub('(?P<value>\,+)', double, s))
```

#### 贪婪匹配
* 正则默认匹配是贪婪匹配，也就是尽可能多的匹配，如：
```python
>>> str = 'abc123'
>>> re.match(r'(\w+)(\d*)',str).groups()
('abc123', '')
```
* 在贪婪陪配的正则后添加？，\w+?只能匹配一个字符，如：
```pyhton
>>> re.match(r'(\w+?)(\d*)',str).groups()
('a', '')
```


