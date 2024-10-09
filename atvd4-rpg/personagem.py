class Personagem:
    def __init__(self, nome, vida=5):
        self._nome = nome
        self._vida = vida

    def atacar(self):
        print(f"O personagem {self._nome} está atacando!")

    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}")

#classe filha 1 - jogador
class Jogador(Personagem):
    def __init__(self, nome, raca, vida=5):
        super().__init__(nome, vida=5) 
        self._raca = raca

    def usarHabilidade(self, poder):
        print(f"{self._nome} da raça {self._raca} está usando seu poder de {poder}")


#classe filha 2 - monstro
class Monstro(Personagem):
    def __init__(self, nome, tipo, forca, vida=20):
        super().__init__(nome, vida=20) 
        self._tipo = tipo
        self._forca = forca

    def exibirInformacoes(self):
        print(f"O nome do monstro é {self._nome}, do tipo {self._tipo}, com uma força de {self._forca} e vida igual à {self._vida}")

    def invocarAliado(self, nomeAliado, tipoAliado):
        print(f"Um aliado foi convocado! Ele é o {self._nome} do tipo {self._tipo}")

