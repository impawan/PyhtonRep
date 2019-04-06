# -*- coding: utf-8 -*-
"""
@author: Pawan
"""

"""
Adaptive thresholding is the method where the threshold value is calculated for smaller regions and therefore, there will be different threshold values for different regions.
"""

import cv2
import numpy as np



img = cv2.imread('img.jpg',0)
_,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thresh2 =  cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,2)
cv2.imshow('img',img)
cv2.imshow('thresh1',thresh1)
cv2.imshow('thresh2',thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()