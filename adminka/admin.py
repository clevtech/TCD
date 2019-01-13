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
"name": "2.2",
"theme": "1",
"block": "1",
  "form": "1.2",
"num": "2.2.2",
"ID": "2.2.2",
"_id": 235235231240998,
"logo": "static/image/logo.png",
"logoLeft": "static/image/left.png",
"logoRight": "static/image/right.png",
"logoHome": "static/image/home.png",
"test": [
  {
  "ID": "2.2.2.1",
"_id": 0.44690356841,
"title": "Nur Otan Trends",
"img": "static/image/nurtrends.png",
"text": "Nur Otan Trends – дискуссионная площадка по обсуждению наиболее важных\nи значимых социальных и экономических аспектов развития общества с участием\nпредставителей государственных и общественных организаций, экспертов.",
"video": "",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block":"2",
"form": "1.2.1"
},
      {
  "ID": "2.2.2.2",
"_id": 0.444719360681,
"title": "Nur Otan Talks",
"img": "static/image/treads",
"text": "Nur Otan Talks – диалоговая площадка по обсуждению интересных тем,\nсобытий и явлений казахстанского общества, а также предоставление широкой\nобщественности возможности познакомиться с известными личностями страны.",
"video": "static/video/",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block":"2",
"form": "1.2.1"
},
      {
  "ID": "2.2.2.3",
"_id": 0.447360346841,
"title": "Резерв",
"img": "static/image/bg.jpg",
"text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
"video": "",
"buttonLeft": "",
"buttonRight": "",
"buttonReturn": "",
"block":"1",
"form": "1.2.1"
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


