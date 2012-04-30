"""
Example 3-14. Complete program to alpha blend the ROI starting at (0,0) in src2
with the ROI starting at (x,y) in src1
"""
from py_ocv import FileImage, show_image

src1 = FileImage("../data/test.jpg")
src2 = src1.clone()

X, Y = 270, 110
W, H =  120, 120
alpha, beta = 0.5, 0.5

src1.set_roi((X   , Y, W, H))
src2.set_roi((X+20, Y, W, H))

src1.add_weighted(alpha, beta, src2)
src1.reset_roi()

show_image(src1)
