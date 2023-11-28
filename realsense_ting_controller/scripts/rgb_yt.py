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




class image_converter:

    def __init__(self):
        self.message = String()
        self.image_pub = rospy.Publisher("image_topic_2",Image)
        self.bridge = CvBridge()
        self.message_sub = rospy.Subscriber("/image_capture_topic", String, self.callback1, queue_size=1000)
        #self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,self.callback, queue_size=1000)
        self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.callback, queue_size=1000)




    def callback1(self, data):
        try:
            self.message = data
        except BufferError:
            print("WTF")

        return





    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data) #desired_encoding='bgr8'
        except CvBridgeError as e:
            print(e)
        rospy.loginfo(self.message)
        while self.message == String("capture"):
            cv2.imshow("Image window", cv_image)
            cv2.waitKey(3)
            #rospy.loginfo("hej")


        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image))
        except CvBridgeError as e:
            print(e)







def main(args):
    rospy.init_node('image_converter', anonymous=True)
    ic = image_converter()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    main(sys.argv)