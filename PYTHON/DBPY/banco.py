import oracledb

def get_conexao():
    return oracledb.connect(user="rm557540", password="250106", dsn="oracle.fiap.com.br/orcl")

def insere_filme(movie: dict):
    sql = '''INSERT INTO TB_FILME(TITULO, DIRETOR, ATORES, NOTA, DATA_LANCAMENTO, SINOPSE, ESTUDIO)
    VALUES(:TITULO, :DIRETOR, :ATORES, :NOTA, TO_DATE(:DATA_LANCAMENTO, 'DD-MM-YYYY'), :SINOPSE, :ESTUDIO)'''

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, movie)
        conn.commit()

def consulta_filme(ator: str) -> list:
    sql = """SELECT ID, TITULO, ATORES, DATA_LANCAMENTO, NOTA, ESTUDIO, SINOPSE 
        FROM TB_FILME 
        WHERE ATORES LIKE ATORES"""
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"atores": f"%{ator}%"})
            lista = cur.fethall()
            return lista
        
def apaga_filme(id: int):
    sql = "delete from tb_filme where id = :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"id": id})
        conn.commit()

def atualiza_filme(movie: dict):
    sql = '''update tb_filme set titulo=:titulo, sinopse=;sinopse, nota=:nota, diretor=:diretor, atores=:atores, estudio=:estudio, data_lancamento=to_date(data, 'dd-mm-yyyy')
    where id=:id'''

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, movie)
        conn.commit()
 
