lista = ['A','B','C']
print(lista)
print('')
lista1 = lista
print(lista1)
#Lista1 não é independente
lista[0] = 'Lurdinha'
print('')
print(lista)
print('')
print(lista1)

#Cópia independente
lista2 = lista[:] #Lista2 é uma cópia independente(outro endereço de memória)
print('')
lista.append('Alcides')
print(lista)
print('')
print(lista1)
print('')
print(lista2)
