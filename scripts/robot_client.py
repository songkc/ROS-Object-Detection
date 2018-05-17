#!/usr/bin/env python3

import rospy
from rosproject.srv import Img
from std_srvs.srv import *

def object_detect_client(image_b64):
    rospy.wait_for_service('object_detect')
    try:
        detect = rospy.ServiceProxy('object_detect', Img)
        response = detect(image_b64)
        print('Client has successfully received image\n')
        return response.output
    except rospy.ServiceException as e:
        print('Service call failed: %s') % str(e)

if __name__ == "__main__":
    object_detect_client()
