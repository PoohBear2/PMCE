#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def extract_points_by_y_value(points_list):
    """
    Extracts points based on unique y-values and returns them as a dictionary.

    Parameters:
        points_list (list): A list of tuples containing (x, y) coordinates of points.

    Returns:
        dict: A dictionary where each key is a unique y-value and the corresponding value is a list of points
              with that y-value, sorted based on their x-coordinate.
    """
    unique_y_values = set()

    for x, y in points_list:
        unique_y_values.add(y)

    unique_y_values_list = list(unique_y_values)
    y_value_points = {}

    for y_value in unique_y_values_list:
        points_with_y_value = [point for point in points_list if point[1] == y_value]
        sorted_points = sorted(points_with_y_value, key=lambda p: p[0])
        y_value_points[y_value] = sorted_points

    return y_value_points

