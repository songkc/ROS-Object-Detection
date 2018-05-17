#!/usr/bin/env python3

from flask import Flask
import time
from flask import render_template
from flask import request
import base64
from PIL import Image
from io import StringIO, BytesIO
# import robo_talker
import cv2
import numpy as np
# from sensor_msgs.msg import Image

app = Flask(__name__)

@app.route('/')
def webcam():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    print('getting data from web.')
    if request.method == 'POST':
        image_b64 = request.form['img']
        # robo_talker.talker(image_b64)
        imgdata = base64.b64decode(image_b64)
        with open('static/images/img.jpg', 'wb') as f:
            f.write(imgdata)
        # imgdata = cv2.imread('org_img.jpg')
    return 'receive'
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, ssl_context='adhoc')
