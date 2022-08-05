#!/usr/bin/env python


import rospy

from std_msgs.msg import String as StringMsg
from limo_status_translator import *

Cdata = None

def Callback_Cli(data):
	global Cdata
	Cdata = data.data
	rospy.loginfo(Cdata)

def Callback_Limo(data):
	rospy.loginfo(data.data)

def stats():
	rospy.init_node('limo_stats_translator_node',anonymous = False)
	limo_sub = rospy.Subscriber('limo_status', StringMsg, Callback_Limo)
	cli_sub = rospy.Subscriber('Received_Stats', String, Callback_Cli)
	cli_pub = rospy.Publisher('Translator_Stats', String, queue_size = 5)
	rate = rospy.Rate(2)
	rtn = "Nothing"
	
	while not rospy.is_shutdown():
		rospy.wait_for_service('GetLimoStatus')
		info = rospy.ServiceProxy('GetLimoStatus', LimoStatus)
		if Cdata == "0" : rtn = "STATUS 0"
		cli_pub.publish(rtn)
		rate.sleep()
		rospy.loginfo(rtn + " sent")
		if Cdata == "1" : rtn = "STATUS 1"
		cli_pub.publish(rtn)
		rate.sleep()
		rospy.loginfo(rtn + " sent")
		if Cdata == "2" : rtn = "STATUS 2"
		cli_pub.publish(rtn)
		rate.sleep()
		rospy.loginfo(rtn + " sent")
		if Cdata == "3" : rtn = "STATUS 3"
		cli_pub.publish(rtn)
		rate.sleep()
		rospy.loginfo(rtn + " sent")
		if Cdata == "4" : rtn = "STATUS 4"
		cli_pub.publish(rtn)
		rate.sleep()
		rospy.loginfo(rtn + " sent")

if __name__ == "__main__":
	try:
		stats()
	except rospy.ROSInterruptException:
		pass
