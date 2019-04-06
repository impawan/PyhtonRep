# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:34:52 2019

@author: Pawan
"""

import cv2
import numpy as np


font = cv2.FONT_HERSHEY_SIMPLEX

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img,'Smaple text',(x,y), font, 4,(255,0,0),2,cv2.LINE_AA)


img = cv2.imread('img.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()