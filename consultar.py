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

#passo 5 - criar comando sql para vonsultar dados
sql = "SELECT * FROM funcionario"

#passo 6 - executar o comando
consulta.execute(sql)

#passo 7 - exibir dados no banco
resultado = consulta.fetchall() #fetchall() irá trazer todos os registros que existem no banco de dados

print(resultado)

#passo 8 - finalizar conexão
conexao.close()