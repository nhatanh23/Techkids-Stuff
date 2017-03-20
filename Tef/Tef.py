from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("commingsoon.html")

@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template("w3cssdemo.html")

@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html")

if __name__ == '__main__':
    app.run()
