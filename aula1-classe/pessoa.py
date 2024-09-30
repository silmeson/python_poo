class Pessoa:
    #atributos - são as carcterísticas da classe
    nome = "Fulano"
    idade = 25
    altura = 1.70

    #métodos - são os comportamnetos da classe
    def falar(self,texto): #self é um parâmetro obrigatório do python que informa que o método pertecence à própria classe que foi criada
        print(f"Tenho algo para te falar: {texto}")


#criando objetos
pessoa1 = Pessoa() #dessa forma estamos criando um objeto do tipo pessoa

print(pessoa1.nome, pessoa1.idade)
pessoa1.falar("Bomdia! Péssima segunda.")