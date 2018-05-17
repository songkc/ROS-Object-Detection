#!/usr/bin/env python3

import cv2
import time
import base64
import robot_client
from PIL import Image
from flask import Flask
from flask import request
from flask import render_template
from io import StringIO, BytesIO

app = Flask(__name__)

@app.route('/')
def webcam():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    print('getting data from web.')
    if request.method == 'POST':
        image_b64 = request.form['img']
        image_b64 = robot_client.object_detect_client(image_b64)
        imgdata = base64.b64decode(image_b64)
        web_image_path = 'output/image.jpg'
        with open(web_image_path, 'wb') as f:
            f.write(imgdata)
        img = cv2.imread(web_image_path)
    return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, ssl_context='adhoc')
