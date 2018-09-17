from contas import *
from cliente import *
funcionarios_banco = {'123':['João','José'], '456':['Ana','Maria']}

def funcionarios(matricula, nome):
    if matricula in funcionarios_banco:
        if funcionarios_banco[matricula][0] == nome:
            return True
    return('Verifique as informações e tente novamente')
    

def cadastraCliente(conta,dados_cli):
    conta[dados_cli[0]] = dados_cli[1]
    return 'Cadastrado com sucesso'





def verificaEmprestimo(cpf,conta_escolhida, valor):
    if conta_escolhida == '1':
        renda = conta_corrente[cpf][5]
        if valor <= 0.3*renda:
            return True
        return False
    elif conta_escolhida == '2':
        renda = conta_poupanca[cpf][5]
        if valor <= 0.3*renda:
            return True
        return False

    


def verificaFinancimento(cpf,conta_escolhida, valor):
    if conta_escolhida == '1':
        renda = conta_corrente[cpf][5]
        if valor <= 10 * renda:
            return True
        return False
    elif conta_escolhida == '2':
        renda = conta_poupanca[cpf][5]
        if valor <= 10 * renda:
            return True
        return False
        

def realizarEmprestimo(cpf,conta_escolhida, valor):
    if conta_escolhida == '1':
        conta_corrente[cpf][5] += valor 
        return('Empréstimo depositado na conta corrente de {} conta {}!'.format(conta_corrente[cpf][1], conta_corrente[cpf][0]))
    elif conta_escolhida == '2':
        conta_poupanca[cpf][5] += valor
        return('Empréstimo depositado na conta poupanca de {} conta {}!'.format(conta_poupanca[cpf][1], conta_poupanca[cpf][0]))

def consultarUsuario(cpf,conta_escolhida):
    dados = []
    if conta_escolhida == '1':
        print('===============================================')
        print('CPF                -- ', cpf)
        for i in range(7):
            dados.append(conta_corrente[cpf][i])
        print('Conta              -- ',dados[0])
        print('Nome               -- ',dados[1])   
        print('Email              -- ',dados[2])
        print('Data de nascimento -- ',dados[3])
        print('Data de cadastro   -- ',dados[4])
        print('Renda              -- ',dados[5])
        print('Saldo              -- ',dados[6])
        print('===============================================')
    elif conta_escolhida == '2':
        print('===============================================')
        print('CPF                -- ', cpf)
        for i in range(7):
            dados.append(conta_poupanca[cpf][i])
        print('Conta              -- ',dados[0])
        print('Nome               -- ',dados[1])   
        print('Email              -- ',dados[2])
        print('Data de nascimento -- ',dados[3])
        print('Data de cadastro   -- ',dados[4])
        print('Renda              -- ',dados[5])
        print('Saldo              -- ',dados[6])
        print('===============================================')
        
            
    
        

    
    
    

