
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
import pymongo
import random

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users
nums = random.random()


@app.route('/ok')
def my_form():
    my_ip = "192.168.1.1"
    return render_template ('index(me).html', **locals()) #моя адмика

@app.route('/ok', methods=['GET' ,'POST'])
def my_form_post():
    text = request.form['title']
    num = random.random()
    car = request.form['image']
    uri = 'static/img/' + car
    url = {'_id':nums ,'url_img' : uri, 'name':'Rob'}
    vid = request.form['video']

    urii = 'static/vid/' + vid

    texts = request.form['texts']
    rad = request.form['radio']
    if rad == 'yes':
        frid = 1
    if rad == 'no':
        frid = 2
    if rad == 'ok':
        frid = 3
    sh = request.form['shablon']

    yse = {'_id':num, 'img1':uri, 'title1' : text,'video':urii, 'theme': frid, 'text1':texts, 'sh':sh, 'title2' : text,'text2':texts,'img2':uri, 'title3' : text,'text3':texts,'img3':uri}
    user.insert(yse)
    for mep in user.find({'_id':num}): #ищет по Id
        print (mep)
    with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
       jsn = json.dump(yse, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги
    return redirect('localhost:8888/ok')

@app.route('/pc')
def add_pc():

    return ('hello!')

@app.route('/pd')
def add_pd():
    return redirect ('http://0.0.0.0:8888/ek')


@app.route('/pp')
def add_pp():
    return redirect ('http://0.0.0.0:8888/ek')

@app.route('/')
def ok():
    return render_template('index.html')


@app.route('/ek')
def ek():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,debug=True)




