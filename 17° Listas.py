#Isto é uma lista
lista = [1,2,3]
print(lista)
print('')

#adiciona elemento no final da lista
lista.append('Lurdinha')
print(lista)
print('')

#Adiciona elemento em qualquer posição da lista
lista.insert(0,'Alcides') #Usando -1 o elemento é inserindo na penúltima posição
print(lista)
print('')

#Posição do elemento pelo nome
posicao = lista.index('Alcides')
print(lista[posicao])
print('')

#Elementos de uma lista são acessados por índice
print(lista[0])
print(lista[4])
print('')

#Remove o último elemento da lista
lista.pop()
print(lista)
print('')

#Remove Algum elemento da lista
del lista[1]  #-1 Remove o último elemento da lista
print(lista)  # [2:6] Significa do 2 ao 6 elemento
print('')

#Remove algum elemento pelo seu nome(Remove primeiro elemento)
lista.remove('Alcides')
print(lista)
print('')
