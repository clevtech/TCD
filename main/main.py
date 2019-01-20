#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Cleverest Technologies"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

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
from flask import Markup
import copy


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


 # Classes
class Click:
	def __init__(self, ID, lang="ru", path='mongodb://localhost:27017/',db_name="NOtest", collection_name="old", path_to_json="static/json/data.json"):
		self.client = MongoClient(path)
		self.db = self.client[db_name]

		self.lang = lang
		if lang == "kz":
			self.data_from_DB = self.db[collection_name + "KZ"]
		else:
			self.data_from_DB = self.db[collection_name]

		self.json_path = path_to_json
		self.id = ""
		self.ID = ID
		self.me = dict()
		self.ip = ""
		self.title = ""
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
		#     "type": "1", # 1 - картинка и текст, 2 - картинка, 3 - видео, 4 - карта
		#     "title": "Новые клиенты за сегодня",
		# 	  "img": "static/image/bg.jpg",
		# 	  "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
		# 	  "video": "static/video/"
		#       }
		self.theme = 1 # TODO: when zhamal finishes
		self.logo = ""
		self.type = ""
		self.ekran = ID[0]
		self.slide = ""
		self.raw = []
		# TODO: write names of displays and logo paths
		self.names = ["1","1","1","1","1","1"]
		self.biglogos = ["1","1","1","1","1","1"]
		self.expor = dict()

		self.get_ip()
		self.read_db()
		self.give_static_values()
		self.obtain_type()
		self.generate_content()
		self.populate_parents()
		self.populate_kids()
		self.export()
		self.write_to_json()


	def read_db(self):
		self.raw = list(self.data_from_DB.find({"name": self.ekran}))
		try:
			self.me = list(self.data_from_DB.find({"ID": self.ID}))[0]
			self.id = str(self.me["_id"])
		except:
			self.me["logo_title"] = self.names[int(self.ID[0]) - 1]
			self.me["logo_path"] = self.biglogos[int(self.ID[0]) - 1]
			self.me["slide_max"] = "0"
			self.id = str("213123123")
			self.me["content"] = []


	def give_static_values(self):
		self.logo = self.ip + "/static" + self.me["logo_path"]
		# self.theme = self.ekran TODO: then do it
		self.title = self.me["logo_title"]
		self.slide = self.me["slide_max"]


	def obtain_type(self): # 0 - 1 slide, 1 - map, 2 - 1+ slides
		try:
			if self.me["content"][0]["map"] != "":
				self.type = "1"
			elif len(self.me["content"]) > 1:
				self.type = "2"
			else:
				self.type = "0"
		except:
			self.type = '0'


	def generate_content(self):
		for el in self.me["content"]:
			post = dict()
			post["type"] = ""
			post["title"] = el["title"]
			try:
				l = el["img"]
			except:
				el["img"] = ""
			if el["img"] == "":
				post["img"] = self.ip + "/static" + self.me["logo_path"]
			if el["map"] != "":
				post["img"] = self.ip + "/static" + el["map"] + ".png"
				post["type"] = "4"
			if el["img_path"] != "":
				post["img"] = self.ip + "/static" + el["img_path"]
			if post["img"] != "" and el["text"] == "":
				post["type"] = "1"
			if el["video"] != ":":
				post["video"] = self.ip + "/static" + el["video"]
			post["text"] = el["text"]
			if el["video"] != "" and post["type"] == "":
				post["type"] = "3"
			if post["type"] == "":
				post["type"] = "2"
			print(post["type"])
			self.content.append(copy.deepcopy(post))
			post.clear()


	def populate_parents(self):
		try:
			list_of_man = self.ID.split(".")[:-1]
		except:
			self.parents = []
			return 0
		father_name = ""
		for man in list_of_man:
			if len(father_name) > 0:
				father_name += "." + man
			else:
				father_name += man
			self.parents.append(father_name)


	def populate_kids(self):
		kids_surname = len(self.ID) + 2
		kids_IDs = []
		for kid in self.raw:
			if len(kid["ID"]) == kids_surname and kid["ID"][:-2] == self.ID: # and kid["lang"] == self.lang:
				child = dict()
				child["ID"] = kid["ID"]
				child["title"] = kid["logo_title"]
				child["img"] = self.ip + "/static" + kid["logo_path"]
				try:
					child["text"] = kid["content"][0]["text"]
				except:
					child["text"] = child["title"]
				self.daughters.append(copy.deepcopy(child))
				child.clear()


	def get_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			# doesn't even have to be reachable
			s.connect(('10.255.255.255', 1))
			IP = s.getsockname()[0]
		except:
			IP = '127.0.0.1'
		finally:
			s.close()
		self.ip = "http://" + IP + ":8888"


	def export(self):
		slide = self.ID + "(" + str(self.slide) + ')'
		self.expor = dict()
		self.expor["id"] = self.id
		self.expor["ID"] = self.ID
		self.expor["theme"] = self.theme
		self.expor["ID"] = self.ID
		self.expor["theme"] = self.theme
		self.expor["ekran"] = self.ekran
		self.expor["lang"] = self.lang
		self.expor["logo"] = self.logo
		self.expor["type"] = self.type
		self.expor["map"] = []
		self.expor["slide"] = slide
		self.expor["dochki"] = self.daughters
		self.expor["roditeli"] = self.parents
		self.expor["content"] = self.content


	def write_to_json(self):
		with open(self.json_path, 'w') as outfile:
			json.dump(self.expor, outfile)


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

ip = Markup("http://" + get_ip())


 ## Routes
@app.route('/tablet/<ekran>/<lang>/') # Вывод на планшеты
def tablet(ekran, lang):
	info = Click(ekran, lang)
	return render_template('index.html', ip=ip, ekran=Markup(ekran), lang=lang)


@app.route('/click/<ekran>/<lang>/<id>/')
def clicked(ekran, lang, id):
	print("Click from: " + ekran + " to ID: " + id)
	info = Click(id, lang)
	pprint(info.expor)
	return jsonify(info.expor)


@app.route('/disp/<ekran>/<lang>/') # Вывод на экраны
def ekrany(ekran, lang):
	info = Click(ekran, lang)
	return render_template('main.html', ip=ip, lang=lang, ekran=ekran)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True)
