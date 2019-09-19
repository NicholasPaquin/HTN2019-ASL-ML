from machine_learning.clean_img import clean_image
from tensorflow.keras.models import load_model

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
        print("BYTE ARRAY", byteArray)

        numpy_array = clean_image(byteArray)

        model = load_model('machine_learning/model/2019-09-15 11_55_30.484543.h5')
        class_pred = model.predict(numpy_array)

        hand_gesture = classes_list[class_pred]

        return json.dumps(hand_gesture)
    
    elif request.method == 'GET':
        return 'Hello, World!'

app.run(host="0.0.0.0", port=5000)