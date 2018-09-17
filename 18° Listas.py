#Conta quantas vezes um elemento aparece na lista
cursos = ['Java','Python','Python','PHP','CSS','Java','Java']
print(cursos.count('Java'))
print('')

#Inverte os elementos da lista
cursos.reverse()
print(cursos)
print('')

#Ordena uma lista
cursos.sort()
print(cursos)
print('')

#Enumera um elemento da lista com seu índice
for i, curso in enumerate(cursos):
    print(i,curso)


