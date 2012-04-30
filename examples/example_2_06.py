"""
Example 2-6. The Canny edge detector writes its output to a single channel (grayscale) image
"""
from py_ocv import FileImage, show_image

image = FileImage("../data/test.jpg")
image.canny(100, 200, 3)

show_image(image)