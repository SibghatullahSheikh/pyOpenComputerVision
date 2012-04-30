"""
Example 2-4. Loading and then smoothing an image before it is displayed on the
screen
"""
from py_ocv import FileImage, show_image

image = FileImage("../data/test.jpg")
image.smooth()

show_image(image)