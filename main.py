from flask import session,redirect,request,render_template,Flask
#flas-microframework
import os
import numpy as np

app=Flask(__name__) #flask ka object
app.secret_key="last topic ki khushi"

@app.route('/') #jitne pages utni baar likho ,first page=/. this will be the first page launch
def index():
    data=np.random.randint(1,100,100)
    return render_template('index.html',data=data)

@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=='POST'
    data=os.listdir()
    return render_template('home.html',
    files=data)

if __name__ == "__main__":
    app.run(debug=True) #run krane ka code,flask ka object
