# Python 与 Mysql的使用笔记
#### 安装MySQL驱动
```
[root@iZ2zee30op42zedrik59weZ ~]# pip install PyMySQL
```

#### Python 操作数据库
```
#!/usr/bin/python

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
```

* 数据的增、删、改、查都是同样的操作

#### 数据库的查询的几种方法

	* Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

		+ fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
		+ fetchall(): 接收全部的返回结果行.
		+ rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
