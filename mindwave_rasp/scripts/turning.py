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
        #rospy.loginfo("meditation = %s", message.meditation)
        #rospy.loginfo("attention = %s", message.attention)

        self.meditation = message.meditation
        self.attention = message.attention

        # if (message.meditation > 70 and message.attention < 70):
        #     self.tm(600, 200, 4000)
        #     rospy.loginfo("right")
        # elif (message.meditation < 70 and message.attention > 70):
        #     rospy.loginfo("left")
        #     self.tm(200, 600, 4000)
        # elif (message.meditation < 70 and message.attention < 70) or (message.meditation > 70 and message.attention > 70):
        #     self.tm(0, 0, 4000)
        #     rospy.loginfo("stop")

if __name__ == '__main__':
    rospy.init_node('mouse_velocity')
    j = Attu()
    sub = rospy.Subscriber('neuro', MindwaveValues, j.callback)
    # rospy.spin()
    rate = rospy.Rate(3)
    while not rospy.is_shutdown():
        if j.meditation == None or j.attention == None:
            rate.sleep()
            continue
        rospy.loginfo("meditation = %s", j.meditation)
        rospy.loginfo("attention = %s", j.attention)
        if (j.meditation >= 65 and j.attention < 65):
            rospy.loginfo("right")
            j.tm(600, 200, 300)
        elif (j.meditation < 65 and j.attention >= 65):
            rospy.loginfo("left")
            j.tm(200, 600, 300)
        else:
            rospy.loginfo("stop")
            j.tm(0, 0, 300)

        rate.sleep()
