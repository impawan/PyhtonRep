# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:31:48 2019

@author: Pawan
"""

import numpy as np
import cv2

# Create a black image
img = cv2.imread("img.jpg")

#draw line
img = cv2.line(img,(0,0),(50,20),(255,255,0),3)


#Draw circle 
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

#Draw rectangle 
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#put text in the image


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Smaple text',(50,100), font, 4,(255,255,255),2,cv2.LINE_AA)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()  