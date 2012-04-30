"""
Example 6-1. Using cvHoughCircles to return a sequence of circles found in a
grayscale image
"""
from py_ocv import FileImage, Image, show_image

image = FileImage("../data/coins.jpg", Image.LOAD_IMAGE_GRAYSCALE)
image.smooth(Image.GAUSSIAN, 7, 7)

for circle in image.hough_circles():
    circle.draw(image)

show_image(image)