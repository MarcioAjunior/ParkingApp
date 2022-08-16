import time
from datetime import datetime

DATETIME_MES = datetime.now().date().strftime("%m")

class Record: 

    def __init__(self, tempoUsado, data=None, mes=DATETIME_MES):
        self.tempoUsado = tempoUsado
        self.data = data
        self.mes = mes
        if data is None:
            self.data = datetime.now().date().strftime("%d/%m/%Y")
            self.mes = DATETIME_MES