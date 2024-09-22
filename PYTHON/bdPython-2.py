import oracledb

def get_conexao () -> oracledb.Connection:
    return oracledb . connect ( user ='rm557540', password ='250106',
        dsn ='oracle.fiap.com/orcl')

def inserir_filme(conn: oracledb.Connection) -> None:
    with conn.cursor() as cur:
        nome_filme = input("Digite o nome do filme: ")
        diretor_filme = input("Digite o nome do diretor do filme: ")
        data_lancamento = input("Digite a data de lançamento do filme (DD-MM-YYY): ")

        cur.execute(
            "INSERT INTO PY_FILMES (NOME_FILME, DIRETOR_FILME, DATA_LANCAMENTO) VALUES (:NOME_FILME, :DIRETOR_FILME, TO_DATE(:DATA_LANCAMENTO, 'DD-MM-YYYY'))",
            {'NOME_FILME': nome_filme, 'DIRETOR_FILME': diretor_filme, 'DATA_LANCAMENTO': data_lancamento}
            )
        conn.commit ()
        print("Filme inserido com sucesso!")

def consultar_filme (conn, nome_filme):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM PY_FILMES WHERE NOME_FILME = :NOME_FILME", {'NOME_FILME': nome_filme})
        resultado = cur.fetchone()    
        return resultado
    cur.close()
    
def alterar_filme(conn, nome_filme):
    with conn.cursor() as cur:
        print("Selecione os campos que deseja alterar:")
        print("1. Nome do filme")
        print("2. Diretor do filme")
        print("3. Data de lançamento")
        print("4. Todos os campos")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1": #Nome do filme
            novo_nome_filme = input("Digite o novo nome do filme: ")
            cur.execute("""
                UPDATE PY_FILMES
                SET NOME_FILME = :NOVO_NOME_FILME
                WHERE NOME_FILME = :NOME_FILME
            """, {
                'NOME_FILME': nome_filme,
                'NOVO_NOME_FILME': novo_nome_filme
            })
        elif escolha == "2": #Diretor do filme
            novo_diretor_filme = input("Digite o novo diretor do filme: ")
            cur.execute("""
                UPDATE PY_FILMES
                SET DIRETOR_FILME = :NOVO_DIRETOR_FILME
                WHERE NOME_FILME = :NOME_FILME
            """, {
                'NOME_FILME': nome_filme,
                'NOVO_DIRETOR_FILME': novo_diretor_filme
            })
        elif escolha == "3": #Data de lançamento
            nova_data_lancamento = input("Digite a nova data de lançamento do filme (DD-MM-YYYY): ")
            cur.execute("""
                UPDATE PY_FILMES
                SET DATA_LANCAMENTO = TO_DATE(:NOVA_DATA_LANCAMENTO, 'DD-MM-YYYY')
                WHERE NOME_FILME = :NOME_FILME
            """, {
                'NOME_FILME': nome_filme,
                'NOVA_DATA_LANCAMENTO': nova_data_lancamento
            })
        elif escolha == "4": #Todos os campos
            novo_nome_filme = input("Digite o novo nome do filme: ")
            novo_diretor_filme = input("Digite o novo diretor do filme: ")
            nova_data_lancamento = input("Digite a nova data de lançamento do filme (DD-MM-YYYY): ")
            cur.execute("""
                UPDATE PY_FILMES
                SET NOME_FILME = :NOVO_NOME_FILME, DIRETOR_FILME = :NOVO_DIRETOR_FILME, DATA_LANCAMENTO = TO_DATE(:NOVA_DATA_LANCAMENTO, 'DD-MM-YYYY')
                WHERE NOME_FILME = :NOME_FILME
            """, {
                'NOME_FILME': nome_filme,
                'NOVO_NOME_FILME': novo_nome_filme,
                'NOVO_DIRETOR_FILME': novo_diretor_filme,
                'NOVA_DATA_LANCAMENTO': nova_data_lancamento
            })
        else:
            print("Opção inválida!")

def apagar_filme(conn, nome_filme):
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM PY_FILMES
                    WHERE NOME_FILME = :NOME_FILME
                    """, {'NOME_FILME': nome_filme})
        conn.commit()
        print("Filme excluído com sucesso!")  


if __name__ == " __main__ ":
    print("Deseja fazer qual ação em sua tabela? \n1- Inserir dados \n2- Consultar dados \n3- Alterar dados \n4-Apagar dados")
    opcao = input("Escolha a opção:")
    if  opcao == 1: #Inserir dados
        with get_conexao() as conn:
            inserir_filme(conn)
        
    elif opcao == 2: #Consultar dados
        with get_conexao() as conn:
            nome_filme = input("Digite o nome do filme: ")
            resultado = consultar_filme(conn, nome_filme)
            if resultado:
                print("Filme encontrado!")
                print("Nome do filme:", resultado[0])
                print("Diretor do filme:", resultado[1])
                print("Data de lançamento:", resultado[2])
            else:
                print("Filme não encontrado!")         
    elif opcao == 3: #Alterar dados
        with get_conexao() as conn:
            nome_filme = input("Digite o nome do filme: ")
            resultado = consultar_filme(conn, nome_filme)
            if resultado:
                print("Filme encontrado!")
                alterar_filme(conn, nome_filme)
                print("Dados do filme alterados com sucesso!")
            else:
                print("Filme não encontrado")
    elif opcao == 4: #Apagar dados
        with get_conexao() as conn:
            nome_filme = input("Digite o nome do filme: ")
            resultado = consultar_filme(conn, nome_filme)
            if resultado:
                print("Filme encontrado!")
                apagar_filme(conn, nome_filme)
            else:
                print("Filme não econtrado!")