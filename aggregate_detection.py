#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def sharpen(img):
    """
    Sharpens the input image using convolution and thresholding.

    Parameters:
        img (numpy.ndarray): A NumPy array representing an image in BGR format.

    Returns:
        numpy.ndarray: A thresholded, sharpened, and inverted binary image.
    """
    kernel = np.array([[-1, -1, -1], [-1, 9.3, -1], [-1, -1, -1]])
    img = cv2.filter2D(img, -1, kernel)
    thresh = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lut_in = np.array([0, 93, 140, 255])
    lut_out = np.array([150, 50, 40, 40])
    lut_8u = np.interp(np.arange(0, 256), lut_in, lut_out).astype(np.uint8)

    thresh = cv2.LUT(thresh, lut_8u)
    ret, thresh = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    thresh = cv2.bitwise_not(thresh)
    return thresh

def enhance_image(image):
    """
    Enhances the input image using Contrast Limited Adaptive Histogram Equalization (CLAHE).

    Parameters:
        image (numpy.ndarray): A NumPy array representing an image in BGR format.

    Returns:
        numpy.ndarray: An enhanced version of the input image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    enhanced_image = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    return enhanced_image

def find_blobs(image_path, contour_array, debug=False, blobs_are_black=False):
    """
    Finds blobs (contours) in the input image and stores them in the contour_array.

    Parameters:
        image_path (str): The file path of an image to be processed.
        contour_array (list): A list to store the found contours.
        debug (bool, optional): If True, displays the image with detected contours. Defaults to False.
        blobs_are_black (bool, optional): If True, assumes blobs are black on a white background.
                                          If False, assumes blobs are white on a black background. Defaults to False.
    """
    image = cv2.imread(image_path)
    if blobs_are_black == False:
        image = cv2.bitwise_not(image)
    enhanced_image = enhance_image(image)
    kernel = np.ones((2, 2), np.uint8)
    ed = cv2.erode(enhanced_image, kernel, iterations=1)
    thresh = sharpen(ed)

    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    cnts = [cnts[i] for i in range(len(cnts)) if hierarchy[0][i][2] == -1]
    for c in cnts:
        area = cv2.contourArea(c)
        cv2.drawContours(enhanced_image, [c], -1, (0, 0, 255), cv2.FILLED)
        contour_array.append(c)

    if debug:
        plt.imshow(enhanced_image, cmap="binary")
        plt.title(f'Detected Contours with Cell Count: {len(contour_array)}')
        plt.show()

