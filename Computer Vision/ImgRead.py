# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:58:52 2019

@author: Pawan
"""

import numpy as np
import cv2 


img = cv2.imread('img.jpg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()  