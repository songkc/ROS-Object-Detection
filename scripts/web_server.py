#!/usr/bin/env python3

import cv2
import time
import base64
import numpy as np
import robot_client
from PIL import Image
from threading import Thread
from io import StringIO, BytesIO

from flask_mail import Mail, Message
from flask import Flask, request, url_for
from flask import render_template, redirect, flash

from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['MAIL_DEBUG'] = True                         # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False                # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = 'smtp.qq.com'               # 邮箱服务器
app.config['MAIL_PORT'] = 465                           # 端口
app.config['MAIL_USE_SSL'] = True                       # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False                      # 不需要使用TLS
app.config['MAIL_USERNAME'] = '847703473@qq.com'        # 填邮箱
app.config['MAIL_PASSWORD'] = 'qilecroptfstbeai'        # 填授权码
app.config['MAIL_DEFAULT_SENDER'] = '847703473@qq.com'  # 填邮箱，默认发送者
mail = Mail(app) 

# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    global count
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

        # send email
        msg = Message(subject='Raccoon!!!',
                    recipients=['weijia_sysu@163.com'])
            # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
        msg.body = 'The raccoon invaded the house!!!'
        msg.html = '<b>The raccoon invaded the house!!!<b>'
        thread = Thread(target=send_async_email, args=[app, msg])
        thread.start()

        return redirect('result')
    elif request.method == 'GET':
        return redirect('index')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(host='0.0.0.0', port=7777, debug=True)
