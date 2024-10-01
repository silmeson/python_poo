class Carro:
    def __init__(self, marca, modelo, ano, precoDiaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria

    def exibirDetalhes(self):
        print(f"O carro selecionado é da marca {self.marca}, modelo {self.modelo}, fabricado no ano de {self.ano} com o preço da diária correspondente à R${self.precoDiaria}")

    def calcularPrecoAluguel(self, dias):
        total = self.precoDiaria * dias
        return total