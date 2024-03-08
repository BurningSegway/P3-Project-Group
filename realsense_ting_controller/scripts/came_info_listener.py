#!/usr/bin/env python3
#Script that listens to the camera info topic, used for debugging.

import rospy
from sensor_msgs.msg import CameraInfo

import numpy as np

from time import sleep

def callback(data): #callback function to handle the message
    print(data) #print the message

    

def listener():

    rospy.init_node('transform_listener', anonymous=True) #initialize node

    rospy.Subscriber('/camera/color/camera_info', CameraInfo, callback) #Subscirbe to the camera info topic, once a message is puplished, sent it to the callback function.

    rospy.spin() #tells python not to shut down the script.

if __name__ == '__main__': #this checks is the file is run as a script, as it should. And would return false if it was imported as a module
    listener()  #Run the main function