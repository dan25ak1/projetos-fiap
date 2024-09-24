import banco
import datetime

lista = [
    ['ET O Estraterrestre', 'Steven Spielberg', 'Drew Barrimore e Peter Coyote', datetime.datetime(1982, 12, 25), 'Universal Studios', 7.9, 'O garoto faz amizade com um ET'],

    ['Uma Mente Brilhante', 'Ron Howard', 'Russel Croew e Jennifer Connely',  datetime.datetime(2002, 2, 15), 'DreamWorks', 8.4 , 'John é conhecido como o gênio da matemática'],

    ['Estrelas Além do Tempo', 'Theodore Melfi', 'Octavia Spencer e Kevin Costner', datetime.datetime(2017, 2, 2), 'Fox', 8.8, 'Na corrida espacial']
]

for linha in lista:
    movie = {'titulo': linha[0],
             'diretor': linha[1],
             'atores': linha[2],
             'data_lancamento': linha[3],
             'estudio': linha[4],
             'nota': linha[5],
             'sinopse': linha[6]}
    banco.insere_filme(movie)