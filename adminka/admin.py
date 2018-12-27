import requests
import glob
import os
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
import pymongo
import random
from pprint import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import random
from threading import Lock
from flask_cors import CORS, cross_origin


async_mode = None

app = Flask(__name__)
CORS(app,support_credentials=True, resources={r"/*": {"origins": "*"}})
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users
nums = random.random()

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

message = {}

@app.route('/', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def mark_selected():
    request.headers.get ('Access-Control-Allow-Origin:*')
    return render_template('index.html', async_mode=socketio.async_mode)


def cycle(a, value):
    head = ""
    tail = ""
    write2 = []
    i = 0
    for el in a:
        with open(el, 'r', encoding='utf-8') as fh: #открываем файл на чтение
            data = json.load(fh) #загружаем из файла данные в словарь data type dict
            # print(data["test"])
            write2.extend(data["test"])
    with open("static/json/data.json", "r") as der :
        old = json.load(der)
        # print(old["test"])
        old["test"].extend(write2)
        print(old["test"])
        old["num"] = value
        print(old)
    with open("static/json/data.json", "w") as der :
        jsn = json.dump(old, der, indent=2, ensure_ascii=False )






@app.route('/button/<value>/', methods = ['GET', 'POST'])
@cross_origin()
def button(value=0):
    global title
    global text
    global car
    global z
    global num1
    global num2
    print(value)
    gl = glob.glob("static/database/" + str(value) +  "*.json", recursive=True) #type list
    print(gl)
    i = 0

    # ## Algorithm for taking daughters
    #
    # parent= str(value) + "."
    # lenofp = len(parent)
    # parentnum = parent.split(".")
    # lenofnumparent = len(parentnum)
    # print(lenofnumparent)
    # slides = []
    # for el in gl:
    #     line = str(el).split("database/")[1].split("json")[0]
    #     number = line.split(".")
    #     print(number)
    #     print(len(number))
    #     slides.append(line)
    #
    # print("Our daughters are:")
    # dau = []
    # for el in slides:
    #     if len(el.split("."))==lenofnumparent+1:
    #         if el[0:lenofp] == parent:
    #             dau.append(el)
    #
    # lenght = len(dau)
    # dau.sort()
    # print(dau)
    # ## Till here
    #
    # paths = []
    #
    # while i < lenght:
    #     a = "static/database/" +dau[i].lstrip()+ "json"
    #     print(a)
    #     paths.append(a)
    #     i = i + 1
    #
    # cycle(paths, value)




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





