class Funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.salario = salario #esse atributo está opcional, caso não seja informado outro valor será atribuído o valor padrão de R$2000

    def getCargo(self): #retorna o atributo
        return self.__cargo

    def setCargo(self, novoCargo): #insere/altera o atributo
        self.__cargo = novoCargo


#iremos utilizar uma forma única do python para acessar atributos privados 
    #cirando o 'get' do salario
    @property #esse elemento irá criar um get'mais amigável'
    def salario(self):
        return self.__salario

    @salario.setter #irá criar um set para o salario 'mais amigável'
    def salario(self,valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__salario = valor
