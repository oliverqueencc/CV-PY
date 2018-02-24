# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:37:56 2018

@author: Oliver
"""
"""
import numpy as np
import cv2 as cv

img = cv.imread('2.jpg',0)
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()"""
import numpy as np
import cv2 as cv
img = cv.imread('2.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()