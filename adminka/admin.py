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
import json
async_mode = None                                       


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["nurotan"]
users = db.users
nums = random.random()

thread = None
thread_lock = Lock()
socketio = SocketIO(app, async_mode=async_mode)


def import_it(ID):
    value = str(ID)

    gl = users.find({"ID":{"$gt": str(value), "$lt": str(value) + ".9"}})

    gl = list(gl)

    value2 = value
    leng = len(value2.split(".")) + 1
    daughters = []
    for el in gl:
        if len(el["ID"].split(".")) <= leng:
            daughters.append(el)

    gl2 = users.find({"ID":str(value)})
    it = list(gl2)


    parents_raw = ID.split(".")[0:-1]
    parents = []
    parent = ""
    for i in range(len(parents_raw)):
        if i == 0:
            parent = str(parents_raw[i])
        else:
            parent += "." + str(parents_raw[i])
        parents.append(parent)

    parents_final = []
    for parent in parents:
        gl3 = list(users.find({"ID":str(parent)}))
        parents_final.extend(gl3)
    return it, parents_final, daughters

x, y, z = import_it("3.1")
print(x)
print(y)
print(z)

@socketio.on('mydisp', namespace='/mydisp')
def handle_message(message):
    print('received message: ' + message)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)



