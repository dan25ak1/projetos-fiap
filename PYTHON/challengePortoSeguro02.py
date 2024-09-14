import os

def limpa_terminal():
    os.system('cls')

def acess():
    print("Bem-vindo à Assistência Veicular da Porto Seguro! \nInforme o número da opção desejada. ")
    print("(1) - Cadastrar")
    print("(2) - Login")
    escolha = int(input("Digite o número correspondente a opção desejada:"))
    while escolha < 1 or escolha > 2:
        escolha = int(input("Opção incorreta! Tente novamente: "))
    return escolha

def cadastro(lista):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    cep = (input("Digite seu cep: "))
    senha = input("Crie uma senha: ")
    conf_senha = input("Confirme a senha: ")
    while senha != conf_senha:
        print("\nNão foram fornecidas senhas idênticas!\n")
        conf_senha = input("Confirme a senha: ")
    print("Conta criada com sucesso!")
    lista.append(nome)
    lista.append(email)
    lista.append(cep)
    lista.append(senha)

def login(lista):
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    print("Login feito com sucesso!")
    
def menu():
    limpa_terminal()
    print("Bem-vindo ao menu da Assistência Veicular da Porto Seguro! \nInforme o número da opção desejada.")
    print("(1) - Fazer um check-up no veículo")
    print("(2) - Qual unicade da Porto mais próxima a mim")
    print("(3) - Estou precisando de uma peça")
    print("(4) - Solicitação de guincho")
    print("(5) - Adicionar veículo")
    print("(6) - Alterar veículo")
    print("(7) - Consultar o veículo")
    print("(8)) - Sair")
    escolha = int(input("Digite o número correspondente a opção desejada: "))
    while escolha < 1 or escolha > 8:
        escolha = int(input("Opção incorreta! Tente novamente: "))
    return escolha

