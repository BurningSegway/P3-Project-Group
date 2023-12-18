#!/usr/bin/env python
#This script will publish the scene transform, so it can be visualized in RViz.

import rospy
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg


class FixedTFBroadcaster:

    def __init__(self):
        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1) #Declare that the node is puplishng to the /tf topic

        while not rospy.is_shutdown():
            # Run this loop at about 10Hz
            rospy.sleep(0.1)

            t = geometry_msgs.msg.TransformStamped() #Make a transform message, where the different parts of the message can be assigned values
            t.header.frame_id = "camera_color_optical_frame" #Name of the parent fram
            t.header.stamp = rospy.Time.now() #Stamped with the time
            t.child_frame_id = "scene" #The name of the child frame, this will create a frame called scene where the camera optical frame is the parent
            #XYZ translation of the frame, these values are will set the origin of the frame at the top left corner of an image.
            t.transform.translation.x = -0.4192 
            t.transform.translation.y = -0.2342
            t.transform.translation.z = 0.61
            #The scene frame has no rotation in relation to the parent frame
            t.transform.rotation.x = 0
            t.transform.rotation.y = 0
            t.transform.rotation.z = 0
            t.transform.rotation.w = 1

            tfm = tf2_msgs.msg.TFMessage([t]) #Convert the geometry msg to a tf2 msg
            self.pub_tf.publish(tfm) #puplish the msg

if __name__ == '__main__': #this checks is the file is run as a script, as it should. And would return false if it was imported as a module
    rospy.init_node('fixed_tf2_broadcaster') #initialize node
    tfb = FixedTFBroadcaster() #Instantiate an object of the class FixedTFBBroadcaster.

    rospy.spin() #tells python not to shutdown the script until the node is told to shotdown