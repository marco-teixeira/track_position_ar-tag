#!/usr/bin/env python

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('odometry_publisher')

odom_pub = rospy.Publisher("odom_hector", Odometry, queue_size=50)
#odom_broadcaster = tf.TransformBroadcaster()

#x = 0.0
#y = 0.0
#th = 0.0

#vx = 0
#vy = 0
#vth = 0

#current_time = rospy.Time.now()
#last_time = rospy.Time.now()

r = rospy.Rate(10)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    listener = tf.TransformListener()
    rospy.sleep(1.5)
    (trans,rot) = listener.lookupTransform("map_hector","scanmatcher_frame",rospy.Time(0))

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "map_hector"

    # set the position
    odom.pose.pose = Pose(Point(trans[0],trans[1],trans[2]), Quaternion(rot[0],rot[1],rot[2],rot[3 ]))

    # set the velocity
    #odom.child_frame_id = "base_link"
    #odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()	
