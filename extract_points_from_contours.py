#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def extract_points_from_contours(contour_list):
    """
    Extracts x and y coordinates from a list of contours.

    Parameters:
        contour_list (list): A list of contours, where each contour is represented as a list of points.

    Returns:
        list: A list of tuples containing (x, y) coordinates of each point in the input contours.
    """
    points_list = []
    for contour in contour_list:
        for point in contour:
            x, y = point[0]
            points_list.append((x, y))
    return points_list

