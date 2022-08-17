from CameraClasse import VideoCamera
import pickle

MAIN_VIDEO_STREAM = None

with open('./src/resources/ParkingPos', 'rb') as f:
    lista_de_vagas = pickle.load(f)
    MAIN_VIDEO_STREAM = VideoCamera(
        src=0,
        lista_de_vagas = lista_de_vagas,
        file = f
    )