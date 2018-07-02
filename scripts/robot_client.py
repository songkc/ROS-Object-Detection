#!/usr/bin/env python3

import os
import cv2
import rospy
import base64
import numpy as np
from PIL import Image
from rosproject.srv import Img
from std_srvs.srv import *

def object_detect_client(image_b64):
    rospy.wait_for_service('object_detect')
    try:
        print('Robot client has successfully received image')
        robot_image_path = 'static/images/robot_image.jpg'
        
        # transfrom foramt
        imgdata = base64.b64decode(image_b64)
        img_np = np.fromstring(imgdata, np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        cv2.imwrite(robot_image_path, img)

        # compress image
        fsize = os.path.getsize(robot_image_path) / (1024*1024)
        if fsize > 1.50:
            scale = 1.5
            img = Image.open(robot_image_path)
            w, h = img.size
            img.thumbnail((int(w/scale), int(h/scale)))
            img.save(robot_image_path)

        with open(robot_image_path, 'rb') as img:
            image_b64 = base64.encodestring(img.read()).decode('gbk')

        os.remove(robot_image_path)

        detect = rospy.ServiceProxy('object_detect', Img)
        response = detect(image_b64)
        return response.output
    except rospy.ServiceException as e:
        print('Service call failed!')
