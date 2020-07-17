#!/usr/bin/env python

import rospy
from std_msgs.msg import ColorRGBA
from ar_track_alvar_msgs.msg import AlvarMarkers
from track_position_ar_tag.msg import info, infoVector
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import math
import numpy



#Getting parameters
track_ar_ids_param = rospy.get_param("/track_position_line/track_ar_ids_param","4, 13").split(",")
track_ar_colors_param = rospy.get_param("/track_position_line/track_ar_colors_param","[0.3,0.5,0.3,1];[1,0,0,1]").split(";")
ros_rate_param = rospy.get_param("/track_position_line/ros_rate_param",10)
queue_size_param = rospy.get_param("/track_position_line/queue_size_param",100)
considered_displacement = rospy.get_param("/track_position_line/considered_displacement",0.02)
output_topic = rospy.get_param("/track_position_line/output_topic","track_position_line")
input_topic = rospy.get_param("/track_position_line/input_topic","/ar_pose_marker")
output_frame = rospy.get_param("/track_position_line/output_frame","usb_cam")
line_scale = rospy.get_param("/track_position_line/line_scale",0.01)


#Global variables
arData = AlvarMarkers()
marker_array = MarkerArray()
info_array = infoVector()
ar_pose_matrix = numpy.full((len(track_ar_ids_param),int(queue_size_param)), Point())
ar_color_rgba = numpy.full(len(track_ar_ids_param), ColorRGBA())
matrix_position = numpy.zeros(len(track_ar_ids_param), int)

pub_rviz_markerArray = rospy.Publisher(output_topic, MarkerArray, queue_size=10)

pub_traveled = rospy.Publisher("/total_traveled", infoVector, queue_size=10)


#configuring the rgb colors of the line
def set_colors():
	global ar_color_rgba
	for i in range(0,len(track_ar_colors_param)):
		if (i<len(track_ar_ids_param)):
			track_ar_colors_param[i] = track_ar_colors_param[i].replace('[','').replace(']','').replace(" ",'')
			temp = track_ar_colors_param[i].split(",")
			ar_color_rgba[i] = ColorRGBA()
			ar_color_rgba[i].r = float(temp[0])
			ar_color_rgba[i].g = float(temp[1])
			ar_color_rgba[i].b = float(temp[2])
			ar_color_rgba[i].a = float(temp[3])
	

#get ar tag position
def ar_callback(data):
	for point in data.markers:
		for i in range(0,len(track_ar_ids_param)):
			if (point.id) == int(track_ar_ids_param[i]):
				if (matrix_position[i] < queue_size_param):
				        if euclidean_distance(ar_pose_matrix[i][matrix_position[i]-1],point.pose.pose.position) > float(considered_displacement):
					        ar_pose_matrix[i][matrix_position[i]] = Point()
					        ar_pose_matrix[i][matrix_position[i]].x = point.pose.pose.position.x
					        ar_pose_matrix[i][matrix_position[i]].y = point.pose.pose.position.y
					        ar_pose_matrix[i][matrix_position[i]].z = point.pose.pose.position.z
					        matrix_position[i] += 1;
				else:
					if euclidean_distance(ar_pose_matrix[i][matrix_position[i]-1],point.pose.pose.position) > float(considered_displacement):
						ar_pose_matrix[i] = numpy.roll(ar_pose_matrix[i], -1, axis=0)
						ar_pose_matrix[i][matrix_position[i]-1] = Point()
						ar_pose_matrix[i][matrix_position[i]-1].x = point.pose.pose.position.x
						ar_pose_matrix[i][matrix_position[i]-1].y = point.pose.pose.position.y
						ar_pose_matrix[i][matrix_position[i]-1].z = point.pose.pose.position.z	
					

def euclidean_distance(p1,p2):
	return math.sqrt(((p2.x-p1.x)**2) + ((p2.y - p1.y)**2) + ((p2.z - p1.z)**2))

#configuring the rgb colors of the line
def pub_tracker():
	marker_array.markers = []

	for i in range(0,len(track_ar_ids_param)):
		marker = Marker()
		marker.header.frame_id = output_frame;
	    	marker.header.stamp = rospy.Time(0);
	    	marker.id = i;
		marker.type = Marker().LINE_STRIP
		marker.action = Marker().ADD
		marker.scale.x = float(line_scale)
		marker.color = ar_color_rgba[i]
		marker.pose.orientation.x = 0.0;
    		marker.pose.orientation.y = 0.0;
    		marker.pose.orientation.z = 0.0;
    		marker.pose.orientation.w = 1.0;
		marker.points = (ar_pose_matrix[i][0:matrix_position[i]]);
		marker_array.markers.append(marker)

	pub_rviz_markerArray.publish(marker_array)

def pub_total_traveled():
        info_array.info_vector = []
        for i in range(0,len(track_ar_ids_param)):
                dist = 0
                for j in range(1, len(ar_pose_matrix[i])-1):   
                        dist = dist + euclidean_distance(ar_pose_matrix[i][j],ar_pose_matrix[i][j+1])
                inf = info()
                inf.id = int(track_ar_ids_param[i])
                inf.dist = dist;
                info_array.info_vector.append(inf)
        pub_traveled.publish(info_array)
        print (dist)


if __name__ == '__main__':
	rospy.init_node('trackPositionArTag', anonymous=True)
	rate = rospy.Rate(float(ros_rate_param)) 
	rospy.Subscriber(input_topic, AlvarMarkers, ar_callback)
	set_colors()
	while not rospy.is_shutdown():
		pub_tracker()
		pub_total_traveled()
		rate.sleep()
	


		
	
	
