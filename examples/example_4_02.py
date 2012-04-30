"""
Example 4-2. Using a trackbar to create a "switch" that the user can turn on
and off
"""
from py_ocv import Window

def switch_callback(on):
    if on:
        print 'on'
    else:
        print 'off'

w = Window("Demo")
w.create_trackbar("Switch", 0, 1, switch_callback)
w.wait_key()
