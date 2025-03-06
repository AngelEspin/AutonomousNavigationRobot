cmake_minimum_required(VERSION 3.0.2)
project(robot_description)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
# find dependencies
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()
find_package(catkin REQUIRED COMPONENTS
  rospy
  urdf
  xacro
  std_msg
  controller_manager
  joint_state_controller
  robot_state_publisher
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)
## Especifique los scripts para instalar

install(
  DIRECTORY
    rviz
    launch
    robot
    controller/controller.py
  DESTINATION
   share/${robot_description}/
)
ament_package()
