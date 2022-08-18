import cv2 as cv
import cvzone
import numpy as np
import pickle 
from time import sleep
from resizeImage import resizingImage

class VideoCamera: 
    def __init__(self, src=None, lista_de_vagas=[], file=None): 
      self.video = cv.VideoCapture(src)
      self.lista_de_vagas = lista_de_vagas
      self.file = file

    def __del__(self): 
      self.video.release()

    def write(self):
      sleep(10)
      with open('./src/resources/ParkingPos','wb') as f:
            pickle.dump(self.lista_de_vagas, f)
      self.write()

    def get_frame(self):
      ret, frame = self.video.read()
      #Tratando a imagem
      sleep(0.01)
      frame = resizingImage(frame)
      frame_blur = cv.GaussianBlur(frame.copy(), (5,5), 3)
      imgGray_blur = cv.cvtColor(frame_blur, cv.COLOR_BGR2GRAY)
      
      self.checkSpaces(imgGray_blur, frame)

      ret, jpeg = cv.imencode('.jpg', frame) 
      jpeg = jpeg.tobytes()
      return {'jpeg' : jpeg, 'frame':frame}

    def checkSpaces(self,imageProcessed,img):
      spaces = 0
      #Recortando em retangulos
      for vaga in self.lista_de_vagas:
        npposition = np.array(vaga.positions,np.int32).reshape((-1, 1, 2))
        rect = cv.boundingRect(npposition)
        x,y,w,h = rect
        croped = imageProcessed[y:y+h, x:x+w].copy()
        laplacian = cv.Laplacian(croped, cv.CV_64F)
        # cv.imshow(str(vaga.id),cv.convertScaleAbs(laplacian))
        delta = np.mean(np.abs(laplacian))

        if delta < 1.1:
            vaga.emUso = False
            color = (0, 200, 0)
 
        else:
            vaga.emUso = True
            spaces += 1
            color = (0, 0, 200)

        cv.rectangle(img, (x, y), (x + w, y + h), color, 1)

        cv.putText(img, str(delta), (x, y + h - 6), cv.FONT_HERSHEY_PLAIN, 1,
                    (255,5,0,0), 1)
        
      cvzone.putTextRect(img, f'Vagas ocupadas: {spaces}/{len(self.lista_de_vagas)}', (50, 60), scale=2, thickness=3, offset=10,
                       colorR=(0, 200, 0))