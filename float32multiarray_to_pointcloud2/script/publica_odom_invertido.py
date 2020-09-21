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


#frame = rospy.get_param("/lidar/frame","Lidar")
#topico = rospy.get_param("/lidar/topic","Lidar")
frameRobo = "laser"
frameGlobal = "map"



#
odometry = Odometry()

def pegaPosicaoRobo():
	global odometry
	try:
		(trans,rot) = listener.lookupTransform(str(frameGlobal), str(frameRobo), rospy.Time(0))
		odometry.pose.pose.position.x = trans[0]
		odometry.pose.pose.position.y = trans[1]
		odometry.pose.pose.position.z = trans[2]
		#odometry.pose.pose.orientation = rot
		odometry.pose.pose.orientation.x = rot[0]
		odometry.pose.pose.orientation.y = rot[1]
		odometry.pose.pose.orientation.z = rot[2]
		odometry.pose.pose.orientation.w = rot[3]
		pub_robot_pose.publish(odometry)
		#print trans[0]
		#print rot
		
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		print "Erro na captura da pose"

def euclidean_distance(p1,p2):
	return math.sqrt(((p2[0]-p1.x)**2) + ((p2[1] - p1.y)**2) + ((p2[2] - p1.z)**2))


def publicaPosicao(data):
	pub = PoseStamped()
	pub.header = data.header
	pub.pose.position = data.point
	pub.pose.orientation.w = 1
	move_goal.publish(pub)


	

if __name__ == '__main__':
	rospy.init_node('odometry_publisher')

	#Subscribe
	#rospy.Subscriber("/clicked_point", PointStamped, callbackClicked_point)
	#publisher
	
	pub_robot_pose = rospy.Publisher("/odom",Odometry)
	listener = tf.TransformListener()
	

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		
		pegaPosicaoRobo()
		
		rate.sleep()

