#!/usr/bin/env python3

import cv2
import rospy
import base64
from rosproject.srv import Img

def detect(req):
    image_b64 = req.input
    imgdata = base64.b64decode(image_b64)
    cloud_image_path = 'input/image.jpg'
    with open(cloud_image_path, 'wb') as f:
        f.write(imgdata)
    print('Server has successfully received image\n')
    # imgstr = StringIO(base64.b64decode(image_b64))
    # img = Image.open(imgstr)
    # buffered = BytesIO()
    # img.save(buffered, format='JEPG')
    # image_b64 = base64.b64encode(buffered.getvalue())
    with open(cloud_image_path, 'rb') as img:
        image_b64 = base64.encodestring(img.read()).decode('gbk')
    return image_b64

def object_detect_server():
    rospy.init_node('object_detect_server', anonymous = True)
    rospy.Service('object_detect', Img, detect)
    rospy.spin()

if __name__ == '__main__':
    object_detect_server()
