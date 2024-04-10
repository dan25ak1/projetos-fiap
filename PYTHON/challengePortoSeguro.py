import os
escolha = 0
while escolha != 1 or escolha !=2:
    print("Bem-vindo à Assistência Veicular da Porto Seguro! \nInforme o número da opção desejada. ")
    print("(1) - Cadastrar")
    print("(2) - Login")
    escolha = int(input("Digite o número correspondente a opção desejada:"))
    senha = "1"
    conf_senha = "0"

    if escolha == 1:
        email = input("Digite seu e-mail: ")
        cep = int(input("Digite seu cep: ")) #validar
        while senha != conf_senha:
            senha = input("Crie uma senha: ")
            conf_senha = input("Confirme a senha: ")
            if senha != conf_senha:
                print("As senhas não correspondem. Por favor, tente novamente.")
        print("Conta criada com sucesso!")
        os.system('cls')

    elif escolha == 2:
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        os.system('cls')

    else:
        print("\nOpção inválida, digite novamente!\n")
        os.system('cls')

    while escolha == 1 or escolha == 2:
        os.system('cls')
        print("Bem-vindo ao menu da Assistência Veicular da Porto Seguro! \nInforme o número da opção desejada.")
        print("(1) - Meu carro quebrou: ")
        print("(2) - Qual a Unidade da Porto Seguro mais próxima a mim: ")
        print("(3) - Estou precisando de uma peça:  ")
        escolha = int(input("Digite o número correspondente a opção desejada: "))

            if escolha == 1:
                os.system('cls')
                print("Opção (1) - Defeito no veículo selecionada. \n\nSabe qual defeito o veiculo apresenta? ") 
                print("(1) Já sabe qual é o defeito.")
                print("(2) Não sei qual defeito o meu veiculo apresenta.")
                escolha = int(input("Digite o número correspondente a opção desejada: "))
            
                while escolha == 1:
                    os.system('cls')
                    if escolha == 1:
                        os.system('cls')
                        print("O seu carro apresenta qual desses defeitos: \n(1) - Sistema de Motor. \n(2) - Sistema de Transmissão. \n(3) - Sistema de Freios. \n(4) - Sistema de Suspensão e Direção. \n(5) - Sistema Elétrico. \n(6) - Sistema de Ar Condicionado e Ventilação. \n(7) - Sistema de Fluidos \n(8) - Sistema de Exaustão")
                        escolha = int(input("Digite o número correspondente a opção desejada: "))

                        if escolha == 1:
                            os.system('cls')
                            print("Opção (1) - Sistema de Motor. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p11 = input("O motor está funcionando de forma irregular?")
                            p12 = input("Há ruídos incomuns vindos do motor?")
                            p13 = input("O veículo está perdendo potência?")
                            p14 = input("O motor está superaquecendo?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 2:
                            os.system('cls')
                            print("Opção (2) - Sistema de Transmissão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p21 = input("Há dificuldades em mudar de marcha?")
                            p22 = input("O veículo está tremendo ou vibrando durante a condução?")
                            p23 = input("Existe algum vazamento de fluido de transmissão?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 3:
                            os.system('cls')
                            print("Opção (3) - Sistema de Freios. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p31 = input("Os freios estão rangendo ou chiando?")
                            p32 = input("Há uma sensação de que os freios estão se desgastando rapidamente?")
                            p33 = input("Existe alguma dificuldade em parar o veículo?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 4:
                            os.system('cls')
                            print("Opção (4) - Sistema de Suspensão e Direção. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p41 = input("O veículo está puxando para um lado enquanto dirige?")
                            p42 = input("Há algum barulho de rangido ou batida na suspensão?")
                            p43 = input("Existe folga excessiva na direção?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 5:
                            os.system('cls')
                            print("Opção (5) - Sistema Elétrico. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p51 = input("Alguma luz de advertência está acesa no painel de instrumentos?")
                            p52 = input("Os faróis, luzes de freio e luzes de sinalização estão funcionando corretamente?")
                            p53 = input("Há problemas com o sistema de partida do veículo?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 6:
                            os.system('cls')
                            print("Opção (6) - Sistema de Ar Condicionado e Ventilação. \n\nResponda (s/n) essas perguntas para um entendimento breve do problema em seu veículo:")
                            p61 = input("O ar condicionado está soprando ar frio?")
                            p62 = input("Existe um odor estranho quando o ar condicionado está ligado?")
                            p63 = input("Há algum ruído anormal vindo do sistema de ventilação?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 7:
                            os.system('cls')
                            print("Opção (7) - Sistema de Fluidos. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p71 = input("Existe algum vazamento visível sob o veículo?")
                            p72 = input("Os níveis de fluido de óleo, refrigerante e fluido de freio estão dentro das especificações recomendadas?")
                            p73 = input("Há alguma contaminação visível nos fluidos?")
                            guincho = input("É necessário guincho para a busca do veículo?")
                        elif escolha == 8:
                            os.system('cls')
                            print("Opção (8) - Sistema de Exaustão. \n\nResponda essas perguntas (s/n) para um entendimento breve do problema em seu veículo:")
                            p81 = input("Há algum ruído anormal vindo do escapamento?")
                            p82 = input("Existe fumaça incomum saindo do escapamento?")
                            p83 = input("O veículo está perdendo potência?")
                            p84 = input("O veículo está apresentando problemas de emissões?")
                            guincho = input("É necessário guincho para a busca do veículo?")

                            if guincho == "S" or guincho == "s":
                                print("Certo, temos uma noção breve do problema em seu veículo. Será mandado um e-mail para confirmar a ida do guincho a sua residência. Obrigado pela preferência!")
                                input('')
                            elif guincho == "N" or guincho == "n":
                                os.system('cls')
                                print("Leve seu carro a uma Unidade da Porto Seguro e apresente o email enviado de confirmação")
                                print("As opções de Unidade da Porto Seguro mais próximas de você, são:")
                                input('')
                            else:
                                print("\nOpção inválida, digite novamente!\n")
                                input('')
                                os.system('cls')

                while escolha == 1:    
                    os.system('cls')
                    print("\nCerto, é necessário que nos diga quais dificuldades estão sendo apresentadas em seu veiculo para um check-up rápido")
                    problema = input("Diga quais problemas o/a senhor/a notou em seu veículo: ")
                    guincho = input("É necessário guincho para a busca do veículo?")
                    if guincho == "S" or guincho == "s":
                        print("Certo, temos uma noção breve do problema em seu veículo. Será mandado um e-mail para confirmar a ida do guincho a sua residência. Obrigado pela preferência!")
                        input('')
                    elif guincho == "N" or guincho == "n":
                        os.system('cls')
                        print("Leve seu carro a uma Unidade da Porto Seguro e apresente o email enviado de confirmação")
                        print("As opções de Unidade da Porto Seguro mais próximas de você, são:")
                        input('')
                    else:
                        print("\nOpção inválida, digite novamente!\n")
                        input('')
                        os.system('cls')
            
            elif escolha == 2:
                os.system('cls')
                print("Opção (2) -Unidade da Porto Seguro mais próxima.")
                print("As opções de Unidade da Porto Seguro mais próximas de você, são:")
                ##direcionar para pagina de unidades mais próximas

            elif escolha == 3:
                os.system('cls')
                print("Opção (3) - Peças automotivas à venda. \n\nEm nosso catalogo de peças contém: \n(1) - Baterias. \n(2) - Pneus. \n(3) - Radiador. \n(4) - Velas de ignição. \n(5) - Faróis. \n(6) - Mangueiras. \n(7) - Correia de distribuição. \n(8) - Bomba de gasolina.")
                escolha = int(input("Digite o número correspondente a opção desejada: "))
                #colocar opções de produtos
                #validação de respostas

        else:
            print("\nOpção inválida, digite novamente!\n")
            confirm = input('')
            os.system('cls')
            
            