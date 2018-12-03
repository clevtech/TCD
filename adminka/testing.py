
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
from admin import *
import pymongo
import random
from pprint import pprint

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users
nums = random.random()


# @app.route('/ok')
# def my_form():
#     my_ip = "192.168.1.1"
#     name = 'hi!'
#     return render_template ('index(me).html', **locals()) #моя адмика
#
#
# @app.route('/ok', methods=['GET' ,'POST'])
# def my_form_post():
#     global text
#     text = request.form['title']
#     num = random.random()
#     car = request.form['image']
#     uri = 'static/img/' + car
#     url = {'_id':nums ,'url_img' : uri}
#     vid = request.form['video']
#     urii = 'static/vid/' + vid
#     texts = request.form['texts']
#     rad = request.form['radio']
#     if rad == 'yes':
#         frid = 1
#     if rad == 'no':
#         frid = 2
#     if rad == 'ok':
#         frid = 3
#     block = request.form['block']
#     print(block)
#     # if block == block: дает # выдает полное кол во блоков с 0 по кол во блоков
#     #     numbr = range(int(block))
#     #     nom = (list(numbr))
#     #     print (nom)
#     # else:
#     #     print("false")
#     global yse
#     yse1 = {'_id':num,'blocks':block, 'img1':uri, 'title1' : text,'video':urii, 'theme': frid, 'text1':texts, 'title2' : text,'text2':"hey!",'img2':uri, 'title3' : 'Hellow!','text3':'My texts','img3':uri}
#     user.insert(yse)
#     for mep in user.find({'_id':num}): #ищет по Id
#         print (mep)
#     with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
#        jsn = json.dump(yse, dat, indent=2, ensure_ascii=False) # mep это зн7ачение которому присвоено наше json значение из монги
#     return render_template('index(me).html', **locals())
#
#

# @app.route('/pc')
# def add_pc():
#
#     return redirect ('http://0.0.0.0:8888/')
#
# @app.route('/pd')
# def add_pd():
#     return render_template ('index.html')
#
#
# @app.route('/pp')
# def add_pp():
#     return render_template ('index.html')
#
# @app.route('/')
# def ok():
#     return render_template('index.html', next = 'http://0.0.0.0:8888/ek')
#
#
@app.route('/ek')
def ek():
    return render_template('main.html')


@app.route('/', methods = ['GET', 'POST'])
def mark_selected():
    return render_template('index.html')


@app.route('/button/<value>/', methods = ['GET', 'POST'])
def button(value=0):
    print("Value from button: " + value)
    print("Now we changed theme")
    if int(value) == 1:
        yse1 = {
"theme": "1",
"block": "1",
"title1": "Новые клиенты за сегодня",
"img1": "static/img/bg.jpg",
"text1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title2": "Новые клиенты за сегодня",
"img2": "static/img/bg.jpg",
"text2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title3": "Новые клиенты за сегодня",
"img3": "static/img/bg.jpg",
"text3": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"img-src1": "static/img/bg.jpg",
"video1": "static/video/vid.mp4",
        }
        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(yse1, dat, indent=2, ensure_ascii=False)
    elif int(value) == 2:
        yse2 = {
"theme": "1",
"block": "2",
"title1": "Новые клиенты за сегодня",
"img1": "static/img/bg.jpg",
"text1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title2": "Новые клиенты за сегодня",
"img2": "static/img/bg.jpg",
"text2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title3": "Новые клиенты за сегодня",
"img3": "static/img/bg.jpg",
"text3": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"img-src1": "static/img/bg.jpg",
"video1": "static/video/vid.mp4"}
        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(yse2, dat, indent=2, ensure_ascii=False)
    elif int(value) == 3:
        yse3 = {{
"theme": "1",
"block": "3",
"title1": "Новые клиенты за сегодня",
"img1": "static/img/bg.jpg",
"text1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title2": "Новые клиенты за сегодня",
"img2": "static/img/bg.jpg",
"text2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"title3": "Новые клиенты за сегодня",
"img3": "static/img/bg.jpg",
"text3": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"img-src1": "static/img/bg.jpg",
"video1": "static/video/vid.mp4"}}
        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(yse3, dat, indent=2, ensure_ascii=False)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,debug=True)




