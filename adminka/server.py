#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Cleverest Technologies"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"


import gevent.monkey
gevent.monkey.patch_all()
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
import json
import socket
from pymongo import*
from pymongo import MongoClient


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

## Functions
def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

ip = get_ip()

## Classes
class Click:
	def __init__(self, ID, ekran, lang="ru"):
		self.ID = ID
		self.daughters = []
		# 	{
		#   "title": "Первая кнопка",
		# 		"img": "static/image/bg.jpg",
		# 		"text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, attest2!",
		# 		"ID": "2.2.1" # Айди кнопки
		# }
		self.parents = []
		# 	{
		#   "title": "Первая кнопка",
		# 		"ID": "2"
		# }
		self.map = []
		#     {
		#       "number": "", # Номер области (1 - астана, 17 - чимкент)
		#       "ID": "" # Его Айди
		#     }
		self.content = []
		# {
		#     "type": "1", # 1 - картинка и текст, 2 - картинка, 3 - видео
		#     "title": "Новые клиенты за сегодня",
		# 	  "img": "static/image/bg.jpg",
		# 	  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
		# 	  "video": "static/video/"
		#       }
		self.theme = 1 # TODO: when zhamal finishes
		self.logo = ""
		self.type = ""
		self.lang = lang
		self.ekran = ekran
		self.slide = ""

	def read_database(self):
		gl = list(users.find({"ID": self.ID})) # find({'files':{'$regex':'^File'}})
		print(gl)

#
# Adam = Click("2.2", "1")
# Adam.read_database()

## Socket
@socketio.on('my event', namespace="/") # Принимать сигналы и отправлять
def handle_my_custom_namespace_event(json1):
	print(json1)
	socketio.sleep(0.1)
	socketio.emit('my_response',
				  {'data': str(random.random()), 'count': "1"})


## Render
@app.route('/<ekran>/<lang>/') # Вывод на планшеты
def tablet(ekran, lang):
	# return render_template('index.html', async_mode=socketio.async_mode, ip=ip)
	return render_template('btest.html', async_mode=socketio.async_mode, ip=ip)


@app.route('/click/<ekran>/<lang>/<id>')
def clicked(ekran, lang, id):
	print(id)
	return "200"


@app.route('/disp/<ekran>/<lang>') # Вывод на экраны
def ekrany(ekran, lang):
	print(ekran)
	return render_template('main.html', async_mode=socketio.async_mode, ip=ip)


if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=8888, debug=True)
