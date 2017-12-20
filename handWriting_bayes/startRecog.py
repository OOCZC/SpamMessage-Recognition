import jieba
import re
import socket
import threading
import time
from LoadData import *
from bayes import *


def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	# addr是tuple ('127.0.0.1', 56610)
	recvString = sock.recv(10240)
	if len(recvString) < 22:
		sock.send('0')
		print(recvString) #显示编码，无法正确显示中文
		print('0')
	else:
		#print str(m).decode('string_escape')
		print(recvString) #显示编码，无法正确显示中文
		messList = jieba.lcut(recvString, cut_all=False)
		# jieba.lcut 直接返回list	
		print(messList)
		receVec = word2Vec(vocabList, messList)
		if classifyNB(array(receVec), p0V, p1V, pSpam) == 1:
			sock.send('1')
			print('1')
		else:
			sock.send('0')
			print('0')
	sock.close()
	print('Connection from %s:%s closed.' % addr)

postingList,classVec = loadData()
vocabList = createVocabList(postingList)
#vocabList 是中文词汇表
trainMat = []  #训练数据矩阵。[[1,0,0,1,0,1],[0,1,1,0,0,1],[1,1,0,0,1,1]]
n = 0 
for doc in postingList:
	n += 1
	if n % 1000 == 0:
		print('doc2Vec',n)
	trainMat.append(word2Vec(vocabList, doc)) #某条短信对应的词向量
p0V,p1V,pSpam = trainNB(array(trainMat), array(classVec))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#创建TCP,IPv4的Socket
s.bind(('0.0.0.0', 6463))
#绑定端口
s.listen(10)
#监听端口，指定等待连接的最大数量5

print('Waiting for connection...')
while True:
	sock, addr = s.accept()
	#接收一个新连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	#创建新线程处理TCP连接
	t.start()


