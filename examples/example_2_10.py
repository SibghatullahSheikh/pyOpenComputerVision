"""
Example 2-10. A complete program to read in a color video and write out the same
video in grayscale
"""
from py_ocv import FileCapture, VideoWriter, NewImage, log_polar


capture = FileCapture("../data/test.mpg")

# Init the video read
in_frame = capture.query_frame()
fps, size = capture.get_fps(), capture.get_size()
center = (size[0]/2, size[1]/2)
out_frame = NewImage(size)

# NOTE: This is not working for me (Ubuntu 11.10)
writer = VideoWriter("../data/test_output.mpg", VideoWriter.MOTION_JPG, fps, size)

while True:
    in_frame = capture.query_frame()
    if not in_frame: break
    log_polar(in_frame, out_frame, center)
    writer.write_frame(out_frame)
