#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('codigo12', anonymous=True)	

float_value=0.0

#se crea la funcion para recibir el mensaje del topico
def callback(data):	    
    float_value=data.data
    print(float_value)

# se suscribe al topico
sub = rospy.Subscriber("float11", Float64, callback)
# el codigo float_pub.py publica al topico 'random_float'

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo