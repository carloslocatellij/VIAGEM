from typing import Any
from mongoTable import MongoTable
from hospede import Hospede as hospede


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, estrelas: int, tamanho: int):
        self.nome = nome
        self.cidade = cidade
        self.estrelas = estrelas
        self.tamanho = tamanho
        self.quartos = [Quarto(n+1) for n in range(0, self.tamanho)]

    def reserva(self, hospede: object, quarto: int):
        reservados = [n.reservado for n in self.quartos]
        if not all(reservados):
            if not self.quartos[quarto].reservado\
                    or not self.quartos[quarto].ocupado:
                self.quartos[quarto].ocupante = hospede
                self.quartos[quarto].reservado = True
                #self.save()
            else:
                raise Exception('Quarto já Reservado/Ocupado')
        else:
            raise Exception(' Hotel Lotado')

    def check_in(self, hospede: object, quarto: int):  
        reserva = self.quartos[quarto]
        if reserva.ocupante == hospede and reserva.reservado:
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

    def __getitem__(self, quarto: int) -> Any:
        return self.quarto

    def __repr__(self) -> str:
        return f'Quarto ({str(self.quarto)}, {repr(self.ocupante)})'


nome = 'Carlos'
idade = 37

h = 'California'
city = 'San Francisco'
qtd_quartos = 3

hosp = hospede(nome, idade)
p1 = hospede('José', 22)
p2 = hospede('João', 33)
p3 = hospede('Raul', 44)


hotel = Hotel(h, city, 3, qtd_quartos)
hotel.reserva(hosp, 1)

print(hotel.quartos[1].ocupante)

print(hotel.quartos[1].ocupado)

hotel.check_in(hosp, 1)

print(hotel.quartos[1].ocupado)
