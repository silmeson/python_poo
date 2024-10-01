class Conta:
    def __init__(self, numero, titular, saldo, limite = 200): #método construtor
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite= limite
#usandop o "_" antes dos nomes dos atributos protegemos/privamos sua visibilidade, 1 '_' protege com método herança e 2 '_' priva a visibilidade do atributo com método encapsulamento

    #criando os métodos
    def detalhes(self):
        print(f"Olá {self.__titular} seu saldo atual é R${self.__saldo}")

    #método irá retornar conteúdo do limite
    def getLimite(self):
        return self.__limite

    #método que irá alterar o valor do limite
    def setLimite(self, valor):
        if valor < 0:
            print("Informe o valor positivo para o limite")
        else:
            self.__limite = valor


#criando método para depositar valor
    def depositar(self, valor):
        if valor < 0:
            print("Informe um valor maior que zero")
        else:
            self.__saldo = self.__saldo + valor

#criar método para sacar valor
    def sacar(self, valor):
        if self.__saldo <= 0 or valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo = self.__saldo - valor    