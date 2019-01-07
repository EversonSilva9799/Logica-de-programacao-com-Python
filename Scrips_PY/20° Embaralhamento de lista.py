from random import shuffle
lista = []

while True:
    lista.append(input('Digite um nome: '))
    resp = input('Continuar? S/N')
    if resp.lower() == 'n':
        break

print('')
print('Lista normal:')
print('')
print(lista)
print('')
shuffle(lista) #shuffle embaralha uma lista
print('Lista embaralhada:')
print('')
print(lista)

