import requests
import glob
import os
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
import random
from pprint import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import random
from threading import Lock
from flask_cors import CORS, cross_origin
from pymongo import*
from pymongo import MongoClient

async_mode = None

app = Flask(__name__)
CORS(app,support_credentials=True, resources={r"/*": {"origins": "*"}})
client = MongoClient('mongodb://localhost:27017/')
db = client["test"]
users = db.users
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


# def cycle(a):
#     with open(a, 'r', encoding='utf-8') as fh: #открываем файл на чтение
#         data = json.load(fh) #загружаем из файла данные в словарь data
#         print(data)
#
#     with open("static/json/mydata.json", "w") as der :
#         jsn = json.dump(data, der, indent=2, ensure_ascii=False )


@app.route('/button/<value>/', methods = ['GET', 'POST'])
@cross_origin()
def button(value=0):
    global title
    global text
    global car
    global z

    print("Value from button: " + value)
    print("Now we changed theme")

    # for i in range(1, 5):
    #     add_user = {"_id":random.random(), "ID": "2." + str(i) + ".1"}
    #
    #     users.insert(add_user)
    #     err_find = users.find()

    gl = users.find({"ID":{"$gt": str(value), "$lt": str(value) + ".99"}})
    items = list(gl)
    print(items)

    results = [ item['ID'] for item in items ]

    print(results)

## Algorithm for taking daughters

    parent= str(value) + "."
    lenofp = len(parent)
    parentnum = parent.split(".")
    lenofnumparent = len(parentnum)
    # print(lenofnumparent)
    slides = []
    for el in results:
        line = str(el)
        number = line.split(".")

        print(number)
        # print(len(number))
        slides.append(line)

    print("Our daughters are:")
    dau = []
    for el in slides:
        if len(el.split("."))==lenofnumparent:
            if el[0:lenofp] == parent:
                dau.append(el)
    lenght = len(dau)
    dau.sort()
    # print(dau)
    list_numbers = list(dau)
    print(list_numbers)
    # if list_numbers2 ==

    algorithm_for_short = dau[0]
    # if algorithm_for_short == numbers:



    ## Till here
    find_user = users.find({"ID":{"$in" : dau}})
    sort_id = list(find_user)
    print(sort_id)
    with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
            jsn = json.dump(sort_id, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги




        # with open('static/json/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
        #     jsn = json.dump(mymsg, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги


    #         jsn = json.dump(message, dat, indent=2, ensure_ascii=False ) # mep это зн7ачение которому присвоено наше json значение из монги


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





