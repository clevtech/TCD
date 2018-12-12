
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
import pymongo
import random
from pprint import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import random
from threading import Lock



async_mode = None

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users
nums = random.random()

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

message = {}

@app.route('/ok')
def my_form():
    global block
    global text
    my_ip = "192.168.1.1"
    name = 'hi!'
    return render_template ('index(me).html', **locals()) #моя адмика


@app.route('/ok', methods=['GET' ,'POST'])
def my_form_post():
    global title
    global car
    global text
    global b
    title = request.form['title'] #имя в скобках (и в html) влияет на их передачу в <div id = ''>
    num = random.random()
    car = request.form['image']
    print(car)
    uri = 'static/img/' + car
    vid = request.form['video']
    urii = 'static/vid/' + vid
    text = request.form['text']
    print(text)
    rad = request.form['radio']
    if rad == 'yes':
        frid = 1
    if rad == 'no':
        frid = 2
    if rad == 'ok':
        frid = 3
    block = request.form['block']
    i = 0
    print(block)
    block = int(block) #очень станно когда просто int(block) он выдает ошибку а с параметром block = int(block) пишет что все ок нужно узнать почему так
    while i < block:
        i = i + 1
        a = {i}
        b = {
                      "title": "Новые клиенты за сегодняeqweqw",
                      "img": "static/img/bg.jpg",
                      "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
                        "num": i
            }

        print(b)
        # user.insert(message)
    return render_template('index(me).html', **locals())



@app.route('/', methods = ['GET', 'POST'])
def mark_selected():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/button/<value>/', methods = ['GET', 'POST'])
def button(value=0):
    global title
    global text
    global car
    global message
    print("Value from button: " + value)
    print("Now we changed theme")
    if int(value) == 1:
        message = {
                "_id": "1",
                "theme": "1",
                "block": "1",
                "num": value,
                "test": [
                  {
                  "title": "Новые клиенты за сегоднsdasdя",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
                  },
                  {
                  "title": "Новые клиенты за сегодняeqweqw",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                  {
                  "title": "Новые клиенты за сегодня",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  }

                ],
                "img-src1": "static/img/bg.jpg",
                "video1": "static/video/vid.mp4"
                }

        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(message, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги

    elif int(value) == 2:
        message = {
                "_id": "1",
                "theme": "1",
                "block": "2",
                "num": value,
                "test": [
                  {
                  "title1": "Новые клиенты за сегоднsdasdя",
                  "img1": "static/img/fon.jpg",
                  "text1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                  {
                  "title": "Новые клиенты за сегодняeqweqw",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                  {
                  "title": "Новые клиенты за сегодня",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                ],
                "img-src1": "static/img/bg.jpg",
                "video1": "static/video/vid.mp4"
                }
        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(message, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги

    elif int(value) == 3:
        message = {
                "_id": "1",
                "theme": "1",
                "block": "3",
                "num": value,
                "test": [
                  {
                  "title": "Новые клиенты за сегоднsdasdя",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                  {
                  "title": "Новые клиенты за сегодняeqweqw",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!"
                  },
                  {
                  "title": "Новые клиенты за сегодня",
                  "img": "static/img/bg.jpg",
                  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
                    "video": "static/video/vid.mp4"
                  },
                ],
                "img-src1": "static/img/bg.jpg",
                "video1": "static/video/vid.mp4"
                }

        with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(message, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги
    print(message)
    return render_template('main.html', async_mode=socketio.async_mode)


# То что крутиться на заднем фоне
def background_thread():
    global message
    old_msg = message
    while True:
        # Спит 0.1 секунду
        socketio.sleep(1)
        if old_msg == message:
            print("Old one")
            pass
        else:
            old_msg = message
            print("New one")
            socketio.emit('my_response',
                          message,
                          namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)



@app.route('/ek')
def ek():
    return render_template('main.html', async_mode=socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888,debug=True)








# try:
#     global a
#     print(type(a))
#     js = {'_id':a}
#     user.insert(js)
# except:
#     global summ
#     num = str(1000)
#     print(type (num))
#     while a > num:
#         a = a + str(1)
#         print(a)
#         a = summ
