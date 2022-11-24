from typing import Any
from mongo_table import MongoTable
from hospede import Hospede as hospede


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, num_quartos: int):
        self.nome = nome
        self.cidade = cidade
        self.num_quartos = num_quartos
        self.quartos = [Quarto(n+1) for n in range(0, self.num_quartos)]

    def reserva(self, hospede: object, quarto: int):
        if None not in (n.ocupante for n in self.quartos):
            return 'Hotel está com lotação máxima'
        else:
            self.quartos[quarto].ocupante = hospede

    def check_in(self, hospede: str):
        pass

    def check_out(self, quarto: object):
        pass

    def __repr__(self) -> str:
        return f'Hotel ({self.nome}, em {self.cidade})'


class Quarto():
    def __init__(self, numero_quarto: int, ocupante: object = None, 
    tipo: str = 'básico', ocupado: bool = False):
        self.quarto = numero_quarto
        self.ocupante = ocupante
        self.tipo = tipo
        self.ocupado = ocupado

    def __setitem__(self, __name: str, __value: Any) -> None:
        self.__name = __value

    def __getitem__(self, __name: str) -> Any:
        return self.__name

    def __repr__(self) -> str:
        return f'Quarto ({self.quarto}, {self.ocupante})'


nome = 'Carlos'
idade = 37

h = 'California'
city = 'San Francisco'
qtd_quartos = 3

hosp = hospede(nome, idade)
hotel = Hotel(h, city, qtd_quartos)
hotel.reserva(hosp, 1)

print(hotel.quartos[1].ocupante)

