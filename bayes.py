#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uniout  #让list正常输出中文，不显示unicode
from numpy import *

'''

trainNB(trainMatrix, trainCategory):
训练出模型

#trainMatrix是二维array类型，为词向量矩阵,每一行为词向量
array((1,0,1,0,1,0),(0,1,1,1,0,1),(0,0,1,1,1,0))
#trainCategory是一维array类型，标记每个词向量的类型
array(1,0,0,0,1,0,1)

p0Vec,p1Vec:array型一维数组，与词向量等长，表示在0/1型短
信中各个词出现的概率，即P(w|c)
pAbusive:浮点数，表示垃圾短信的概率，即P(c1)

'''
def trainNB(trainMatrix, trainCategory):
	# trainMatrix是二维array类型，为词向量矩阵
	# trainCategory是一维array类型
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0]) #总词数
	pAbusive = sum(trainCategory) / float(numTrainDocs) 
	#spam短信的概率
	p0Num = ones(numWords) #array数组，初始化为1
	p1Num = ones(numWords) #防止多个概率相乘为0
	p0Denom = 2.0 #浮点型数据
	p1Denom = 2.0 #垃圾短信总词数
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Demon += sum(trainMatrix[i])
	p1Vect = log(p1Num/p1Demon) #array数组除浮点数，得array数组
	p0Vect = log(p0Num/p0Demon) #取log，之后相加即可
	#每个词在普通短信中出现的概率，p(w|c0)
	return p0Vec,p1Vec,pAbusive
	# 两个向量，一个垃圾短信概率

'''

classifyNB(vec2Classify, p0Vec, p1Vec, pClass):
判断vec2Classify这个词向量所属类型

#vec2Classify是词向量，(1,0,0,1,0,1)
#p0Vec,p1Vec,PClass 为trainNB的三个输出

'''
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass):
	#判断vec2Classify向量的分类
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	# sum(vec2Classify * p1Vec)为log(p(w|c))
	# p1为log( p(w|c)*p(c1) )
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
	if p1 > p0:
		return 1 #为垃圾短信
	else:
		return 0 #为正常短信

