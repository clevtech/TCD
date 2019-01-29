#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Cleverest Technologies"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"


from gevent import monkey
monkey.patch_all()

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
from werkzeug.utils import secure_filename
import base64
import telepot



UPLOAD_FOLDER = '/home/akbota/TCD/main/static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4', 'mpeg4'])



async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
client = MongoClient("mongodb://localhost:27017/")
db = client["NOtest"]


# Propusk
def send_tlg_msg(msg, ids, photo):
	x = 1
	bot = telepot.Bot('636656567:AAGJNwvclwoJLHoice4DJkS_03H3m5Fpmso')
	for id in ids:
		try:
			bot.sendPhoto(str(id), photo, caption=msg)
		except:
			pass


@app.route('/zayavka/', methods=['GET','POST'])
def welcome2():
	return render_template('zayava.html', text = "Введите данные:")


@app.route('/zayavka/check/', methods=['GET','POST'])
def welcome3():
	text = request.form['FIOin'] + ":" + request.form['FIOout'] + ":" + request.form['room']
	first = random.choice(range(1, 10))
	leftover = set(range(10)) - {first}
	rest = random.sample(leftover, 5)
	digits = [first] + rest
	name = ''
	for let in digits:
		name += str(let)
	print("name is " + str(name))
	print("value is " + text)
	with open('./static/logs/' + name + '.txt', "w") as file:
		data = file.write(text)
	return render_template('zayava.html', text = "Код доступа: " + str(name))


@app.route('/propusk/')
def welcome():
	return render_template('index3.html')


@app.route('/give/', methods=['GET','POST'])
def give():
	return render_template('enter.html')


@app.route('/photo/', methods=['GET','POST'])
def ava():
	with open("static/face.png", "wb") as fh:
		fh.write(base64.decodebytes(request.form['file'].split("base64,")[1].encode()))
	return "200"


@app.route('/give/check/', methods=['GET','POST'])
def chechit():
	if request.method=="POST":
		kod = request.form['kod']
		try:
			with open('./static/logs/' + kod + '.txt', "r") as file:
				data = file.readline()
				data2 = data.split(":")
				data3 = "Заказал пропуск: " + str(data2[0])
				data3 += ", в кабинет: : " + str(data2[2])
				data3 += ", для гражданина: : " + str(data2[1])
				send_tlg_msg(data3, ['-1001403922890'], open('./static/face.png', "rb"))
		except:
			return render_template('index2.html', text=Markup("Вы ввели неправильный пароль"))
		return render_template('index2.html', text=Markup("Входите"))


# Admin pages

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_logo/<ID>/<lang>', methods=['GET', 'POST'])
def upload_logo(ID, lang):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = file.filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			data_from_DB.update_one({'ID': ID},{'$set': {'logo_path': "/img/" + filename}}, upsert=False)
			return redirect("/slide/" + ID + "/" + lang, code=302)
	return '''
	<!doctype html>
	<title>Upload new LOGO</title>
	<h1>Upload new LOGO</h1>
	<form method=post enctype=multipart/form-data>
	  <p><input type=file name=file>
		 <input type=submit value=Upload>
	</form>
	'''


@app.route('/upload_img/<ID>/<lang>/<slide>', methods=['GET', 'POST'])
def upload_img(ID, lang, slide):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = file.filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			line = list(data_from_DB.find({'ID': ID}))[0]
			line["content"][int(slide)]["img_path"] = "static/img/" + filename
			data_from_DB.delete_many({'ID': ID})
			data_from_DB.insert_one(line)
			return redirect("/slide/" + ID + "/" + lang, code=302)
	return '''
	<!doctype html>
	<title>Upload new LOGO</title>
	<h1>Upload new IMAGE</h1>
	<form method=post enctype=multipart/form-data>
	  <p><input type=file name=file>
		 <input type=submit value=Upload>
	</form>
	'''


@app.route('/upload_vid/<ID>/<lang>/<slide>', methods=['GET', 'POST'])
def upload_vid(ID, lang, slide):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = file.filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			line = list(data_from_DB.find({'ID': ID}))[0]
			line["content"][int(slide)]["video"] = "static/img/" + filename
			data_from_DB.delete_many({'ID': ID})
			data_from_DB.insert_one(line)
			return redirect("/slide/" + ID + "/" + lang, code=302)
	return '''
	<!doctype html>
	<title>Upload new LOGO</title>
	<h1>Upload new VIDEO</h1>
	<form method=post enctype=multipart/form-data>
	  <p><input type=file name=file>
		 <input type=submit value=Upload>
	</form>
	'''


