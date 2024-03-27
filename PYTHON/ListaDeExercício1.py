#2
nome = input("Qual seu nome?")
sonbrenome = input("Qual seu sobrenome?")

print(sonbrenome, nome)

#3
nome = input("Qual seu nome?")
nascimento = input("Qual seu ano de nascimento?")

idade = 2024 - int(nascimento)

print("Em 2024" , nome, " tera", idade ," anos!")

#4
primeiro_numero = input("Escolha um numero: ")
segundo_numero = input("Escolha outro numero: ")

numA = int(primeiro_numero)
numB = int(segundo_numero)

soma = numA + numB
multiplicacao = numA * numB
divisao =  numA / numB
divisao_inteia = numA // numB

print("Soma:",soma,"Multiplicação" ,multiplicacao,"Divisão:",divisao,"Divisão Inteira:", divisao_inteia)

#5
numeA = input("Diga um número:")
numeB = input("Diga outro número:")

x = int(numeA)
y = int(numeB)

elevacao = x ** y
print("Elevação:" ,elevacao)

#6
pi = 3.141592
pergunta = input("Diga qual o raio de um circulo:")
raio = float(pergunta)

area = pi * raio ** 2
perimetro = 2 * pi * raio
print("Area:", area , "Perimetro:" , perimetro)

#7
pergunta = input("Diga um numero de 0 a 99: ")

numero = int(pergunta)

conta1 = numero // 10

conta2 = numero % 10

print('Número de dezenas: ' , conta1,'Número de unidades: ' , conta2)

#8
camisa = int(input("Número de camisas:"))
calca = int(input("Número de calças:"))
sapato = int(input("Número de pares de sapato:"))

conta = camisa * calca * sapato 
print(conta, "Formas diferentes")

#9
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desnconto; "))

valor_desconto = (preco * desconto)/100
novo_valor = preco - valor_desconto
print("Valor total do produto:" , novo_valor)

#10
distancia = float(input("Digite a distância em metros: "))
tempo = float(input("Digite o tempo em seundos: "))

veloc_ms = (distancia / tempo)
veloc_km = ((distancia / tempo)*3.6)

print("Velocidade em m/s:", veloc_ms, "Velocidade em km: ", veloc_km)

#11
salario1 = float(input("Digite seu primeiro salário: "))
salario2 = float(input("Digite seu segundo salário: "))

porcentagem = ((salario2 - salario1)/salario1)*100
print("Salário Inicial:", salario1, "Salário Atual:", salario2, "Porcentagem de aumento:" f"{porcentagem}%")

#12
rm = int(input("Diga seu rm(apenas números): "))
conta1 = rm // 10
conta2 = rm // 100
conta3 = rm // 1000
conta4 = rm // 10000
conta5 = rm // 100000
primeiro_dig = rm % 10
segundo_dig = conta1 % 10
terceiro_dig = conta2 % 10
quarto_dig = conta3 % 10
quinto_dig = conta4 % 10
sexto_dig = conta5 % 10

print("A soma do seu rm é:", sexto_dig + quinto_dig +quarto_dig + terceiro_dig + segundo_dig + primeiro_dig)

#13
nac = float(input("Digite a nota da avaliação NAC:"))
am = float(input("Digite a nota da avaliação AM:"))
ps = float(input("Digite a nota da avaliação PS:"))

media = (2 * nac + 3 + am + 5 * ps)/10

print("Sua média é:", media)

#14
valor_total = float(input("Digite o valor do IPTU: "))
valor_parcela = float(input("Digite o valor de cada parcela: "))

valor_parcelado = valor_parcela * 10
desconto = ((valor_parcelado - valor_total) / valor_parcelado) * 100

print("Seu desconto para pagamento à vista é:", f"{desconto}%")