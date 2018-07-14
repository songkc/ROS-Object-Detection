#!/usr/bin/env python3

import sys
import cv2
import rospy
import base64
import random
import numpy as np

sys.path.append(r'./database')

from database import *
from rosproject.srv import Img
from obj_detect import object_detection


def object_detect_server():
    rospy.init_node('object_detect_server', anonymous = True)
    rospy.Service('object_detect', Img, detect)
    rospy.spin()

def detect(request):
    image_b64 = request.input

    # generate file name for image
    file = generateImageName()
    file += '.jpeg'
    print(file)

    # origin, taged and result path
    origin_image_path = 'database/origins/' + file
    taged_image_path = 'database/tagged/' + file
    result_image_path = 'database/results/' + file
    print(len(result_image_path))

    # origin image transfrom format from base64 to jpeg
    imgdata = base64.b64decode(image_b64)
    img_np = np.fromstring(imgdata, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    # save jpeg image
    cv2.imwrite(origin_image_path, img)
    cv2.imwrite(taged_image_path, img)
    print('Cloud server has successfully received image')

    # object detection
    image_b64 = object_detection(origin_image_path)
    print('Cloud server has completed object detection')
    # result image transform format from base64 to jpeg
    imgdata = base64.b64decode(image_b64)
    img_np = np.fromstring(imgdata, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    cv2.imwrite(result_image_path, img)    

    # insert database table origins, taged and results
    # connect to the database
    mydb = database()
    mydb.createTable()
    mydb.insert("origins", "'" + origin_image_path + "'")
    mydb.insert("tagged", "'" + taged_image_path + "', FALSE")
    mydb.insert("results", "'" + result_image_path + "'")
    print('Cloud server has inserted records into database!')

    return image_b64

def generateImageName():
    """
    generate a random string of length 32 for image name
    """
    name = ''
    nameLength = 32
    chars = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    for i in range(nameLength):
        name += chars[random.randint(0, length)]
    return name
    
if __name__ == '__main__':
    object_detect_server()