@app.route('/delete/<ID>/<lang>', methods=['GET', 'POST'])
def delete(ID, lang="ru"):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]
	myquery = { "ID": ID }
	try:
		data_from_DB.delete_many(myquery)
		print("deleted old one")
	except:
		pass
	return redirect("/admin/" + ID[0] + "/" + lang, code=302)


@app.route('/add/<ID>/<lang>', methods=['GET', 'POST'])
def add(ID, lang="ru"):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	regx = re.compile("^" + ID, re.IGNORECASE)
	value = list(data_from_DB.find({"ID": regx}))
	data = []
	print(ID.split("."))
	print(len(ID.split(".")))
	leng = len(ID.split("."))
	for el in value:
		if len(el["ID"].split(".")) == leng + 1:
			data.append(el)
	IDnew = ID + "." + str(len(data))
	olddata = list(data_from_DB.find({"ID": ID}))[0]
	slide = { "name" : ID[0], "ID" : IDnew, "logo_title" : olddata["logo_title"], "logo_path" : olddata["logo_path"], "slide_max" : 1, "slide_now" : 1, "content" : [{"title" : "NEW ADDED", "img_path" : "", "video" : "", "map" : "", "text" : ""}]}
	data_from_DB.insert_one(slide)
	slide.clear()
	return redirect("/admin/" + ID[0] + "/" + lang, code=302)


@app.route('/delete_slide/<ID>/<lang>/<slide>', methods=['GET', 'POST'])
def delete_slide(ID, lang="ru", slide="0"):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]
	myquery = { "ID": ID }
	value = list(data_from_DB.find(myquery))[0]
	try:
		data_from_DB.delete_many(myquery)
		print("deleted old one")
	except:
		pass

	del value["content"][int(slide)]
	data_from_DB.insert_one(value)

	return redirect("/slide/" + ID + "/" + lang, code=302)


