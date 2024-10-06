import banco


mensagens = [
    {'assunto': 'Reunião de Projeto', 'destinatario': 'Lucas', 'remetente': 'Mariana', 'conteudo': 'Precisamos agendar uma reunião para discutir os próximos passos do projeto.'},
    {'assunto': 'Parabéns pela Promoção!', 'destinatario': 'Thiago', 'remetente': 'Amanda', 'conteudo': 'Parabéns pela sua promoção! Você merece todo o sucesso.'},
    {'assunto': 'Atualização do Sistema', 'destinatario': 'João', 'remetente': 'Beatriz', 'conteudo': 'O sistema será atualizado amanhã às 20h. Por favor, esteja preparado.'},
    {'assunto': 'Convite para Evento', 'destinatario': 'Rafael', 'remetente': 'Larissa', 'conteudo': 'Gostaria de convidá-lo para o evento que acontecerá na próxima semana.'},
    {'assunto': 'Relatório Semanal', 'destinatario': 'Pedro', 'remetente': 'Camila', 'conteudo': 'Segue anexo o relatório semanal com os dados atualizados.'},
    {'assunto': 'Planejamento da Viagem', 'destinatario': 'Felipe', 'remetente': 'Carolina', 'conteudo': 'Precisamos discutir o planejamento da nossa viagem no mês que vem.'},
    {'assunto': 'Feedback sobre o Trabalho', 'destinatario': 'Bruno', 'remetente': 'Fernanda', 'conteudo': 'Seu trabalho foi excelente, parabéns pela dedicação.'},
    {'assunto': 'Feliz Aniversário!', 'destinatario': 'Guilherme', 'remetente': 'Isabela', 'conteudo': 'Feliz aniversário! Que seu dia seja repleto de alegrias.'},
    {'assunto': 'Pedido de Ajuda', 'destinatario': 'Leonardo', 'remetente': 'Vanessa', 'conteudo': 'Estou precisando de ajuda com aquele projeto, podemos conversar?'},  
    {'assunto': 'Lembrete: Reunião de Equipe', 'destinatario': 'Gabriel', 'remetente': 'Julia', 'conteudo': 'Lembre-se que amanhã temos uma reunião importante com a equipe.'},
    {'assunto': 'Confraternização de Fim de Ano', 'destinatario': 'Daniel', 'remetente': 'Luiza', 'conteudo': 'Você está convidado para a confraternização de fim de ano da empresa.'},
    {'assunto': 'Orientações para o Novo Projeto', 'destinatario': 'Eduardo', 'remetente': 'Sofia', 'conteudo': 'Aqui estão as orientações para o início do novo projeto.'},
    {'assunto': 'Boas Festas!', 'destinatario': 'Matheus', 'remetente': 'Letícia', 'conteudo': 'Desejo a você e sua família um ótimo final de ano e boas festas!'},
    {'assunto': 'Agradecimento pelo Suporte', 'destinatario': 'André', 'remetente': 'Patrícia', 'conteudo': 'Muito obrigado pelo suporte que você me deu no último projeto.'},
    {'assunto': 'Mudança de Horário', 'destinatario': 'Rodrigo', 'remetente': 'Aline', 'conteudo': 'Houve uma mudança no horário da reunião. Ela será às 14h.'},
    {'assunto': 'Confirmação de Inscrição', 'destinatario': 'Henrique', 'remetente': 'Mônica', 'conteudo': 'Sua inscrição no curso foi confirmada com sucesso.'},
    {'assunto': 'Entrega de Documentos', 'destinatario': 'Vinícius', 'remetente': 'Tatiana', 'conteudo': 'Por favor, não esqueça de entregar os documentos até sexta-feira.'},
    {'assunto': 'Nova Tarefa Designada', 'destinatario': 'Diego', 'remetente': 'Carla', 'conteudo': 'Foi designada uma nova tarefa para você, consulte o sistema.'},
    {'assunto': 'Confirmação de Envio', 'destinatario': 'Ricardo', 'remetente': 'Ana', 'conteudo': 'Confirmamos o envio dos materiais solicitados, eles chegarão em breve.'},
    {'assunto': 'Reunião Cancelada', 'destinatario': 'César', 'remetente': 'Eliana', 'conteudo': 'A reunião de amanhã foi cancelada, entraremos em contato para reagendar.'}
]

for mensagem in mensagens:
    banco.inclui(mensagem)

print("Mensagens inseridas com sucesso!")