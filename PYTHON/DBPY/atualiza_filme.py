import banco

if __name__ == "__main__":
    filme = {'titulo': 'The Immitation Game',
             'diretor': 'Morten Tylu',
             'atores': 'Benedict Cumverbatch',
             'nota': 9.1,
             'id': 1,
             'estudio': 'Black Bear Pictures',
             'data': '28-9-2014',
             'sinopse': 'Agencia de Inteligencia recruta Alan Turing'
            }
    banco.atualiza_filme(filme)