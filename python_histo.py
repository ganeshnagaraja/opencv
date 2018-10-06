# draw histogram in python

'''
Code to produce rgb histogram of an image
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gorilla-1893013__340.png')
h = np.zeros((300,256,3))

bins = np.arange(255).reshape(255,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]

for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[255],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)

h=np.flipud(h)
'''
color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[255],[0,255])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
'''
cv2.imshow('colorhist',h)
cv2.waitKey(25000)  # time the image is displayed on screen
