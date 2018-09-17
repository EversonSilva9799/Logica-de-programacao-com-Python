from cliente import *
from funcionario import *
from time import sleep
from contas import *
from random import randint





    
def menuCliente():
    print('============================')
    print('LOCAL RESTRITO PARA CLIENTES')
    print('============================')
    print('')
    print('1 - Consultar saldo')
    print('2 - Depósito')
    print('3 - Sacar')
    print('4 - Transferência')
    print('5 - Voltar ao menu usuário')
    print('')
    resposta = input('Selecionar: ')
    print('')

    if resposta == '1':
        cpf = input('Informe seu CPF: ')
        conta_escolhida = tipo_conta(cpf)
        saldo_conta = saldo(cpf, conta_escolhida)
        print(saldo_conta)
        print('')
        voltar = input('Enter para voltar ao menu ')
        menuCliente()
        
    elif resposta == '2':
        cpf = input('Informe seu CPF: ')
        conta_escolhida = tipo_conta(cpf)
        print('')
        print('')
        valor = int(input('Informe o valor de depósito: '))
        print('')
        print('')
        depositado = depositar(cpf, conta_escolhida, valor)
        print(depositado)
        print('')
        voltar = input('Enter para voltar ao menu ')
        menuCliente()
        
    elif resposta == '3':
        cpf = input('Informe seu CPF: ')
        conta_escolhida = tipo_conta(cpf)
        valor = int(input('Informe o valor do saque: '))
        print('')
        print('')
        sacado = sacar(cpf, conta_escolhida, valor)
        print('')
        voltar = input('Enter para voltar ao menu ')
        menuCliente()
        
    elif resposta == '4':
        
        print('=========================')
        print('INFORME A CONTA DE ORIGEM')
        print('=========================')
        cpf1 = input('Informe o CPF da conta de origem: ')
        print('')
        conta_origem = tipo_conta(cpf1)
        print('')
        print('==========================')
        print('INFORME A CONTA DE DESTINO')
        print('==========================')
        cpf2 = input('Informe o CPF da conta de destino: ')
        print('')
        conta_destino = tipo_conta(cpf2)
        valor = int(input('Valor da tranferência: '))
        resposta_transferir = transferir(cpf1, cpf2, conta_origem, conta_destino, valor)
        print(resposta_transferir)
        print('')
        voltar = input('Enter para voltar ao menu ')
        menuCliente()
        
    elif resposta == '5':
        print('Finalizado')
        print('')
        print('')
        sleep(2)
        usuarioAtual()
        
    else:
        print('Escolha uma das opções')





