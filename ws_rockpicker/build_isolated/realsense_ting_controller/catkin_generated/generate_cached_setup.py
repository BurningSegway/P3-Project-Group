# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/pe/ws_rockpicker/devel_isolated/moveit_calibration_gui;/home/pe/ws_rockpicker/devel_isolated/moveit_calibration_plugins;/home/pe/ws_rockpicker/devel_isolated/realsense_ting_controller;/home/pe/ws_rockpicker/devel_isolated/wsg_gripper;/home/pe/ws_rockpicker/devel_isolated/ur_calibration;/home/pe/ws_rockpicker/devel_isolated/ur_robot_driver;/home/pe/ws_rockpicker/devel_isolated/ur_kinematics;/home/pe/ws_rockpicker/devel_isolated/ur_gazebo;/home/pe/ws_rockpicker/devel_isolated/ur_description;/home/pe/ws_rockpicker/devel_isolated/ur_dashboard_msgs;/home/pe/ws_rockpicker/devel_isolated/ur5e_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur5_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur5_module;/home/pe/ws_rockpicker/devel_isolated/ur3e_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur3_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur16e_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur10e_moveit_config;/home/pe/ws_rockpicker/devel_isolated/ur10_moveit_config;/home/pe/ws_rockpicker/devel_isolated/universal_robots;/home/pe/ws_rockpicker/devel_isolated/moveit_tutorials;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/pe/ws_rockpicker/devel_isolated/realsense_ting_controller/env.sh')

output_filename = '/home/pe/ws_rockpicker/build_isolated/realsense_ting_controller/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
