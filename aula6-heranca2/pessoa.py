class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def info(self):
        print(f"Nome: {self._nome}. Idade: {self._idade}")


#classe filha 1 - aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade) #utilizando o construtor da classe mãe 
        self._serie = serie #estamos utilizando um atributo exclusivo da classe filha

    def estudar(self):
        print(f"{self._nome} está estudando no {self._serie}")


#classe 2 - professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def ensinar(self):
        print(f"{self._nome} é professor da disciplina {self._disciplina}")
