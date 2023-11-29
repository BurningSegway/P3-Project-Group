# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "wsg_gripper: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(wsg_gripper_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_custom_target(_wsg_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "wsg_gripper" "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(wsg_gripper
  "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/wsg_gripper
)

### Generating Module File
_generate_module_cpp(wsg_gripper
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/wsg_gripper
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(wsg_gripper_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(wsg_gripper_generate_messages wsg_gripper_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_dependencies(wsg_gripper_generate_messages_cpp _wsg_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(wsg_gripper_gencpp)
add_dependencies(wsg_gripper_gencpp wsg_gripper_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS wsg_gripper_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(wsg_gripper
  "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/wsg_gripper
)

### Generating Module File
_generate_module_eus(wsg_gripper
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/wsg_gripper
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(wsg_gripper_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(wsg_gripper_generate_messages wsg_gripper_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_dependencies(wsg_gripper_generate_messages_eus _wsg_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(wsg_gripper_geneus)
add_dependencies(wsg_gripper_geneus wsg_gripper_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS wsg_gripper_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(wsg_gripper
  "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/wsg_gripper
)

### Generating Module File
_generate_module_lisp(wsg_gripper
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/wsg_gripper
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(wsg_gripper_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(wsg_gripper_generate_messages wsg_gripper_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_dependencies(wsg_gripper_generate_messages_lisp _wsg_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(wsg_gripper_genlisp)
add_dependencies(wsg_gripper_genlisp wsg_gripper_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS wsg_gripper_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(wsg_gripper
  "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/wsg_gripper
)

### Generating Module File
_generate_module_nodejs(wsg_gripper
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/wsg_gripper
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(wsg_gripper_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(wsg_gripper_generate_messages wsg_gripper_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_dependencies(wsg_gripper_generate_messages_nodejs _wsg_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(wsg_gripper_gennodejs)
add_dependencies(wsg_gripper_gennodejs wsg_gripper_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS wsg_gripper_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(wsg_gripper
  "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/wsg_gripper
)

### Generating Module File
_generate_module_py(wsg_gripper
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/wsg_gripper
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(wsg_gripper_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(wsg_gripper_generate_messages wsg_gripper_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/wsg_gripper/srv/GripperCommand.srv" NAME_WE)
add_dependencies(wsg_gripper_generate_messages_py _wsg_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(wsg_gripper_genpy)
add_dependencies(wsg_gripper_genpy wsg_gripper_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS wsg_gripper_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/wsg_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/wsg_gripper
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(wsg_gripper_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/wsg_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/wsg_gripper
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(wsg_gripper_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/wsg_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/wsg_gripper
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(wsg_gripper_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/wsg_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/wsg_gripper
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(wsg_gripper_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/wsg_gripper)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/wsg_gripper\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/wsg_gripper
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(wsg_gripper_generate_messages_py std_msgs_generate_messages_py)
endif()
