import oracledb

def get_conexao():
    return oracledb.connect(user="rm557540", password="250106", dsn="oracle.fiap.com.br/orcl")

def inclui(mensagem : dict):
    sql = '''INSERT INTO T_PY_MENSAGEM ( ASSUNTO, DESTINATARIO, REMETENTE, CONTEUDO)
    VALUES (:ASSUNTO, :DESTINATARIO, :REMETENTE, :CONTEUDO)'''

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, mensagem)
        conn.commit()

def altera(mensagem: dict):
    sql = '''UPDATE T_PY_MENSAGEM SET ASSUNTO=:ASSUNTO, DESTINATARIO=:DESTINATARIO, REMETENTE=:REMETENTE, CONTEUDO=:CONTEUDO
     WHERE ID=:ID'''
    
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, mensagem)
        conn.commit()

def recupera(id: int) -> dict:
    sql = "SELECT * FROM T_PY_MENSAGEM WHERE id = :id"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"id": id})
            row = cur.fetchone()
            if row:
                return {
                    'id': row[0],
                    'assunto': row[1],
                    'destinatario': row[2],
                    'remetente': row[3],
                    'conteudo': row[4]
                }
            else:
                return None

def recupera_assunto(assunto: str) -> list:
    sql = "SELECT * FROM T_PY_MENSAGEM WHERE ASSUNTO LIKE :ASSUNTO"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"assunto": f"%{assunto}%"})
            rows = cur.fetchall()
            result = []
            for row in rows:
                result.append({
                    'id': row[0],
                    'assunto': row[1],
                    'destinatario': row[2],
                    'remetente': row[3],
                    'conteudo': row[4]
                })
            return result

def recupera_destinatario(destinatario: str) -> list:
    sql = "SELECT * FROM T_PY_MENSAGEM WHERE DESTINATARIO LIKE :DESTINATARIO"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"destinatario": f"%{destinatario}%"})
            rows = cur.fetchall()
            result = []
            for row in rows:
                result.append({
                    'id': row[0],
                    'assunto': row[1],
                    'destinatario': row[2],
                    'remetente': row[3],
                    'conteudo': row[4]
                })
            return result

def apaga(id: int):
    sql = "DELETE FROM T_PY_MENSAGEM WHERE ID=:ID"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"ID": id})
        conn.commit()