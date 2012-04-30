"""
Example 2-7. Combining the pyramid down operator (twice) and the Canny
subroutine in a simple image pipeline
"""
from py_ocv import FileImage, show_image

image = FileImage("../data/test.jpg")
image.pyr_down()
image.pyr_down()
image.canny(100, 200, 3)

show_image(image)