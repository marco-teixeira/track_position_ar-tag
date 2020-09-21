#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16
import math
from geometry_msgs.msg import Twist

from std_msgs.msg import Float64




#variaveis globais
menorDist = []	
angulo = 0.0	
pub_controle = rospy.Publisher('/parar', Int16, queue_size=10)
pub_cmd = rospy.Publisher("/cmd_vel_acoes",Twist)
#cmd_vel_topico = rospy.get_param("/mux_cmd_vel/topico_cmd_vel","cmd_vel")
cmd_vel_topico = "cmd_vel";
msg_cmd = Twist()
menorDistXY = [0,0]
tamanhoRobo = 0.4
desvioObstaculo = 0 #0 para desligado, 1 para ligado 
linha = 1000
angularV = 0
distParada = 0.5

def callback_lidar(data):
	global menorDist, angulo, menorDistXY
	angulo = 0
	menorDist = 200
	for i in range(0, len(data.ranges)):
	        if data.ranges[i] < menorDist and data.ranges[i] != 0 and data.ranges[i]>0.05:
	                anguloTemp = data.angle_min + i*data.angle_increment
	                if anguloTemp < -1.9 and data.ranges[i] < 0.3:
	                        continue
	                else:
	                        angulo = anguloTemp
	                        menorDist = data.ranges[i] 
	                

        menorDistXY[1] = menorDist * math.sin(angulo) #positivo a direita, negativo a esquerda
        menorDistXY[0] = menorDist * math.cos(angulo)
        angulo =  math.degrees(angulo)
  	

                 
def callback_cmd_vel(data):
        global angularV
        angularV = data.angular.z

         
        
def callback_linha(data):        
	   global linha
	   linha = data.data
			 	 
if __name__ == '__main__':
	rospy.init_node('monitoramento_ambiente')
	#Subscribe
	rospy.Subscriber("/scan", LaserScan, callback_lidar)
	rospy.Subscriber("/linha_cv", Float64, callback_linha)
	rospy.Subscriber(str(cmd_vel_topico), Twist, callback_cmd_vel)

	
        #globais
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
	        #pegar diferenca angular
	        #print ("menor dist" +str(menorDist))
	        #print ("Angulo "+str(angulo))
	        #print ("Ponto em X e Y" + str(menorDistXY))
	        
	              
	        if (angularV> 0.1):
	                #print ("Virando para a esquerda "+ str(-angularV-(tamanhoRobo/2)))
	                if (menorDistXY[0] < 0.2 and menorDistXY[1]<0 and menorDistXY[1]> (-angularV-(tamanhoRobo/2))):
	                        print ("Virando para a esquerda "+ str(-angularV-(tamanhoRobo/2)))
	                        pub_controle.publish(1)
	        
	        elif (angularV< -0.1):
	                #print ("Virando para a direita "+ str(-angularV+(tamanhoRobo/2)))
	                if (menorDistXY[0] < 0.25 and menorDistXY[1]>0 and menorDistXY[1]< (-angularV+(tamanhoRobo/2)) ):
	                        print ("Virando para a direita "+ str(-angularV+(tamanhoRobo/2)))
	                        pub_controle.publish(1)
	       
	                                     
	        elif (menorDist < distParada) and (abs(menorDistXY[1]) < (tamanhoRobo/2)):
	                #print("Estou parando")
	                pub_controle.publish(1)
	               
	        else:
	                pub_controle.publish(0)

		rate.sleep()

