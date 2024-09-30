class Pessoa:
    #criando o método construtor
    def __init__(self, nome, hobby, endereco):
        #estamos criando os atributos da classe utilizando método construtor. nesse caso, precisamos passar os parâmetros que serão usados como valores dos atributos
        self.nome = nome 
        self.hobby = hobby
        self.endereco = endereco

    #criando os métodos normais
    def exibirDados(self):
        print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")


#criando objetos
pessoa1 = Pessoa("Geraldo", "corredor", "Rua 10 Natal")
pessoa1.exibirDados() #chamando o método classe

pessoa2 = Pessoa("Karla", "artes maciais", "Renascença")
print(pessoa2.nome)