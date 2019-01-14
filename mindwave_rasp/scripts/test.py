#!/usr/bin/env python

from __future__ import print_function
import time                  
import bluetooth
from mindwavemobile.MindwaveDataPoints import *
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import rospy
from std_msgs.msg import String
from mindwave_ros.msg import MindwaveValues

def main():
    rospy.init_node('mindwave')
    pub = rospy.Publisher('neuro', MindwaveValues, queue_size=100)
    rate = rospy.Rate(100)
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    if (mindwaveDataPointReader.isConnected()):
        while not rospy.is_shutdown():  
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (dataPoint.__class__ is MeditationDataPoint):
                print(dataPoint.__class__)
                print(dataPoint)
                dic = dataPoint.__dict__
                meditation = dic['meditationValue']
                print(meditation)
            if (dataPoint.__class__ is AttentionDataPoint):
                print(dataPoint.__class__)
                print(dataPoint)
                dic = dataPoint.__dict__
                attention = dic['attentionValue']
                print(attention)  
                
                send_values = MindwaveValues()
                send_values.meditation = meditation
                send_values.attention = attention
                pub.publish(send_values)
                rate.sleep()         
    else:
       print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))


if __name__ == '__main__':
    main()

