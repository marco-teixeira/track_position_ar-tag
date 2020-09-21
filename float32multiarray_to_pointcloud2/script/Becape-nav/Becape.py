#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry
import math
import numpy as np
#Controle Fuzzy
import Fuzzy_posicao 
import Fuzzy_desvio_obstaculo 
from skfuzzy import control as ctrl
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


#Variaveis Fuzzy 
Fangular = ctrl.ControlSystemSimulation(Fuzzy_posicao.tipping_ctrl)
Fdesvio = ctrl.ControlSystemSimulation(Fuzzy_desvio_obstaculo.tipping_ctrl)

menorDist = []	
angulo = 0.0	
posDesejada = [1,1]
robotPosition = [0,0]
robotOrientation = 0.0
ErroAngular = 0.0
ErroLinear = 0.0
Avel = 0.0
Lvel = 0.0
odomTopico = "/odom"
cmdVelTopico = "RosAria/cmd_vel"
desviarObstaculo = 0 #0 desativado, 1 ativado
#pub
velocity_publisher = rospy.Publisher(cmdVelTopico, Twist, queue_size=10)
msg = Twist()

def callback_lidar(data):
	global menorDist, angulo
	angulo = 0
	menorDist = 200
	for i in range(0, len(data.ranges)):
	        if data.ranges[i] < menorDist and data.ranges[i] != 0:
	                menorDist = data.ranges[i] 
	                angulo = data.angle_min + i*data.angle_increment
	                angulo =  math.degrees(angulo)
	#print "Menor Distancia"+ str(menorDist) + "Menor angulo "+str(angulo)
	
	
def callbackClicked_point(data):
	global posDesejada
	print("Estou aqui")
	posDesejada[0] = data.point.x
	posDesejada[1] = data.point.y
	
	
def callbacOdom(data):
        global robotOrientation
        robotPosition[0] = data.pose.pose.position.x;
        robotPosition[1] = data.pose.pose.position.y;
        robotOrientation = (float(tf.transformations.euler_from_quaternion([data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w])[2]))
        #print(str(temp));
        

        
        
def angle_between():
            global ErroAngular
	    ang1 = math.atan2((posDesejada[1]-robotPosition[1]),(posDesejada[0]-robotPosition[0]))
	    if ang1 < 0:
	        ang1 = 3.14 + (3.14 - abs(ang1))
	        
	    temp = ang1 - robotOrientation
	    if abs(temp)>3.14:
	         temp = 6.28 - abs(temp)
	         if (robotOrientation < ang1):
	                temp = temp*-1
	          
	    
	    ErroAngular = math.degrees(temp)

	    
def distanciaEuclidiana():
        global ErroLinear
	ErroLinear =  math.sqrt(((posDesejada[0]-robotPosition[0])**2) + ((posDesejada[1] - robotPosition[1])**2));


if __name__ == '__main__':
	rospy.init_node('navegacao_ponto_a_ponto')
        rate = rospy.Rate(5) # 10hz
	#Subscribe
	rospy.Subscriber("/clicked_point", PointStamped, callbackClicked_point)
	rospy.Subscriber(odomTopico, Odometry, callbacOdom)
	rospy.Subscriber("/scan", LaserScan, callback_lidar)
	#publisher
	angle_between()
	while not rospy.is_shutdown():
	        angle_between()
	        distanciaEuclidiana()
	        #print (ErroLinear)
	        #print("Dados Lidar: menor dist "+str(menorDist)+"Angulo "+str(angulo))
	        #print("Pos clicada "+str(posDesejada))
	        #print("Pos do Robo "+str(robotPosition))
	        #print("orientacao do robo: "+str(robotOrientation))
	        #print("Diferenca angular "+str(ErroAngular))
	        try:
	                if menorDist < 0.5 and abs(angulo) < 70:
	                        if desviarObstaculo == 1:
	                                print("Estou desviando")
	                                Fdesvio.input['DistanciaY'] = (angulo+180)
	                                Fdesvio.input['DistanciaX'] = 5
	                                Fdesvio.compute()
	                                Avel = Fdesvio.output['velocidadeAngular']
	                                Lvel = Fdesvio.output['velocidadeLinear']
		                        if (Avel >= 0.45):
		                                Avel = 0.45
		                        if (Avel <= -0.45):
			                        Avel = -0.45
	                
	                
	                else:
	                        if ErroLinear < 0.2:
	                                Avel = 0
	                                Lvel = 0
	                        else:
	                                Fangular.input['DistanciaY'] = ErroAngular
	                                Fangular.input['DistanciaX'] = ErroLinear
	                                Fangular.compute()
	                                Avel = Fangular.output['velocidadeAngular']
	                                Lvel = Fangular.output['velocidadeLinear']
		                        if (Avel >= 0.45):
		                                Avel = 0.45
		                        if (Avel <= -0.45):
			                        Avel = -0.45
			                
		        msg.angular.z = Avel
		        msg.linear.x = Lvel
	                velocity_publisher.publish(msg)
	        except:
	                msg.angular.z = 0
	                velocity_publisher.publish(msg)
	        
	        rate.sleep()

