#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import google_speech_recognition as sr
import RobotTasks as Tasks


def speech_talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('speecher', anonymous=True)

    rate = rospy.Rate(100) # 100hz: go through the loop 100 times per second
    while not rospy.is_shutdown():
        # speech recognition
        original_recognition = sr.speech()

        # extract useful information(commands) from speech
        task_str = extract_task(original_recognition) 

        if task_str != "":
            print("Command: " + task_str)
            rospy.loginfo(task_str)
            pub.publish(task_str)
        else:
            print("There is no any command from what you said!")

        rate.sleep()


def extract_task(original_recognition):
    # Convert the speech into lowercase
    speech = original_recognition.lower()

    # To check if the speech contains robot task
    for token in speech.split():
        if token in RobotTasks.robot_tasks_list:
            return token
    
    return ""


if __name__ == '__main__':
    try:
        speech_talker()
    except rospy.ROSInterruptException:
        pass



