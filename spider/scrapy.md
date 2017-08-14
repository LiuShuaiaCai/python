# scrapy执行系统命令 - subprocess模块

#### 执行系统命令的模块

    + os.system
    + os.spawn
    + os.popen
    + popen2
    + commands
    + subprocess
    
##### subprocess模块的方法
* call() 执行命令，返回状态码，shell = True允许shell命令是字符串的形式

```python
# 以下两种形式，以下方法都有这两种形式
subprocess.call(["ls", "-l"])
subprocess.call("ls -l",shell=True)
```

* check_call() 如果执行状态吗是0，则返回0，否则抛出异常
* check_output() 如果执行状态吗是0，则返回执行结果，否则抛出异常
* Popen() 用于执行复杂的系统命令

#### 具体可参考文章
[http://www.cnblogs.com/sweet521/p/7324884.html](http://www.cnblogs.com/sweet521/p/7324884.html)
[http://www.cnblogs.com/sweet521/p/7324893.html](http://www.cnblogs.com/sweet521/p/7324893.html)