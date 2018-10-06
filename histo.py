#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:47:45 2018

@author: ganesh
"""

# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
'''ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
'''
# load the image and show it
image = cv2.imread('frog-2495715__340.png')
cv2.imshow("image", image)
