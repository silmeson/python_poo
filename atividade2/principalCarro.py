from carro import Carro

carro1 = Carro("Chevrolet", "Onix", 2022, 150)
carro2 = Carro("Fiat", "Fusion", 2021, 100)

carro1.exibirDetalhes()
print("O valor total das diárias é ",carro1.calcularPrecoAluguel(4))

carro2.exibirDetalhes()
print("O valor total das diárias é ",carro2.calcularPrecoAluguel(7))
