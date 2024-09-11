def cadastro(lista: list):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    cep = (input("Digite seu cep: "))
    senha = input("Crie uma senha: ")
    conf_senha = input("Confirme a senha: ")
    while senha != conf_senha:
        print("\nNão foram fornecidas senhas idênticas!\n")
        conf_senha = input("Confirme a senha: ")
    print("Conta criada com sucesso!")
    lista.append(nome)
    lista.append(email)
    lista.append(cep)
    lista.append(senha)

def busca(lista: list, nome: str) -> int:
    for i in range(len(lista)):
        if list[i][0] == nome:
            return i
    return -1

def excluir(lista):
    nome = input("Nome: ")
    pos = busca(lista, nome)
    if pos == -1:
        print("Nenhuma peça encontrada")
    else:
        info = lista.pop(pos)
        print(info)
        print("Foi excluída com sucesso!")

usuario = []
while True:
    cadastro(usuario)
    excluir(usuario)
    print(usuario)