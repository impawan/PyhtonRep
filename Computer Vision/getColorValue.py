# -*- coding: utf-8 -*-
"""
@author: Pawan
"""


import cv2
import numpy


cap = cv2.cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    y,x,c = frame.shape
    #print(y,x)
    mid_y = int(y/2)
    mid_x = int(x/2)
    #print(mid_y-10,mid_x-10)
    temp =  frame[mid_y, mid_x]
    #print(temp)
    frame = cv2.rectangle(frame,(mid_x-10,mid_y-10),(mid_x+10,mid_y+10),(0,255,0),1)
    #frame[mid_y,mid_x] = [0,0,255]
    print(frame[mid_y,mid_x])
    cv2.imshow('video',frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.waitKey(0)
cv2.destroyAllWindows()  