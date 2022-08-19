from time import sleep
from VagasClasse import Vagas
from datetime import datetime
from RecordClasse import Record
from MainStramVideo import MAIN_VIDEO_STREAM

def verify():
    for vaga in MAIN_VIDEO_STREAM.lista_de_vagas:
        if vaga.emUso == True:
            if vaga.record == []:
                print(vaga.id, 'vaga.id')
                new_record = Record(tempoUsado=0, vaga=vaga.id)
                print(new_record, 'New_Record')
                vaga.record.append(new_record)
            for record in vaga.record:
                if record.data == datetime.now().strftime("%d/%m/%Y"):
                    record.tempoUsado +=1
                    vaga.tempoPorMes[int(record.mes) - 1] += 1
                else:
                    vaga.record.append(Record(0, vaga=vaga.id))
    sleep(1.1)
    verify()