# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 02:12:55 2018

@author: Oliver
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
cv.imshow('frame',cap)
while(True):
#    ret,frame=cap.read()
#    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destoryAllWindows()