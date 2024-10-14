import sqlite3 #importando uma biblioteca de banco de dados

#estabelecendo conexão com o banco
conexao = sqlite3.connect("departamento.db") #estamos ciando um arquivo que irá guardar o nosso banco de dados

#passo 2 - verificar se a tabela existe
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""

#passo 3 - acessar objetos da biblioteca sqlite3 para manipular o banco
consulta = conexao.cursor() #o objeto cursor() é responsável por manipular dados do banco

#passo 4 - executar o comando de criação da tabela
consulta.execute(tabela)

#passo 5 - solicitar dados
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#passo 6 - criando comando sql para inserir os dados
sql = "INSERT INTO funcionario VALUES(?,?,?,?)" #colocamos ? no lugar dos dados reai, para evitar possíveis ataques d sql injection, isso é uma implementação da biblioteca sqlite3

#passo 7 - organizar os dados que irão substituir o ? no comando sql para inserir os dados
campos = (None, nome, salario, cargo) #criando uma tupla com os dados que serão trocados por ?. ao informar o valor none, estamos dizendo que será atribuído o valor padrão do AUTOINCREMENT

#passo 8 - executar o comando sql e substituir ? pelos campos
consulta.execute(sql, campos)

#passo 9 - gravar dados no banco
conexao.commit()

print(consulta.rowcount, "linha(s) inseridas com sucesso")

#passo 10 - finalizar conexão
conexao.close()
