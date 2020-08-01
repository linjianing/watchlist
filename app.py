from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>欢迎来到我的Watchlist~</h1><img src="http://helloflask.com/totoro.gif">'

