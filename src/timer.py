from time import sleep
from VagasClasse import Vagas
from datetime import datetime
from RecordClasse import Record
from MainStramVideo import MAIN_VIDEO_STREAM


#Rever essa lógica
def verify():
    for vaga in MAIN_VIDEO_STREAM.lista_de_vagas:
        if vaga.emUso == True:
            if vaga.record == []:
                new_record = Record(tempoUsado=0, vaga=vaga.id)
                vaga.record.append(new_record)
            for record in vaga.record:
                if record.data == datetime.now().strftime("%d/%m/%Y"):
                    record.tempoUsado +=1
                    vaga.tempoPorMes[int(record.mes) - 1] += 0.00027
                    vaga.tempoPorMes[int(record.mes) - 1] = round(vaga.tempoPorMes[int(record.mes) - 1])
            data_hoje = [rec for rec in vaga.record if rec.data == datetime.now().strftime("%d/%m/%Y")]
            if data_hoje == []:
                record = Record(tempoUsado=0, vaga=vaga.id)
                vaga.record.append(record)
    sleep(1.3)
    verify()