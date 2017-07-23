#!/usr/bin/python

'''简单实现Elasticsearch在Python中的几个方法，待完善...'''

from elasticsearch import Elasticsearch,helpers
import random,string

class ES(object):
	# 定义全局变量
	__host = 'localhost'
	__port = 9200
	__index = 'test'
	__type = 'test'
	__client = ''

	# 初始化，连接ES
	def __init__(self, host='', port=''):
		if host and port:
			self.__host = host
			self.__port = port

		self.__client = Elasticsearch([{"host":self.__host,"port":self.__port,"verify_certs":True}])
		print(self.__client)

	# 判断index是否存在
	def exists(self,index):
		if not self.__client.indices.exists(index):
			print('not index')
			return False
		
		return True

	# 删除索引
	def delete(self, index):
		self.__client.indices.delete(index)

	# 文档统计
	def count(self, index, doc_type):
		if not self.exists(index):
			print("not index")
			return False
		ret = self.__client.count(index)
		print(ret)

	# 创建index、type、mapping
	def indices(self, settings, index):
		if not self.exists(index):
			self.__index = index
		else:
			self.delete(index)
		ret = self.__client.indices.create(index=self.__index, ignore=[400,404], body=settings)
		print(ret)		

	# 写入数据index、create
	def create(self):
		params = {
			"index": "test",
			"doc_type": "test",
			"id": 1,
			"body": {
				"name": "Liushuaicai",
				"age": 25,
				"other":{
					"job": "PHP"
				}
			}
		}

		if self.__client.exists(index = params['index'],doc_type=params['doc_type'],id=params['id']):
			print('docment already exists...')
			print('deleting...')
			delete = self.__client.delete(index = params['index'],doc_type=params['doc_type'],id=params['id'])
			if delete['result'] == 'deleted':
				print('already deleted...')
		result = self.__client.create(index=params['index'],doc_type=params['doc_type'],id=params['id'],body=params['body'])
		print(result)
	
	def bulk(self):
		count = 1002
		start = 1
		params = []
		while(start < count):
			name = ''.join(random.choice(string.ascii_letters) for x in range(6))
			age = random.randint(1,100)
			param = {
				"_index": "test",
				"_type": "test",
				"_id": start,
				"_source": {
					"name": name,
					"age": age,
					"other": {"job":"PHP"}	
				}
			}
			start += 1
			params.append(param)
			# 每次写入50个
			if (len(params)%50==0):
				helpers.bulk(self.__client, params)
				del params[0:len(params)]
		# 写入剩余的数据
		if (len(params)>0):
			helpers.bulk(self.__client, params)
			del params[0:len(params)]
		
	# 数据的查询 get、search
	def search(self,index,doc_type=''):
		if self.exists(index):
			result = self.__client.search(index=index,doc_type=doc_type)
			if not result:
				print("not found data...")
				return False
			print(result)
	
	def get(index, doc_type, id):
		if not self.__client.exists(index=index,doc_type=doc_type,id=id):
			print("not find %d data" % id)
			return False
		result = self.__client.get(index=index,doc_type=doc_type,id=id)	
		print(result)
	
client = ES()

# index配置
settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "test": {
            "properties": {
                "name": {
                    "type": "string",
					"index": "analyzed"
                },
				"age": {
					"type": "integer",
					"index": "not_analyzed"
				},
				"other": {
					"type":"object",
					"properties": {
						"job": {
							"type": "string"
						}
					}
				}
            }
        }
     }
}
# client.indices(settings, 'test')

# 文档统计
client.count('test','test')

# 写入单条数据
#client.create()

# 批量写入数据
# client.bulk()

# 查询数据
id = random.randint(1,1002)
#client.get('test', 'test', 1)
client.search('test','test')
