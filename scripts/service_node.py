#! /usr/bin/env python3

import rospy
import assignment_2_2023.msg
from assignment_2_2023.srv import GetLastTarget, GetLastTargetResponse
import actionlib
import actionlib.msg


#initialize variable to count how many goals are reached and how many goals are deleted
goal_deleted = 0
goal_reached = 0

def results(msg):
	"""
	This function returns the reached position
	"""
	
	global last_target_coordinates
	
	response = GetLastTargetResponse()
	response.coordinates = last_target_coordinates
	
	return response
	print(response)

def target_callback(msg):

	global last_target_coordinates
	last_target_coordinates = msg.data
	
def main():
	"""
	The main function to be called at the end.

	Args: None
	"""

	#initialize the node
	rospy.init_node('service_node')
	
	#define the subscriber: it gets from "Odom" the position and the velocity
	sub_result = rospy.Subscriber('/reaching_goal/result', assignment_2_2023.msg.PlanningActionResult, target_callback)
	
	#keep the node running
	rospy.spin()
	

if __name__ == '__main__':
	main()
	
	

