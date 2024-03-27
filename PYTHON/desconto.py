#entrada de dados : preço e o percentual de desconto
aux = input('Preço: ')

#existe funcoes  que convertem uma string em numero: real ou int
preco = float(aux)

aux = input('Desconto: ')
desconto = float(aux)

valor_desconto = preco * desconto / 100
novo_preco = preco - valor_desconto

print("O valor do produto será de:", novo_preco)

print(f"O valor do produto sera de {novo_preco}")