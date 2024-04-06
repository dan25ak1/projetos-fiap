#6
nota = int(input("Informe a nota: "))
maior = nota
menor = nota
contador = 1
quant_aluno = 20

while True:
    nota = int(input("Informe a nota: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    contador = contador + 1

print(f"A maior nota é {maior} e a menor é {menor}")

#10
n = int(input("Digite um número inteiro positivo: "))

contador = 1
i=1
while i <= n:
    contador = contador * i
    i = i + 1
