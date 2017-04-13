#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re

try:
	f = open('./data/带标签短信.txt','r')
	n = 1
	if f:
		print 'open file succeeed'
	while n <6:  #600000
		n = n + 1
		line = f.readline()
		print line
		line = '1	344ddddd'
		#if  re.match('^(\d{3})-(\d{3,8})$','010-12345'):
		if re.match('(\d)\s\*',line):
			print 'match succeed'
		else:
			print 'match error'
		
		m = re.match('(\d)\s\*',line)
		print m.group(0)
		#print m.group(1)
		#print m.group(2)
		
# jieba.lcut 直接返回list	
finally:
	if f:
		f.close()

