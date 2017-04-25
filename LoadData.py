#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import re
import uniout  #让list正常输出中文，不显示unicode
trainDataNum = 100000  #设置训练数据的数量
testDataNum = 1000  #设置测试数据的数量

'''
testLoadData():
加载test数据，已除去train数据

#testPostingList:数据为list的list，把垃圾短信进行了分词
[['我','最近','在','学车'],['然后','科二','科三','都','挂了'],['是的','都','挂了']]
#testClassVec:一维list，表示testPostingList中数据的类型
[1,1,0,0,1,0]

'''

def testLoadData():

	testPostingList = []; testClassVec = []
	try:
		f = open('./data/带标签短信.txt','r')
		n = 0
		if not f:
			print 'open file failed~'
			raise ValueError('open file failed~')
		print 'open file succeed~'
		while n < trainDataNum:  #600000
			n = n + 1
			line = f.readline()
		n = 0
		while n < testDataNum:
			n = n + 1
			line = f.readline()
			m = re.split('\t',line)  #返回list
			#print str(m).decode('string_escape')
			#print m #显示编码，无法正确显示中文
			flag = int(m[0])  # str -> int
			mess = m[1]  #str类型
			messList = jieba.lcut(mess,cut_all=False)
			# jieba.lcut 直接返回list	
			if(n % 1000 == 0):
				print 'testLoadData',n
			#print str(messlist).decode('string_escape')
			#print messlist #一条短信分词的list,没处理
			testPostingList.append(messList)
			testClassVec.append(flag)
		#print classVec
		#print postingList
	finally:
		if f:
			f.close()
	return testPostingList, testClassVec


'''
LoadData():
加载train数据

#PostingList:数据为list的list，把垃圾短信进行了分词
[['我','最近','在','学车'],['然后','科二','科三','都','挂了'],['是的','都','挂了']]
#ClassVec:一维list，表示testPostingList中数据的类型
[1,1,0,0,1,0]

'''

def loadData():

	postingList = []; classVec = []
	try:
		f = open('./data/带标签短信.txt','r')
		n = 0
		if f:
			print 'open file succeeed'
		while n < trainDataNum:  
			n = n + 1
			line = f.readline()
			m = re.split('\t',line)  #返回list
			#print str(m).decode('string_escape')
			#print m #显示编码，无法正确显示中文
			flag = int(m[0])  # str -> int
			mess = m[1]  #str类型
			messList = jieba.lcut(mess,cut_all=False)
			if(n % 1000 == 0):
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

'''
createVocabList(dataSet):
构建词向量列表

#dataSet:loadData()函数返回的postingList
[['我','最近','在','学车'],['然后','科二','科三','都','挂了'],['是的','都','挂了']]
#vocabSet:一维list，表示PostingList中所有词的集合
['我','最近','在','学车','然后','科二','科三','都','挂了','是的']

'''

def createVocabList(dataSet):
	vocabSet = set([])
	n = 0
	for doc in dataSet:
		n += 1
		vocabSet = vocabSet | set(doc)
		if n % 1000 == 0:
			print 'createVocabList',n
	return list(vocabSet)

'''
word2Vec(vocabList, inputSet):
把分词后的短信转化为词向量

#vocabList:createVocabList函数返回的vocabSet
vocabSet:一维list，['我','最近','在','学车','然后','科二','科三','都','挂了','是的']
#inputSet:分词后的短信list。可以是postingList中的一个元素。
['我','最近','在','学车']

returnVec:一维list，为词向量。
[1,1,0,0,1,0]
'''

def word2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList) #与词汇表等长的list
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
			#returnVec从0开始
		#else:
		#	print "the word: %s is not in my Vocabulary!" % word
	return returnVec  #list 类型
'''
#####test code
postingList,classVec = loadData() 
vocabSet = createVocabList(postingList) #vocabSet是词汇表
#print len(vocabSet)

for doc in postingList:
	print word2Vec(vocabSet, doc),'ooc' #某条短信对应的词向量
	#returnVec
'''
