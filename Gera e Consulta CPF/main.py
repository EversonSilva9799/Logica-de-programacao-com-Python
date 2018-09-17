from cc_cpf import *

def menu():
    print('')
    print('')
    print('====================')
    print('1 - Gerar CPF manualmente')
    print('2 - Gerar CPF aleatório')
    print('3 - Consultar CPF')
    print('4 - Sair')
    print('====================')
    print('')
    selecao = input('SELECIONAR: ')

    if selecao == '1':
        cpfGerado = CriaCpf()
        print(cpfGerado)
        seguir = input('Enter para voltar ao menu ')
        menu()

    elif selecao == '2':
        resultado = geraCpfRandomico()
        print(resultado)
        print('')
        seguir = input('Enter para voltar ao menu ')
        menu()

        
    elif selecao == '3':
        numeros = list(input('Digite o CPF: '))
        
        resultado = consultaCpf(numeros[:9])

        if numeros == resultado:
            print('CPF válido')
            seguir = input('Enter para voltar ao menu ')
            menu()
        else:
            print('CPF inválido')
            seguir = input('Enter para voltar ao menu ')
            menu()
            del cpf[:]
        
    elif selecao == '4':
        print('Programa finalizado!')
    else:
        print('Selecione uma das opções')
        time.sleep(2)
        menu()
menu()
