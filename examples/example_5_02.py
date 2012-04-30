"""
Example 5-2. Example code making use of cvThreshold()
"""
from py_ocv import NewImage, FileImage, show_image


def sum_rgb(src):
    r, g, b = src.rgb_split()
    
    # Sum (r,g,b) into s
    s = NewImage(src.get_size(), channels=1)
    r.add_weighted(1./3., 1./3., g, s)
    s.add_weighted(2./3., 1./3., b)
    
    s.threshold(100, 100)
    return s

show_image(sum_rgb(FileImage("../data/test.jpg")))