from contaBancaria import Conta

minhaConta = Conta(123, "Silvano Silva", 1000, 500)

minhaConta.detalhes()

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(100)
minhaConta.detalhes()

minhaConta.sacar(500)
minhaConta.detalhes()

