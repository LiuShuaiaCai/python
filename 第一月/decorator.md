# 装饰器学习笔记

#### 特点：能够动态的添加功能
#### 本质上就是返回一个函数的高阶函数
#### 用符号@，把decorator置于函数的定义处

* 不带参数的装饰器
```python
>>> import functools
>>> def log(func):
		@functools.wraps(func)
...     def wrapper(*args,**kw):
...             print('call %s():' % func.__name__)
...             return func(*args,**kw)
...     return wrapper
... 
>>> @log		# 相当于 now=log(now)
... def now():
...     print('20170627')
... 
>>> now()	
call now():
20170627
```

* 带参数的装饰器
```python
#!/usr/bin/python3
import functools

def log(text):
	def de(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('%s %s():' % (text,func.__name__))
        return func(*args,**kw)
    return wrapper
    return de

@log('execute')
def now():
    print('20170629')

if __name__=='__main__':
	now()
```

