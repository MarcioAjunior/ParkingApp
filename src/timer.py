from time import sleep
from VagasClasse import Vagas

def verify(lista_de_vagas=[]):
    for vaga in lista_de_vagas:
        if vaga.emUso == False:
            vaga.tempoTotalUsado += 1000
    sleep(1.1)
    verify(lista_de_vagas=lista_de_vagas)