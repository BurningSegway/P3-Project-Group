3rd semester project: Automatic sensing of the enviornment

Here is what you need to do in order to run the system on an UR5 robotic manipulator equipped with an Intel RealSense D435 camera. It is assumed that ROS Noetic is installed.

-----
On your PC setup your wired connection as a static IP.

-----
The UR5 must be able to communicate with ROS, so a UR ROS driver must be installed according to: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/tree/master

sudo apt install ros-noetic-ur-robot-driver

If this doesnt work, you might need to install it from source into your catkin src folder, please refer to the link for this guide.

Build your workspace

-----
Now the robot itself must be prepared, for this a URCap must be installed on the UR pendant. The newest version of the URCap can be found here: https://github.com/UniversalRobots/Universal_Robots_ExternalControl_URCap/releases
Then the URCap must be installed on the robot according to: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/install_urcap_cb3.md

Copy the URCap file onto a USB drive and insert it into the UR pendant. From the welcome screen on the pendant navigate to: Setup Robot -> URCaps. Here click on the plus sign, select the URCap from the USB drive and click open. Restart the robot when promted to.

After the reboot 'External Control' should be visible inside the installation section, once you have pressed program robot from the welcome screen. 

Select 'External Control' and enter the IP of the PC that will run the ROS driver. Leave the custom port as is.

Now to enable the robot to be controlled by the ROS driver, create a program, and insert the ExternalControl node into the programming tree.

-----
Each UR manipulator is calibrated form the factory given precise forward and inverse kinematics. This can be utilized by ROS, by extrating this calibration from the robot. This is highly recommended to do, as the end effectors position could be off by centimeters.
To do so:

roslaunch ur_calibration calibration_correction.launch \
  robot_ip:=<robot_ip> target_filename:="${HOME}/my_robot_calibration.yaml"

Insert the robots ip adress, and a full path to where you want the calibrations to be stored.

-----
Now you should install MoveIt, which handles the motion planning of the manipulator.

This is done according to the installation guide: https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html

Start by installing wstool

sudo apt install python3-wstool

Then install MoveIt

wstool init .
wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
wstool remove moveit_tutorials  # this is cloned in the next section
wstool update -t .

The tutaorials are removed, since in the guide they recommend cloning this into the workspace.
This is not neccassry for this project, but it is included in this packages folder.
If you do desire the tutorials can be cloned into the workspace like so.
First navigate to the src folder of your workspace then:

git clone https://github.com/ros-planning/moveit_tutorials.git -b master
git clone https://github.com/ros-planning/panda_moveit_config.git -b noetic-devel

If there are dependencies not yet installed ROS can install them by:

rosdep install -y --from-paths . --ignore-src --rosdistro noetic

Then build the workspace

-----
Now copy the following packages into your workspace src folder: realsense_ting_controller, ur5_module and wsg_gripper.

You can also copy the joint_limits_corrected.yaml this will be used to limit the maniulators joints, as to avoid solutions to the motion planning that would cause the manipulator to do a configuration change. Navigate to: universal_robot -> ur_description -> config -> ur5 in here, replace the joint_limits.yaml, with the one you copied, and rename it to joint_limits.yaml

-----
To get the Intel Realsense camera up and running, install the realsense package according to:https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy

sudo apt-get install ros-$ROS_DISTRO-realsense2-camera

That should be it, to test out the camera, launch it:

roslaunch realsense2_camera rs_camera.launch

An easy way of seeing if the camera is publishing images, is to launch RViz, and add a view form topic, and selcet color image raw topic.

-----
The last thing that should be done, is to do a eye-in-hand calibration. Since there could be a difference in the setup used in this project, and yours setup. For this purpose MovieIt has a calibration package, that provides a graphical interface for this in RViz. To install the package according to: https://ros-planning.github.io/moveit_tutorials/doc/hand_eye_calibration/hand_eye_calibration_tutorial.html

Navigate to the src folder of your workspace and clone the package:

git clone git@github.com:ros-planning/moveit_calibration.git

Then make sure all the dependencies are installed:

rosdep install -y --from-paths . --ignore-src --rosdistro melodic

Build your workspace.

Launch RViz with the UR demo:

roslaunch ur5_moveit_config demo.launch

When RViz has launched go to 'Displays' and click 'Add' and select 'HandEyeCalibration from the list and click 'OK'

When The GUI shows up, create and print out a target, and measure the squares and the seperation between them, and put it into the boxes.

Launch the camera with the following arguments: roslaunch realsense2_camera rs_camera.launch color_width:="1920" color_height:="1080" color_fps:="30"

In the calibration GUI, in the image topic dropdown, select the color raw image, and for the camerainfo topic dropdown, select the color info.

Now in the 'Context' tap, select eye-in-hand as the sensor configuration. Then as the Sensor Frame select color optical frame, and the object frame as handeye target, in this project the end effector frame is set to tool0, and the base frame as the base link.

The initial guess can be left as is.

Now in RViz add another view from a topic, this should be under handeye calibration and then target detection. This view is in black and white and will display the detected corners on the target, and show a frame, locating the targets origin.

Now you are ready to make your calibration, move the end effector around, where the target is in the frame, and the frame shows up correctly, press take sample, and continue this for several different positions, in this project 20 samples were taken.

Once all the desired samples are taken, click 'Save camera pose'. This will create a launch file, that puplishes a static transform of where the optical frame of the camera is in relation to tool0 which can be visualized in RViz.

-----
At this point you can launch the core implementation of the project, that will take a picture of the sandbox, process the image, identify the rocks present, and pick up all the rocks in the sandbox, starting with the longest rock, all autonomously.

First launch the UR ROS driver:

roslaunch ur_robot_driver ur5_bringup.launch robot_ip:=<robot_ip> \
  kinematics_config:="${HOME}/my_robot_calibration.yaml"
  
Where you enter the robots IP adress and the path to the extrated robot calibration.

Then in the program on the UR pendant created earlier with only the ExterControl node in, press run, and the terminal should say it is connected.

In a new terminal enter:

roslaunch ur5_moveit_config moveit_planning_execution.launch

When this terminal says its ready to recieve commands, open a new terminal and enter:

roslaunch ur5_moveit_config moveit_rviz.launch

Once RViz has launched, launch the camera in a new terminal:

roslaunch realsense2_camera rs_camera.launch color_width:="1920" color_height:="1080" color_fps:="30"

Once the camera is launched start the gripper command node in a new terminal:

rosrun wsg_gripper gripper_command_server2.py

Then start the camera server in a new terminal:

rosrun realsense_ting_controller camera_server.py

Then start the image proccesor server in a new terminal:

rosrun realsense_ting_controller image_processing_server.py

And finally, once all the required nodes are started, run the get poses script in a new terminal:

rosrun ur5_module get_poses.py

Now the manipulator should start picking up rocks.

-----
Further information.

You can find alot of pictures taken from when the robot has run during testing by navigating to realsense_ting_controller -> scripts -> final_test

Here are folders with the raw RGB images, depth images, ellipse images, and various steps in the computer vision pipeline, all images has a corresponding RGB, depth, ellipse etc. version, as seen on the stamp in the file name.

In some of the pictures, a ArUco marker board is visible, if you want to do your own transforms and such. The squares' sides measure 0.057 meters and the seperation 0.0058 meters.

The dpeth images are 16 bit, so this has to be kept in mind, if the images are to be opened and processed correctly. The pixel values in the depth image should represesnt the distance from the camera to the object in millimeters.



