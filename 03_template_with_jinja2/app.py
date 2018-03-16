from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ['Elie', 'Tim', 'Matt']
    random_name = 'Tom'
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return 'WELCOME TO THE SECOND PAGE'

@app.route('/title')
def title():
    return render_template('title.html')

@app.route('/show-form')
def show_form():
    return render_template('first-form.html')

@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return f"You put {first} {last}"

@app.route('/person/<name>/<int:age>')
def person(name, age):
    return render_template('person.html', name=name, age=age)

@app.route('/calculate')
def calculate():
    return render_template('calculate.html')

@app.route('/math')
def fname():
    import pdb; pdb.set_trace()

    operation = request.args.get('operation')
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    return render_template("result.html")