def check_up(lista_problema):
    limpa_terminal()
    print("Opção (1) - Fazer um check-up no veículo. \n\nSabe qual defeito o veiculo apresenta? ") 
    print("(1) Já sabe qual é o defeito.")
    print("(2) Não sei qual defeito o meu veiculo apresenta.")
    escolha = int(input("Digite o número correspondente a opção desejada: "))
    while escolha < 1 or escolha >= 3: #caso o usuário não inserir a opção correta tera que inserir novamente, até ser uma opção válida
        limpa_terminal()
        print("\nOpção inválida, digite novamente!\n")
        print("Opção (1) - Defeito no veículo selecionada. \n\nSabe qual defeito o veiculo apresenta? ") 
        print("(1) Já sabe qual é o defeito.")
        print("(2) Não sei qual defeito o meu veiculo apresenta.")
        escolha = int(input("Digite o número correspondente a opção desejada: "))

    if escolha == 1: #caso usúario saiba o exatamente aonde e quais defeitos o veículo aprensenta
        limpa_terminal()
        print("O seu carro apresenta qual desses defeitos: \n(1) - Sistema de Motor. \n(2) - Sistema de Transmissão. \n(3) - Sistema de Freios. \n(4) - Sistema de Suspensão e Direção. \n(5) - Sistema Elétrico. \n(6) - Sistema de Ar Condicionado e Ventilação. \n(7) - Sistema de Fluidos \n(8) - Sistema de Exaustão")
        escolha = int(input("Digite o número correspondente a opção desejada: "))
        limpa_terminal()
        while escolha < 1 or escolha >= 8: #caso o usuário não inserir a opção correta tera que inserir novamente, até ser uma opção válida
            print("\nOpção inválida, digite novamente!\n")
            print("O seu carro apresenta qual desses defeitos: \n(1) - Sistema de Motor. \n(2) - Sistema de Transmissão. \n(3) - Sistema de Freios. \n(4) - Sistema de Suspensão e Direção. \n(5) - Sistema Elétrico. \n(6) - Sistema de Ar Condicionado e Ventilação. \n(7) - Sistema de Fluidos \n(8) - Sistema de Exaustão")
            escolha = int(input("Digite o número correspondente a opção desejada: ")) 

        if escolha == 1: #opção sistema de motor
            limpa_terminal()
            print("Opção (1) - Sistema de Motor. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p11 = input("O motor está funcionando de forma irregular?")
            p12 = input("Há ruídos incomuns vindos do motor?")
            p13 = input("O veículo está perdendo potência?")
            p14 = input("O motor está superaquecendo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p11)
            lista_problema.append(p12)
            lista_problema.append(p13)
            lista_problema.append(p14)
        elif escolha == 2: #opção Sistema de Transmissão
            limpa_terminal()
            print("Opção (2) - Sistema de Transmissão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p21 = input("Há dificuldades em mudar de marcha?")
            p22 = input("O veículo está tremendo ou vibrando durante a condução?")
            p23 = input("Existe algum vazamento de fluido de transmissão?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p21)
            lista_problema.append(p22)
            lista_problema.append(p23)
        elif escolha == 3: #opção Sistema de Freios
            limpa_terminal()
            print("Opção (3) - Sistema de Freios. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p31 = input("Os freios estão rangendo ou chiando?")
            p32 = input("Há uma sensação de que os freios estão se desgastando rapidamente?")
            p33 = input("Existe alguma dificuldade em parar o veículo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)        
            lista_problema.append(p31)
            lista_problema.append(p32)
            lista_problema.append(p33)
        elif escolha == 4: #opção Sistema de Suspensão e Direção
            limpa_terminal()
            print("Opção (4) - Sistema de Suspensão e Direção. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p41 = input("O veículo está puxando para um lado enquanto dirige?")
            p42 = input("Há algum barulho de rangido ou batida na suspensão?")
            p43 = input("Existe folga excessiva na direção?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p41)
            lista_problema.append(p42)
            lista_problema.append(p43)
        elif escolha == 5: #opção Sistema Elétrico
            limpa_terminal()
            print("Opção (5) - Sistema Elétrico. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p51 = input("Alguma luz de advertência está acesa no painel de instrumentos?")
            p52 = input("Os faróis, luzes de freio e luzes de sinalização estão funcionando corretamente?")
            p53 = input("Há problemas com o sistema de partida do veículo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p51)
            lista_problema.append(p52)
            lista_problema.append(p53)
        elif escolha == 6: #opção Sistema de Ar Condicionado e Ventilação
            limpa_terminal()
            print("Opção (6) - Sistema de Ar Condicionado e Ventilação. \n\nResponda (s/n) essas perguntas para um entendimento breve do problema em seu veículo:")
            p61 = input("O ar condicionado está soprando ar frio?")
            p62 = input("Existe um odor estranho quando o ar condicionado está ligado?")
            p63 = input("Há algum ruído anormal vindo do sistema de ventilação?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p61)
            lista_problema.append(p62)
            lista_problema.append(p63)
        elif escolha == 7: #opção Sistema de Fluidos
            limpa_terminal()
            print("Opção (7) - Sistema de Fluidos. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p71 = input("Existe algum vazamento visível sob o veículo?")
            p72 = input("Os níveis de fluido de óleo, refrigerante e fluido de freio estão dentro das especificações recomendadas?")
            p73 = input("Há alguma contaminação visível nos fluidos?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p71)
            lista_problema.append(p72)
            lista_problema.append(p73)
        elif escolha == 8: #opção Sistema de Exaustão
            limpa_terminal()
            print("Opção (8) - Sistema de Exaustão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p81 = input("Há algum ruído anormal vindo do escapamento?")
            p82 = input("Existe fumaça incomum saindo do escapamento?")
            p83 = input("O veículo está perdendo potência?")
            p84 = input("O veículo está apresentando problemas de emissões?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(escolha)
            lista_problema.append(p81)
            lista_problema.append(p82)
            lista_problema.append(p83)
            lista_problema.append(p84)

    elif escolha == 2:  #caso usúario não saiba exatamente quais e aonde veículo aprensenta defeito
        limpa_terminal()
        print("\nCerto, é necessário que nos diga quais dificuldades estão sendo apresentadas em seu veiculo para um check-up rápido")
        problema = input("Diga quais problemas o/a senhor/a notou em seu veículo: ")
        lista_problema.append(problema)

def unidade_prox():
    limpa_terminal()
    print("Opção (2) -Unidade da Porto Seguro mais próxima.")
    print("\nAs opções de Unidade da Porto Seguro mais próximas de você, são:")
    #exemplo hipotético
    print("CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO \nR PEDROSO, 394 - BELA VISTA - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")
    print("\nCENTRO AUTOMOTIVO - RIO BRANCO \nAV RIO BRANCO, 1448 - CAMPOS ELISEOS - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")
    print("\nCENTRO AUTOMOTIVO - TATUAPÉ TIJUCO PRETO \nR TIJUCO PRETO, 434 - TATUAPÉ - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")

def pecas():
    limpa_terminal()
    print("Opção (3) - Peças automotivas à venda. \n\nEm nosso catalogo de peças contém: \n(1) - Baterias. \n(2) - Pneus. \n(3) - Radiador. \n(4) - Velas de ignição. \n(5) - Faróis. \n(6) - Mangueiras. \n(7) - Correia de distribuição. \n(8) - Bomba de gasolina.")
    escolha = int(input("Digite o número correspondente a opção desejada: "))
    while escolha < 1 or escolha >= 9:
        escolha = int(input("Opção incorreta! Tente novamente: "))
    if escolha == 1:
        print("\nBaterias em nosso estoque: ")
        print("\nBateria moura m60gd mge \nPreço: R$ 419,90")
        print("\nBateria Zetta 60ah Z60d \nPreço: R$ 321,85")
    if escolha == 2:
        print("\nPneus em nosso estoque: ")
        print("\nKit 4 Pneu Pirelli 205/60R16 92H Scorpion Atr Original \nPreço: R$ 1.169,21")
        print("\nPneu Aro 16 205/55R16 Firestone F-600 91V \nPreço: R$ R$ 573,46")
    if escolha == 3:
        print("\nRadiador em nosso estoque: ")
        print("\nRadiador De Agua Do Motor Com Ar Peca Nova Celta 2000 A 2006 Pi0123 \nPreço:R$ 276,36")
        print("\nRadiador De Óleo Universal Com 10 Linhas e Saídas 10an Epman \nPreço: R$ 364,90")
    if escolha == 4:
        print("\nVelas de ignição em nosso estoque: ")
        print("\nJogo De Velas Renault Express 1.6 8v Motor C3l Bpr5ey-d NGK \nPreço: R$ 110,00")
        print("\nJogo 6 Velas Ignição Rural 2.6 12v 1960 1961 1962 1963 1964 Bosch \nPreço:R$ 114,09")
    if escolha == 5:
        print("\nFaróis estoque: ")
        print("\nPar De Faróis Dianteiros Fiat Siena 2008 A 2016 Mopar \nPreço: R$ 1.534,57")
        print("\nPar Farol Fox 2003 2004 2005 2006 2007 2008 2009 Cromado \nPreço: R$ 283,32")
    if escolha == 6:
        print("\nMangueiras em nosso estoque: ")
        print("\nConjunto 8 Mangueiras + 4 Tubos Corsa 1.0 1.4 1.8 2003/2012 \nPreço: R$ 519,99 ")
        print("\nKit 7 Mangueiras + 3 Canos Onix 1.0 1.4 8v Manual 94749565 \nPreço: R$ 309,99")
    if escolha == 7:
        print("\nCorreia de distribuição em nosso estoque: ")
        print("\nKit Distribuição Correia 500 2011/2017 Ks359050 INDISA \nPreço: 159,81")
        print("\nKit Distribuição Correia Clio 2000/2016 Ks959046 INDISA \nPreço: R$ 244,1")
    if escolha == 8:
        print("\nBomba de gasolina em nosso estoque: ")
        print("\nBomba Combustivel Kit Sistema Bosch Gasolina Universal 10107 Euro \nPreço: 76,90")
        print("\nF000te164w Kit Bomba Gasolina Universal Bosch \nPreço:R$ 180,00")

def solicitar_guincho(lista_endereco):
    limpa_terminal()
    print("Opção (3) - Solicitação de Guincho. \n\nInsira sua localização atual:\n") 
    rua = input("Insira a rua: ")
    bairro = input("Insira o bairro: ")
    numero = input("Caso esteja em uma residência, insira o número: ")
    print("Verificaremos se há algum guincho capaz de ir ao indereço do/a senhor/a e mandaremos confirmação no seu e-mail!")
    lista_endereco.append(rua)
    lista_endereco.append(bairro)
    lista_endereco.append(numero)

def adiciona_veiculo(lista_veiculo):
    placa = input("Informe a placa:")
    modelo = input("Informe o modelo:")
    montadora = input("Montadora: ")
    ano = int(input("Ano: "))
    lista_veiculo.append(placa)
    lista_veiculo.append(modelo)
    lista_veiculo.append(montadora)
    lista_veiculo.append(ano)

def altera_veiculo(pos, placa, modelo, montadora, ano, lista):
    if  len(placa) > 0:
        lista[pos+0] = placa
    if len(modelo) > 0:
        lista[pos+1] = modelo
    if len(montadora) > 0:
        lista[pos+2] = montadora
    if len(ano) > 0:
        lista[pos+3] = ano
    

def consulta_veiculo(placa, lista):
    i = 0 
    while i < len(lista) and lista[i] != placa:
        i = i + 4
    if i >= len(lista):
        return -1
    else:
        return i

usuario = []
problema = []
endereco = []
veiculos = []

ac = acess()

if ac == 1:
    cadastro(usuario)
    print(usuario)
else:
    login(usuario)

op = menu()

while op != 8:
    if op == 1:
        check_up(problema)
        print(problema)
        confirm = input('Aperte Enter para confirmar!')
    elif op == 2:
        unidade_prox()
        confirm = input('Aperte Enter para confirmar!')
    elif op == 3:
        pecas()
        confirm = input('Aperte Enter para confirmar!')
    elif op == 4:
        solicitar_guincho(endereco)
        print(endereco)
    elif op == 5:
        adiciona_veiculo(veiculos)
        print(veiculos)
        confirm = input('Aperte Enter para confirmar!')
    elif op == 6:
        placa = input("Placa: ")
        pos = consulta_veiculo(placa, veiculos)
        pos = pos - 1
        if pos < 0:
            print(f"Não existe placa cadastrada!")
        else:
            tipo = input(f"Tipo ({veiculos[pos]}): ")
            placa = input(f"Placa ({veiculos[pos+1]}): ")
            modelo = input(f"Modelo ({veiculos[pos+2]}): ")
            montadora = input(f"Montadora:({veiculos[pos+3]}): ")
            ano = input(f"Ano ({veiculos[pos+4]}): ")
            km = input(f"Km ({veiculos[pos+5]}): ")
            capacidade = input(f"Capacidade ({veiculos[pos+6]}): ")
            altera_veiculo(veiculos, pos, tipo, placa, modelo, montadora, ano, km, capacidade)
        

    elif op == 7:
        placa = input("Placa: ")
        pos = consulta_veiculo(placa, veiculos)
        if pos != -1:
            print(f"Placa : {veiculos[pos-1]}")
            print(f"Modelo : {veiculos[pos]}")
            print(f"Montadora : {veiculos[pos+1]}")
        else:
            print(f"Não existe veículo com a placa {placa}")     
    
    op = menu()

