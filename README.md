Assignment 2 2023
================================

Description of the assignment
-----------------------------
The aim of this second assignment is to develop a mobile robot simulator in ROS. The robot has to be able to move in the desired position which is the input insert by the user with the keyboard.
The robot is situated in a 3D simulation environment called "Gazebo". To do this, it is requested to crete a new package, in which three different nodes are implemented:

*(a) A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. Try to use the feedback/status of the action server to k now then the target has been reached. The node also publishes the robot position and velocity as a custom message (x,v,vel_x,vel_z), by relying on the values published on the topic/odom.

*(b) A service node that, when called, returns the coordinates of the last target sent by the user.

*(c) Another service node that subscribes to the robot's position and velocity (using the custom message) and implements a server to retrieve the distance of the robot from the target the target and the robot's average speed.

-Create a launch file to start the whole simulation. Use a parameter to select the size of the averaging window of node (c).

Installing and running
----------------------

In order to run the simulation, it is necessary to clone the assignment folder in the 'src' folder of the 'ROS' workspace using the command:

	git clone https://github.com/ilacolo/assignment_2_2023.git


It is also necessary to update the 'ROS' space running the following command in the 'ROS' workspace:

	catkin_make
	
In order to run the the whole program, use the following command in the terminal:

	roslaunch assingment_2_2023 assignment1.launch
	
Implementation
---------------

To complete the task, the three requested nodes has implemented in the following way:

* 'action_client.py' is node A
* 'service_node.py' is the node B
* 'rob_pos_vel' is the node C

The launch file is completed with the three nodes in order to run at the same time. 

## 'action_client' node (a)

In order to explain in the best way how this node works, the pseudocode of the code is reported in the next part. In this node three functions are implemented in order to optimize the code. The function 'pos_and_vel(msg)' publishes the position and the velocity of the robot. The function 'target() ask to the user to insert the input which is the target position of the robot. Then the robot reaches the robot reaches the the target position. then, the function 'main()' is implemented in order to be called at the end.

## Pseudocode of the node A

Import all the necessary library

Define a global publisher pub

function 'pos_and_vel(msg)':

	Get position and velocity from msg
    	Create a custom message info_pos_vel
    	Assign parameters of of the costume message 
    	Publish the costume message info_pos_vel using pub

function 'target()':

	Sleep for 3 seconds to let the terminator works better
	Prompt user to insert desired x and y positions
   	Read user input for x and y
	Create a goal message with the specified x and y positions
	Create an action client with the server name '/reaching_goal'
	Wait for the server to be ready	
        Send the goal using the action client
        Wait for the server to be ready
	Prompt user to input 'd' to delete the target position or any other key to send the goal
    	Read user input for delete_value

    	If delete_value is 'd':
        	Cancel the goal using the action client
        	Print "The goal is deleted"
    	Else:
        	Send the goal using the action client
        	Print "The target position is always the same" and "Target sent to the server"

	
function 'main()':

	Initialize ROS node 'action_client'
    	Define publisher pub
    	Define subscriber sub
	Initialize the publisher to publish to "/pos_vel" topic
    	Initialize the subscriber to subscribe to "/Odom" topic and callback to pos_and_vel

Call `main()` function to start the program

## 'service_node' node (b)
In this node, two functions are implemented. The first one is the function 'results(msg): it returns the value of the goal position.

## 'rob_pos_vel' node (c)
In this node, two functions are implemented. The first one is the function 'pos_vel_dist(msg): it contains the subscriber information. It also compute the distance between the robot and the goal position and also the velocity of the robot. The distance and the velocity are computed if the time is passed from the last time. Then the time is updated. The second function is the 'main() which is called at the end.

## launch file

A small part of the code is added to the launch file, in order to start the whole simulation. In the launch file the following code is added:

    <node pkg="assignment_2_2023" type="action_client.py" name="action_client" output="screen" />
    <node pkg="assignment_2_2023" type="service_node.py" name="service_node" output="screen" />
    <node pkg="assignment_2_2023" type="rob_pos_vel.py" name="rob_pos_vel" output="screen" />

## Possible improvements for the code
In order to improve the code, it is possible to add some small details:

*Add a check when the user digits the input: sometimes may happen that the target position is not inside the borders of the arena or it is in on the wall obstacles. To do this it is necessary to know the dimensions of the arena where the robot is moving and the position of the obstacles.

*It may be possible to mark the target position in the arena, in order to know where the robot is going and where is located the goal position oin the arena because at the moment it is not possible to know where the robot is moving on.
