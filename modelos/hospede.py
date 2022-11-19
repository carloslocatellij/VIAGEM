from mongo_table import MongoTable


class Hospede(MongoTable):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
