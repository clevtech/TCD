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

def bread_read(my_json):
        f = open('static/bread.txt', 'a')
        my_jsn = my_json
        my_jsn = my_jsn["num"]
        # print(my_jsn )

        f.write( '' + my_jsn + '' + '/')
        f.close()
        f = open('static/bread.txt', 'r')
        read_file = f.read()
        show_to_path = print(read_file)
        f.close()
        return



@app.route('/', methods = ['GET', 'POST'])
def mark_selected():
    return render_template('index.html', async_mode=socketio.async_mode)


# @app.route('/<new_breads>/', methods = ['GET', 'POST'])
# def my_bread(new_breads):
#     f = open('static/bread.txt', 'r')
#     bread = f.read()
#     f.close()
#     print("hi")
#     textlookfor = r"(?!/)[\d+.\d+]+"
#     allresults = re.findall(textlookfor, bread)
#     # bread = len(allresults)
#     # print(allresults)
#     my_bread  = new_breads
#     print(my_bread)
#     # button(value = my_bread )
#     allresults.index(my_bread)
#     index_bread = (allresults.index(my_bread))
#     button(value = allresults[index_bread])
#     return render_template('index.html', async_mode=socketio.async_mode, name = new_breads)
#


@socketio.on('message', namespace='/server')
def my_msg(message):
    print('message', {'data': message})
    with open('static/json/data.json', 'r', encoding='utf-8') as data: # открывает json файл "W"- это команда на запись (write, read)
        my_json = json.load(data)
        print(my_json["test"])




def my_short_algoritm(value, results):
    parent= str(value) + "."
    lenofp = len(parent)
    parentnum = parent.split(".")
    lenofnumparent = len(parentnum)
    # print(lenofnumparent)
    slides = []
    for el in results:
        line = str(el)
        number = line.split(".")

        print(number)
        # print(len(number))
        slides.append(line)

    print("Our daughters are:")
    print(slides)
    dau = []
    for el in slides:
        if len(el.split("."))==lenofnumparent:
            if el[0:lenofp] == parent:
                dau.append(el)
    lenght = len(dau)
    dau.sort()
    print(dau)
    list_numbers = list(dau)
    print(list_numbers)
    return list_numbers



@app.route('/button/<value>/', methods = ['GET', 'POST'])
@socketio.on('message', namespace='/server')
def button(value):
    global title
    global text
    global car
    global z
    print("Value from button: " + str(value))
    print("Now we changed theme")
    gl = users.find({"ID":{"$gt": str(value), "$lt": str(value) + ".99"}})
    items = list(gl)
    print("Items are: ")
    print(items)
    print( ", ".join( repr(e) for e in items ) )
#     results = [ item['ID'] for item in items ]
#     # print("Values from MongoDB: ")
#     # print(results)
#
# ## Algorithm for taking daughters
#     list_numbers = my_short_algoritm(value, results)
#     ## Till here
#     find_user = users.find({"ID":{"$in" : list_numbers}})
#     sort_id = list(find_user)

    # print(sort_id)
    write2 = []
    with open('static/json/data.json', 'r', encoding='utf-8') as dat: # открывает json файл "W"- это команда на запись (write, read)
        global my_json
        my_json = json.load(dat)
        # write2.extend(my_json["test"])
        write2.extend(items)
        # print(my_json["test"])
        # print(my_json["block"])
        # print(my_json["test"])
        print(write2)
        print( ", ".join( repr(e) for e in write2 ) )
        my_val = str(value)




        # del (my_json["test"])[:]
        # # print(my_json)
        # my_json["test"].extend(sort_id)
        # my_json["num"] = str(value)
        #
        # ## TODO: Check is there video, if so - send 3, if only img send 2, if text+img send 1
        # print(sort_id)

        # bread_read(my_json)
    with open("static/json/data.json", "w") as der :
        jsn = json.dump(write2, der, indent=2, ensure_ascii=False )
    background_thread(my_json)
    return render_template('index.html', async_mode=socketio.async_mode)




# # TODO: def to change display content
# def display_it(value):
#     global message
#     print(value)
#     message = {}
#     if value["num"] != "":
#         message = value




# То что крутиться на заднем фоне
def background_thread(message):
    old_msg = ""

    print(message)
    # Спит 0.1 секунду
    socketio.sleep(1)
    if message != {}:
        if old_msg != message:
            print("Message is: ")
            print(message)
            old_msg = message
            print("New one")
            socketio.emit('my_response',
                          message,
namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


@app.route('/ek')
def ek():
    return render_template('main.html', async_mode=socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888,debug=True)

