#!/usr/bin/env python3

#The get_poses script, is the main script of the implementation. This script is started when the robot should do its thing, this script is responsible for making the robot move, calling the appropriete services, to operate the gripper, and process images.

import sys
import copy
import rospy
import moveit_commander
import numpy as np
from math import pi
from wsg_gripper.srv import *
from realsense_ting_controller.srv import *

#Variable to keep track, of how many times the code has itereated, equals to how many times the manipultor has grabbed a rock
run_count = 1 

def gripper_command_client(c):

    '''
    This function will do the service call to the gripper_commands serivce.

    The input c into the function, is the command the gripper should perform.

    Once the the function has sent its request to the service, it waits for a response and then returns this.
    '''
    #Wait for the gripper_commands service to become available
    rospy.wait_for_service('gripper_commands') 

    try:
        #Declares what type of service message and to what service the request is sent to
        gripper_commands = rospy.ServiceProxy('gripper_commands', GripperCommand) 
        #The input to the function is sent as a command, and the response from the service is saved
        resp = gripper_commands(c)  
        #The response part of the service message is returned
        return resp.response 

    except rospy.ServiceException:
        print("Service call failed :(")

def image_processing_command_client(c):
    '''
    This function will do the service call to the process_image serivce.

    The input c into the function, is the command for the service to process an image.

    Once the the function has sent its request to the service, it waits for a response and then returns this.
    '''
    #Wait for the process_image service to become available
    rospy.wait_for_service('process_image') 

    try:
        #Declares what type of service message and to what service the request is sent to
        process_commands = rospy.ServiceProxy('process_image', ImgProc) 
        #The input to the function is sent as a command, and the response from the service is saved
        resp = process_commands(c) 
        #The response part of the service message is returned
        return resp.response 

    except rospy.ServiceException:
        print("Service call failed :(")

def response_to_coords(a, z):
    '''
    This function takes a and z as input, a is a list one the form ((x, y), (short, long), theta)
    x and y is the center of an ellipse in pixel coordinates, then it contains the length of the shortest and longest axis of the ellipse in pixel
    and theta is the angle of the shortest axis, compared to the world x axis

    This functions takes the pixel coordinates, and translates them into world coordinates, that the gripper can navigate to

    The z input is the z height of the end effector so effectively, how far down the end effector will go.
    '''
    #Finding the amount of meters pr pixel in the x and ydirection
    px = 0.86/1920 
    py = 0.47/1080   

    #Saving the pixel x and y coordinates
    img_x = a[0]
    img_y = a[1]

    #The length of the axes are are saved, and the length is calculated in meters, based on the amount of pixel pr distance ratio found earlier
    long_axis_px_leng = a[3]
    short_axis_px_leng = a[2]

    #this should be calculated using the angle and the corresponding x and y pixel  ratios, but it was deemed adequite to use the x value, since they are close to each other in the x and y direction
    actual_long_leng = long_axis_px_leng*px 
    actual_short_leng = short_axis_px_leng*px

    #Intermediate variables for calculating the volume of an ellipsoid
    A = actual_short_leng/2
    B = actual_long_leng/2
    #Constant ellipsoid heigth is set
    C = 0.03 

    #Calculating the volume
    V = (4/3)*pi*A*B*C 

    #Density of granite
    rho = 2700 

    weight = V*rho #Weight estimation

    #print the various findings, for the operator to see
    print(f"Length of longest axis: {actual_long_leng}")
    print(f"Length of shortest axis: {actual_short_leng}")
    print(f"Volume of rock: {V}")
    print(f"Weight of rock: {weight}")

    #Saving the angle of the shortest axis.
    theta = a[4] 

    #Converting pixel coordinates in the image, to the corresponding distances on the actual image in the real world
    scene_x = img_x*px
    scene_y = img_y*py

    #print(scene_x)
    #print(scene_y)
    #print(theta)

    #Creating a transformation matrix, for the point, using the just found scene coordinates
    point_mtx = np.array(([1, 0, 0, -(scene_x)], [0, 1, 0, -(scene_y)], [0, 0, 1, 0], [0, 0, 0, 1]), dtype=np.double)
    #print(point_mtx)

    #Declaring the transformation matrix, for translating a point in the image, to the world coordinate system, this is found in ROS using tf_echo
    scene_T_base_mtx = np.array(([1, 0.0060, 0.0080, 0.4477], [0.0060, -1, 0.0060, 0.8174], [0.0080, -0.0060, -1, 0.0525], [0, 0, 0, 1]), dtype=np.double)
    #print(scene_T_base_mtx)

    #Multiplying the matrices together to find the matrix that represents the point in the world frame
    world_mtx = np.matmul(point_mtx, scene_T_base_mtx)
    #print(world_mtx)
    #print(world_mtx[0,3])
    #print(world_mtx[1,3])

    #print(-(theta*pi/180)-(pi/4))

    #Returns the position and angle of the ellipse, as a pose command, that the MoveIt commander API can understand
    return [-(world_mtx[0,3]), world_mtx[1,3], z, -pi, 0, -(theta*pi/180)-(pi/4)]


