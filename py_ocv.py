import cv

###############################################################################
# Window
###############################################################################
class Window:
    ESC_KEY = 27
    
    def __init__(self, name):
        self.name = name
        cv.NamedWindow(name, cv.CV_WINDOW_AUTOSIZE)
    
    def show_image(self, image):
        cv.ShowImage(self.name, image.img)
    
    def create_trackbar(self, name, start, end, callback):
        cv.CreateTrackbar(name, self.name, start, end, callback)
    
    def set_mouse_listener(self, mouse_listener, data):
        cv.SetMouseCallback(self.name, mouse_listener.listen, data)
    
    @staticmethod
    def wait_key(ms=0):
        return cv.WaitKey(ms)
    
    @staticmethod
    def wait_esc(ms=0):
        key = Window.wait_key(ms)
        return key == Window.ESC_KEY
    
    def __del__(self):
        cv.DestroyWindow(self.name)


class MouseListener:
    def on_mouse_move(self, x, y, flags, data): pass
    def on_left_button_down(self, x, y, flags, data): pass
    def on_left_button_up(self, x, y, flags, data): pass
    
    def listen(self, event, x, y, flags, data):
        if event == cv.CV_EVENT_MOUSEMOVE:
            self.on_mouse_move(x, y, flags, data)
        
        elif event == cv.CV_EVENT_LBUTTONDOWN:
            self.on_left_button_down(x, y, flags, data)
        
        elif event == cv.CV_EVENT_LBUTTONUP:
            self.on_left_button_up(x, y, flags, data)

def show_image(image, title="Image"):
    w = Window(title)
    w.show_image(image)
    w.wait_key()

###############################################################################
# Image
###############################################################################
class Image:
    LOAD_IMAGE_GRAYSCALE = cv.CV_LOAD_IMAGE_GRAYSCALE
    
    GAUSSIAN = cv.CV_GAUSSIAN
    
    HOUGH_GRADIENT = cv.CV_HOUGH_GRADIENT
    
    THRESH_BINARY = cv.CV_THRESH_BINARY
    THRESH_BINARY_INV = cv.CV_THRESH_BINARY_INV
    
    ADAPTIVE_THRESH_MEAN_C = cv.CV_ADAPTIVE_THRESH_MEAN_C
    ADAPTIVE_THRESH_GAUSSIAN_C = cv.CV_ADAPTIVE_THRESH_GAUSSIAN_C
    
    def __init__(self, img):
        self.img = img
    
    def __nonzero__(self):
        return bool(self.img)
    
    def clone(self):
        return Image(cv.CloneImage(self.img))
    
    def zero(self):
        cv.Zero(self.img)
    
    def set_roi(self, rectangle):
        cv.SetImageROI(self.img, rectangle)
    
    def reset_roi(self):
        cv.ResetImageROI(self.img)
    
    def copy_to(self, dest):
        cv.Copy(self.img, dest.img)
    
    def add_value(self, value):
        cv.AddS(self.img, value, self.img)
    
    def acc(self, img):
        cv.Acc(img.img, self.img)
    
    def add_weighted(self, alpha, beta, beta_src, target=None, gamma=0.0):
        if target is None: target = self
        cv.AddWeighted(self.img, alpha, beta_src.img, beta, gamma, target.img)
    
    def rgb_split(self):
        size = self.get_size()
        r, g, b = NewImage(size, channels=1), NewImage(size, channels=1), NewImage(size, channels=1)
        # Split image onto the color planes.
        cv.Split(self.img, r.img, g.img, b.img, None)
        return r, g, b
    
    def get_size(self):
        return cv.GetSize(self.img)
    
    def get_height(self):
        return self.img.height
    
    def get_width(self):
        return self.img.width
    
    def get_depth(self):
        return self.img.depth
    
    def get_n_channels(self):
        return self.img.nChannels
    
    def smooth(self, smooth_type=cv.CV_GAUSSIAN, param1=3, param2=3, param3=0, param4=0):
        cv.Smooth(self.img, self.img, smooth_type, param1, param2, param3, param4)
    
    def pyr_down(self):
        width, height = self.get_size()
        if not ((width % 2 == 0) and (height % 2 == 0)):
            raise Exception("The image is not divisible by two")
        img = cv.CreateImage((width/2, height/2), self.get_depth(), self.get_n_channels())
        cv.PyrDown(self.img, img)
        self.img = img
    
    def canny(self, lowThresh, highThresh, aperture):
        # canny only handles grayscale images. So convert RGB to grayscale
        if self.get_n_channels() != 1:
            img = cv.CreateImage(self.get_size(), self.get_depth(), 1)
            cv.CvtColor(self.img, img, cv.CV_RGB2GRAY)
            self.img = img
        
        cv.Canny(self.img, self.img, lowThresh, highThresh, aperture)
    
    def threshold(self, threshold, max_value, threshold_type=cv.CV_THRESH_TRUNC):
        cv.Threshold(self.img, self.img, threshold, max_value, threshold_type)
    
    def adaptive_threshold(self, max_value, adaptive_method, threshold_type, block_size, offset):
        cv.AdaptiveThreshold(self.img, self.img, max_value, adaptive_method, threshold_type, block_size, offset)
    
    def hough_circles(self):
        circle_storage = cv.CreateMat(self.get_height(), 1, cv.CV_32FC3)
        cv.HoughCircles(self.img, circle_storage, Image.HOUGH_GRADIENT, 2, self.get_width()/10)
        circles = []
        for i in range(circle_storage.rows):
            p = circle_storage[i, 0]
            center = (cv.Round(p[0]), cv.Round(p[1]))
            radius = cv.Round(p[2])
            circles.append(Circle(center, radius))
        return circles


