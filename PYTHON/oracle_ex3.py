import oracledb

conn = oracledb.connect(user="rm557540", password="250106", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

upt = "update cliente set crm=:crm where id=:id"
cliente = {"id": '09', "nome": "Jeracebo"}

cur.close
conn.close()