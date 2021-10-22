# FRF21_lab1

Create a ROS workspace 

``source /opt/ros/setup.bash``

Create the workspace:

``mkdir p ~/catkin_ws src`

``cd ~/catkin_ws/``

``catkin_make``

Create a new package:

`` cd ~/catkin_ws src``

``catkin_create_pkg beginner_tutorials std_msgs rospy roscpp``

Build the workspace

``cd ~/catkin_ws``

``catkin_make``

Add in the .bashrc file:

``source ~/catkin_ws devel setup.bash`` 

Navigate to SRC folder: 

``cd ~/catkin_ws/src`` 

Clone the repository content: 

``git clone https://github.com/Albertdemian/FRF21_lab1.git .``
