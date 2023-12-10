#!/usr/bin/env python3
from __future__ import print_function

import roslib
roslib.load_manifest('realsense_ting_controller')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from realsense_ting_controller.srv import ImageCapture, ImageCaptureResponse
import numpy as np


last_number = ''
number = 0
number_depth = 0

image_sub = ''
depth_sub = ''




def image_converter(data):

    cmd = data.request

    if cmd == "Capture":

        global image_sub
        #global depth_sub


        #self.message_sub = rospy.Subscriber("/image_capture_topic", String, self.callback1, queue_size=1000)
        #self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,self.callback, queue_size=1000)
        image_sub = rospy.Subscriber("/camera/color/image_raw",Image,callback, queue_size=1)
        #depth_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,callback1, queue_size=1000)
        
        print("What")
        return ImageCaptureResponse('Image captured')
    else:
        print("Invalid command")
        return ImageCaptureResponse("Invalid command")

def callback(data):

    global number
    global image_sub

    bridge = CvBridge()

    try:
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8') #desired_encoding='bgr8'
    except CvBridgeError as e:
        print(e)
    #rospy.loginfo(message)

    
    number +=1
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image.jpg'
    cv2.imwrite(filename, cv_image)
    image_sub.unregister()
    #cv2.imshow("wow", cv_image)
    #cv2.waitKey(0)
    #rospy.loginfo("hej")

#def callback1(data):
 #   global number_depth
  #  global depth_sub

   # bridge = CvBridge()

    #print(data.data)

    #try:
     #   cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough') #desired_encoding='bgr8'
    #except CvBridgeError as e:
    #    print(e)
    #rospy.loginfo(message)

    
    #number_depth +=1
    #filename = '/home/pe/Desktop/P3-Project-Group/Billeder/RGB_UP_1/Image_depth_' + str(number_depth) +'.png'
    #cv2.imwrite(filename, cv_image)
    #depth_sub.unregister()
    #print(cv_image.shape)
    #print(cv_image.dtype)
    #cv2.imshow("wow", cv_image)
    #cv2.waitKey(0)
    #rospy.loginfo("hej")




def main(args):

    rospy.init_node('image_converter', anonymous=True)
    s = rospy.Service('capture_command', ImageCapture, image_converter)
    print("Ready to recieve capture command")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    main(sys.argv)