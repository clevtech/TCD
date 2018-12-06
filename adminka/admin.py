








from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
import pymongo
import random
from pprint import pprint
import random
from threading import Lock



async_mode = None

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users
nums = random.random()

app.config['SECRET_KEY'] = 'secret!'




@app.route('/ok')
def ok():
    global blocks
    return render_template('DIVid.html', **locals())

@app.route('/')
def os():
    global blocks
    return render_template('DIVid.html', **locals())


@app.route('/', methods = ['GET', 'POST'])
def er():
    global blocks
    blocks = request.form['block']
    print(blocks)
    return redirect('http://0.0.0.0:8888/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,debug=True)







# a = input('passwd!:')
# g = int(a)
# n = 10000
# if g < int(n):
#
#     b =g + 1
#     print(b)


