class Vagas:

    COUNT = 0

    def __init__(self, 
                id = 'Num',
                positions = [],
                emUso=False,
                tempoTotalUsado=0,
                create = False
                ):
        self.id = id
        if id == 'Num' and create:
            self.id = Vagas.my_id()
        self.positions = positions
        self.emUso = emUso
        self.tempoTotalUsado = tempoTotalUsado

    @classmethod
    def my_id(c):
        c.COUNT += 1
        return c.COUNT

    def __repr__(self):
        repr = '{}'.format(self.id)
        reprVagas = str([item for item in self.positions])
        return "id :{}, emUso:{}, tempoTotal: {} positions: {}".format(repr,self.emUso,self.tempoTotalUsado,reprVagas)


    def rep_positions(self):
        return self.positions