#!/usr/bin/env python3
import sys
print(sys.path)

from wsg import WSG

from wsg_gripper.srv import GripperCommand, GripperCommandResponse

from time import sleep

import rospy

sleep_time = 2

def handle_command(req):
    print(f"Recieved command: {req.command}")

    cmd = req.command

    if cmd == 'grip':
        print("Gripping...")
        wsg.grip(40)
        #sleep(sleep_time)
        return GripperCommandResponse('Grip command finished')
    if cmd == 'release':
        #print("Releasing...")
        wsg.release()
        sleep(sleep_time)
        return GripperCommandResponse('Release command finished')
    if cmd == 'home':
        print("Homing...")
        wsg.home()
        #sleep(sleep_time)
        return GripperCommandResponse('Home command finished')
    else:
        print("Invalid message!")
        return GripperCommandResponse('Invalid Command')

def gripper_command_server():
    rospy.init_node('gripper_command_server')
    s = rospy.Service('gripper_commands', GripperCommand, handle_command)
    print('Ready to recieve gripper command...')
    rospy.spin()



if __name__ == '__main__':
    wsg = WSG()
    wsg.home()
    gripper_command_server()