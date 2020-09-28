
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


# Get example method
@app.route('/get', methods=['GET'])
def user():
    if request.method == 'GET':
        return f"Hello get !"


# Post example method
@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        return f"Hello post !"


# Multiply by 2 - with Get, example method
@app.route('/multiply/<int:number>')
def multiply(number):
    return f"Result: {number * 2}"


if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)
