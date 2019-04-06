# -*- coding: utf-8 -*-
"""

@author: Pawan
"""

import cv2
import numpy as np

img = cv2.imread('img.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
res = cv2.warpAffine(img,M,(cols,rows))


cv2.imshow('original',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()