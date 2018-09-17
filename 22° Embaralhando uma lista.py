from random import shuffle
lista = []
for i in range(1,5):
    nome = input('Digite o {}° nome: '.format(i))
    lista.append(nome)

shuffle(lista)

print('A ordem de apresentação é:')
print('\n'.join(lista))
