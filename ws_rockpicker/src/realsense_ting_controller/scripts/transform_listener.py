#!/usr/bin/env python

import rospy
from tf2_msgs.msg import TFMessage

import numpy as np

from time import sleep

def callback(data):

    test = data.transforms
    print(test[0])

    

def listener():

    rospy.init_node('transform_listener', anonymous=True)

    rospy.Subscriber('tf_static', TFMessage, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()