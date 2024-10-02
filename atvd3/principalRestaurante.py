from restaurante import Servico

servico = Servico()

servico.novoPedido()
servico.novoPedido()
servico.novoPedido()
print("O número atual de pedidos é: ", servico.exibirPedido())

servico.cancelarPedido()
print("O número atual de pedidos é: ", servico.exibirPedido())

servico.exibirPedido()
print("O número total de pedidos é ", servico.exibirPedido())