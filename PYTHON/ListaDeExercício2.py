#1
numA = float(input("Digite um número: "))

if numA > 10:
    print("Esse número é maior que 10")
else:
    print("Esse número é menor que 10")

#2
numA = int(input("Digite um número inteiro: "))
numB = int(input("Digite outro número inteiro: "))    

if numA < numB:
    print(numB , "é maior que" , numA)
elif numA > numB:
    print(numA , "é maior que" , numB)
else:
    print("Os dois números tem o mesmo valor")

#3
time1 = input("Nome do time 1: ")
time2 = input("Nome do time 2: ")
placarA = int(input(f"Gols do {time1}: "))
placarB = int(input(f"Gols do {time2}: "))

if placarA < placarB:
    print(time2 , "venceu!")
elif placarA > placarB: 
    print(time1 , "venceu!")
else:
    print("Empate!")

#4
dias_uteis = int(input("Dias úteis: "))
horas_trabalhadas = int(input("Digite quantas horas trabalhar por dia: "))
sal_hora = int(input("Quanto recebe por hora: "))

jornada_padrao = dias_uteis * 8 

if jornada_padrao < horas_trabalhadas: 
    #tenho hora extra para calcular
    hora_extra = horas_trabalhadas - jornada_padrao
    valor_extra = hora_extra * sal_hora * 1.5
    salario_total = jornada_padrao * sal_hora + valor_extra
    print("Valor hora-extra", valor_extra)

else:
    salario_total = horas_trabalhadas * sal_hora

print("Salario total: ", salario_total)

#5
num1 = int(input("Escolha um número: "))


#6
import math

numero = float(input("Informe um número: "))

if numero < 0:
    print(f"Impossível extrair raiz quadrada de {numero}")
    print("Impossível extrair raiz quadrada de ", numero)
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz:.4f}")
    print("A raiz quadrada de ", numero, " é ", raiz)

#7
idade = int(input("Informe a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria Infantil")
elif idade >= 8 and idade <= 10:
    print("Categoria Juvenil")
elif idade >= 11 and idade <= 15:
    print("Categoria Adolescente")
elif idade >= 16 and idade <= 30:
    print("Categoria Adulto")
elif idade >= 30:
    print("Categoria Senior")
else:
    print("Idade Inválida")

#8
numA = float((input("Digite um número: ")))
op = input("Escolha o operador (+,-,*,/): ")
numB = float((input("Escolha outro número: ")))

if op == "+":
    resultado = numA + numB
elif op == "-":
    resultado = numA - numB
elif op == "*":
    resultado = numA * numB
elif op == "/":
    if numB != 0:
        resultado = numA / numB
    else:
        print("Impossível dividir por 0")
        quit() #em java system.exit(0);

print("Resposta: {}".format(resultado))

#9
import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("Não é equação de 2 grau")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Não tenho raízes reais!")
    else:
        x1 = (-b + math.sqrt(delta) / (2 * a))
        x2 = (-b - math.sqrt(delta) / (2 * a))
        print(f"As raízes da equação são {x1} e {x2}")

#10
valor = float(input("Informe o valor total: "))

forma_pgto = int(input("Informe a forma de pgto (1-4): "))

if forma_pgto == 1:
    valor = valor - valor * 0.1
    print(f"Valor a ser pago {valor}")
elif forma_pgto == 2:
    valor = valor - valor * 0.05
    print(f"Valor a ser pago: {valor}")
elif forma_pgto == 3:
    parcela = valor / 2
    print(f"Em 2x {parcela}")
elif forma_pgto == 4:
    valor = valor + valor * 0.07
    parcela = valor / 4
    print(f"Sua compraa saiu {valor} em 4x de {parcela}")
else:
    print("Forma de pagamento inválida!")

#11
media1 = float(input("Média do primeiro bimestre: "))
media2 = float(input("Média do segundo bimestre: "))
aulas_totais = int(input("Número de aulas ministradas: "))
aulas_assistidas = int(input("Número de aulas aassistidas: "))
media_final = (media1 * 4 + media2 * 6) / 10
presenca = (aulas_assistidas * 100) / aulas_totais

if media_final >= 6 and presenca >= 70:
    print("Aprovado")
elif media_final >= 6 and presenca < 70:
    print("Reprovado")
elif media_final >= 3 or media_final <= 5.9:
    print("Exame")
else:
    print("Reprovado")

#12
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
 
if dia < 1 or dia > 31:
    print("Data invalida")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
elif mes == 2 and dia > 28:
    print("Data inválida")
else:
    print("Data válida!")

#13 
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
 
if dia < 1 or dia > 31:
    print("Data invalida")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
elif mes == 2 and dia > 28:
    if dia == 29 and ano % 400 == 0:
        print("Data inválida")
    elif dia == 29 and ano % 4 == 0 and ano % 100 != 0:
        print("Data válida")
    else:
        print("Data invalida")
else:
    print("Data válida!")

