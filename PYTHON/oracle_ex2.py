#Inserindo registro

import oracledb

conn = oracledb.connect(user="rm557540", password="250106", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()


ins = '''Insert into cliente (id_cliente, nome) #coluna da tabela
            values(:id_cliente, :nome)''' #parametros nomeados


cur.execute(ins, {"id_cliente": "10",
                  "nome": "Eduarda"})

conn.commit()
cur.close
conn.close()