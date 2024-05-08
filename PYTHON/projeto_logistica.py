#SISTEMA QUE PERMITE O CADASTRAMENTO DE UMA FROTA PARA UMA EMPRESA LOGÍSTICA E FAÇA A ESCOLHA DO VEÍCULO QUE ATENDERÁ A DEMANDA.

#funcionalidade: cadastro de veículo (insere, altera e consulta); agendamento de transporte; 
#os dados serão armazenados em uma ou mais listas

def menu():
    print("1 - insere veículo")
    print("2 - consulta veículo")
    print("3 - altera veículo")
    print("4 - agendamento de transporte de carga")
    print("5 - sair")
    opcao = int(input("Escolha uma opção acima: "))
    while opcao < 1 or opcao > 5:
        opcao = int(input("Erro! Escolha novamente: "))
    return opcao

def insere_veiculo(lista):
    tipo = input("Tipo (vuc, furgão, ônibus ou caminhão): ")
    placa = input("Informe a placa:")
    modelo = input("Informe o modelo:")
    montadora = input("Montadora: ")
    ano = int(input("Ano: "))
    km = int(input("Km: "))
    capacidade = float(input("Capacidade de carga (T): "))
    lista.append(tipo)
    lista.append(placa)
    lista.append(modelo)
    lista.append(montadora)
    lista.append(ano)
    lista.append(km)
    lista.append(capacidade)

def consulta_veiculo(placa, lista):
    i = 0 
    while i < len(lista) and lista[i] != placa:
        i = i + 7
    if i >= len(lista):
        return -1
    else:
        return i

def atualiza_lista(lista, pos, tipo, placa, modelo, montadora, ano, km, capacidade):
    if len(tipo) > 0:
        lista[pos] = tipo
    if  len(placa) > 0:
        lista[pos+1] = placa
    if len(modelo) > 0:
        lista[pos+2] = modelo
    if len(montadora) > 0:
        lista[pos+3] = montadora
    if len(ano) > 0:
        lista[pos+4] = ano
    if len(km) > 0:
        lista[pos+5] =  km
    if len(capacidade) > 0:
        lista[pos+6] =  capacidade

veiculos = []
op = menu()

while op != 5:
    if op == 1:
        insere_veiculo(veiculos)
        print(veiculos)
    elif op == 2:
        placa = input("placa: ")
        pos = consulta_veiculo(placa, veiculos)
        if pos != -1:
            print(f"Tipo : {veiculos[pos-1]}")
            print(f"Tipo : {veiculos[pos]}")
            print(f"Tipo : {veiculos[pos+1]}")

        else:
            print(f"Não existe veículo com a placa {placa}")
    elif op == 3:
        placa = input("Placa: ")
        pos = consulta_veiculo(placa, veiculos)
        pos = pos - 1
        if pos < 0:
            print(f"Não existe placa cadastrada!")
        else:
            tipo = input(f"Tipo ({veiculos[pos]}): ")
            placa = input(f"Placa ({veiculos[pos+1]}): ")
            modelo = input(f"Modelo ({veiculos[pos+2]}): ")
            montadora = input(f"Montadora:({veiculos[pos+3]}): ")
            ano = input(f"Ano ({veiculos[pos+4]}): ")
            km = input(f"Km ({veiculos[pos+5]}): ")
            capacidade = input(f"Capacidade ({veiculos[pos+6]}): ")
            atualiza_lista(veiculos, pos, tipo, placa, modelo, montadora, ano, km, capacidade)

    op = menu()