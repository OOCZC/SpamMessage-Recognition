#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re
import uniout  #让list正常输出中文，不显示unicode

def loadData():

	postingList = []; classVec = []
	try:
		f = open('./data/带标签短信.txt','r')
		n = 1
		if f:
			print 'open file succeeed'
		while n <80000:  #600000
			n = n + 1
			line = f.readline()
			m = re.split('\t',line)  #返回list
			#print str(m).decode('string_escape')
			#print m #显示编码，无法正确显示中文
			flag = int(m[0])  # str -> int
			mess = m[1]  #str类型
			messList = jieba.lcut(mess,cut_all=False)
			if(n%1000 == 0):
				print 'loadData',n
			#print str(messlist).decode('string_escape')
			#print messlist #一条短信分词的list,没处理
			postingList.append(messList)
			classVec.append(flag)
		#print classVec
		#print postingList
	finally:
		if f:
			f.close()
	return postingList,classVec

# jieba.lcut 直接返回list	
def createVocabList(dataSet):
	vocabSet = set([])
	n = 0
	for doc in dataSet:
		n = n + 1
		vocabSet = vocabSet | set(doc)
		if n % 1000 == 0:
			print 'createVocabList',n
	return list(vocabSet)
def word2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList) #与词汇表等长的list
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
			#returnVec从0开始
		else:
			print "the word: %s is not in my \
Vocabulary!" % word
	return returnVec  #list 类型

postingList,classVec = loadData() 
vocabSet = createVocabList(postingList) #vocabSet是词汇表
#print len(vocabSet)

for doc in postingList:
	print word2Vec(vocabSet, doc) #某条短信对应的词向量
	#returnVec


