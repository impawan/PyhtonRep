# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:11:21 2019

@author: Pawan
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img.jpg')

kernel = np.ones((7,7),np.float32)/149 #kernal matrix of 3*3 and sum is divide by 9 It  takes the average 
#of all the pixels under kernel area and replaces the central element with this average
res = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(7,7))

cv2.imshow('original',img)
cv2.imshow('res',res)
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
