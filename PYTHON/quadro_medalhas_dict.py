quadro = {
    "china": [18, 20, 15]
    "EUA": [8, 6, 5]
    "Brasil": [4, 9, 6]
}

pais = ""
while pais != "Sair":
    pais = input("Pais: ")
    cor_medalha = input("Informe a medalha: ")
    if cor_medalha == "ouro":
        pos = 0
    elif cor_medalha == "prata":
        pos = 1
    else:
        pos = 2

    registro = [0, 0, 0]
    if pais inf quadro:
        #registro = quadro.get(pais)
        quadro[pais]
    registro[pos] = registro[pos] + 1
    quadro[pais] = registro
    print(quadro)