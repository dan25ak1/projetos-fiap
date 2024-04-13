num = int(input("Escreva um número decimal: "))
resultado = ''

while num != 0:
    resto = num % 16
    num = num // 16
    resultado = str(resto) + resultado 
    if resultado == "10":
        resultado = "A"
    elif resultado == "11":
        resultado = "B"
    elif resultado == "12":
        resultado = "C"
    elif resultado == "13":
        resultado = "D"
    elif resultado == "14":
        resultado = "E"
    elif resultado == "15":
        resultado = "F"
print(resultado)



