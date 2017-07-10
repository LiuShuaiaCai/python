#!/usr/bin/python3
# -*- coding: utf-8 -*-

'显示一个目录下的所有目录、文件'
'''
	1、判断是否是绝对路径
	2、判断文件是否存在
	3、判断是文件还是目录，如果是文件直接返回，是目录继续

	输出：
	[root@iZ2zee30op42zedrik59weZ python]# python3 file.py
	输入文件路径：./lscmodule/filetree
	/root/virtualenv/python/work/python/lscmodule/filetree目录下有以下文件：
	|-- tree.py 1.37 KB
	|-- .tree.py.swp 12.00 KB
	|-- __init__.pyc 0.15 KB
	+-- __pycache__ 4.00 KB
	    |-- __init__.cpython-35.pyc 0.15 KB
		    |-- tree.cpython-35.pyc 1.35 KB
			|-- tree.pyc 0.43 KB
			|-- __init__.py 0.00 KB
'''

__author__ = 'lsc'

import os

def tree(filepath):
	# 获取文件的绝对路径
	if not os.path.isabs(filepath):
		abspath = os.path.abspath(filepath)
	else:
		abspath = filepath

	# 判断文件或者目录是否存在
	if os.path.exists(abspath):
		# 判断是文件还是目录
		if os.path.isfile(abspath):
			print(abspath)
		elif os.path.isdir(abspath):
			print("{}目录下有以下文件：".format(abspath))
			dirtree(abspath)
	else:
		print('{} not exists'.format(abspath))
	

def dirtree(dirpath,num=0):
	# 获取文件下的所有文件和目录
	allfile = os.listdir(dirpath)
	for filename in allfile:
		sub_dir = dirpath+'/'+filename
		file_size = filesize(sub_dir)
		if os.path.isfile(sub_dir):
			print(num*' '+'|-- '+filename+' '+file_size)
		elif os.path.isdir(sub_dir):
			print(num*' '+'+-- '+filename+' '+file_size)
			dirtree(sub_dir,num+4)

def filesize(filename):
	filesize = os.path.getsize(filename)
	ksize = filesize/1024
	if ksize>1024:
		msize = ksize/1024
		if msize>1024:
			gsize = msize/1024
			rsize = "%.2f GB" % gsize
		else:
			rsize = "%.2f MB" % msize
	else:
		rsize = "%.2f KB" % ksize

	return rsize
#if __name__=='__main__':
#	tree('world')
