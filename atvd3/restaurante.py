class Servico:
    def __init__(self, pedido = 0):
        self.__pedido = pedido #usando os 2 '_' privamos a visibilidade do valor do atributo com método encapsulamento


    def novoPedido(self):
        self.__pedido += 1 #operação de incremento para adicionar 1 pedido


    def cancelarPedido(self):
        if self.__pedido > 0:
            self.__pedido -= 1  #operação de decremento para cancelar 1 pedido
        else:
            print("Não existe pedidos para serem cancelados.")


    def exibirPedido(self): #retorna valor do atributo
        return self.__pedido





