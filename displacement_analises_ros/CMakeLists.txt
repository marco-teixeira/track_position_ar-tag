cmake_minimum_required(VERSION 2.8.3)
project(displacement_analises_ros)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)



catkin_package(

)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


