"""
Example 2-3. Program to add a trackbar slider to the basic viewer window: when
the slider is moved, the function onTrackbarSlide() is called and then passed
to the slider's new value
"""
from py_ocv import Window, FileCapture, play_loop

w = Window("Video")
capture = FileCapture("../data/test.mpg")

# NOTE: Video playback under linux is still just bad, this may not work
w.create_trackbar("Position", 0, capture.get_frame_count(),
                  lambda pos: capture.set_pos_frames(pos))

play_loop(w, capture)
