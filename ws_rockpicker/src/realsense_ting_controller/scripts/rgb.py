#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2 as cv
import numpy as np
from cv_bridge import CvBridge


bridge = CvBridge()
cv_image = np.zeros((480, 640, 3), dtype='uint8')
def Cynts(data):
    #img = data.stamp
    #help(data)
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    #print(data.data.shape)
    cv_image = cv.cvtColor(cv_image, cv.COLOR_RGB2BGR)
    
        























if __name__ == '__main__':
    rospy.init_node("RGB_Capture")
    rospy.loginfo("node has been started.")

    rospy.Subscriber("/camera/color/image_raw", Image, Cynts, queue_size=1)

    while not rospy.is_shutdown():

        cv.imshow("cunts", cv_image)
        print("hej")
    
    cv.waitKey()
    cv.destroyAllWindows()


    #pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rospy.spin()



