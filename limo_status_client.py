 #!/usr/bin/env python
 
 
import rospy
from limo_status_translator import *
 
def callback(data):
	rospy.loginfo(%s ,data.data) 


def Get_Limo_Status_client():
	rospy.init_node('limo_stats_client_node', anonymous = False)
	sub = rospy.Subscriber('Translator_Stats', String, callback)
	pub = rospy.Publisher('Received_Stats', String, queue_size = 5)	 	
	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		for get_stats in range(0,5)		
		if get_stats = 0 : request_str = "0"
		pub.publish(request_str)
		rospy.loginfo("Status " + request_str)
		rate.sleep()
		if get_stats = 1 : request_str = "1"
		pub.publish(request_str)
		rospy.loginfo("Status " + request_str)
		rate.sleep()
		if get_stats = 2 : request_str = "2"
		pub.publish(request_str)
		rate.sleep()
		rospy.loginfo("Status " + request_str)
		if get_stats = 3 : request_str = "3"
		pub.publish(request_str)
		rate.sleep()
		rospy.loginfo("Status " + request_str)
		if get_stats = 4 : request_str = "4"
		pub.publish(request_str)
		rate.sleep()
		rospy.loginfo("Status " + request_str)
if __name__ == "__main__":
	Get_Limo_Status_client()
