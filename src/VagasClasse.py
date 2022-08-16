from RecordClasse import Record

class Vagas:

    COUNT = 0

    def __init__(self, 
                id = 'Num',
                positions = [],
                emUso=False,
                record=[],
                create = False
                ):
        self.id = id
        if id == 'Num' and create:
            self.id = Vagas.my_id()
        self.positions = positions
        self.emUso = emUso
        self.record = [Record(item) for item in record]

    @classmethod
    def my_id(c):
        c.COUNT += 1
        return c.COUNT

    def __repr__(self):
        repr = '{}'.format(self.id)
        reprVagas = str([item for item in self.positions])
        record = str([item for item in self.record])
        return "id :{}, emUso:{}, record: {} positions: {}".format(repr,self.emUso,record,reprVagas)


    def rep_positions(self):
        return self.positions