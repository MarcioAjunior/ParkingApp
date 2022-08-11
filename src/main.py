import cv2 as cv
import pickle
import cvzone
import numpy as np
from resizeImage import resizingImage
from VagasClasse import Vagas

cap = cv.VideoCapture(0)
with open('./src/resources/ParkingPos', 'rb') as f:
    lista_de_vagas = pickle.load(f)
    posList = [item.positions for item in lista_de_vagas]

def empty(a):
    pass

 
cv.namedWindow("Vals")
cv.resizeWindow("Vals", 640, 240)
cv.createTrackbar("Val1", "Vals", 25, 50, empty)
cv.createTrackbar("Val2", "Vals", 16, 50, empty)
cv.createTrackbar("Val3", "Vals", 5, 50, empty)
 
def checkSpaces():
    spaces = 0
    for position in posList:
        print(position, 'show position')
        npposition = np.array(position,np.int32).reshape((-1, 1, 2))
        
        #Recortando em retangulos
        rect = cv.boundingRect(npposition)
        x,y,w,h = rect
        croped = imgThres[y:y+h, x:x+w].copy()
        cv.imshow(str(x*y+h),croped)

        total_pixeis = np.sum(croped == 255) + np.sum(croped == 0)

        print(total_pixeis, 'Totais de pixeis')
        print(np.sum(croped == 255), 'Pixeis branco')
        print(np.sum(croped == 0), 'Pixeis pretos')

        #Pixeis pretos, contagem dos 0 na imagem
        count = cv.countNonZero(croped)

        print(np.sum(croped == 0), 'pretos segundo o countNonZero')

        if count < 900:
            color = (0, 200, 0)
            thic = 1
            spaces += 1
 
        else:
            color = (0, 0, 200)
            thic = 1
 
        cv.rectangle(img, (x, y), (x + w, y + h), color, thic)
 
        cv.putText(img, str(cv.countNonZero(croped)), (x, y + h - 6), cv.FONT_HERSHEY_PLAIN, 1,
                    color, 2)
 
    cvzone.putTextRect(img, f'Livres: {spaces}/{len(posList)}', (50, 60), thickness=3, offset=20,
                       colorR=(0, 200, 0)) 

while True:
 
    # Get image frame
    success, img = cap.read()
    img = resizingImage(img)

    # img = cv.imread('img.png')
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # imgBlur = cv.GaussianBlur(imgGray, (3, 3), 1)

    ret, imgThres = cv.threshold(imgGray, 150, 255, cv.THRESH_BINARY)
 
    val1 = cv.getTrackbarPos("Val1", "Vals")
    val2 = cv.getTrackbarPos("Val2", "Vals")
    val3 = cv.getTrackbarPos("Val3", "Vals")
    if val1 % 2 == 0: val1 += 1
    if val3 % 2 == 0: val3 += 1
    imgThres = cv.adaptiveThreshold(imgThres, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv.THRESH_BINARY_INV, val1, val2)
    #imgThres = cv.medianBlur(imgThres, val3)
    kernel = np.ones((1, 1), np.uint8)
    imgThres = cv.dilate(imgThres, kernel, iterations=1)
 
    checkSpaces()
    # Display Output
 
    cv.imshow("Image", img)
    #cv.imshow("imgThres", imgThres)
    # cv.imshow("ImageBlur", imgBlur)
    if cv.waitKey(1) & 0xFF==ord('x'):
        break