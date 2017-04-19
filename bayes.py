#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uniout  #让list正常输出中文，不显示unicode
from numpy import *

def trainNB(trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pSpam = sum(trainCategory) / float(numTrainDocs)
	p0Num = zeros(numWords)
	p1Num = zeros(numWords)
	p0Denom = 0.0
	p1Denom = 0.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Demon += sum(trainMatrix[i])
	p1Vect = p1Num/p1Demon
	p0Vect = p0Num/p0Demon
	return p0Vect,p1Vect,pAbusive

