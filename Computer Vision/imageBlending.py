# -*- coding: utf-8 -*-
"""
@author: Pawan
"""


import cv2
import numpy as np
img1 = cv2.imread('img.jpg')
img1 = img1[100:300,100:300]
cv2.imshow('img1',img1)
img2 = cv2.imread('img2.jpg')

img2 = img2[100:300,100:300]

cv2.imshow('img2',img2)

res = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
