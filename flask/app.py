from machine_learning.model import return_hello

from flask import Flask
from flask import request, Response
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return json.dumps(data)
    
    elif request.method == 'GET':
        return_hello()
        return 'Hello, World!'

app.run(host="0.0.0.0", port=5000)