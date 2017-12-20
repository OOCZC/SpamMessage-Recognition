import jieba
import re
from LoadData import *
from bayes import *

postingList,classVec = loadData()
vocabList = createVocabList(postingList)

trainMat = []  #训练数据矩阵。[[1,0,0,1,0,1],[0,1,1,0,0,1],[1,1,0,0,1,1]]
n = 0 
for doc in postingList:
	n += 1
	if n % 1000 == 0:
		print('doc2Vec',n)
	trainMat.append(word2Vec(vocabList, doc)) #某条短信对应的词向量
p0V,p1V,pSpam = trainNB(array(trainMat), array(classVec))

testSet,testClass = testLoadData()
errorCount = 0 ; n = 0
for doc in testSet:
	if n % 1000 == 0:
		print('doc2Vec',n)
	testVec = word2Vec(vocabList, doc)
	if classifyNB(array(testVec), p0V, p1V, pSpam) != testClass[n]:
		errorCount += 1
		print(testClass[n],'----',doc)
	n += 1

print('errorCount:',errorCount)