@app.route('/slide/<ID>', methods=['GET', 'POST'])
@app.route('/slide/<ID>/<lang>', methods=['GET', 'POST'])
@app.route('/slide/<ID>/<lang>/<more>', methods=['GET', 'POST'])
def admin(ID, lang="ru", more="0"):
	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	if request.method == 'POST':

		data = request.values
		print(data)
		raw = {}
		raw["logo_title"] = data["logo_title"]
		raw["logo_path"] = data["logo_path"]
		raw["name"] = ID[0]
		raw["slide_now"] = "1"
		raw["ID"] = ID
		num = 0
		for i in range(100):
			try:
				g = data["title" + str(i)]
				num += 1
			except:
				break
		raw["slide_max"] = num
		raw["content"] = []
		line = {}
		for i in range(num):
			print("Line #: ")
			print(i)
			title = data["title" + str(i)]
			img_path = data["img_path" + str(i)]
			map = data["map" + str(i)]
			video = data["video" + str(i)]
			text = data["text" + str(i)]
			line = {"title": title, "img_path": img_path, "map": map, "video": video, "text": text}
			raw["content"].append(copy.deepcopy(line))
			line.clear()
		myquery = { "ID": ID }
		try:
			data_from_DB.delete_many(myquery)
			print("deleted old one")
		except:
			pass
		print("raw is: ")
		print(raw)
		data_from_DB.insert_one(raw)
		return redirect("/slide/" + ID + "/" + lang, code=302)

	raw = list(data_from_DB.find({"ID": ID}))[0]
	print(list(data_from_DB.find({"ID": ID})))

	logo_title = raw["logo_title"]
	logo_path = raw["logo_path"]
	value = ''
	for i in range(len(raw["content"])):
		el = raw["content"][i]
		value = value + "<h5> Slide №" + str(i) + "</h5>"
		title = el["title"]
		img_path = el["img_path"]
		video = el["video"]
		map = el["map"]
		text = el["text"]

		value = value + str('Title: <br><input type="text" name="') + str("title") + str(i) + '" value="' + str(title) + '"><a href="/delete_slide/' + ID + '/' + lang + '/' + str(i) + '"> [DELETE SLIDE]</a><br>'
		value = value + str('Image: <br><img width="100" src="/' + str(img_path) + '"></img><br><input type="text" name="') + str("img_path") + str(i) + '" value="' + str(img_path) + '"><br><a href=/upload_img/' + ID + '/' + lang + '/' + str(i) + '>Change it<br></a>'
		value = value + str('Video: <br><input type="text" name="') + str("video") + str(i) + '" value="' + str(video) + '"><br><a href=/upload_vid/' + ID + '/' + lang + '/' + str(i) + '>Change it<br></a>'
		value = value + str('Map: <br><input type="text" name="') + str("map") + str(i) + '" value="' + str(map) + '"><br>'
		value = value + str('Text: <br><textarea name="') + str("text") + str(i) + '">' + str(text) + '</textarea><br><hr>'
	if more == "1":
		i = len(raw["content"])
		value = value + "<h5> Slide №" + str(i) + "</h5>"
		title = ""
		img_path = ""
		video = ""
		map = ""
		text = ""
		value = value + str("New slide") + "<br><br>"
		value = value + str('Title: <br><input type="text" name="') + str("title") + str(i) + '" value="' + str(title) + '"><a href="/delete_slide/' + ID + '/' + lang + '/' + str(i) + '"> [DELETE SLIDE]</a><br>'
		value = value + str('Image: <br><img width="100" src="/' + str(img_path) + '"></img><br><input type="text" name="') + str("img_path") + str(i) + '" value="' + str(img_path) + '"><br><a href=/upload_img/' + ID + '/' + lang + '/' + str(i) + '>Change it<br></a>'
		value = value + str('Video: <br><input type="text" name="') + str("video") + str(i) + '" value="' + str(video) + '"><br><a href=/upload_vid/' + ID + '/' + lang + '/' + str(i) + '>Change it<br></a>'
		value = value + str('Map: <br><input type="text" name="') + str("map") + str(i) + '" value="' + str(map) + '"><br>'
		value = value + str('Text: <br><textarea name="') + str("text") + str(i) + '">' + str(text) + '</textarea><br><hr>'

	value = value + "<a href='/slide/" + ID + "/" + lang + "/1'> Add more </a>"

	return render_template('admin_slide.html', content=Markup(value), logo_title=logo_title, logo_path=logo_path, ID = ID, lang = lang, ekran=ID[0])


@app.route('/admin/', methods=['GET', 'POST']) # Вывод на экраны
@app.route('/admin/<ekran>', methods=['GET', 'POST']) # Вывод на экраны
@app.route('/admin/<ekran>/<lang>', methods=['GET', 'POST'])
def tree(ekran="1", lang="ru"):

	if request.method == 'POST':
		ekran = request.values.get('ekran')
		lang = request.values.get('lang')

	if lang == "kz":
		data_from_DB = db["old" + "KZ"]
	else:
		data_from_DB = db["old"]

	raw = list(data_from_DB.find({"name": ekran}))
	data = []
	elem = {}

	for el in raw:
		elem.clear()
		p = []
		elem["v"] = el["ID"]
		try:
			TITLE = str(el['content'][0]['title'])
		except:
			TITLE = "no title"

		try:
			LOGO = str(el['logo_path'])
		except:
			LOGO = "no logo"

		try:
			SLIDES = str(el["slide_max"])
		except:
			SLIDES = "no info"

		elem["f"] = "<h4>" + str(el["ID"]) + "</h4><br><img width='42' src='/static" + LOGO + "'></img><br><a href='/slide/" + str(el["ID"]) + "/" + lang + "'>" + TITLE + "</a><br>Slides: " + SLIDES
		elem["f"] = elem["f"] + "<br><a href='/delete/" + str(el["ID"]) + "/" + lang + "'>DELETE</a>"
		elem["f"] = elem["f"] + "<br><a href='/add/" + str(el["ID"]) + "/" + lang + "'>ADD</a>"
		p.append(copy.deepcopy(elem))
		if len(str(el["ID"]).split("."))>1:
			if len(str(el["ID"]).split(".")[-1]) > 1:
				p.append(str(el["ID"])[:-3])
			else:
				p.append(str(el["ID"])[:-2])
		else:
			p.append("")
		data.append(p)

	data = Markup(data)
	return render_template('admin.html', data=data)

