#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re
import uniout  #让list正常输出中文，不显示unicode
import random

'''
由于数据中0数据过多，0:1大约为10:1
由此函数处理数据，去除一些标签为0的数据。
'''
trainDataNum = 799000  

f = open('带标签短信.txt','r')
fw = open('filterMess.txt','w')
def cutLoadData():
	try:
		n = 0
		if not f:
			print 'open file failed~'
			raise ValueError('open file failed~')
		if not fw:
			print 'open file failed~'
			raise ValueError('open file failed~')
		print 'open file succeed~'
		while n < trainDataNum:  
			n = n + 1
			line = f.readline()
			m = re.split('\t',line)  #返回list
			flag = int(m[0])  # str -> int
			r = random.randint(1,3) 
			#这里大约去除2/3 标签为0的短信
			if flag == 0 and r % 2 == 0:
				fw.write(line)
			if flag == 1:
				fw.write(line)
			if(n % 100000 == 0):
				print 'cutLoadData',n
	finally:
		f.close()
		fw.close()

cutLoadData()
