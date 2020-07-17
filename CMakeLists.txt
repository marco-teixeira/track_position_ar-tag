cmake_minimum_required(VERSION 2.8.3)
project(track_position_ar_tag)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
    info.msg
    infoVector.msg
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


