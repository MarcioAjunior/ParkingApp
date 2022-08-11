class Vagas:

    def __init__(self, 
                positions = [],
                status=False,
                tempoTotalUsado=0,
                s_id = 0):
        self.id = s_id
        self.positions = positions
        self.status = status
        self.tempoTotalUsado = tempoTotalUsado

    def __repr__(self):
        repr = '{}'.format(self.id)
        reprVagas = str([item for item in self.positions])
        return "id :{}, status:{}, tempoTotal: {} positions: {}".format(repr,self.status,self.tempoTotalUsado,reprVagas)


    def rep_positions(self):
        return self.positions