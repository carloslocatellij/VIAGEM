from typing import Any
from mongo_table import MongoTable
from hospede import Hospede as hospede


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, estrelas: int, tamanho: int):
        self.nome = nome
        self.cidade = cidade
        self.estrelas = estrelas
        self.tamanho = tamanho
        self.quartos = [Quarto(n+1) for n in range(0, self.tamanho)]

    def reserva(self, hospede: object, quarto: int):
        for n in self.quartos:
            if not n.reservado:
                self.quartos[quarto].ocupante = hospede
                #self.save()
            else:
                raise Exception(' Hotel Lotado')

    def check_in(self, hospede: object, quarto: int):
        reserva = self.quartos[quarto]
        if reserva.ocupante == hospede:
            reserva.ocupado = True
            return reserva.ocupado
            #self.save()
        else:
            raise Exception('Quarto {} não está reservado para {}.'.format(
                quarto, hospede))

    def check_out(self, quarto: object):
        pass

    def __repr__(self) -> str:
        return f'Hotel ({self.nome}, em {self.cidade})'


class Quarto():
    def __init__(self, numero_quarto: int, ocupante: object = None, 
                    reservado: bool = False, ocupado: bool = False):
        self.quarto = numero_quarto
        self.ocupante = ocupante
        self.reservado = reservado
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
hotel = Hotel(h, city, 3, qtd_quartos)
hotel.reserva(hosp, 1)

print(hotel.quartos[1].ocupante)

print(hotel.quartos[1].ocupado)

hotel.check_in(hosp, 1)

print(hotel.quartos[1].ocupado)
