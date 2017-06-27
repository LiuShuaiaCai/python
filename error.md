# 异常学习笔记

#### 异常处理机制：
```python
try:
	...
except Exception as e:
	...
else:
	...
finally:
	...
```

#### 有很多的异常类，例如：ValueError、ZeroDivisionError等，这些异常类都继承于基类BaseException。

	BaseException
	 +-- SystemExit
	 +-- KeyboardInterrupt
	 +-- GeneratorExit
	 +-- Exception
	      +-- StopIteration
	      +-- StopAsyncIteration
	      +-- ArithmeticError
	      |    +-- FloatingPointError
	      |    +-- OverflowError
	      |    +-- ZeroDivisionError
	      +-- AssertionError
	      +-- AttributeError
	      +-- BufferError
	      +-- EOFError
	      +-- ImportError
	           +-- ModuleNotFoundError
	      +-- LookupError
	      |    +-- IndexError
	      |    +-- KeyError
	      +-- MemoryError
	      +-- NameError
	      |    +-- UnboundLocalError
	      +-- OSError
	      |    +-- BlockingIOError
	      |    +-- ChildProcessError
	      |    +-- ConnectionError
	      |    |    +-- BrokenPipeError
	      |    |    +-- ConnectionAbortedError
	      |    |    +-- ConnectionRefusedError
	      |    |    +-- ConnectionResetError
	      |    +-- FileExistsError
	      |    +-- FileNotFoundError
	      |    +-- InterruptedError
	      |    +-- IsADirectoryError
	      |    +-- NotADirectoryError
	      |    +-- PermissionError
	      |    +-- ProcessLookupError
	      |    +-- TimeoutError
	      +-- ReferenceError
	      +-- RuntimeError
	      |    +-- NotImplementedError
	      |    +-- RecursionError
	      +-- SyntaxError
	      |    +-- IndentationError
	      |         +-- TabError
	      +-- SystemError
	      +-- TypeError
	      +-- ValueError
	      |    +-- UnicodeError
	      |         +-- UnicodeDecodeError
	      |         +-- UnicodeEncodeError
	      |         +-- UnicodeTranslateError
	      +-- Warning
	           +-- DeprecationWarning
	           +-- PendingDeprecationWarning
	           +-- RuntimeWarning
	           +-- SyntaxWarning
	           +-- UserWarning
	           +-- FutureWarning
	           +-- ImportWarning
	           +-- UnicodeWarning
	           +-- BytesWarning
	           +-- ResourceWarning

* 主动抛出错误
	+ raise命令抛出错误
	```python
	>>> def foo(s):
	...     n=int(s)
	...     if n==0:
	...             raise ValueError('invalid value %s' % s)
	...     return 10/n
	... 
	>>> def bar():
	...     try:
	...             foo('0')
	...     except ValueError as e:
	...             print('ValueError')
	...             raise
	... 
	>>> bar()
	ValueError
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 3, in bar
	File "<stdin>", line 4, in foo
	ValueError: invalid value 0
