from machine_learning.model import return_hello

from flask import Flask
from flask import request, Response
import json
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        encodedMessage = request.get_json()
        print(encodedMessage)

        byteArray = encodedMessage['byteArray']

        print(byteArray)

        decodedMessage = base64.b64decode(byteArray)

        # send decoded model, return data

        return decodedMessage
    
    elif request.method == 'GET':
        return_hello()
        return 'Hello, World!'

app.run(host="0.0.0.0", port=5000)