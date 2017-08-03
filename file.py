# -*- coding:utf-8 -*-
import os

def findFile(strFilePath):
	print('This is the dir:%s.'%strFilePath)
	try:
		for filename in os.listdir(strFilePath):
			if os.path.isdir(filename):
				print('This is a dir:%s.'%filename)
				findFile(os.path.join(strFilePath,filename))
			elif os.path.isfile(os.path.join(strFilePath,filename)):#注意这个地方，使用文件的相对路径
				print('This is a file dir:%s.'%os.path.join(strFilePath,filename))
			else:
				print('This is:%s.'%filename)
	except BaseException as e:
		print(e)
		print('输出当前目录的情况。当前目录为：',os.path.abspath('.'))
	finally:
		print('目录（%s）遍历结束'%strFilePath)

if __name__ =='__main__':
	strPath = input('Please input a filepath:')
	findFile(strPath)