from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/recog', methods=['POST'])
def recog():
    #import mt
    #transText = mt.mtChinese(request.form['yuanwen'])
    print("recog()", request.form['message'], "***")
    print("recog()", request.form['algorithm_name'], "***")
    #print("recog()", request.form['algorithm2'], "***")
    return "return recog"

@app.route('/')
def index():
    print("index()")
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6464)
    #外部可访问。  app.run() #外部不可访问
