#!/usr/bin/env python3
# --------------publicador-suscriptor de Point----------------
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Float64

rospy.init_node('codigo44', anonymous=True)

'''
correr el codigo python
publicar en el topico 'pointsub' con:

rostopic pub /pointsub geometry_msgs/Point "x: 3.0
y: 2.0
z: 1.0" 

escuchar en el topico 'pointpub' con:

rostopic echo /pointpub
'''

float_value=0.0
float_value2=0.0
float_value3=0.0

#se crean funciones para recibir el mensaje del topico
def callback(data):
    global float_value  
    float_value=data.data
    rospy.loginfo("x: %f", float_value)

def callback2(data):
    global float_value2    
    float_value2=data.data
    rospy.loginfo("y: %f", float_value2)

def callback3(data):
    global float_value3  
    float_value3=data.data
    rospy.loginfo("z: %f", float_value3)

# se crea el publicador
pub = rospy.Publisher('point44', Point, queue_size=10)
# se suscribe al topico
sub = rospy.Subscriber("float41", Float64, callback)
# se suscribe al topico
sub2 = rospy.Subscriber("float42", Float64, callback2)
# se suscribe al topico
sub3 = rospy.Subscriber("float43", Float64, callback3)

rate = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():	
	xvalor=float_value
	yvalor=float_value2
	zvalor=float_value3	
	pointmessage = Point(xvalor, yvalor, zvalor)
	pub.publish(pointmessage)
	rate.sleep()