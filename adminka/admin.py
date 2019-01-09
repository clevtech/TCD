import flask
from breadcrump import breadcrumb

app = flask.Flask(__name__)

@app.route('/')
@breadcrumb('The index page')
def index():
    return flask.render_template('zip.html')

@app.route('/a')
@breadcrumb('')
def pagea():
    return flask.render_template('zip.html')

@app.route('/b')
@breadcrumb('rob')
def pageb():
    name = "rob"
    return flask.render_template('zip.html', name = name)

@app.route('/c')
@breadcrumb('Chimp')
def pagec(id = 1):
    return flask.render_template('zip.html', name = id)

@app.route('/d')
@breadcrumb('Donkey')
def paged():
    return flask.render_template('zip.html')





if __name__ == '__main__':
    app.secret_key = '83cf5ca3-b1ee-41bb-b7a8-7a56c906b05f'
    app.debug = True
    app.run(host='0.0.0.0', port=8888, debug=True)
