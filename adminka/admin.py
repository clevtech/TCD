
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


@app.route('/')
def os():
    return render_template('DIVid.html')


# @app.route('/', methods = ['GET', 'POST'])
# def er():
#     global blocks
#     blocks = request.form['block']
#     print(blocks)
#     return render_template('DIVid.html')
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,debug=True)

