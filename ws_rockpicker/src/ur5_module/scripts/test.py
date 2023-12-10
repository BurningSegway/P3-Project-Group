#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs
from std_msgs.msg import String

def test_moves():
    
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

    pub = rospy.Publisher('gripper_publisher', String, queue_size=10)
    
    
    #scene = moveit_commander.PlanningSceneInterface()

    #robot = moveit_commander.RobotCommander()

    #display_trajectory_publisher = rospy.Publisher(
    #"/move_group/display_planned_path",
    #moveit_msgs.msg.DisplayTrajectory,
    #queue_size=20,
    #)

    group_name = "manipulator"
    ur5 = moveit_commander.MoveGroupCommander(group_name)

    start_pose = ur5.get_current_joint_values()
    
    end_pose = ur5.get_current_joint_values()
    end_pose[2] = -1.3

    while not rospy.is_shutdown():

        ur5.set_joint_value_target(end_pose)

        pub.publish("grip")

        plan = ur5.plan()

        #print(plan[1])

        input("Tryk enter for at eksekver")

        ur5.execute(plan[1], wait=True)

        ur5.stop()

        input("Tryk enter for at planlægge næste move")

        ur5.set_joint_value_target(start_pose)
        plan = ur5.plan()

        input("Tryk enter for at eksekver")

        ur5.execute(plan[1])
        pub.publish("home")


if __name__ == '__main__':
    try:
        test_moves()
    except rospy.ROSInterruptException:
        pass