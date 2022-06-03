#!/usr/bin/env python
import rospy
import time
import random
from std_srvs.srv import Empty as EmptyServiceCall
from std_srvs.srv import Empty
from turtlesim.srv import Spawn
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import SetPen
rospy.wait_for_service('turtle1/teleport_absolute')
turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
input = 1
turtle1_teleport1 = [[1, 1,0],
 		    [10,1,0],
		    [10,2,0 ], 
	            [1, 2, 0],
	            [1, 3, 0],
		    [10,3,0 ],
	            [10,4,0],
                    [1,4,0 ],
                    [1,5,0],
                    [10,5,0],
                    [10,6,0], 
                    [1, 6,0 ],
                    [1, 7, 0],
                    [10,7 , 0],
                    [10,8 ,0 ],
                    [1, 8,0 ],
                    [1,9 ,0 ],
                    [10, 9,0 ],
                    [10,10,0],
                    [1,10,0]]
                    

s = turtle1_teleport1[::-1]                   
#turtle1_teleport1 = []
def do_the_zigzag_forward():
  for i in turtle1_teleport1:
   if type(i)== list:
    if i== ([1,1,0]):         
      turtle1_teleport(i[0],i[1],i[2])
      time.sleep(0.5)
      rospy.wait_for_service('clear')
      clear_background = rospy.ServiceProxy('clear', EmptyServiceCall)
      clear_background()
    else:
      turtle1_teleport(i[0],i[1],i[2])
      time.sleep(0.5)
def do_the_zigzag_backward():
  for i in s:
   if type(i)== list:
    if i== ([1,10,0]):         
      turtle1_teleport(i[0],i[1],i[2])
      time.sleep(0.5)
      rospy.wait_for_service('clear')
      clear_background = rospy.ServiceProxy('clear', EmptyServiceCall)
      clear_background()
    else:
      turtle1_teleport(i[0],i[1],i[2])
      time.sleep(0.5)
  
  
if __name__ == '__main__':
    try:
        while (input !=0):
         do_the_zigzag_forward()
         do_the_zigzag_backward()
    except rospy.ROSInterruptException:
        pass  
       
          
 
  
