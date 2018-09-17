
print('Formando uma matriz')
print('')
lin = int(input('Linhas: '))
col = int(input('Colunas: '))

matriz = []
for i in range(lin):
  lista = []
  for j in range(col):
    num = int(input('Número: '))
    lista.append(num)
  matriz.append(lista)

for i in range(lin):
  for j in range(col):
    print(matriz[i][j])
