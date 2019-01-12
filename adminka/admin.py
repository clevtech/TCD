import requests
import glob
from flask import Flask
import os
from pprint import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import random
from threading import Lock
from pymongo import*
from pymongo import MongoClient
import csv

async_mode = None                                       


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["nurotan"]
users = db.users
nums = random.random()

thread = None
thread_lock = Lock()
socketio = SocketIO(app, async_mode=async_mode)

@socketio.on('message', namespace='/server')
def msg(message):
    print("message is: " + message)


# def structure_number_one(): #ПАРТИЯ «НҰР ОТАН»
#     users.insert({})





# def structure_number_tree(): #МОЛОДЕЖНОЕ КРЫЛО «ЖАС ОТАН»
#     users.insert({})
#
#
# def structure_number_four(): #РЕСПУБЛИКАНСКАЯ ОБЩЕСТВЕННАЯ ПРИЕМНАЯ
#     users.insert({})




# @app.route('/', methods = ['GET', 'POST'])
# def mark_selected():
#     return render_template('indexZM.html', async_mode=socketio.async_mode)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)
