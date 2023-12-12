#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import numpy as np
from math import pi
from wsg_gripper.srv import *
from realsense_ting_controller.srv import *

def gripper_command_client(c):

    rospy.wait_for_service('gripper_commands')

    try:
        gripper_commands = rospy.ServiceProxy('gripper_commands', GripperCommand)
        resp = gripper_commands(c)
        return resp.response

    except rospy.ServiceException:
        print("Service call failed :(")

def image_processing_command_client(c):

    rospy.wait_for_service('process_image')

    try:
        process_commands = rospy.ServiceProxy('process_image', ImgProc)
        resp = process_commands(c)
        return resp.response

    except rospy.ServiceException:
        print("Service call failed :(")

def response_to_coords(a, z):
    px = 0.86/1920
    py = 0.47/1080   

    img_x = a[0]
    img_y = a[1]

    theta = a[4]

    #if theta+(pi/4) > 180:
        #theta -= 180

    scene_x = img_x*px
    scene_y = img_y*py

    print(scene_x)
    print(scene_y)
    print(theta)

    point_mtx = np.array(([1, 0, 0, -(scene_x)], [0, 1, 0, -(scene_y)], [0, 0, 1, 0], [0, 0, 0, 1]), dtype=np.double)
    print(point_mtx)

    scene_T_base_mtx = np.array(([1, 0.0060, 0.0080, 0.4477], [0.0060, -1, 0.0060, 0.8174], [0.0080, -0.0060, -1, 0.0525], [0, 0, 0, 1]), dtype=np.double)
    print(scene_T_base_mtx)

    world_mtx = np.matmul(point_mtx, scene_T_base_mtx)
    print(world_mtx)
    print(world_mtx[0,3])
    print(world_mtx[1,3])

    print(-(theta*pi/180)-(pi/4))

    return [-(world_mtx[0,3]), world_mtx[1,3], z, -pi, 0, -(theta*pi/180)-(pi/4)]


def test_moves():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("move_group_python_interface_tutorial", anonymous=True) 
    
    #scene = moveit_commander.PlanningSceneInterface()

    #robot = moveit_commander.RobotCommander()

    #display_trajectory_publisher = rospy.Publisher(
    #"/move_group/display_planned_path",
    #moveit_msgs.msg.DisplayTrajectory,
    #queue_size=20,
    #)    

    group_name = "manipulator"
    ur5 = moveit_commander.MoveGroupCommander(group_name)

    print(ur5.get_current_pose())
    print(ur5.get_current_rpy())

    input("Tryk enter: ")
    counter = 1

    ur5.set_pose_target([0, 0.5, 0.7, -pi, 0, -(pi/4)])

    plan = ur5.plan()

    #input("Tryk enter: ")

    ur5.execute(plan[1])

    while True:

        print(counter)
        counter += 1

        #input("Tryk enter: ")

        x = 0

        y = 0.7

        z = 0.3

        ur5.set_pose_target([x, y, z, -pi, 0, -(pi/4)])

        plan = ur5.plan()

        #input("Tryk enter: ")

        ur5.execute(plan[1])

        #input("Tryk enter: ")

        waypoints = []

        wpose = ur5.get_current_pose().pose
        wpose.position.z = 0.235   # First move up (z)
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = ur5.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        #input("Tryk enter: ")

        ur5.execute(plan)

        print(gripper_command_client("grip"))

        #input("Tryk enter: ")

        waypoints = []

        wpose = ur5.get_current_pose().pose
        wpose.position.z = 0.45   # First move up (z)
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.z = 0.235   # First move up (z)
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = ur5.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        #input("Tryk enter: ")

        ur5.execute(plan)

        print(gripper_command_client("home"))

        

if __name__ == '__main__':
    try:
        test_moves()
    except rospy.ROSInterruptException:
        pass