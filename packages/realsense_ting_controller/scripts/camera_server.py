#!/usr/bin/env python3

#The camera_server is a service server, when called it will take the latest image puplished to te image topic by the camera, and save it on the computer

#import modules and message dependencies
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


import datetime

#using datetime to create a stamp for the pictures, so that next time the server is started, it wont overwrite the images taken previously
date_time = datetime.datetime.now()
stamp = str(date_time.year)+'_'+str(date_time.month)+'_'+str(date_time.day)+'_'+str(date_time.hour)+'_'+str(date_time.minute)

#Declaring global values, that is used in several functions, this could be avoided by making the functions methods of a class
last_number = ''
number = 0
number_depth = 0

image_sub = ''
depth_sub = ''




def image_converter(data): #function for handling requests 

    cmd = data.request #seperate message to only contain the request

    if cmd == "Capture": #if the request is "Capture" capture an image

        #initiliaze to global variables in the function scope, so they can be saved and used in other functions
        global image_sub
        global depth_sub

        image_sub = rospy.Subscriber("/camera/color/image_raw",Image,callback, queue_size=1) #Subscribe to the color image topic, and send the image to callback function
        depth_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,callback1, queue_size=1000) #Subscribe to the depth image topic, and send the image to the callback1 function
        
        #Let user know the images have been captured.
        print("Image captured")
        return ImageCaptureResponse('Image captured')
    else:
        #if the request is not "Capture" the command is invalid
        print("Invalid command")
        return ImageCaptureResponse("Invalid command")

def callback(data): #Function that handles the Image messages from the color image topic.

    #initalize variables in function scope
    global stamp
    global number
    global image_sub

    bridge = CvBridge() #The CvBridge can convert and image from the Image msg to openCV format

    try:
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8') #desired_encoding='bgr8' 8 bit color image #try to convert the Image msg to an image
    except CvBridgeError as e:
        print(e)
    #rospy.loginfo(message)

    
    number +=1 #iterate the number variable, used to name images uniquely
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image.jpg' #An image is save just as Image.jpg, because it will be overwritten each time a new image is taken, this way the image processor server only uses the newest image.
    cv2.imwrite(filename, cv_image)
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_'+str(stamp)+'_'+str(number)+'.jpg' #For the sake of saving all the images taken, each image taken is also saved with a unique name, in a different folder.
    cv2.imwrite(filename, cv_image)
    image_sub.unregister() #Unsubscribe from the image topic, this is neccessary because once it has subscirbed to the topic, there is always new pictures incoming, and thus this will save images until the node is stopped, and the purpose is to only save 1 image, the newest one.
    #cv2.imshow("wow", cv_image)
    #cv2.waitKey(0)
    #rospy.loginfo("hej")

def callback1(data): #Function that handle the Image message from the depth image topic

    #initialize global variables in function scope.
    global stamp
    global number_depth
    global depth_sub

    bridge = CvBridge()

    #print(data.data)

    try:
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough') #This time it is saved as a 16 bit grayscale image
    except CvBridgeError as e:
        print(e)
        #rospy.loginfo(message)

    
    number_depth +=1
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_depth_'+str(stamp)+'_'+str(number_depth)+ '.png'
    cv2.imwrite(filename, cv_image)
    depth_sub.unregister()
    #print(cv_image.shape)
    #print(cv_image.dtype)
    #cv2.imshow("wow", cv_image)
    #cv2.waitKey(0)
    #rospy.loginfo("hej")




def main(args):

    rospy.init_node('image_converter', anonymous=True) #initialize the note
    s = rospy.Service('capture_command', ImageCapture, image_converter) #Start the service which listens to ImageCapture, and image_converte is the function to handle the service request
    print("Ready to recieve capture command") #Once the node it initialized let the user knoe

    try:                            #try block, to catch a keyboard interrupt, so that potential windoes openen in opencv are closed
        rospy.spin()                #Tells pytho not to stop the script
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
 
if __name__ == '__main__': #this checks is the file is run as a script, as it should. And would return false if it was imported as a module
    main(sys.argv) #run the main function