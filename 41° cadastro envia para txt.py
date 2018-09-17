nomes = []
idade = []
'''
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
banco_dados = open('cadastro.txt','w')
banco_dados.write(nome)
banco_dados.write('\n')
banco_dados.write(str(idade))
banco_dados.close()
'''
while True:
    
    banco_dados = open('cadastro.txt','r')
    cadastros = banco_dados.read()
    banco_dados.close()
    
    
    print('Digite sair para cancelar a entrada de dados!')
    nome = input('Digite seu nome: ')
    banco_dados = open('cadastro.txt','a')
    
    if nome in cadastros:
        print('Este nome já existe no banco de dados')
        continue
    elif nome.lower() == 'sair':
        break
    else:
        cadastros = banco_dados.write(nome)
        cadastros = banco_dados.write('\n')
        banco_dados.close()
    
    


'''
banco_dados.write('\n')
banco_dados.write(str(idade))
banco_dados.close()
'''
