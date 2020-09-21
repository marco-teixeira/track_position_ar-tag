#!/usr/bin/env python


# Python includes
import numpy
import random

# ROS includes
import roslib
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from tf import transformations # rotation_matrix(), concatenate_matrices()
from visualization_msgs.msg import Marker


# Initialize the ROS Node
rospy.init_node('m09', anonymous=False, log_level=rospy.INFO, disable_signals=False)




pub_rviz_marker = rospy.Publisher("marker", Marker, queue_size=10)

while not rospy.is_shutdown():

 	#----
	markers = Marker()
	markers.header.frame_id = "/odom";
    	markers.header.stamp = rospy.Time(0);
	markers.ns = "my_namespace";
    	markers.id = 0;
	markers.type = 9;
	markers.action = Marker().ADD
	# Set the pose of the marker.  This is a full 6DOF pose relative to the frame/time specified in the header
	markers.pose.position.x = -5.1;
	markers.pose.position.y = -11.3;
	markers.pose.position.z = 0;
	#markers.pose.orientation.x = 0;
	#markers.pose.orientation.y = 0;
	#markers.pose.orientation.z = 0;
	#markers.pose.orientation.w = 1;
	#// Set the scale of the marker -- 1x1x1 here means 1m on a side
	#markers.scale.x = 0.001;
	#markers.scale.y = 0.001;
	markers.scale.z = 5;
	#// Set the color -- be sure to set alpha to something non-zero!
	markers.color.r = 0;
	markers.color.g = 0;
	markers.color.b = 1;
	markers.color.a = 1;

	markers.text = "M09";

	#---------------------
	pub_rviz_marker.publish(markers);

    	rospy.Rate(1).sleep() #1 Hz

		
		
