#!/usr/bin/env python3
#--------------publicador de Float64--------------
import rospy
from std_msgs.msg import Float64
import random

#el codigo se identifica ante ros
rospy.init_node('codigo21', anonymous=True)

#se crea el publicador
pub = rospy.Publisher('float21', Float64, queue_size=1)

rate = rospy.Rate(0.5) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    valor=round(random.uniform(1, 10), 2) #valor random con 2 decimales
    valor2=valor*2.5
    print(valor2)
    pub.publish(valor2) # se publica el valor
    rate.sleep() # delay de 1 segundo