#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from lscmodule.filetree import tree

def entrance():
	print("输入文件路径：",end='')
	while True:
		filepath = input()
		if filepath=='q':
			break;
		elif filepath:
			data = tree.tree(filepath)
			print("继续输入文件路径 OR 输入'q'退出：",end='')
		else:
			print("输入正确的文件路径 OR 输入'q'退出：",end='')


if __name__=='__main__':	
	entrance()
