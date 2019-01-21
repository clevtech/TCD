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
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4', 'mpeg4'])

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
client = MongoClient("mongodb://localhost:27017/")
db = client["NOtest"]


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


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True)
