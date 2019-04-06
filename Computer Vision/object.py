# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:04:09 2019

@author: Pawan
"""

"""

OpenCV usually captures images and videos in 8-bit, unsigned integer, BGR format. 
In other words, captured images can be considered as 3 matrices, BLUE,RED and GREEN with integer values ranges from 0 to 255.

[113  58  53]
[102  90  51]
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower_blue = np.array([98,80,50])
    upper_blue = np.array([115,120,80])

    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv',hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()