cmake_minimum_required(VERSION 2.8.3)
project(alvaro)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)


generate_messages(
  DEPENDENCIES
    std_msgs
)


catkin_package(
  CATKIN_DEPENDS
    message_runtime
    std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


