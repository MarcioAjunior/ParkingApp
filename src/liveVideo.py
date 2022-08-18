from flask import Flask, Response, stream_with_context, jsonify
from CameraClasse import VideoCamera
from MainStramVideo import MAIN_VIDEO_STREAM
from VagasClasse import Vagas
from flask_cors import CORS
import threading
import time
from timer import verify
import json

app = Flask(__name__)
CORS(app)

def gen(camera):
        while True:
            frame = MAIN_VIDEO_STREAM.get_frame().get('jpeg')
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
        return Response(gen(MAIN_VIDEO_STREAM),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def send_all_data():
    #Aqui
    objt_list = [item.json() for item in MAIN_VIDEO_STREAM.lista_de_vagas]
    print(objt_list,'MINHA LISTA SAINDO')
    return {"msg" : json.dumps(objt_list)}

@app.route('/<vaga_id>')
def send_one_data(vaga_id: str):
        for vaga in MAIN_VIDEO_STREAM.lista_de_vagas:
            if str(vaga.id) == vaga_id:
                return {
                        "msg" : f'{vaga}'
                    }
            return json.dumps({"msg" :"Não encontrado"})



def startServer():
    app.run(host='0.0.0.0', port=5001, threaded=True, use_reloader=False)

def verify_timer():
    verify()

def write():
    MAIN_VIDEO_STREAM.write()

if __name__ == '__main__':
    threadServer = threading.Thread(target=startServer,name='StarterServer')
    timer = threading.Thread(target=verify_timer, name='Verify')
    write = threading.Thread(target=write, name='Write')
    write.start()
    timer.start()
    threadServer.start()