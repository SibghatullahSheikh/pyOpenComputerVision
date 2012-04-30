"""
Example 3-12. Using ImageROI to increment all of the pixels in a region

The Region Of Interest (ROI) contains an xOffset, a yOffset, a height, a width,
and Channel Of Interest (COI). Once the ROI is set, functions that would
normally operate on the entire image will instead act only on the subset of the
image indicated by the ROI.
"""
from py_ocv import FileImage, show_image

image = FileImage("../data/test.jpg")
image.set_roi((270, 110, 120, 120))
image.add_value(50)
image.reset_roi()

show_image(image)