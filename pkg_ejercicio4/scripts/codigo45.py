#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('codigo45', anonymous=True)	

float_value1 = 0.0
float_value2 = 0.0
float_value3 = 0.0

#se crea la funcion para recibir el mensaje del topico
def callback(data):
    global float_value1,float_value2,float_value3	
    float_value1 = data.x;
    float_value2 = data.y;
    float_value3 = data.z;
    rospy.loginfo("x: %f", float_value1)
    rospy.loginfo("y: %f", float_value2)
    rospy.loginfo("z: %f", float_value3)

# se suscribe al topico
sub = rospy.Subscriber("point44", Point, callback)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo