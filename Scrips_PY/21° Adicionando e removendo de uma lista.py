#O programa recebe nomes para adicionar a lista e depois pergunta ao usuário se que exluir ou não algum nome


nomes = []
print('Digite SAIR para cancelar a entrada de dados')
while True:
    print('')
    print('=============================')
    nome = input('Digite o nome: ')
    print('=============================')
    if nome == 'sair':
        break
    nomes.append(nome)
    print('')
    
resp = input('Deseja excluir algum nome da lista? Sim/Não: ')
if resp.lower() == 'sim': 
    while True:
        print('')
        excluir = input('Excluir qual nome da lista: ')
        print('')
        if excluir in nomes:
            exclusao = nomes.index(excluir)
            del nomes[exclusao]
            print('{} exluído da lista!'.format(excluir))
        else:
            print('')
            print('Nome não encontrado!')
            print('')
            resp2 = input('Deseja continuar a exlusão? Sim/Não: ')
            if resp2.lower() == 'sim':
                continue
            else:
                print('==============')
                print('\n'.join(nomes))
                print('==============')
                break
        resp = input('continuar exlusão? Sim/Não: ')
        print('')
        if resp.lower() == 'não':
            print('==============')
            print('\n'.join(nomes))
            print('==============')
            break
        else:
          continue       
else:
    print('==============')
    print('\n'.join(nomes))
    print('==============')
