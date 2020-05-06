#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PointStamped
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped
import tf
import math


def callbackClicked_point(data):
	global posDesejada
	posDesejada.append(data)


def publicaTrajetoria():
	marker = Marker()
	marker.header.frame_id = "map";
	marker.header.stamp = rospy.Time(0);
	marker.id = 0;
	marker.type = Marker().LINE_STRIP
	marker.action = Marker().ADD
	marker.scale.x = 0.2
	marker.color.a = 1.0
	marker.color.r = 0.0
	marker.color.g = 1.0
	marker.color.b = 0.0
	marker.pose.orientation.x = 0.0
    	marker.pose.orientation.y = 0.0
    	marker.pose.orientation.z = 0.0
    	marker.pose.orientation.w = 1.0
	for i in range (0, len(posDesejada)):
		marker.points.append(posDesejada[i].point)
	pub_rviz_marker.publish(marker)

def pegaPosicaoRobo():
	global robotPose
	try:
		(trans,rot) = listener.lookupTransform('/map', '/Lidar', rospy.Time(0))
		robotPose = trans
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

def limpaMapa(data):
	pub_pose = PoseWithCovarianceStamped()
	try:
		(trans,rot) = listener.lookupTransform('/map', '/Lidar', rospy.Time(0))
		robotPose = trans
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		print "Erro na captura da pose"

	pub_pose.header = data.header
	pub_pose.pose.pose.position = trans
	pub_pose.pose.pose.orientation = rot
	reset_map.publish("reset")
	pub_robot_pose.publish(pub_pose)
	

if __name__ == '__main__':
	rospy.init_node('odometry_publisher')

	#Subscribe
	rospy.Subscriber("/clicked_point", PointStamped, callbackClicked_point)
	#publisher
	move_goal = rospy.Publisher("move_base_simple/goal",PoseStamped)
	pub_rviz_marker = rospy.Publisher("TrajetoriaCrida", Marker, queue_size=10)
	reset_map = rospy.Publisher("/syscommand", String, queue_size=10)
	pub_robot_pose = rospy.Publisher("/initialpose",PoseWithCovarianceStamped)
	
	


	posDesejada = [];
	Quantidade = 1;
	robotPose = []
	listener = tf.TransformListener()
	pontoAtual = -1

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		if Quantidade != len(posDesejada):
			publicaTrajetoria()
			Quantidade = len(posDesejada)

		#logica para ir para o proximo
		pegaPosicaoRobo()
		if len(posDesejada) == 1:
			pontoAtual = 0
			publicaPosicao(posDesejada[pontoAtual])
		

		if len(posDesejada)>0: 
			if (euclidean_distance(posDesejada[pontoAtual].point,robotPose) <= 0.5):
				pontoAtual += 1
				if pontoAtual != -1 and pontoAtual<len(posDesejada):
					publicaPosicao(posDesejada[pontoAtual])

				elif (pontoAtual == (len(posDesejada))):
					pontoAtual = 0
					publicaPosicao(posDesejada[pontoAtual])
					#limpaMapa(posDesejada[pontoAtual])
			
			


		rate.sleep()

