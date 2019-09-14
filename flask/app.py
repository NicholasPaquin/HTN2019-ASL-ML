from machine_learning.model import return_hello

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return_hello()
    return 'Hello, World!'
