#1
num1 = float(input("Digite um número real: "))
num2 = float(input("Digite um número real novamente: "))
num3 = float(input("Digite um número real novamente: "))
num4 = float(input("Digite um número real novamente: "))
media_aritmetrica = (num1 + num2 + num3 + num4) / 4
media_geometrica = (num1 * num2 * num3 * num4) ** 0.25


if num1 == 0 or num2 < 0:
    print("Média aritmétrica: ", media_aritmetrica)
elif num2 == 0 or num2 < 0:
    print("Média aritmétrica: ", media_aritmetrica)
elif num3 == 0 or num3 < 0:
    print("Média aritmétrica: ", media_aritmetrica)
elif num4 == 0 or num4 < 0:
    print("Média aritmétrica: ", media_aritmetrica)
else:
    print("Média geométrica: ", media_geometrica)

#2
num1 = float(input("Consumo mensal do mês passado: "))
num2 = float(input("Consumo mensal do mês atual: "))
desconto = (num2 - 1) - (((num2 * 15) / 100))

if num1 > num2:
    if num2 > 0 and num2 <= 20:
        valor_consumo = num2 * 2
        multa = ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor do desconto:", desconto , "\nTotal da conta:", valor_consumo - desconto)
    elif num2 > 20 and num2 <= 35:
        valor_consumo = num2 * 3.5
        multa = valor_consumo + ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor do desconto:", desconto , "\nTotal da conta:", valor_consumo - desconto)
    elif num2 > 35 and num2 <= 50:
        valor_consumo = num2 * 5.5
        multa = valor_consumo + ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor do desconto:", desconto , "\nTotal da conta:", valor_consumo - desconto)
    elif num2 > 50:
        valor_consumo = num2 * 7
        multa = valor_consumo + ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor do desconto:", desconto , "\nTotal da conta:", valor_consumo - desconto)
else:
    if num2 > 0 and num2 <= 20:
        valor_consumo = num2 * 2
        multa = ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor da multa:", multa , "\nTotal da conta:", valor_consumo + multa)
    elif num2 > 20 and num2 <= 35:
        valor_consumo = num2 * 3.5
        multa = ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor da multa:", multa , "\nTotal da conta:", valor_consumo + multa)
    elif num2 > 35 and num2 <= 50:
        valor_consumo = num2 * 5.5
        multa = ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor da multa:", multa , "\nTotal da conta:", valor_consumo + multa)
    elif num2 > 50:
        valor_consumo = num2 * 7
        multa = ((valor_consumo * 10) / 100)
        print("Valor do consumo:" , valor_consumo , "\nValor da multa:", multa , "\nTotal da conta:", valor_consumo + multa)

#3
num1 = float(input("Valor da compra: "))

pix = ((num1 * 10) / 100)
debito = ((num1 * 5) / 100)
vezes2 = num1 / 2
vezes3 = ((num1 * 5) / 100)
vezes4 = ((num1 * 10) / 100) 

print("A vista em dinheiro ou pix: " , num1 - pix , "\nA vista no débito: " , num1 - debito
, "\nEm duas vezes, 2 parcelas de: ", vezes2 , "\nEm três vezes, 3 parcelas de: ", (num1 + vezes3) / 3 , "\nEm quatro vezes, 4 parcelas de: ", (num1 + vezes4) / 4)
