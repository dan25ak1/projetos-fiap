import banco
import datetime

if __name__ == "__main__":
    tit = input("Titulo: ")
    dir = input("Diretor: ")
    dia_lanc = int(input("Dia do laçamento: "))
    mes_lanc = int(input("mês do laçamento: "))
    ano_lanc = int(input("Ano do laçamento: "))
    data = datetime.datetime(ano_lanc, mes_lanc, dia_lanc)
    sin = input("Sinopse: ")
    nota = int(input("Nota: "))
    atores = input("Atores: ")
    estudio = input("Estudio: ")

    movie = {} 
    movie['TITULO'] = tit #nome dentro da chave tem que bater com nome na tabela
    movie['DIRETOR'] = dir
    movie['DATA_LANCAMENTO'] = data
    movie['SINOPSE'] = sin
    movie['NOTA'] = nota
    movie['ATORES'] = atores
    movie['ESTUDIO'] = estudio

    banco.insere_filme(movie)