#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CameraInfo

import numpy as np

from time import sleep

def callback(data):
    print(data)

    

def listener():

    rospy.init_node('transform_listener', anonymous=True)

    rospy.Subscriber('/camera/color/camera_info', CameraInfo, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()