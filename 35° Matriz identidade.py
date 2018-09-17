
# Descobrir se a matriz é identidade
A = []
lin = int(input("Digite o numero de linhas da matriz"))
col = int(input("Digite o numero de colunas da matriz"))
if lin != col :
  print ("A matriz não é identidade")
else:
  for i in range (lin):
    E =[]
    for j in range (col):
      a = int(input("Digite um elemento : "))
      E.append(a)
    A.append(E)
  identidade = True
  for i in range (lin):
    for j in range (col):
      if i == j and A[i][j] !=1  or  i != j and A[i][j]  != 0 :
        identidade = False
        break
  if identidade == True:
       print('Matriz I.')
  else:
       print('Matriz não I')
