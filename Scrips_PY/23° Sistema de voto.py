
import time
nomes_candidatos = []
total_votos = []
caracter_especial = ['?', '*', '$','@','%','&','#','!','-','_','(',')','=','/',':','+',',','"']
soma_votos = 0

print('')
print('')
while True:
    print('DIGITE "SAIR" PARA CANCELAR A ENTRADA DE DADOS')
    nome = input('Digite o nome do candidato: ')
    if nome.lower() == 'sair':
        break
    if nome.lower() == 'sair' and len(nomes_candidatos) == 0:
        print('Nenhum candidato cadastrado!')
        break
    if nome.capitalize() in nomes_candidatos:
        print('==================')
        print('Nome já existente!')
        print('==================')
        continue
    if nome.isdigit():
        print('======================')
        print('Digite um nome válido!')
        print('======================')
        continue
    if nome.isspace():
        print('===============')
        print('Digite um nome!')
        print('===============')
        continue
    if len(nome) == 0:
        print('===============')
        print('Digite um nome!')
        print('===============')
        continue
    if nome in caracter_especial:
       print("Ops")
       continue
        
    nomes_candidatos.append(nome.capitalize())
nomes_candidatos.sort()

    
    

for i in nomes_candidatos:
    print('')
    print('CANDIDATO')
    print('===============')
    print('Nome:',i)
    print('===============')

print('')

print('')
while True:
    print('DIGITE "SAIR" PARA CANCELAR A ENTRADA DE DADOS')
    voto = input('Digite o nome do candidato para votar: ')
    
    
    if voto.lower() == 'sair':
        break
    if voto.lower() == 'sair' and len(total_votos) == 0:
           print('Níngém votou')
           break

    if voto.capitalize() in nomes_candidatos:
        total_votos.append(voto.capitalize())     
    else:
        print('=====================')
        print('Nome não encontrado: ')
        print('=====================')
        continue
    
    soma_votos = soma_votos+1
print('')
print('======================')
print('Pessoas que votaram:',soma_votos)
print('======================')

for i in nomes_candidatos:
    total = total_votos.count(i)
    print('')
    time.sleep(1.2)   
    print('=======================')

    print('{}: {} voto(s)'.format(i, total))

    
    
            
    
    
    

