nome = input('Digite seu nome: ')

print('nome: ',nome)

print('capitalize: ',nome.capitalize()) #Primeira letra maiúscula

print('center:',nome.center(50)) #Centraliza  50 = espaço

print('count:',nome.count('a')) #Conta quanto de alguma coisa existe em nome

print(nome.endswith('va'))  #Se termina com algo que vc detrmina

#print(nome.find('e'))#Encontra algo e diz sua posição

#print(nome.index('e'))#Encontra algo e diz sua posição

print('São caracteres:   ',nome.isalpha()) #verifica se há só caracteres

print('São números:  ',nome.isnumeric()) #Verifica se é número

print('É decimal:  ',nome.isdecimal()) #Verifica se é decimal

print('São dígitos:  ',nome.isdigit()) #Verifica se são dígitos

print('Transformando em letras minúsculas:  ',nome.lower())
print('Verifica se é minúscula: ',nome.islower())

print('Transformando em letras maiúsculas:  ',nome.upper())
print('Verifica se é maiúscula: ',nome.isupper())

print('Transforma a primeira letra de cada palavra em maiúscula:  ',nome.title())
print('Verifica se a primeira letra é minúscula:  ',nome.istitle())

print('É só espaço:  ',nome.isspace()) #Verifica se é só espaços




