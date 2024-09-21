import oracledb

def get_conexao () -> conn :
    return oracledb . connect ( user ='rm557540', password ='250106',
        dsn ='oracle.fiap.com/orcl')

if __name__ == " __main__ ":
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(
            "INSERT INTO PY_FILMES (NOME_FILME, DIRETOR_FILME, DATA_LANCAMENTO) VALUES (:NOME_FILME, :DIRETOR_FILME, TO_DATE(:DATA_LANCAMENTO, 'DD-MM-YYYY'))",
            {'NOME_FILME': 'Sonic 2 - O Filme', 'DIRETOR_FILME': 'Jeff Fowler', 'DATA_LANCAMENTO': '07-04-2022'}
            )
        conn.commit () 

print("Executado com sucesso!")

cur.close()
conn.close()