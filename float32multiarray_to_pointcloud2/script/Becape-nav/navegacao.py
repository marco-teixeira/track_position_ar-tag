#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PointStamped
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
import tf
import math
from geometry_msgs.msg import Twist, Pose
import numpy as np
import tf


frame = rospy.get_param("/lidar/frame","base_link")
#topico = rospy.get_param("/lidar/topic","Lidar")

pub_cmd = rospy.Publisher("cmd_vel",Twist)
msg_cmd = Twist()


		

def callbackClicked_point(data):
	global posDesejada
	posDesejada = (data)
	#print posDesejada.pose.position.x


def callbackOdom(data):
	global robotPose, roboOrientation
	robotPose = (data.pose)
	#print robotPose.pose.orientation
	roll, pitch, yaw = tf.transformations.euler_from_quaternion([robotPose.pose.orientation.x,robotPose.pose.orientation.y, robotPose.pose.orientation.z, robotPose.pose.orientation.w])
	roboOrientation = yaw
	#print roboOrientation



def euclidean_distance(p1,p2):
	return math.sqrt(((p2[0]-p1.x)**2) + ((p2[1] - p1.y)**2) + ((p2[2] - p1.z)**2))
	
	
def angle_between(p1, p2, robotA):
	ang1 = np.arctan2(*p1[::-1])
	ang2 = np.arctan2(*p2[::-1])
	dif = ((ang1 - ang2) % (2 * np.pi)) - robotA
	if dif<0:
	        dif =  3.14 + (3.14 - abs(dif));
	if (abs(dif) > 3.14):
	     dif =   6.28 - abs(dif) 
	     dif = dif*-1
	return np.rad2deg(dif) - 90


			   
			 	 
if __name__ == '__main__':
	rospy.init_node('navegacao_AMR')
	#Subscribe
	rospy.Subscriber("/move_base_simple/goal", PoseStamped, callbackClicked_point)
	rospy.Subscriber("/odom", Odometry, callbackOdom)
	
        #globais
	posDesejada = []
	robotPose = []
	roboOrientation = 0
	
	

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
	        #pegar diferenca angular
	        if (posDesejada != []):
	                digAng = angle_between([robotPose.pose.position.x, robotPose.pose.position.y],[posDesejada.pose.position.x, posDesejada.pose.position.y], roboOrientation)
	                print digAng
	        #pegar dist euclidiana
			
			


		rate.sleep()

