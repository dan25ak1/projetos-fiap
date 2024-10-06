import oracledb

def get_conexao():
    return oracledb.connect(user='rm557540', password='250106',
                            dsn='oracle.fiap.com.br/orcl')

def insere_partida(partida):
    sql = """INSERT INTO TB_PARTIDA(RODADA, GOLS_CASA, GOLS_VISITANTE, ID_CASA, ID_VISITANTE) VALUES(:RODADA, :GOLS_CASA, :GOLS_VISITANTE, ID_CASA, :ID_VISITANTE)
"""
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()

def altera_time(time: dict):
    sql = """UPDATE TB_TIME SET VOTORIAS=:VITORIAS, EMPATES=:EMPATES, DERROTAS=:DERROTAS. GOLS_CONTRA=:GOLS_CONTRA, GOLS_PRO=:GOLS_PRO WHERE ID=:ID"""
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, time)
        con.commit()

def recupera_nome(nome: str):
    sql="""SELECT ID, NOME, VITORIAS, EMPATES, DERROTAS, GOLS_PRO, GOLS_CONTRA FROM TB_TIME WHERE NOME=:NOME"""
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute({'nome', nome})
            reg = cur.fetchone()
            if reg:
                return {}
        con.commit()

def insere_time(time: dict):
    sql = """INSERT INTO """
