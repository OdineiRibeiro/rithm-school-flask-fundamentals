from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/welcome')
def welcome():
    return 'Welcome to our app!'

@app.route('/welcome/home')
def welcome_home():
    return 'Welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'Welcome back!'

@app.route('/sum')
def sum():
    return '5 + 5 = %d' % (5 + 5)
