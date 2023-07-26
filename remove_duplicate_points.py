#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove_duplicate_points(contours):
    """
    Removes duplicate points from the given list of contours.

    Parameters:
        contours (list): A list of contours, where each contour is represented as a list of points.

    Returns:
        list: A list of cleaned contours, where duplicate points within each contour have been removed.
    """
    cleaned_contours = []

    for contour in contours:
        unique_points_set = set()
        cleaned_contour = []

        for point in contour:
            point_tuple = tuple(point[0])  # Convert point array to a tuple for set comparison
            if point_tuple not in unique_points_set:
                unique_points_set.add(point_tuple)
                cleaned_contour.append(point)

        cleaned_contours.append(cleaned_contour)

    return cleaned_contours

