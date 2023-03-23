import rospy
import numpy as np
import cv2
import math
from sensor_msgs.msg import Image
from robot_vision_lectures.msg import XYZarray
from robot_vision_lectures.msg import SphereParams

msg_received = False

def get_points(XYZpoints):
	global ros_points
	global msg_received
	ros_points = []
	XYZcords = []
	#loop through and recieve all the points
	for i in XYZpoints.points:
		XYZcords = [i.x, i.y, i.z]
		ros_points.append(XYZcords)
	msg_received = True
	
	#print(ros_points[0])
	
	#maybe move into one function?
def getRaidus(ros_points):
	B = []
	A = []
	for p in ros_points:
		B.append(math.pow(p[0], 2) + math.pow(p[1], 2) + math.pow(p[2], 2))
		A.append([2*p[0], 2*p[1], 2*p[2], 1])
	print(B)
	print(A)
			

if __name__ == '__main__':
	#define node, subscribers, and publishers
	rospy.init_node('sphere_fit', anonymous = True)
	#define a subscriber to recieve the points
	xyz_sub = rospy.Subscriber("/xyz_cropped_ball", XYZarray, get_points) 
	#get points
	#define a publisher to publish images to /sphere_params task and therefore set the radius
	xyz_pub = rospy.Publisher('/sphere_params', SphereParams, queue_size = 1)
	#need to publish to xc, yx, zc, radius - must be calculated first
	# set the loop frequency
	rate = rospy.Rate(10)
	

	while not rospy.is_shutdown():
		# make sure we process if the camera has started streaming images
		if msg_received:
			# publish the 
			img_pub.publish(img_msg)
		# pause until the next iteration			
		rate.sleep()
