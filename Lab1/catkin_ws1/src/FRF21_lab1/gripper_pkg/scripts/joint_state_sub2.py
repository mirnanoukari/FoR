#!/usr/bin/env python
import rospy

from std_msgs.msg import Float32
from sensor_msgs.msg import JointState



def callback(data):

    global angles
    angles = data
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    angle_pub = rospy.Publisher("formated_positions",Float32 )
    
    global angles
    angles = JointState()

    g1 = Float32()
    
    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        print(angles)
        g1.data = angles.position

        angle_pub.publish(g1)


   

if __name__ == '__main__':
    listener()



        
       


