# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:08:29 2019

@author: Pawan
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('farme',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
print(cap.isOpened())       
cap.release()
print(cap.isOpened())
cv2.destroyAllWindows()        