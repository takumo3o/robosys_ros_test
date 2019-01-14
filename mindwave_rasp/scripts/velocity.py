#!/usr/bin/env python

import rospy
from pimouse_ros.srv import TimedMotion
from std_srvs.srv import Trigger
from mindwave_rasp.msg import MindwaveValues
import sys

class Attu:
    def __init__(self):
        self.meditation = None
        self.attention = None
        print("wait service")
        map(rospy.wait_for_service,['/timed_motion','/motor_on','/motor_off'])
        print("wait service done")
        rospy.ServiceProxy('/motor_on', Trigger).call()
        self.tm = rospy.ServiceProxy('/timed_motion', TimedMotion)

    def callback(self, message):
       
        self.meditation = message.meditation*10
        self.attention = message.attention*10

if __name__ == '__main__':
    rospy.init_node('mouse_volocity')
    j = Attu()
    sub = rospy.Subscriber('neuro', MindwaveValues, j.callback)
    # rospy.spin()
    rate = rospy.Rate(1000)
    while not rospy.is_shutdown():
        if j.meditation == None or j.attention == None:
            rate.sleep()
            continue
        rospy.loginfo("meditation = %s", j.meditation)
        rospy.loginfo("attention = %s", j.attention)
        j.tm(j.meditation, j.attention, 1000)
        rate.sleep()
