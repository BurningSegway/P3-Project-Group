#!/usr/bin/env python

#The get_poses script, is the main script of the implementation. This script is started when the robot should do its thing, this script is responsible for making the robot move, calling the appropriete services, to operate the gripper, and process images.

import sys
import copy
import rospy
import moveit_commander
import numpy as np
from math import pi
from wsg_gripper.srv import *
from realsense_ting_controller.srv import *

run_count = 1 #Variable to keep track, of how many times the code has itereated, equals to how many times the manipultor has grabbed a rock

def gripper_command_client(c):

    '''
    This function will do the service call to the gripper_commands serivce.

    The input c into the function, is the command the gripper should perform.

    Once the the function has sent its request to the service, it waits for a response and then returns this.
    '''

    rospy.wait_for_service('gripper_commands') #Wait for the gripper_commands service to become available

    try:
        gripper_commands = rospy.ServiceProxy('gripper_commands', GripperCommand) #Declares what type of service message and to what service the request is sent to
        resp = gripper_commands(c)  #The input to the function is sent as a command, and the response from the service is saved
        return resp.response #The response part of the service message is returned

    except rospy.ServiceException:
        print("Service call failed :(")

def image_processing_command_client(c):
    '''
    This function will do the service call to the process_image serivce.

    The input c into the function, is the command for the service to process an image.

    Once the the function has sent its request to the service, it waits for a response and then returns this.
    '''
 
    rospy.wait_for_service('process_image') #Wait for the process_image service to become available

    try:
        process_commands = rospy.ServiceProxy('process_image', ImgProc) #Declares what type of service message and to what service the request is sent to
        resp = process_commands(c) #The input to the function is sent as a command, and the response from the service is saved
        return resp.response #The response part of the service message is returned

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
    actual_long_leng = long_axis_px_leng*px #this should be calculated using the angle and the corresponding x and y pixel  ratios, but it was deemed adequite to use the x value, since they are close to each other in the x and y direction
    actual_short_leng = short_axis_px_leng*px

    #Intermediate variables for calculating the volume of an ellipsoid
    A = actual_short_leng/2
    B = actual_long_leng/2
    C = 0.03 #Constant ellipsoid heigth is set

    V = (4/3)*pi*A*B*C #Calculating the volume

    rho = 2700 #Density of granite

    weight = V*rho #Weight estimation

    #print the various findings, for the operator to see
    print(f"Length of longest axis: {actual_long_leng}")
    print(f"Length of shortest axis: {actual_short_leng}")
    print(f"Volume of rock: {V}")
    print(f"Weight of rock: {weight}")

    theta = a[4] #Saving the angle of the shortest axis.

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
    moveit_commander.roscpp_initialize(sys.argv) #Initialize the MoveIt commander API
    rospy.init_node("move_group_python_interface_tutorial", anonymous=True) #Initialize the note

    #Declaring the global variable in the function scope
    global run_count

    group_name = "manipulator"
    ur5 = moveit_commander.MoveGroupCommander(group_name) #Intanceiating a robot object, to be controlled with MoveIt commander

    #Print current pose when the program starts, this is primarely used for debugging
    print(ur5.get_current_pose())
    print(ur5.get_current_rpy())

    #Once everything has been initialized, the robot is ready to go, and the user must press enter before any movement begins
    input("Tryk enter: ")

    while True: #The program loops

        print(f"Starting run: {run_count}")

        ur5.set_pose_target([0, 0.5, 0.7, -pi, 0, -(pi/4)]) #Set a targe for the end effector to reach, this is the home position, from where a picture will be taken

        plan = ur5.plan() #Plan the joint move to the target

        #input("Tryk enter: ") #Before implementing joint limits, the user must press enter before executing the planned movement, after obersving in RViz that the planned movement is valid, and wont make the robot collide with anything, these checks have been commented out after implemnting proper joint limits

        ur5.execute(plan[1]) #Execute the planned move, this will make the manipulator move in real life

        #input("Tryk enter: ")

        ur5.set_pose_target(response_to_coords(image_processing_command_client("Process"), 0.30)) #Set a new target, this target is placed where the CV pipeline hat detected a rock, and a preset z height is also parsed to the function

        plan = ur5.plan() #Plan the movement to the rock

        #input("Tryk enter: ")

        ur5.execute(plan[1]) #Execute the plan

        #input("Tryk enter: ")

        waypoints = [] #Declare waypoints list for cartesian move

        #Get current position, and modify the z position, this will lower the end effector further down, to where it is able to grip a rock
        wpose = ur5.get_current_pose().pose
        wpose.position.z = 0.235   
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.
        (plan, fraction) = ur5.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        #input("Tryk enter: ")

        ur5.execute(plan) #Once planned execute the downward movement

        print(gripper_command_client("grip")) #Call the gripper_commands service, with a request to grip, this will make the gripper close around the rock

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
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        #input("Tryk enter: ")

        ur5.execute(plan) #Execute upwards movement

        #input("Tryk enter: ")

        ur5.set_pose_target([-0.7281, 0.009, 0.45, -pi, 0, -(pi/4)]) #Set target outside of the sandbox

        plan = ur5.plan() #Plan the joint move

        #input("Tryk enter: ")

        ur5.execute(plan[1]) #Execute movement

        print(gripper_command_client("home")) #Once end effector is outside the sandbox, another request is sent to the gripper_commands service, to home the gripper, this will open the gripper and drop the rock

        run_count += 1 #Iterate the run counter

if __name__ == '__main__': #this checks is the file is run as a script, as it should. And would return false if it was imported as a module
    try:             
        move_robot() #Run the main function.
    except rospy.ROSInterruptException:
        pass