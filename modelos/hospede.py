from mongo_table import MongoTable


class Hospede(MongoTable):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'O ocupante chama {self.nome} !'