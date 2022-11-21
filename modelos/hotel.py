from typing import Any
from mongo_table import MongoTable
from hospede import Hospede as hospede

class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, num_quartos: int):
        self.nome = nome
        self.cidade = cidade
        self.num_quartos = num_quartos
        self.quartos = [Quarto(n, None) for n in range(0, self.num_quartos)]

    def reserva(self, hospede: object, quarto: object):
        if not None in (n.ocupante for n in self.quartos):
            return 'Hotel está com lotação máxima'
        else:
            for q in self.quartos:
                if q.ocupante is None:
                    q.ocupante = hospede
                    break

    def check_in(self, hospede: str):
        pass

    def check_out(self, quarto: object):
        pass

    def __repr__(self) -> str:
        return f'Hotel ({self.nome}, em {self.cidade})'

class Quarto():
    def __init__(self, numero_quarto: int, ocupante: object=None , tipo: str = 'básico', ocupado: bool = False):
        self.quarto = numero_quarto
        self.ocupante = ocupante
        self.tipo = tipo
        self.ocupado =ocupado

    def __setitem__(self, __name: str, __value: Any) -> None:
        self.__name = __value
    
    def __getitem__(self, __name: str) -> Any:
        return self.__name

    def __repr__(self) -> str:
        return f'Quarto ({self.quarto})'
