# 模块学习笔记

* 引入模块的几种形式
	+ import语句，如：import sys
	+ from sys import argv
	+ from sys import *

* __name__属性
	+ 主程序的属性
	+ 可以通过 __name__=='__main__' 定义本模块主程序执行的程序块

* 查看模块内定义的所有名称
	+ dir()函数，如：dir(sys)

## 包

* 包是管理python命名空间的的形式，采用‘点模块名称’，如：A.B，表示包A中的子模块B
	+ 导入包模块：from A.B import C
* 注意：
	+ 如果没有相应的包，会抛出一个ImportError异常
	+ 包下面的文件夹中都有一个__init__.py文件，只有有这个文件才是包，__init__.py文件可以初始化一些代码，也可以为空
	+ 如果使用import A.B.C这种形式，要注意```除了```最后一项(C)，都必须是包，最后一项可以是包、模块，但不能是类、变量、函数
