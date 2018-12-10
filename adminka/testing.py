from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect

app = Flask(__name__)

@app.route("/")
def route():
    render_template('index.html', name = name)



@app.route("/")
def routtte():
    re
