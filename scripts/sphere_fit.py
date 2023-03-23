import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from robot_vision_lectures.msg import XYZarray
from robot_vision_lectures.msg import SphereParams

msg_received = False

def get_points(XYZpoints):
	global ros_points
	global msg_received
	#loop through and recieve all the points
	for i in XYZpoints.points:
		ros_msg.append(i)
	msg_received = True
	
def estimate():
	


if __name__ == '__main__':
	#define node, subscribers, and publishers
	rospy.init_node('sphere_fit', anonymous = True)
	#define a subscriber to ream images
	xyz_sub = rospy.Subscriber("/xyz_cropped_ball", XYZarray, get_points) 
	#define a publisher to publish images to /ball_2D task
	xyz_pub = rospy.Publisher('/sphere_params', SphereParams, queue_size = 1)
	
	# set the loop frequency
	rate = rospy.Rate(10)
	

	while not rospy.is_shutdown():
		# make sure we process if the camera has started streaming images
		if img_received:
			# publish the 
			img_pub.publish(img_msg)
		# pause until the next iteration			
		rate.sleep()
