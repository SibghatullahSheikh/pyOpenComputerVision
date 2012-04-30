"""
Example 2-5. Using PyrDown to create a new image that is half the width and
height of the input image
"""
from py_ocv import FileImage, show_image

image = FileImage("../data/test.jpg")
image.pyr_down()

show_image(image)