## EKRANY
 # Classes
class Click:
	def __init__(self, ID, lang="ru", slide = "0", path='mongodb://localhost:27017/',db_name="NOtest", collection_name="old", path_to_json="static/json/data.json"):
		self.client = MongoClient(path)
		self.db = self.client[db_name]

		self.lang = lang
		if lang == "kz":
			self.data_from_DB = self.db[collection_name + "KZ"]
		else:
			self.data_from_DB = self.db[collection_name]

		self.json_path = "http://"
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
		self.slide = slide
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
		self.give_theme()
		self.export()
		self.write_to_json()

	def give_theme(self):
		if self.ekran == "1":
			self.theme = "2"
		elif self.ekran == "2":
			self.theme = "4"
		elif self.ekran == "3":
			self.theme = "3"
		elif self.ekran == "4":
			self.theme = "5"
		else:
			self.theme = "1"

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
				post["img"] = self.ip + "/" + el["img_path"]
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
				child["title"] = kid["content"][0]["title"]
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
		self.json_path = self.ip + "/static/json/data" + str(self.ID[0]) + ".json"
		self.json_path2 = "./static/json/data" + str(self.ID[0]) + ".json"


	def export(self):
		slide = self.ID + "(" + str(self.slide) + ')'
		self.expor = dict()
		self.expor["id"] = random.randint(0, 100)
		self.expor["ID"] = self.ID
		self.expor["theme"] = self.theme
		self.expor["ekran"] = self.ekran
		self.expor["lang"] = self.lang
		self.expor["logo"] = self.logo
		self.expor["type"] = self.type
		self.expor["map"] = []
		self.expor["slide"] = 0
		self.expor["dochki"] = self.daughters
		self.expor["roditeli"] = self.parents
		self.expor["content"] = self.content


	def write_to_json(self):
		with open(self.json_path2, 'w') as outfile:
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
@socketio.on('connect', namespace='/clicked')
def test_connect():
    print("Socket is started")


@app.route('/tablet/<ekran>/<lang>/') # Вывод на планшеты
def tablet(ekran, lang):
	info = Click(ekran, lang)
	return render_template('index.html', ip=ip, ekran=Markup(ekran), lang=lang, json_path=Markup(info.json_path))


@app.route('/click/<ekran>/<lang>/<id>/')
def clicked(ekran, lang, id):
	print("Click from: " + ekran + " to ID: " + id)
	info = Click(id, lang)
	pprint(info.expor)
	socketio.emit('my_response', ekran, namespace='/clicked')
	print("sended")
	return jsonify(info.expor)


@app.route('/click/<ekran>/<lang>/<id>/<napravlenie>')
def clicked_value(ekran, lang, id):
	print("Click from: " + ekran + " to ID: " + id)
	info = Click(id, lang)
	lenght = len(info.exor["content"])
	now = slide[0:-1]
	direction = slide[-1]
	if direction == "+":
		if now == lenght - 1:
			now = "0"
		else:
			now = str(int(now) + 1)
	elif direction == "-":
		if now == "0":
			now = str(lenght - 1)
		else:
			now = str(int(now) - 1)
	else:
		now = "0"
	print("########################################")
	print("#### Slide change ##########")
	print("########################################")
	print("Slide is: ")
	print(now)
	print("ID is: ")
	print(id)
	print("########################################")
	print("#### End of slide change ##########")
	print("########################################")
	info = Click(id, lang, now)
	return jsonify(info.expor)



@app.route('/disp/<ekran>/<lang>/') # Вывод на экраны
def ekrany(ekran, lang):
	json_path = ip + ":8888/static/json/data" + str(ekran) + ".json"
	return render_template('main.html', ip=ip, lang=lang, ekran=ekran, json_path=json_path)


@app.route('/') # Вывод на экраны
def glavnaia():
	return render_template('welcome.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)

# if __name__ == '__main__':
#     http_server = WSGIServer(('0.0.0.0', 8888), app)
#     http_server.serve_forever()
	# app.run(host='0.0.0.0', port=8888, debug=True)
