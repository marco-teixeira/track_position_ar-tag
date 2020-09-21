#!/usr/bin/env python

import rospy
import tf
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

#parametros do ROS
cmd_vel_topico = rospy.get_param("/mux_cmd_vel/topico_cmd_vel","RosAria/cmd_vel")


#variaveis globais
parar = 0
cmd_vel_magnetico = Twist()	
cmd_vel_linha_cv = Twist()

cmd_vel_monitoramento_ambiente =  Twist()


pub_cmd = rospy.Publisher(str(cmd_vel_topico),Twist)
msg_cmd = Twist()

def callback_parar(data):
	global parar
	parar = data.data
	
def callback_cmd_vel_magnetico(data):
	global cmd_vel_magnetico
	cmd_vel_magnetico = data

	
def callback_cmd_vel_linha_cv(data):
	global cmd_vel_linha_cv
	cmd_vel_linha_cv = data
	
def callback_cmd_vel_monitoramento_ambiente(data):
	global cmd_vel_monitoramento_ambiente
	cmd_vel_monitoramento_ambiente = data

			    	 
if __name__ == '__main__':
	rospy.init_node('mux_cmd_vel')
	#Subscribe
	rospy.Subscriber("/parar", Int16, callback_parar)
	rospy.Subscriber("/cmd_vel_magnetico", Twist, callback_cmd_vel_magnetico)
	rospy.Subscriber("/cmd_vel_linha_cv", Twist, callback_cmd_vel_linha_cv)
	rospy.Subscriber("/cmd_vel_acoes", Twist, callback_cmd_vel_monitoramento_ambiente)

	
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
	        #pegar diferenca angular
	        if (parar == 1):
	                print ("Estou no parar")
	                msg_cmd.linear.x = 0
	                msg_cmd.angular.z = 0
	                pub_cmd.publish(msg_cmd)

	        elif (parar == 2):
	                print("Estou no acao")
	                pub_cmd.publish(cmd_vel_monitoramento_ambiente)

	        else:
	                pub_cmd.publish(cmd_vel_linha_cv)

		rate.sleep()

