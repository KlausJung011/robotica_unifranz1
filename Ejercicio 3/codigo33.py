#!/usr/bin/env python3
# --------------publicador-suscriptor de Int32--------------
# el codigo escucha al topico 'sub'
# Y publica al topico 'pub' el cuadrado de los valores que lleguen
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('codigo33', anonymous=True)	
# nombre-nodo puede ser cualquiera, 
# preferible que sea igual al nombre del codigo
int_value=0
int_value2=0
 
#se crea la funcion para recibir el mensaje del topico
def callback(data):
	global int_value	
	int_value=data.data
	rospy.loginfo("I heard %d", int_value)	#print de ROS
 
def callback2(data):
	global int_value2	
	int_value2=data.data
	rospy.loginfo("I heard %d", int_value2)	#print de ROS
 
# se crea el publicador
pub = rospy.Publisher('int33', Int32, queue_size=1)
# se suscribe al topico
sub = rospy.Subscriber("int31", Int32, callback)
# se suscribe al topico
sub2 = rospy.Subscriber("int32", Int32, callback2) 

# publicar a floatsub desde terminal con: 
# rostopic pub /intsub std_msgs/Int32 "data: 4"
rate = rospy.Rate(1) # 10hz --> 1/10hz = 0.1s
while not rospy.is_shutdown():
	valor=int_value+int_value2
	pub.publish(valor) # se publica el valor
	rate.sleep() # delay de 0.1 segundos