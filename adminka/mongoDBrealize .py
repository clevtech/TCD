import requests
import glob
import os
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
import random
import re
from pprint import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import random
from threading import Lock
from pymongo import*
from pymongo import MongoClient


ip = "192.168.8.100"
async_mode = None

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["nurotan"]
users = db.users
nums = random.random()

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

message = {}

def bread_read(my_json):
        f = open('static/bread.txt', 'a')
        my_jsn = my_json
        my_jsn = my_jsn["num"]
        # print(my_jsn )

        f.write( '' + my_jsn + '' + '/')
        f.close()
        f = open('static/bread.txt', 'r')
        read_file = f.read()
        show_to_path = print(read_file)
        f.close()
        return



@app.route('/', methods = ['GET', 'POST'])
def mark_selected():
    return render_template('index.html', async_mode=socketio.async_mode, ip=ip)


@app.route('/1', methods = ['GET', 'POST'])
def one():
    button(value = 2)
    msg = {
          "ID": "2",
          "_id": 5141241249,
        "theme":"1",
          "block": "1",
          "form": "",
          "logo": "static/image/logo.png",
          "logoHome": "static/image/home.png",
          "logoLeft": "static/image/left.png",
          "logoRight": "static/image/right.png",
          "name": "2.2",
          "num": "3.2",
          "test": [
            {
              "ID": "2.2",
              "_id": 0.447690146841,
              "block": "1",
              "buttonLeft": "",
              "buttonReturn": "",
              "buttonRight": "",
              "form": "1.2",
              "img": "static/image/bg.jpg",
              "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
              "title": "Институт стратегических инициатив",
              "video": "static/video/"
            }
          ]
        }
    background_thread(msg)
    return render_template('index.html', async_mode=socketio.async_mode, ip=ip)





# @app.route('/button/<value>/', methods = ['GET', 'POST'])
# @socketio.on('message', namespace='/server')
def button(value):
    global title
    global text
    global car
    global z
    print("Value from button: " + str(value))
    print("Now we changed theme")
    gl = users.find({"ID":str(value)})
    items = list(gl)
    print("Items are: ")
    print(items)

        # ## TODO: Check is there video, if so - send 3, if only img send 2, if text+img send 1

    with open("static/json/data.json", "w") as der:
        jsn = json.dump(items[0], der, indent=2, ensure_ascii=False)
        print(items)
        background_thread(items[0])
    # return render_template('index.html', async_mode=socketio.async_mode, ip=ip)




# # TODO: def to change display content
# def display_it(value):
#     global message
#     print(value)
#     message = {}
#     if value["num"] != "":
#         message = value




# То что крутиться на заднем фоне
def background_thread(message):
    old_msg = ""

    print(message)
    # Спит 0.1 секунду
    socketio.sleep(1)

    if message != {}:
        if old_msg != message:
            print("Message is: ")
            print(message)
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

@socketio.on('message', namespace='/server')
def my_msg(message, message2):
    print('message is: ' "+" ,message ,"+" 'json:',message2)
    button(message)
    disp(message2)


@socketio.on('my_disp', namespace='/disp')
def disp(message2):
    print("disp connected!")
    socketio.emit('my_disp',message2 , namespace='/disp')



@app.route('/ek')
def ek():
    return render_template('main.html', async_mode=socketio.async_mode, ip=ip)

@app.route('/e')
def em():
    return ("HELLO")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888,debug=True)

