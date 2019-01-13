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

users.insert({
"theme": "2",
"block": "2",
  "_id": 41241241212,
  "num": "2.2",
  "ID": "2.2",
  "form": "2",
"logo": "static/image/logo.png",
"logoLeft": "static/image/left.png",
"logoRight": "static/image/right.png",
"logoHome": "static/image/home.png",
"test": [
{
  "ID": "2.2.1",
"_id": 0.44471930146841,
"title": "Аналитическая деятельность",
"img": "static/image/bg.jpg",
"text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"video": "static/video/",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block": "2",
"form": "2",
  "theme":"2"
},
  {
    "name": "2.2",
  "ID": "2.2.2",
"_id": 0.4471936903481,
"title": "Работа с экспертным сообществом",
"img": "static/image/bg.jpg",
"text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"video": "static/video/",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block": "1",
"form": "2"
},
    {
  "ID": "2.2.3",
"_id": 0.190346841,
"title": "Информационно-разъяснительные материалы",
"img": "static/image/bg.jpg",
"text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"video": "static/video/",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block": "1",
"form": "2"
}

]
}

)


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


