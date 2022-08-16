import cv2 as cv
import pickle
import cvzone
import numpy as np
from resizeImage import resizingImage
from VagasClasse import Vagas
from MainStramVideo import MAIN_VIDEO_STREAM
import threading
from timer import verify

def verify_timer():
    verify()

timer = threading.Thread(target=verify_timer, name='Verify')
timer.start()

def init():
    while True:
        # img = MAIN_VIDEO_STREAM.get_frame().get('frame')
        # cv.imshow('Image', img)
        
        if cv.waitKey(1) & 0xFF==ord('x'):
            cv.destroyAllWindows()
            break