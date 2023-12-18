#!/usr/bin/env python

#This listener is not used, but was the first succesful attempt, to control the gripper through ROS

import rospy
from std_msgs.msg import String

from wsg import WSG
#import numpy as np
from time import sleep

def callback(data):

    print(data)

    msg = data.data

    if msg == 'grip':
        print("Gripping...")
        wsg.grip(40)
        sleep(5)
    if msg == 'release':
        print("Releasing...")
        wsg.release()
        sleep(5)
    if msg == 'home':
        print("Homing...")
        wsg.home()
        sleep(5)
    else:
        print("Invalid message!")

def listener():

    rospy.init_node('gripper_listener', anonymous=True)

    rospy.Subscriber('gripper_publisher', String, callback)

    rospy.spin()

if __name__ == '__main__':
    wsg = WSG()
    wsg.home()
    listener()