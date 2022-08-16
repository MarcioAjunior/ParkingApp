from flask import Flask, Response, stream_with_context
from CameraClasse import VideoCamera
from main2 import init
from MainStramVideo import MAIN_VIDEO_STREAM
import threading
import time
app = Flask(__name__)

def gen(camera):
        while True:
            frame = MAIN_VIDEO_STREAM.get_frame().get('jpeg')
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def streamer(json):
    while True:
        yield str(json)
        time.sleep(5)



@app.route('/video_feed')
def video_feed():
        return Response(gen(MAIN_VIDEO_STREAM),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def send_all_data():
    return {
        "msg" : f"{MAIN_VIDEO_STREAM.lista_de_vagas}"
     }   

@app.route('/<vaga_id>')
def send_one_data(vaga_id: str):
        for vaga in MAIN_VIDEO_STREAM.lista_de_vagas:
            print(vaga)
            if str(vaga.id) == vaga_id:
                return {
                        "msg" : f'{vaga}'
                    }
            return {"msg" :"Não encontrado"}



def startServer():
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

if __name__ == '__main__':
    threadServer = threading.Thread(target=startServer,name='StarterServer')
    threadApp = threading.Thread(target=init, name='startApp')
    threadApp.start()
    time.sleep(1)
    threadServer.start()