def move_robot():
    '''
    The main script that controls the robots movement, and calling the appropriete services
    '''
    #Initialize the MoveIt commander API
    moveit_commander.roscpp_initialize(sys.argv) 
    #Initialize the node
    rospy.init_node("move_group_python_interface_tutorial", anonymous=True) 

    #Declaring the global variable in the function scope
    global run_count

    #Intanceiating a robot object, to be controlled with MoveIt commander
    group_name = "manipulator"
    ur5 = moveit_commander.MoveGroupCommander(group_name) 

    #Print current pose when the program starts, this is primarely used for debugging
    print(ur5.get_current_pose())
    print(ur5.get_current_rpy())

    #Once everything has been initialized, the robot is ready to go, and the user must press enter before any movement begins
    input("Tryk enter: ")

    #The program loops
    while True: 

        print(f"Starting run: {run_count}")

        #Set a targe for the end effector to reach, this is the home position, from where a picture will be taken
        ur5.set_pose_target([0, 0.5, 0.7, -pi, 0, -(pi/4)]) 

        #Plan the joint move to the target
        plan = ur5.plan() 

        #input("Tryk enter: ") #Before implementing joint limits, the user must press enter before executing the planned movement, after obersving in RViz that the planned movement is valid, and wont make the robot collide with anything, these checks have been commented out after implemnting proper joint limits

        #Execute the planned move, this will make the manipulator move in real life
        ur5.execute(plan[1]) 

        #input("Tryk enter: ")

        #Set a new target, this target is placed where the CV pipeline hat detected a rock, and a preset z height is also parsed to the function
        ur5.set_pose_target(response_to_coords(image_processing_command_client("Process"), 0.30)) 

        #Plan the movement to the rock
        plan = ur5.plan() 

        #input("Tryk enter: ")

        #Execute the plan
        ur5.execute(plan[1]) 

        #input("Tryk enter: ")

        #Declare waypoints list for cartesian move
        waypoints = [] 

        #Get current position, and modify the z position, this will lower the end effector further down, to where it is able to grip a rock
        wpose = ur5.get_current_pose().pose
        wpose.position.z = 0.235   
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.
        (plan, fraction) = ur5.compute_cartesian_path(
            # waypoints to follow  
            waypoints, 0.01, 0.0  
            # eef_step
            # jump_threshold
        )  

        #input("Tryk enter: ")

        #Once planned execute the downward movement
        ur5.execute(plan) 

        #Call the gripper_commands service, with a request to grip, this will make the gripper close around the rock
        print(gripper_command_client("grip")) 

        #input("Tryk enter: ")

        
        #Once gripped, another cartesian path upwards is planned, just like the first
        waypoints = []

        wpose = ur5.get_current_pose().pose
        wpose.position.z = 0.45
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.
        (plan, fraction) = ur5.compute_cartesian_path(
            # waypoints to follow  
            waypoints, 0.01, 0.0  
            # eef_step
            # jump_threshold
        )  

        #input("Tryk enter: ")

        #Execute upwards movement
        ur5.execute(plan) 

        #input("Tryk enter: ")

        #Set target outside of the sandbox
        ur5.set_pose_target([-0.7281, 0.009, 0.45, -pi, 0, -(pi/4)]) 

        #Plan the joint move
        plan = ur5.plan() 

        #input("Tryk enter: ")

        #Execute movement
        ur5.execute(plan[1]) 

        #Once end effector is outside the sandbox, another request is sent to the gripper_commands service, to home the gripper, this will open the gripper and drop the rock
        print(gripper_command_client("home")) 

        #Iterate the run counter
        run_count += 1 

if __name__ == '__main__': 
    try:             
        move_robot()
    except rospy.ROSInterruptException:
        pass