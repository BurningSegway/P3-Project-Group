#!/usr/bin/env python3
from __future__ import print_function

import roslib
roslib.load_manifest('realsense_ting_controller')
import sys
import rospy
from std_msgs.msg import String




if __name__ == '__main__':
    rospy.init_node("trigger")
    rospy.loginfo("node has been started.")



    pub = rospy.Publisher("/image_capture_topic", String, queue_size=None)


    rate1 = rospy.Rate(2)

    msg = String()
    now = rospy.Time.now()
    while not rospy.is_shutdown():
        msg.data = "capture"
        pub.publish(msg)
        rate1.sleep()
        msg.data = "wait"
        pub.publish(msg)
        rate1.sleep()




