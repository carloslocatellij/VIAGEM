from modelos.mongo_table import MongoTable
import hospede

class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, num_quartos: int):
        self.nome = nome
        self.cidade = cidade
        self.num_quartos = num_quartos
        self.quartos = [Quarto(n, None) for n in range(0, self.num_quartos)]

    def reserva(self, hospede: object, quarto: object):
        if not None in self.quartos:
            return 'Hotel está com lotação máxima'
        else:
            for q in self.quartos:
                if q[1] is None:
                    q[1] = hospede
                    break
                


    def check_in(self, hospede: str):
        pass

    def check_out(self, quarto: object):
        pass

class Quarto():
    def __init__(self, numero_quarto: int, tipo: str = 'básico', ocupado: bool = False):
        self.quarto = numero_quarto
        self.tipo = tipo

