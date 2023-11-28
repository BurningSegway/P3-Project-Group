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



def processing(data):
    (rows, colums, width) = data.shape
    cv2.circle(data, (50,50), 10, 255)





class image_converter:

    def __init__(self, name, number):
        self.image_pub = rospy.Publisher("image_topic_2",Image)
        self.bridge = CvBridge()
        #self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.callback, queue_size=1)
        self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,self.callback)
        self.name = name
        self.number = number

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data) #desired_encoding='bgr8'
        except CvBridgeError as e:
            print(e)


        print(self.name + self.number)
        #cv2.imshow("Image window", cv_image)
        #cv2.waitKey(3)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image))
        except CvBridgeError as e:
            print(e)



class listener:

    def __init__(self):
        self.command = rospy.Subscriber("/image_capture_topic", String, queue_size=10)

    def callback(self):
        if self.command == "capture":
            print("capture")
            return 1










def main(args, k):
    rospy.init_node('image_converter', anonymous=True)
    k += 1
    ls = listener()
    if ls.callback() == 1:
        ic = image_converter("billede", str(k))
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    k = 0
    main(sys.argv, k)