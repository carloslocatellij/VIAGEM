from mongo_table import MongoTable
import hospede

class Hotel(MongoTable):
    def __init__(self, num_quartos, cidade):
        self.num_quartos = num_quartos
        self.cidade = cidade
        self.quartos = ([], self.num_quartos)

    def reserva():
        pass

    def check_in():
        pass

    def check_out():
        pass

class Quarto():
    def __init__(self, numero_quarto) -> None:
        self.quarto = numero_quarto
