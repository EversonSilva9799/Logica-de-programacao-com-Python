lista = []
while True:

    #O split recebe valores e os insere numa lista
    nome = input('Digite seu nome e sua idade: ').split(' ')
    lista.append(nome)
    resposta = input('Deseja continuar? Sim/Não ')
    if resposta.lower() == 'não':
        break
    elif resposta.lower() == 'sim':
        continue
    else:
        print('Escolha Sim/Não')
        continue
        
    
for nome, idade in lista:
    print('=======================================')
    print('Nome: {}\nIdade: {}'.format(nome, idade))
    print('=======================================')





