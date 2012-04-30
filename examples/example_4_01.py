"""
Example 4-1. Toy program for using a mouse to draw boxes on the screen
"""
from py_ocv import MouseListener, FileImage, Window, Rectangle


class BoxDrawer(MouseListener):
    def __init__(self):
        self.box = None
    
    def on_left_button_down(self, x, y, flags, img):
        self.box = Rectangle(x, y, x, y, Rectangle.BLUE)
    
    def on_mouse_move(self, x, y, flags, img):
        if self.box is not None:
            self.box.x1, self.box.y1 = x, y
    
    def on_left_button_up(self, x, y, flags, img):
        self.box.draw(img)
        self.box = None


image = FileImage('../data/test.jpg')
temp = image.clone()

w = Window("Box Example")
bow_drawer = BoxDrawer()
w.set_mouse_listener(bow_drawer, image)

while True:
    image.copy_to(temp)
    if bow_drawer.box is not None:
        bow_drawer.box.draw(temp)
    
    w.show_image(temp)
    
    if w.wait_esc(15): break

