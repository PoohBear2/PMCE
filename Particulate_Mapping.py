#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def create_blank_frame_with_contours(all_contours, frame_height, frame_width, output_directory, output_filename="blank_frame.png"):
    """
    Creates a blank frame with all contours drawn on it and saves it to the specified output directory.

    Parameters:
        all_contours (list): A list of contours to be drawn on the blank frame.
        frame_height (int): Height of the blank frame in pixels.
        frame_width (int): Width of the blank frame in pixels.
        output_directory (str): The directory path to save the blank frame.
        output_filename (str, optional): The filename to save the blank frame. Defaults to "blank_frame.png".
    """
    # Create the blank frame and draw all contours on it
    blank_frame = np.full((frame_height, frame_width, 3), 255, dtype=np.uint8)
    for contour in all_contours:
        cv2.drawContours(blank_frame, [contour], -1, (0, 0, 255), cv2.FILLED)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Save the blank_frame with everything drawn on it
    output_path = os.path.join(output_directory, output_filename)
    cv2.imwrite(output_path, blank_frame)

    # Display the image (optional)
    plt.imshow(blank_frame)
    plt.title("Particulate Mapping")
    plt.axis("on")
    plt.show()

