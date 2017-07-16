# Python的Json模块学习笔记
#### Python 编码为Json类型的转换对应表
| Python | Json |
|:-------:|:-----:|
| dict | Object |
| list,tuple | Array |
| str | string |
#### json.dumps()对数据进行编码
```python
>>> import json
>>> info = {'name':'liushuaicai','age':25,'job':'php'}
>>> info
{'name': 'liushuaicai', 'age': 25, 'job': 'php'}
>>> print(json.dumps(info))
{"name": "liushuaicai", "age": 25, "job": "php"}
```
#### json.loads()对数据进行解码
```python
>>> load
'{"name": "liushuaicai", "age": 25, "job": "php"}'
>>> print(json.loads(load))
{'name': 'liushuaicai', 'age': 25, 'job': 'php'}
```