# The following algorithms need an output buffer different from the input buffer
def log_polar(img_in, img_out, center, magnitude=40, flags=cv.CV_INTER_LINEAR+cv.CV_WARP_FILL_OUTLIERS):
    cv.LogPolar(img_in.img, img_out.img, center, magnitude, flags)


class FileImage(Image):
    def __init__(self, path, iscolor=cv.CV_LOAD_IMAGE_COLOR):
        Image.__init__(self, cv.LoadImage(path, iscolor))


class NewImage(Image):
    def __init__(self, size, depth=cv.IPL_DEPTH_8U, channels=3):
        Image.__init__(self, cv.CreateImage(size, depth, channels))

###############################################################################
# Video Capture
###############################################################################
class Capture:
    def __init__(self, capture):
        self.capture = capture
    
    def query_frame(self):
        return Image(cv.QueryFrame(self.capture))
    
    def set_pos_frames(self, pos):
        cv.SetCaptureProperty(self.capture, cv.CV_CAP_PROP_POS_FRAMES, pos)
    
    def get_frame_count(self):
        return int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_COUNT))
    
    def get_fps(self):
        return cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FPS)
    
    def get_frame_width(self):
        return int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
    
    def get_frame_height(self):
        return int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
    
    def get_size(self):
        return (self.get_frame_width(), self.get_frame_height())


class FileCapture(Capture):
    def __init__(self, path):
        Capture.__init__(self, cv.CreateFileCapture(path))


class CameraCapture(Capture):
    def __init__(self, cam_n=0):
        Capture.__init__(self, cv.CreateCameraCapture(cam_n))


class VideoWriter:
    MOTION_JPG = cv.CV_FOURCC('M','J','P','G')
    
    def __init__(self, path, fourcc, fps, frame_size):
        self.writer = cv.CreateVideoWriter(path, fourcc, fps, frame_size)
    
    def write_frame(self, frame):
        cv.WriteFrame(self.writer, frame.img)


def play_loop(window, capture, ms=33):
    while True:
        frame = capture.query_frame()
        if not frame: break
        
        window.show_image(frame)
        
        # default: play the video at 30 frames per second: pause 33ms
        if Window.wait_esc(ms): break

###############################################################################
# Shapes
###############################################################################
class Shape:
    BLUE = (0xff, 0x00, 0x00)
    
    def __init__(self, color):
        if color is None: color = Shape.BLUE
        self.color = color

class Rectangle(Shape):
    def __init__(self, x0, y0, x1, y1, color=None):
        Shape.__init__(self, color)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    def draw(self, img, color=None):
        if color is None: color = self.color
        cv.Rectangle(img.img, (self.x0, self.y0), (self.x1, self.y1), self.color)


class Circle(Shape):
    def __init__(self, center, radius, color=None):
        Shape.__init__(self, color)
        self.center = center
        self.radius = radius
    
    def draw(self, img, color=None):
        if color is None: color = self.color
        cv.Circle(img.img, self.center, self.radius, self.color)


