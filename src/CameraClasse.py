import cv2 as cv 

class VideoCamera: 
    def __init__(self): 
      self.video = cv.VideoCapture(0)

    def __del__(self): 
      self.video.release()

    def get_frame(self): 
      ret, frame = self.video.read() 
      ret, jpeg = cv.imencode('.jpg', frame) 
      return jpeg.tobytes()
    