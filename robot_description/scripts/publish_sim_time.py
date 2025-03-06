#!/usr/bin/env python

import rospy
from rosgraph_msgs.msg import Clock

if __name__ == '__main__':
    rospy.init_node('clock_publisher')
    pub = rospy.Publisher('/clock', Clock, queue_size=10)
    rate = rospy.Rate(1)  # Frecuencia de publicación (1 Hz)

    while not rospy.is_shutdown():
        clock_msg = Clock()
        clock_msg.clock = rospy.Time.now()
        pub.publish(clock_msg)
        rate.sleep()
