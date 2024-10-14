import sqlite3

#conexão e criação da tabela
conexao = sqlite3.connect("departamento.db")

tabela =  """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""

consulta = conexao.cursor()

consulta.execute(tabela)

#solicitar campos para atualizar

codigo = int(input("Qual o código do funcionário: "))

sql = "DELETE FROM funcionario WHERE codigo = ?"

campos = (codigo,) #é preciso colocar uma vírgula dps do item para configurar uma tupla, caso contrário n será considerado uma tupla válida

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, "linha(s) excluída com sucesso!\n")
conexao.close