"""
Example 2-1. A simple OpenCV program that loads an image from disk and displays
it on the screen
"""
from py_ocv import FileImage, show_image

show_image(FileImage("../data/test.jpg"))