print('CADASTRO')
login_cadastro = input('Informe um nome de usuário: ')
senha_cadastro = int(input('Informe uma senha numérica de 4 dígitos: '))
print('==============================')
print('VOCÊ SE CADASTROU COM SUCESSO!')
print('==============================')


for i in range(1,4):
    login = input('Digite o login: ')
    senha = int(input('Digite a senha: '))
    if login == login_cadastro and senha == senha_cadastro:
        print('****************')
        print('Acesso liberado!')
        print('****************')

        break
    else:
        print('==============================')
        print('Senha ou login errados!')
        print('Tentativa',i,'/3')
        print('==============================')
    if i > 2:
        print('Número de tentativas excedeu!')

       
       