def menuFuncionario():

    print('================================')
    print('LOCAL RESTRITO PARA FUNCIONÁRIOS')
    print('================================')
    print('')
    print('1 - Cadastrar novo cliente: ')
    print('2 - Verificar a validação de empréstimo')
    print('3 - Verificar a validação de financiamento')
    print('4 - Consultar cliente')
    print('5 - Voltar ao menu usuário')
    print('')
    resposta = input('Selecionar: ')
    print('')
    print('')
    

    if resposta == '1':
        conta = ''
        for i in range(4):
           numero = randint(0, 50)         
           conta += str(numero)
        dados = []
        cpf = input('CPF: ')
        dados.append(conta)
        dados.append(input('Nome: '))
        dados.append(input('Email: '))
        dados.append(input('Data de nascimento: '))
        dados.append(input('Data de cadastro: '))
        dados.append(float(input('Renda: ')))
        dados.append(int(0.0))
        dados_cli = [cpf, dados]
        print('=======================')
        print('ESCOLHA O TIPO DA CONTA')
        print('=======================')
        print('')
        print('1 - Corrente')
        print('2 - Poupanca')
        criar_conta = input('Selecionar: ')
        if criar_conta == '1':
            cadastro = cadastraCliente(conta_corrente, dados_cli)
            print('===========')
            print(cadastro)
            print('===========')
            print('')
            voltar = input('Enter para voltar ao menu ')
            menuFuncionario()
        elif criar_conta == '2':
            cadastro = cadastraCliente(conta_poupanca, dados_cli)
            print('===================')
            print(cadastro)
            print('===================')
            print('')
            voltar = input('Enter para voltar ao menu ')
            menuFuncionario()
        else:
            print('Escolha um tipo de conta')
            print('')
            voltar = input('Enter para voltar ao menu ')
            menuFuncionario()

    elif resposta == '2':
        cpf = input('Informe seu cpf: ')
        conta_escolhida = tipo_conta(cpf)
        valor = int(input('Informe o valor do empréstimo: '))
        print('')
        print('')
        empresto = verificaEmprestimo(cpf,conta_escolhida, valor)
        print('===========')
        print(empresto)
        print('===========')
        sleep(2)

        seguir_emprestimo = input('Seguir para empréstimo? (sim/não): ')
        print('')
        print('')
        if seguir_emprestimo.lower() == 'sim':
            seguir_emprestimo = True
            if seguir_emprestimo:
               emprestimo = realizarEmprestimo(cpf,conta_escolhida, valor)
               print('=============================================================')
               print(emprestimo)
               print('=============================================================')
               print('')
               voltar = input('Enter para voltar ao menu ')
               menuFuncionario()
               
        elif seguir_emprestimo == 'não':
            print('')
            print('')
            print('Voltando ao menu')
            sleep(1.5)
            menuFuncionario()

    elif resposta == '3':
        cpf = input('Digite seu cpf: ')
        conta_escolhida = tipo_conta(cpf)
        valor = int(input('valor do financiamento pedido: '))
        print('')
        print('')
        resposta_financiamento = verificaFinancimento(cpf,conta_escolhida, valor)
        print('====================')
        print(resposta_financiamento)
        print('====================')
        sleep(2)
        
        seguir_financiamento = input('Seguir para financiamento? (sim/não): ')
        print('')
        print('')
        if seguir_financiamento.lower() == 'sim':
            seguir_financiamento = True
            if seguir_financiamento:
               financiamento = realizarEmprestimo(cpf,conta_escolhida, valor)
               print('===========')
               print(financiamento)
               print('===========')
               print('')
               voltar = input('Enter para voltar ao menu ')
               menuFuncionario()
        elif seguir_financiamento == 'não':
            print('Voltando ao menu')
            sleep(1.5)
            menuFuncionario()

    elif resposta == '4':
        cpf = input('Difite seu cpf: ')
        conta_escolhida = tipo_conta(cpf)
        print('')
        print('')
        dados_do_cliente = consultarUsuario(cpf,conta_escolhida)
        print('')
        print('')
        voltar = input('Enter para voltar ao menu ')
        menuFuncionario()
        
        
    elif resposta == '5':
        print('Operação cancelada')
        print('')
        print('')
        sleep(2)
        usuarioAtual()
    else:
        print('Escolha uma das opções')
        print('')
        print('')
def usuarioAtual():
    print('')
    print('Usuário atual')
    print(20 * '-')
    print('1 - Cliente')
    print('2 - Funcionário')
    print('3 - Finalizar programa')
    print(20 * '-')
    print('')

    usuario = input('Selecionar: ')
    print('')
    print('')

    if usuario == '1':
        menuCliente()
        
    elif usuario == '2':

        print('=============')
        print('TELA DE LOGIN')
        print('=============')
        nome = input('Informe seu nome: ')
        matricula = input('Informe a sua matrícula: ')
        print('')
        print('')
        verificador = funcionarios(matricula, nome)
        if verificador == True:
            menuFuncionario()
        else:
           erro = funcionarios(matricula, nome)
           print(erro)
           usuarioAtual()
    elif usuario == '3':
        print('Programa finalizado')
        
    else:
        print('')
        print('')
        print('Selecione um usuário')
        usuarioAtual()

usuarioAtual()


    
