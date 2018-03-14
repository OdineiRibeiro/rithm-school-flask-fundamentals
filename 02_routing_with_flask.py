from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/name/<person>')
def say_name(person):
    return f"The name is {person}"

@app.route('/name/<int:num>')
def favorite_num(num):
    return f"Your favorite number is {num}, wich is half of {num * 2}"

@app.route('/math/<operation>/<int:number_1>/<int:number_2>')
def math_operations(operation, number_1, number_2):
    if operation == 'addition':
        return f"{number_1} + {number_2} = {number_1 + number_2}"
    elif operation == 'subtraction':
        return f"{number_1} - {number_2} = {number_1 - number_2}"
    elif operation == 'multiplication':
        return f"{number_1} * {number_2} = {number_1 * number_2}"
    elif operation == 'division':
        return f"{number_1} / {number_2} = {number_1 / number_2}"
    else:
        return "Uh-oh... Something goes wrong O.O'"
