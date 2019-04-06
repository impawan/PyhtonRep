# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:36:23 2019

@author: Pawan
"""


import cv2
import numpy as np

image = cv2.imread('img.jpg')

print(image.shape[1])

r = 200.0 / image.shape[1]
dim = (200, int(image.shape[0] * r))
 
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()