#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def overlay_contours_on_image(base_image_path, contour_image_path):
    """
    Overlays the detected contours on the base image and displays the result using matplotlib.

    Parameters:
        base_image_path (str): The file path of the base image.
        contour_image_path (str): The file path of the image with detected contours.

    Returns:
        None
    """
    contour_frame, _ = noise_removal(contour_image_path)
    base_image = cv2.imread(base_image_path)
    contour_frame_rgb = cv2.cvtColor(contour_frame, cv2.COLOR_BGR2RGB)
    base_image_rgb = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)

    combined_image = cv2.addWeighted(base_image_rgb, 1, contour_frame_rgb, 1, 0)
    plt.imshow(combined_image)
    plt.title("Boundary Detection Overlay")
    plt.axis("on")  # Hide axis ticks and labels
    plt.show()

