from time import sleep
from VagasClasse import Vagas
from datetime import datetime
from RecordClasse import Record
from MainStramVideo import MAIN_VIDEO_STREAM

def verify():
    for vaga in MAIN_VIDEO_STREAM.lista_de_vagas:
        if vaga.emUso == True:
            if vaga.record == []:
                vaga.record.append(Record(0))
            for record in vaga.record:
                if record.data == datetime.now().strftime("%d/%m/%Y"):
                    record.tempoUsado +=1
                else:
                    vaga.record.append(Record(0))
                    
    MAIN_VIDEO_STREAM.write()
    sleep(1.1)
    verify()