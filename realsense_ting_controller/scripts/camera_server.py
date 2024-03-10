#!/usr/bin/env python3

"""
This ROS node serves as a camera server e.g. for RealSense cameras, offering a 
service to capture and save both color and depth images when requested.

When receiving a 'Capture' request through a ROS service call, it subscribes 
to the RealSense camera topics for color (/camera/color/image_raw) and 
depth images (/camera/depth/image_rect_raw). It captures the next incoming 
image from each stream, saves them to the disk with unique filenames that 
include a timestamp, and then unsubscribes from the image topics. This 
ensures that each captured image set (color and depth) is synchronized and 
saved without overwriting previous captures.

The images are stored in a directory within the 'scripts' folder of the 
'realsense_ting_controller' ROS package.

Usage:
Start the camera server node:
    $ rosrun realsense_ting_controller camera_server.py

The service can be called from the command line using the 'rosservice' command:
    $ rosservice call /capture_command "request: 'Capture'"
"""


# Standard Python libraries
import os
import sys
import datetime

# ROS libraries
import rospy
import rospkg
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String

# Custom service message
from realsense_ting_controller.srv import ImageCapture, ImageCaptureResponse

# OpenCV for image processing
import cv2

# NumPy for array manipulation
import numpy as np


class CameraServer:
    def __init__(self):
        """
        Initialize the CameraServer class and set up the ROS node, service, and
        image and depth subscribers. Also initialize the paths for image storage.
        """
        # Initialize ROS node
        rospy.init_node('image_converter', anonymous=True)

        # Initialize class attributes
        self.bridge = CvBridge()
        self.image_subscriber = None
        self.depth_subscriber = None
        self.number = 0
        self.number_depth = 0
        self.initialize_paths()

        # Initialize ROS service
        self.service = rospy.Service('capture_command', ImageCapture, self.image_converter)
        rospy.loginfo("========================================")
        rospy.loginfo("=== Camera server initialized and    ===")
        rospy.loginfo("=== ready to receive capture command ===")
        rospy.loginfo("========================================")

    def initialize_paths(self):
        """
        Initializes the paths for image directory and final test directory.
        """
        # Setup dynamic path management
        ros_package_path = rospkg.RosPack().get_path('realsense_ting_controller')
        self.image_dir = os.path.join(ros_package_path, 'scripts')
        self.final_test_dir = os.path.join(self.image_dir, 'final_test')
        if not os.path.exists(self.final_test_dir):
            os.makedirs(self.final_test_dir, exist_ok=True)

    def image_converter(self, req):
        """
        When receiving a service request with a 'Capture' command, this function 
        subscribes to the color and depth image topics of the RealSense camera,
        capturing and saving the next image from each stream. Each image is saved 
        with a unique timestamp in its filename to ensure no overwriting happens.
        """
        rospy.loginfo("Attempting to capture images now.")
        if req.request == "Capture":
            # Capture the timestamp when the capture command is received
            self.capture_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.setup_subscribers()
            rospy.loginfo("Capture command received. Subscribers set up for image and depth capture.")
            return ImageCaptureResponse('Image captured')
        else:
            rospy.logwarn("You sent an invalid request: %s", req.request)
            return ImageCaptureResponse("Invalid request")

    def setup_subscribers(self):
        """
        Set up image and depth subscribers if they are not already initialized.
        """
        if not self.image_subscriber:
            rospy.logdebug("Setting up image subscriber.")
            self.image_subscriber = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback, queue_size=1)
        if not self.depth_subscriber:
            rospy.logdebug("Setting up depth subscriber.")
            self.depth_subscriber = rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.depth_callback, queue_size=1)

    def image_callback(self, data):
        """
        Callback function for processing color images.
        """
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            # Process and save the color image as needed
            rospy.logdebug("Color image received and processed.")

            # Use the stored timestamp for filename
            filename = os.path.join(self.final_test_dir, f"{self.capture_timestamp}_rgb.png")
            # Save the image
            cv2.imwrite(filename, cv_image)
            rospy.loginfo(f"Color image saved to {filename}.")

            # Unregister the subscriber to stop receiving new images
            self.image_subscriber.unregister()
            rospy.logdebug("Image subscriber unregistered.")
            # Reset the subscriber to None
            self.image_subscriber = None
        except CvBridgeError as e:
            rospy.logerr(e)

    def depth_callback(self, data):
        """
        Callback function for processing depth image data.
        """
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
            # Process and save the depth image as needed
            rospy.logdebug("Depth image received and processed.")

            # Use the stored timestamp for filename
            filename = os.path.join(self.final_test_dir, f"{self.capture_timestamp}_depth.png")
            # Save the image
            cv2.imwrite(filename, cv_image)
            rospy.loginfo(f"Depth image saved to {filename}.")

            # Unregister the subscriber to stop receiving new depth images
            self.depth_subscriber.unregister()
            rospy.logdebug("Depth subscriber unregistered.")
            # Reset the subscriber to None
            self.depth_subscriber = None
        except CvBridgeError as e:
            rospy.logerr(e)


if __name__ == '__main__':
    try:
        camera_server = CameraServer()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Camera server node terminated.")
