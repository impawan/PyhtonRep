# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:03:46 2019

@author: Pawan
"""
import cv2
import numpy as np
img = cv2.imread('img.jpg',0)
y,x = img.shape

M = cv2.getRotationMatrix2D((x/2,y/2),90,1) #return matrix
res = cv2.warpAffine(img,M,(x,y))

cv2.imshow('original',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

