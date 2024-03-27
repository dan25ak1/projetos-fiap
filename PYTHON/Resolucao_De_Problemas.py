valor = input("Digite um número: ")
numA = int(valor)
valor = input("Digite um número: ")
numB = int(valor)
valor = input("Digite um número: ")
numC = int(valor)
valor = input("Digite um número: ")
numD = int(valor)
valor = input("Digite um número: ")
numE = int(valor)

soma = numA + numB + numC + numD + numE

print(soma)

#problema_2.1 segunda versão:

soma = 0

while True:
    valor = input("Digite um numero: ")
    num = int(valor)
    soma = soma + num
    print(soma)

#problema 3.1
    
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Esse número é par!")

else:
    print("Esse número é impar!")

#solução com elif:
    
    placarA = int(input("Gols do time A: "))
    placarB = int(input("Gols do time B: "))

    if placarA < placarB:
        print("Time B venceu!")
    elif placarA > placarB: 
        print("Time A venceu!")
    else:
        print("Empate!")

#problema 3.2

num = int(input("Digite um número: "))
if num > 0 :
    print(str(num) + " é positivo!")
elif num < 0:
    print(str(num) + " é negativo!")
else:
    print(str(num) + " é ugual a zero!")

#problema 3.3
    
numA = (input("Digite um número: "))
op = input("Escolha o operador (+,-,*,/): ")
numB = (input("Escolha outro número: "))

if op == "+":
    resultado = numA + numB
elif op == "-":
    resultado = numA - numB
elif op == "*":
    resultado = numA * numB
elif op == "/":
    resultado = numA / numB

print("Resposta: {}".format(resultado))

