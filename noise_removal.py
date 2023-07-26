#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def noise_removal(image_path):
    """
    Detects contours in a given image and returns the contour frame and a list of contours.

    Parameters:
        image_path (str): The file path of the input image.

    Returns:
        tuple: A tuple containing the contour frame (numpy array) and a list of contours.
    """
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    contour_frame = np.zeros_like(image)
    cv2.drawContours(contour_frame, contours, -1, (0, 0, 255), 2)

    return contour_frame, contours

