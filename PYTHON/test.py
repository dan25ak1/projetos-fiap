#3
num1 = float(input("Valor de compras: "))

pix = ((num1 * 10) / 100)
debito = ((num1 * 5) / 100)
vezes2 = num1 / 2
vezes3 = ((num1 * 5) / 100)
vezes4 = ((num1 * 8) / 100) 

print("A vista em dinheiro ou pix: " , num1 - pix , "\nA vista no débito: " , num1 - debito
, "\nEm duas vezes, 2 parcelas de: ", vezes2 , "\nEm três vezes, 3 parcelas de: ", (num1 + vezes3) / 3 , "\nEm quatro vezes, 4 parcelas de: ", (num1 + vezes4) / 4)

#teste
