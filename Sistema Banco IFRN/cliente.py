from contas import *
    



def tipo_conta(cpf):
    
    if cpf in conta_corrente or cpf in conta_poupanca:
        print('1 - Corrente')
        print('2 - Poupança')
        tipo_conta = input('Conta corrente ou poupança? ')
         
        if tipo_conta == '1':
            conta_escolhida = '1'
            return conta_escolhida
        elif tipo_conta == '2':
            conta_escolhida = '2'
            return conta_escolhida
        
            

 

def saldo(cpf, conta_escolhida):
    
    if conta_escolhida == '1' :
        if cpf not in conta_corrente:
            return('Erro! Conta corrente não encontrada')
        else:
            saldo_corrente = conta_corrente[cpf][6]
            print('Saldo da conta corrente de {}!'.format(conta_corrente[cpf][1]))
            return saldo_corrente

    elif conta_escolhida == '2':
        if cpf not in conta_poupanca:
            return('Erro! Conta poupança não encontrada')
        else:
            saldo_poupanca = conta_poupanca[cpf][6]
            print('Saldo da conta poupança de {}!'.format(conta_poupanca[cpf][1]))
            return saldo_poupanca
    


def sacar(cpf, conta_escolhida, valor):
    
    if conta_escolhida == '1' :
        if cpf not in conta_corrente:
            return('Erro! Conta corrente não encontrada')
        else:
            conta_corrente[cpf][6] -= valor
            print('Saque realizado na conta corrente de {}!'.format(conta_corrente[cpf][1])) 
            return valor  

    elif conta_escolhida == '2':
        if cpf not in conta_poupanca:
            return('Erro! Conta poupança não encontrada')
        else:
            conta_poupanca[cpf][6] -= valor
            print('Saque realizado na conta poupanca de {}!'.format(conta_poupanca[cpf][1])) 
            return valor


def depositar(cpf, conta_escolhida, valor):
    
    if conta_escolhida == '1':
        if cpf not in conta_corrente:
            return('Erro! Conta corrente não encontrada')
        else:
            conta_corrente[cpf][6] += valor 
            return('Depósito realizado na conta corrente de {}!'.format(conta_corrente[cpf][1]))      
    elif conta_escolhida == '2':
        if cpf not in conta_poupanca:
            return('Erro! Conta poupança não encontrada')
        else:
            conta_poupanca[cpf][6] += valor
            return('Depósito realizado na conta poupança de {}!'.format(conta_poupanca[cpf][1]))


def transferir(cpf1, cpf2, conta_origem, conta_destino, valor):
   valor_deposito = sacar(cpf1,conta_origem, valor)
   valor_depositado = depositar(cpf2, conta_destino, valor_deposito)
   return ('Transferência realizada com sucesso')

    

