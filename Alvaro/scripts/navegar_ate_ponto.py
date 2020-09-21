#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry
import math
import numpy as np
#Controle Fuzzy
import Fuzzy_posicao 
from skfuzzy import control as ctrl
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Path
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int16
from std_msgs.msg import Float64
#Variaveis Fuzzy 
Fangular = ctrl.ControlSystemSimulation(Fuzzy_posicao.tipping_ctrl)

topico_pose_des = rospy.get_param("/navegar_ate_ponto/topico_ponto","/ponto_desejado")

menorDist = []	
angulo = 0.0	
posDesejada = [0,0]
robotPosition = [0,0]
robotOrientation = 0.0
ErroAngular = 0.0
ErroLinear = 0.0
Avel = 0.0
Lvel = 0.0
odomTopico = "/odom"
cmdVelTopico = "/cmd_vel"
debug = 1
#pub
velocity_publisher = rospy.Publisher(cmdVelTopico, Twist, queue_size=10)
msg = Twist()
path = Path()

	
def callback_point(data):
	global posDesejada, path ,robotPosition
	robotPosition[0] = data.x
	robotPosition[1] = data.y
	
	
def callbacOrientation(data):
        global robotOrientation
        #print ("Estou aqui")
        robotOrientation = math.radians(data.data-180)
       
        

def angle_between():
            global ErroAngular
	    ang1 = math.atan2((posDesejada[1]-robotPosition[1]),(posDesejada[0]-robotPosition[0]))
	    '''
	    if ang1 < 0:
	        ang1 = 3.14 + (3.14 - abs(ang1))
	        
	    temp = ang1 - robotOrientation
	    if abs(temp)>3.14:
	         temp = 6.28 - abs(temp)
	         if (robotOrientation < ang1):
	                temp = temp*-1
	    ErroAngular = math.degrees(temp)      
	    if temp > 0:
	       ErroAngular = 180 -math.degrees(temp)
	    else:
                ErroAngular = 180 +math.degrees(temp) + math.degrees(robotOrientation)
	    '''
	    ErroAngular = math.degrees(ang1-robotOrientation)+90
	    
	    
def distanciaEuclidiana():
        global ErroLinear
	ErroLinear =  math.sqrt(((posDesejada[0]-robotPosition[0])**2) + ((posDesejada[1] - robotPosition[1])**2));


if __name__ == '__main__':
	rospy.init_node('navegacao_ponto_a_ponto')
        rate = rospy.Rate(5) # 10hz
	#Subscribe
	rospy.Subscriber("/position", Point, callback_point)
	rospy.Subscriber("/orientation", Float64, callbacOrientation)

	
	#pubPath = rospy.Publisher("/nav_path",Path)
	
	#publisher
	angle_between()
	while not rospy.is_shutdown():
	        angle_between()
	        distanciaEuclidiana()
	        
	        #verifica as veriaveiz 
	        if debug == 1:
	                print (ErroLinear)
	                print("Dados Lidar: menor dist "+str(menorDist)+"Angulo "+str(angulo))
	                print("Pos clicada "+str(posDesejada))
	                print("Pos do Robo "+str(robotPosition))
	                print("orientacao do robo: "+str(math.degrees(robotOrientation)))
	                print("Diferenca angular "+str(ErroAngular))
	                
	        try:
	                if ErroLinear < 0.1:
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
		        msg.linear.x = 0
	                velocity_publisher.publish(msg)
	        
	        rate.sleep()

