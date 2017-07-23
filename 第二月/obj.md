# Python面向对象
#### 特点
* 封装、继承、多态
* 这些概念就不说了，就直接看简单的例子吧

#### 构造函数 __init__
* 第一个参数：self（不变）
* Python中ES的连接
```python
  1 #!/usr/bin/python
  2 
  3 from elasticsearch import Elasticsearch
  4 
  5 class ES(object):
  6     __host = 'localhost'
  7     __port = 9200
  8     __index = 'test'
  9     __type = 'test'
 10     __client = ''
 11     def __init__(self, host='', port=''):
 12         if host and port:
 13             self.__host = host
 14             self.__port = port
 15 
 16         self.__client = Elasticsearch([{'host':self.__host,'port':self.__port}])                          
 17         print(self.__client)
 18 
 19 
 20 es = ES()
 ```
 运行结果
 ```python
[root@iZ2zee30op42zedrik59weZ work]# python obj.py 
<Elasticsearch([{'host': 'localhost', 'port': 9200}])>
```

#### 类的封装
* 简单实现Elasticsearch在Python中的几个方法
链接地址：[https://github.com/LiuShuaiaCai/python/blob/master/%E7%AC%AC%E4%BA%8C%E6%9C%88/obj.py](https://github.com/LiuShuaiaCai/python/blob/master/%E7%AC%AC%E4%BA%8C%E6%9C%88/obj.py)

运行结果
```python
[root@iZ2zee30op42zedrik59weZ work]# python obj.py 
<Elasticsearch([{'host': 'localhost', 'port': 9200, 'verify_certs': True}])>
{'count': 1001, '_shards': {'total': 1, 'successful': 1, 'failed': 0}}
{'took': 17, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'failed': 0}, 'hits': {'total': 1001, 'max_score': 1.0, 'hits': [{'_index': 'test', '_type': 'test', '_id': '1', '_score': 1.0, '_source': {'name': 'iLGnWB', 'age': 44, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '2', '_score': 1.0, '_source': {'name': 'iAWtCf', 'age': 31, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '3', '_score': 1.0, '_source': {'name': 'KAZzPe', 'age': 53, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '4', '_score': 1.0, '_source': {'name': 'fUuyxx', 'age': 62, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '5', '_score': 1.0, '_source': {'name': 'giGhsg', 'age': 31, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '6', '_score': 1.0, '_source': {'name': 'ibiYDY', 'age': 97, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '7', '_score': 1.0, '_source': {'name': 'aSaevz', 'age': 49, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '8', '_score': 1.0, '_source': {'name': 'TwXeCE', 'age': 31, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '9', '_score': 1.0, '_source': {'name': 'VdbQIR', 'age': 39, 'other': {'job': 'PHP'}}}, {'_index': 'test', '_type': 'test', '_id': '10', '_score': 1.0, '_source': {'name': 'FhFmTI', 'age': 22, 'other': {'job': 'PHP'}}}]}}
```
#### 获取对象信息
* type() 与 isinstance()
```python
>>> import random
>>> a = random.random()
>>> a
0.4274845737415822
>>> type(a)
<class 'float'>
>>> isinstance(a,float)
True
>>> isinstance(a,int)
False
```
* type 与 isinstance 的区别

#### 与PHP不同的是Python可以实现多继承，参考文章：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000
```python
  1 #! /usr/bin/python
  2 
  3 class People(object):
  4     def sysed(self):
  5         print('I am People...')
  6 
  7 class Man():
  8     def sysed(self):
  9         print("I am Man")
 10 
 11 class Person(People, Man):
 12     def sysed(self):
 13         print(People.sysed)
 14         print(Man.sysed)
 15         print("I am Person")
 16 
 17 
 18 p = Person()                                                                                              
 19 p.sysed()
```
运行结果：
```python
[root@iZ2zee30op42zedrik59weZ work]# python obj2.py 
<function People.sysed at 0x7fcb1d5f3950>
<function Man.sysed at 0x7fcb1d5f39d8>
I am Person
```

