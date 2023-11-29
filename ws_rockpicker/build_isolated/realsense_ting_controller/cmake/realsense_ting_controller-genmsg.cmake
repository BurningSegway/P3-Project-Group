# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "realsense_ting_controller: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(realsense_ting_controller_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_custom_target(_realsense_ting_controller_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "realsense_ting_controller" "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(realsense_ting_controller
  "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_ting_controller
)

### Generating Module File
_generate_module_cpp(realsense_ting_controller
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_ting_controller
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(realsense_ting_controller_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(realsense_ting_controller_generate_messages realsense_ting_controller_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_dependencies(realsense_ting_controller_generate_messages_cpp _realsense_ting_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_ting_controller_gencpp)
add_dependencies(realsense_ting_controller_gencpp realsense_ting_controller_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_ting_controller_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(realsense_ting_controller
  "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_ting_controller
)

### Generating Module File
_generate_module_eus(realsense_ting_controller
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_ting_controller
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(realsense_ting_controller_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(realsense_ting_controller_generate_messages realsense_ting_controller_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_dependencies(realsense_ting_controller_generate_messages_eus _realsense_ting_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_ting_controller_geneus)
add_dependencies(realsense_ting_controller_geneus realsense_ting_controller_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_ting_controller_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(realsense_ting_controller
  "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_ting_controller
)

### Generating Module File
_generate_module_lisp(realsense_ting_controller
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_ting_controller
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(realsense_ting_controller_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(realsense_ting_controller_generate_messages realsense_ting_controller_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_dependencies(realsense_ting_controller_generate_messages_lisp _realsense_ting_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_ting_controller_genlisp)
add_dependencies(realsense_ting_controller_genlisp realsense_ting_controller_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_ting_controller_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(realsense_ting_controller
  "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_ting_controller
)

### Generating Module File
_generate_module_nodejs(realsense_ting_controller
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_ting_controller
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(realsense_ting_controller_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(realsense_ting_controller_generate_messages realsense_ting_controller_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_dependencies(realsense_ting_controller_generate_messages_nodejs _realsense_ting_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_ting_controller_gennodejs)
add_dependencies(realsense_ting_controller_gennodejs realsense_ting_controller_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_ting_controller_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(realsense_ting_controller
  "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_ting_controller
)

### Generating Module File
_generate_module_py(realsense_ting_controller
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_ting_controller
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(realsense_ting_controller_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(realsense_ting_controller_generate_messages realsense_ting_controller_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pe/ws_rockpicker/src/realsense_ting_controller/srv/ImageCapture.srv" NAME_WE)
add_dependencies(realsense_ting_controller_generate_messages_py _realsense_ting_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(realsense_ting_controller_genpy)
add_dependencies(realsense_ting_controller_genpy realsense_ting_controller_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS realsense_ting_controller_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_ting_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/realsense_ting_controller
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(realsense_ting_controller_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_ting_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/realsense_ting_controller
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(realsense_ting_controller_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_ting_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/realsense_ting_controller
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(realsense_ting_controller_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_ting_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/realsense_ting_controller
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(realsense_ting_controller_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_ting_controller)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_ting_controller\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/realsense_ting_controller
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(realsense_ting_controller_generate_messages_py std_msgs_generate_messages_py)
endif()
