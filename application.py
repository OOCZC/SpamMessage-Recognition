from flask import Flask, render_template, request, flash

app = Flask(__name__)

#测试算法需要
import jieba
from handWriting_bayes.LoadData import *
from handWriting_bayes.bayes import *

@app.route('/recog', methods=['POST'])
def recog():
    #传回的两个参数，message为短信内容，algorithm_name为1时使用第一种算法，2时使用第二种。
    print("recog()", request.form['message'], "***")
    print("recog()", request.form['algorithm_name'], "***")
    #模拟使用算法
    messList = jieba.lcut(request.form['message'], cut_all=False)
    # jieba.lcut 直接返回list   
    print("***",messList)
    receVec = word2Vec(vocabList, messList)
    if classifyNB(array(receVec), p0V, p1V, pSpam) == 1:
        print("识别为垃圾短信")
        return "识别为垃圾短信"
    else:
        print("识别为正常短信")
        return "识别为正常短信"

@app.route('/')
def index():
    print("index()")
    return render_template('index.html')


if __name__ == '__main__':
    #以下代码测试算法的初始化过程
    postingList,classVec = loadData()
    vocabList = createVocabList(postingList)
    #print("test test test")
    #vocabList 是中文词汇表
    trainMat = []  #训练数据矩阵。[[1,0,0,1,0,1],[0,1,1,0,0,1],[1,1,0,0,1,1]]
    n = 0 
    for doc in postingList:
        n += 1
        if n % 1000 == 0:
            print('doc2Vec',n)
        trainMat.append(word2Vec(vocabList, doc)) #某条短信对应的词向量
    p0V,p1V,pSpam = trainNB(array(trainMat), array(classVec))
    #以下代码Flask必需
    app.debug = True
    app.run(host='0.0.0.0', port=6464)
    #外部可访问。  app.run() #外部不可访问
