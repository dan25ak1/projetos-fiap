import os

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
    os.system('cls')
    print("Bem-vindo ao menu da Assistência Veicular da Porto Seguro! \nInforme o número da opção desejada.")
    print("(1) - Fazer um check-up no veículo")
    print("(2) - Qual unicade da Porto mais próxima a mim")
    print("(3) - Estou precisando de uma peça")
    print("(4) - Solicitação de guincho")
    print("(5) - Adicionar veículo")
    print("(6) - Alterar veículo")
    print("7) - Sair")
    escolha = int(input("Digite o número correspondente a opção desejada: "))
    while escolha < 1 or escolha > 7:
        escolha = int(input("Opção incorreta! Tente novamente: "))
    return escolha

def check_up(lista_problema):
    os.system('cls')
    print("Opção (1) - Fazer um check-up no veículo. \n\nSabe qual defeito o veiculo apresenta? ") 
    print("(1) Já sabe qual é o defeito.")
    print("(2) Não sei qual defeito o meu veiculo apresenta.")
    escolha = int(input("Digite o número correspondente a opção desejada: "))
    while escolha < 1 or escolha >= 3: #caso o usuário não inserir a opção correta tera que inserir novamente, até ser uma opção válida
        os.system('cls')
        print("\nOpção inválida, digite novamente!\n")
        print("Opção (1) - Defeito no veículo selecionada. \n\nSabe qual defeito o veiculo apresenta? ") 
        print("(1) Já sabe qual é o defeito.")
        print("(2) Não sei qual defeito o meu veiculo apresenta.")
        escolha = int(input("Digite o número correspondente a opção desejada: "))

    if escolha == 1: #caso usúario saiba o exatamente aonde e quais defeitos o veículo aprensenta
        os.system('cls')
        print("O seu carro apresenta qual desses defeitos: \n(1) - Sistema de Motor. \n(2) - Sistema de Transmissão. \n(3) - Sistema de Freios. \n(4) - Sistema de Suspensão e Direção. \n(5) - Sistema Elétrico. \n(6) - Sistema de Ar Condicionado e Ventilação. \n(7) - Sistema de Fluidos \n(8) - Sistema de Exaustão")
        escolha = int(input("Digite o número correspondente a opção desejada: "))
        os.system('cls')
        while escolha < 1 or escolha >= 8: #caso o usuário não inserir a opção correta tera que inserir novamente, até ser uma opção válida
            print("\nOpção inválida, digite novamente!\n")
            print("O seu carro apresenta qual desses defeitos: \n(1) - Sistema de Motor. \n(2) - Sistema de Transmissão. \n(3) - Sistema de Freios. \n(4) - Sistema de Suspensão e Direção. \n(5) - Sistema Elétrico. \n(6) - Sistema de Ar Condicionado e Ventilação. \n(7) - Sistema de Fluidos \n(8) - Sistema de Exaustão")
            escolha = int(input("Digite o número correspondente a opção desejada: ")) 

        if escolha == 1: #opção sistema de motor
            os.system('cls')
            print("Opção (1) - Sistema de Motor. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p11 = input("O motor está funcionando de forma irregular?")
            p12 = input("Há ruídos incomuns vindos do motor?")
            p13 = input("O veículo está perdendo potência?")
            p14 = input("O motor está superaquecendo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p11)
            lista_problema.append(p12)
            lista_problema.append(p13)
            lista_problema.append(p14)
        elif escolha == 2: #opção Sistema de Transmissão
            os.system('cls')
            print("Opção (2) - Sistema de Transmissão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p21 = input("Há dificuldades em mudar de marcha?")
            p22 = input("O veículo está tremendo ou vibrando durante a condução?")
            p23 = input("Existe algum vazamento de fluido de transmissão?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p21)
            lista_problema.append(p22)
            lista_problema.append(p23)
        elif escolha == 3: #opção Sistema de Freios
            os.system('cls')
            print("Opção (3) - Sistema de Freios. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p31 = input("Os freios estão rangendo ou chiando?")
            p32 = input("Há uma sensação de que os freios estão se desgastando rapidamente?")
            p33 = input("Existe alguma dificuldade em parar o veículo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")        
            lista_problema.append(p31)
            lista_problema.append(p32)
            lista_problema.append(p33)
        elif escolha == 4: #opção Sistema de Suspensão e Direção
            os.system('cls')
            print("Opção (4) - Sistema de Suspensão e Direção. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p41 = input("O veículo está puxando para um lado enquanto dirige?")
            p42 = input("Há algum barulho de rangido ou batida na suspensão?")
            p43 = input("Existe folga excessiva na direção?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p41)
            lista_problema.append(p42)
            lista_problema.append(p43)
        elif escolha == 5: #opção Sistema Elétrico
            os.system('cls')
            print("Opção (5) - Sistema Elétrico. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p51 = input("Alguma luz de advertência está acesa no painel de instrumentos?")
            p52 = input("Os faróis, luzes de freio e luzes de sinalização estão funcionando corretamente?")
            p53 = input("Há problemas com o sistema de partida do veículo?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p51)
            lista_problema.append(p52)
            lista_problema.append(p53)
        elif escolha == 6: #opção Sistema de Ar Condicionado e Ventilação
            os.system('cls')
            print("Opção (6) - Sistema de Ar Condicionado e Ventilação. \n\nResponda (s/n) essas perguntas para um entendimento breve do problema em seu veículo:")
            p61 = input("O ar condicionado está soprando ar frio?")
            p62 = input("Existe um odor estranho quando o ar condicionado está ligado?")
            p63 = input("Há algum ruído anormal vindo do sistema de ventilação?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p61)
            lista_problema.append(p62)
            lista_problema.append(p63)
        elif escolha == 7: #opção Sistema de Fluidos
            os.system('cls')
            print("Opção (7) - Sistema de Fluidos. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p71 = input("Existe algum vazamento visível sob o veículo?")
            p72 = input("Os níveis de fluido de óleo, refrigerante e fluido de freio estão dentro das especificações recomendadas?")
            p73 = input("Há alguma contaminação visível nos fluidos?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p71)
            lista_problema.append(p72)
            lista_problema.append(p73)
        elif escolha == 8: #opção Sistema de Exaustão
            os.system('cls')
            print("Opção (8) - Sistema de Exaustão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
            p81 = input("Há algum ruído anormal vindo do escapamento?")
            p82 = input("Existe fumaça incomum saindo do escapamento?")
            p83 = input("O veículo está perdendo potência?")
            p84 = input("O veículo está apresentando problemas de emissões?")
            print("Processaremos todas suas respostas, e tentaremos encontrar um possível problema")
            lista_problema.append(p81)
            lista_problema.append(p82)
            lista_problema.append(p83)
            lista_problema.append(p84)

    elif escolha == 2:  #caso usúario não saiba exatamente quais e aonde veículo aprensenta defeito
        os.system('cls')
        print("\nCerto, é necessário que nos diga quais dificuldades estão sendo apresentadas em seu veiculo para um check-up rápido")
        problema = input("Diga quais problemas o/a senhor/a notou em seu veículo: ")
        lista_problema.append(problema)

def unidade_prox():
    os.system('cls')
    print("Opção (2) -Unidade da Porto Seguro mais próxima.")
    print("\nAs opções de Unidade da Porto Seguro mais próximas de você, são:")
    #exemplo hipotético
    print("CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO \nR PEDROSO, 394 - BELA VISTA - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")
    print("\nCENTRO AUTOMOTIVO - RIO BRANCO \nAV RIO BRANCO, 1448 - CAMPOS ELISEOS - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")
    print("\nCENTRO AUTOMOTIVO - TATUAPÉ TIJUCO PRETO \nR TIJUCO PRETO, 434 - TATUAPÉ - SAO PAULO \nATENDIMENTO: DE SEG. A SEX. DAS 08:00 ÀS 18:00, SÁB. DAS 08:00 ÀS 12:00, EXCETO DOM. E FERIADOS")




usuario = []
ac = acess()

if ac == 1:
    cadastro(usuario)
    print(usuario)
else:
    login(usuario)

op = menu()

while op != 7:
    if op == 1:
        problema = []
        check_up(problema)
        print(problema)
        confirm = input('Aperte Enter para confirmar!')
    if op == 2:
        unidade_prox()
        confirm = input('Aperte Enter para confirmar!')
    


    
   

