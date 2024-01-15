#! /usr/bin/env python3

import rospy
import time
import math
import assignment_2_2023.msg
from assignment_2_2023.msg import pos_vel_info

#select the frequency (frequency) and the last time printed (old) information
frequency = 1.0
old = 0

def pos_vel_dist(msg):
	"""
	Function which compute the distance between
	the robot and the goal and also the velocity of the robot.
	
	Arg: msg(RobotMsg): it contains the coordinates of velocity of the robot

	"""
	
	global frequency
	global old_time
	
	#compute period [ms], and the time [ms]
	period = (1.0/freq) * 100
	now_time = time.time() * 1000
	
	#if the time which is passed from the last time the function
	#can compute and print the distance and the velocity of the robot
	if now_time - old_time > period:
		des_x = rospy.get_param("des_pos_x")
		des_y = rospy.get_param("des_pos_y")
		dist = math.sqrt(pow(des_x - msg.x, 2) + pow(des_y - msg.y, 2))
		print("the goal distance is: ")
		print(dist)
		speed = math.sqrt(pow(msg.vel_x, 2) + (msgh.vel_y, 2))
		print("the average speed is: ")
		print(speed)
		
		#update time
		old_time = now_time
	
def main():
	"""
	The main function to be called at the end.

	Args: None
	"""

	global frequency
	
	#initilize the node
	rospy.init_node('rob_vel_pos')
		
	#define the subscriber:
	sub_res = rospy.Subscriber('/pos_vel', pos_vel_info , pos_vel_dist)
	
	#keep the node running
	rospy.spin()
	
if __name__ == "__main__":
	main()
	
