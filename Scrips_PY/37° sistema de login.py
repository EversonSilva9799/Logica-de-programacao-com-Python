print('SISTEMA DE LOGIN E ESQUECI MINHA SENHA')
banco_nome = ['Alcides','Lurdinha','Everson','Emile','Kemile']
usuarioSenha = {"Alcides": 123, "Lurdinha": 6253, "Everson": 7458, "Emile": 9527, "Kemile": 3495}
banco_senha = ['1252','6253','7458','9527','3495']
banco_email = ['Alcides123@gmail.com','Ludrinha123@gmail.com','everson123@gmail.com','emile123@gmail.com','kemile123@gmail.com']
banco_codigo_verificador = ['sddf','454f','453gb','124f','hdc8']
entrou = False

print('Para fazer login informe o usuário e senha!')

for i in range(3):
    login = input('Digite o nome do usuário: ')
    senha = input('Informe sua senha: ')
    if login in banco_nome and senha in banco_senha[banco_nome.index(login)]:
        print('Acesso liberado!')
        entrou = True
        break
    else:
        print('Nome de usuário ou senha errados')
        continue
    print('Número de tentativas excedeu o limite')
    if entrou == True:
        break
    else:

        lembra = input('Esqueceu a senha? [s/n] ')
        while True:
            if lembra.lower() == 's':
                email = input('Digite seu email cadastrado no sistema: ')
                if email in banco_email:
                    posicao = banco_email.index(email)
                    banco_nome[posicao] = input('Digite o novo nome de usuário: ')
                    banco_senha[posicao] = input('Digite a nova senha de usuário:')
            else:
                 print('Email não encontado no sistema!')
                 cont = input('Deseja continua? [s/n] ')
                 if cont.lower() == 's':
                     continue
                 else:
                     print('Programa finalizado!')
                     break

