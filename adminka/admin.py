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

async_mode = None

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["test"]
users = db.users
nums = random.random()

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()



@app.route('/', methods = ['GET', 'POST'])
def mark_selected():
    return render_template('index.html', async_mode=socketio.async_mode)


# То что крутиться на заднем фоне
def background_thread():


    message = {
"test": [
{
  "ID": "3.1",
  "_id": 0.4447193690146881,
  "img": "static/img/fon.jpg",
  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at3.2!",
  "title": "Новые клиенты за сегоднsdasdя"
},
{
  "ID": "3.2",
  "_id": 0.8919366036324966,
  "img": "static/img/fon.jpg",
  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at3.2!",
  "title": "Новые клиенты за сегоднsdasdя"
},
{
  "ID": "3.3",
  "_id": 0.587351931604674,
  "img": "static/img/fon.jpg",
  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at3.2!",
  "title": "Новые клиенты за сегоднsdasdя"
}
]
}
    print(message)
    # Спит 0.1 секунду
    socketio.sleep(1)
    if message != {}:
            print("Message is: ")
            print(message)

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




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=7777, debug=True)
