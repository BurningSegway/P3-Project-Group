execute_process(COMMAND "/home/pe/ws_rockpicker/build_isolated/ur_kinematics/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/pe/ws_rockpicker/build_isolated/ur_kinematics/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
