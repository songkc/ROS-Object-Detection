#!/usr/bin/env python3

import cv2
import time
import base64
import numpy as np
import robot_client
from PIL import Image
from io import StringIO, BytesIO
from flask import Flask, request, url_for
from flask import render_template, redirect, flash

from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    print('Getting data from web.')
    if request.method == 'POST':
        # print(request.form)
        image_b64 = request.form['img']

        web_image_path = 'static/images/web_image.jpg'
        image_b64 = robot_client.object_detect_client(image_b64)
        imgdata = base64.b64decode(image_b64)
        img_np = np.fromstring(imgdata, np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        cv2.imwrite(web_image_path, img)
        return redirect('result')
    elif request.method == 'GET':
        return redirect('index')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(host='0.0.0.0', port=7777, debug=True)
