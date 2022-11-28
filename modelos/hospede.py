from mongoTable import MongoTable


class Hospede(MongoTable):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Hospede({self.nome}, {self.idade})'