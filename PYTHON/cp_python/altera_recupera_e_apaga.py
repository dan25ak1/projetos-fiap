import banco

#def_altera
mensagem = {'id': 20, 'assunto': 'Reunião Reagendada', 'destinatario': 'César', 'remetente': 'Eliana', 'conteudo': 'A reunião de amanhã foi remarcada para depois de amanhã (08/10/24)'}
banco.altera(mensagem)
print(f"Mensagem com ID {mensagem['id']} alterada com sucesso!")

#def_recupera
id_mensagem = 1
mensagem = banco.recupera(id_mensagem)
print(f"Mensagem com ID {id_mensagem}:")
print(mensagem)

#def_recupera_assunto
assunto = 'Reunião de Projeto'
mensagens = banco.recupera_assunto(assunto)
print(f"Mensagens com assunto '{assunto}':")
for mensagem in mensagens:
    print(mensagem)

#def_recupera_destinatario
destinatario = 'Thiago'
mensagens = banco.recupera_destinatario(destinatario)
print(f"Mensagens para destinatário '{destinatario}':")
for mensagem in mensagens:
    print(mensagem)

#def_apaga
id_mensagem = 19
banco.apaga(id_mensagem)
print(f"Mensagem com ID {id_mensagem} apagada com sucesso!")




