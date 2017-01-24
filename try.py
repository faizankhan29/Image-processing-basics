import cv2
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join

img=cv2.imread('10.1.1.1.2004_4.tif',cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(img, (5, 5), 0)

#blurred  = cv2.bilateralFilter(gray,9,75,75)

# apply Canny Edge Detection
edged = cv2.Canny(blurred, 0, 20)

#Find external contour

(_,contours, _) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('image',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()


mypath='Math Dataset/Dataset/image'
'''onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
cv2.imshow('image',images[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
