import cv2 as cv
import pickle
import numpy as np
from resizeImage import resizingImage
from VagasClasse import Vagas

try:
    with open('src/resources/ParkingPos', 'rb') as f:
        lista_de_vagas = pickle.load(f)
        vagasList = [vaga.positions for vaga in lista_de_vagas]
except:
    vagasList = []

cordenates = []

#Função que adiciona e remove vagas
def mouseClick(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        global cordenates
        cordenates.append([x,y])
        if len(cordenates) == 2:
            vagasList.append(cordenates)
            cordenates = []
    if event == cv.EVENT_RBUTTONDOWN:
        vagasList.pop()


while True:
    #Lendo e redimensionando a imagem
    img = cv.imread('./src/resources/quarto.jpeg')
    img = resizingImage(img)

    for inicial, final in vagasList:
        cv.rectangle(img, inicial, final, (255, 0, 255), 2)
    cv.imshow("Image", img)
    cv.setMouseCallback("Image", mouseClick)
    
    if cv.waitKey(1) & 0xFF==ord('x'):
        lista_de_vagas = [Vagas(positions=item,create=True) for item in vagasList]

        with open('./src/resources/ParkingPos','wb') as f:
            pickle.dump(lista_de_vagas, f)
        break
