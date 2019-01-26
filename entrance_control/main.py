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
import base64


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def welcome():
	return render_template('index.html')


@app.route('/give/', methods=['GET','POST'])
def give(val="face"):
	if request.method == 'POST':
		if request.form['file']:
			with open("static/udo.png", "wb") as fh:
				fh.write(base64.decodebytes(request.form['file'].split("base64,")[1].encode()))
			gg = 1
			if gg == 1:
				text = "Улыбнитесь"
				return render_template('camera_face.html', text = text)
			else:
				text = "Штрих код не видно"
				return render_template('camera.html', text = text)
		else:
			with open("static/face.png", "wb") as fh:
				fh.write(base64.decodebytes(request.form['face'].split("base64,")[1].encode()))
			return render_template('index.html')
	else:
		text = "Поднесите ИИН штрих код и нажмите отправить"
		return render_template('camera.html', text = text)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True)
