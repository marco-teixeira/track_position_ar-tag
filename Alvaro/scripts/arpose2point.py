#!/usr/bin/env python

import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
import math
import numpy
import tf
import math



#Global variables
pub_point = rospy.Publisher("/position", Point, queue_size=10)
pub_orientation = rospy.Publisher("/orientation", Float64, queue_size=10)
ponto = Point()
roboID = 9

#get ar tag position
def ar_callback(data):
	for point in data.markers:
                if (point.id) == roboID:
                        #print ("Estou aqui dentro")
			ponto.x	= point.pose.pose.position.x
			ponto.y = point.pose.pose.position.y
			ponto.z = point.pose.pose.position.z	
			pub_point.publish(ponto)
			
			#print(math.degrees(float(tf.transformations.euler_from_quaternion([point.pose.pose.orientation.x, point.pose.pose.orientation.y, point.pose.pose.orientation.z, point.pose.pose.orientation.w])[2])))
			pub_orientation.publish(math.degrees(float(tf.transformations.euler_from_quaternion([point.pose.pose.orientation.x, point.pose.pose.orientation.y, point.pose.pose.orientation.z, point.pose.pose.orientation.w])[2]))+180)





if __name__ == '__main__':
	rospy.init_node('trackPositionArTag', anonymous=True)
	rate = rospy.Rate(10) 
	rospy.Subscriber("/ar_pose_marker", AlvarMarkers, ar_callback)
	rospy.spin()
	
	


		
	
	
