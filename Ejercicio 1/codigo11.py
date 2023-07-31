#!/usr/bin/env python3
#--------------publicador de Float64--------------
import rospy
from std_msgs.msg import Float64
import random

#el codigo se identifica ante ros
rospy.init_node('codigo11', anonymous=True)

#se crea el publicador
pub = rospy.Publisher('float11', Float64, queue_size=1)

rate = rospy.Rate(0.5) # 0.5hz --> 1/0.5hz=2s
while not rospy.is_shutdown():
    valor=round(random.uniform(1, 10), 2) #valor random con 2 decimales
    print(valor)
    pub.publish(valor) # se publica el valor
    rate.sleep() # delay de 1 segundo