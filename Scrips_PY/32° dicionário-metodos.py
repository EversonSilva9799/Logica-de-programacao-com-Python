agenda = {}

for i in range(4):

    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone')
    agenda[nome] = telefone
print('')
print('')
print('======================')    
print('Chaves dodicionário')
print('======================') 
# Acessando as chaves do dicionário
for chave in agenda.keys():
    print(chave)
    print('')
    print('')
print('======================')
print('')

#Acessando os valores do dicionário
print('======================') 
print('Valores dodicionário')
print('======================') 
for valor in agenda.values():
    print(valor)
    print('')
    print('')
print('======================') 
print('Acessando ambos os items')
print('======================')
print('')
#Acessando ambos
for  chave, valor in agenda.items():
    print('Nome {} | Telefone {}'.format(chave, valor))
    print('')
    print('')
print('===========================') 
print('Acessando de forma ordenada')
print('===========================') 
#Acessando as chaves do dicionário de forma ordenada
for chave in sorted(agenda.keys()):
    print('Nome {} | Telefone {}'.format(chave, agenda[chave]))
