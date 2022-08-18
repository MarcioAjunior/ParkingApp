from RecordClasse import Record

class Vagas:

    COUNT = 0

    def __init__(self, _id = None,positions = [],emUso=False,record=[],create = False):
        if _id == None:
            self.id = Vagas.my_id()
        else:
            self.id = _id       
        self.positions = positions
        self.emUso = emUso
        self.record = [Record(item, vaga=self.id) for item in record]

    @classmethod
    def my_id(c):
        c.COUNT += 1
        return c.COUNT

    def __repr__(self):
        reprVagas = str([item for item in self.positions])
        record = str([item for item in self.record])
        return "id :{}, emUso:{}, record: {} positions: {}".format(self.id,self.emUso,record,reprVagas)


    def json(self):
        """Retorna o objeto como um json"""
        return {
        'id' : self.id,
        'positions' : self.positions,
        'emUso': self.emUso,
        'record' : [record.json() for record in self.record],
        }

    def rep_positions(self):
        return self.positions