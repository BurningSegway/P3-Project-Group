#!/usr/bin/env python3

#This is the service server that takes requests, that control the gripper.

import sys
print(sys.path)

from wsg import WSG #Import the wsg script as a module, a script to communicate with the wsg gripper through its text based command interface, provided by Columbia Robovision Lab, as stated by the license

from wsg_gripper.srv import GripperCommand, GripperCommandResponse

from time import sleep

import rospy

def handle_command(req):
    '''
    This function handles the service requests, executes the command on the gripper, and returns a response that it has finished the requested command
    '''

    #Print the command, to let the operator know
    print(f"Recieved command: {req.command}")

    #Takes the message, and saves the command part
    cmd = req.command

    #Check if the command is a valid command, through and if chain.
    if cmd == 'grip':
        print("Gripping...")
        wsg.grip(80) #Gripping with 80 newtons of force
        return GripperCommandResponse('Grip command finished')
    if cmd == 'release':
        print("Releasing...")
        wsg.release() #Realease the gripper, moving the fingers exactly 10 mm back from the gripping position
        return GripperCommandResponse('Release command finished')
    if cmd == 'home':
        print("Homing...")
        wsg.home() #Homing the gripper, moving the fingers furthest apart from eachother
        return GripperCommandResponse('Home command finished')
    else: #If the command was invalid, return Invalid command
        print("Invalid message!")
        return GripperCommandResponse('Invalid Command')

def gripper_command_server():
    '''
    This function handles the initialization of the service server node
    '''
    rospy.init_node('gripper_command_server') #Init node
    s = rospy.Service('gripper_commands', GripperCommand, handle_command) #Declare the servide, with the name of the service, the service message, and what function handles the requests
    print('Ready to recieve gripper command...') 
    rospy.spin() #Tells python not to exit script unless the node is shutdown



if __name__ == '__main__': #this checks is the file is run as a script, as it should. And would return false if it was imported as a module
    wsg = WSG() #Instanciate an object of WSG
    wsg.home() #Home the gripper as te first thing
    gripper_command_server() #Run main function