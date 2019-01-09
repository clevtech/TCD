import csv
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
filename = 'static/forms/nurform.csv'


@app.route('/', methods = ['GET', 'POST'])
def button(value=0):

    # gl = users.find({"ID":{"$gt": str(value), "$lt": str(value) + ".99"}})
    # items = list(gl)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777,debug=True)
