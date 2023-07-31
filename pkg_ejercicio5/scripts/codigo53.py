#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('codigo53', anonymous=True)	
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
pub = rospy.Publisher('point53', Point, queue_size=10)
# se suscribe al topico
sub = rospy.Subscriber("int51", Int32, callback)
# se suscribe al topico
sub2 = rospy.Subscriber("int52", Int32, callback2) 

rate = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():
	xvalor=int_value
	yvalor=int_value2
	zvalor=int_value+int_value2
	pointmessage = Point(xvalor, yvalor, zvalor)
	print(pointmessage)
	pub.publish(pointmessage) 
	rate.sleep()
