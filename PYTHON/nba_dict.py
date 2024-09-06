def cadastra_equipe(conferir: dict):
    nome = input("Digite o nome:")
    if nome in conferir:
        print(f"ERRO, {nome} ja cadastrado")
    else:
        conferir[nome] = []

def cadastra_jogador(conferir: dict):
    time = input("Informe o time:")
    if not time in conferir:
        print(f"ERRO, {time} não cadastrado")
    else:
        nome = input("Insira o nome do jogador: ")
        camisa = int(input("Insira a camisa do jogador: "))
        posicao = input("Insira a posicao do jogador: ")
        player = {
            "nome": nome, "numero": camisa, "posicao": posicao
        }
        conferir[time].append(player)

def lista_equipe(conferir: dict):
    time = input("Time: ")
    if not time in conferir:
        print(f"{time} não existe!")
    else: 
        for player in conferir[time]:
            print(player.get('nome'), player.get('camisa'), player.get('posicao'))


equipes = {}

while True:
    print("1 - Cadastrar Equipe")
    print("2 - Cadastrar Jogador")
    print("3 - Lista equipes")
    print("4 - Sair")
    opcao = int(input("opcao: "))

    if opcao == 1:
        cadastra_equipe(equipes)
    elif opcao == 2:
        cadastra_jogador(equipes)
    elif opcao == 3:
        lista_equipe(equipes)