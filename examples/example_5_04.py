"""
Example 5-4. Threshold versus adaptive threshold
"""
from py_ocv import FileImage, Image, Window

# Read in gray image
image = FileImage("../data/test.jpg", Image.LOAD_IMAGE_GRAYSCALE)
image_t = image.clone()
image_at = image.clone()

# Threshold
image_t.threshold(50, 255, Image.THRESH_BINARY)
image_at.adaptive_threshold(255, Image.ADAPTIVE_THRESH_MEAN_C,
                            Image.THRESH_BINARY_INV, 71, 15)

w = Window("Raw")
w.show_image(image)

w_t = Window("Threshold")
w_t.show_image(image_t)

w_at = Window("Adaptive Threshold")
w_at.show_image(image_at)

Window.wait_key(0)