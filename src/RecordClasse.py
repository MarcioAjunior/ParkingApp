import time
from datetime import datetime

DATETIME_MES = datetime.now().date().strftime("%m")

class Record: 

    def __init__(self, tempoUsado, data=None, mes=DATETIME_MES, _id = None, vaga=0):
        self.tempoUsado = tempoUsado
        self.data = data
        self.mes = mes
        if data is None:
            self.data = datetime.now().date().strftime("%d/%m/%Y")
            self.mes = DATETIME_MES
        if _id is None:
            self.id = self.data + '-{}'.format(vaga)
        else:
            self.id = _id

    def json(self):
        """Retorna o objeto como um json"""
        return {
        'id' : self.id,
        'tempoUsado' : self.tempoUsado,
        'data' : self.data,
        'mes': self.mes,
        }