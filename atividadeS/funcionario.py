class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome 
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Olá caro funcionário {self.nome}, seu cargo na empresa é {self.cargo} e o valor do seu salário corresponde à R${self.salario}")

    def verificarSalario(self):
        if self.salario <= 2000:
            print(f"{self.nome}, você tem direito a um bônus")
        else:
            print(f"{self.nome}, você não tem direito ao bônus.")

