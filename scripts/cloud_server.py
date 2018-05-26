#!/usr/bin/env python3

import cv2
import rospy
import base64
import numpy as np
from rosproject.srv import Img
from obj_detect import object_detection

def detect(request):
    image_b64 = request.input
    cloud_image_path = 'input/cloud_image.jpeg'

    # transfrom format
    imgdata = base64.b64decode(image_b64)
    img_np = np.fromstring(imgdata, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    cv2.imwrite(cloud_image_path, img)
    print('Cloud server has successfully received image')

    image_b64 = object_detection(cloud_image_path)
    return image_b64

def object_detect_server():
    rospy.init_node('object_detect_server', anonymous = True)
    rospy.Service('object_detect', Img, detect)
    rospy.spin()

if __name__ == '__main__':
    object_detect_server()
