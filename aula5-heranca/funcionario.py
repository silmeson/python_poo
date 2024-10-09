class Pessoa: #superclasse ou classe-mãe
    def __init__(self, nome, cargo):
        self._nome = nome #estamos mudando a visibilidade do atributo de privado para protegido, dessa forma, as clsses filhas poderão acessar os atributos da classe mãe
        self._cargo = cargo

    def informacoes(self):
        print(f"Olá {self._nome}, na empresa seu cargo é: {self._cargo}")

#criando classe filha
class Engenheiro(Pessoa):  # a classe engenheiro está herdando as caracteristicas da classe Pessoa, que será sua classe mãe
    def mostraDetalhes(self):
        print(f"Olá, eu sou {self._nome} e sou um engenheiro")


class Secretario(Pessoa):
    def relatorio(self):
        print(f"Olá, meu nome é {self._nome} e meu cargo na empresa é {self._cargo} ")