#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist

rospy.init_node('codigo55', anonymous=True)	

int_value1=0
int_value2=0
int_value3=0
int_value4=0

def callback(data):
	#rospy.loginfo("I heard %d", data.x) #como print
	global int_value1,int_value2,int_value3,int_value4
	int_value1 = data.x;
	int_value2 = data.y;
	int_value3 = data.z;
	int_value4 = data.w;
	rospy.loginfo("x: %f", int_value1)
	rospy.loginfo("y: %f", int_value2)
	rospy.loginfo("z: %f", int_value3)
	rospy.loginfo("w: %f", int_value4)
	
pub = rospy.Publisher('twist55', Twist, queue_size=10)
sub = rospy.Subscriber("quat54", Quaternion, callback) 
 
rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
    twistmessage = Twist()
    twistmessage.linear.x= int_value1
    twistmessaje.linear.y= int_value2
    twistmessaje.linear.z= int_value3
    twistmessaje.angular.x=int_value4
    int_value5=int_value1+int_value2+int_value3+int_value4
    twistmessaje.angular.y= int_value5
    twistmessaje.angular.z=int_value5*int_value5
    pub.publish(twistmessaje)
    print(twistmessaje)
    rate.sleep()
