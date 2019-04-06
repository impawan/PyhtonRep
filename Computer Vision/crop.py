# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:39:43 2019

@author: Pawan
"""

import cv2
import numpy as np

image = cv2.imread("img.jpg")

cropped = image[100:500, 100:600]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows() 