#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point


rospy.init_node('codigo54', anonymous=True)	

int_value1=0
int_value2=0
int_value3=0

#se crea la funcion para recibir el mensaje del topico
def callback(data):
    global int_value1,int_value2,int_value3	
    int_value1 = data.x;
    int_value2 = data.y;
    int_value3 = data.z;
    rospy.loginfo("x: %f", int_value1)
    rospy.loginfo("y: %f", int_value2)
    rospy.loginfo("z: %f", int_value3)

pub = rospy.Publisher('quat54', Quaternion, queue_size=10)
sub = rospy.Subscriber("point53", Point, callback)

rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():	
    xvalor=int_value1
    yvalor=int_value2
    zvalor=int_value3
    wvalor=int_value1+int_value2+int_value3
    pointmessage = Quaternion(xvalor, yvalor, zvalor, wvalor)
    print(pointmessage)
    pub.publish(pointmessage)
    rate.sleep()