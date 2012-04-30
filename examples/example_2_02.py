"""
Example 2-2. A simple OpenCV program for playing a video file from disk
"""
from py_ocv import Window, FileCapture, play_loop

play_loop(Window("Video"), FileCapture("../data/test.mpg"))