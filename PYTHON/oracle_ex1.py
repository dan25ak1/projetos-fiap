import oracledb


url = "oracle.fiap.com.br/orcl"
conexao = oracledb.connect(user="rm557540", password="250106", dsn=url)

print("Versão do banco", conexao.version)
cur = conexao.cursor()
cur.execute("select placa from ddd_carro")
registros = cur.fetchall() #pega todos os dados da tabela e guarda na variavel

#que tipo de dado é o registro?
#registros é uma lista <class list

for reg in registros:
    print(reg)

cur.close
conexao.close()