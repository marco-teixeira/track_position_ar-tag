#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped



rospy.init_node('arrumaRviz',anonymous=True)
pub = rospy.Publisher("/move_base_simple/goal",PoseStamped)

#variaveis globais

def callback(data):
	data.pose.orientation.w = 1
	pub.publish(data)


#Subscribe
rospy.Subscriber("/goal", PoseStamped, callback)

#publisher


rospy.spin()



	

	

