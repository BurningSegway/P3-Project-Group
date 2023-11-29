#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs
from std_msgs.msg import String
from math import pi

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

    ur5.set_pose_target([0, 0.5, 0.7, -pi, 0, -(pi/4)])

    plan = ur5.plan()

    input("Tryk enter: ")

    ur5.execute(plan[1])

    #input("Tryk enter: ")

    #ur5.set_pose_target([0.1, 0.38, 0.54, -(pi-(pi/4)), (pi/4), -(pi/4)])

    #plan = ur5.plan()

    #input("Tryk enter: ")

    #ur5.execute(plan[1])

    






if __name__ == '__main__':
    try:
        test_moves()
    except rospy.ROSInterruptException:
        pass