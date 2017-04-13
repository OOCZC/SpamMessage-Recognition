#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re
import uniout  # 输出显示正常中文，不显示unicode

try:
	f = open('./data/带标签短信.txt','r')
	n = 1
	if f:
		print 'open file succeeed'
	while n <6:  #600000
		n = n + 1
		line = f.readline()
		m = re.split('\t',line)  #返回list
		print m
		#print str(m).decode('string_escape')
		# print m 显示编码，无法正确显示中文
		flag = int(m[0])  # str -> int
		mess = m[1]  #str类型
		messlist = jieba.lcut(mess,cut_all=False)
		# jieba.lcut 直接返回list
		print str(messlist).decode('string_escape')
finally:
	if f:
		f.close()

