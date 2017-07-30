#! /usr/local/python

import pymysql

class Mysql:
	HOST = "localhost"
	USER = "root"
	PWD = "root"
	DATABASE = "test"
	DB = ""
	TABLE=""

	def __init__(self, host="",user="",pwd="",database=""):
		if not host == "":
			self.HOST = host
		if not user == "":
			self.USER = user
		if not pwd == "":
			self.PWD = pwd
		if not database == "":
			self.DATABASE = database

		# 打开数据库
		self.DB = pymysql.connect(self.HOST, self.USER, self.PWD, self.DATABASE)
		

	def table(self,table):
		if not table=="":
			self.TABLE = table
			return self
		else:
			raise Exception("invalid value table")

	def execute(self,sql,cate=''):
		# 使用cursor()方法获取操作游标
		cursor = self.DB.cursor()
		
		# 执行事务操作
		try:
			# 执行sql语句
			result = cursor.execute(sql)
			if result and cate == 'select':
				# 获取所有记录的列表
				results = cursor.fetchall()
				for row in results:
					id = row[0]
					name = row[1]
					sex = row[2]
					age = row[3]
					job = row[4]
					time = row[5]
					# 打印结果
					print("id=%d,name=%s,age=%d,sex=%s,job=%s,time=%s" % (id,name,age,sex,job,time))
			elif result:
				print("SUCCESS!!!")
			else:
				print("FILED")
			# 提交到数据库执行
			self.DB.commit()
		except:
			# 如果出错，则回滚
			self.DB.rollback()

		# 关闭数据库
		self.DB.close()

	def add(self,params={}):
		if params and not self.TABLE=="":
			table = self.TABLE
			keys = ','.join(list(params.keys()))
			values = ""
			for i in list(params.values()):
				values += "'%s'," % i
			values = values.strip(',')
			sql = "INSERT INTO %s(%s) VALUES(%s)" % (table,keys,values)
			
			# self.execute(sql)
		else:
			exit("can not empty")
		

if __name__ == '__main__':
	# 实例化Mysql类
	mysql = Mysql()

	# 添加数据
	data = {"name":"liushuaicai","age":25,"sex":"man","job":"php"}
	mysql.table('test').add(data)
	
	# 查询数据
	sql = "select * from test"
	mysql.execute(sql)
