#!/usr/bin/env python3

from std_msgs.msg import Header
from std_msgs.msg import Int8MultiArray
from geometry_msgs.msg import Twist, Vector3
import rospy
import time


def response():
	linear = Vector3(0,0,0)
	angular = Vector3(0,0,0)
	twist = Twist(linear, angular)
	pub.publish(twist)
	print("Emergency stop time")


rospy.init_node('emergency_stop')    # initialize ourselves with roscore
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

init_twist = Twist(Vector3(0.5,0,0), Vector3(0,0,0))
pub.publish(init_twist)

sub = rospy.Subscriber("/bump", Int8MultiArray, response())
rospy.spin()

time.sleep(1)


# rospy.Rate specifies the rate of the loop (in this case 2 Hz)
# r = rospy.Rate(2)
# while not rospy.is_shutdown():
#     # my_point_stamped.header.stamp = rospy.Time.now()    # update timestamp
#     pub.publish(init_twist)
#     print('hiiii')
#     r.sleep()

# rospy.spin()