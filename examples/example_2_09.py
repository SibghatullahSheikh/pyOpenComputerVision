"""
Example 2-9. After the capture structure is initialized, it no longer matters
whether the image is from a camera or a file
"""
from py_ocv import Window, CameraCapture, play_loop


play_loop(Window("Video"), CameraCapture())
