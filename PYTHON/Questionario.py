nome = input("Nome?")
idade = input("Qual a sua idade?")
curso_superior = input("Já fez algum curso superior? Qual?")
escolha = input("Por quê escolheu TI?")
area = input("Área que deseja trabalhar?")
hobbies = input("Quais são os seus hobbies?")

arq = open("resp.txt", "w")
arq.write(f"{nome}|{idade}|{curso_superior}|{escolha}|{area}|{hobbies}")

arq.close()